
# EXAMPLE OF USE
# make an ice aura (just using gradient 2) to last 5 minutes....
#aura= Auras.MakeAura ("Player1",5.0*60.0,(25,1.0,1.0,1,0,0), (),(),(2,  0.8,0.8,1.0, 1.0, 0.6  , 0.0,0.0,1.0, 0.0, 1.0))
# interpolate to a fire aura over 1 second
#aura.Data.AddEvent(Bladex.GetTime()+1.0, (25,1.0,1.0,1,0,0), (),(),(2,  1.0,0.7,0.0, 1.0, 0.5  , 1.0,0.0,0.0, 0.0, 1.0))
# interpolate back to ice aura over 0.1 seconds
#aura.Data.AddEvent(Bladex.GetTime()+0.1, (25,1.0,1.0,1,0,0), (),(),(2,  0.8,0.8,1.0, 1.0, 0.6  , 0.0,0.0,1.0, 0.0, 1.0))

# See the special damage functions in the file Damage.py for more examples...


import Bladex
import ObjStore

Bladex.CreateTimer('Timer20',1.0/20.0)

class AnimateableAura:
	def __init__(self, aura, time2live, AuraParams, AuraGradient0=(),AuraGradient1=(),AuraGradient2=(),Active=1,XtraParam=()):
		self.ObjId=ObjStore.GetNewId()
		ObjStore.ObjectsStore[self.ObjId]=self

		self.EventList=[]
		self.Name= aura.Name
		self.TimerName= 'Timer20'
		self.TimerFrequency= 1.0/20.0

		# set initial params
		self.AuraParams= AuraParams
		apply(aura.SetAuraParams, self.AuraParams)

		# set initial gradient 0
		if AuraGradient0: self.AuraGradient0= AuraGradient0			
		else: self.AuraGradient0= (0,  0.0,0.0,0.0, 0.0, 0.0  , 0.0,0.0,0.0, 0.0, 0.0)			
		apply(aura.SetAuraGradient, self.AuraGradient0)		

		# set initial gradient 1
		if AuraGradient1: self.AuraGradient1= AuraGradient1			
		else: self.AuraGradient1= (1,  0.0,0.0,0.0, 0.0, 0.0  , 0.0,0.0,0.0, 0.0, 0.0)			
		apply(aura.SetAuraGradient, self.AuraGradient1)

		# set initial gradient 2
		if AuraGradient2: self.AuraGradient2= AuraGradient2
		else: self.AuraGradient2= (2,  0.0,0.0,0.0, 0.0, 0.0  , 0.0,0.0,0.0, 0.0, 0.0)
		apply(aura.SetAuraGradient, self.AuraGradient2)

		# set deathtime, & subscribe to timer...
		if time2live>0.0: self.DeathTime= Bladex.GetTime()+time2live
		else: self.DeathTime= -1.0
		aura.TimerFunc= self.TimerFunc
		aura.SubscribeToList(self.TimerName)

		# set active by default
		self.Active= Active
		aura.SetAuraActive(self.Active)

		# Establece el valor inicial del parametro extra
		self.OldXtraParam=self.XtraParam=XtraParam
		if XtraParam:
			exec_string = XtraParam[0] + '=' + str(XtraParam[1])
			exec(exec_string)

	def persistent_id(self):
		return self.ObjId


	def __getstate__(self):
		# Tiene que devolver como poder guardar el estado de la clase

		return (1,
				self.ObjId,
				self.EventList,
				self.Name,
				self.TimerName,
				self.TimerFrequency,
				self.AuraParams,
				self.AuraGradient0,
				self.AuraGradient1,
				self.AuraGradient2,
				self.DeathTime,
				self.Active,
				self.OldXtraParam,
				self.XtraParam
				)

	def __setstate__(self,parm):
		# Toma como par⮥tro lo que devuelve __getstate__() y debe recrear la clase

		if parm[0]==1:
			#self.ObjId=parm[1] En GameStateAux.PersistentObject()
			self.ObjId=parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self
			self.EventList=parm[2]
			self.Name=parm[3]
			self.TimerName=parm[4]
			self.TimerFrequency=parm[5]
			self.AuraParams=parm[6]
			self.AuraGradient0=parm[7]
			self.AuraGradient1=parm[8]
			self.AuraGradient2=parm[9]
			self.DeathTime=parm[10]
			self.Active=parm[11]
			self.OldXtraParam=parm[12]
			self.XtraParam=parm[13]
		else:
			print "AnimateableAura.__setstate__() -> Version mismatch"
			self.ObjId=ObjStore.GetNewId()
			ObjStore.ObjectsStore[self.ObjId]=self
			self.EventList=[]
			self.Name= "Error loading"
			self.TimerName= 'Timer20'
			self.TimerFrequency= 1.0/20.0


	# comparison function for time-based sort
	def FirstTime(self, e1, e2):		
		if e1[0]<e2[0]: return -1 #CHOOSE_FIRST			
		elif e2[0]>e1[0]: return 1  #CHOOSE_SECOND			
		else: return 0  #CHOOSE_EITHER				

	def AddEvent (self, time, AuraParams, AuraGradient0=(),AuraGradient1=(),AuraGradient2=(),Active=1,XtraParam=()):
		self.EventList.append([time, AuraParams, AuraGradient0, AuraGradient1, AuraGradient2,Active,XtraParam])
		# Sort the events into first event first order...
		self.EventList.sort(self.FirstTime)
		
	def TimerFunc(self, obj_name, time):		
		if self.DeathTime>=0.0 and time>self.DeathTime:
			self.EventList=[]
			self.Active=0
			if self.OldXtraParam:
				exec_string = self.OldXtraParam[0] + '=' + str(self.OldXtraParam[1])
				exec(exec_string)
			aura= Bladex.GetEntity(self.Name)
			aura.SetAuraActive(0)			
			aura.RemoveFromList(self.TimerName)
			aura.SubscribeToList('Pin') # this should remove this class instance too			
			return
		elif len(self.EventList)<1:
			# No events to process, return
			return
		else:
			# Process using the first event
			NextTime, AuraParams, AuraGradient0, AuraGradient1, AuraGradient2, Active, XtraParam= self.EventList[0]
			if time>=NextTime:
				# We have reached an event				
				aura= Bladex.GetEntity(self.Name)
				
				# set params
				self.AuraParams= AuraParams
				apply(aura.SetAuraParams, self.AuraParams)
				
				# set gradient0
				if AuraGradient0:
					self.AuraGradient0= AuraGradient0
					apply(aura.SetAuraGradient, self.AuraGradient0)
				
				# set gradient1
				if AuraGradient1:
					self.AuraGradient1= AuraGradient1
					apply(aura.SetAuraGradient, self.AuraGradient1)
				
				# set gradient2
				if AuraGradient2:
					self.AuraGradient2= AuraGradient2
					apply(aura.SetAuraGradient, self.AuraGradient2)
								
				if Active!=self.Active:
					self.active= Active
					aura.SetAuraActive(self.Active)

				if XtraParam:
					self.XtraParam=XtraParam
					exec_string = XtraParam[0] + '=' + str(XtraParam[1])
					exec(exec_string)

				# Comprueba si va a haber cambios en el intervalo actual, para no estar llamando al timer innecesariamente

				nNextTime, nAuraParams, nAuraGradient0, nAuraGradient1, nAuraGradient2, nActive, nXtraParam= self.EventList[1]

				if not ((AuraParams<>nAuraParams) or (AuraGradient2<>nAuraGradient2) or (XtraParam<>nXtraParam) or (AuraGradient0<>nAuraGradient0) or (AuraGradient1<>nAuraGradient1)):
					aura.RemoveFromList(self.TimerName)
					Bladex.AddScheduledFunc(nNextTime, aura.SubscribeToList, (self.TimerName,))

				# remove the event, it is dealt with
				del self.EventList[0]
			else:
				# interpolate towards the next event								

				a= self.TimerFrequency/(self.TimerFrequency+NextTime-time)
				aura= Bladex.GetEntity(self.Name)

				# interpolate params
				fSize, fAlpha,fIntensity, iFrontFaceCulling, iBackFaceCulling, iAdditive= self.AuraParams
				fSize= fSize+(AuraParams[0]-fSize)*a
				fAlpha= fAlpha+(AuraParams[1]-fAlpha)*a
				fIntensity= fIntensity+(AuraParams[2]-fIntensity)*a
				self.AuraParams= fSize, fAlpha,fIntensity, iFrontFaceCulling, iBackFaceCulling, iAdditive
				apply(aura.SetAuraParams, self.AuraParams)
				
				# interpolate gradient0
				if AuraGradient0:
					iStage, fR0, fG0, fB0, fA0, fStart, fR1, fG1, fB1, fA1, fEnd= self.AuraGradient0
					fR0= fR0+(AuraGradient0[1]-fR0)*a
					fG0= fG0+(AuraGradient0[2]-fG0)*a
					fB0= fB0+(AuraGradient0[3]-fB0)*a
					fA0= fA0+(AuraGradient0[4]-fA0)*a
					fStart= fStart+(AuraGradient0[5]-fStart)*a
					fR1= fR1+(AuraGradient0[6]-fR1)*a
					fG1= fG1+(AuraGradient0[7]-fG1)*a
					fB1= fB1+(AuraGradient0[8]-fB1)*a
					fA1= fA1+(AuraGradient0[9]-fA1)*a
					fEnd= fEnd+(AuraGradient0[10]-fEnd)*a
					self.AuraGradient0= iStage, fR0, fG0, fB0, fA0, fStart, fR1, fG1, fB1, fA1, fEnd
					apply(aura.SetAuraGradient, self.AuraGradient0)
				
				# interpolate gradient1
				if AuraGradient1:
					iStage, fR0, fG0, fB0, fA0, fStart, fR1, fG1, fB1, fA1, fEnd= self.AuraGradient1
					fR0= fR0+(AuraGradient1[1]-fR0)*a
					fG0= fG0+(AuraGradient1[2]-fG0)*a
					fB0= fB0+(AuraGradient1[3]-fB0)*a
					fA0= fA0+(AuraGradient1[4]-fA0)*a
					fStart= fStart+(AuraGradient1[5]-fStart)*a
					fR1= fR1+(AuraGradient1[6]-fR1)*a
					fG1= fG1+(AuraGradient1[7]-fG1)*a
					fB1= fB1+(AuraGradient1[8]-fB1)*a
					fA1= fA1+(AuraGradient1[9]-fA1)*a
					fEnd= fEnd+(AuraGradient1[10]-fEnd)*a
					self.AuraGradient1= iStage, fR0, fG0, fB0, fA0, fStart, fR1, fG1, fB1, fA1, fEnd
					apply(aura.SetAuraGradient, self.AuraGradient1)
				
				# interpolate gradient2
				if AuraGradient2:
					iStage, fR0, fG0, fB0, fA0, fStart, fR1, fG1, fB1, fA1, fEnd= self.AuraGradient2
					fR0= fR0+(AuraGradient2[1]-fR0)*a
					fG0= fG0+(AuraGradient2[2]-fG0)*a
					fB0= fB0+(AuraGradient2[3]-fB0)*a
					fA0= fA0+(AuraGradient2[4]-fA0)*a
					fStart= fStart+(AuraGradient2[5]-fStart)*a
					fR1= fR1+(AuraGradient2[6]-fR1)*a
					fG1= fG1+(AuraGradient2[7]-fG1)*a
					fB1= fB1+(AuraGradient2[8]-fB1)*a
					fA1= fA1+(AuraGradient2[9]-fA1)*a
					fEnd= fEnd+(AuraGradient2[10]-fEnd)*a
					self.AuraGradient2= iStage, fR0, fG0, fB0, fA0, fStart, fR1, fG1, fB1, fA1, fEnd
					apply(aura.SetAuraGradient, self.AuraGradient2)

				if XtraParam:
					Param, Value=self.XtraParam
					exec_string = Param + '=' + Param + '+(' + str(XtraParam[1]) + '-' + Param + ')*' + str(a)
					exec(exec_string)
					exec_string2 = 'Value=' + Param
					exec(exec_string2)
					self.XtraParam=Param, Value



def MakeAura (EntityName,time2live,StartAuraParams,StartAuraGradient0=(),StartAuraGradient1=(),StartAuraGradient2=(),StartActive=1,XtraParam=()):
	# EntityName is the entity to link to
	# give time2live as -1 to last forever
	me= Bladex.GetEntity(EntityName)
	pos= me.Position	
	aura= Bladex.CreateEntity(EntityName+"_Aura","Entity Aura",pos[0],pos[1],pos[2])	
	me.Link(aura)
	aura.Data= AnimateableAura(aura,time2live,StartAuraParams, StartAuraGradient0,StartAuraGradient1,StartAuraGradient2,StartActive,XtraParam)
	return aura
