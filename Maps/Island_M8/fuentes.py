

Bladex.AddParticleGType("GUATERCL","WaterParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	r=90
	g=100
	b=100
	a=60
	size=80.0
	Bladex.SetParticleGVal("GUATERCL",i,r,g,b,a,size)

Bladex.AddParticleGType("EspumaCL","SmokeParticle",B_PARTICLE_GTYPE_BLEND,10)

for i in range(10):
	aux=(10.0-i)/10.0
	r=70
	g=80
	b=80
	#a=255*math.sqrt(1.0-aux)
	a=255
	size=700.0*math.sqrt(1.0-aux)
	Bladex.SetParticleGVal("EspumaCL",i,r,g,b,a,size)




#FUENTE VIDA

###chorro1
CreateFuente("surtidor1",(-41100,3880.9,-15600),(250.0, 0.0, 0.0),(0.0, 1000.0, 2300.0),(-41100,5800,-14500),15)

###chorro2
CreateFuente("surtidor2",(-36200,3891.4,-15614.577000),(250.0, 0.0, 0.0),(0.0, 1000.0, 2300.0),(-36200,5800,-14500),15)

