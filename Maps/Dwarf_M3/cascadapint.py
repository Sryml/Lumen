

Bladex.AddParticleGType("AguaCpi","WaterParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	r=70
	g=80
	b=90
	a=60
	size=200.0
	Bladex.SetParticleGVal("AguaCpi",i,r,g,b,a,size)

Bladex.AddParticleGType("Espumapi","SmokeParticle",B_PARTICLE_GTYPE_BLEND,10)

for i in range(10):
	aux=(10.0-i)/10.0
	r=70
	g=80
	b=90
	#a=255*math.sqrt(1.0-aux)
	a=200
	size=2000.0*math.sqrt(1.0-aux)
	Bladex.SetParticleGVal("Espumapi",i,r,g,b,a,size)


##	Fuente dentro de la gruta de inicio

CreateCascada2("Cascadai1",(52850,2000,-112500),(600.0, 0.0, 250),(250, 0.0, -1500),(53000,7900,-113500),25)


