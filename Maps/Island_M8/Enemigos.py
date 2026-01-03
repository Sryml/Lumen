#from megaimport import *

from math import pow
import EnemyTypes
import Sparks
import Actions
import pocimac
import darfuncs
import Bladex
import ItemTypes
import Breakings

#################################################
#MUERTOS VIVIENTES en el exterior, al ppio

RigorMortis = darfuncs.E_Grup()
RigorMortis.OnDeath = TerminanLasMuertes



#1
o=Bladex.CreateEntity("IslandHacha1","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("KeAsko1","Lich",-68438.128096, -2121.00968329, 57372.6181675,"Person")
pers.Angle=3.15394837713
pers.Level=5
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
Actions.TakeObject(pers.Name,o.Name)

pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

RigorMortis.AddGuy(pers.Name)
RigorMortis.OnDeath = TerminanLasMuertes

#pers.AddBayPoint=-68438.128096, -2121.00968329, 57372.6181675
#pers.AddBayPoint=-69039.7462708, -714.894931353, 22125.3512758
#pers.AddBayPoint=-65937.4887508, -707.506774998, 21863.5495292
#pers.AddBayPoint=-66381.2779406, -2122.86334454, 57482.2188051




#2
o=Bladex.CreateEntity("IslandHacha2","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("KeAsko2","Lich",-72400.8695964, -693.92957139, 23328.4474167,"Person")
pers.Angle=5.28669458423
pers.Level=4
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
Actions.TakeObject(pers.Name,o.Name)

pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

RigorMortis.AddGuy(pers.Name)
RigorMortis.OnDeath = TerminanLasMuertes




#3
o=Bladex.CreateEntity("IslandHacha3","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)



pers=Bladex.CreateEntity("KeAsko3","Lich",-62497.9696204, -2103.40961774, 57622.5223302,"Person")
pers.Angle=2.42289605954
pers.Level=6
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
Actions.TakeObject(pers.Name,o.Name)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

RigorMortis.AddGuy(pers.Name)
RigorMortis.OnDeath = TerminanLasMuertes




#4
o=Bladex.CreateEntity("IslandHacha4","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("KeAsko4","Lich",-69579.2141577, -523.350288042, 1626.83626823,"Person")
pers.Angle=5.61849587613
pers.Level=6
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
Actions.TakeObject(pers.Name,o.Name)

pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

RigorMortis.AddGuy(pers.Name)
RigorMortis.OnDeath = TerminanLasMuertes



#5
o=Bladex.CreateEntity("IslandHacha5","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("KeAsko5","Lich",-59339.8671024, 75.8712357736, -27805.1893859,"Person")
pers.Angle=0.0237028405075
pers.Level=5
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)
Actions.TakeObject(pers.Name,o.Name)

RigorMortis.AddGuy(pers.Name)
RigorMortis.OnDeath = TerminanLasMuertes



#6
o=Bladex.CreateEntity("IslandHacha6","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("KeAsko6","Lich",-74723.1858851, -133.641552901, -29260.4645433,"Person")
pers.Angle=4.74487932209
pers.Level=4
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
Actions.TakeObject(pers.Name,o.Name)

pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

RigorMortis.AddGuy(pers.Name)
RigorMortis.OnDeath = TerminanLasMuertes



################## eskeletos  en almenas


pers=Bladex.CreateEntity("Islandarq1", "Skeleton",-73296.675281, -8145.65259639, -11730.825829,"Person")
pers.Angle=5.81596143344
pers.Level=4
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()


o=Bladex.CreateEntity("Islandesp1","HookSword",0,0,0,"Weapon")
inv=pers.GetInventory()
inv.AddWeapon("Islandesp1")
Breakings.SetBreakableWS("Islandesp1")

o=Bladex.CreateEntity("Islandbow1","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddBow("Islandbow1")

o=Bladex.CreateEntity("Islandquiver1","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Islandquiver1")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)

RigorMortis.AddGuy(pers.Name)
RigorMortis.OnDeath = TerminanLasMuertes


############################################################################

o=Bladex.CreateEntity("Islandesp2","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo2","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("Skeleton1","Skeleton",-77663.0257286, -7895.96218264, 11783.3533041,"Person")
pers.Angle=4.0605413165
pers.Level=5
Actions.TakeObject(pers.Name,"Islandesp2")
Actions.TakeObject(pers.Name,"IslandEscudo2")
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

RigorMortis.AddGuy(pers.Name)
RigorMortis.OnDeath = TerminanLasMuertes


###################################################################
### arquero cabron que te dispara si apareces en el punto 2

pers=Bladex.CreateEntity("Islandarq2", "Skeleton",-71762.2257503, -7746.4012341, 55140.4137675,"Person")
pers.Angle=3.51235477728
pers.Level=5
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()



#pers.AddBayPoint=-71762.2257503, -7746.4012341, 55140.4137675
#pers.AddBayPoint=-71810.57009, -7720.28401616, 40963.0369839
#pers.AddBayPoint=-75627.8311714, -7719.93852522, 40574.0733997
#pers.AddBayPoint=-75262.0460457, -7724.62540349, 55161.9322088

o=Bladex.CreateEntity("Islandesp3","Espadaelfica",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv=pers.GetInventory()
inv.AddWeapon("Islandesp3")


o=Bladex.CreateEntity("Islandbow2","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddBow("Islandbow2")

o=Bladex.CreateEntity("Islandquiver2","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Islandquiver2")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)

RigorMortis.AddGuy(pers.Name)
RigorMortis.OnDeath = TerminanLasMuertes


##################################################################################################



pers=Bladex.CreateEntity("Islandarq3", "Skeleton",-63055.1846394, -8116.75412706, 61385.6659753,"Person")
pers.Angle=2.84618219835
pers.Level=6
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()

o=Bladex.CreateEntity("Islandesp4","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv=pers.GetInventory()
inv.AddWeapon("Islandesp4")


o=Bladex.CreateEntity("Islandbow3","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddBow("Islandbow3")

o=Bladex.CreateEntity("Islandquiver3","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Islandquiver3")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)

RigorMortis.AddGuy(pers.Name)
RigorMortis.OnDeath = TerminanLasMuertes



##################################################################################################

o=Bladex.CreateEntity("Islandesp5","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo5","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("Skeleton2","Skeleton",-65698.9467212, -7615.48577207, 68092.1386817,"Person")
pers.Angle=3.33648464312
pers.Level=4
Actions.TakeObject(pers.Name,"Islandesp5")
Actions.TakeObject(pers.Name,"IslandEscudo5")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

RigorMortis.AddGuy(pers.Name)
RigorMortis.OnDeath = TerminanLasMuertes





##################################################################################################
## 	ultimos lich delante de puerta ppal
##################################################################################################

#1
o=Bladex.CreateEntity("IslandHacha7","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("KeAsko7","Lich",-46773.8940715, -5125.37891076, 68285.328818,"Person")
pers.Angle=3.05428962131
pers.Level=6
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
Actions.TakeObject(pers.Name,"IslandHacha7")
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

RigorMortis.AddGuy(pers.Name)
RigorMortis.OnDeath = TerminanLasMuertes



#2
o=Bladex.CreateEntity("IslandHacha8","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("KeAsko8","Lich",-33054.3131722, -5714.56828336, 75496.0946143,"Person")
pers.Angle=2.60907609938
pers.Level=5
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
Actions.TakeObject(pers.Name,"IslandHacha8")
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

RigorMortis.AddGuy(pers.Name)
RigorMortis.OnDeath = TerminanLasMuertes


#3
o=Bladex.CreateEntity("IslandHacha9","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("KeAsko9","Lich",-47628.9788879, -6125.46376462, 74336.4537323,"Person")
pers.Angle=4.64024504218
pers.Level=2
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
Actions.TakeObject(pers.Name,"IslandHacha9")
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

RigorMortis.AddGuy(pers.Name)
RigorMortis.OnDeath = TerminanLasMuertes


#4
o=Bladex.CreateEntity("IslandHacha10","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("KeAsko10","Lich",-26302.4785179, -5728.57896317, 72800.0683025,"Person")
pers.Angle=0.582651242498
pers.Level=4
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
Actions.TakeObject(pers.Name,"IslandHacha10")
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

RigorMortis.AddGuy(pers.Name)
RigorMortis.OnDeath = TerminanLasMuertes


#####################################################################
######### ultimos eskeletos exterior inicial
#####################################################################

pers=Bladex.CreateEntity("Islandarq4", "Skeleton",-39038.8418358, -11617.8854019, 70090.2006068,"Person")
pers.Angle=1.95569725209
pers.Level=6
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

o=Bladex.CreateEntity("Islandesp6","Espadaelfica",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv=pers.GetInventory()
inv.AddWeapon("Islandesp6")


o=Bladex.CreateEntity("Islandbow4","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddBow("Islandbow4")

o=Bladex.CreateEntity("Islandquiver4","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Islandquiver4")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)

RigorMortis.AddGuy(pers.Name)
RigorMortis.OnDeath = TerminanLasMuertes


###############################

o=Bladex.CreateEntity("Islandesp7","Espadaelfica",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo7","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("Skeleton3","Skeleton",-43515.5620316, -11629.3429535, 76802.2683884,"Person")
pers.Angle=2.93972237743
pers.Level=7
Actions.TakeObject(pers.Name,"Islandesp7")
Actions.TakeObject(pers.Name,"IslandEscudo7")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

RigorMortis.AddGuy(pers.Name)
RigorMortis.OnDeath = TerminanLasMuertes


################################################################################################
##################
##################
#################### bichos genericos exteriores que SOLO aparecen una vez se ha 
##################	eliminado a los 17 anteriores


#1
o=Bladex.CreateEntity("Islandesp8","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo8","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("Skeleton4","Skeleton",-67348.4175161, -2099.9884021, 56956.6278818,"Person")
pers.Angle=3.09958934548
pers.Level=6
Actions.TakeObject(pers.Name,"Islandesp8")
Actions.TakeObject(pers.Name,"IslandEscudo8")
pers.ActionAreaMin=pow(2,10)
pers.ActionAreaMax=pow(2,11)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("Skeleton4")

##2

o=Bladex.CreateEntity("Islandesp9","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo9","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("Skeleton5","Skeleton",-64751.6855427, -699.801188619, 16647.0001854,"Person")
pers.Angle=0.704245060291
pers.Level=5
Actions.TakeObject(pers.Name,"Islandesp9")
Actions.TakeObject(pers.Name,"IslandEscudo9")
pers.ActionAreaMin=pow(2,10)
pers.ActionAreaMax=pow(2,11)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("Skeleton5")



#3
o=Bladex.CreateEntity("Islandesp10","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo10","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("Skeleton6","Skeleton",-76483.0581147, -101.389617082, -30254.51525,"Person")
pers.Angle=4.93360651082
pers.Level=7
Actions.TakeObject(pers.Name,"Islandesp10")
Actions.TakeObject(pers.Name,"IslandEscudo10")
pers.ActionAreaMin=pow(2,10)
pers.ActionAreaMax=pow(2,11)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("Skeleton6")



#4

pers=Bladex.CreateEntity("Islandarq5", "Skeleton",-73356.573616, -8116.71610187, -1486.28613534,"Person")
pers.Angle=4.68377057262
pers.Level=4
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

o=Bladex.CreateEntity("Islandesp11","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv=pers.GetInventory()
inv.AddWeapon("Islandesp11")


o=Bladex.CreateEntity("Islandbow5","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddBow("Islandbow5")

o=Bladex.CreateEntity("Islandquiver5","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Islandquiver5")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("Islandarq5")



#5

pers=Bladex.CreateEntity("Islandarq6", "Skeleton",-71742.674073, -7708.77042428, 41844.9402448,"Person")
pers.Angle=5.84091912156
pers.Level=5
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

o=Bladex.CreateEntity("Islandesp12","Espadaelfica",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv=pers.GetInventory()
inv.AddWeapon("Islandesp12")


o=Bladex.CreateEntity("Islandbow6","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddBow("Islandbow6")

o=Bladex.CreateEntity("Islandquiver6","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Islandquiver6")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("Islandarq6")



#6

pers=Bladex.CreateEntity("Islandarq7", "Skeleton",-61001.8431075, -8118.13104086, 61495.9763893,"Person")
pers.Angle=4.88012478993
pers.Level=6
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()

o=Bladex.CreateEntity("Islandesp13","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv=pers.GetInventory()
inv.AddWeapon("Islandesp13")


o=Bladex.CreateEntity("Islandbow7","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddBow("Islandbow7")

o=Bladex.CreateEntity("Islandquiver7","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Islandquiver7")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("Islandarq7")



#7

o=Bladex.CreateEntity("Islandesp14","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo14","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("Skeleton7","Skeleton",-46045.3237303, -5120.45525583, 63045.0101557,"Person")
pers.Angle=4.62451369885
pers.Level=6
Actions.TakeObject(pers.Name,"Islandesp14")
Actions.TakeObject(pers.Name,"IslandEscudo14")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("Skeleton7")


#8

o=Bladex.CreateEntity("Islandesp15","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo15","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Skeleton8","Skeleton",-29516.3201955, -5109.3588304, 65963.5007031,"Person")
pers.Angle=1.7778453642
pers.Level=5
Actions.TakeObject(pers.Name,"Islandesp15")
Actions.TakeObject(pers.Name,"IslandEscudo15")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("Skeleton8")



#9

o=Bladex.CreateEntity("Islandesp16","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo16","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Skeleton9","Skeleton",-26454.0242073, -5706.38961109, 75740.587405,"Person")
pers.Angle=1.83090250121
pers.Level=6
Actions.TakeObject(pers.Name,"Islandesp16")
Actions.TakeObject(pers.Name,"IslandEscudo16")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("Skeleton9")


#10

pers=Bladex.CreateEntity("Islandarq8", "Skeleton",-31231.3557091, -11599.5499429, 70460.6583618,"Person")
pers.Angle=2.45813590288
pers.Level=3
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

o=Bladex.CreateEntity("Islandesp17","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv=pers.GetInventory()
inv.AddWeapon("Islandesp17")


o=Bladex.CreateEntity("Islandbow8","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddBow("Islandbow8")

o=Bladex.CreateEntity("Islandquiver8","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Islandquiver8")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("Islandarq8")



#11

pers=Bladex.CreateEntity("Islandarq9", "Skeleton",-41640.7912513, -11619.8021585, 71738.7278389,"Person")
pers.Angle=3.74719830032
pers.Level=4
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

o=Bladex.CreateEntity("Islandesp18","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv=pers.GetInventory()
inv.AddWeapon("Islandesp18")


o=Bladex.CreateEntity("Islandbow9","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddBow("Islandbow9")

o=Bladex.CreateEntity("Islandquiver9","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Islandquiver9")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)
darfuncs.HideBadGuy("Islandarq9")





###################################################################################################
#########
#########
#########
#########
#########ENTRAMOS EN LA PRIMERA AREA INTERIOR
#########AREAS DE ACCION PERMITIDAS:A PARTIR DE (2,12) INCLUSIVE -ES DECIR, DEL AREA 13 EN 
#########ADELANTE
#########
#########
#########
##################################################################################################

## knight_zombi patrullante


## bichos 2,12  2,13 

#1
o=Bladex.CreateEntity("IslandHachaZombi1","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi1","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi1","Knight_Zombie",-30770.0487876, -5536.22179344, 53487.5000219,"Person")
pers.Angle=3.11010049659
pers.Level=7
Actions.TakeObject(pers.Name,"IslandHachaZombi1")
Actions.TakeObject(pers.Name,"IslandEscudoZombi1")
pers.ActionAreaMin=pow(2,12)
pers.ActionAreaMax=pow(2,13)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()



#pers.AddBayPoint=-30770.0487876, -5536.22179344, 53487.5000219
#pers.AddBayPoint=-21814.1431014, -5478.08675621, 51651.509479
#pers.AddBayPoint=-22429.0532965, -5455.45292167, 41907.706976
#pers.AddBayPoint=-18200.6089672, -5456.70105277, 39959.2644867
#pers.AddBayPoint=-21592.0557009, -5568.84921808, 50742.5767926

#2
o=Bladex.CreateEntity("IslandHachaZombi2","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi2","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi2","Knight_Zombie",-57149.266865, -5453.81266386, 21300.0074889,"Person")
pers.Angle=0.0427177033743
pers.Level=6
Actions.TakeObject(pers.Name,"IslandHachaZombi2")
Actions.TakeObject(pers.Name,"IslandEscudoZombi2")
pers.ActionAreaMin=pow(2,12)
pers.ActionAreaMax=pow(2,13)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("Zombi2")


#zombi3

o=Bladex.CreateEntity("IslandHachaZombi3","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi3","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi3","Knight_Zombie",-22049.9590796, -5448.36511525, 8915.84526076,"Person")
pers.Angle=6.28106061334
pers.Level=8
Actions.TakeObject(pers.Name,"IslandHachaZombi3")
Actions.TakeObject(pers.Name,"IslandEscudoZombi3")
pers.ActionAreaMin=pow(2,18)
pers.ActionAreaMax=pow(2,18)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("Zombi3")


sectx2=Bladex.GetSector(-38648.9721958, -5456.94094092, 57790.5787746)

sectx2.OnEnter=x2



zombiesplantabaja=darfuncs.E_Grup()
zombiesplantabaja.OnDeath = FinMuertesPLantabaja


zombiesplantabaja.AddGuy("Zombi1")
zombiesplantabaja.AddGuy("Zombi2")
zombiesplantabaja.AddGuy("Zombi3")


######################################################################################################
######		SKELETOS DENTRO DE LA SALA CON ARMAS
#1
o=Bladex.CreateEntity("Islandesp95","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo95","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Skeleton95","Skeleton",-32989.1262598, -5449.20371838, 39309.6364768,"Person")
pers.Angle=3.33648464312
pers.Level=7
Actions.TakeObject(pers.Name,"Islandesp95")
Actions.TakeObject(pers.Name,"IslandEscudo95")
#pers.ActionAreaMin=pow(2,6)
#pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


darfuncs.HideBadGuy("Skeleton95")

#2
o=Bladex.CreateEntity("Islandesp96","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo96","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Skeleton96","Skeleton",-38348.6304005, -5468.02762069, 27181.295966,"Person")
pers.Angle=3.33648464312
pers.Level=7
Actions.TakeObject(pers.Name,"Islandesp96")
Actions.TakeObject(pers.Name,"IslandEscudo96")
#pers.ActionAreaMin=pow(2,6)
#pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("Skeleton96")

######################################################################################################
#bichos 2,14 2,15	ZOMBIES EN LA SALA DE LOS HUECOS QUE DESLIZAN



# se entra en el area con estos 2 de espaldas, si no se hace ruido, uno puede quitarle una pocima
# a un muerto convenientemente colocado. Tal vez se cambiaran los zombies por otra cosa


#1
o=Bladex.CreateEntity("IslandHachaZombi4","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi4","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi4","Lich",-39448.5185068, -5454.20633212, -15451.3786187,"Person")
pers.Angle=1.59955321241
pers.Level=5
Actions.TakeObject(pers.Name,"IslandHachaZombi4")
Actions.TakeObject(pers.Name,"IslandEscudoZombi4")
pers.ActionAreaMin=pow(2,18)
pers.ActionAreaMax=pow(2,18)
EnemyTypes.EnemyDefaultFuncs(pers)

pers.SetOnFloor()


#2
o=Bladex.CreateEntity("IslandHachaZombi5","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi5","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi5","Lich",-31155.1444883, -5214.48949829, -11261.717171,"Person")
pers.Angle=0.227585291373
pers.Level=7
Actions.TakeObject(pers.Name,"IslandHachaZombi5")
Actions.TakeObject(pers.Name,"IslandEscudoZombi5")
pers.ActionAreaMin=pow(2,14)
pers.ActionAreaMax=pow(2,15)
EnemyTypes.EnemyDefaultFuncs(pers)

pers.SetOnFloor()



## bichos 2,16 2,17

#1
o=Bladex.CreateEntity("IslandHachaZombi6","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi6","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi6","Knight_Zombie",-46273.3974882, -5097.07729825, 9835.30575365,"Person")
pers.Angle=3.65993783909
pers.Level=7
Actions.TakeObject(pers.Name,"IslandHachaZombi6")
Actions.TakeObject(pers.Name,"IslandEscudoZombi6")
pers.ActionAreaMin=pow(2,16)
pers.ActionAreaMax=pow(2,17)
EnemyTypes.EnemyDefaultFuncs(pers)

pers.SetOnFloor()


#2
o=Bladex.CreateEntity("IslandHachaZombi7","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi7","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi7","Knight_Zombie",-33003.2731928, -5056.82371233, 10160.9966984,"Person")
pers.Angle=4.44820126831
pers.Level=9
Actions.TakeObject(pers.Name,"IslandHachaZombi7")
Actions.TakeObject(pers.Name,"IslandEscudoZombi7")
pers.ActionAreaMin=pow(2,16)
pers.ActionAreaMax=pow(2,17)
EnemyTypes.EnemyDefaultFuncs(pers)

pers.SetOnFloor()

### los bichos siguientes se mueven por areas 0 y 1 de nuevo



### keleto arquero patrullando en muralla patio 

#1
pers=Bladex.CreateEntity("Islandarq10", "Skeleton",-45741.5494777, -12558.2842123, -5222.84393704,"Person")
pers.Angle=4.78700593675
pers.Level=5
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

o=Bladex.CreateEntity("Islandesp19","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv=pers.GetInventory()
inv.AddWeapon("Islandesp19")


o=Bladex.CreateEntity("Islandbow10","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddBow("Islandbow10")

o=Bladex.CreateEntity("Islandquiver10","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Islandquiver10")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)

#pers.AddBayPoint=-45741.5494777, -12558.2842123, -5222.84393704
#pers.AddBayPoint=-21137.006131, -13056.4023654, -5197.54752707
#pers.AddBayPoint=-19923.6886829, -13053.9217452, -21728.8058132
#pers.AddBayPoint=-22125.4062023, -13055.4263556, -21332.5767121
#pers.AddBayPoint=-22367.2823365, -13113.0388053, -6977.8704057
#pers.AddBayPoint=-46093.7540002, -12533.0754013, -7385.26915656



## keleto Skondido TAMBIEN EN LA MURALLA


o=Bladex.CreateEntity("Islandesp20","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo20","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Skeleton10","Skeleton",-54753.7859556, -12555.2172969, -8326.59395597,"Person")
pers.Angle=4.4626008681
pers.Level=8
Actions.TakeObject(pers.Name,"Islandesp20")
Actions.TakeObject(pers.Name,"IslandEscudo20")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


## keletos en exterior puerta rota (2,0) (2,1)

#1
o=Bladex.CreateEntity("Islandesp21","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo21","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Skeleton11","Skeleton",-11158.5113591, -5473.90512029, 29960.3308124,"Person")
pers.Angle=3.34293924418
pers.Level=5
Actions.TakeObject(pers.Name,"Islandesp21")
Actions.TakeObject(pers.Name,"IslandEscudo21")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


#2
o=Bladex.CreateEntity("Islandesp22","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo22","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Skeleton12","Skeleton",6629.13943061, -5069.33502863, 17998.0805805,"Person")
pers.Angle=2.43168948193
pers.Level=4
Actions.TakeObject(pers.Name,"Islandesp22")
Actions.TakeObject(pers.Name,"IslandEscudo22")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


## lich en piscina tablilla (2,2) (2,3)

#1
o=Bladex.CreateEntity("IslandHachaZombi8","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi8","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi8","Lich",2122.3679237, 1582.06593181, -1532.52211582,"Person")
pers.Angle=0.264945882925
pers.Level=7
Actions.TakeObject(pers.Name,"IslandHachaZombi8")
Actions.TakeObject(pers.Name,"IslandEscudoZombi8")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


#2
o=Bladex.CreateEntity("IslandHachaZombi9","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi9","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi9","Lich",-3541.79285742, 1590.32777678, -3620.10063457,"Person")
pers.Angle=4.62129424042
pers.Level=8
Actions.TakeObject(pers.Name,"IslandHachaZombi9")
Actions.TakeObject(pers.Name,"IslandEscudoZombi9")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


#3
o=Bladex.CreateEntity("IslandHachaZombi10","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi10","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi10","Lich",2494.33541961, 2802.89585252, -28408.3893316,"Person")
pers.Angle=4.47444683732
pers.Level=7
Actions.TakeObject(pers.Name,"IslandHachaZombi10")
Actions.TakeObject(pers.Name,"IslandEscudoZombi10")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


## lich en zona inferior a piscina tablilla (2,0) (2,1)

#1
o=Bladex.CreateEntity("IslandHachaZombi11","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi11","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi11","Lich",6335.06570788, 8990.15300083, -34364.5555,"Person")
pers.Angle=4.79591635991
pers.Level=3
Actions.TakeObject(pers.Name,"IslandHachaZombi11")
Actions.TakeObject(pers.Name,"IslandEscudoZombi11")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

#2
o=Bladex.CreateEntity("IslandHachaZombi12","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi12","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi12","Lich",12674.3755225, 9272.64896061, -40031.7295633,"Person")
pers.Angle=5.70512554363
pers.Level=4
Actions.TakeObject(pers.Name,"IslandHachaZombi12")
Actions.TakeObject(pers.Name,"IslandEscudoZombi12")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


#3
o=Bladex.CreateEntity("IslandHachaZombi13","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi13","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi13","Lich",-1765.62251574, 11276.0556969, -43602.4268535,"Person")
pers.Angle=6.25951729953
pers.Level=2
Actions.TakeObject(pers.Name,"IslandHachaZombi13")
Actions.TakeObject(pers.Name,"IslandEscudoZombi13")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


#4
o=Bladex.CreateEntity("IslandHachaZombi14","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi14","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi14","Lich",-1819.48685629, 11628.7967112, -50112.5155133,"Person")
pers.Angle=6.25951741025
pers.Level=8
Actions.TakeObject(pers.Name,"IslandHachaZombi14")
Actions.TakeObject(pers.Name,"IslandEscudoZombi14")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

####################################################################
### zombies junto a mazmorras y reja acceso a escaleras
####################################################################

## zombi saliendo de mazmorras

o=Bladex.CreateEntity("IslandHachaZombi15","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi15","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi15","Knight_Zombie",-10969.7833698, 1379.68293421, 21849.4464825,"Person")
pers.Angle=1.55927416443
pers.Level=8
Actions.TakeObject(pers.Name,"IslandHachaZombi15")
Actions.TakeObject(pers.Name,"IslandEscudoZombi15")
pers.ActionAreaMin=pow(2,19)
pers.ActionAreaMax=pow(2,20)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("Zombi15")


sectx3=Bladex.GetSector(-18908.5013404, 447.847957256, 7878.54462993)

sectx3.OnEnter=x3




## zombi susto

o=Bladex.CreateEntity("IslandHachaZombi16","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi16","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi16","Knight_Zombie",-27871.9741511, 1936.545382, 3343.59362644,"Person")
pers.Angle=1.63919504818
pers.Level=8
Actions.TakeObject(pers.Name,"IslandHachaZombi16")
Actions.TakeObject(pers.Name,"IslandEscudoZombi16")
pers.ActionAreaMin=pow(2,19)
pers.ActionAreaMax=pow(2,20)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("Zombi16")

pers.Data.nodos=[(-38628.0890915, 1947.16723306, 2843.96937268), (-38141.9414619, 3431.02263318, -7559.85723523)]
pers.Data.nodo_actual=0



listazombis=[pers]



sectx4=Bladex.GetSector(-38936.4601642, 3146.72945504, -5000.72940065)

sectx4.OnEnter=x4



#otro zombi	en la misma zona

o=Bladex.CreateEntity("IslandHachaZombi17","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi17","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi17","Knight_Zombie",-18850.5328584, 387.504016728, 16862.711863,"Person")
pers.Angle=3.09526635054
pers.Level=4
Actions.TakeObject(pers.Name,"IslandHachaZombi17")
Actions.TakeObject(pers.Name,"IslandEscudoZombi17")
pers.ActionAreaMin=pow(2,19)
pers.ActionAreaMax=pow(2,20)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


######################################################################################################
## caballero negro guardian de mazmorras con llave

o=Bladex.CreateEntity("Islandesp23","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo23","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

potion=Bladex.CreateEntity("Potion1kd","Pocima200",0,0,0)
potion.Static=0
potion.Solid=1
potion.Scale=1.220190
pocimac.CreatePotion("Potion1kd")


pers=Bladex.CreateEntity("1kd","Dark_Knight",3777.96423783, 1370.82104427, 16345.4371265,"Person")
pers.Angle=1.54744998942
pers.Level=4
Actions.TakeObject(pers.Name,"Islandesp23")
Actions.TakeObject(pers.Name,"IslandEscudo23")
Actions.TakeObject(pers.Name,"Potion1kd")
pers.ActionAreaMin=pow(2,19)
pers.ActionAreaMax=pow(2,20)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)




##########################################################################################
####################
####################
####################
####################  EN TORRES Y HASTA EL FINAL -estoy hasta los mismísimos ya
####################
####################
##########################################################################################


# caballeros negros areas 21 y 22 al abrir puerta palanca

#1
o=Bladex.CreateEntity("Islandesp24","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo24","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

potion=Bladex.CreateEntity("Potion2kd","Pocima50",0,0,0)
potion.Static=0
potion.Solid=1
potion.Scale=1.220190
pocimac.CreatePotion("Potion2kd")

pers=Bladex.CreateEntity("2kd","Dark_Knight",-22565.6045742, -12101.4183309, 43721.7116204,"Person")
pers.Angle=3.48380752933
pers.Level=4
Actions.TakeObject(pers.Name,"Islandesp24")
Actions.TakeObject(pers.Name,"IslandEscudo24")
Actions.TakeObject(pers.Name,"Potion2kd")
pers.ActionAreaMin=pow(2,21)
pers.ActionAreaMax=pow(2,22)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


#2
o=Bladex.CreateEntity("Islandesp25","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo25","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


pers=Bladex.CreateEntity("3kd","Dark_Knight",-22748.4739307, -12107.170243, 16213.5280393,"Person")
pers.Angle=5.87554653453
pers.Level=3
Actions.TakeObject(pers.Name,"Islandesp25")
Actions.TakeObject(pers.Name,"IslandEscudo25")
pers.ActionAreaMin=pow(2,21)
pers.ActionAreaMax=pow(2,22)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


#3
o=Bladex.CreateEntity("Islandesp26","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo26","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("4kd","Dark_Knight",-48515.2393297, -12105.3326946, 50976.1049162,"Person")
pers.Angle=4.79665690514
pers.Level=5
Actions.TakeObject(pers.Name,"Islandesp26")
Actions.TakeObject(pers.Name,"IslandEscudo26")
pers.ActionAreaMin=pow(2,21)
pers.ActionAreaMax=pow(2,22)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

################################################################################################
# caballeros negros areas 23 y 24 Estas areas tambien son las del centro de la zona de combate
#del minotauro
################################################################################################


#1
o=Bladex.CreateEntity("Islandesp27","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo27","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("5kd","Dark_Knight",-55936.1608449, -12050.5719103, 14578.7186614,"Person")
pers.Angle=4.90171230187
pers.Level=5
Actions.TakeObject(pers.Name,"Islandesp27")
Actions.TakeObject(pers.Name,"IslandEscudo27")
pers.ActionAreaMin=pow(2,23)
pers.ActionAreaMax=pow(2,24)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("5kd")


#2
o=Bladex.CreateEntity("Islandesp28","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo28","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

potion=Bladex.CreateEntity("Potion6kd","Pocima50",0,0,0)
potion.Static=0
potion.Solid=1
potion.Scale=1.220190
pocimac.CreatePotion("Potion6kd")

pers=Bladex.CreateEntity("6kd","Dark_Knight",-52058.9767426, -12065.4156033, 30426.8343728,"Person")
pers.Angle=0.305249192199
pers.Level=4
Actions.TakeObject(pers.Name,"Islandesp28")
Actions.TakeObject(pers.Name,"IslandEscudo28")
Actions.TakeObject(pers.Name,"Potion6kd")
pers.ActionAreaMin=pow(2,23)
pers.ActionAreaMax=pow(2,24)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("6kd")


##################################################
# caballeros negros areas 25 y 26
##################################################

#1
o=Bladex.CreateEntity("Islandesp29","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo29","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("7kd","Dark_Knight",-29139.2175355, -17551.8497171, 34371.0194348,"Person")
pers.Angle=1.23591229631
pers.Level=3
Actions.TakeObject(pers.Name,"Islandesp29")
Actions.TakeObject(pers.Name,"IslandEscudo29")
pers.ActionAreaMin=pow(2,25)
pers.ActionAreaMax=pow(2,26)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("7kd")


#2
o=Bladex.CreateEntity("Islandesp30","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo30","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("8kd","Dark_Knight",-30060.2542443, -17555.3409873, 27378.5579381,"Person")
pers.Angle=2.10310206124
pers.Level=4
Actions.TakeObject(pers.Name,"Islandesp30")
Actions.TakeObject(pers.Name,"IslandEscudo30")
pers.ActionAreaMin=pow(2,25)
pers.ActionAreaMax=pow(2,26)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("8kd")


#3
o=Bladex.CreateEntity("Islandesp31","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo31","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

potion=Bladex.CreateEntity("IslandPotion9kd","Pocima100",0,0,0)
potion.Static=0
potion.Solid=1
potion.Scale=1.220190
pocimac.CreatePotion("IslandPotion9kd")

pers=Bladex.CreateEntity("9kd","Dark_Knight",-27399.2676239, -17565.763073, 30729.4021506,"Person")
pers.Angle=1.54152923697
pers.Level=6
Actions.TakeObject(pers.Name,"Islandesp31")
Actions.TakeObject(pers.Name,"IslandEscudo31")
Actions.TakeObject(pers.Name,"IslandPotion9kd")
pers.ActionAreaMin=pow(2,25)
pers.ActionAreaMax=pow(2,26)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("9kd")



sectx5=Bladex.GetSector(-59203.9160341, -17260.8653201, 46201.0754526)

sectx5.OnEnter=x5



################################################################
## minotauro con llave 
################################################################

o=Bladex.CreateEntity("IslandGarropin","Hachacarnicero",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("minot1","Minotaur",-31510.8903815, -12065.5567243, 12512.9797995,"Person")
pers.Angle=1.54041524447
pers.Level=0
Actions.TakeObject(pers.Name,"IslandGarropin")
Actions.TakeObject(pers.Name,"llave8")
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("minot1")

	
RigorMortisMinorx = darfuncs.E_Grup()
RigorMortisMinorx.OnDeath = MuerteMinorx
RigorMortisMinorx.AddGuy("minot1")

pers.Data.nodos=[(-38264.5661822, -12066.9456352, 12902.9504927), (-38159.3109332, -12066.6234116, 18682.5197885)]
pers.Data.nodo_actual=0


listabichos=[pers]

res=ReadGSFile.ReadGhostSectorFile("minorx.sf")
for igs in res:
   Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

Bladex.SetTriggerSectorFunc("minorx", "OnEnter", x6 )


########################################################################################
########################################################################################
###############
###############
###############
###############
###############   ZONA  DE  LA  ESCALERA  DOBLE
###############
###############
###############
########################################################################################
########################################################################################


## zombies zona power potion

#1
o=Bladex.CreateEntity("IslandHachaZombi18","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi18","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi18","Knight_Zombie",-28390.6667751, -23771.1893003, 18324.70785,"Person")
pers.Angle=1.57017288111
pers.Level=7
Actions.TakeObject(pers.Name,"IslandHachaZombi18")
Actions.TakeObject(pers.Name,"IslandEscudoZombi18")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


#2
o=Bladex.CreateEntity("IslandHachaZombi19","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi19","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi19","Knight_Zombie",-48981.934086, -23554.6760926, 18155.9049183,"Person")
pers.Angle=6.26552907236
pers.Level=9
Actions.TakeObject(pers.Name,"IslandHachaZombi19")
Actions.TakeObject(pers.Name,"IslandEscudoZombi19")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


#3
o=Bladex.CreateEntity("IslandHachaZombi20","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi20","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi20","Knight_Zombie",-48850.2559291, -23550.7761943, 42637.1016521,"Person")
pers.Angle=4.68490839774
pers.Level=9
Actions.TakeObject(pers.Name,"IslandHachaZombi20")
Actions.TakeObject(pers.Name,"IslandEscudoZombi20")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


############## zombis junto a ascensor
#1
o=Bladex.CreateEntity("IslandHachaZombi21","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi21","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi21","Knight_Zombie",-47929.0750002, -37567.5393222, 22131.9242075,"Person")
pers.Angle=6.19250951481
pers.Level=5
Actions.TakeObject(pers.Name,"IslandHachaZombi21")
Actions.TakeObject(pers.Name,"IslandEscudoZombi21")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


#2
o=Bladex.CreateEntity("IslandHachaZombi22","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi22","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi22","Knight_Zombie",-47186.9312231, -37550.5209578, 36476.6970397,"Person")
pers.Angle=3.14838707289
pers.Level=8
Actions.TakeObject(pers.Name,"IslandHachaZombi22")
Actions.TakeObject(pers.Name,"IslandEscudoZombi22")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


####################################################################################################
##
## zombis sobre ascensor en sala de vigas inclinadas
##
####################################################################################################

##al morirse se abre la puerta del demonio

#1
o=Bladex.CreateEntity("IslandHachaZombi23","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi23","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

#pers=Bladex.CreateEntity("Zombi23","Knight_Zombie",-38324.5325889, -42565.0447624, 28889.2300579,"Person")
pers=Bladex.CreateEntity("Zombi23","Skeleton",-38324.5325889, -42565.0447624, 28889.2300579,"Person")
pers.Angle=2.8844594068
pers.Level=8
Actions.TakeObject(pers.Name,"IslandHachaZombi23")
Actions.TakeObject(pers.Name,"IslandEscudoZombi23")
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

#Skeletos.AddGuy("Zombi23")


#2
o=Bladex.CreateEntity("IslandHachaZombi24","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi24","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

#pers=Bladex.CreateEntity("Zombi24","Knight_Zombie",-27786.8822281, -43550.9917405, 37005.5759918,"Person")
pers=Bladex.CreateEntity("Zombi24","Skeleton",-27786.8822281, -43550.9917405, 37005.5759918,"Person")
pers.Level=7
pers.Angle=2.92983385429
Actions.TakeObject(pers.Name,"IslandHachaZombi24")
Actions.TakeObject(pers.Name,"IslandEscudoZombi24")
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

#Skeletos.AddGuy("Zombi24")


#3
o=Bladex.CreateEntity("IslandHachaZombi25","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi25","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

#pers=Bladex.CreateEntity("Zombi25","Knight_Zombie",-28445.2749964, -42547.0715181, 21171.8260755,"Person")
pers=Bladex.CreateEntity("Zombi25","Skeleton",-28445.2749964, -42547.0715181, 21171.8260755,"Person")
pers.Level=4
pers.Angle=1.71015256092
Actions.TakeObject(pers.Name,"IslandHachaZombi25")
Actions.TakeObject(pers.Name,"IslandEscudoZombi25")
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

#Skeletos.AddGuy("Zombi25")


Skeletos=darfuncs.E_Grup()
Skeletos.OnDeath = FinMuertesVigasinclinadas

Skeletos.AddGuy("Zombi23")
Skeletos.AddGuy("Zombi24")
Skeletos.AddGuy("Zombi25")



###################################################################################
## zombis nueva zona areas 2,6  2,7 en la zona de las escaleras dobles
###################################################################################

#1
o=Bladex.CreateEntity("IslandHachaZombi26","Hacha3",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi26","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi26","Knight_Zombie",-44744.9983552, -28560.719704, 42719.3693338,"Person")
pers.Angle=4.80689489969
pers.Level=6
Actions.TakeObject(pers.Name,"IslandHachaZombi26")
Actions.TakeObject(pers.Name,"IslandEscudoZombi26")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


#2
o=Bladex.CreateEntity("IslandHachaZombi27","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi27","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi27","Knight_Zombie",-49570.4266094, -30046.4299247, 20775.802963,"Person")
pers.Angle=6.05545373548
pers.Level=4
Actions.TakeObject(pers.Name,"IslandHachaZombi27")
Actions.TakeObject(pers.Name,"IslandEscudoZombi27")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


#3
o=Bladex.CreateEntity("IslandHachaZombi28","Martillo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudoZombi28","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Zombi28","Knight_Zombie",-28045.4109893, -30448.477614, 18203.7961525,"Person")
pers.Angle=1.39375597471
pers.Level=11
Actions.TakeObject(pers.Name,"IslandHachaZombi28")
Actions.TakeObject(pers.Name,"IslandEscudoZombi28")
pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)



##########################################################################################################
##	ARQUERO EN LA ZONA DE LA ESCALERA DOBLE
#1
pers=Bladex.CreateEntity("Islandarq11", "Skeleton",-25000, -37136.0328281, 30345.9248186,"Person")
pers.Angle=1.8
pers.Level=8
pers.ActionAreaMin=pow(2,30)
pers.ActionAreaMax=1<<31
pers.SetOnFloor()

o=Bladex.CreateEntity("IslandespM1","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv=pers.GetInventory()
inv.AddWeapon("IslandespM1")


o=Bladex.CreateEntity("Islandbow11","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddBow("Islandbow11")

o=Bladex.CreateEntity("Islandquiver11","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("Islandquiver11")
o.Data.ArrowsLeft=10
EnemyTypes.EnemyDefaultFuncs(pers)



##SKELETOS EN MAZMORRAS


#90
o=Bladex.CreateEntity("Islandesp90","Espadaelfica",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo90","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Skeleton90","Skeleton",-13233.8, 2431.9, -7007.6,"Person")
pers.Angle=1.71
pers.Level=7
Actions.TakeObject(pers.Name,"Islandesp90")
Actions.TakeObject(pers.Name,"IslandEscudo90")
#pers.ActionAreaMin=pow(2,8)
#pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("Skeleton90")


#91
o=Bladex.CreateEntity("Islandesp91","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo91","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Skeleton91","Skeleton",-10963.9, 2447.8, -11357.8,"Person")
pers.Angle=0.65
pers.Level=6
Actions.TakeObject(pers.Name,"Islandesp91")
Actions.TakeObject(pers.Name,"IslandEscudo91")
#pers.ActionAreaMin=pow(2,8)
#pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("Skeleton91")


#94
o=Bladex.CreateEntity("Islandesp94","Maza2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("IslandEscudo94","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Skeleton94","Skeleton",-12468.2, 2445.4, -5074.8,"Person")
pers.Angle=1.71
pers.Level=7
Actions.TakeObject(pers.Name,"Islandesp94")
Actions.TakeObject(pers.Name,"IslandEscudo94")
#pers.ActionAreaMin=pow(2,8)
#pers.ActionAreaMax=pow(2,9)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy("Skeleton94")