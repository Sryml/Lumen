import Bladex
import InitDataField
import AuxFuncs
import GameStateAux
import ObjStore
import Scorer

CLOSED=0
OPENED=1
AC=2
UNIF=3
AC_UNIF_DEC=4
UNIF_DEC=5
AC_UNIF=6
AC_DEC=7
DEC=8


Bladex.CreateTimer("DoorTimer",0.1)


def DisplaceSound(sld_name, time):

	sld_area=Bladex.GetEntity(sld_name)
	door=sld_area.Data.doordata
	door.currdispl=sld_area.Displacement
	displ_var=door.prevdispl-door.currdispl
	v=door.surface[0]*displ_var, door.surface[1]*displ_var, door.surface[2]*displ_var
	door.soundpos=door.soundpos[0]-v[0], door.soundpos[1]-v[1], door.soundpos[2]-v[2]
	door.prevdispl=door.currdispl
	if (door.WhileOpenSound):
		door.WhileOpenSound.Position=door.soundpos
	if (door.WhileCloseSound):
		door.WhileCloseSound.Position=door.soundpos


def EndOpenFunc(sld_name):

	sld_area=Bladex.GetEntity(sld_name)
	sld_area.RemoveFromList("DoorTimer")
	door=sld_area.Data.doordata

	door.currdispl=sld_area.Displacement
	displ_var=door.prevdispl-door.currdispl
	v=door.surface[0]*displ_var, door.surface[1]*displ_var, door.surface[2]*displ_var
	door.soundpos=door.soundpos[0]-v[0], door.soundpos[1]-v[1], door.soundpos[2]-v[2]
	door.prevdispl=door.currdispl
	if (door.WhileOpenSound):
		door.WhileOpenSound.StopSound()
	if (door.EndOpenSound):
		door.EndOpenSound.Position=door.soundpos
		door.EndOpenSound.PlaySound(0)
	door.status=OPENED
	if (door.OnEndOpenFunc):
		apply(door.OnEndOpenFunc, door.OnEndOpenArgs)


def EndCloseFunc(sld_name):

	sld_area=Bladex.GetEntity(sld_name)
	sld_area.RemoveFromList("DoorTimer")
	door=sld_area.Data.doordata

	door.currdispl=sld_area.Displacement
	displ_var=door.prevdispl-door.currdispl
	v=door.surface[0]*displ_var, door.surface[1]*displ_var, door.surface[2]*displ_var
	door.soundpos=door.soundpos[0]-v[0], door.soundpos[1]-v[1], door.soundpos[2]-v[2]
	door.prevdispl=door.currdispl

	if (door.WhileCloseSound):
		door.WhileCloseSound.StopSound()
	if (door.EndCloseSound):
		door.EndCloseSound.Position=door.soundpos
		door.EndCloseSound.PlaySound(0)
	door.status=CLOSED

	if (door.OnEndCloseFunc):
		apply(door.OnEndCloseFunc, door.OnEndCloseArgs)



def EndOpen(sld_name):

	sld_area=Bladex.GetEntity(sld_name)
	door=sld_area.Data.doordata


	dec=((door.o_end_vel**2-door.o_med_vel**2)/(2*door.o_end_displ))
	if (door.o_med_vel<0):
		dec=-dec
	sld_area.SlideTo(door.closed_displ-door.o_init_displ-door.o_med_displ-door.o_end_displ, door.o_med_vel, dec)
	sld_area.OnStopFunc=EndOpenFunc


def MedOpen(sld_name):

	sld_area=Bladex.GetEntity(sld_name)
	door=sld_area.Data.doordata
	sld_area.SlideTo(door.closed_displ-door.o_init_displ-door.o_med_displ, door.o_med_vel, 0)
	if (door.opentype==AC_UNIF_DEC):
		sld_area.OnStopFunc=EndOpen
	else:
		sld_area.OnStopFunc=EndOpenFunc


def EndClose(sld_name):

	sld_area=Bladex.GetEntity(sld_name)
	door=sld_area.Data.doordata


	dec=((door.c_end_vel**2-door.c_med_vel**2)/(2*door.c_end_displ))
	if (door.c_med_vel<0):
		dec=-dec
	sld_area.SlideTo(door.opened_displ+door.c_init_displ+door.c_med_displ+door.c_end_displ, door.c_med_vel, dec)
	sld_area.OnStopFunc=EndCloseFunc


def MedClose(sld_name):

	sld_area=Bladex.GetEntity(sld_name)
	door=sld_area.Data.doordata
	sld_area.SlideTo(door.opened_displ+door.c_init_displ+door.c_med_displ, door.c_med_vel, 0)
	if (door.closetype==AC_UNIF_DEC):
		sld_area.OnStopFunc=EndClose
	else:
		sld_area.OnStopFunc=EndCloseFunc



##class Door(GameStateAux.PersistentObject):
class Door:


	Name= "Unnamed class Door"
	opentype=UNIF
	o_init_vel=0
	o_med_vel=0
	o_end_vel=0
	o_init_displ=0
	o_med_displ=0
	o_end_displ=0

	closetype=UNIF
	c_init_vel=0
	c_med_vel=0
	c_end_vel=0
	c_init_displ=0
	c_med_displ=0
	c_end_displ=0

	OnEndOpenFunc=""
	OnEndCloseFunc=""

	OnEndOpenArgs=()
	OnEndCloseArgs=()

	InitOpenSound=""
	WhileOpenSound=""
	EndOpenSound=""

	InitCloseSound=""
	WhileCloseSound=""
	EndCloseSound=""

	surface=(0,1,0)
	closed_displ=0
	opened_displ=0
	currdispl=0
	prevdispl=0
	soundpos=(0,0,0)
	Squezze=1
	status=0



	def __init__(self, Name):
		self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
##		GameStateAux.PersistentObject.__init__(self)
		self.Name= Name

		ObjStore.ObjectsStore[self.ObjId]=self

	def sld_area(self):
		return Bladex.GetEntity(self.Name)


	def OpenDoor(self):
		if (self.status==OPENED):
			return

		sld_area= Bladex.GetEntity(self.Name)
		self.prevdispl=sld_area.Displacement

		if self.Squezze:
			sld_area= Bladex.GetEntity(self.Name)
			sld_area.HitFunc = None

		if (self.InitOpenSound):
			self.InitOpenSound.Position=self.soundpos
			self.InitOpenSound.PlaySound(0)

		if (self.WhileOpenSound):
			self.WhileOpenSound.Position=self.soundpos
			self.WhileOpenSound.PlaySound(-1)

		sld_area.TimerFunc=DisplaceSound
		sld_area.SubscribeToList("DoorTimer")

		if (self.opentype==AC or self.opentype==AC_UNIF_DEC or self.opentype==AC_UNIF or self.opentype==AC_DEC):
			ac=((self.o_med_vel**2-self.o_init_vel**2)/(2*self.o_init_displ))
			if (self.o_med_vel<0):
				ac=-ac

			sld_area.SlideTo(self.closed_displ-self.o_init_displ, self.o_init_vel, ac)
			if (self.opentype==AC_UNIF_DEC or self.opentype==AC_UNIF):
				sld_area.OnStopFunc=MedOpen
			elif (self.opentype==AC_DEC):
				sld_area.OnStopFunc=EndOpen
			else:
				sld_area.OnStopFunc=EndOpenFunc
			return

		if (self.opentype==UNIF or self.opentype==UNIF_DEC):

			sld_area.SlideTo(self.closed_displ-self.o_med_displ, self.o_med_vel, 0)
			if (self.opentype==UNIF_DEC):
				sld_area.OnStopFunc=EndOpen
			else:
				sld_area.OnStopFunc=EndOpenFunc
			return

		if (self.opentype==DEC):
			dec=((self.o_end_vel**2-self.o_med_vel**2)/(2*self.o_end_displ))
			if (self.o_med_vel<0):
				dec=-dec

			sld_area.SlideTo(self.closed_displ-self.o_end_displ, self.o_med_vel, dec)
			sld_area.OnStopFunc=EndOpenFunc



	def CloseDoor(self):
##		import pdb
##		pdb.set_trace()

		if (self.status==CLOSED):
			return
		sld_area= Bladex.GetEntity(self.Name)
		self.prevdispl=sld_area.Displacement
		if self.Squezze:
			sld_area.HitFunc = DoorHit

		if (self.InitCloseSound):
			self.InitCloseSound.Position=self.soundpos
			self.InitCloseSound.PlaySound(0)

		if (self.WhileCloseSound):
			self.WhileCloseSound.Position=self.soundpos
			self.WhileCloseSound.PlaySound(-1)

		sld_area.TimerFunc=DisplaceSound
		sld_area.SubscribeToList("DoorTimer")

		if (self.closetype==AC or self.closetype==AC_UNIF_DEC or self.closetype==AC_UNIF or self.closetype==AC_DEC):
			ac=((self.c_med_vel**2-self.c_init_vel**2)/(2*self.c_init_displ))
			if (self.c_med_vel<0):
				ac=-ac
			sld_area.SlideTo(self.opened_displ+self.c_init_displ, self.c_init_vel, ac)
			if (self.closetype==AC_UNIF_DEC or self.closetype==AC_UNIF):
				sld_area.OnStopFunc=MedClose
			elif (self.closetype==AC_DEC):
				sld_area.OnStopFunc=EndClose
			else:
				sld_area.OnStopFunc=EndCloseFunc
			return

		if (self.closetype==UNIF or self.closetype==UNIF_DEC):
			sld_area.SlideTo(self.opened_displ+self.c_med_displ, self.c_med_vel, 0)
			if (self.closetype==UNIF_DEC):
				sld_area.OnStopFunc=EndClose
			else:
				sld_area.OnStopFunc=EndCloseFunc
			return

		if (self.closetype==DEC):
			dec=((self.c_end_vel**2-self.c_med_vel**2)/(2*self.c_end_displ))
			if (self.c_med_vel<0):
				dec=-dec
			sld_area.SlideTo(self.opened_displ+self.c_end_displ, self.c_med_vel, dec)
			sld_area.OnStopFunc=EndCloseFunc


	def SetInitOpenSound(self, sound):
		self.InitOpenSound=sound

	def SetWhileOpenSound(self, sound):
		self.WhileOpenSound=sound

	def SetEndOpenSound(self, sound):
		self.EndOpenSound=sound

	def SetInitCloseSound(self, sound):
		self.InitCloseSound=sound

	def SetWhileCloseSound(self, sound):
		self.WhileCloseSound=sound

	def SetEndCloseSound(self, sound):
		self.EndCloseSound=sound

##	def __str__(self):
##		return self.Name

	def persistent_id(self):
		return self.ObjId

	def __getstate__(self):
		# Tiene que devolver cómo poder guardar el estado de la clase
		return (1,
					self.ObjId, # De GameStateAux.PersistentObject
					self.Name,
					self.opentype,
					self.o_init_vel,
					self.o_med_vel,
					self.o_end_vel,
					self.o_init_displ,
					self.o_med_displ,
					self.o_end_displ,

					self.closetype,
					self.c_init_vel,
					self.c_med_vel,
					self.c_end_vel,
					self.c_init_displ,
					self.c_med_displ,
					self.c_end_displ,

					GameStateAux.SaveFunctionAux(self.OnEndOpenFunc),
					GameStateAux.SaveFunctionAux(self.OnEndCloseFunc),

					self.OnEndOpenArgs,
					self.OnEndCloseArgs,

					self.InitOpenSound,
					self.WhileOpenSound,
					self.EndOpenSound,

					self.InitCloseSound,
					self.WhileCloseSound,
					self.EndCloseSound,
					self.status,
					self.Squezze,
					self.closed_displ,
					self.opened_displ,
					self.surface,
					self.soundpos,
					self.prevdispl,
					GameStateAux.SaveNewMembers(self)
				)


	def __setstate__(self,parm):
		# Toma como parámetro lo que devuelve __getstate__() y debe recrear la clase
		if parm[0]==1:
			#self.ObjId=parm[1] En GameStateAux.PersistentObject()
##			GameStateAux.PersistentObject.__setstate__(self,parm)
			self.ObjId=parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self
			self.Name=parm[2]

			self.opentype=parm[3]
			self.o_init_vel=parm[4]
			self.o_med_vel=parm[5]
			self.o_end_vel=parm[6]
			self.o_init_displ=parm[7]
			self.o_med_displ=parm[8]
			self.o_end_displ=parm[9]

			self.closetype=parm[10]
			self.c_init_vel=parm[11]
			self.c_med_vel=parm[12]
			self.c_end_vel=parm[13]
			self.c_init_displ=parm[14]
			self.c_med_displ=parm[15]
			self.c_end_displ=parm[16]

			GameStateAux.LoadFunctionAux(parm[17],self,"OnEndOpenFunc")
			GameStateAux.LoadFunctionAux(parm[18],self,"OnEndCloseFunc")

			self.OnEndOpenArgs=parm[19]
			self.OnEndCloseArgs=parm[20]

			self.InitOpenSound=parm[21]
			self.WhileOpenSound=parm[22]
			self.EndOpenSound=parm[23]

			self.InitCloseSound=parm[24]
			self.WhileCloseSound=parm[25]
			self.EndCloseSound=parm[26]
			self.status = parm[27]
			self.Squezze = parm[28]
			self.closed_displ = parm[29]
			self.opened_displ = parm[30]
			self.surface = parm[31]
			self.soundpos = parm[32]
			self.prevdispl= parm[33]
			GameStateAux.LoadNewMembers(self,parm[34])

		else:
			print "Door.__setstate__() -> Version mismatch"
			# Valores por si valen para algo.
			self.Name= "Error loading"
			self.ObjId=ObjStore.GetNewId()
			ObjStore.ObjectsStore[self.ObjId]=self

# Funcion de muerte por aplastamiento
def DoorHit(sld,per,x,y,z,dx,dy,dz,wcx,wcy,wcz,wdx,wdy,wdz):

	p = Bladex.GetEntity(per)
	if dy!=0:
		p.LaunchAnmType("dth_rock")
	p.Life = -1
	if per == "Player1":
		cam = Bladex.GetEntity("Camera")
		cam.SType=0
		cam.TType=0
		AuxFuncs.FadeTo(3.0,60.0,32,0,0)
		Scorer.SetVisible(0)
		
def Restore():
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	AuxFuncs.FadeFrom(3.0,0.0,255,0,0)
	char          = Bladex.GetEntity("Player1")
	char.UnFreeze()
	char.Alpha    = 1
	char.SelfIlum = 0
	char.LaunchAnmType("rlx")
	Scorer.SetVisible(1)
	char.Data.ReSpawn("Player1")

	

def CreateDoor(sld_name, sector, sld_surface, opened_displ, closed_displ, init_status=CLOSED):
	door=Door(sld_name)
	sld_area=Bladex.CreateEntity(sld_name, "Entity Sliding Area", sector[0], sector[1], sector[2])
	sld_area.SlidingSurface=sld_surface
	door.surface=sld_surface
	if (init_status==OPENED):
		door.status=OPENED
		v=sld_surface[0]*closed_displ, sld_surface[1]*closed_displ, sld_surface[2]*closed_displ
		door.soundpos=sector[0]-v[0], sector[1]-v[1], sector[2]-v[2]
		door.prevdispl=door.currdispl=sld_area.Displacement=opened_displ
	else:
		door.status=CLOSED
		door.soundpos=sector
		door.prevdispl=door.currdispl=sld_area.Displacement=closed_displ
	door.opened_displ=opened_displ
	door.closed_displ=closed_displ
	InitDataField.Initialise(sld_area)
	sld_area.Data.doordata=door
	door.Squezze = 0
	#sld_area.HitFunc = DoorHit
	return door

