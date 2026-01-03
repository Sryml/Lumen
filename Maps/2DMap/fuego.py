import Bladex
import math

###   FUEGOS
"""
#1
Lucex=Bladex.CreateEntity("hkgfoweua","Entity Spot",-27750, -43800, -8750)
Lucex.Color=251,59,7
Lucex.Intensity=6
Lucex.Precission=0.1
Lucex.CastShadows=1
Lucex.Visible=0
Lucex.Flick=1

towFire=Bladex.CreateEntity("cyioj", "Entity Particle System D1", -28000, -44000, -9000)
towFire.ParticleType="LargeFire"
towFire.YGravity=-2000.0
towFire.Friction=0.12
towFire.PPS=100
towFire.Velocity= 0.0, -500.0, 0.0
towFire.Time2Live=32
towFire.RandomVelocity=40
"""

#############################################################################################
###	LUCES CON HUMO ROJO


####	SISTEMA DE PARTICULAS	###############

Bladex.AddParticleGType("HumoRojo","SmokeParticle",B_PARTICLE_GTYPE_BLEND,50)

for i in range(50):
	aux=(50.0-i)/50.0
	r=150
	g=150
	b=150
	a=250
	size=1000.0*math.sqrt(1.0-aux)
	Bladex.SetParticleGVal("HumoRojo",i,r,g,b,a,size)
	
	
####	mapa enanos
#1
kazelzalam=Bladex.CreateEntity("kazelzalam", "Entity Particle System D1", -99963.620000,14950,-1505.120000)
kazelzalam.ParticleType="HumoRojo"
kazelzalam.YGravity=-3000.0
kazelzalam.Friction=0.12
kazelzalam.PPS=25
kazelzalam.Velocity= 0.0, -100.0, 0.0
kazelzalam.Time2Live=50
kazelzalam.RandomVelocity=40


