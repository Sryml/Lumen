##########################################################
#
#	SCRIPT	: libreria para poner viruta delante de la camara
#
#	AUTH	: Yuio
#
#
##########################################################

#
# esto se lo dedico a uno de mis idolos : al pitufo gruñon
# (al que le seguia encima siempre una nube con tormenta) 
#

import math
import Bladex
import AuxFuncs
import cameraAux


distances={}

# import storm; storm.createDustStorm("test",2500); storm.setupStorm("test");

Bladex.CreateTimer("dustStormTimer",0.1)
B_PARTICLE_GTYPE_BLEND=1
Bladex.AddParticleGType("dustStormPT","SmokeParticle",B_PARTICLE_GTYPE_BLEND,32)
for i in range(64):
	r=200
	g=170
	b=140
	a=i + 25.0
	size= (i/64.0)*1000.0
	Bladex.SetParticleGVal("dustStormPT",i,r,g,b,a,size)

def setupStorm(name,dist,fov=3.14*0.57):
	storm=Bladex.GetEntity(name)
	cameraAux.updateInfo()
	cam = Bladex.GetEntity("Camera")
	opos=cam.Position
	tpos=cam.TPos
	v=tpos[0]-opos[0], tpos[1]-opos[1], tpos[2]-opos[2]

	hfovtan			= math.tan(fov*0.5)
	disthfov		= dist*hfovtan

	px				= cam.Position[0]+cameraAux.n[0]*dist
	py				= cam.Position[1]+cameraAux.n[1]*dist
	pz				= cam.Position[2]+cameraAux.n[2]*dist

	dx				= -cameraAux.u[0]*disthfov
	dy				= -cameraAux.u[1]*disthfov
	dz				= -cameraAux.u[2]*disthfov
	
	storm.Position	= px-dx-cameraAux.v[0]*disthfov, py-dy-cameraAux.v[1]*disthfov, pz-dz-cameraAux.v[2]*disthfov
	storm.D1		= dx*2.0, dy*2.0, dz*2.0

def deleteStorm(storm):
	partSys = Bladex.GetEntity(storm)
	partSys.SubscribeToList("Pin")

def updateTimer(ent, time):
	setupStorm(ent,	distances[ent])

def createDustStorm(name,dist):
	char = Bladex.GetEntity("Player1")
	partSys=Bladex.CreateEntity(name, "Entity Particle System D2", char.Position[0],char.Position[1],char.Position[2] )
	partSys.D1= 1000,0,0
	partSys.ParticleType="dustStormPT"
	partSys.YGravity=-1030.0
	partSys.Friction=0.2
	partSys.PPS=400
	partSys.DeathTime=Bladex.GetTime()+999999.0
	partSys.Time2Live=31
	partSys.Velocity=0.0, 20000.0, 0.0
	partSys.RandomVelocity=200.0

	partSys.TimerFunc = updateTimer
	partSys.SubscribeToList("Timer15")

	distances[name]=dist

	return partSys
