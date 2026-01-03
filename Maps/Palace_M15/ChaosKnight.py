import Bladex
import EnemyTypes
import Damage
import math
import Sounds
import Reference
import Select
import Change
import Actions
import B3DLib
import OnInitTake
import GameText
import Scorer
import Sparks
import EnemyTypes
import Interpolator
import ConcenEf
import darfuncs

##################################################################################
############# portones que se abren al morir el caballero del caos################
##################################################################################

kSceneOpenDoorsTime=20.0
kSceneOpenDoorsPrec=0.025

kaosdoor1=Bladex.CreateEntity("kaosdoor1","PuertaFernando",90799.356000,-11900.780000,195045.357000)
kaosdoor1.Static=0
kaosdoor1.Scale=1.000000
kaosdoor1.Orientation=0.707107,0.707107,0.000000,0.000000

kaosdoor2=Bladex.CreateEntity("kaosdoor2","PuertaFernando",97874.461000,-11900.776000,195087.409000)
kaosdoor2.Static=0
kaosdoor2.Scale=1.000000
kaosdoor2.Orientation=0.000000,0.000000,0.707107,-0.707107

Bladex.CreateTimer("kaosdoortimer",kSceneOpenDoorsPrec)
kSceneOpenDoorsStartTime=0.0



#######################
#     Preparacion     #
#######################


chaosk1=Bladex.CreateEntity("ChaosK1", "ChaosKnight", 94631.1636238, -1934.6, 215856.809821)
chaosk1.Person=1
chaosk1.Angle=0
chaosk1.Level=9
EnemyTypes.EnemyDefaultFuncs(chaosk1)
chaosk1.Blind=1
chaosk1.Deaf=1
#chaosk1.Life=1000
chaosk1.DamageFunc=ChaosDamage

chaosk1.Data.DamageFactorNone=0.15
chaosk1.Data.DamageFactorLight=0.35
chaosk1.Data.DamageFactorHeavy=0.35
chaosk1.Data.PrepareWeapons("Espadon", "Escudon")
chaosk1.Data.PrepareDisappearance()
chaosk1.SetOnFloor()
darfuncs.HideBadGuy(chaosk1.Name)



####################
#     Acciones     #
####################


sectorcamarachk=Bladex.GetSector(85300.0805598, -2284.6, 239120.168188)

sectorcamarachk.OnEnter=MueveCamaraChk

TOTAL_TIME=8.0
TOTAL_STEPS=TOTAL_TIME*60.0
ANGLE_VARIATION=2.0*3.14159/TOTAL_STEPS


chaosk1.ImDeadFunc=MuereChaosK1

