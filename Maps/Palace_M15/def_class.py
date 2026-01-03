import Bladex
import B3DLib
import math
import ObjStore

ANGLE_VARIATION = 3.14 /2000.0

class LinkObj:
	def __init__(self,obj,sld,y):		
		self.obj = obj
		self.sld = sld
		self.y = y
		self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
		ObjStore.ObjectsStore[self.ObjId]=self

	def ObjetoSigueSliding(self,entity,time):		
		X = self.obj.Position[0]
		Z = self.obj.Position[2]
		D = self.sld.Displacement
		Y = self.y - D

		self.obj.Position = X,Y,Z
		if self.FollowTarget:
			cam=Bladex.GetEntity("Camera")
			cam.TPos=X,Y,Z

	def persistent_id(self):
		return self.ObjId

	def __getstate__(self):
		return (1,
				self.ObjId,
				self.obj,
				self.sld,
				self.y,
				)

	def __setstate__(self,parm):
		if parm[0]==1:
			self.ObjId=parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self
			self.obj   = parm[2]
			self.sld   = parm[3]
			self.y     = parm[4]
		else:
			print "FATAL ERROR : Version mismatch in LinkObj"
			self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
			ObjStore.ObjectsStore[self.ObjId]=self
			self.obj   = None
			self.sld   = None
			self.y     = None

class RoundCamera:
	def __init__(self,initpos,tarpos,dist):
		cam=Bladex.GetEntity("Camera")		
		cam.TimerFunc=self.GiraCamara
		cam.SType=0
		cam.TType=0

		self.initpos = initpos
		self.dist = dist
	
		vcam=initpos[0]-tarpos[0], initpos[1]-tarpos[1], initpos[2]-tarpos[2]

		self.vcamnorm=B3DLib.Normalize(vcam)
		
		cam.TPos= tarpos
		
		self.init_tpos=cam.TPos
		self.paso_n=0

		cam.SubscribeToList("Timer60")

		self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
		ObjStore.ObjectsStore[self.ObjId]=self

	def GiraCamara(self,entity, time):
		cam=Bladex.GetEntity("Camera")	
		self.paso_n=self.paso_n+1
	
		vcamrot=self.vcamnorm[0]*math.cos(self.paso_n*ANGLE_VARIATION)-self.vcamnorm[2]*math.sin(self.paso_n*ANGLE_VARIATION), 0.0, self.vcamnorm[0]*math.sin(self.paso_n*ANGLE_VARIATION)+self.vcamnorm[2]*math.cos(self.paso_n*ANGLE_VARIATION)
		tpos=vcamrot[0]*self.dist, 0.0, vcamrot[2]*self.dist

		cam.Position=self.init_tpos[0]+tpos[0], self.initpos[1], self.init_tpos[2]+tpos[2]

	def persistent_id(self):
		return self.ObjId

	def __getstate__(self):
		return (1,
				self.ObjId,
				self.initpos,
				self.dist,
				self.vcamnorm,
				self.init_tpos,
				self.paso_n,
				)

	def __setstate__(self,parm):
		if parm[0]==1:
			self.ObjId=parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self
			self.initpos   = parm[2]
			self.dist      = parm[3]
			self.vcamnorm  = parm[4]
			self.init_tpos = parm[5]
			self.paso_n    = parm[6]
			
		else:
			print "FATAL ERROR : Version mismatch in LinkObj"
			self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
			ObjStore.ObjectsStore[self.ObjId]=self
			self.initpos   = None
			self.dist      = None
			self.vcamnorm  = None
			self.init_tpos = None
			self.paso_n    = None
