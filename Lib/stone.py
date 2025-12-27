##########################################################
#
#	SCRIPT	: libreria para lanzar cosas
#
#	AUTH	: Yuio
#
#
##########################################################

import math
import Bladex
import Sounds
import GameStateAux
import ObjStore

# sonidos de las bolas
stoneDrop = "../../Sounds/golpe-bola-piedra.wav"	# sonido de inicio
stoneLoop = "../../Sounds/piedra-rodando-1.wav"	# loop

stoneDSound=Sounds.CreateEntitySound(stoneDrop, "stoneSound")
stoneDSound.Volume=1.0
stoneDSound.MinDistance=10000
stoneDSound.MaxDistance=90000

MESSAGE_START_WEAPON=7
MESSAGE_STOP_WEAPON=8

SQR_DELTA_HIT_VARIATION = 10000000

class DataStone:

	ObjId=""
	stoneDictionary=None
	stoneDictionaryB=None
	stoneDictionaryC=None
	stoneDictionaryD=None
	Entidad = None
	LastDelta = 0,0,0


	def __init__(self,entName,A,B,C,D):
		self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
		self.stoneDictionary=A
		self.stoneDictionaryB=B
		self.stoneDictionaryC=C
		self.stoneDictionaryD=D
		self.Entidad = entName
		ObjStore.ObjectsStore[self.ObjId]=self
		self.LastDelta = 0,0,0

	def persistent_id(self):
		return self.ObjId

	def __getstate__(self):
		# Tiene que devolver como poder guardar el estado de la clase

		return (1,
				self.ObjId,
				self.stoneDictionary,
				self.stoneDictionaryB,
				GameStateAux.SaveEntityAux(self.stoneDictionaryC),
				GameStateAux.SaveEntityAux(self.stoneDictionaryD),
				self.Entidad,
				GameStateAux.SaveNewMembers(self)
				)

	def __setstate__(self,parm):
		# Toma como par�metro lo que devuelve __getstate__() y debe recrear la clase
		if parm[0]==1:
			#self.ObjId=parm[1] En GameStateAux.PersistentObject()
##			GameStateAux.PersistentObject.__setstate__(self,parm)
			self.ObjId=parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self
			self.stoneDictionary  = parm[2]
			self.stoneDictionaryB = parm[3]
			self.stoneDictionaryC = GameStateAux.LoadEntityAux(parm[4])
			self.stoneDictionaryD = GameStateAux.LoadEntityAux(parm[5])
			self.Entidad = GameStateAux.LoadEntityAux(parm[6])
			self.Entidad.Data = self
			self.Entidad = parm[6]
			GameStateAux.LoadNewMembers(self,parm[7])
			self.LastDelta = 0,0,0

#			GameStateAux.LoadedPickledData[self.ObjId]=self
		else:
			# Valores de creaci�n por si valen para algo.
			self.stoneDictionary  = 0,0,0,0,0,0,0,0,0
			self.stoneDictionaryB = 0,0,0
			self.stoneDictionaryC = None
			self.stoneDictionaryD = None
			self.Entidad = None
			self.ObjId=ObjStore.GetNewId()
			ObjStore.ObjectsStore[self.ObjId]=self
			self.LastDelta = 0,0,0


Bladex.CreateTimer("stoneLibTimer",0.1)
B_PARTICLE_GTYPE_BLEND=1
Bladex.AddParticleGType("DesertDustB","SmokeParticle",B_PARTICLE_GTYPE_BLEND,32)
for i in range(32):
	r=200
	g=170
	b=140
	a=i + 50.0
	size= (i/32.0)*1000.0
	Bladex.SetParticleGVal("DesertDustB",i,r,g,b,a,size)

Bladex.AddParticleGType("DesertDarkDustB","SmokeParticle",B_PARTICLE_GTYPE_BLEND,32)
for i in range(32):
	r=85
	g=55
	b=35
	a=i + 125.0
	size= (i/32.0)*1500.0
	Bladex.SetParticleGVal("DesertDarkDustB",i,r,g,b,a,size)


DROPNULL = 0
DROPBROWNDUST = 1
DROPDARKDUST = 2

SOUNDNULL = 0
STONESOUND = 1

def cuadradox(x):
	return x*x

def stoneHandler(ent,time) :
	sto = Bladex.GetEntity(ent)
	stoneData = sto.Data
	params = stoneData.stoneDictionary
	pos = sto.Position
	cpos = (pos[0]+params[1], pos[1]+params[2], pos[2]+params[3] )
	ppos = stoneData.stoneDictionaryB
	stoneData.stoneDictionaryB = cpos
	dx = ppos[0]-cpos[0]
	dy = ppos[1]-cpos[1]
	dz = ppos[2]-cpos[2]
	size = math.sqrt(dx*dx + dy*dy + dz*dz)
	eval = size * stoneData.stoneDictionary[5]
	deltaVariation = cuadradox(dx-stoneData.LastDelta[0])+cuadradox(dx-stoneData.LastDelta[1])+cuadradox(dx-stoneData.LastDelta[2])

	if SQR_DELTA_HIT_VARIATION < deltaVariation:
		stoneDSound.Position = pos
		if not stoneDSound.Playing:
			stoneDSound.PlaySound(0)


	#print ent,": delta(",dx,",",dy,",",dy,",",dz," eval:", eval

	dtype = stoneData.stoneDictionary[0]
	if (dtype<>DROPNULL and stoneData.stoneDictionaryC) :
		if (dtype==DROPBROWNDUST) :
			dust  = stoneData.stoneDictionaryC
			dust.Position = cpos
			dust.D1 = dx, dy, dz
			dust.PPS = eval
		elif (dtype==DROPDARKDUST):
			dust  = stoneData.stoneDictionaryC
			dust.Position = cpos
			dust.D1 = dx, dy, dz
			dust.PPS = eval * 0.85

	stype = params[6]
	if (stype<>SOUNDNULL and stoneData.stoneDictionaryD) :
		if	(stype==STONESOUND) :
			sound = stoneData.stoneDictionaryD
			soundvolume = eval * 0.025 * params[7]
			sound.Position = cpos
			if (soundvolume>1.0): soundvolume=1.0
			sound.Volume = 1
			if not sound.Playing:
				sound.PlaySound(0)
			#print soundvolume

	stoneData.LastDelta = dx,dy,dz

def lock(entName, trail, offsetX, offsetY, offsetZ, trailParam, autodest, sound, soundParam ) :
	ent = Bladex.GetEntity(entName)
	stoneDictionary= trail, offsetX, offsetY, offsetZ, autodest, trailParam, sound, soundParam
	stoneDictionaryB = ( ent.Position[0]+offsetX, ent.Position[1]+offsetY, ent.Position[2]+offsetZ )
	stoneDictionaryC = 0
	stoneDictionaryD = 0

	if (trail<>DROPNULL) :
		if	(trail==DROPBROWNDUST):
			stoneDust=Bladex.CreateEntity("ps"+entName, "Entity Particle System D2", ent.Position[0], ent.Position[1], ent.Position[2] )
			stoneDust.D1= 0,0,0
			stoneDust.ParticleType="DesertDustB"
			stoneDust.YGravity=-1030.0
			stoneDust.Friction=0.3
			stoneDust.PPS=0
			stoneDust.DeathTime=Bladex.GetTime()+999999.0
			stoneDust.Time2Live=31
			stoneDust.Velocity=0.0, 4000.0, 0.0
			stoneDust.RandomVelocity=110.0
			stoneDictionaryC = stoneDust
		elif (trail==DROPDARKDUST):
			stoneDust=Bladex.CreateEntity("ps"+entName, "Entity Particle System D2", ent.Position[0], ent.Position[1], ent.Position[2] )
			stoneDust.D1= 0,0,0
			stoneDust.ParticleType="DesertDarkDustB"
			stoneDust.YGravity=-1030.0
			stoneDust.Friction=0.3
			stoneDust.PPS=0
			stoneDust.DeathTime=Bladex.GetTime()+999999.0
			stoneDust.Time2Live=31
			stoneDust.Velocity=0.0, 4000.0, 0.0
			stoneDust.RandomVelocity=110.0
			stoneDictionaryC = stoneDust

	if (sound<>SOUNDNULL) :
		if	(sound==STONESOUND) :
			stonelSound=Sounds.CreateEntitySound(stoneLoop, "stoneSound")
			stonelSound.Volume=1
			stonelSound.MinDistance=7000
			stonelSound.MaxDistance=70000
			stoneDictionaryD = stonelSound

	ent.Data = DataStone(entName,stoneDictionary,stoneDictionaryB,stoneDictionaryC,stoneDictionaryD)


def unlock(entName):
	#print"entName",l
	ent = Bladex.GetEntity(entName)
	ent.TimerFunc = ""
	ent.RemoveFromList("stoneLibTimer")
	stoneData = ent.Data

	if (stoneData.stoneDictionary[0]<>DROPNULL and stoneData.stoneDictionaryC):
		stoneData.stoneDictionaryC.DeathTime=Bladex.GetTime()

	if (stoneData.stoneDictionary[6]<>SOUNDNULL and stoneData.stoneDictionaryD):
		stoneData.stoneDictionaryD.StopSound()

	del stoneData
	#print("delete")

def drop(entName,impulseX, impulseY, impulseZ):
	ent = Bladex.GetEntity(entName)
	ent.Impulse(impulseX, impulseY, impulseZ)
	ent.TimerFunc = stoneHandler
	ent.SubscribeToList("stoneLibTimer")
	ent.MessageEvent(MESSAGE_START_WEAPON,0,0)
	autodest = ent.Data.stoneDictionary[4]
	if (autodest>0.0) :
		import stone
		Bladex.AddScheduledFunc( Bladex.GetTime()+ent.Data.stoneDictionary[4], stone.unlock, (entName,) )

	if (ent.Data.stoneDictionary[6]<>SOUNDNULL and ent.Data.stoneDictionaryD):
		snd = ent.Data.stoneDictionaryD
		#snd.PlaySound(-1)

		stoneDSound.Position = ent.Position
		stoneDSound.PlaySound(0)
