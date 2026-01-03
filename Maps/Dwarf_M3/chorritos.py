import Sounds
import Bladex
import math

Bladex.AddParticleGType("AguaC","WaterParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	r=60
	g=60
	b=60
	a=60
	size=120.0
	Bladex.SetParticleGVal("AguaC",i,r,g,b,a,size)

Bladex.AddParticleGType("Espuma","SmokeParticle",B_PARTICLE_GTYPE_BLEND,10)

for i in range(10):
	aux=(10.0-i)/10.0
	r=70
	g=70
	b=70
	#a=255*math.sqrt(1.0-aux)
	a=255
	size=600.0*math.sqrt(1.0-aux)
	Bladex.SetParticleGVal("Espuma",i,r,g,b,a,size)


#char.Position = -45250, 2000,-30000


#FUENTE de frente

###chorro1
CreateCascada("chorro1",(-249290 ,-20801 ,62400 ),(200.0, 0.0, 0.0),(0.0, -1000.0, -2000.0),(-249290,-19500 ,61500),15)

#v1=Bladex.CreateSound("../../Sounds/agua-canal.wav","v1")
#v1.MaxDistance=15000
#v1.MinDistance=2000
#v1.Volume=1
#v1.BaseVolume=1.0
#v1.SendNotify=0
#v1.Play(-249290 ,-20801 ,62400,-1)



###chorro2
CreateCascada("chorro2",(-257100,-20660,54580),( 0, 250, 0 ),(2000.0, -1000.0, 0.0),(-256500,-19500,54580),15)

#v2=Bladex.CreateSound("../../Sounds/agua-canal.wav","v2")
#v2.MaxDistance=15000
#v2.MinDistance=2000
#v2.Volume=1.0
#v2.BaseVolume=1.0
#v2.SendNotify=0
#v2.Play(-256500,-19500,54580,-1)
