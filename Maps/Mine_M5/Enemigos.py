from math import pow
import EnemyTypes
#import AniSound
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


#------------------inicio-----------------------


####Orcos en la primera pasarela

#orco 111 
o=Bladex.CreateEntity("Mine1Orksword1","Garrote",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("Mine1Escudo1","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("1orc1","Ork",31439.6465817, -17171.6014525, -55167.6109542,"Person")
pers.Angle=5.61791240012
pers.Level=lvl_control.GiveLevel(0,1)
Actions.TakeObject(pers.Name,"Mine1Orksword1")
Actions.TakeObject(pers.Name,"Mine1Escudo1")
#pers.ActionAreaMin=pow(2,0)
#pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup("1orc1", "foso")



#orco 222

o=Bladex.CreateEntity("Mine2Orksword2","Hacha",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("Mine2Escudo2","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("2orc2","Ork",34059.6288747, -17134.1921515, -89268.9903977,"Person")
pers.Angle=0.296523650577
pers.Level=lvl_control.GiveLevel(1,5)
Actions.TakeObject(pers.Name,"Mine2Orksword2")
Actions.TakeObject(pers.Name,"Mine2Escudo2")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup("2orc2", "foso")
#AniSound.AsignarSonidosCaballeroTraidor(pers.Name)


#orco retrasado mental al cual aplasta la bola

o=Bladex.CreateEntity("Mine3Orksword3","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("Mine3Escudo3","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("3orc3","Great_Ork",57884.0074695, -9881.73426543, -100242.777899,"Person")
pers.Angle=5.53001499478
pers.Level=lvl_control.GiveLevel(0,3)
Actions.TakeObject(pers.Name,"Mine3Orksword3")
Actions.TakeObject(pers.Name,"Mine3Escudo3")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup("3orc3", "foso")
#AniSound.AsignarSonidosCaballeroTraidor(pers.Name)





#jefe orco mas listo que ninguno con pocion 50

o=Bladex.CreateEntity("Mine4Orksword4","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("Mine4Escudo4","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
potion=Bladex.CreateEntity("Potion4orc4","Pocima50",0,0,0)
potion.Static=0
potion.Solid=1
potion.Scale=1.220190
pocimac.CreatePotion("Potion4orc4")

pers=Bladex.CreateEntity("4orc4","Ork",5069.78562023, -17107.4362661, -58178.6849501,"Person")
pers.Angle=4.67194140129 
pers.Level=lvl_control.GiveLevel(2,5)
Actions.TakeObject(pers.Name,"Mine4Orksword4")
Actions.TakeObject(pers.Name,"Mine4Escudo4")
Actions.TakeObject(pers.Name,"Potion4orc4")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup("4orc4", "foso")

darfuncs.HideBadGuy("4orc4")

sectx1=Bladex.GetSector(15574.3966886, -8119.53715131, -102926.843622)


sectx1.OnEnter=x1



###########
##### jEFE ORCO ANTES DEL TUNEL
########### TIENE LLAVEEEEEEEEEE

o=Bladex.CreateEntity("Mine5Orksword5","Orksword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("Mine5Escudo5","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("5orc5","Great_Ork",-52250,-22000,-28250,"Person")
pers.Angle=3.0
pers.Level=lvl_control.GiveLevel(1,3)
Actions.TakeObject(pers.Name,"Mine5Orksword5")
Actions.TakeObject(pers.Name,"Mine5Escudo5")
Actions.TakeObject("5orc5","llave1")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)
#AniSound.AsignarSonidosCaballeroTraidor(pers.Name)


###############
###########
########BICHITOS INICIALES


pers=Bladex.CreateEntity("1cospas","Cos",-34250, -31000, 26500,"Person")
pers.Angle=5.36277230846
pers.Level=lvl_control.GiveLevel(2,5)
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


pers=Bladex.CreateEntity("2cospas","Cos",-34750, -31000, 27500,"Person")
pers.Angle=5.36277230846
pers.Level=lvl_control.GiveLevel(3,6)
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers=Bladex.CreateEntity("3cospas","Cos",-21000, -24000, 2850,"Person")
pers.Angle=1.49589570635
pers.Level=lvl_control.GiveLevel(2,4)
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers=Bladex.CreateEntity("4cospas","Cos",-24000, -24000, 450,"Person")
pers.Angle=1.49589570635
pers.Level=lvl_control.GiveLevel(0,5)
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


## Troll apostado tras puente justo antes de gema roja y con pocion 100

"""
potion=Bladex.CreateEntity("Pocima100mine1","Pocima100",0,0,0)
potion.Static=0
potion.Solid=0
potion.Scale=1.220190
pocimac.CreatePotion("Pocima100mine1")

Garropin=Bladex.CreateEntity("MineGarropin1","Garropin",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Trollpuente","Troll_Dark",-138492.923724, -4351.27240326, 62589.892,"Person")
pers.Angle=1.51627983557
#pers.Level=4
pers.Level= lvl_control.GiveLevel(3,5)
Actions.TakeObject(pers.Name,"Pocima100mine1")
Actions.TakeObject(pers.Name,"MineGarropin1")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)
"""

###############
###########
########BICHITOS DEL SEGUNDO RECORRIDO
##############
## Cositas in catacombs en zona bicho zampon

pers=Bladex.CreateEntity("1cos","Cos",-133651.251388, -20874.3118976, -150063.526349,"Person")
pers.Angle=1.02623270478
pers.Level=lvl_control.GiveLevel(2,5)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers=Bladex.CreateEntity("3cos","Cos",-86212.602362, -19127.7938545, -163565.757707,"Person")
pers.Angle=1.29204534754
pers.Level=lvl_control.GiveLevel(0,3)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers=Bladex.CreateEntity("4cos","Cos",-104015.867796, -19122.7311565, -152010.349768,"Person")
pers.Angle=5.89905362032
pers.Level=lvl_control.GiveLevel(0,4)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers=Bladex.CreateEntity("2cos","Cos",-97722.1130683, -20122.3526209, -132126.664354,"Person")
pers.Angle=0.0899482238858
pers.Level=lvl_control.GiveLevel(2,5)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)



pers=Bladex.CreateEntity("5cos","Cos",-150197, -20971, -136922,"Person")
pers.Angle=6.26937419901
pers.Level=lvl_control.GiveLevel(0,6)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)



#jefe orco en puente tras conseguir gema bichito zampon



o=Bladex.CreateEntity("MineOrksword6","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("MineEscudo6","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("6orc6","Great_Ork",-95823.3260545, -21373.6822187, -59063.632159,"Person")
pers.Angle=1
pers.Level=lvl_control.GiveLevel(0,4)
Actions.TakeObject(pers.Name,"MineOrksword6")
Actions.TakeObject(pers.Name,"MineEscudo6")
pers.ActionAreaMin=pow(2,1)
pers.ActionAreaMax=pow(2,2)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)












######################
#################
########## ORCOS DEL TERCER RECORRIDO
######################
######################
######################
######################

#############
##### JEFE ORCO
####################

o=Bladex.CreateEntity("MineTOrkswordJ1","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("MineTEscudoJ1","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
potion=Bladex.CreateEntity("MineTPotionJ1","Pocima50",0,0,0)
potion.Static=0
potion.Solid=1
potion.Scale=1.220190
pocimac.CreatePotion("MineTPotionJ1")

pers=Bladex.CreateEntity("TorcJ1","Great_Ork",-30967.3395088, -17615.5546553, -188828.548871,"Person")
pers.Angle=6.15771443316
pers.Level=lvl_control.GiveLevel(1,4)
Actions.TakeObject(pers.Name,"MineTOrkswordJ1")
Actions.TakeObject(pers.Name,"MineTEscudoJ1")
Actions.TakeObject(pers.Name,"MineTPotionJ1")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)
#AniSound.AsignarSonidosCaballeroTraidor(pers.Name)

#orco TERCER11111

o=Bladex.CreateEntity("MineTOrksword1","Hacha",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("MineTEscudo1","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("Torc1","Ork",-31429.1717165, -17172.9123783, -150968.580323,"Person")
pers.Angle=6.22798739817
pers.Level=lvl_control.GiveLevel(3,6)
Actions.TakeObject(pers.Name,"MineTOrksword1")
Actions.TakeObject(pers.Name,"MineTEscudo1")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)
#AniSound.AsignarSonidosCaballeroTraidor(pers.Name)

#orco TERCER 2222222

o=Bladex.CreateEntity("MineTOrksword2","Garrote",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("MineTEscudo2","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("Torc2","Ork",33327.5037499, -17374.0005206, -166493.695318,"Person")
pers.Angle=1.17176615186
pers.Level=lvl_control.GiveLevel(3,6)
Actions.TakeObject(pers.Name,"MineTOrksword2")
Actions.TakeObject(pers.Name,"MineTEscudo2")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)
#AniSound.AsignarSonidosCaballeroTraidor(pers.Name)


o=Bladex.CreateEntity("MineTOrksword3","Hacha",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("Torc3","Ork",-4757.18864251, -17369.5797479, -151506.281712,"Person")
pers.Angle=1.32747646475
pers.Level=lvl_control.GiveLevel(2,5)
Actions.TakeObject(pers.Name,"MineTOrksword3")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)
#AniSound.AsignarSonidosCaballeroTraidor(pers.Name)



#############
########## MONSTRUOS TRAS PUENTE ROTO
################3

###########
###### despues de las aranas
#orco TERCER 5555
#TIENE LLAVEEEEEE

o=Bladex.CreateEntity("MineTOrksword5","Orksword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("MineTEscudo5","Escudo1",0,0,0)
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("Torc5","Great_Ork",-11255,-6660,-150500,"Person")
pers.Angle=3.0
pers.Level=lvl_control.GiveLevel(2,4)
Actions.TakeObject(pers.Name,"MineTOrksword5")
Actions.TakeObject(pers.Name,"MineTEscudo5")
Actions.TakeObject("Torc5","llaver3")
pers.ActionAreaMin=pow(2,3)
pers.ActionAreaMax=pow(2,4)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)
#AniSound.AsignarSonidosCaballeroTraidor(pers.Name)

#orco TERCER 666

o=Bladex.CreateEntity("MineTOrksword6","Gladius",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("MineTEscudo6","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("Torc6","Ork",-7481.23334016, -5123.03008961, -169080.878575,"Person")

pers.Angle=3.42595413918
pers.Level=lvl_control.GiveLevel(3,6)
Actions.TakeObject(pers.Name,"MineTOrksword6")
Actions.TakeObject(pers.Name,"MineTEscudo6")
pers.ActionAreaMin=pow(2,3)
pers.ActionAreaMax=pow(2,4)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)
#AniSound.AsignarSonidosCaballeroTraidor(pers.Name)






#----TERCER RECORRIDO
# ARANAS
pers=Bladex.CreateEntity("TSPD1","Spidersmall",93000,-6000,-141500,"Person")
pers.Angle=0
pers.Level=lvl_control.GiveLevel(3,5)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,0)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers=Bladex.CreateEntity("TSPD2","Spidersmall",95750,-6000,-141000,"Person")

pers.Angle=1.49589570635
pers.Level=lvl_control.GiveLevel(3,6)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,0)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers=Bladex.CreateEntity("TSPD3","Spidersmall",92250,-6000,-144000,"Person")

pers.Angle=3.0
pers.Level=lvl_control.GiveLevel(4,5)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,0)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

# ARANAS segundo grupo
pers=Bladex.CreateEntity("TSPD4","Spidersmall",-2750,-6000,-209500,"Person")
pers.Angle=0
pers.Level=lvl_control.GiveLevel(0,6)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,0)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers=Bladex.CreateEntity("TSPD5","Spidersmall",-1500,-6000,-218000,"Person")
pers.Angle=1.49589570635
pers.Level=lvl_control.GiveLevel(0,7)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,0)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

pers=Bladex.CreateEntity("TSPD6","Spidersmall",-2000,-6000,-220000,"Person")
pers.Angle=3.0
pers.Level=lvl_control.GiveLevel(0,4)
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,0)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)




#########################
#########################
####### ARQUEROS ########
#########################
#########################

enm=Bladex.CreateEntity("Minearq1", "Ork",-57289.0063689, -26622.4135123, -22459.4327933,"Person")
enm.Angle=3.43
enm.Level=lvl_control.GiveLevel(3,6)
enm.ActionAreaMin=pow(2,2)
enm.ActionAreaMax=pow(2,3)
enm.SetOnFloor()

o=Bladex.CreateEntity("MineArqesp1","Maza",0,0,0,"Weapon")
inv=enm.GetInventory()
ItemTypes.ItemDefaultFuncs(o)
inv.AddWeapon("MineArqesp1")

o=Bladex.CreateEntity("MineArqbow1","Arco",0,0,0,"Weapon")
inv.AddBow("MineArqbow1")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("MineArqquiver1","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("MineArqquiver1")
o.Data.ArrowsLeft=10

EnemyTypes.EnemyDefaultFuncs(enm)

#########################

enm2=Bladex.CreateEntity("Minearq2", "Ork",-22611, -17170, -166591,"Person")
enm2.Angle=1.22
enm2.Level=lvl_control.GiveLevel(0,6)
enm2.ActionAreaMin=pow(2,0)
enm2.ActionAreaMax=pow(2,1)
enm2.SetOnFloor()

o=Bladex.CreateEntity("MineArqesp2","Hacha",0,0,0,"Weapon")
inv=enm2.GetInventory()
ItemTypes.ItemDefaultFuncs(o)
inv.AddWeapon("MineArqesp2")

o=Bladex.CreateEntity("MineArqbow2","Arco",0,0,0,"Weapon")
inv.AddBow("MineArqbow2")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("MineArqquiver2","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("MineArqquiver2")
o.Data.ArrowsLeft=10

EnemyTypes.EnemyDefaultFuncs(enm2)
#char.Position=(-31617.1568303, -17080.8819229, -168471.206019)

#########################

enm3=Bladex.CreateEntity("Minearq3", "Ork",64727.295287, -17744.3664948, -164715.4522,"Person")
enm3.Angle=3.0
enm3.Level=lvl_control.GiveLevel(0,5)
enm3.ActionAreaMin=pow(2,3)
enm3.ActionAreaMax=pow(2,2)
enm3.SetOnFloor()

o=Bladex.CreateEntity("MineArqesp3","Gladius",0,0,0,"Weapon")
inv=enm3.GetInventory()
ItemTypes.ItemDefaultFuncs(o)
inv.AddWeapon("MineArqesp3")

o=Bladex.CreateEntity("MineArqbow3","Arco",0,0,0,"Weapon")
inv.AddBow("MineArqbow3")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("MineArqquiver3","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver("MineArqquiver3")
o.Data.ArrowsLeft=10

EnemyTypes.EnemyDefaultFuncs(enm3)




########Troll al final

o=Bladex.CreateEntity("MineGarropin22","Garropin",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)


troll_final=Bladex.CreateEntity("Trollfinal","Troll_Dark",-10095.5237414, -13096.1415455, -26958.450,"Person")
troll_final.Angle=4.7
troll_final.Level=lvl_control.GiveLevel(1,3)
Actions.TakeObject(troll_final.Name,"MineGarropin22")
troll_final.ActionAreaMin=pow(2,0)
troll_final.ActionAreaMax=pow(2,1)
troll_final.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(troll_final)
troll_final.Data.VeryOldImDeadFunc = troll_final.ImDeadFunc
troll_final.ImDeadFunc = OnFinalTrollDied


#######
#######donde la cosita


o=Bladex.CreateEntity("MineOrksword616","Maza",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
#o=Bladex.CreateEntity("MineEscudo6616","Escudo2",0,0,0)
#Sparks.MakeShield("MineEscudo616")
#Breakings.SetBreakableWS("MineEscudo616")

pers=Bladex.CreateEntity("616orc6","Great_Ork",-60519.2066138, -19472.5681651, -153636.19521,"Person")
pers.Angle=1
pers.Level=lvl_control.GiveLevel(2,4)
Actions.TakeObject(pers.Name,"MineOrksword616")
#Actions.TakeObject(pers.Name,"MineEscudo616")
Actions.TakeObject("616orc6","llavemaz")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)

"""
o=Bladex.CreateEntity("MineOrksword626","Garrote",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("MineEscudo626","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("62orc6","Ork",-63188.1383585, -19318.1783737, -152239.80,"Person")
pers.Angle=1
pers.Level=lvl_control.GiveLevel(2,7)
Actions.TakeObject(pers.Name,"MineOrksword626")
Actions.TakeObject(pers.Name,"MineEscudo626")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)
"""


o=Bladex.CreateEntity("MineOrksword636","Hacha",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("MineEscudo636","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
pers=Bladex.CreateEntity("63orc6","Ork",-67163.5222375, -19316.117977, -157883.539,"Person")
pers.Angle=1
pers.Level=lvl_control.GiveLevel(3,6)
Actions.TakeObject(pers.Name,"MineOrksword636")
Actions.TakeObject(pers.Name,"MineEscudo636")
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(pers)


#muertos en la sala de las gemas
darfuncs.MuertoyTroceado(19945.3404076, -23034.8860086, -35682.766,"Ork","",(1,5,7,2))
darfuncs.MuertoyTroceado(23982.4667786, -23038.1376258, -18921.137,"Ork","",(1,5,7,2))
darfuncs.MuertoyTroceado(20704.5867037, -23048.2473619, -29537.773,"Ork","",(1,5,7,2))

#muertos en el primer recorrido
darfuncs.MuertoyTroceado(-83611.9283522, -9056.13658137, -32172.52,"Ork","",(1,5,7,2))
darfuncs.MuertoyTroceado(-83319.2943736, -9057.04500597, -16955.27,"Ork","",(1,5,7,2))
darfuncs.MuertoyTroceado(-131235.493898, -5055.14906521, -28892.27,"Great_Ork","",(1,5,7,2))