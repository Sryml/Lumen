from math import pow
import EnemyTypes
import Breakings
import Sparks
import Actions
import pocimac
import darfuncs
import ItemTypes
import LevelFuncs

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 1
expected_player_lvl_max= 6
lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)

# orcos exteriores en primer tramo hasta rastrillo


# orco mamon 1 a la izquierda del.. bla, bla, bla..con saquito racion
# Areas 1 y 2

saquito2orc=Bladex.CreateEntity("Saquito2orc","Saquito",0,0,0,"Physic")
saquito2orc.Solid=0
saquito2orc.Scale=1.220190
pocimac.CreatePotion("Saquito2orc")

Cimitarra2=Bladex.CreateEntity("LabyrGladius2","Gladius",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo2","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra2)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("2ORC","Ork",-11195.587509, 928.911474764, 43284.782207,"Person")
pers.Angle=4.73528938699
pers.Level=lvl_control.GiveLevel(1,3)
Actions.TakeObject(pers.Name,"LabyrGladius2")
Actions.TakeObject(pers.Name,"LabyrEscudo2")
Actions.TakeObject(pers.Name,"Saquito2orc")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("2ORC", "exterior")

#pers.AddBayPoint=-11195.587509, 928.911474764, 43284.782207
#pers.AddBayPoint=16101.0518923, 943.746102373, 44930.0759177
#pers.AddBayPoint=24783.0070428, 931.076412549, 45625.4705883
#pers.AddBayPoint=27145.9346273, 929.937284837, 43487.3911896
#pers.AddBayPoint=26057.2091716, 936.959992022, 41759.8066021
#pers.AddBayPoint=16101.0518923, 943.746102373, 44930.0759177
#pers.AddBayPoint=-11315.5949407, 1006.1042937, 47297.6883326
#pers.AddBayPoint=-14073.9952578, 941.997246601, 44170.0288377



## orco despistado
# Areas 1 y 2

Cimitarra3b=Bladex.CreateEntity("LabyrGladius3b","Garrote",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo3b","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra3b)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("3ORCb","Ork",27974.2542337, 989.551011421, 32881.3043258,"Person")
pers.Angle=3.89921012244
pers.Level=lvl_control.GiveLevel(2,4)
Actions.TakeObject(pers.Name,"LabyrGladius3b")
Actions.TakeObject(pers.Name,"LabyrEscudo3b")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("3ORC", "exterior")



## orco 1 vigilando rastrillo
# Areas 1 y 2

pocima50orc4=Bladex.CreateEntity("Pocima50orc4","Pocima50",0,0,0,"Physic")
pocima50orc4.Solid=0
pocima50orc4.Scale=1.220190
pocimac.CreatePotion("Pocima50orc4")

Cimitarra4=Bladex.CreateEntity("LabyrGladius4","Orksword",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo4","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra4)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("4ORC","Great_Ork",46295.4303708, 946.560498419, 7910.86425069,"Person")
pers.Angle=0.505036773869
pers.Level=lvl_control.GiveLevel(1,3)
Actions.TakeObject(pers.Name,"LabyrGladius4")
Actions.TakeObject(pers.Name,"LabyrEscudo4")
Actions.TakeObject(pers.Name,"Pocima50orc4")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("4ORC", "exterior")



# orcos interiores primer tramo hasta rastrillo
# Areas 3 y 4

Cimitarra5=Bladex.CreateEntity("LabyrGladius5","Maza",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo5","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra5)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("5ORC","Ork",-22076.5245677, -8074.25174338, 65328.9384972,"Person")
pers.Angle=4.75800846434
pers.Level=lvl_control.GiveLevel(2,5)
Actions.TakeObject(pers.Name,"LabyrGladius5")
Actions.TakeObject(pers.Name,"LabyrEscudo5")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("5ORC", "exterior")


# Areas 3 y 4

Cimitarra6=Bladex.CreateEntity("LabyrGladius6","Maza",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo6","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra6)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("6ORC","Ork",9833.3395426, -8071.23255414, 57663.6502687,"Person")
pers.Angle=0.250805629912
pers.Level=lvl_control.GiveLevel(2,4)
Actions.TakeObject(pers.Name,"LabyrGladius6")
Actions.TakeObject(pers.Name,"LabyrEscudo6")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Blind=1
pers.Deaf=1
#pers.Data.JoinGroup("6ORC", "exterior")



## orco taimado aguardando tras puerta cerrada ji, ji, ji..
# Areas 3 y 4

Cimitarra7=Bladex.CreateEntity("LabyrGladius7","Maza",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo7","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra7)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("7ORC","Ork",57678.4805135, -7068.89358308, 7583.01130795,"Person")
pers.Angle=0.114110719632
pers.Level=lvl_control.GiveLevel(3,5)
Actions.TakeObject(pers.Name,"LabyrGladius7")
Actions.TakeObject(pers.Name,"LabyrEscudo7")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Deaf=1
#pers.Data.JoinGroup("7ORC", "exterior")



## orco arquero colega del anterior
# Areas 3 y 4

pocima50Labyrarq3=Bladex.CreateEntity("Pocima50Labyrarq3","Pocima50",0,0,0,"Physic")
pocima50Labyrarq3.Solid=0
pocima50Labyrarq3.Scale=1.220190
pocimac.CreatePotion("Pocima50Labyrarq3")

enm=Bladex.CreateEntity("Labyrarq3", "Ork",38613.5330186, -7080.40737303, -73.1900538848,"Person")
enm.Angle=4.74196461006
enm.Level=lvl_control.GiveLevel(2,4)
enm.ActionAreaMin=pow(2,2)
enm.ActionAreaMax=pow(2,3)
Actions.TakeObject(pers.Name,"Pocima50Labyrarq3")

o=Bladex.CreateEntity("LabyrArqesp3","Maza",0,0,0,"Weapon")
inv=enm.GetInventory()
inv.AddWeapon("LabyrArqesp3")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrArqbow3","Arco",0,0,0,"Weapon")
inv.AddBow("LabyrArqbow3")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrArqquiver3","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs(o)
inv.AddQuiver("LabyrArqquiver3")
o.Data.ArrowsLeft=10

EnemyTypes.EnemyDefaultFuncs(enm)


# Orco en establo
# Areas 1 y 2

Cimitarra8b=Bladex.CreateEntity("LabyrGladius8b","Hacha",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo8b","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra8b)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("8ORCb","Ork",12020.5496902, 700.088821012, 55999.0153944,"Person")
pers.Angle=3.93809002338
pers.Level=lvl_control.GiveLevel(1,4)
Actions.TakeObject(pers.Name,"LabyrGladius8b")
Actions.TakeObject(pers.Name,"LabyrEscudo8b")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("8ORCb", "exterior")






###############
###############
###############
#################ORCOS EN PERIMETRO EXTERIOR TRAS ABRIR RASTRILLO. LOS 3 PRIMEROS
############### DEBEN VER MODIFICADAS SUS AREAS DE ACCION 


# Areas 17 y 18

Cimitarra9=Bladex.CreateEntity("LabyrGladius9","Gladius",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo9","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra9)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("9ORC","Ork",25169.9511808, 968.875589319, -39699.3440822,"Person")
pers.Angle=5.66116924923
pers.Level=lvl_control.GiveLevel(2,4)
Actions.TakeObject(pers.Name,"LabyrGladius9")
Actions.TakeObject(pers.Name,"LabyrEscudo9")
pers.ActionAreaMin=pow(2,16)
pers.ActionAreaMax=pow(2,17)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("9ORC", "exterior")



## orco 2 en mitad de otra escalera
# Areas 19 y 20

Cimitarra10a=Bladex.CreateEntity("LabyrGladius10a","Hacha",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo10a","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra10a)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("10ORCa","Ork",21367.2411537, -2837.01349949, -65808.4882139,"Person")
pers.Angle=5.63171453942
pers.Level=lvl_control.GiveLevel(3,5)
Actions.TakeObject(pers.Name,"LabyrGladius10a")
Actions.TakeObject(pers.Name,"LabyrEscudo10a")
pers.ActionAreaMin=pow(2,18)
pers.ActionAreaMax=pow(2,19)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("10ORC", "exterior")


# Areas 17 y 18

Cimitarra10b=Bladex.CreateEntity("LabyrGladius10b","Maza",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo10b","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra10b)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("10ORCb","Ork",-26995.3486757, 960.507401152, -47814.4677108,"Person")
pers.Angle=5.4958629088
pers.Level=lvl_control.GiveLevel(3,5)
Actions.TakeObject(pers.Name,"LabyrGladius10b")
Actions.TakeObject(pers.Name,"LabyrEscudo10b")
pers.ActionAreaMin=pow(2,16)
pers.ActionAreaMax=pow(2,17)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("10ORC", "exterior")



## orco papando moscas
# Areas 17 y 18

Cimitarra11=Bladex.CreateEntity("LabyrGladius11","Orksword",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo11","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra11)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("11ORC","Great_Ork",-49811.3237844, 963.513486665, -10033.0971542,"Person")
pers.Angle=4.26658972271
pers.Level=lvl_control.GiveLevel(2,4)
Actions.TakeObject(pers.Name,"LabyrGladius11")
Actions.TakeObject(pers.Name,"LabyrEscudo11")
pers.ActionAreaMin=pow(2,16)
pers.ActionAreaMax=pow(2,17)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("11ORC", "exterior")



# Orco arquero 1
# Areas 19 y 20

enm=Bladex.CreateEntity("Labyrarq1", "Ork",-7059.07364518, -8071.91786723, -59659.5146591,"Person")
enm.Angle=5.30636459658
enm.Level=lvl_control.GiveLevel(3,4)
enm.ActionAreaMin=pow(2,18)
enm.ActionAreaMax=pow(2,19)

o=Bladex.CreateEntity("LabyrArqesp1","Maza",0,0,0,"Weapon")
inv=enm.GetInventory()
inv.AddWeapon("LabyrArqesp1")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrArqbow1","Arco",0,0,0,"Weapon")
inv.AddBow("LabyrArqbow1")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrArqquiver1","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs(o)
inv.AddQuiver("LabyrArqquiver1")
o.Data.ArrowsLeft=10

EnemyTypes.EnemyDefaultFuncs(enm)

darfuncs.HideBadGuy("Labyrarq1")

######## Funcion: CreaOrcoListo()

######## Funcion: CorreOrcoListo()

######## Funcion: MueveOrcoListo(Entity)

sectx1=Bladex.GetSector(-20202.2381191, 928.231043982, 44365.7558512)

######## Funcion: x1(sectorindex,entityname)

sectx1.OnEnter=x1



## ultimo orco del perimetro exterior
# Areas 21 y 22

Cimitarra12b=Bladex.CreateEntity("LabyrGladius12b","Orksword",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo12b","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra12b)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("12bORC","Great_Ork",-51500, -7030.59731496, -4600,"Person")
pers.Level=lvl_control.GiveLevel(3,4)
pers.Angle=1.59723992684
Actions.TakeObject(pers.Name,"LabyrGladius12b")
Actions.TakeObject(pers.Name,"LabyrEscudo12b")
pers.ActionAreaMin=pow(2,20)
pers.ActionAreaMax=pow(2,21)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("12ORC", "exterior")
pers.Position=-40000, -7030.59731496, -2.3033989468






#############orcos arqueros congelados en perimetro interior

# Areas 23 y 24

pocima100labyrarq4=Bladex.CreateEntity("Pocima100Labyrarq4","Pocima100",0,0,0,"Physic")
pocima100labyrarq4.Solid=1
pocima100labyrarq4.Scale=1.220190
pocimac.CreatePotion("Pocima100Labyrarq4")

enm=Bladex.CreateEntity("Labyrarq4", "Ork",33883.3564534, -7031.6075783, -2892.26324591,"Person")
enm.Angle=2.55644921808
enm.Level=lvl_control.GiveLevel(2,5)
enm.ActionAreaMin=pow(2,22)
enm.ActionAreaMax=pow(2,23)
Actions.TakeObject(pers.Name,"Pocima100Labyrarq4")


o=Bladex.CreateEntity("LabyrArqesp4","Maza",0,0,0,"Weapon")
inv=enm.GetInventory()
inv.AddWeapon("LabyrArqesp4")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrArqbow4","Arco",0,0,0,"Weapon")
inv.AddBow("LabyrArqbow4")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrArqquiver4","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs(o)
inv.AddQuiver("LabyrArqquiver4")
o.Data.ArrowsLeft=10

EnemyTypes.EnemyDefaultFuncs(enm)

darfuncs.HideBadGuy("Labyrarq4")

######## Funcion: CreaLabyrarq4()
	

sectx4=Bladex.GetSector(-36881.3806616, -7075.90386161, 318.319750917)

######## Funcion: x4(sectorindex,entityname)

sectx4.OnEnter=x4



# Areas 23 y 24

enm=Bladex.CreateEntity("Labyrarq5", "Ork",-33258.3412789, -7053.73678965, -3559.76294538,"Person")
enm.Angle=3.71864433083
enm.Level=lvl_control.GiveLevel(2,4)
enm.ActionAreaMin=pow(2,22)
enm.ActionAreaMax=pow(2,23)

o=Bladex.CreateEntity("LabyrArqesp5","Hacha",0,0,0,"Weapon")
inv=enm.GetInventory()
inv.AddWeapon("LabyrArqesp5")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrArqbow5","Arco",0,0,0,"Weapon")
inv.AddBow("LabyrArqbow5")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrArqquiver5","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs(o)
inv.AddQuiver("LabyrArqquiver5")
o.Data.ArrowsLeft=10

EnemyTypes.EnemyDefaultFuncs(enm)

darfuncs.HideBadGuy("Labyrarq5")

######## Funcion: CreaLabyrarq5()

sectx5=Bladex.GetSector(21681.8352986, -1032.3364653, -21563.965888)

######## Funcion: x5(sectorindex,entityname)

sectx5.OnEnter=x5



######### orco arquero congelado en zona exterior torre
# Areas 23 y 24

enm=Bladex.CreateEntity("Labyrarq6", "Ork",12100.8707996, -9068.2272798, 12157.851132,"Person") # -12100.8707996, -9068.2272798, 12157.851132,"Person")
enm.Level=lvl_control.GiveLevel(0,3)
enm.Angle=3.6
enm.ActionAreaMin=pow(2,22)
enm.ActionAreaMax=pow(2,23)

o=Bladex.CreateEntity("LabyrArqesp6","Garrote",0,0,0,"Weapon")
inv=enm.GetInventory()
inv.AddWeapon("LabyrArqesp6")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrArqbow6","Arco",0,0,0,"Weapon")
inv.AddBow("LabyrArqbow6")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrArqquiver6","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs(o)
inv.AddQuiver("LabyrArqquiver6")
o.Data.ArrowsLeft=10

EnemyTypes.EnemyDefaultFuncs(enm)

darfuncs.HideBadGuy("Labyrarq6")

######## Funcion: CreaLabyrarq6()

sectx6=Bladex.GetSector(-49811.3237844, 963.513486665, -10033.0971542)

######## Funcion: x6(sectorindex,entityname)

sectx6.OnEnter=x6



######### orco arquero congelado sobre puerta torre central

# Areas 25 y 26

enm=Bladex.CreateEntity("Labyrarq6b", "Ork",4546.29137754, -10072.5529467, 26105.7494362,"Person")
enm.Level=lvl_control.GiveLevel(0,3)
enm.Angle=-3.14159/2
enm.ActionAreaMin=pow(2,24)
enm.ActionAreaMax=pow(2,25)
enm.SetOnFloor()

o=Bladex.CreateEntity("LabyrArqesp6b","Garrote",0,0,0,"Weapon")
inv=enm.GetInventory()
inv.AddWeapon("LabyrArqesp6b")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrArqbow6b","Arco",0,0,0,"Weapon")
inv.AddBow("LabyrArqbow6b")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrArqquiver6b","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs(o)
inv.AddQuiver("LabyrArqquiver6b")
o.Data.ArrowsLeft=10

EnemyTypes.EnemyDefaultFuncs(enm)

darfuncs.HideBadGuy("Labyrarq6b")





###################################### orcos en perimetro interior


#orco patrullando bobaliconamente 
# Areas 7 y 8

Cimitarra13=Bladex.CreateEntity("LabyrGladius13","Maza",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo13","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra13)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("13ORC","Ork",-17908.27348, -1111.18079826, -24756.4784718,"Person")
pers.Level= lvl_control.GiveLevel(3,5)
pers.Angle=4.15139877484
Actions.TakeObject(pers.Name,"LabyrGladius13")
Actions.TakeObject(pers.Name,"LabyrEscudo13")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("13ORC", "exterior")

#pers.AddBayPoint=-17908.27348, -1060.27253597, -24756.4784718
#pers.AddBayPoint=-6543.94589756, -1075.03642868, -32131.7017467
#pers.AddBayPoint=6123.19675555, -1053.75217256, -32522.2932065
#pers.AddBayPoint=6093.74076022, -1087.35320566, -26976.4796208
#pers.AddBayPoint=-5129.85956625, -1071.07936611, -26511.0862816
#pers.AddBayPoint=-12883.5671744, -1056.33490011, -18919.3414671



#orco p3
# Areas 7 y 8

Cimitarra15=Bladex.CreateEntity("LabyrGladius15","Hacha",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo15","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra15)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("15ORC","Ork",31550.0645441, -1111.18079826, -12449.1503736,"Person")
pers.Level=lvl_control.GiveLevel(2,5)
pers.Angle=2.33508163815
Actions.TakeObject(pers.Name,"LabyrGladius15")
Actions.TakeObject(pers.Name,"LabyrEscudo15")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("15ORC", "exterior")

#pers.AddBayPoint=31550.0645441, -1038.31095158, -12449.1503736
#pers.AddBayPoint=32721.513028, -1102.45446631, -102.985686836
#pers.AddBayPoint=32534.7072404, -1104.41489726, 6121.53592097
#pers.AddBayPoint=28104.3339651, -1127.92774615, 13032.1680532
#pers.AddBayPoint=32534.7072404, -1104.41489726, 6121.53592097
#pers.AddBayPoint=32721.513028, -1102.45446631, -102.985686836





###################################### orcos en perimetro interior


#orco p4b
# Areas 5 y 6

Cimitarra17=Bladex.CreateEntity("LabyrGladius17","Maza",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo17","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra17)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("17ORC","Ork",10963.439517, -1111.18079826, 26891.2164484,"Person")
pers.Level=lvl_control.GiveLevel(4,6)
pers.Angle=4.34104059393
Actions.TakeObject(pers.Name,"LabyrGladius17")
Actions.TakeObject(pers.Name,"LabyrEscudo17")
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("17ORC", "exterior")

#pers.AddBayPoint=10963.439517, -1058.24703976, 26891.2164484
#pers.AddBayPoint=4780.6276668, -1117.39295379, 30972.052284
#pers.AddBayPoint=-4780.6276668, -1117.39295379, 30972.052284
#pers.AddBayPoint=-12036.725594, -1102.60354919, 27640.310141
#pers.AddBayPoint=-13730.6192475, -1125.77970583, 22835.9265606
#pers.AddBayPoint=-11520.1014277, -1129.15663293, 20680.6335677
#pers.AddBayPoint=-8805.65809772, -1099.41205292, 22330.1493014
#pers.AddBayPoint=-7450.90797465, -1122.77145559, 25342.244108
#pers.AddBayPoint=-7053.77611587, -1105.36120825, 30340.6736805
#pers.AddBayPoint=4780.6276668, -1117.39295379, 30972.052284



#orco p5

#Cimitarra17b=Bladex.CreateEntity("LabyrGladius17b","Orksword",0,0,0,"Weapon")
#escudo=Bladex.CreateEntity("LabyrEscudo17b","Escudo1",0,0,0,"Weapon")
#ItemTypes.ItemDefaultFuncs(Cimitarra17b)
#ItemTypes.ItemDefaultFuncs(escudo)

#pers=Bladex.CreateEntity("17ORCb","Great_Ork",6815.480906, -1045.40616884, 29940.9049757,"Person")
#pers.Level=3
#pers.Angle=4.26526095071
#Actions.TakeObject(pers.Name,"LabyrGladius17b")
#Actions.TakeObject(pers.Name,"LabyrEscudo17b")
#pers.ActionAreaMin=pow(2,4)
#pers.ActionAreaMax=pow(2,5)
#EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("17ORCb", "exterior")



# Areas 5 y 6

enm=Bladex.CreateEntity("Labyrarq2", "Ork",-26157.8115449, -1069.43116039, 9773.06157285,"Person")
enm.Angle=3.93068133475
enm.Level=lvl_control.GiveLevel(3,5)
enm.ActionAreaMin=pow(2,4)
enm.ActionAreaMax=pow(2,5)
enm.Position=-29111.723854, -1069.43116039, 16775.8412149

o=Bladex.CreateEntity("LabyrArqesp2","Maza",0,0,0,"Weapon")
inv=enm.GetInventory()
inv.AddWeapon("LabyrArqesp2")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrArqbow2","Arco",0,0,0,"Weapon")
inv.AddBow("LabyrArqbow2")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrArqquiver2","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs(o)
inv.AddQuiver("LabyrArqquiver2")
o.Data.ArrowsLeft=10

EnemyTypes.EnemyDefaultFuncs(enm)






##########################
##########################
##########################
##########################
##########################
##########################
########################## orcos en interior fortaleza de Duke Nukem

##
####### Orcos en recibidor
##

## colocar pocion a este??
# Areas 9 y 10

Cimitarra19=Bladex.CreateEntity("LabyrGladius19","Orksword",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo19","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra19)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("19ORC","Great_Ork",3917.09184428, -2055.91940894, 1591.4822367,"Person") # 75.4174286021, -2063.95361387, -2489.73818363,"Person")
pers.Angle=1.570795 # 6.2611700272
pers.Level=lvl_control.GiveLevel(2,4)
Actions.TakeObject(pers.Name,"LabyrGladius19")
Actions.TakeObject(pers.Name,"LabyrEscudo19")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("19ORC", "exterior")


# Areas 9 y 10

Cimitarra3=Bladex.CreateEntity("LabyrGladius3","Hacha",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo3","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra3)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("3ORC","Ork",-7318.7672762, -2019.20328836, 11479.0912428,"Person")
pers.Angle=4.21198804966
pers.Level=lvl_control.GiveLevel(3,5)
Actions.TakeObject(pers.Name,"LabyrGladius3")
Actions.TakeObject(pers.Name,"LabyrEscudo3")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("3ORC", "exterior")



##
####### Orcos en primer piso
##

# Areas 11 y 12

Cimitarra20=Bladex.CreateEntity("LabyrGladius20","Gladius",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo20","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra20)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("20ORC","Ork",13386.1140985, -10323.0520814, -1408.13620262,"Person")
pers.Level=lvl_control.GiveLevel(2,4)
pers.Angle=1.02082713473
Actions.TakeObject(pers.Name,"LabyrGladius20")
Actions.TakeObject(pers.Name,"LabyrEscudo20")
pers.ActionAreaMin=pow(2,10)
pers.ActionAreaMax=pow(2,11)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("20ORC", "exterior")


# Areas 11 y 12

Cimitarra14=Bladex.CreateEntity("LabyrGladius14","Gladius",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo14","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra14)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("14ORC","Ork",-16397.9188781, -10360.0977018, 1269.37512684,"Person")
pers.Level=lvl_control.GiveLevel(1,4)
pers.Angle=3.9531259451
Actions.TakeObject(pers.Name,"LabyrGladius14")
Actions.TakeObject(pers.Name,"LabyrEscudo14")
pers.ActionAreaMin=pow(2,10)
pers.ActionAreaMax=pow(2,11)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("14ORC", "exterior")




##
####### Orcos finales
##


## Orco almacen (segundo piso)
# Areas 13 y 14

Cimitarra21=Bladex.CreateEntity("LabyrGladius21","Maza",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo21","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra21)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("21ORC","Ork",61.3244545388, -18069.9076164, 10025.8004267,"Person")
pers.Level=lvl_control.GiveLevel(3,5)
pers.Angle=3.12639019638
Actions.TakeObject(pers.Name,"LabyrGladius21")
Actions.TakeObject(pers.Name,"LabyrEscudo21")
pers.ActionAreaMin=pow(2,12)
pers.ActionAreaMax=pow(2,13)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("21ORC", "exterior")


## Orco primer descansillo (segundo piso)
# Areas 13 y 14

Cimitarra16=Bladex.CreateEntity("LabyrGladius16","Maza",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo16","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra16)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("16ORC","Ork",-1623.9596329, -16622.9476294, 4786.88000013,"Person")
pers.Level= lvl_control.GiveLevel(2,4)
pers.Angle=1.55054561667
Actions.TakeObject(pers.Name,"LabyrGladius16")
Actions.TakeObject(pers.Name,"LabyrEscudo16")
pers.ActionAreaMin=pow(2,12)
pers.ActionAreaMax=pow(2,13)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("16ORC", "exterior")


#Cimitarra22=Bladex.CreateEntity("LabyrGladius22","Gladius",0,0,0,"Weapon")
#escudo=Bladex.CreateEntity("LabyrEscudo22","Escudo5",0,0,0,"Weapon")
#ItemTypes.ItemDefaultFuncs(Cimitarra22)
#ItemTypes.ItemDefaultFuncs(escudo)

#pers=Bladex.CreateEntity("22ORC","Ork",13523.6233076, -20155.8533953, 1259.85945102,"Person")
#pers.Level=5
#pers.Angle=1.55920221529
#Actions.TakeObject(pers.Name,"LabyrGladius22")
#Actions.TakeObject(pers.Name,"LabyrEscudo22")
#pers.ActionAreaMin=pow(2,12)
#pers.ActionAreaMax=pow(2,13)
#EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("21ORC", "exterior")


## Orco descansillo hacia tercer piso
# Areas 13 y 14

Cimitarra23=Bladex.CreateEntity("LabyrGladius23","Garrote",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo23","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra23)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("23ORC","Ork",-17003.8938156, -21380.4407636, -2446.99927244,"Person")
pers.Level=lvl_control.GiveLevel(3,5)
pers.Angle=5.77751218573
Actions.TakeObject(pers.Name,"LabyrGladius23")
Actions.TakeObject(pers.Name,"LabyrEscudo23")
pers.ActionAreaMin=pow(2,12)
pers.ActionAreaMax=pow(2,13)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("21ORC", "exterior")




## Orco puerta azotea
# Areas 15 y 16

Cimitarra24=Bladex.CreateEntity("LabyrGladius24","Maza",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo24","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra24)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("24ORC","Ork",-41.438646139, -27064.5963117, 583.800838625,"Person")
pers.Level=lvl_control.GiveLevel(3,4)
pers.Angle=3.17144515817
Actions.TakeObject(pers.Name,"LabyrGladius24")
Actions.TakeObject(pers.Name,"LabyrEscudo24")
pers.ActionAreaMin=pow(2,14)
pers.ActionAreaMax=pow(2,15)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("21ORC", "exterior")



## Jefe orco azotea
# Areas 15 y 16

Cimitarra25=Bladex.CreateEntity("LabyrGladius25","Maza",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("LabyrEscudo25","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Cimitarra25)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("25ORC","Great_Ork",-349.710110346, -29572.9468567, 10966.3128413,"Person") # 4800.20044297, -27050.0431415, -8449.19040859,"Person")
pers.Angle=3.16971034531
pers.Level=lvl_control.GiveLevel(3,5)
Actions.TakeObject(pers.Name,"LabyrGladius25")
Actions.TakeObject(pers.Name,"LabyrEscudo25")
pers.ActionAreaMin=pow(2,14)
pers.ActionAreaMax=pow(2,15)
EnemyTypes.EnemyDefaultFuncs(pers)
#pers.Data.JoinGroup("21ORC", "exterior")

######## Funcion: CorreOrcohijoputa()

#Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, CorreOrcohijoputa,())
