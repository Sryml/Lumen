import Bladex
import Enm_Gen
import B3DLib




######################
#     Particulas     #
######################

Bladex.AddParticleGType("Tierra2","SmokeParticle",B_PARTICLE_GTYPE_BLEND,64)

for i in range(64):
	aux=(64.0-i)/64.0
	r=210
	g=190
	b=140
	a=255.0*(1.0-aux)**0.5
	size=80.0+aux*400.0
	Bladex.SetParticleGVal("Tierra2",i,r,g,b,a,size)


Bladex.AddParticleGType("Tierra2sub","SmokeParticle",B_PARTICLE_GTYPE_BLEND,64)

for i in range(64):
	aux=(64.0-i)/64.0
	r=200
	g=140
	b=100
	a=255.0*(1.0-aux)**0.5
	size=80.0+aux*400.0
	Bladex.SetParticleGVal("Tierra2sub",i,r,g,b,a,size)


Bladex.AddParticleGType("Tierra3","GenericParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	aux=(60-i)/60
	r=40
	g=30
	b=0
	a=255*(1.0-aux/2.0)
	size=60.0*(1.0-aux)
	Bladex.SetParticleGVal("Tierra3",i,r,g,b,a,size)


###################################################
#     Funciones complementarias del generador     #
###################################################

######## Funcion: RemueveTierraGen(pos, v1, v2, v3)

######## Funcion: SaltaTierraGen(enmgen)


#######################
#     Generadores     #
#######################

generador1=Enm_Gen.CreateEnemiesGenerator(-21000.0, 1000.0, -7000.0, "Generador1", 4, ("Gen1Skl", "Skeleton", "Hacha", 0, "Escudo2", 1), "Skl_appears1")
generador1.InitGenFunc=SaltaTierraGen
generador1.InitGenArgs=(generador1,)
#generador1.Activate()

generador2=Enm_Gen.CreateEnemiesGenerator(-60000.0, 1000.0, -8000.0, "Generador2", 4, ("Gen2Skl", "Skeleton", "Maza", 0, "Escudo5", 1), "Skl_appears1")
generador2.InitGenFunc=SaltaTierraGen
generador2.InitGenArgs=(generador2,)
#generador2.Activate()

generador3=Enm_Gen.CreateEnemiesGenerator(-1000.0, 1000.0, 58000.0, "Generador3", 4, ("Gen3Skl", "Skeleton", "Hacha", 0, "Escudo5", 1), "Skl_appears1")
generador3.InitGenFunc=SaltaTierraGen
generador3.InitGenArgs=(generador3,)
#generador3.Activate()

generador4=Enm_Gen.CreateEnemiesGenerator(13500.0, 1000.0, 20000.0, "Generador4", 4, ("Gen4Skl", "Skeleton", "Garrote", 0, "Escudo5", 1), "Skl_appears1")
generador4.InitGenFunc=SaltaTierraGen
generador4.InitGenArgs=(generador4,)
#generador4.Activate()

generador5=Enm_Gen.CreateEnemiesGenerator(13500.0, 1000.0, -20000.0, "Generador5", 4, ("Gen5Skl", "Skeleton", "Garrote", 0, "Escudo2", 1), "Skl_appears1")
generador5.InitGenFunc=SaltaTierraGen
generador5.InitGenArgs=(generador5,)
#generador5.Activate()

generador6=Enm_Gen.CreateEnemiesGenerator(-14000.0, 1000.0, -58000.0, "Generador6", 4, ("Gen6Skl", "Skeleton", "Maza", 0, "Escudo5", 1), "Skl_appears1")
generador6.InitGenFunc=SaltaTierraGen
generador6.InitGenArgs=(generador6,)
#generador6.Activate()


### Generadores de las catacumbas

######## Funcion: SetAreas2728(enm)

######## Funcion: SetAreas2930(enm)

# Areas 27 y 28

generador7a=Enm_Gen.CreateEnemiesGenerator(56000.0, 8500.0, -8500.0, "Generador7a", 1, ("Gen7aSkl", "Lich", "Hacha", 0, "", 0), "Lch_appears1", SetAreas2728)
generador7a.InitGenFunc=SaltaTierraGen
generador7a.InitGenArgs=(generador7a,)
generador7a.Activate()

generador7b=Enm_Gen.CreateEnemiesGenerator(48000.0, 8500.0, -15000.0, "Generador7b", 1, ("Gen7bSkl", "Lich", "", 0, "", 0), "Lch_appears1", SetAreas2728)
generador7b.InitGenFunc=SaltaTierraGen
generador7b.InitGenArgs=(generador7b,)
generador7b.Activate()

# Areas 29 y 30

generador8a=Enm_Gen.CreateEnemiesGenerator(36000.0, 10000.0, -56000.0, "Generador8a", 1, ("Gen8aSkl", "Lich", "Garrote", 0, "", 0), "Lch_appears1", SetAreas2930)
generador8a.InitGenFunc=SaltaTierraGen
generador8a.InitGenArgs=(generador8a,)
generador8a.Activate()

generador8b=Enm_Gen.CreateEnemiesGenerator(34000.0, 10000.0, -52000.0, "Generador8b", 1, ("Gen8bSkl", "Lich", "", 0, "", 0), "Lch_appears1", SetAreas2930)
generador8b.InitGenFunc=SaltaTierraGen
generador8b.InitGenArgs=(generador8b,)
generador8b.Activate()
