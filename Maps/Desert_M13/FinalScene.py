import EnmGenRnd
import Bladex
import AuxFuncs
import LevelFuncs

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 9
expected_player_lvl_max= 16

lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)

#
#Glm_appear_desert01.bmv (-138109,19444,-4496)
#
#Glm_appear_desert02.bmv (-138109,3270,-4496)
#
#
#C�maras:
#
#Final_desierto2Golemcamara01	0-200


GolemsMuertos = 0

_SoundTemblorFatidico=Bladex.CreateSound("../../Sounds/derrumbe2.wav","SoundTemblorFatidico")
_SoundTemblorFatidico.MinDistance= 80000
_SoundTemblorFatidico.MaxDistance=100000
_SoundTemblorFatidico.Volume = 1


#golemfinal1 = EnmGenRnd.CreateEnemy((-137109,4496,19444),"GolemFinal1", "Golem_stone", "", 0, "", 0)
#golemfinal2 = EnmGenRnd.CreateEnemy((-137109,4496,3270),"GolemFinal2", "Golem_stone", "", 0, "", 0)

#golemfinal1.ImDeadFunc = GolemFinalMuerto
#golemfinal2.ImDeadFunc = GolemFinalMuerto



FinDesert1 = Bladex.GetSector(-129000,0,11000)
FinDesert1.OnEnter = ActivateFinalDesert

FinDesert2 = Bladex.GetSector(-126000,0,2000)
FinDesert2.OnEnter = ActivateFinalDesert

FinDesert3 = Bladex.GetSector(-126000,0,21000)
FinDesert3.OnEnter = ActivateFinalDesert


###ROCAS



#	o=Bladex.CreateEntity("DER3","Roca1",-109985.680000,7149.424000,-3851.826000,"Physic")
#	o.Scale=1.909366
#	o.Orientation=0.008536,-0.978110,-0.207904,-0.001814


#	o=Bladex.CreateEntity("DER2","Roca1",-112665.369000,5693.222000,-6579.507000,"Physic")
#	o.Scale=2.238882
#	o.Orientation=0.079484,-0.756240,0.067886,-0.645890


#	o=Bladex.CreateEntity("DER1","Roca2",-113955.369000,9145.504000,-2542.603000,"Physic")
#	o.Scale=1.082857
#	o.Orientation=0.026177,-0.999657,0.000000,0.000000



pers=Bladex.CreateEntity("GolemMalo1","Golem_stone",-137109,4496,19444,"Person")
pers.Angle=-3.14159/2.0
pers.Level=lvl_control.GiveLevel(6,9)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
pers.ImDeadFunc = GolemFinalMuerto
darfuncs.HideBadGuy("GolemMalo1")


pers=Bladex.CreateEntity("GolemMalo2","Golem_stone",-137109,4496,3270,"Person")
pers.Angle=-3.14159/2.0
pers.Level=lvl_control.GiveLevel(6,9)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
pers.ImDeadFunc = GolemFinalMuerto
darfuncs.HideBadGuy("GolemMalo2")


o=Bladex.CreateEntity("GolemTrucho1","EstatuaGolem",-137109,4496,19444)
o.Scale=1.000000
o.Orientation=0.495699197054, 0.495699167252, -0.504264116287, 0.504264116287


o=Bladex.CreateEntity("GolemTrucho2","EstatuaGolem",-137109,4496,3270)
o.Scale=1.000000
o.Orientation=0.495699197054, 0.495699167252, -0.504264116287, 0.504264116287


derrumbemuroagua=Bladex.CreateSound("../../Sounds/impact-watersplash.wav", "DerrumbeMuroAgua")
derrumbemuroagua.Volume=1
derrumbemuroagua.MinDistance=50000
derrumbemuroagua.MaxDistance=400000