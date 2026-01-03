import Bladex
import math

Bladex.AddParticleGType("AguaC","WaterParticle",1,60)

for i in range(60):
	r=50
	g=50
	b=40
	a=100
	size=120.0
	Bladex.SetParticleGVal("AguaC",i,r,g,b,a,size)

Bladex.AddParticleGType("Espuma","SmokeParticle",1,10)

for i in range(10):
	aux=(10.0-i)/10.0
	r=90
	g=90
	b=100
	#a=255*math.sqrt(1.0-aux)
	a=150
	size=800.0*math.sqrt(1.0-aux)
	Bladex.SetParticleGVal("Espuma",i,r,g,b,a,size)


#char.Position = -45250, 2000,-30000

###primera cascada  del rio
CreateCascada2("Cascada1",(-80000,9000,62000),(1250.0, 0.0, 0.0),(0.0, 0.0, 1.0),(-80000,15800,62000),33)
