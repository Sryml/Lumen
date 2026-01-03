import math

Bladex.AddParticleGType("AguaC","WaterParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	r=90
	g=100
	b=100
	a=60
	size=80.0
	Bladex.SetParticleGVal("AguaC",i,r,g,b,a,size)

Bladex.AddParticleGType("Espuma","SmokeParticle",B_PARTICLE_GTYPE_BLEND,10)

for i in range(10):
	aux=(10.0-i)/10.0
	r=90
	g=90
	b=90
	#a=255*math.sqrt(1.0-aux)
	a=255
	size=500.0*math.sqrt(1.0-aux)
	Bladex.SetParticleGVal("Espuma",i,r,g,b,a,size)


#char.Position = -45250, 2000,-30000


#FUENTE VIDA

###chorro1
CreateCascada("chorro1",(6875,-2000,-2125),(250.0, 0.0, 0.0),(0.0, -1000.0, -2000.0),(6875,-1100,-2635),15)

###chorro2
CreateCascada("chorro2",(8875,-2000,-2125),(250.0, 0.0, 0.0),(0.0, -1000.0, -1700.0),(8875,-900,-2635),15)

#FUENTE VENENO

###chorro3
CreateCascada("chorro3",(-55312,-1650,-21875),(125.0, 0.0, 0.0),(0.0, -500.0, 1000.0),(-55312,-800,-21500),12)



###chorro4
CreateCascada("chorro4",(-52937,-1650,-21875),(125.0, 0.0, 0.0),(0.0, -500.0, 1000.0),(-52937,-700,-21500),12)


##  AGUA SULFUROSA PARA EL ALTAR

CreateEspuma("espuma1",(6800,500,-22500),(525.0, 0.0, 0.0),20)
CreateEspuma("espuma2",(9250,400,-23800),(525.0, 0.0, 300.0),20)
CreateEspuma("espuma3",(8800,300,-25500),(125.0, 0.0, 100.0),30)
CreateEspuma("espuma4",(8000,400,-23500),(125.0, 0.0, 200.0),10)