import Bladex
import AuxFuncs
import EnemyTypes
import Sparks
import Actions
import math
import Breakings
import darfuncs
import Enm_Gen
import LevelFuncs

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 12
expected_player_lvl_max= 16

lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)



######################
#     Particulas     #
######################

Bladex.AddParticleGType("PolvoNieve","SmokeParticle2",B_PARTICLE_GTYPE_BLEND,64)

for i in range(64):
	aux=(64.0-i)/64.0
	r=255
	g=255
	b=255
	a=255.0*(1.0-aux)**0.5
	size=80.0+aux*400.0
	Bladex.SetParticleGVal("PolvoNieve",i,r,g,b,a,size)


Bladex.AddParticleGType("Nievecilla","GenericParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	aux=(60-i)/60
	r=255
	g=255
	b=255
	a=150*(1.0-aux/2.0)
	size=60.0*(1.0-aux)
	Bladex.SetParticleGVal("Nievecilla",i,r,g,b,a,size)



###################################################
#     Funciones complementarias del generador     #
###################################################

######## Funcion: RemueveNieveGen(gen_pos, v1, v2, v3)

######## Funcion: SaltaNieveGen(gen_pos)



###############################################
#     Generadores explanada fortificacion     #
###############################################

######## Funcion: ZombieListo(person)

######## Funcion: LevantaZombieExplanada(person, gen_pos)

######## Funcion: ZombiesExplanada(tr_sector, ent_name)

Bladex.SetTriggerSectorFunc("Explanada", "OnEnter", ZombiesExplanada)



#############################
#     Restos de batalla     #
#############################

darfuncs.MuertoyTroceado(23000, -33500, 59000, "Knight_Traitor", "CrushBo", (1,), 3.0*3.14159/4.0)
#armamuertoexpl1=Bladex.CreateEntity("OrlokArmaMuertoExpl1", "Espadaromana", 0, 0, 0, "Weapon")
#ItemTypes.ItemDefaultFuncs(armamuertoexpl1)
#muertoexpl1=Bladex.CreateEntity("OrlokMuertoExpl1", "Knight_Traitor", 23000, -33500, 59000, "Person")
#muertoexpl1.Angle=3.0*3.14159/4.0
#muertoexpl1.SetOnFloor()
#Actions.TakeObject(muertoexpl1.Name, armamuertoexpl1.Name)
#EnemyTypes.EnemyDefaultFuncs(muertoexpl1)

darfuncs.MuertoyTroceado(26500, -33500, 58000, "Knight_Traitor", "Espadaromana", (1,), 3.14159)
#armamuertoexpl2=Bladex.CreateEntity("OrlokArmaMuertoExpl2", "Espadaromana", 0, 0, 0, "Weapon")
#ItemTypes.ItemDefaultFuncs(armamuertoexpl2)
#muertoexpl2=Bladex.CreateEntity("OrlokMuertoExpl2", "Knight_Traitor", 26500, -33500, 58000, "Person")
#muertoexpl2.Angle=3.14159
#muertoexpl2.SetOnFloor()
#Actions.TakeObject(muertoexpl2.Name, armamuertoexpl2.Name)
#EnemyTypes.EnemyDefaultFuncs(muertoexpl2)

######## Funcion: MuertosExplanada()

#Bladex.AddScheduledFunc(Bladex.GetTime()+24.0, MuertosExplanada, ())



####################
#     Enemigos     #
####################


# 3 zombies en el valle interior secreto. Areas de accion 3 y 4.

generador1=Enm_Gen.CreateEnemiesGenerator(-58500.0, -35350.0, 45000.0, "TSGenerador1", 1, ("OrlokGen1Lich", "Lich", "Martillo", 0, "Escudo1", 0, lvl_control.GiveLevel(7,10)), "Lch_appears1")
generador1.InitGenFunc=SaltaNieveGen
generador1.InitGenArgs=(generador1.Position, 1)
generador1.Activate()

generador2=Enm_Gen.CreateEnemiesGenerator(-55500.0, -35350.0, 49500.0, "TSGenerador2", 1, ("OrlokGen2Lich", "Lich", "", 0, "", 0, lvl_control.GiveLevel(9,13)), "Lch_appears1")
generador2.InitGenFunc=SaltaNieveGen
generador2.InitGenArgs=(generador2.Position, 0)
generador2.Activate()

generador3=Enm_Gen.CreateEnemiesGenerator(-48000.0, -35350.0, 49000.0, "TSGenerador3", 1, ("OrlokGen3Lich", "Lich", "Hacha3", 0, "Escudo1", 0, lvl_control.GiveLevel(8,11)), "Lch_appears1")
generador3.InitGenFunc=SaltaNieveGen
generador3.InitGenArgs=(generador3.Position, 0)
generador3.Activate()

for n in range(3):
	enemigo=Bladex.GetEntity("OrlokGen"+`n+1`+"Lich1")
	enemigo.ActionAreaMin=math.pow(2,2)
	enemigo.ActionAreaMax=math.pow(2,3)


# 3 zombies en la explanada de la fortificacion. Areas de accion 13 y 14.

for n in range(3):
	enemigo=Bladex.CreateEntity("OrlokZombieExpl"+`n+1`, "Lich", 0, 0, 0, "Person")
	enemigo.Angle=0.0
	if n==1:
		arma=Bladex.CreateEntity("OrlokArmaZombieExpl"+`n+1`, "Martillo", 0, 0, 0, "Weapon")
		ItemTypes.ItemDefaultFuncs(arma)
		Actions.TakeObject(enemigo.Name, arma.Name)
		escudo=Bladex.CreateEntity("OrlokEscudoZombieExpl"+`n+1`, "Escudo2", 0, 0, 0, "Weapon")
		ItemTypes.ItemDefaultFuncs(escudo)
		Actions.TakeObject(enemigo.Name, escudo.Name)
	enemigo.ActionAreaMin=math.pow(2,12)
	enemigo.ActionAreaMax=math.pow(2,13)
	enemigo.Level=lvl_control.GiveLevel(8,12)
	EnemyTypes.EnemyDefaultFuncs(enemigo)
	enemigo.Blind=1
	enemigo.Deaf=1
	enemigo.Freeze()
	enemigo.RemoveFromWorldWithChilds()
