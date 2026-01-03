import whrandom
import math
import darfuncs
import Bladex
import Gems



o=Bladex.CreateEntity("gema1a","Gema",-17644,-7349,30699)
o.Scale=2.216715
o.Orientation=0.504344,0.504344,0.495618,0.495618

#
o=Bladex.CreateEntity("gema2a","Gema",-17641.307, -4304.583, 22953.586)
o.Scale=1.402577
o.Orientation=0.500000,0.500000,0.500000,0.500000

#
o=Bladex.CreateEntity("gema3a","Gema",-17641.951000,-7900.881000,56957.049000)
o.Scale=3.047852
o.Orientation=0.707107,0.707107,0.000000,0.000000

#
o=Bladex.CreateEntity("gema1b","Gema",-32158.296000,-7350.198000,30734.251000)
o.Scale=2.261271
o.Orientation=0.500000,0.500000,0.500000,0.500000

#
o=Bladex.CreateEntity("gema2b","Gema",-32116.878000,-4276.731000,22953.283000,"Physic")
o.Scale       = 1.549318
o.Orientation = 0.496456,0.500937,-0.482381,-0.519521
o.Solid       = 0
o.SelfIlum    = -2

#
o=Bladex.CreateEntity("gema3b","Gema",-32108.510000,-7801.219000,56841.394000)
o.Scale=2.731862
o.Orientation=0.707107,0.707107,0.000000,0.000000





LASER_GEMCOLOR = 10,128,10

LASER_INERFAC  = 0.5
LASER_COREFAC  = 0.1


LaserPuerta1 = [CreaRayo("gema2a","gema1a"),CreaRayo("gema2a","gema3a")]

LaserPuerta2 = [CreaRayo("gema2b","gema1b"),CreaRayo("gema2b","gema3b")]

#########################################################
###############  EFECTO DE CONCENTRACION  ###############
#########################################################
#
#def ConcentraTimer(e_name, time):
#	o = Bladex.GetEntity(e_name)
#	o.Data.Counter = o.Data.Counter + 1
#	
#	o.Scale = o.Data.Scale*(o.Data.Frames - o.Data.Counter)/o.Data.Frames + 1.0
#	
#	if o.Data.Counter > o.Data.Decon:
#		o.Alpha = 0.15-(0.15*(o.Data.Counter-o.Data.Decon))/(o.Data.Frames-o.Data.Decon)
#	else:
#		o.Alpha = 0.15*o.Data.Counter/o.Data.Frames
#	
#	o.Rotate(o.Data.x, o.Data.y, o.Data.z, o.Data.delta)
#	if o.Data.Counter+1 > o.Data.Frames :
#		o.RemoveFromList("Timer30")
#		o.SubscribeToList("Pin")
#
#def EfectoConcentracion(pos,name,frames=150,Scale = 30.0,RotSpeed = 32.0,Decon=100):
#	global ActualColor
#	class vacio:
#		pass
#	
#	if ActualColor == GREEN_GEM:
#		o=Bladex.CreateEntity(name,"EsferaGemaVerde", 0,0 ,0)
#	if ActualColor == RED_GEM:
#		o=Bladex.CreateEntity(name,"EsferaGemaRoja",  0,0 ,0)
#	if ActualColor == BLUE_GEM:
#		o=Bladex.CreateEntity(name,"EsferaGemaAzul",  0, 0,0)
#	
#	o.Static      = 1
#	o.Orientation = 0.707107,0.707107,0.000000,0.000000
#	o.Position    = pos
#	o.SelfIlum    = 1
#	o.CastShadows = 0
#	o.RasterMode  ="AdditiveAlpha"
#	o.RasterMode  ="Read"
#	o.Alpha       = 0.0
#	o.Scale       = 6.0
#	o.TimerFunc   = ConcentraTimer
#	o.SubscribeToList("Timer30")
#	o.Data        = vacio()
#	x             = whrandom.random()
#	y             = whrandom.random()
#	z             = whrandom.random()
#	tot           = x*x + y*y + z*z
#	x             = math.sqrt(x*x/tot)
#	y             = math.sqrt(y*y/tot)
#	z             = math.sqrt(z*z/tot)
#
#	if whrandom.random() >0.5:
#		o.Data.x      = +x
#	else:
#		o.Data.x      = -x
#
#	if whrandom.random() >0.5:
#		o.Data.y      = +y
#	else:
#		o.Data.y      = -y
#
#	if whrandom.random() >0.5:
#		o.Data.z      = +z
#	else:
#		o.Data.z      = -z
#		
#	o.Data.delta   = (whrandom.random()+0.5)/RotSpeed
#	o.Data.Counter = 0
#	o.Data.Frames  = frames
#	o.Data.Scale   = Scale	
#	o.Data.Decon   = Decon
#	
#	
#	print o.Data.x,o.Data.y,o.Data.z,o.Data.delta	
#	return o
#	
#
#
#Bladex.AddParticleGType("GemaConc","FireParticle",B_PARTICLE_GTYPE_ADD,64)
#
#for i in range(64):
#	aux = 1.0-i/64.0
#	r=10
#	g=205
#	b=150
#	a=aux*128.0
#	size=aux*128+64
#	Bladex.SetParticleGVal("GemaConc",i,r,g,b,a,size)
#	
#Bladex.AddParticleGType("Particulate","Estrellita",1,32)
#
#for i in range(32):
#	
#	a = i*4
#	
#	r=128.0
#	g=255.0
#	b=128.0
#	size= (i%8)*6
#	Bladex.SetParticleGVal("Particulate",i,r,g,b,a,size)
#
#
#def PiecesOfGema(pos):
#	RayoHit=Bladex.CreateEntity("RayoBastonHit", "Entity Particle System D1", pos[0],pos[1],pos[2])
#	RayoHit.Time2Live=32
#	RayoHit.YGravity=20000
#	RayoHit.ParticleType="Particulate"
#	RayoHit.Friction=0.95
#	RayoHit.Velocity=0,0,0
#	RayoHit.RandomVelocity=-5
#	RayoHit.DeathTime     = Bladex.GetTime()+1.0
#
#GREEN_GEM = 0
#RED_GEM   = 1
#BLUE_GEM  = 2
#
#ActualColor = GREEN_GEM
#
#def SetGemColor(color):
#	global ActualColor
#	ActualColor = color
#		
#	if ActualColor==GREEN_GEM:
#		r = 10 
#		g = 205
#		b = 150
#	if ActualColor==RED_GEM:
#		r = 205
#		g = 150
#		b = 10 
#	if ActualColor==BLUE_GEM:
#		r = 10
#		g = 150
#		b = 205
#	
#	for i in range(64):
#		aux = 1.0-i/64.0
#		r=10
#		g=205
#		b=150
#		a=aux*128.0
#		size=aux*128+64
#		Bladex.SetParticleGVal("GemaConc",i,r,g,b,a,size)
#
#
#	#########################################################
#	if ActualColor==GREEN_GEM:
#		r = 128.0
#		g = 255.0
#		b = 128.0
#	if ActualColor==RED_GEM:
#		r = 255.0
#		g = 128.0
#		b = 128.0
#	if ActualColor==BLUE_GEM:
#		r = 128.0
#		g = 128.0
#		b = 255.0
#	
#	for i in range(32):		
#		a = i*4		
#		r=128.0
#		g=255.0
#		b=128.0
#		size= (i%8)*6
#		Bladex.SetParticleGVal("Particulate",i,r,g,b,a,size)	
#
#def ConcentratorParticulate(pos,delta=(0,0,0)):
#
#	RayoHit=Bladex.CreateEntity("RayoBastonHit", "Entity Particle System D1", pos[0],pos[1],pos[2])
#	RayoHit.ParticleType="GemaConc"
#	RayoHit.Time2Live=64
#	RayoHit.YGravity=0.0
#	RayoHit.Friction=0
#	RayoHit.PPS=255
#	RayoHit.Velocity=delta
#	RayoHit.RandomVelocity=-10
#	RayoHit.DeathTime     = Bladex.GetTime()+4.0
#
#GemCallBack = None
#GemParams   = ()
#
#def FlashGem():	
#	if ActualColor==GREEN_GEM:
#		AuxFuncs.FadeFrom(0.15,0.0,128,255,128)
#	if ActualColor==RED_GEM:
#		AuxFuncs.FadeFrom(0.15,0.0,255,128,128)
#	if ActualColor==BLUE_GEM:
#		AuxFuncs.FadeFrom(0.15,0.0,128,128,255)
#
#	if GemCallBack != None:
#		apply(GemCallBack,GemParams)
#
#def Concentrator(pos,delta=(0,0,0)):
#	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.5,  EfectoConcentracion,(pos,"C1gema1a",))
#	Bladex.AddScheduledFunc(Bladex.GetTime() + 1.0,  EfectoConcentracion,(pos,"C2gema1a",))
#	Bladex.AddScheduledFunc(Bladex.GetTime() + 1.5,  EfectoConcentracion,(pos,"C3gema1a",))
#	Bladex.AddScheduledFunc(Bladex.GetTime() + 5.95, PiecesOfGema,(pos,))
#	Bladex.AddScheduledFunc(Bladex.GetTime() + 6.0,  FlashGem,())
#	ConcentratorParticulate(pos,delta)
#	
#
######################################################
##                       ESCENA                     ##
######################################################


p=Bladex.CreateEntity("GemBGPointer","GhostPointer",-32142.875, -4335.11, 23029.048)
p.Static=0
p.Scale=0.100000
p.Orientation=0.568413,0.420603,-0.420603,-0.568413
p.UseFunc = useInGemGhostP
darfuncs.SetHint(p,"Empty Eye")



o             = Bladex.GetEntity("gema2b")
o.Position    = -24827.844000,-12343.442000,34750.099000
o.Scale       = 1.528790
o.Orientation = 0.989336,0.015508,-0.144800,-0.002444
	

