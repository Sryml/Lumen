import Bladex
import Sounds
import math
import Reference
import Select
import Change
import Actions
import Bladex
import AuxFuncs
import GameText

#############charco del inicio 

agua_chok=Bladex.CreateEntity("agua_chok","Entity Water",207882, 2550, 93541)
agua_chok.Reflection=0.0
agua_chok.Color=8,8,8


#############almacen 

agua_pilonk=Bladex.CreateEntity("agua_pilonk","Entity Water",335750,-5420,125875)
agua_pilonk.Reflection=0.0
agua_pilonk.Color=8,8,8




Bladex.AddParticleGType("AguaC2","WaterParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	r=90
	g=100
	b=100
	a=60
	size=120.0
	Bladex.SetParticleGVal("AguaC2",i,r,g,b,a,size)

Bladex.AddParticleGType("Espuma2","SmokeParticle",B_PARTICLE_GTYPE_BLEND,10)

for i in range(10):
	aux=(10.0-i)/10.0
	r=90
	g=90
	b=90
	#a=255*math.sqrt(1.0-aux)
	a=255
	size=500.0*math.sqrt(1.0-aux)
	Bladex.SetParticleGVal("Espuma2",i,r,g,b,a,size)


#char.Position = -45250, 2000,-30000

def CreateCascada(Cascada,p,d,v,pc,Time = 18,Grav = 8000,PPS = 400):
	cascada=Bladex.CreateEntity(Cascada, "Entity Particle System D2",p[0],p[1],p[2])
	cascada.D=d[0],d[1],d[2]
	cascada.ParticleType="AguaC2"
	cascada.Friction=0.07
	cascada.RandomVelocity=10.0
	cascada.Velocity=v[0],v[1],v[2]
	cascada.PPS=PPS
	cascada.YGravity=Grav
	cascada.Time2Live=Time

	Espuma2=Bladex.CreateEntity(Cascada+"Espuma2", "Entity Particle System D2",pc[0],pc[1],pc[2])
	Espuma2.D=d[0],d[1],d[2]
	Espuma2.ParticleType="Espuma2"
	Espuma2.PPS=40
	Espuma2.YGravity=0.0
	Espuma2.Friction=0.07
	Espuma2.Velocity=0.0, -1000.0, 0.0
	Espuma2.RandomVelocity=30.0
	Espuma2.RandomVelocity_V=30.0
	Espuma2.Time2Live=10

def CreateEspuma2(Espuma2,pc,d,PPS = 40):
	Espuma2=Bladex.CreateEntity(Espuma2, "Entity Particle System D2",pc[0],pc[1],pc[2])
	Espuma2.D=d[0],d[1],d[2]
	Espuma2.ParticleType="Espuma2"
	Espuma2.PPS=PPS
	Espuma2.YGravity=0.0
	Espuma2.Friction=0.07
	Espuma2.Velocity=0.0, -1000.0, 0.0
	Espuma2.RandomVelocity=30.0
	Espuma2.RandomVelocity_V=30.0
	Espuma2.Time2Live=10


def BorrarCascada(cascada):
	cascada = Bladex.GetEntity(cascada)
	cascada.SubscribeToList("Pin")
	
	Espuma2 = Bladex.GetEntity(cascada+"Espuma2")
	Espuma2.SubscribeToList("Pin")
	
	#FUENTE VIDA

###chorro1
CreateCascada("chorro1",(336418.826422,-6553.917430,125895.954788),(-300.0, 0.0, 0.0),(-2000.0, 0.0, 0.0),(335818.826422,-5400.917430,125895.954788),15)
"""
###chorro2
CreateCascada("chorro2",(294081.291655,-882.423731,117411.196938),(-300.0, 0.0, 0.0),(-2000.0, 0.0, 0.0),(293781.291655,130,118311.196938),15)
"""