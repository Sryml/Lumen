import Bladex
import netgame
import whrandom
import LavaDefDamage
import whrandom
import math
import Netval
import string
import Sounds
import ReadGSFile
import storm

ReadGSFile.ProcessGhostSectorFile("terremoto.sf")

despSound1=Sounds.CreateEntitySound("../../Sounds/terremoto-piedras.wav","desprendimiento1")
despSound1.Volume=1; despSound1.MinDistance=2000; despSound1.MaxDistance=90000;

despSound2=Sounds.CreateEntitySound("../../Sounds/Rock-floor-collapse.wav","desprendimiento2")
despSound2.Volume=1; despSound2.MinDistance=2000; despSound2.MaxDistance=90000;

despSound3=Sounds.CreateEntitySound("../../Sounds/ground-collapse.wav","desprendimiento3")
despSound3.Volume=1; despSound3.MinDistance=2000; despSound3.MaxDistance=90000;

floodDelay			= 0.0
floodOsc1Frec		= 0.0
floodOsc2Frec		= 0.0
floodOscAmp			= 0.0
floodX				= -42173
floodStartHeight	= 67260
floodZ				= 3047
floodHeightIncr		= - 70475
floodY				= 0.0
floodYPrev			= 0.0
floodTime			= 0.0
floodTimeOscFrec	= 0.0
floodTimeOscAmp		= 0.0

quakeTime			= 2.0
quakeInt			= 1.0
quakeUmbra			= 200.0

lava_ImServer		= 0

lavaLocalTime_lastroundstart	= 0

randngenerator = whrandom.whrandom()

def floodTouchFunc( ent, entity_name, entity_damaged, factor):
	#print("mueto!!")
	pass

earthQuake = 0
def earthQuakeOff() :
	global earthQuake
	cam = Bladex.GetEntity("Camera")
	cam.EarthQuake = 0
	earthQuake = 0

def earthQuakeDustOff():
	deleteStorm("eqdust")

def earthQuakeDustOn():
	storm.createDustStorm("eqdust",2500); storm.setupStorm("eqdust");
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5,earthQuakeDustOff,())

def earthQuakeOn( fact ) :
	global earthQuake
	if (earthQuake) : return
	earthQuake = 1
	cam = Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor = fact * quakeInt
	cam.EarthQuake = 1

	rndid =randngenerator.randint(0,2)
	if (rndid==0) 	: despSound=despSound1
	elif (rndid==1) 	: despSound=despSound2
	else		: despSound=despSound3

	char= Bladex.GetEntity("Player1")
	despSound.Position = char.Position
	despSound.PlaySound(1)

	#Bladex.AddScheduledFunc(Bladex.GetTime()+quakeTime-1.0,earthQuakeDustOn,())
	Bladex.AddScheduledFunc(Bladex.GetTime()+quakeTime,earthQuakeOff,())

def floodTimer(ent, time) :
	global floodY
	global floodYPrev

	if (lava_ImServer):
		time = Bladex.GetTime() - lavaLocalTime_lastroundstart
 		segTime = int(time/floodDelay)*floodDelay
		segTimeOsc = segTime+((math.sin(segTime*floodTimeOscFrec)-1.0)*floodTimeOscAmp)
		floodYPrev = floodY
		floodY = floodStartHeight + ( floodHeightIncr * (segTimeOsc/floodTime) )
		floodYMax = floodStartHeight + floodHeightIncr
		if ( floodY < floodYMax ) : floodY = floodYMax
		floodY=floodY+(math.sin(time*floodOsc1Frec)*math.sin(time*floodOsc2Frec)*floodOscAmp)
		floodY=floodYPrev+((floodY-floodYPrev)/10)
		if ( floodY > floodStartHeight ) : floodY = floodStartHeight
		sendFloodHeight()

	delta = abs(floodY-floodYPrev)
	if (delta>quakeUmbra) : earthQuakeOn(delta)

	Bladex.GetEntity("volcanolava").Position = floodX, floodY, floodZ

def sendFloodHeight() :
	#print("-mandando el tiempo para sincronizar a los clientes")
	dataToSend = '%6.4f' % ( floodY )
	#print dataToSend
	netgame.SendUnguaranteedUserString(Netval.NET_GAME_LAVAPOSITION,dataToSend)

if netgame.GetNetState() == 2:
	def recvFloodString(id,type,cad):
		global floodY
		global floodYPrev
		#print id," ", type," ", cad
		if (type==Netval.NET_GAME_LAVAPOSITION):
			argarray = string.split(cad)
			floodYPrev	= floodY
			floodY		= string.atof(argarray[0])
		else:
			ReadUserString(id,type,cad)

	netgame.SetStringUserFunc(recvFloodString)

def floodOnStartRound() :
	#print("-empezando un round")
	global floodDelay
	global floodY
	global floodYPrev
	global floodTime
	global floodOsc1Frec
	global floodOsc2Frec
	global floodOscAmp
	global floodTimeOscFrec
	global floodTimeOscAmp
	global lavaLocalTime_lastroundstart

	#print("floodOnStartRound")


	if (lava_ImServer) :
		floodDelay			= randngenerator.random() * 5.0   + 10.0
		floodOsc1Frec		= randngenerator.random() * 0.3 + 0.3
		floodOsc2Frec		= randngenerator.random() * 1.0 + 2.5
		floodOscAmp			= randngenerator.random() * 1160.0 + 1110.0
		floodTime			= 35 + 45 * randngenerator.random()
		floodTimeOscFrec	= randngenerator.random() * 1.0
		floodTimeOscAmp		= 18.0
		lavaLocalTime_lastroundstart = Bladex.GetTime()

	floodY		= floodStartHeight
	floodYPrev	= floodStartHeight


def floodOnJoin (id,objname,name,race,weapon,shield) :
	#print ("-se ha unido otro pakete a la partida ")
	sendFloodHeight()
	pass



def setNullParams():
	floodHeightIncr		= - 1000
	floodDelay			= 1
	floodTime			= 1
	floodY				= floodStartHeight
	floodYPrev			= floodStartHeight



Bladex.CreateTimer("volcanolavatimer",0.1)
def startFlood() :
	floodArea = LavaDefDamage.LAVA_AREA()
	floodArea.CreateLava ("volcanolava" , floodX, floodStartHeight, floodZ , "cala2", 0.02 )
	#floodArea.TouchFluidFunc = floodTouchFunc

	setNullParams()

	lava = Bladex.GetEntity("volcanolava")
	lava.TimerFunc = floodTimer
	lava.SubscribeToList("volcanolavatimer")
