import math

Bladex.AddParticleGType("AguaC","WaterParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	r=150
	g=170
	b=170
	a=40
	size=500.0
	Bladex.SetParticleGVal("AguaC",i,r,g,b,a,size)

Bladex.AddParticleGType("Espuma","SmokeParticle",B_PARTICLE_GTYPE_BLEND,10)

for i in range(10):
	aux=(10.0-i)/10.0
	r=200
	g=200
	b=200
	#a=255*math.sqrt(1.0-aux)
	a=255
	size=1400.0*math.sqrt(1.0-aux)
	Bladex.SetParticleGVal("Espuma",i,r,g,b,a,size)


#char.Position = -45250, 2000,-30000


###primera cascada  del rio

CreateCascada("Cascada1",(-169250,2500,-79750),(2500.0, 0.0, 2000.0),(5000.0, 0.0, -6000.0),(-167000,6800,-82500),23)

CreateCascada("Cascada2",(-165500,2500,-77000),(2500.0, 0.0, 2000.0),(5000.0, 0.0, -6000.0),(-164000,6800,-79250),23)


####cascada gorda al final del rio

CreateCascada("Cascada3",(-215250,-5000,217000),(-3250, 0, 500),(1000.0, 3000.0, -16000.0),(-214500,3800,208250),30)

CreateCascada("Cascada4",(-220000,-5000,218000),(-2600, 0, 350),(2000.0, 3000.0, -17000.0),(-219000,3500,210000),30)