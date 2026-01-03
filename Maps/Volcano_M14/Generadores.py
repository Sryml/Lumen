import Bladex
import Enm_Gen
import AuxFuncs
import ReadGSFile
import LevelFuncs

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 12
expected_player_lvl_max= 16

lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)

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
	g=90
	b=40
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

generador1=Enm_Gen.CreateEnemiesGenerator(-7250, 10050, 33500, "SKL1", 3, ("ENSKL1", "Skeleton", "HookSword", 0, "Escudo2", 1, lvl_control.GiveLevel(6,10)), "Skl_appears1")
generador1.InitGenFunc=SaltaTierraGen
generador1.InitGenArgs=(generador1,)
generador1.Activate()

generador2=Enm_Gen.CreateEnemiesGenerator(-13000.0, 10005, 28000, "SKL2", 2, ("ENSKL2", "Skeleton", "Espadacurva", 0, "Escudo2", 1, lvl_control.GiveLevel(7,11)), "Skl_appears1")
generador2.InitGenFunc=SaltaTierraGen
generador2.InitGenArgs=(generador2,)
generador2.Activate()

generador3=Enm_Gen.CreateEnemiesGenerator(-10000.0, 10005, 30000, "SKL2", 1, ("ENSKL3", "Skeleton", "Espadacurva", 0, "Escudo1", 1, lvl_control.GiveLevel(8,12)), "Skl_appears1")
generador3.InitGenFunc=SaltaTierraGen
generador3.InitGenArgs=(generador3,)
generador3.Activate()