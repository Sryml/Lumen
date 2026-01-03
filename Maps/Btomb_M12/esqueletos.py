

import Bladex
import Enm_Gen
import B3DLib
import ReadGSFile
import LevelFuncs

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 7
expected_player_lvl_max= 16

lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)

######################
#     Particulas     #
######################

Bladex.AddParticleGType("Tierra2","SmokeParticle",B_PARTICLE_GTYPE_BLEND,64)

for i in range(64):
	aux=(64.0-i)/64.0
	r=100
	g=100
	b=100
	a=255.0*(1.0-aux)**0.5
	size=80.0+aux*400.0
	Bladex.SetParticleGVal("Tierra2",i,r,g,b,a,size)


Bladex.AddParticleGType("Tierra3","GenericParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	aux=(60-i)/60
	r=100
	g=100
	b=100
	a=255*(1.0-aux/2.0)
	size=60.0*(1.0-aux)
	Bladex.SetParticleGVal("Tierra3",i,r,g,b,a,size)




Rres = ReadGSFile.ReadGhostSectorFile("eskeletos.sf")

for igs in Rres:
   Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

#######################
#     Generadores     #
#######################

generador1=Enm_Gen.CreateEnemiesGenerator(449898, 49373+2000, 29092, "generador1", 1, ("BtombGen1Skl", "Skeleton", "HookSword", 0, "Escudo1", 1, lvl_control.GiveLevel(6,7)), "Skl_appears1",AsingaPropiedadesEsqueletos)
generador1.InitGenFunc=SaltaTierraGen
generador1.InitGenArgs=(generador1,)
generador1.Activate()

generador2=Enm_Gen.CreateEnemiesGenerator(477948, 52635+2000, 16613, "generador2", 1, ("BtombGen2Skl", "Skeleton", "HookSword", 0, "Escudo1", 1, lvl_control.GiveLevel(7,8)), "Skl_appears1",AsingaPropiedadesEsqueletos)
generador2.InitGenFunc=SaltaTierraGen
generador2.InitGenArgs=(generador2,)
generador2.Activate()

generador3=Enm_Gen.CreateEnemiesGenerator(446533, 51335+2000, 92675, "generador3", 1, ("BtombGen3Skl", "Skeleton", "Espadacurva", 0, "Escudo1", 1, lvl_control.GiveLevel(8,9)), "Skl_appears1",AsingaPropiedadesEsqueletos)
generador3.InitGenFunc=SaltaTierraGen
generador3.InitGenArgs=(generador3,)
generador3.Activate()

generador4=Enm_Gen.CreateEnemiesGenerator(479432, 54735+2000, 101703, "generador4", 1, ("BtombGen4Skl", "Skeleton", "Espadacurva", 0, "Escudo1", 1, lvl_control.GiveLevel(9,11)), "Skl_appears1",AsingaPropiedadesEsqueletos)
generador4.InitGenFunc=SaltaTierraGen
generador4.InitGenArgs=(generador4,)
generador4.Activate()

char = Bladex.GetEntity("Player1")
char.SendTriggerSectorMsgs = 1
