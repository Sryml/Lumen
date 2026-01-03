

Bladex.AddParticleGType("AguaCpi","WaterParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	r=70
	g=70
	b=70
	a=60
	size=250.0
	Bladex.SetParticleGVal("AguaCpi",i,r,g,b,a,size)

Bladex.AddParticleGType("Espumapi","SmokeParticle",B_PARTICLE_GTYPE_BLEND,10)

for i in range(10):
	aux=(10.0-i)/10.0
	r=75
	g=70
	b=70
	#a=255*math.sqrt(1.0-aux)
	a=200
	size=1300.0*math.sqrt(1.0-aux)
	Bladex.SetParticleGVal("Espumapi",i,r,g,b,a,size)


####	Fuente dentro del pueblo

CreateCascada("Cascadai4",(-191500,-17500,223000),(1500.0, 0.0, 2500.0),(5000.0, 0.0, -6000.0),(-190000,-15600,220500),20)


###dentro de la gruta en el camino alternativo

CreateCascada("Cascadai1",(-40500,-650,-21000),(1250.0, 0.0, -4500.0),(-4300.0, 0.0, -2250.0),(-42500,1800,-22000))