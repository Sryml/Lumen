#########################################################
#														#
# Los malotes que salen en la plaza (3 grupos de malos)	#
#														#
# (Yuio)												#
#														#
#########################################################

import Reference
import Select
import Doors
import Change
import Actions
import EnemyTypes
import LevelFuncs
#import AniSound
import Sparks
from math import pow

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 1
expected_player_lvl_max= 6
lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)

tunnelAGroupOut =0
tunnelBGroupOut =0
EnemyGroupsOut=0

orksInScene = 0





o=Bladex.CreateEntity("MineEspadaromana18","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("MineEsc18kgt","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("18orc","Ork",-34515.5005822, -31054.9340439, -4962.07,"Person")
pers.Angle=3.71852209359
pers.Level=lvl_control.GiveLevel(3,6)
Actions.TakeObject(pers.Name,"MineEspadaromana18")
Actions.TakeObject(pers.Name,"MineEsc18kgt")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup("18orc", "plataf")
pers.SetOnFloor()
#AniSound.AsignarSonidosCaballeroTraidor(pers.Name)
orksInScene=orksInScene+1

#caballero 18b

o=Bladex.CreateEntity("MineEspadaromana18b","Orksword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("MineEsc18bkgt","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("18borc","Great_Ork",-41741.6497465, -31110.3650603, -37553.024,"Person")
pers.Angle=0.06
pers.Level=lvl_control.GiveLevel(2,3)
Actions.TakeObject(pers.Name,"MineEspadaromana18b")
Actions.TakeObject(pers.Name,"MineEsc18bkgt")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup("18borc", "plataf")
pers.SetOnFloor()
#AniSound.AsignarSonidosCaballeroTraidor(pers.Name)
orksInScene=orksInScene+1

#caballero 18c

o=Bladex.CreateEntity("MineEspadaromana18c","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("MineEsc18ckgt","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("18corc","Ork",-42903.9764533, -31067.0198168, -26437.577,"Person")
pers.Angle=5.8
pers.Level=lvl_control.GiveLevel(4,6)
Actions.TakeObject(pers.Name,"MineEspadaromana18c")
Actions.TakeObject(pers.Name,"MineEsc18ckgt")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup("18corc", "plataf")
pers.SetOnFloor()
orksInScene=orksInScene+1

#AniSound.AsignarSonidosCaballeroTraidor(pers.Name)



	
tunnelASector=Bladex.GetSector(-53000,-28000,-20500)
tunnelASector.OnEnter=tunnelACheck

tunnelBSector=Bladex.GetSector(-51750,-28000,-34500)
tunnelBSector.OnEnter=tunnelBCheck

tunnelCSector=Bladex.GetSector(-29000, -31000, -8000)
tunnelCSector.OnEnter=tunnelCCheck


darfuncs.HideBadGuy("18orc")
darfuncs.HideBadGuy("18borc")
darfuncs.HideBadGuy("18corc")