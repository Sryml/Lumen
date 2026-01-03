import Bladex
import Enm_Gen
import B3DLib
import ReadGSFile

res=ReadGSFile.ReadGhostSectorFile("generador.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

char.SendTriggerSectorMsgs=1



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


Bladex.AddParticleGType("Tierra3","GenericParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	aux=(60-i)/60
	r=40
	g=30
	b=0
	a=255*(1.0-aux/2.0)
	size=60.0*(1.0-aux)
	Bladex.SetParticleGVal("Tierra3",i,r,g,b,a,size)




#######################
#     Generadores     #
#######################

generador1=Enm_Gen.CreateEnemiesGenerator(-185500, -9500, 174000, "gzombie1", 3, ("Gen1Skl", "Skeleton", "Hacha", 0, "Escudo1", 1), "Skl_appears1")
generador1.InitGenFunc=SaltaTierraGen
generador1.InitGenArgs=(generador1,)
generador1.Activate()

generador2=Enm_Gen.CreateEnemiesGenerator(-170000, -11500, 192000, "gzombie2", 2, ("Gen2Skl", "Skeleton", "Hacha", 0, "Escudo1", 1), "Skl_appears1")
generador2.InitGenFunc=SaltaTierraGen
generador2.InitGenArgs=(generador2,)
generador2.Activate()

generador3=Enm_Gen.CreateEnemiesGenerator(-164000, -11500, 186000, "gzombie3", 2, ("Gen3Skl", "Skeleton", "Hacha", 0, "Escudo1", 1), "Skl_appears1")
generador3.InitGenFunc=SaltaTierraGen
generador3.InitGenArgs=(generador3,)
generador3.Activate()

generador4=Enm_Gen.CreateEnemiesGenerator(-175000, 5500, 127500, "gzombie4", 3, ("Gen4Skl", "Skeleton", "Hacha", 0, "Escudo1", 1), "Skl_appears1")
generador4.InitGenFunc=SaltaTierraGen
generador4.InitGenArgs=(generador4,)
generador4.Activate()

generador5=Enm_Gen.CreateEnemiesGenerator(-184000, 5500, 12500, "gzombie5", 3, ("Gen5Skl", "Skeleton", "Hacha", 0, "Escudo1", 1), "Skl_appears1")
generador5.InitGenFunc=SaltaTierraGen
generador5.InitGenArgs=(generador5,)
generador5.Activate()

generador6=Enm_Gen.CreateEnemiesGenerator(-174000, 5500, 117500, "gzombie6", 2, ("Gen6Skl", "Skeleton", "Hacha", 0, "Escudo1", 1), "Skl_appears1")
generador6.InitGenFunc=SaltaTierraGen
generador6.InitGenArgs=(generador6,)
generador6.Activate()


#######################    en exterior de las tumbas

res=ReadGSFile.ReadGhostSectorFile("EXTERIOR.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

char.SendTriggerSectorMsgs=1

generador7=Enm_Gen.CreateEnemiesGenerator(93000, -53500, 116250, "EXTSF2", 1, ("Gen7Skl", "Lich", "Hacha", 0, "Escudo1", 1), "Lch_appears1")
generador7.InitGenFunc=SaltaTierraGen
generador7.InitGenArgs=(generador7,)
generador7.Activate()

generador8=Enm_Gen.CreateEnemiesGenerator(85000, -53500, 131500, "EXTSF2", 1, ("Gen8Skl", "Lich", "Hacha", 0, "Escudo1", 1), "Lch_appears1")
generador8.InitGenFunc=SaltaTierraGen
generador8.InitGenArgs=(generador8,)
generador8.Activate()

generador9=Enm_Gen.CreateEnemiesGenerator(119250, -52500, 134750, "EXTSF3", 1, ("Gen9Skl", "Skeleton", "Hacha", 0, "Escudo1", 1), "Skl_appears1")
generador9.InitGenFunc=SaltaTierraGen
generador9.InitGenArgs=(generador9,)
generador9.Activate()

generador10=Enm_Gen.CreateEnemiesGenerator(108000, -52500, 144500, "EXTSF3", 1, ("Gen10Skl", "Skeleton", "Hacha", 0, "Escudo1", 1), "Skl_appears1")
generador10.InitGenFunc=SaltaTierraGen
generador10.InitGenArgs=(generador10,)
generador10.Activate()


