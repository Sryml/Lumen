from math import pow
import EnemyTypes
import Sparks
import Actions
import darfuncs
import ItemTypes
import LevelFuncs

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 12
expected_player_lvl_max= 16

lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)
# e.g. to give an enemy a level between 0 and 4, do
# pers.Level= lvl_control.GiveLevel(0, 4)
#

execfile("SleepingKnights.py")

#------------------inicio-----------------------

#caballeros traidores el foso, al principio.

##1


o=Bladex.CreateEntity("IceArma1","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo1","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("1kngt","Knight_Traitor",-30196.3548908, 9890.57314587, 53794.9221941,"Person")
pers.Angle=3.98028957317
pers.Level=lvl_control.GiveLevel(8,12)
Actions.TakeObject(pers.Name,"IceArma1")
Actions.TakeObject(pers.Name,"IceEscudo1")
Actions.TakeObject("1kngt","llave0")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers.Data.JoinGroup("1kngt", "foso")

##2
#o=Bladex.CreateEntity("IceArma2","Espadaelfica",0,0,0,"Weapon")
#o=Bladex.CreateEntity("IceEscudo2","Escudo1",0,0,0)
#Sparks.MakeShield("IceEscudo2")
#Breakings.SetBreakableWS("IceEscudo2")

#pers=Bladex.CreateEntity("2kngt","Knight_Traitor",-28488.7547891, 9890.49298528, 51812.7610362,"Person")
#pers.Angle=0.838693187709
#pers.Level=7
#Actions.TakeObject(pers.Name,"IceArma2")
#Actions.TakeObject(pers.Name,"IceEscudo2")
#pers.ActionAreaMin=pow(2,0)
#pers.ActionAreaMax=pow(2,1)
#EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("2kngt", "foso")
#pers.SetOnFloor()

## PATRULLANTE

o=Bladex.CreateEntity("IceArma3","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo3","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
potion=Bladex.CreateEntity("IcePotion1","Pocima100",0,0,0)
potion.Static=0
potion.Solid=1
potion.Scale=1.0
pocimac.CreatePotion("IcePotion1")


pers=Bladex.CreateEntity("3kngt","Knight_Traitor",-34770.7235401, 9880.02351089, 37821.2237245,"Person")
pers.Angle=3.17232422146
pers.Level=lvl_control.GiveLevel(7,11)
Actions.TakeObject(pers.Name,"IceArma3")
Actions.TakeObject(pers.Name,"IceEscudo3")
Actions.TakeObject(pers.Name,"IcePotion1")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers.Data.JoinGroup("3kngt", "foso")

#pers.AddBayPoint=-34570.7235401, 9880.02351089, 37621.2237245
#pers.AddBayPoint=-34990.1042137, 9878.70188822, -6176.37846685
#pers.AddBayPoint=-30695.4145028, 9874.64636988, -5419.82924115
#pers.AddBayPoint=-30447.8021254, 9879.11379107, 37581.613523


##### tras elevador inicial




Inicio = darfuncs.E_Grup()
Inicio.OnDeath = TerminanLasMuertes1





#1 caballero de espaldas al elevador

o=Bladex.CreateEntity("IceArma4","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo4","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("4kngt","Knight_Traitor",-25471.7330112, 536.880766049, 72868.1946339,"Person")
pers.Angle=5.32461423781
pers.Level=lvl_control.GiveLevel(8,12)
Actions.TakeObject(pers.Name,"IceArma4")
Actions.TakeObject(pers.Name,"IceEscudo4")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers.Data.JoinGroup("4kngt", "entrada")

Inicio.AddGuy(pers.Name)
Inicio.OnDeath = TerminanLasMuertes1


##caballero patrullante

o=Bladex.CreateEntity("IceArma5","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo5","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("5kngt","Knight_Traitor",-14737.2519019, 444.692607305, 76353.7687798,"Person")
pers.Angle=4.71565447247
pers.Level=lvl_control.GiveLevel(8,11)
Actions.TakeObject(pers.Name,"IceArma5")
Actions.TakeObject(pers.Name,"IceEscudo5")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers.Data.JoinGroup("5kngt", "entrada")

Inicio.AddGuy(pers.Name)
Inicio.OnDeath = TerminanLasMuertes1

#pers.AddBayPoint=-14737.2519019, 444.692607305, 76353.7687798
#pers.AddBayPoint=7574.30473885, -1358.11120838, 76675.5337678
#pers.AddBayPoint=22012.4792171, -1142.9446157, 77209.4673967
#pers.AddBayPoint=22545.439716, -1156.39845089, 74709.4884224
#pers.AddBayPoint=8011.08041968, -1351.61692476, 74497.9182899
#pers.AddBayPoint=-14648.5494794, 459.258379067, 73974.7793292


# caballeros papando moscas


o=Bladex.CreateEntity("IceArma6","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo6","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("6kngt","Knight_Traitor",34723.7371793, -2345.34400568, 79462.6169748,"Person")
pers.Angle=6.25824962985
pers.Level=lvl_control.GiveLevel(7,12)
Actions.TakeObject(pers.Name,"IceArma6")
Actions.TakeObject(pers.Name,"IceEscudo6")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers.Data.JoinGroup("6kngt", "entrada")

potion=Bladex.CreateEntity("IcePotion1b","Pocima50",0,0,0)
potion.Static=0
potion.Solid=1
potion.Scale=1.0
pocimac.CreatePotion("IcePotion1b")


o=Bladex.CreateEntity("IceArma7","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo7","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("7kngt","Knight_Traitor",33407.2319019, -1167.35136952, 109226.645065,"Person")
pers.Angle=0.893234827971
pers.Level=lvl_control.GiveLevel(8,12)
Actions.TakeObject(pers.Name,"IceArma7")
Actions.TakeObject(pers.Name,"IceEscudo7")
#Actions.TakeObject(pers.Name,"llave1")
Actions.TakeObject(pers.Name,"IcePotion1b")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers.Data.JoinGroup("7kngt", "entrada")


##caballeros contingentes con muerte 2 primeros zona actual



#1 arkero


pers=Bladex.CreateEntity("IceArq4","Knight_Traitor",16285.3830443, -1173.61524461, 99453.5105027,"Person")
pers.Angle=6.26441672716
pers.Level=lvl_control.GiveLevel(5,10)
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

o=Bladex.CreateEntity("IceArcArma4","Espadacurva",0,0,0,"Weapon")
inv=pers.GetInventory()
ItemTypes.ItemDefaultFuncs(o)
inv.AddWeapon("IceArcArma4")

inv=pers.GetInventory()
o=Bladex.CreateEntity("Icebow4","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv.AddBow("Icebow4")
#ItemTypes.ItemDefaultFuncs(Bladex.GetEntity("Icebow4"))


o=Bladex.CreateEntity("Icequiver4","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Icequiver4")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("IceArq4")


#2

o=Bladex.CreateEntity("IceArma9","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo9","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("9kngt","Knight_Traitor",15915.5552955, -1063.03496558, 111198.9237,"Person")
pers.Angle=3.2129605562
pers.Level=lvl_control.GiveLevel(8,12)
Actions.TakeObject(pers.Name,"IceArma9")
Actions.TakeObject(pers.Name,"IceEscudo9")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers.Data.JoinGroup("9kngt", "entrada")
darfuncs.HideBadGuy("9kngt")


### zona arkeros lokos

ambiente = darfuncs.E_Grup()
ambiente.OnDeath = Suenamusica

#arkero loko 1

pers=Bladex.CreateEntity("IceArq1", "Knight_Traitor",69485.500647, -6535.20602315, 89484.4437733,"Person")
pers.Angle=4.77325249667
pers.Level=lvl_control.GiveLevel(7,10)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

o=Bladex.CreateEntity("IceArcArma1","Maza2",0,0,0,"Weapon")
inv=pers.GetInventory()
ItemTypes.ItemDefaultFuncs(o)
inv.AddWeapon("IceArcArma1")

inv=pers.GetInventory()
o=Bladex.CreateEntity("Icebow1","Arco",0,0,0,"Weapon")
inv.AddBow("Icebow1")
ItemTypes.ItemDefaultFuncs(Bladex.GetEntity("Icebow1"))

o=Bladex.CreateEntity("Icequiver1","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Icequiver1")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)


#arkero loko 2

pers=Bladex.CreateEntity("IceArq1a", "Knight_Traitor",77588.2670673, -6721.99899115, 88697.2035191,"Person")
pers.Angle=3.16412415424
pers.Level=lvl_control.GiveLevel(6,9)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

o=Bladex.CreateEntity("IceArcArma1a","Hacha4",0,0,0,"Weapon")
inv=pers.GetInventory()
ItemTypes.ItemDefaultFuncs(o)
inv.AddWeapon("IceArcArma1a")

inv=pers.GetInventory()
o=Bladex.CreateEntity("Icebow1a","Arco",0,0,0,"Weapon")
inv.AddBow("Icebow1a")
ItemTypes.ItemDefaultFuncs(Bladex.GetEntity("Icebow1a"))

o=Bladex.CreateEntity("Icequiver1a","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Icequiver1a")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)




# potionman

potion=Bladex.CreateEntity("IcePotion2","Pocima50",0,0,0)
potion.Static=0
potion.Solid=1
potion.Scale=1.0
pocimac.CreatePotion("IcePotion2")

o=Bladex.CreateEntity("IceArma13","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo13","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("13kngt","Knight_Traitor",63545.7636693, -2094.66127988, 79510.8283948,"Person")
pers.Angle=3.18991550827
pers.Level=lvl_control.GiveLevel(6,11)
Actions.TakeObject(pers.Name,"IceArma13")
Actions.TakeObject(pers.Name,"IceEscudo13")
Actions.TakeObject(pers.Name,"IcePotion2")
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers.Data.JoinGroup("13kngt", "loko")
ambiente.AddGuy(pers.Name)
ambiente.OnDeath = Suenamusica

## patrullantes lokos

#1

o=Bladex.CreateEntity("IceArma14","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo14","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("14kngt","Knight_Traitor",61339.6344771, -2150.44472845, 76356.0547344,"Person")
pers.Angle=3.2028606222
pers.Level=lvl_control.GiveLevel(9,12)
Actions.TakeObject(pers.Name,"IceArma14")
Actions.TakeObject(pers.Name,"IceEscudo14")
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers.Data.JoinGroup("14kngt", "loko")
ambiente.AddGuy(pers.Name)
ambiente.OnDeath = Suenamusica

#pers.AddBayPoint=61339.6344771, -2150.44472845, 76356.0547344
#pers.AddBayPoint=61780.9059647, -2469.44176428, 49724.3581262
#pers.AddBayPoint=66349.6227498, -2551.95579005, 49439.6966914
#pers.AddBayPoint=65853.2322413, -2151.28836172, 77130.2641588



#2

o=Bladex.CreateEntity("IceArma15","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo15","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("15kngt","Knight_Traitor",82715.4760073, -2518.11328179, 58939.6489339,"Person")
pers.Angle=1.53980111075
pers.Level=lvl_control.GiveLevel(8,11)
Actions.TakeObject(pers.Name,"IceArma15")
Actions.TakeObject(pers.Name,"IceEscudo15")
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers.Data.JoinGroup("15kngt", "loko")
ambiente.AddGuy(pers.Name)
ambiente.OnDeath = Suenamusica





## sobre estructura central

#1

o=Bladex.CreateEntity("IceArma16","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo16","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("16kngt","Knight_Traitor",72659.0442957, -12104.4470614, 67665.8476024,"Person")
pers.Angle=3.71548463074
pers.Level=lvl_control.GiveLevel(8,11)
Actions.TakeObject(pers.Name,"IceArma16")
Actions.TakeObject(pers.Name,"IceEscudo16")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers.Data.JoinGroup("16kngt", "central")
#2

potion=Bladex.CreateEntity("IcePotion3","Pocima200",0,0,0)
potion.Static=0
potion.Solid=1
potion.Scale=1.0
pocimac.CreatePotion("IcePotion3")

o=Bladex.CreateEntity("IceArma17","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo17","Escudo8",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("17kngt","Knight_Traitor",64238.3712697, -12119.4147305, 60468.7855198,"Person")
pers.Angle=4.68552681581
pers.Level=lvl_control.GiveLevel(9,12)
Actions.TakeObject(pers.Name,"IceArma17")
Actions.TakeObject(pers.Name,"IceEscudo17")
Actions.TakeObject(pers.Name,"IcePotion3")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers.Data.JoinGroup("17kngt", "central")

#####
#####
#####
##### SEGUNDA PARTE -a partir escaleras tras zona arkero loko

#patrullante solitario

o=Bladex.CreateEntity("IceArma18","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo18","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("18kngt","Knight_Traitor",92650.1409497, -6905.17658901, 49801.5591252,"Person")
pers.Angle=3.11606942678
pers.Level=lvl_control.GiveLevel(8,11)
Actions.TakeObject(pers.Name,"IceArma18")
Actions.TakeObject(pers.Name,"IceEscudo18")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers.Data.JoinGroup("18kngt", "solitario")

#pers.AddBayPoint=92650.1409497, -6905.17658901, 49801.5591252
#pers.AddBayPoint=92481.3565721, -6105.78489167, 19094.1705448
#pers.AddBayPoint=94531.1415344, -6104.16290155, 18932.7497759
#pers.AddBayPoint=94854.9434414, -6931.49961211, 49237.3456306


##caballero susceptible de ser acribillado a flechazos

o=Bladex.CreateEntity("IceArma19","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo19","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("19kngt","Knight_Traitor",87014.3479945, -5131.28717544, 12032.7157904,"Person")
pers.Angle=1.51293480041
pers.Level=lvl_control.GiveLevel(7,10)
Actions.TakeObject(pers.Name,"IceArma19")
Actions.TakeObject(pers.Name,"IceEscudo19")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers.Data.JoinGroup("19kngt", "solitario")

# caballero andarin junto a arkero intrepido

#1

o=Bladex.CreateEntity("IceArma20","Espadacurva",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo20","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
enric2=Bladex.CreateEntity("20kngt","Knight_Traitor",95767.7638289, -6082.34577875, 3893.10870023,"Person")
enric2.Angle=3.13476563765
enric2.Level=lvl_control.GiveLevel(8,11)
Actions.TakeObject(enric2.Name,"IceArma20")
Actions.TakeObject(enric2.Name,"IceEscudo20")
enric2.ActionAreaMin=pow(2,0)
enric2.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(enric2)
enric2.SetOnFloor()

enric2.Data.nodos=[(95838.0531607, -6080.28025, -15116.6994464), (101252.305027, -6081.27091684, -15232.2127298)]
enric2.Data.nodo_actual=0



sectx3=Bladex.GetSector(89441.9222207, -5666.59394625, 7197.80742773)
sectx3.OnEnter=x3






#2

pers=Bladex.CreateEntity("IceArq2", "Knight_Traitor",92469.9393481, -6078.37168578, -16300.7906906,"Person")
pers.Angle=1.47985622355
pers.Level=lvl_control.GiveLevel(8,12)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

o=Bladex.CreateEntity("IceArcArma2","Espadacurva",0,0,0,"Weapon")
inv=pers.GetInventory()
ItemTypes.ItemDefaultFuncs(o)
inv.AddWeapon("IceArcArma2")

inv=pers.GetInventory()
o=Bladex.CreateEntity("Icebow2","Arco",0,0,0,"Weapon")
inv.AddBow("Icebow2")
ItemTypes.ItemDefaultFuncs(Bladex.GetEntity("Icebow2"))

o=Bladex.CreateEntity("Icequiver2","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Icequiver2")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)


## caballeros cerca de minotauros

#1

o=Bladex.CreateEntity("IceArma21","Espadaelfica",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo21","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
enric3=Bladex.CreateEntity("21kngt","Knight_Traitor",60192.5558817, -863.5275263, 15812.6603246,"Person")
enric3.Angle=3.14775021242
enric3.Level=lvl_control.GiveLevel(6,10)
Actions.TakeObject(enric3.Name,"IceArma21")
Actions.TakeObject(enric3.Name,"IceEscudo21")
#Actions.TakeObject(enric3.Name,"llavetoro2")
enric3.ActionAreaMin=pow(2,8)
enric3.ActionAreaMax=pow(2,9)
enric3.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(enric3)




#2

o=Bladex.CreateEntity("IceArma22","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo22","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("22kngt","Knight_Traitor",59872.1784343, -854.931619542, 6520.46728546,"Person")
pers.Angle=3.18550418823
pers.Level=lvl_control.GiveLevel(6,9)
Actions.TakeObject(pers.Name,"IceArma22")
Actions.TakeObject(pers.Name,"IceEscudo22")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

ambiente2.AddGuy(pers.Name)
ambiente2.OnDeath = Suenamusica2

#pers.AddBayPoint=59872.1784343, -854.931619542, 6520.46728546
#pers.AddBayPoint=59617.7368974, -854.101269811, -13635.297643
#pers.AddBayPoint=67127.8336163, -854.97131793, -14020.0711996
#pers.AddBayPoint=70475.4794726, -854.462601897, -16130.4876588
#pers.AddBayPoint=83086.0639244, -856.972992328, -16080.6345719
#pers.AddBayPoint=82851.5655877, -854.637415593, -12579.5796606
#pers.AddBayPoint=62632.7459064, -852.048634587, -12219.3151148
#pers.AddBayPoint=62283.3829055, -853.289313592, 6304.60577308






## caballero oscuro frente a puerta pre-final con llave

ambiente4 = darfuncs.E_Grup()
ambiente4.OnDeath = Suenamusica4


o=Bladex.CreateEntity("IceArma23","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo23","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("23kngt","Dark_Knight",-14205.9956689, -222.440050306, 21420.5163179,"Person")
pers.Angle=1.58157547943
pers.Level=lvl_control.GiveLevel(5,9)
Actions.TakeObject(pers.Name,"IceArma23")
Actions.TakeObject(pers.Name,"IceEscudo23")
Actions.TakeObject(pers.Name,"llavevid")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


ambiente4.AddGuy(pers.Name)
ambiente4.OnDeath = Suenamusica4

## caballero oscuro despistado -fichaje de ultima hora-

ambiente3 = darfuncs.E_Grup()
ambiente3.OnDeath = Suenamusica3


o=Bladex.CreateEntity("IceArma23a","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo23a","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("23akngt","Dark_Knight",-8796.23186171, -554.822608727, -12106.6041326,"Person")
pers.Angle=1.69177051101
pers.Level=lvl_control.GiveLevel(5,9)
Actions.TakeObject(pers.Name,"IceArma23a")
Actions.TakeObject(pers.Name,"IceEscudo23a")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

ambiente4.AddGuy(pers.Name)
ambiente4.OnDeath = Suenamusica4


## caballero oscuro taimado


o=Bladex.CreateEntity("IceArma23b","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo23b","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IcePotion1c","PocimaTodo",0,0,0)
o.Static=0
o.Solid=1
o.Scale=1.0
pocimac.CreatePotion("IcePotion1c")


pers=Bladex.CreateEntity("23bkngt","Dark_Knight",19853.3190916, -454.049054676, -6236.71503761,"Person")
pers.Angle=3.16039888725
pers.Level=lvl_control.GiveLevel(6,10)
Actions.TakeObject(pers.Name,"IceArma23b")
Actions.TakeObject(pers.Name,"IceEscudo23b")
Actions.TakeObject(pers.Name,"IcePotion1c")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

ambiente3.AddGuy(pers.Name)
ambiente3.OnDeath = Suenamusica3

ambiente4.AddGuy(pers.Name)
ambiente4.OnDeath = Suenamusica4


## caballeros oscuros charlando bajo boton tablilla

potion=Bladex.CreateEntity("IcePotion4","Pocima200",0,0,0)
potion.Static=0
potion.Solid=1
potion.Scale=1.0
pocimac.CreatePotion("IcePotion4")

o=Bladex.CreateEntity("IceArma24","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo24","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("24kngt","Dark_Knight",43443.8878373, -1315.23598302, 23096.9023894,"Person")
pers.Angle=3.6800036269
pers.Level=lvl_control.GiveLevel(7,10)
Actions.TakeObject(pers.Name,"IceArma24")
Actions.TakeObject(pers.Name,"IceEscudo24")
Actions.TakeObject(pers.Name,"IcePotion4")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy("24kngt")


o=Bladex.CreateEntity("IceArma25","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo25","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
enric4=Bladex.CreateEntity("25kngt","Dark_Knight",44876.0590147, -1329.17075173, 21098.5861585,"Person")
enric4.Angle=0.504629504037
enric4.Level=lvl_control.GiveLevel(6,9)
Actions.TakeObject(enric4.Name,"IceArma25")
Actions.TakeObject(enric4.Name,"IceEscudo25")
enric4.ActionAreaMin=pow(2,8)
enric4.ActionAreaMax=pow(2,9)
enric4.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(enric4)
darfuncs.HideBadGuy("25kngt")

enric4.Data.nodos=[(45542.5974018, -9077.44663809, 56045.4286446), (30877.9578359, -9078.41929267, 55864.5683148)]
enric4.Data.nodo_actual=0


sectx5=Bladex.GetSector(18893.3708712, -1077.19922664, 22301.3824679)
sectx5.OnEnter=x5

## los 2 caballeros anteriores solo aparecen tras entrar en un sector el jugador
## debido a que oyen de muy lejos y no interesa que se desmadren antes de tiempo

sectx7=Bladex.GetSector(-18203.3671639, -538.09542193, -4666.93729585)
sectx7.OnEnter=x7




o=Bladex.CreateEntity("IceArma26","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo26","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("26kngt","Dark_Knight",25710.9602383, -9058.93893895, 57703.5255038,"Person")
pers.Angle=4.65669640927
pers.Level=lvl_control.GiveLevel(6,9)
Actions.TakeObject(pers.Name,"IceArma26")
Actions.TakeObject(pers.Name,"IceEscudo26")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


#arkero kabron


pers=Bladex.CreateEntity("IceArq3", "Dark_Knight",18696.887767, -9077.64064596, 27146.0600151,"Person")
pers.Angle=6.27089499043
pers.Level=lvl_control.GiveLevel(5,8)
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()

o=Bladex.CreateEntity("IceArcArma3","EgyptSword",0,0,0,"Weapon")
inv=pers.GetInventory()
ItemTypes.ItemDefaultFuncs(o)
inv.AddWeapon("IceArcArma3")

inv=pers.GetInventory()
o=Bladex.CreateEntity("Icebow3","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv.AddBow("Icebow3")


o=Bladex.CreateEntity("Icequiver3","CarcajEnvenenado",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Icequiver3")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)



darfuncs.HideBadGuy("IceArq3")


sectx6=Bladex.GetSector(21891.9198517, -9117.70576371, 49396.7420681)
sectx6.OnEnter=x6




#keleto FLAMIGERO

ambiente5 = darfuncs.E_Grup()
ambiente5.OnDeath = Suenamusica5


o=Bladex.CreateEntity("IceArmaFLAM","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudoFLAM","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("FLAMEsq","Skeleton",23390.9717744, 8902.70444271, 41071.458,"Person")
pers.Angle=1.374089431
pers.Level=lvl_control.GiveLevel(10,12)
Actions.TakeObject(pers.Name,"IceArmaFLAM")
Actions.TakeObject(pers.Name,"IceEscudoFLAM")
#pers.ActionAreaMin=pow(2,10)
#pers.ActionAreaMax=pow(2,11)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

ambiente5.AddGuy(pers.Name)
ambiente5.OnDeath = Suenamusica5

darfuncs.HideBadGuy("FLAMEsq")






#keletos finales

#1

o=Bladex.CreateEntity("IceArma27","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo27","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("1Esq","Skeleton",30043.2921497, -9046.366474, -12236.4186353,"Person")
pers.Angle=1.53634089431
pers.Level=lvl_control.GiveLevel(10,13)
Actions.TakeObject(pers.Name,"IceArma27")
Actions.TakeObject(pers.Name,"IceEscudo27")
#pers.ActionAreaMin=pow(2,10)
#pers.ActionAreaMax=pow(2,11)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("1Esq")

#2

o=Bladex.CreateEntity("IceArma28","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceEscudo28","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("2Esq","Skeleton",7300.31646551, -9071.4321271, -11991.0331074,"Person")
pers.Angle=4.69384135965
pers.Level=lvl_control.GiveLevel(9,11)
Actions.TakeObject(pers.Name,"IceArma28")
Actions.TakeObject(pers.Name,"IceEscudo28")
#pers.ActionAreaMin=pow(2,10)
#pers.ActionAreaMax=pow(2,11)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("2Esq")



############
#########################ESQUELETOS DE LA CRIPTA
################################################

o=Bladex.CreateEntity("IceeHachaCR1","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("CR1SKL","Skeleton",32964.6927408, 9879.72345214, 34670.5902,"Person")
pers.Angle=6.1
pers.Level=lvl_control.GiveLevel(9,12)
Actions.TakeObject(pers.Name,"IceeHachaCR1")
pers.ActionAreaMin=pow(2,30)
pers.ActionAreaMax=1<<31
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

ambiente5.AddGuy(pers.Name)
ambiente5.OnDeath = Suenamusica5


o=Bladex.CreateEntity("IceeHachaCR2","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("CR2SKL","Skeleton",29244.2047397, 9881.06844307, 30788.99470,"Person")
pers.Angle=6.1
pers.Level=lvl_control.GiveLevel(10,12)
Actions.TakeObject(pers.Name,"IceeHachaCR2")
pers.ActionAreaMin=pow(2,30)
pers.ActionAreaMax=1<<31
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

ambiente5.AddGuy(pers.Name)
ambiente5.OnDeath = Suenamusica5


o=Bladex.CreateEntity("IceeHachaCR4","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IceeEscCR4","Escudo1",0,0,0)
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("CR4SKL","Skeleton",40978.1781857, 8874.61938641, 25570.7167,"Person")
pers.Angle=0.65
pers.Level=lvl_control.GiveLevel(9,12)
Actions.TakeObject(pers.Name,"IceeHachaCR4")
Actions.TakeObject(pers.Name,"IceeEscCR4")
pers.ActionAreaMin=pow(2,30)
pers.ActionAreaMax=1<<31
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

ambiente5.AddGuy(pers.Name)
ambiente5.OnDeath = Suenamusica5

darfuncs.HideBadGuy("CR1SKL")
darfuncs.HideBadGuy("CR2SKL")
darfuncs.HideBadGuy("CR4SKL")


#darfuncs.MuertoyTroceado(77400,-1200,17000,"Knight_Traitor","",(1,5,7,2))