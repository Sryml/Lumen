from math import pow
import EnemyTypes
import Actions



##Orco acechando taimadamente al principio del mapa Gladius en ristre. Sin area de accion

#orco 1

Gladius=Bladex.CreateEntity("RuinsGladius1","Garrote",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)

pers=Bladex.CreateEntity("1orc","Ork",63750,-1000,-14000,"Person")
pers.Angle=1.5
pers.Level=0
Actions.TakeObject(pers.Name,"RuinsGladius1")
pers.ActionAreaMin=pow(2,30)
pers.ActionAreaMax=1<<31
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.ImDeadFuncX=pers.ImDeadFunc
pers.ImDeadFunc=AmazonDefeatsOrc
pers.SetOnFloor()


## 3 orcos apestosos más, socios de los 2 anteriores, merodean en los alrededores del puente con Gladiuss.


#orco 4 en puente. Areas 3 y 4.

Gladius=Bladex.CreateEntity("RuinsGladius4","Garrote",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("RuinsEsc4orc","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("4orc","Ork",50000,-2000,32250,"Person")
pers.Angle=2.3 #0.75
pers.Level=2
Actions.TakeObject(pers.Name,"RuinsGladius4")
Actions.TakeObject(pers.Name,"RuinsEsc4orc")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.ImDeadFuncX=pers.ImDeadFunc
pers.ImDeadFunc=AmazonDefeatsOrc
pers.SetOnFloor()

pers.Freeze()



#orco 5 en alrededores puente. Areas 5 y 6.

Gladius=Bladex.CreateEntity("RuinsGladius5","Gladius",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("RuinsEsc5orc","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("5orc","Ork",32000,-1000,42000,"Person")
pers.Angle=0.75
pers.Level=1
Actions.TakeObject(pers.Name,"RuinsGladius5")
Actions.TakeObject(pers.Name,"RuinsEsc5orc")
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.ImDeadFuncX=pers.ImDeadFunc
pers.ImDeadFunc=AmazonDefeatsOrc
pers.SetOnFloor()

pers.Blind=1
pers.Deaf=1

pers.Freeze()

sec1actenelab=Bladex.GetSector(36000, -1000, 32000)
sec2actenelab=Bladex.GetSector(30000, -1000, 30000)
secdesenelab=Bladex.GetSector(24000, -1000, 42000)

######## Funcion: ActivaOrco5(SectorIndex,EntityName)

######## Funcion: DesactivaOrco5(SectorIndex,EntityName)

sec1actenelab.OnEnter=ActivaOrco5
sec2actenelab.OnEnter=ActivaOrco5
secdesenelab.OnEnter=DesactivaOrco5



#orco 6 en alrededores puente. Areas 7 y 8.

Gladius=Bladex.CreateEntity("RuinsGladius6","Garrote",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("RuinsEsc6orc","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("6orc","Ork",48750,-1000,42750,"Person")
pers.Angle=0.75
pers.Level=2
Actions.TakeObject(pers.Name,"RuinsGladius6")
Actions.TakeObject(pers.Name,"RuinsEsc6orc")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.goto_limit2aa=0
pers.Data.ImDeadFuncX=pers.ImDeadFunc
pers.ImDeadFunc=AmazonDefeatsOrc
pers.SetOnFloor()

pers.Freeze()


## Por si no hubieran bastantes.. ¡2 orcos malolientes más frente a una pirámide! Areas 9 y 10.

## Deberían patrullar
#orco maloliente 8

Gladius=Bladex.CreateEntity("RuinsGladius8","Gladius",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)

pers=Bladex.CreateEntity("8orc","Ork",-16500,-1000,3000,"Person")
pers.Angle=1.5
pers.Level=1
Actions.TakeObject(pers.Name,"RuinsGladius8")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.ImDeadFuncX=pers.ImDeadFunc
pers.ImDeadFunc=AmazonDefeatsOrc
pers.SetOnFloor()



#orco maloliente 9

Gladius=Bladex.CreateEntity("RuinsGladius9","Garrote",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("RuinsEsc9orc","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("9orc","Ork",-16500,-1000,-3000,"Person")
pers.Angle=1.5
pers.Level=1
Actions.TakeObject(pers.Name,"RuinsGladius9")
Actions.TakeObject(pers.Name,"RuinsEsc9orc")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.ImDeadFuncX=pers.ImDeadFunc
pers.ImDeadFunc=AmazonDefeatsOrc
pers.SetOnFloor()



## .. No se vayan todavía, ¡aún hay más! 2 orquitos adorables en el interior zona NorOeste. Areas 11 y 12.


#orquito adorable 10

Gladius=Bladex.CreateEntity("RuinsGladius10","Hacha",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("RuinsEsc10orc","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("10orc","Ork",-35500,-1000,28000,"Person")
pers.Angle=5
pers.Level=3
Actions.TakeObject(pers.Name,"RuinsGladius10")
Actions.TakeObject(pers.Name,"RuinsEsc10orc")
pers.ActionAreaMin=pow(2,10)
pers.ActionAreaMax=pow(2,11)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.ImDeadFuncX=pers.ImDeadFunc
pers.ImDeadFunc=AmazonDefeatsOrc
pers.SetOnFloor()

pers.Freeze()


#orquito adorable 11

Gladius=Bladex.CreateEntity("RuinsGladius11","Garrote",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("RuinsEsc11orc","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("11orc","Ork",-28000,-1000,35500,"Person")
pers.Angle=2.7
pers.Level=3
Actions.TakeObject(pers.Name,"RuinsGladius11")
Actions.TakeObject(pers.Name,"RuinsEsc11orc")
pers.ActionAreaMin=pow(2,10)
pers.ActionAreaMax=pow(2,11)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.ImDeadFuncX=pers.ImDeadFunc
pers.ImDeadFunc=AmazonDefeatsOrc
pers.SetOnFloor()

pers.Freeze()



##orco gay patrullando en lo alto de la piramide central 19 y 20.

potion=Bladex.CreateEntity("RuinsPotiongay","Pocima100",0,0,0,"Physic")
potion.Solid=0
potion.Scale=1.220190
pocimac.CreatePotion("RuinsPotiongay")

Gladius=Bladex.CreateEntity("RuinsGladius15","Garrote",0,0,0,"Weapon") #"Orksword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)


pers=Bladex.CreateEntity("15orc","Ork",0,-13590,-10500,"Person") #"Great_Ork",0,-13590,-10500,"Person")
pers.Angle=5.33479707957
pers.Level=1
Actions.TakeObject(pers.Name,"RuinsGladius15")
pers.ActionAreaMin=pow(2,18)
pers.ActionAreaMax=pow(2,19)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.ImDeadFuncX=pers.ImDeadFunc
pers.ImDeadFunc=AmazonDefeatsOrc
Actions.TakeObject(pers.Name,"RuinsPotiongay")
pers.SetOnFloor()

#pers.AddBayPoint=0, -13590, -10500
#pers.AddBayPoint=6000, -13590, -6000
#pers.AddBayPoint=10500, -13590, 0
#pers.AddBayPoint=6000, -13590, 6000
#pers.AddBayPoint=0, -13590, 10500
#pers.AddBayPoint=-6000, -13590, 6000
#pers.AddBayPoint=-10500, -13590, 0
#pers.AddBayPoint=-6000, -13590, -6000



##10 esqueletos horripilantes en zona cementerio SE. Las areas de accion min y max son 13 y 14 


#OJO! Estan en el Cementerio.py



###### LOS QUE DEBERIAN ESTAR PATRULLANDO!! ######


##Orco 16 patrullando en al empezar el mapa.No Areas.

Gladius=Bladex.CreateEntity("RuinsGladius16","Garrote",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)

pers=Bladex.CreateEntity("16orc","Ork",40000.0, -1112.0, -17500.0,"Person")
pers.Angle=0.0356775304217
pers.Level=0
Actions.TakeObject(pers.Name,"RuinsGladius16")
pers.ActionAreaMin=pow(2,30)
pers.ActionAreaMax=1<<31
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.ImDeadFuncX=pers.ImDeadFunc
pers.ImDeadFunc=AmazonDefeatsOrc
pers.SetOnFloor()

#pers.AddBayPoint=40000.0, -1112.0, -17500.0
#pers.AddBayPoint=21500.0, -1112.0, -17000.0
#pers.AddBayPoint=20000.0, -1112.0, -14000.0
#pers.AddBayPoint=21000.0, -1112.0, 0.0
#pers.AddBayPoint=20000.0, -1112.0, 14000.0
#pers.AddBayPoint=22000.0, -1112.0, 17000.0
#pers.AddBayPoint=40000.0, -1112.0, 18000.0
#pers.AddBayPoint=22000.0, -1112.0, 17000.0
#pers.AddBayPoint=20000.0, -1112.0, 14000.0
#pers.AddBayPoint=21000.0, -1112.0, 0.0
#pers.AddBayPoint=20000.0, -1112.0, -14000.0
#pers.AddBayPoint=21500.0, -1112.0, -17000.0





##Orco 12 patrullando en zona Norte alrededor de una pirámide. Sin area de acción.


Gladius=Bladex.CreateEntity("RuinsGladius12","Garrote",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)

pers=Bladex.CreateEntity("12orc","Ork",-15750,-1000,57250,"Person")
pers.Angle=3 #1.5
pers.Level=0
Actions.TakeObject(pers.Name,"RuinsGladius12")
pers.ActionAreaMin=pow(2,30)
pers.ActionAreaMax=1<<31
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.ImDeadFuncX=pers.ImDeadFunc
pers.ImDeadFunc=AmazonDefeatsOrc
pers.SetOnFloor()

#pers.AddBayPoint=-15750,-1000,57250
#pers.AddBayPoint=-20750,-1000,46250
#pers.AddBayPoint=-17250,-1000,36000
#pers.AddBayPoint=-18000,-1000,22000
#pers.AddBayPoint=-14000,-1000,20000
#pers.AddBayPoint=14000,-1000,20000
#pers.AddBayPoint=17000,-1000,21500
#pers.AddBayPoint=18000,-1000,41500
#pers.AddBayPoint=21000,-1000,46000
#pers.AddBayPoint=15500,-1000,57250




##Orco 13 patrullando en zona Sur. Sin area de acción.


Gladius=Bladex.CreateEntity("RuinsGladius13","Garrote",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)

pers=Bladex.CreateEntity("13orc","Ork",15000,-1000,-57500,"Person")
pers.Angle=1.5
pers.Level=0
Actions.TakeObject(pers.Name,"RuinsGladius13")
pers.ActionAreaMin=pow(2,30)
pers.ActionAreaMax=1<<31
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.ImDeadFuncX=pers.ImDeadFunc
pers.ImDeadFunc=AmazonDefeatsOrc
pers.SetOnFloor()

#pers.AddBayPoint=15000,-1000,-57500
#pers.AddBayPoint=21000,-1000,-46000
#pers.AddBayPoint=17750,-1000,-36000
#pers.AddBayPoint=17000,-1000,-21500
#pers.AddBayPoint=14000,-1000,-20000
#pers.AddBayPoint=0,-1000,-20000
#pers.AddBayPoint=-14000,-1000,-20000
#pers.AddBayPoint=-17250,-1000,-22000
#pers.AddBayPoint=-17250,-1000,-39250
#pers.AddBayPoint=-20500,-1000,-45250
#pers.AddBayPoint=-15750,-1000,-56750



### ATENCION!!!
### Hay tres enemigos mas en el script del pozo:
### - Un jefe orco con areas 1 y 2 que guarda la puerta de acceso a la fuente 3
### - Dos orcos con areas 17 y 18 que aparecen cuando activamos las fuentes 1 y 2



### MUERTOS VIVIENTES MERLUZOIDES EN CATACUMBAS


#tras generador 2 y antes de puente que se rompe. Areas 23 24

#1

pers=Bladex.CreateEntity("Beej1","Lich",28000, 7910.83056043, -53380.5956018,"Person")
pers.Angle=5.02497039344
pers.Level=0
pers.ActionAreaMin=pow(2,22)
pers.ActionAreaMax=pow(2,23)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

pers.Freeze()



#2

pers=Bladex.CreateEntity("Beej2","Lich",23289.9188824, 7905.8613011, -55711.9454813,"Person")
pers.Angle=4.83888113356
pers.Level=0
pers.ActionAreaMin=pow(2,22)
pers.ActionAreaMax=pow(2,23)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

pers.Freeze()


#3

pers=Bladex.CreateEntity("Beej3","Lich",3295.55495171, 7913.80905795, -62374.2905767,"Person")
pers.Angle=5.2250823893
pers.Level=0
pers.ActionAreaMin=pow(2,22)
pers.ActionAreaMax=pow(2,23)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

pers.Freeze()


## tras puente que se rompe y antes de zona sepulcro areas 21, 22.


#4

Hachabeej4=Bladex.CreateEntity("RuinsHachabeej4","Hacha",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Hachabeej4)

pers=Bladex.CreateEntity("Beej4","Lich",-25550.6993636, 7661.62293911, -49536.5500976,"Person")
pers.Angle=4.68199689632
pers.Level=1
pers.ActionAreaMin=pow(2,20)
pers.ActionAreaMax=pow(2,21)
Actions.TakeObject(pers.Name,"RuinsHachabeej4")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

pers.Freeze()


#5

pers=Bladex.CreateEntity("Beej5","Lich",-29291.3893231, 6918.28995449, -58693.8800449,"Person")
pers.Angle=6.04452380889
pers.Level=0
pers.ActionAreaMin=pow(2,20)
pers.ActionAreaMax=pow(2,21)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

pers.Freeze()


#6

Hachabeej6=Bladex.CreateEntity("RuinsHachabeej6","Garrote",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Hachabeej6)

pers=Bladex.CreateEntity("Beej6","Lich",-32458.7098738, 6911.38356765, -69292.6454364,"Person")
pers.Angle=5.97624982108
pers.Level=1
pers.ActionAreaMin=pow(2,20)
pers.ActionAreaMax=pow(2,21)
Actions.TakeObject(pers.Name,"RuinsHachabeej6")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

pers.Freeze()




## tras sepulcro areas 25, 26


#7

Hachabeej7=Bladex.CreateEntity("RuinsHachabeej7","Hacha",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Hachabeej7)

pers=Bladex.CreateEntity("Beej7","Lich",-71690.4295932, 4895.92124613, -29937.7879119,"Person")
pers.Angle=4.11602355557
pers.Level=1
pers.ActionAreaMin=pow(2,24)
pers.ActionAreaMax=pow(2,25)
Actions.TakeObject(pers.Name,"RuinsHachabeej7")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

pers.Freeze()


#8

pers=Bladex.CreateEntity("Beej8","Lich",-78518.3987108, 4898.74128975, -22111.404962,"Person")
pers.Angle=3.17154677813
pers.Level=1
pers.ActionAreaMin=pow(2,24)
pers.ActionAreaMax=pow(2,25)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

## en zona trampa areas 27, 28

pers.Freeze()


#9

pers=Bladex.CreateEntity("Beej9","Lich",-76810.605114, 4924.73465117, 3973.388881,"Person")
pers.Angle=3.03110101595
pers.Level=0
pers.ActionAreaMin=pow(2,26)
pers.ActionAreaMax=pow(2,27)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

pers.Freeze()


#10

pers=Bladex.CreateEntity("Beej10","Lich",-68243.6073818, 4921.56444521, 5451.96502711,"Person")
pers.Angle=2.06330197475
pers.Level=0
pers.ActionAreaMin=pow(2,26)
pers.ActionAreaMax=pow(2,27)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

pers.Freeze()


## tras trampa y antes puerta final areas 15, 16


#11

Hachabeej11=Bladex.CreateEntity("RuinsHachabeej11","Hacha",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Hachabeej11)

pers=Bladex.CreateEntity("Beej11","Lich",-28299.5569147, 5902.47745314, 14418.2035836,"Person")
pers.Angle=1.55087033484
pers.Level=1
pers.ActionAreaMin=pow(2,14)
pers.ActionAreaMax=pow(2,15)
Actions.TakeObject(pers.Name,"RuinsHachabeej11")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

pers.Freeze()


#12

Hachabeej12=Bladex.CreateEntity("RuinsHachabeej12","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Hachabeej12)

pers=Bladex.CreateEntity("Beej12","Lich",-25434.9877139, 5918.63896997, 10970.0037556,"Person")
pers.Angle=1.17586899882
pers.Level=1
pers.ActionAreaMin=pow(2,14)
pers.ActionAreaMax=pow(2,15)
Actions.TakeObject(pers.Name,"RuinsHachabeej12")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

pers.Freeze()


## tras trampa y antes zona ultima llave, areas 25, 26

#13

pers=Bladex.CreateEntity("Beej13","Lich",-63063.4398694, 4913.2515481, 27060.7946051,"Person")
pers.Angle=2.17168614962
pers.Level=0
pers.ActionAreaMin=pow(2,24)
pers.ActionAreaMax=pow(2,25)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

pers.Freeze()


#14

pers=Bladex.CreateEntity("Beej14","Lich",-62953.3985083, 4895.76141766, 24746.9262426,"Person")
pers.Angle=1.93731003342
pers.Level=0
pers.ActionAreaMin=pow(2,24)
pers.ActionAreaMax=pow(2,25)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

pers.Freeze()
