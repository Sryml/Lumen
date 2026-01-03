##################################
#
# dos esqueletos salen de unas puertas
#
# Yuio 10-8-97
#
##################################

import Bladex
import AuxFuncs
import EnemyTypes
import Sparks
import Actions
import InitDataField
import math
import AuxFuncs
import Breakings
import Doors

############################################# SHARED FUNCS ###################################################
tsmaderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
tsmaderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


############################################### PUERTA A #######################################################


tsAxeA=Bladex.CreateEntity("TombtsAxeA","Hacha",0,0,0)
tsAxeA.Weapon=1
tsShieldA=Bladex.CreateEntity("TombtsShieldA","Escudo5",0,0,0)
Sparks.MakeShield("TombtsShieldA")
Breakings.SetBreakableWS("TombtsShieldA")


tsSkeletonA=Bladex.CreateEntity("tsSkeletonA","Skeleton",41500,-3000,46750)
tsSkeletonA.Person=1
tsSkeletonA.Level=5
tsSkeletonA.Angle=4.58605574849
Actions.TakeObject(tsSkeletonA.Name,"TombtsAxeA")
Actions.TakeObject(tsSkeletonA.Name,"TombtsShieldA")
tsSkeletonA.ActionAreaMin=pow(2,2)
tsSkeletonA.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(tsSkeletonA)
tsSkeletonA.Blind=1
tsSkeletonA.Deaf=1

tsSkeletonA.Data.ImDeadFuncPlus   = tsSkeletonA.ImDeadFunc
tsSkeletonA.ImDeadFunc = MuerteesqueletoDeMierda

tsDoorA=Doors.CreateDoor("tsDoorA", (41500,-2500,44650), (0.0,1.0,0.0), 400.0, 4100.0, Doors.CLOSED)




############################################### PUERTA B #######################################################

tsAxeB=Bladex.CreateEntity("TombtsAxeB","Hacha",0,0,0)
tsAxeB.Weapon=1
tsShieldB=Bladex.CreateEntity("TombtsShieldB","Escudo5",0,0,0)
Sparks.MakeShield("TombtsShieldB")
Breakings.SetBreakableWS("TombtsShieldB")
Breakings.SetBreakableWS("TombtsAxeB")

tsSkeletonB=Bladex.CreateEntity("tsSkeletonB","Skeleton",31500,-3000,47000)
tsSkeletonB.Person=1
tsSkeletonB.Level=5
tsSkeletonB.Angle=4.58605574849
Actions.TakeObject(tsSkeletonB.Name,"TombtsAxeB")
Actions.TakeObject(tsSkeletonB.Name,"TombtsShieldB")
tsSkeletonB.ActionAreaMin=pow(2,2)
tsSkeletonB.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(tsSkeletonB)
tsSkeletonB.Blind=1
tsSkeletonB.Deaf=1

tsSkeletonB.Data.ImDeadFuncPlus   = tsSkeletonB.ImDeadFunc
tsSkeletonB.ImDeadFunc = MuerteesqueletoDeMierda

tsDoorB=Doors.CreateDoor("tsDoorB", (31500,-2500,44650), (0.0,1.0,0.0), 400.0, 4100.0, Doors.CLOSED)

############################################### START #######################################################
tsStarted=0

tsStartSec = Bladex.GetSector(31000,-2000,32000)
tsStartSec.OnEnter = tsStart
