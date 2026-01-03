from math import pow
import EnemyTypes
import AniSound
import Sparks
import Actions
import pocimac
import Ontake
import darfuncs

### cuevas iniciales

Inicio0 = darfuncs.E_Grup()

darfuncs.EnterSecEvent(302455.734263, 46904.4564206, 28656.8540238,PrimerTurnoVuelta)



#1

o=Bladex.CreateEntity("Hachacarnicero0","Mazapiedra",0,0,0,"Weapon")

pers=Bladex.CreateEntity("Minot0","Minotaur",323472.115469, 38402.7531006, -54918.7437495,"Person")
pers.Level=13
pers.Angle=1.79431868168
Actions.TakeObject(pers.Name,"Hachacarnicero0")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()
darfuncs.HideBadGuy(pers.Name)

Inicio0.AddGuy(pers.Name)

#2


pers=Bladex.CreateEntity("2Skeleton","Skeleton",321122.124712, 38884.1544308, -22731.0545916,"Person")
pers.Angle=2.92730373384
pers.Level=16
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

sword=Bladex.CreateEntity("ChaosEspada2","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("ChaosEscudo2","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy(pers.Name)

Inicio0.AddGuy(pers.Name)

#3

pers=Bladex.CreateEntity("3Skeleton","Skeleton",325601.363455, 38881.68613, -24021.1072868,"Person")
pers.Angle=2.32630702085
pers.Level=17
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

sword=Bladex.CreateEntity("ChaosEspada3","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Chaosbow3","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Chaosquiver3","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy(pers.Name)

Inicio0.AddGuy(pers.Name)
darfuncs.EnterSecEvent(306936.921945, 34331.4799066, -70921.7535892,PrimerTurno)


### segundo turno


#2

pers=Bladex.CreateEntity("5Skeleton", "Skeleton",307184.132611, 41849.6275328, -3016.72884758,"Person")
pers.Angle=4.45390121909
pers.Level=18
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

sword=Bladex.CreateEntity("ChaosEspada5","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("ChaosEscudo5","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy(pers.Name)

#3 encaramado en el acceso al exterior

pers=Bladex.CreateEntity("6Skeleton","Skeleton",319618.958332, 38724.0071257, 6314.50882739,"Person")
pers.Angle=1.57682634025
pers.Level=17
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

sword=Bladex.CreateEntity("ChaosEspada6","Maza3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Chaosbow6","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Chaosquiver6","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy(pers.Name)

darfuncs.EnterSecEvent(323000, 38843, -25000,SegundoTurno)




### tercer turno -minorx-

#2
o=Bladex.CreateEntity("Hachacarnicero2","Mazapiedra",0,0,0,"Weapon")

pers=Bladex.CreateEntity("Minot2","Minotaur",285386.924621, 42626.7747615, 14351.1025855,"Person")
pers.Level=14
pers.Angle=2.92553028696
Actions.TakeObject(pers.Name,"Hachacarnicero2")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

darfuncs.HideBadGuy(pers.Name)


darfuncs.EnterSecEvent(287049.312241, 41818.8433033, -423.971001599,TercerTurno)



###esqueleto arkero jodepusilanimes

pers=Bladex.CreateEntity("7Skeleton","Skeleton",315862.317931, 41058.940754, 31185.8643691,"Person")
pers.Angle=1.38546541869
pers.Level=15
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()

sword=Bladex.CreateEntity("ChaosEspada7","Maza3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Chaosbow7","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Chaosquiver7","CarcajEnvenenado",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy(pers.Name)



## minorx escondido junto a eskeleto anterior

o=Bladex.CreateEntity("Hachacarnicero7","Mazapiedra",0,0,0,"Weapon")

pers=Bladex.CreateEntity("Minot7","Minotaur",325837.768927, 38856.7959711, 7408.78039794,"Person")
pers.Level=17
pers.Angle=4.95997407277
Actions.TakeObject(pers.Name,"Hachacarnicero7")
#pers.ActionAreaMin=pow(2,4)
#pers.ActionAreaMax=pow(2,5)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

darfuncs.HideBadGuy(pers.Name)

darfuncs.EnterSecEvent(321016.077991, 38776.2325207, 25373.0417071,MueveMinot7)

darfuncs.EnterSecEvent(290000, 46000, 23000,CuartoTurno)



#########
#########al regreso

## guardianes puerta a interior -minorx o keletos-

#1

pers=Bladex.CreateEntity("8Skeleton","Skeleton",310115.70378, 38431.442615, -49283.8439917,"Person")
pers.Angle=0.960525527496
pers.Level=18
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

sword=Bladex.CreateEntity("ChaosEspada8","Maza3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("ChaosEscudo8","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

Inicio0.AddGuy(pers.Name)

darfuncs.HideBadGuy(pers.Name)




#2

pers=Bladex.CreateEntity("9Skeleton","Skeleton",323860.193624, 38390.5555487, -52893.6977768,"Person")
pers.Angle=1.24119106798
pers.Level=17
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

sword=Bladex.CreateEntity("ChaosEspada9","Maza3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("ChaosEscudo9","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

darfuncs.HideBadGuy(pers.Name)

Inicio0.AddGuy(pers.Name)


## minot sorpresa

o=Bladex.CreateEntity("Hachacarnicero8","Mazapiedra",0,0,0,"Weapon")

pers=Bladex.CreateEntity("Minot8","Minotaur",317006.994928, 40900.1063577, -5563.40885526,"Person")
pers.Level=19
pers.Angle=0.971070588174
Actions.TakeObject(pers.Name,"Hachacarnicero8")
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

darfuncs.HideBadGuy(pers.Name)

Inicio0.AddGuy(pers.Name)



######## entre los 2 rastrillos. Zona de guardia keletos en llamas


#1

pers=Bladex.CreateEntity("14Skeleton","Skeleton",370124.228775, 47354.8891409, -86660.5093306,"Person")
pers.Angle=6.22151573595
pers.Level=16
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

sword=Bladex.CreateEntity("ChaosEspada14","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("ChaosEscudo14","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)

#2

pers=Bladex.CreateEntity("15Skeleton","Skeleton",374286.949561, 48879.4163383, -63411.7713125,"Person")
pers.Angle=2.64740433533
pers.Level=18
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

sword=Bladex.CreateEntity("ChaosEspada15","Maza3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("ChaosEscudo15","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs. EnterSecEvent(348273.809792, 42130.8901411, -70266.7906723,Skelpas)

## cab negros en zona habitaciones


#1

pers=Bladex.CreateEntity("11Kngt","Dark_Knight",350366.009566, 43879.098254, -87339.6430849,"Person")
pers.Angle=3.10415584556
pers.Level=18
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()

sword=Bladex.CreateEntity("ChaosEspada11","Espadafilo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

potion=Bladex.CreateEntity("Potion1","Pocima200",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

shield=Bladex.CreateEntity("ChaosEscudo11","Escudo7",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)


#2


pers=Bladex.CreateEntity("12Kngt","Dark_Knight",340568.710943, 41819.9904355, -79211.7733415,"Person")
pers.Angle=3.22785864482
pers.Level=18
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()

sword=Bladex.CreateEntity("ChaosEspada12","Espadafilo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

potion=Bladex.CreateEntity("Potion2","Pocima200",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

shield=Bladex.CreateEntity("ChaosEscudo12","Escudo7",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy(pers.Name)

darfuncs.EnterSecEvent(353637.855248, 44273.964308, -92256.388985,ApareceCaballero)


#3


pers=Bladex.CreateEntity("13Kngt","Dark_Knight",337475.925123, 43851.5120544, -93294.1475622,"Person")
pers.Angle=5.44467168915
pers.Level=17
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()

sword=Bladex.CreateEntity("ChaosEspada13","Espadafilo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

potion=Bladex.CreateEntity("Potion3","Pocima200",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

EnemyTypes.EnemyDefaultFuncs(pers)

