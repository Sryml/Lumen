import netgame
import Bladex
import LavaDefDamage
import Netval
import math
import NetMisc
import dust
import whrandom
import Sounds
import Actions

def rand(time):
	PRIME = 123457
	MULTI = 510510

	return (1.0*((MULTI*time)%PRIME))/PRIME

def CPrime(min):
	p = [2,3,5,7,11]
	c = 12

	while p[len(p)-1]<min:
		c = c + 1
		ip = 1
		for v in p:
			if c % v==0:
				ip = 0
				break
		if ip:
			p.append(c)
			print c


StartTime   = 0.0 					# Variable global que marca el inicio de un round
ListOfTraps = []					# Lista de trampas en el juego

def LeeCadena(id,type,cad):
	global StartTime

	if type ==  Netval.NET_GAME_START_TRAPS:
		StartTime = float(cad)

	for o in ListOfTraps:
		o.Start()


NetMisc.LReadUserString.append(LeeCadena)

def IniciaRound():
	global StartTime

	StartTime           = netgame.GetTime()
	netgame.SendUserString(Netval.NET_GAME_START_TRAPS,`StartTime`)

	for o in ListOfTraps:
		o.Start()


NetMisc.LOnStartRoundFunc.append(IniciaRound)

#################### TRAMPA DE LA LAVA ####################
class LavaFlood:
	TimeRound  = 3
	DeltaRound = 5000
	Quake      = 0
	sino       = 0

	def SetCameraOutOfLava(self):
		cam = Bladex.GetEntity("Camera")
		cam.SType   = 0
		cam.TType   = 0
		cam.TPos = cam.TPos[0], self.Surface.Position[1], cam.TPos[2]
		cam.Position = cam.Position[0], self.Max-500-self.DeltaRound, cam.Position[2]


	def QuemarCliente(self,entid):
		namex = entid.Name+"LavaFire"
		wps = Bladex.GetEntity(namex)
		if netgame.GetPlayerData(entid.Name)[1] <= 0:
			if entid.Name=="Player1":
				self.SetCameraOutOfLava()
			if not entid.Data.LavaDeath:
				Actions.FireDeath(entid.Name)
				entid.Data.LavaDeath = 1
		else:
			entid.Data.LavaDeath = 0
			pos = entid.Position
			if wps:
				wps.Position = pos[0], self.Surface.Position[1]+1, pos[2]
			else:
				wps=Bladex.CreateEntity(namex, "Entity Particle System D1", entid.Position[0], self.Surface.Position[1]+1, entid.Position[2])
				wps.ParticleType="LargeFire"
				wps.Time2Live=16
				wps.RandomVelocity=10.0
				wps.Velocity=0,-1000,0
				wps.YGravity=0
				wps.PPS=50


			snd_name=entid.Name+"_LavaSnd"
			sound=Bladex.GetEntity(snd_name)
			if not sound:
				sound=Bladex.CreateEntity(snd_name, "Entity Sound", pos[0], pos[1], pos[2] )
				sound.SetSound("../../Sounds/muerte-acida.wav")
			else:
				sound.Position=pos
			if sound.Playing==0:
				sound.PlaySound(0)

			wps.DeathTime=Bladex.GetTime()+1.0

	def __init__(self,Max,Min,MaxT,MinT,text="cala2"):
		global ListOfTraps

		self.Max      = Max
		self.Min      = Min
		self.MaxT     = MaxT
		self.MinT     = MinT
		self.Surface  = None
		self.Texture  = text

		ListOfTraps.append(self)

	# check for lava values on lineX
	def TestLavaDamage(self,ent):
		if ent.Position[1]+1500 > self.Surface.Position[1]:
			self.QuemarCliente(ent)
			return 1
		return 0

	def Start(self):
		global StartTime

		if not self.Surface:
			self.LavaName     = "Lava"+Bladex.GenerateEntityName()
			print "Creating '"+self.LavaName+"' for fun"
			self.LavaDamage   = LavaDefDamage.LAVA_AREA()
			self.LavaDamage.CreateLava (self.LavaName,self.Position[0],self.Position[1],self.Position[2], self.Texture, 0.01 )
			self.Surface      = Bladex.GetEntity(self.LavaName)
			NetMisc.LOnDamageFunc.append(self.TestLavaDamage)

		self.Surface.TimerFunc   = self.floodTimer
		self.Surface.SubscribeToList("Timer30")

		self.MaxTime = (self.MaxT-self.MinT)*rand(StartTime) + self.MinT
		self.EndTime = int((self.MaxTime+self.TimeRound*2)/self.TimeRound)*self.TimeRound + self.TimeRound/2
		self.sino    = 0

	def floodTimer(self,ent, time):
		global StartTime

		time = netgame.GetTime()

		tetha = (time-StartTime)/self.MaxTime

		if self.EndTime+StartTime < time:
			time = self.EndTime+StartTime

		if tetha>1:
			tetha = 1
		else:
			tetha = ((tetha+1)%2)-1

		sino = (time-StartTime)/self.TimeRound
		AddSin = math.sin(3.1515*sino)*self.DeltaRound

		pos = (self.Max-self.Min)*tetha+self.Min + AddSin

		self.Surface.Position = self.Position[0], pos, self.Position[2]

		if self.Quake:
			if sino > self.sino+2.0:
				temblOn(0)
				self.sino = int(sino/2)*2






#################### Temblores Aleatorios ####################

mQuakeTime     = 2
MQuakeTime     = 4

mQuakeDelay    = 5
MQuakeDelay    = 10

QuakeIntensity = 100

Temblon_ = [1,1,1]

Temblon_[0]=Sounds.CreateEntitySound("../../Sounds/terremoto-piedras.wav","desprendimiento1")
Temblon_[0].Volume=1; Temblon_[0].MinDistance=90000; Temblon_[0].MaxDistance=100000;

Temblon_[1]=Sounds.CreateEntitySound("../../Sounds/Rock-floor-collapse.wav","desprendimiento2")
Temblon_[1].Volume=1; Temblon_[1].MinDistance=90000; Temblon_[1].MaxDistance=100000;

Temblon_[2]=Sounds.CreateEntitySound("../../Sounds/ground-collapse.wav","desprendimiento3")
Temblon_[2].Volume=1; Temblon_[2].MinDistance=90000; Temblon_[2].MaxDistance=100000;


def temblOff():
	cam = Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor = 0
	cam.EarthQuake = 0

def temblOn(repeat = 1):
	global mQuakeTime
	global MQuakeTime
	global mQuakeDelay
	global MQuakeDelay
	global QuakeIntensity

	cam = Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor = QuakeIntensity
	cam.EarthQuake = 1
	Bladex.AddScheduledFunc(Bladex.GetTime()+whrandom.randint(mQuakeTime, MQuakeTime), temblOff,())
	if repeat:
		Bladex.AddScheduledFunc(Bladex.GetTime()+whrandom.randint(mQuakeDelay,MQuakeDelay), temblOn,())
	char= Bladex.GetEntity("Player1")
	m = whrandom.randint(0,2)
	Temblon_[m].Position = char.Position
	Temblon_[m].PlaySound(1)



######################[ E J E M P L O S ]######################
"""
import NetTraps

# Agrega una trampa de lava
lava = NetTraps.LavaFlood(-5000,60000,240,120)	# <limite superior>,<limite inferior>,<maximo de tiempo>,<minimo de tiempo>
lava.Position = (26837, 74000, 4427)		# Posicion donde esta la lava
lava.TimeRound  = 4				# Tiempo de oscilacion
lava.DeltaRound = 3000				# Radio de oscilacion
lava.Quake      = 1				# asigna el evento de temblores a la oscilacion.

# Temblores
NetTraps.mQuakeTime     =   2			# Duracion minima del temblores
NetTraps.MQuakeTime     =   4			# Duracion maxima del temblores
NetTraps.mQuakeDelay    =   5			# Retardo minimo entre temblores
NetTraps.MQuakeDelay    =  10			# Retardo maximo entre temblores
NetTraps.QuakeIntensity = 100			# Intensidad del temblor

NetTraps.temblOn()				# activa los temblores para siempre (no usar si se asigna a la lava)

"""