from math import pow
import EnemyTypes
"""
import SleepingKnights
import TalkingKnights
import BurningKnights
"""

execfile("SleepingKnights.py")
execfile("TalkingKnights.py")
#execfile("BurningKnights.py")

import Sparks
import Actions
import darfuncs
import Bladex
import Breakings
import pocimac
import AniSound


## Cositas in catacombs

pers=Bladex.CreateEntity("1cos","Cos",-152468.216339, 13251.5, 46106.5728533,"Person")
pers.Angle=1.49589570635
pers.Level=0
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.ImDeadFuncX=pers.ImDeadFunc
pers.ImDeadFunc=KnightDefeatsCos
darfuncs.HideBadGuy("1cos")
pers.SetOnFloor()

pers=Bladex.CreateEntity("2cos","Cos",-156262.592877, 12776.0072536, 44434.5921197,"Person")
pers.Angle=5.75
pers.Level=0
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.ImDeadFuncX=pers.ImDeadFunc
pers.ImDeadFunc=KnightDefeatsCos
darfuncs.HideBadGuy("2cos")
pers.SetOnFloor()


pers=Bladex.CreateEntity("4cos","Cos",-149074.713201, 7465.63351556, 26185.7401127,"Person")
pers.Angle=0.547243850511
pers.Level=0
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.ImDeadFuncX=pers.ImDeadFunc
pers.ImDeadFunc=KnightDefeatsCos
pers.SetOnFloor()
darfuncs.HideBadGuy("4cos")


sencos=Bladex.GetSector(-136750,15000,69550)
sencos.OnEnter=ApareceCosita




## Cositas in las segundas alcantarillas

pers=Bladex.CreateEntity("1cos1","Cos",-91400,2300,49600,"Person")
pers.Angle=1.49589570635
pers.Level=0
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
darfuncs.HideBadGuy("1cos1")

pers=Bladex.CreateEntity("2cos2","Cos",-92400,2300,47400,"Person")
pers.Angle=5.75
pers.Level=1
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
darfuncs.HideBadGuy("2cos2")

pers=Bladex.CreateEntity("3cos3","Cos",-97900,2300,48200,"Person")
pers.Angle=0.0532455606238
pers.Level=1
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
darfuncs.HideBadGuy("3cos3")


sencos2=Bladex.GetSector(-114394, 3885, 49000)
sencos2.OnEnter=ApareceCosita2





#caballero traidor 3, estático en almacén junto alcantarillas

Gladius=Bladex.CreateEntity("RagnarGladius3","Gladius",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
escudo=Bladex.CreateEntity("RagnarEsc3kgt","Escudo5",0,0,0)
ItemTypes.ItemDefaultFuncs(escudo)


pers=Bladex.CreateEntity("3kngt","Knight_Traitor",-126000,750,48000,"Person")
pers.Angle=1.5
pers.Level=0
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
Actions.TakeObject(pers.Name,"RagnarGladius3")
Actions.TakeObject(pers.Name,"RagnarEsc3kgt")
pers.SetOnFloor()

#AniSound.AsignarSonidosCaballeroTraidor('3kngt')


#####################################
#####################################CABALLERO EN KOMEDOR tiene la llaveeeeeeee

Gladius=Bladex.CreateEntity("RagnarGladiusKOM","Gladius",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
escudo=Bladex.CreateEntity("RagnarEscudoKOM","Escudo5",0,0,0)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("KOMkngt","Knight_Traitor",-81406.529435, -6366.32180405, 45316.01156,"Person")
pers.Angle=5.8640284647
pers.Level=1
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
#pers.Data.JoinGroup(pers.Name, "KOMEDOR")
Actions.TakeObject(pers.Name,"RagnarGladiusKOM")
Actions.TakeObject(pers.Name,"RagnarEscudoKOM")
Actions.TakeObject("KOMkngt","llave45")

darfuncs.HideBadGuy("KOMkngt")


senkom=Bladex.GetSector(-74000,-5000,51500)
senkom.OnEnter=ApareceKOMkngt




N_KT_Patio = 2


#####Caballeros traidores 4 y 5 patrullando en patio exterior junto a lampara colgante

##caballero 5b - LIDERRRR

Gladius=Bladex.CreateEntity("RagnarGladius5b","Gladius",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
escudo=Bladex.CreateEntity("RagnarEscudo2b","Escudo5",0,0,0)
ItemTypes.ItemDefaultFuncs(escudo)


pers=Bladex.CreateEntity("5bkngt","Knight_Traitor",-113145.903704, -6101.25270551, 43379.6814897,"Person")
pers.Angle=6.0587611088

pers.Level=0
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
pers.Data.JoinGroup(pers.Name, "patio exterior junto a lampara colgante")
Actions.TakeObject(pers.Name,"RagnarGladius5b")
Actions.TakeObject(pers.Name,"RagnarEscudo2b")
pers.Data.DefImDeadFunc = pers.ImDeadFunc
pers.ImDeadFunc = Muere_KT_Patio

darfuncs.HideBadGuy("5bkngt")

#AniSound.AsignarSonidosCaballeroTraidor(pers.Name)

##caballero 4

Gladius=Bladex.CreateEntity("RagnarGladius4","Gladius",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
escudo=Bladex.CreateEntity("RagnarEscudo1","Escudo5",0,0,0)
ItemTypes.ItemDefaultFuncs(escudo)
potion=Bladex.CreateEntity("4kngtsPotion","Pocima25",0,0,0)
potion.Static=0
potion.Solid=0
potion.Scale=1.220190
pocimac.CreatePotion("4kngtsPotion")



pers=Bladex.CreateEntity("4kngt","Knight_Traitor",-107683.183349, -6077.11016841, 49451.1265,"Person")
pers.Angle=4.7
pers.Level=1
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
pers.Data.JoinGroup(pers.Name, "patio exterior junto a lampara colgante")
Actions.TakeObject(pers.Name,"RagnarGladius4")
Actions.TakeObject(pers.Name,"RagnarEscudo1")
Actions.TakeObject(pers.Name,"4kngtsPotion")
#AniSound.AsignarSonidosCaballeroTraidor(pers.Name)
pers.Data.DefImDeadFunc = pers.ImDeadFunc
pers.ImDeadFunc = Muere_KT_Patio

#darfuncs.HideBadGuy("4kngt")





#pers.AddBayPoint=-107683.183349, -6077.11016841, 49451.1265
#pers.AddBayPoint=-96226.4351292, -6053.59308429, 48277.7423
#pers.AddBayPoint=-94717.3697911, -6049.38559077, 49798.6649
#pers.AddBayPoint=-95679.7741666, -6058.90268095, 51917.0940
#pers.AddBayPoint=-114498.969415, -6058.75582126, 52012.824
#pers.AddBayPoint=-115453.59665, -6051.82273262, 50318.73902

##caballero 5

Gladius=Bladex.CreateEntity("RagnarGladius5","Gladius",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
escudo=Bladex.CreateEntity("RagnarEscudo2","Escudo5",0,0,0)
ItemTypes.ItemDefaultFuncs(escudo)



pers=Bladex.CreateEntity("5kngt","Knight_Traitor",-100566.188266, -6067.36205855, 59148.9432,"Person")
pers.Angle=1.57997371669
pers.Level=0
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
pers.Data.JoinGroup(pers.Name, "patio exterior junto a lampara colgante")
Actions.TakeObject(pers.Name,"RagnarGladius5")
Actions.TakeObject(pers.Name,"RagnarEscudo2")
pers.Data.DefImDeadFunc = pers.ImDeadFunc
pers.ImDeadFunc = Muere_KT_Patio

#darfuncs.HideBadGuy("5kngt")

#AniSound.AsignarSonidosCaballeroTraidor(pers.Name)

#pers.AddBayPoint=-100566.188266, -6067.36205855, 59148.9432
#pers.AddBayPoint=-111756.127044, -6068.32319228, 58923.9618
#pers.AddBayPoint=-113471.66198, -6064.17610447, 57494.56409
#pers.AddBayPoint=-112021.565462, -6070.20153086, 54231.8774
#pers.AddBayPoint=-103850.687769, -6062.51438425, 54651.9083
#pers.AddBayPoint=-94405.6017274, -6081.74545861, 54816.7771
#pers.AddBayPoint=-93416.6204042, -6046.50176579, 56577.2626
#pers.AddBayPoint=-94659.8540291, -6067.09109463, 58436.6521


sen4kngt=Bladex.GetSector(-80687.1221719, -7359.35871655, 62703.5401247)
sen4kngt.OnEnter=Aparece4kngt

#####################################cabakkero detras de la puerta del patio

#caballero tres1

Gladius=Bladex.CreateEntity("RagnarGladiustres1","Gladius",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
escudo=Bladex.CreateEntity("RagnarEscudotres1","Escudo2",0,0,0)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("tres1kngt","Knight_Traitor",-124976.265294, -6012.03293651, 47583.049,"Person")
pers.Angle=4.34
pers.Level=2
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
#pers.Data.JoinGroup(pers.Name, "tras puente levadizo")
Actions.TakeObject(pers.Name,"RagnarGladiustres1")
Actions.TakeObject(pers.Name,"RagnarEscudotres1")
pers.Blind = 1
pers.Deaf = 1


###talkingknights.py

##FUNCION QUE HACE DESAPARECER LOS ENEMIGOS HASTA EL patio con los tres caballeros


sendes1=Bladex.GetSector(-122552.583148, -6321.28490453, 48176.4895)
sendes1.OnEnter=Desaparecen1


###########################
##########PATRULLANDO EN LA MURALLA DE LA TORRE OCTOGONAL
###########################

#caballero JUNTO A LA PALANCA1

Gladius=Bladex.CreateEntity("RagnarGladius330","Gladius",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
escudo=Bladex.CreateEntity("RagnarEscudo330","Escudo2",0,0,0)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("330kngt","Knight_Traitor",-96619, -9256, -54029,"Person")
pers.Angle=5.68
pers.Level=2
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
#pers.Data.JoinGroup(pers.Name, "tras puente levadizo")
Actions.TakeObject(pers.Name,"RagnarGladius330")
Actions.TakeObject(pers.Name,"RagnarEscudo330")


#caballero JUNTO A LA PALANCA2

Gladius=Bladex.CreateEntity("RagnarGladius331","Gladius",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
escudo=Bladex.CreateEntity("RagnarEscudo331","Escudo2",0,0,0)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("331kngt","Knight_Traitor",-117500, -8770, -47850,"Person")
pers.Angle=0.73
pers.Level=2
pers.ActionAreaMin=pow(2,10)
pers.ActionAreaMax=pow(2,11)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
#pers.Data.JoinGroup(pers.Name, "tras puente levadizo")
Actions.TakeObject(pers.Name,"RagnarGladius331")
Actions.TakeObject(pers.Name,"RagnarEscudo331")

#pers.AddBayPoint=-117500, -8770, -47850
#pers.AddBayPoint=-120050, -8770, -36950
#pers.AddBayPoint=-123300, -8770, -10950
#pers.AddBayPoint=-121350, -8770, -4100
#pers.AddBayPoint=-123300, -8770, -10950
#pers.AddBayPoint=-120050, -8770, -36950



#caballeros traidores en patio del puente levadizo

#caballero 15

Gladius=Bladex.CreateEntity("RagnarGladius15","Alabarda",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
escudo=Bladex.CreateEntity("RagnarEscudo15","Escudo2",0,0,0)
ItemTypes.ItemDefaultFuncs(escudo)
potion=Bladex.CreateEntity("15kngtsPotion","Pocima100",0,0,0)
potion.Static=0
potion.Solid=0
potion.Scale=1.220190
pocimac.CreatePotion("15kngtsPotion")

pers=Bladex.CreateEntity("15kngt","Knight_Traitor",-96000,0,-29000,"Person")
pers.Angle=1.5
pers.Level=2
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
pers.Data.goto_limit2aa=0
pers.Data.JoinGroup(pers.Name, "patio del puente levadizo")
Actions.TakeObject(pers.Name,"RagnarGladius15")
Actions.TakeObject(pers.Name,"RagnarEscudo15")
Actions.TakeObject(pers.Name,"15kngtsPotion")


#pers.AddBayPoint=-96000,0,-29000
#pers.AddBayPoint=-96000,0,-14000
#pers.AddBayPoint=-114000,0,-14000
#pers.AddBayPoint=-114000,0,-29000


#caballero 16

Gladius=Bladex.CreateEntity("RagnarGladius16","Alabarda",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
escudo=Bladex.CreateEntity("RagnarEscudo16","Escudo5",0,0,0)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("16kngt","Knight_Traitor",-99000,1000,-26000,"Person")
pers.Angle=1.5
pers.Level=1
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
pers.Data.goto_limit2aa=0
pers.Data.JoinGroup(pers.Name, "patio del puente levadizo")
Actions.TakeObject(pers.Name,"RagnarGladius16")
Actions.TakeObject(pers.Name,"RagnarEscudo16")


#pers.AddBayPoint=-99000,1000,-26000
#pers.AddBayPoint=-110000,1000,-26000
#pers.AddBayPoint=-110000,1000,-17000
#pers.AddBayPoint=-99000,1000,-17000



#caballero 18c
############
############## TIENE LLAVEEEEEEEEEEE


Gladius=Bladex.CreateEntity("RagnarGladius18c","Gladius",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
escudo=Bladex.CreateEntity("RagnarEsc18ckgt","Escudo5",0,0,0)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("18ckngt","Knight_Traitor",-103955.812202, 940.318380757, -51576.249,"Person")
pers.Angle=5.94
pers.Level=2
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
pers.Data.JoinGroup(pers.Name, "torre octogonal mayor")
Actions.TakeObject(pers.Name,"RagnarGladius18c")
Actions.TakeObject(pers.Name,"RagnarEsc18ckgt")
Actions.TakeObject("18ckngt","llave7")


#pers.AddBayPoint=-103955.812202, 940.318380757, -51576.249
#pers.AddBayPoint=-100643.252321, 941.300902582, -45716.470
#pers.AddBayPoint=-96090.5980977, 1188.18925463, -38375.869
#pers.AddBayPoint=-91374.5634457, 1689.17567429, -36075.81
#pers.AddBayPoint=-87601.3706975, 1936.87386403, -37286.6021836
#pers.AddBayPoint=-86245.2031582, 1940.5974571, -34810.585852
#pers.AddBayPoint=-88266.0644168, 1940.9119521, -34463.073
#pers.AddBayPoint=-93594.0423325, 1443.23164697, -35332.19
#pers.AddBayPoint=-98987.3411629, 944.843725714, -39171.98
#pers.AddBayPoint=-103547.369257, 940.573928319, -40855.110
#pers.AddBayPoint=-106835.543871, 941.928612783, -44580.275
#pers.AddBayPoint=-105783.946296, 943.44901424, -49079.8062










#caballeros traidores tras puente levadizo


#caballero 22  TIENE LLAVEEEEEEEEEEE la que abre la puerta del primer piso de la torre de Ragnar.

Gladius=Bladex.CreateEntity("RagnarGladius22","Garrote",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
escudo=Bladex.CreateEntity("RagnarEscudo22","Escudo2",0,0,0)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("22kngt","Knight_Traitor",-131000,-600,-106000,"Person")
pers.Angle=5.1
pers.Level=2
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "tras puente levadizo")
Actions.TakeObject(pers.Name,"RagnarGladius22")
Actions.TakeObject(pers.Name,"RagnarEscudo22")
Actions.TakeObject("22kngt","llave69")
#Actions.TakeObject(pers.Name,"22kngtsPotion")
pers.SetOnFloor()
darfuncs.HideBadGuy("22kngt")


#caballero 23

Gladius=Bladex.CreateEntity("RagnarGladius23","Garrote",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
escudo=Bladex.CreateEntity("RagnarEscudo23","Escudo5",0,0,0)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("23kngt","Knight_Traitor",-127000,1000,-98000,"Person")
pers.Angle=5.1
pers.Level=1
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "tras puente levadizo")
Actions.TakeObject(pers.Name,"RagnarGladius23")
Actions.TakeObject(pers.Name,"RagnarEscudo23")
pers.SetOnFloor()
darfuncs.HideBadGuy("23kngt")








#################################
#################################
##########ENEMIGOS NUEVOS DESPUES DE LA REVISION
#################################

################CERCA DE LA POWER POTION
#caballero 24

Gladius=Bladex.CreateEntity("RagnarGladius224","Garrote",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
escudo=Bladex.CreateEntity("RagnarEscudo224","Escudo5",0,0,0)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("224kngt","Knight_Traitor",-92530.5290154, 1238.66888474, -104170.3271,"Person")
pers.Angle=3.6
pers.Level=2
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup(pers.Name, "tras puente levadizo")
Actions.TakeObject(pers.Name,"RagnarGladius224")
Actions.TakeObject(pers.Name,"RagnarEscudo224")
pers.SetOnFloor()

#caballero 25

Gladius=Bladex.CreateEntity("RagnarGladius325","Garrote",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
escudo=Bladex.CreateEntity("RagnarEscudo325","Escudo2",0,0,0)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("325kngt","Knight_Traitor",-97594.7030708, 6696.80320815, -89973.212,"Person")
pers.Angle=5.13
pers.Level=1
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup(pers.Name, "tras puente levadizo")
Actions.TakeObject(pers.Name,"RagnarGladius325")
Actions.TakeObject(pers.Name,"RagnarEscudo325")
pers.SetOnFloor()








################
################
#######en la torre despues de las flechas
#########################################
#caballero 227

Gladius=Bladex.CreateEntity("RagnarGladius227","Gladius",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
escudo=Bladex.CreateEntity("RagnarEscudo227","Escudo5",0,0,0)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("227kngt","Knight_Traitor",-125646.106173, -6253.4934965, -91876.822,"Person")
pers.Angle=3.07
pers.Level=2
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup(pers.Name, "tras puente levadizo")
Actions.TakeObject(pers.Name,"RagnarGladius227")
Actions.TakeObject(pers.Name,"RagnarEscudo227")
pers.SetOnFloor()
darfuncs.HideBadGuy("227kngt")


sen227kngt=Bladex.GetSector(-135500,-5500,-93000)
sen227kngt.OnEnter=Aparece227kngt






################
################
#######en la torre despues de Ragnar dando ordenes
#########################################
#caballero 228

Gladius=Bladex.CreateEntity("RagnarGladius228","Hacha",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
escudo=Bladex.CreateEntity("RagnarEscudo228","Escudo2",0,0,0)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("228kngt","Knight_Traitor",-126507.637242, -12248.7607739, -94109.471,"Person")
pers.Angle=3.4
pers.Level=3
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup(pers.Name, "tras puente levadizo")
Actions.TakeObject(pers.Name,"RagnarGladius228")
Actions.TakeObject(pers.Name,"RagnarEscudo228")
pers.SetOnFloor()
darfuncs.HideBadGuy("228kngt")


sen228kngt=Bladex.GetSector(-127727.850637, -12613.5904283, -110488.57)
sen228kngt.OnEnter=Aparece228kngt
