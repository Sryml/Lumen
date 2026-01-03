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
import persPath

# char.Position = -2500,-33000,24625
##############################################################################################3
## DEFINICION DE LOS 3 MANDRILES ESTOS

sksAxeA=Bladex.CreateEntity("sksAxeA","Espadacurva",0,0,0)
sksAxeA.Weapon=1
sksShieldA=Bladex.CreateEntity("sksShieldA","Escudo4",0,0,0)
Sparks.MakeShield("sksShieldA")
Breakings.SetBreakableWS("sksShieldA")
#Breakings.SetBreakableWS("sksAxeA") 
sksSkeletonA=Bladex.CreateEntity("sksSkeletonA","Skeleton",3750,-33000,17125 )  
sksSkeletonA.Person=1
sksSkeletonA.Angle=4.58605574849
sksSkeletonA.Level=15
#sksSkeletonA.ActionAreaMin=pow(2,15)
#sksSkeletonA.ActionAreaMax=pow(2,0)
Actions.TakeObject(sksSkeletonA.Name,"sksAxeA")
Actions.TakeObject(sksSkeletonA.Name,"sksShieldA")
EnemyTypes.EnemyDefaultFuncs(sksSkeletonA)
#AniSound.AsignarSonidosOrco("sksSkeletonA")
sksSkeletonA.Blind=1
sksSkeletonA.Deaf=1

sksAxeB=Bladex.CreateEntity("sksAxeB","Espadacurva",0,0,0)
sksAxeB.Weapon=1
sksShieldB=Bladex.CreateEntity("sksShieldB","Escudo4",0,0,0)
Sparks.MakeShield("sksShieldB")
Breakings.SetBreakableWS("sksShieldB")
#Breakings.SetBreakableWS("sksAxeB") 
sksSkeletonB=Bladex.CreateEntity("sksSkeletonB","Skeleton",3250,-33000,18250)
sksSkeletonB.Person=1
sksSkeletonB.Angle=4.58605574849
sksSkeletonB.Level=14
#sksSkeletonB.ActionAreaMin=pow(2,15)
#sksSkeletonB.ActionAreaMax=pow(2,0)
Actions.TakeObject(sksSkeletonB.Name,"sksAxeB")
Actions.TakeObject(sksSkeletonB.Name,"sksShieldB")
EnemyTypes.EnemyDefaultFuncs(sksSkeletonB)
#AniSound.AsignarSonidosOrco("sksSkeletonB")
sksSkeletonB.Blind=1
sksSkeletonB.Deaf=1

sksAxeC=Bladex.CreateEntity("sksAxeC","Espadacurva",0,0,0)
sksAxeC.Weapon=1
sksShieldC=Bladex.CreateEntity("sksShieldC","Escudo4",0,0,0)
Sparks.MakeShield("sksShieldC")
Breakings.SetBreakableWS("sksShieldC")
#Breakings.SetBreakableWS("sksAxeC") 
sksSkeletonC=Bladex.CreateEntity("sksSkeletonC","Skeleton",3000,-33000,19625)
sksSkeletonC.Person=1
sksSkeletonC.Angle=4.58605574849
sksSkeletonC.Level=15
#sksSkeletonC.ActionAreaMin=pow(2,15)
#sksSkeletonC.ActionAreaMax=pow(2,0)
Actions.TakeObject(sksSkeletonC.Name,"sksAxeC")
Actions.TakeObject(sksSkeletonC.Name,"sksShieldC")
EnemyTypes.EnemyDefaultFuncs(sksSkeletonC)
#AniSound.AsignarSonidosOrco("sksSkeletonC")
sksSkeletonC.Blind=1
sksSkeletonC.Deaf=1


sksStarted=0

sksSec =  Bladex.GetSector(-25000,-35000,25000)
sksSec.OnEnter = sksStart




