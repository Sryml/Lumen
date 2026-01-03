

Bladex.AddParticleGType("AguaCi","WaterParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	r=75
	g=80
	b=80
	a=70
	size=450.0
	Bladex.SetParticleGVal("AguaCi",i,r,g,b,a,size)

Bladex.AddParticleGType("Espumai","SmokeParticle",B_PARTICLE_GTYPE_BLEND,10)

for i in range(10):
	aux=(10.0-i)/10.0
	r=100
	g=105
	b=105
	#a=255*math.sqrt(1.0-aux)
	a=255
	size=1400.0*math.sqrt(1.0-aux)
	Bladex.SetParticleGVal("Espumai",i,r,g,b,a,size)




##dentro de la gruta en el camino alternativo

CreateCascada("Cascadai1",(-40500,-650,-21000),(1250.0, 0.0, -4500.0),(-4300.0, 0.0, -2250.0),(-42500,1800,-22000))

####cascada gorda en el interior de la gruta

CreateCascada("Cascadai2",(-5000,-7000,-65250),(200.0, 0.0, 2650.0),(-6000.0, 0.0, 500.0),(-8500,-400,-64000),30)

CreateCascada("Cascadai3",(-4750,-7000,-61275),(120.0, 0.0, 1850.0),(-6000.0, 0.0, 500.0),(-8000,-1000,-61000),30)


