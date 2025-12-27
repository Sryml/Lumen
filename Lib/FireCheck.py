
import Bladex
import InitDataField
import GameStateAux
import ObjStore

#####################################################################################
#																					#
#	FireCheck.py																	#
#																					#
#	Las culpas a --> Yuio															#
#																					#
#####################################################################################



######## handler por defecto 

def debugPSCEvent(name,hit_entity,x,y,z,vx,vy,vz,wcx,wcy,wcz,wdx,wdy,wdz):
	print("unhandled hit_entity:"+hit_entity+" by:"+name)
	if hit_entity=="Player1":
		print "player hit!!!!!!!!!!!!!!!!!!!!!!!!!!!"



######## timer de checkeo

def checkPSysTimer(partSys,time):
	#print("checkPSysTimer(partSys,time)");
	partSysEnt			= Bladex.GetEntity(partSys)
	partSysCheckerEnt	= partSysEnt.Data.psCheckerData	

	if (time > partSysCheckerEnt.stopTime) :
		#print("stopTimer");
		partSysCheckerEnt.stopCheck()
		return 

	i=0
	n=partSysCheckerEnt.precission
	for i in range(n) :
		hitParticle			= partSysEnt.GetParticleEntity()
		hitParticle.HitFunc = partSysCheckerEnt.onHitFunc
		hitParticle.ObjCTest= 1

Bladex.CreateTimer("partSysCheck", 0.1 )



######### clase checkeadora de colisiones (PSysChecker)

class PSysChecker:

	ObjId=""
	onHitFunc = debugPSCEvent
	precission = 1
	pSys=None


	def __init__(self):

		self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
		ObjStore.ObjectsStore[self.ObjId]=self
		self.pSys=None

	def startCheck(self,partSys,time):		
		#print("PSysChecker.startCheck(time)")
		t = Bladex.GetTime()
		self.startTime	= t
		self.stopTime	= t+ time
		self.pSys		= partSys
		InitDataField.Initialise(self.pSys)
		self.pSys.Data.psCheckerData=self
		self.pSys.TimerFunc=checkPSysTimer
		self.pSys.SubscribeToList("partSysCheck")

	def stopCheck(self):
		#print("PSysChecker.stopCheck()")
		if self.pSys:
			self.pSys.TimerFunc=""
			self.pSys.RemoveFromList("partSysCheck")

	def persistent_id(self):
		return self.ObjId

	def __getstate__(self):
		# Tiene que devolver cómo poder guardar el estado de la clase
		return (1,
				self.ObjId,
				GameStateAux.SaveFunctionAux(self.onHitFunc),
				self.precission,
				GameStateAux.SaveEntityAux(self.pSys),
				GameStateAux.SaveNewMembers(self)
				)

	def __setstate__(self,parm):
		# Toma como parámetro lo que devuelve __getstate__() y debe recrear la clase
		if parm[0]==1:
			self.ObjId=parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self
			GameStateAux.LoadFunctionAux(parm[2],self,"onHitFunc")
			self.precission=parm[3]
			self.pSys=GameStateAux.LoadEntityAux(parm[4])
			GameStateAux.LoadNewMembers(self,parm[5])
		else:
			print "PSysChecker.__setstate__() -> Version mismatch"
			# Valores de creación por si valen para algo.
			self.onHitFunc	= debugPSCEvent
			self.precission = 1
			self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
			self.pSys=None



######### creacion de la clase PSysChecker

def createPSysChecker():
	#print("createPSysChecker(*)")
	psChecker=PSysChecker()
	return psChecker

