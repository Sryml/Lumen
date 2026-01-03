import Doors
import Levers
import Locks
import Objects
import Sounds
import Sparks
import Button
import darfuncs
import AuxFuncs
import Stars

###############################
###---PUERTA DEL PALACIO---####
###############################
#-PUERTA-LLAVE-1


#spuertal1d=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
#spuertal1d.MaxDistance=20000
#spuertal1d.MinDistance=1000
#spuertal1d.Volume=1.0
#
#
#spuertal1g=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
#spuertal1g.MaxDistance=20000
#spuertal1g.MinDistance=1000
#spuertal1g.Volume=1.0
#
#puertal1=Doors.CreateDoor("Puertal1", (13437,-7000,25000), (0,1,0), 700, 5100, Doors.CLOSED)
#
#
#puertal1.opentype=Doors.UNIF
#puertal1.o_med_vel=-500
##puertal1.o_med_displ=4400
#
#
#puertal1.closetype=Doors.AC
#puertal1.c_init_displ=4400
#puertal1.c_med_vel=8000
#
#
#puertal1.SetWhileOpenSound(spuertal1d)
#puertal1.SetEndOpenSound(spuertal1g)
#
#puertal1.SetWhileCloseSound(spuertal1d)
#puertal1.SetEndCloseSound(spuertal1g)
#
###llave1 abrepuerta1###
#
#
#cerradurp1=Locks.PlaceLock("cerradurp1","Cerraduracutre",(12750.527394,-3913.883828,23023.731593),(0.006171,0.006171,0.707080,-0.707080),2.5)
#cerradurp1.key="llave1"
#
#
#cerradurp1.OnUnLockFunc=AbrePuertaLlave1
#cerradurp1.OnUnLockArgs=()
#
#cerradurp1.OnLockFunc=CierraPuertaLlave1
#cerradurp1.OnLockArgs=()
#
#darfuncs.SetHint(cerradurp1.obj,"Palace Lock")
#
#o=Bladex.CreateEntity("llave1","Llavecutre",11177.864234,-2425.544644,23457.325321,"Physic")
#o.Scale=1.0
#o.Orientation=0.014533,-0.997615,0.000385,0.067469
#darfuncs.SetHint(o,"Palace Key")

############################################################
############################################################
####-----PUERTAS---GALERIA--------ENTRADA AL PALACIO----------------------------#####
####----------------------------------------------------------------------------#####
############################################################
############################################################

spuertar1d=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
spuertar1d.MaxDistance=20000
spuertar1d.MinDistance=1000
spuertar1d.Volume=1.0


spuertar1g=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
spuertar1g.MaxDistance=20000
spuertar1g.MinDistance=2000
spuertar1g.Volume=1.0

puertar1=Doors.CreateDoor("Puertar1", (4687,-7500,11000), (0,1,0), 500, 5500, Doors.CLOSED)


puertar1.opentype=Doors.UNIF
puertar1.o_med_vel=-800
puertar1.o_med_displ=5000


puertar1.closetype=Doors.AC
puertar1.c_init_displ=5000
puertar1.c_med_vel=8000


puertar1.SetWhileOpenSound(spuertar1d)
puertar1.SetEndOpenSound(spuertar1g)

puertar1.SetWhileCloseSound(spuertar1d)
puertar1.SetEndCloseSound(spuertar1g)

###### Accionar puertas al accionar una palanca
#
#
#palanr1=Levers.PlaceLever("PALAP1",Levers.LeverType3,(2993.814489,-5320.805021,12239.742580),(0.183013,0.183013,-0.683013,0.683013),1.0)
#
#palanr1.mode=1
#
#
#
#
#
#
#palanr1.OnTurnOnFunc=AbrePuertar1
#palanr1.OnTurnOnArgs=()
#
#palanr1.OnTurnOffFunc=CierraPuertar1
#palanr1.OnTurnOffArgs=()
#
##################################
##################################2
##################################

spuertar2d=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
spuertar2d.MaxDistance=20000
spuertar2d.MinDistance=2000
spuertar2d.Volume=1.0


spuertar2g=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
spuertar2g.MaxDistance=20000
spuertar2g.MinDistance=2000
spuertar2g.Volume=1.0

puertar2=Doors.CreateDoor("Puertar2", (4687,-7500,3800), (0,1,0), 500, 5500, Doors.CLOSED)


puertar2.opentype=Doors.UNIF
puertar2.o_med_vel=-800
puertar2.o_med_displ=5000


puertar2.closetype=Doors.AC
puertar2.c_init_displ=5000
puertar2.c_med_vel=8000


puertar2.SetWhileOpenSound(spuertar2d)
puertar2.SetEndOpenSound(spuertar2g)

puertar2.SetWhileCloseSound(spuertar2d)
puertar2.SetEndCloseSound(spuertar2g)

###### Accionar puertas al accionar una palanca
#
#
#palanr2=Levers.PlaceLever("PALAP2",Levers.LeverType3,(6367.556072,-5534.301393,3038.806392),(0.707107,0.707107,0.0,0.0),1.0)
#
#palanr2.mode=1
#
#
#def AbrePuertar2():
#	puertar2.OpenDoor()
#
#
#def CierraPuertar2():
#	puertar2.CloseDoor()
#
#
#
#
#palanr2.OnTurnOnFunc=AbrePuertar2
#palanr2.OnTurnOnArgs=()
#
#palanr2.OnTurnOffFunc=CierraPuertar2
#palanr2.OnTurnOffArgs=()
#

################################
###---PUERTA DE LA CRIPTA---------------------####
################################
#-PUERTA-LLAVE-4


spuertal4d=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "MaderaDesliz")
spuertal4d.MaxDistance=20000
spuertal4d.MinDistance=2000
spuertal4d.Volume=1.0


spuertal4g=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "MaderaGolpe")
spuertal4g.MaxDistance=20000
spuertal4g.MinDistance=2000
spuertal4g.Volume=1.0

#puertal4=Doors.CreateDoor("Puerta4", (41500,-1000,15000), (0,1,0), 700, 4500, Doors.CLOSED)
puertal4=Doors.CreateDoor("Puerta4", (34250,-7000,49300), (0,1,0), 300, 5300, Doors.CLOSED)

puertal4.opentype=Doors.UNIF
puertal4.o_med_vel=-500
puertal4.o_med_displ=5000


puertal4.closetype=Doors.AC
puertal4.c_init_displ=5000
puertal4.c_med_vel=8000


puertal4.SetWhileOpenSound(spuertal4d)
puertal4.SetEndOpenSound(spuertal4g)

puertal4.SetWhileCloseSound(spuertal4d)
puertal4.SetEndCloseSound(spuertal4g)

###llave4 abrepuertal4###


cerradurp4=Locks.PlaceLock("cerradurp4","Cerraduracutre",(32264.656553,-4280.082849,48536.820385),(0.5,0.5,0.5,-0.5),2.5)
cerradurp4.key="llave4"

darfuncs.SetHint(cerradurp4.obj,"Crypt Lock")


cerradurp4.OnUnLockFunc=AbrePuertaLlave4
cerradurp4.OnUnLockArgs=()

cerradurp4.OnLockFunc=CierraPuertaLlave4
cerradurp4.OnLockArgs=()


#en la sala del trono
o=Bladex.CreateEntity("llave4","Llavecutre",-24081.664110,-1691.281205,-10789.123136,"Physic")
o.Scale=1.0
o.Orientation=0.567150,0.024639,-0.822649,0.031350
Stars.Twinkle("llave4")

#en la puerta
#o=Bladex.CreateEntity("llave4","Llavecutre",42932.308228,2723.693670,19050.841600,"Physic")
#o.Scale=1.0
#o.Orientation=0.027774,-0.998423,-0.006024,0.048422

darfuncs.SetHint(o,"Crypt Key")




##########################################################33
#####-------PUERTA DOBLE---SECRETO-MASTABA-----------#######
############################################################

spuertadoble1d=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "MaderaDesliz")
spuertadoble1d.MaxDistance=20000
spuertadoble1d.MinDistance=2000
spuertadoble1d.Volume=1.0


spuertadoble1g=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "MaderaGolpe")
spuertadoble1g.MaxDistance=20000
spuertadoble1g.MinDistance=2000
spuertadoble1g.Volume=1.0

puertadoble1=Doors.CreateDoor("PuertaDoble1", (-25750,-8000,86000), (-1,0,0), 0, 1750, Doors.CLOSED)


puertadoble1.opentype=Doors.UNIF
puertadoble1.o_med_vel=-400
puertadoble1.o_med_displ=1750

puertadoble1.closetype=Doors.UNIF
puertadoble1.c_med_displ=1750
puertadoble1.c_med_vel=400


puertadoble1.SetWhileOpenSound(spuertadoble1d)
puertadoble1.SetEndOpenSound(spuertadoble1g)

puertadoble1.SetWhileCloseSound(spuertadoble1d)
puertadoble1.SetEndCloseSound(spuertadoble1g)

#####
puertadoble2=Doors.CreateDoor("PuertaDoble2", (-27000,-8000,86000), (1,0,0), 0, 1750, Doors.CLOSED)

puertadoble2.opentype=Doors.UNIF
puertadoble2.o_med_vel=-400
puertadoble2.o_med_displ=1750

puertadoble2.closetype=Doors.UNIF
puertadoble2.c_med_displ=1750
puertadoble2.c_med_vel=400


#puertadoble2.SetWhileOpenSound(maderadesliz)
#puertadoble2.SetEndOpenSound(maderagolpe)

#puertadoble2.SetWhileCloseSound(maderadesliz)
#puertadoble2.SetEndCloseSound(maderagolpe)

##### Accionar puertas al accionar una palanca


paland5=Levers.PlaceLever("PALAP5",Levers.LeverType3,(-29225.783943,-5932.177901,86898.389463),(0.000000,0.000000,0.707107,-0.707107),1.0)

paland5.mode=1



paland5.OnTurnOnFunc=AbrePuertadoble
paland5.OnTurnOnArgs=()

paland5.OnTurnOffFunc=CierraPuertadoble
paland5.OnTurnOffArgs=()



#################################
######-----PUERTA A TERRAZAS ------ ########
#################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puertar6=Doors.CreateDoor("Puertar6", (1562,-11000,-14000), (0,1,0), 900, 4400, Doors.OPENED)


puertar6.opentype=Doors.UNIF
puertar6.o_med_vel=-800
puertar6.o_med_displ=3500


puertar6.closetype=Doors.AC
puertar6.c_init_displ=3500
puertar6.c_med_vel=8000


puertar6.SetWhileOpenSound(maderadesliz)
puertar6.SetEndOpenSound(maderagolpe)

puertar6.SetWhileCloseSound(maderadesliz)
puertar6.SetEndCloseSound(maderagolpe)

##### Accionar puertas al accionar una palanca


palanr6=Levers.PlaceLever("PALAP6",Levers.LeverType3,(2713.561494,-9095.757512,-15681.973560),(0.270598,0.270598,-0.653282,0.653282),1.0)

palanr6.mode=1





palanr6.OnTurnOnFunc=AbrePuertar6
palanr6.OnTurnOnArgs=()

palanr6.OnTurnOffFunc=CierraPuertar6
palanr6.OnTurnOffArgs=()


###########################################################################################################
##############################------------------------------------------------##############################
####---------------------------PUERTA----SALIDA---MURALLAS---------------------------------------------------#####
####---------------------------PUERTAS-PALANCA-----------------------------(se abre desde dentro)------#####
#############################-------------------------------------------------###############################
###########################################################################################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")

puertar7=Doors.CreateDoor("Puertar7", (11000,-13000,-1900), (0,1,0), 0, 4000, Doors.OPENED)

puertar7.opentype=Doors.UNIF
puertar7.o_med_vel=-800
puertar7.o_med_displ=4000

puertar7.closetype=Doors.AC
puertar7.c_init_displ=4000
puertar7.c_med_vel=8000

puertar7.SetWhileOpenSound(maderadesliz)
puertar7.SetEndOpenSound(maderagolpe)

puertar7.SetWhileCloseSound(maderadesliz)
puertar7.SetEndCloseSound(maderagolpe)

###### Accionar puertas al accionar una palanca


palanr7=Levers.PlaceLever("PALAP7",Levers.LeverType3,(9456.586137,-11352.064178,-3836.196309),(0.500000,0.500000,-0.500000,0.500000),1.0)
palanr7.mode=2

#def AbrePuertar7():
#	puertar7.OpenDoor()
#def CierraPuertar7():
#	puertar7.CloseDoor()
#

palanr7.OnTurnOnFunc=AbrePuertar7
palanr7.OnTurnOnArgs=()

palanr7.OnTurnOffFunc=CierraPuertar7
palanr7.OnTurnOffArgs=()


############################################################
#####---------------------------RASTRILLO-----------entrada----########################
############################################################

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

reja3=Bladex.CreateEntity("Reja3","Rastrillo",-24127.240290,-6180.838344,-52111.046901)
reja3.Static=1
reja3.Scale=1.22
reja3.Orientation=0.707080,0.707080,0.006171,-0.006171
Sparks.SetSparkling("Reja3")

reja3din=Objects.CreateDinamicObject("Reja3")

##### Abrir el rastrillo al accionar una palanca -comentado por Enric-


#darfuncs.EnterSecEvent(-10338.3556749, -1640.0134856, -29671.4120094,Cierrareja3)
#darfuncs.EnterSecEvent(-37515.6436505, -753.756454933, -28708.0127972,Cierrareja3)

#################################
######----PUERTA DOBLE FINAL----------#######
#################################

spuertadobleFdesliz=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "MaderaDesliz")
spuertadobleFdesliz.MaxDistance=40000
spuertadobleFdesliz.MinDistance=15000
spuertadobleFdesliz.Volume=1.0

spuertadobleFgolpe=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "MaderaGolpe")
spuertadobleFgolpe.MaxDistance=40000
spuertadobleFgolpe.MinDistance=15000
spuertadobleFgolpe.Volume=1.0



puertadobleF1=Doors.CreateDoor("PuertaDobleF1", (-154000,0,13000), (0,0,-1), 0, 4000, Doors.CLOSED)


puertadobleF1.opentype=Doors.UNIF
puertadobleF1.o_med_vel=-400
puertadobleF1.o_med_displ=4000

puertadobleF1.closetype=Doors.UNIF
puertadobleF1.c_med_displ=4000
puertadobleF1.c_med_vel=400


puertadobleF1.SetWhileOpenSound(spuertadobleFdesliz)
puertadobleF1.SetEndOpenSound(spuertadobleFgolpe)

puertadobleF1.SetWhileCloseSound(spuertadobleFdesliz)
puertadobleF1.SetEndCloseSound(spuertadobleFgolpe)

#####
puertadobleF2=Doors.CreateDoor("PuertaDobleF2", (-154000,0,10000), (0,0,1), 0, 4000, Doors.CLOSED)

puertadobleF2.opentype=Doors.UNIF
puertadobleF2.o_med_vel=-400
puertadobleF2.o_med_displ=4000

puertadobleF2.closetype=Doors.UNIF
puertadobleF2.c_med_displ=4000
puertadobleF2.c_med_vel=400


#puertadobleF2.SetWhileOpenSound(spuertadobleFdesliz)
#puertadobleF2.SetEndOpenSound(spuertadobleFgolpe)

#puertadobleF2.SetWhileCloseSound(spuertadobleFdesliz)
#puertadobleF2.SetEndCloseSound(spuertadobleFgolpe)

#####




#################################
#######----- PUERTA TABLILLA------------#######
#################################

spuertatablilladesliz=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "MaderaDesliz")
spuertatablilladesliz.MaxDistance=20000
spuertatablilladesliz.MinDistance=5000
spuertatablilladesliz.Volume=1.0

spuertatablillag=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "MaderaGolpe")
spuertatablillag.MaxDistance=20000
spuertatablillag.MinDistance=5000
spuertatablillag.Volume=1.0



puertatablilla=Doors.CreateDoor("Puertatablilla", (-44500,-9000,135500), (0,1,0), 1000, 7000, Doors.CLOSED)


puertatablilla.opentype=Doors.UNIF
puertatablilla.o_med_vel=-1000
puertatablilla.o_med_displ=6000

puertatablilla.closetype=Doors.UNIF
puertatablilla.c_med_displ=6000
puertatablilla.c_med_vel=1000


puertatablilla.SetWhileOpenSound(spuertatablilladesliz)
puertatablilla.SetEndOpenSound(spuertatablillag)

puertatablilla.SetWhileCloseSound(spuertatablilladesliz)
puertatablilla.SetEndCloseSound(spuertatablillag)



#####


o=Bladex.CreateEntity("bloquetF","AdoquinRuna",-44530.963040,-11507.139065,135833.931967,"Physic")
o.Scale=2.987797
o.Orientation=0.500000,0.500000,0.500000,-0.500000


buttonta=Button.CreateButtonCombination(0,AbrePuertatablilla,"")
buttonta.AddButton("bloquetF",3,(0,0,1),100,0,0,1)


#############################################
########  PUERTAS SALIDA DE TABLILLA  #######
#############################################

#1
maderadesliz=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "MaderaGolpe")


puertatablilla2=Doors.CreateDoor("Puertatablilla2", (-55250,-4000,124250), (0,1,0), 2000, 9500, Doors.CLOSED)


puertatablilla2.opentype=Doors.UNIF
puertatablilla2.o_med_vel=-1000
puertatablilla2.o_med_displ=7500

puertatablilla2.closetype=Doors.UNIF
puertatablilla2.c_med_displ=7500
puertatablilla2.c_med_vel=1000


puertatablilla2.SetWhileOpenSound(maderadesliz)
puertatablilla2.SetEndOpenSound(maderagolpe)

puertatablilla2.SetWhileCloseSound(maderadesliz)
puertatablilla2.SetEndCloseSound(maderagolpe)



#2
maderadesliz=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "MaderaGolpe")


puertatablilla3=Doors.CreateDoor("Puertatablilla3", (-50500,-1000,134937), (0,1,0), 0, 5500, Doors.CLOSED)


puertatablilla3.opentype=Doors.UNIF
puertatablilla3.o_med_vel=-1000
puertatablilla3.o_med_displ=5500

puertatablilla3.closetype=Doors.UNIF
puertatablilla3.c_med_displ=5500
puertatablilla3.c_med_vel=1000


puertatablilla3.SetWhileOpenSound(maderadesliz)
puertatablilla3.SetEndOpenSound(maderagolpe)

puertatablilla3.SetWhileCloseSound(maderadesliz)
puertatablilla3.SetEndCloseSound(maderagolpe)



##### Accionar puertas al accionar una palanca


palanPuertatablilla3=Levers.PlaceLever("PALAPPuertatablilla3",Levers.LeverType3,(-52723.996364,2416.056578,134007.642921),(0.707107,0.707107,0.0,0.0),1.0)

palanPuertatablilla3.mode=1





palanPuertatablilla3.OnTurnOnFunc=AbrePuertatablilla3
palanPuertatablilla3.OnTurnOnArgs=()

palanPuertatablilla3.OnTurnOffFunc=CierraPuertatablilla3
palanPuertatablilla3.OnTurnOffArgs=()

#############################################################
#-PUERTA-11	@@@@@@@@@@@@@@@		AL TEMPLO INFERIOR
#############################################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puertal11=Doors.CreateDoor("Puertal11", (-31700,-6000,57500), (0,1,0), 400, 4900, Doors.CLOSED)


puertal11.opentype=Doors.UNIF
puertal11.o_med_vel=-500
puertal11.o_med_displ=4500


puertal11.closetype=Doors.AC
puertal11.c_init_displ=4500
puertal11.c_med_vel=8000


puertal11.SetWhileOpenSound(maderadesliz)
puertal11.SetEndOpenSound(maderagolpe)

puertal11.SetWhileCloseSound(maderadesliz)
puertal11.SetEndCloseSound(maderagolpe)





############################################################################
#-PUERTA-12	@@@@@@@@@@@@@@@		ABRE LA PARTE ALTA DEL TEMPLO
############################################################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puertal12=Doors.CreateDoor("Puertal12", (-17600,-6000,57500), (0,1,0), 400, 4900, Doors.CLOSED)


puertal12.opentype=Doors.UNIF
puertal12.o_med_vel=-500
puertal12.o_med_displ=4500


puertal12.closetype=Doors.AC
puertal12.c_init_displ=4500
puertal12.c_med_vel=3000


puertal12.SetWhileOpenSound(maderadesliz)
puertal12.SetEndOpenSound(maderagolpe)

puertal12.SetWhileCloseSound(maderadesliz)
puertal12.SetEndCloseSound(maderagolpe)






##############################3
#-PUERTA-13	@@@@@@@@@@@@@@@		ABRE EL AGUA DEL MONOLITO
###############################



puertal13=Bladex.GetSector(-24750,12500,54000)
puertal13.Active = 0



##########################################################################3

####	COMPUERTAS DEL TEMPLO


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")

#1
compuerta1=Doors.CreateDoor("compuerta1", (-18000,-11600,28500), (0,0,1), 250, 3500, Doors.OPENED)

compuerta1.opentype=Doors.UNIF
compuerta1.o_med_vel=-500
compuerta1.o_med_displ=3250

compuerta1.closetype=Doors.AC
compuerta1.c_init_displ=3250
compuerta1.c_med_vel=3000

#puerta1.SetWhileOpenSound(maderadesliz)
#puerta1.SetEndOpenSound(maderagolpe)

#puerta1.SetWhileCloseSound(maderadesliz)
#puerta1.SetEndCloseSound(maderagolpe)


#2
compuerta2=Doors.CreateDoor("compuerta2", (-32000,-11600,28500), (0,0,1), 250, 3500, Doors.OPENED)

compuerta2.opentype=Doors.UNIF
compuerta2.o_med_vel=-500
compuerta2.o_med_displ=3250

compuerta2.closetype=Doors.AC
compuerta2.c_init_displ=3250
compuerta2.c_med_vel=3000

compuerta2.SetWhileOpenSound(maderadesliz)
compuerta2.SetEndOpenSound(maderagolpe)

compuerta2.SetWhileCloseSound(maderadesliz)
compuerta2.SetEndCloseSound(maderagolpe)




oo=Bladex.CreateEntity("blosu1","Adoquinpulsador2",-24877.117277,-2681.561885,42009.871041)
#o=Bladex.CreateEntity("blosu1","Bloque",-24870.406680,-2754.074488,41161.592563)
oo.Scale=1.518790
oo.Orientation=0.5,0.5,0.5,0.5
darfuncs.SetHint(oo,"Sacred Stone")

button=Button.CreateButtonCombination(0,FirstGemaScene,"")
button.AddButton("blosu1",3,(0,1,0),1100,0,0,1)


################################################################33333
####	BARROTES HORIZONTALES DE LA SALA DEL TRONO


#1
BARROTE1=Doors.CreateDoor("BARROTE1", (-14750,-2300,-12000), (0,0,-1), 250, 3000, Doors.CLOSED)

BARROTE1.opentype=Doors.UNIF
BARROTE1.o_med_vel=-500
BARROTE1.o_med_displ=2750

BARROTE1.closetype=Doors.AC
BARROTE1.c_init_displ=2750
BARROTE1.c_med_vel=3000

BARROTE1.SetWhileOpenSound(maderadesliz)
BARROTE1.SetEndOpenSound(maderagolpe)

BARROTE1.SetWhileCloseSound(maderadesliz)
BARROTE1.SetEndCloseSound(maderagolpe)

#2
BARROTE2=Doors.CreateDoor("BARROTE2", (-14750,-3800,-12000), (0,0,-1), 250, 3000, Doors.CLOSED)

BARROTE2.opentype=Doors.UNIF
BARROTE2.o_med_vel=-500
BARROTE2.o_med_displ=2750

BARROTE2.closetype=Doors.AC
BARROTE2.c_init_displ=2750
BARROTE2.c_med_vel=3000



##########################	AL OTRO LADO

#3
BARROTE3=Doors.CreateDoor("BARROTE3", (-33750,-2300,-12000), (0,0,-1), 250, 3000, Doors.CLOSED)

BARROTE3.opentype=Doors.UNIF
BARROTE3.o_med_vel=-500
BARROTE3.o_med_displ=2750

BARROTE3.closetype=Doors.AC
BARROTE3.c_init_displ=2750
BARROTE3.c_med_vel=3000

#BARROTE3.SetWhileOpenSound(maderadesliz)
#BARROTE3.SetEndOpenSound(maderagolpe)

#BARROTE3.SetWhileCloseSound(maderadesliz)
#BARROTE3.SetEndCloseSound(maderagolpe)

#4
BARROTE4=Doors.CreateDoor("BARROTE4", (-33750,-3800,-12000), (0,0,-1), 250, 3000, Doors.CLOSED)

BARROTE4.opentype=Doors.UNIF
BARROTE4.o_med_vel=-500
BARROTE4.o_med_displ=2750

BARROTE4.closetype=Doors.AC
BARROTE4.c_init_displ=2750
BARROTE4.c_med_vel=3000




##############################################################################
###
###	PUERTA DE LA MURALLA



#2
maderadesliz=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "MaderaGolpe")


PTAMURALLA=Doors.CreateDoor("PTAMURALLA", (-1000,-4000,-36000), (0,0,-1), 0, 2500, Doors.CLOSED)


PTAMURALLA.opentype=Doors.UNIF
PTAMURALLA.o_med_vel=-1000
PTAMURALLA.o_med_displ=2500

PTAMURALLA.closetype=Doors.UNIF
PTAMURALLA.c_med_displ=2500
PTAMURALLA.c_med_vel=1000


PTAMURALLA.SetWhileOpenSound(maderadesliz)
PTAMURALLA.SetEndOpenSound(maderagolpe)

PTAMURALLA.SetWhileCloseSound(maderadesliz)
PTAMURALLA.SetEndCloseSound(maderagolpe)



##### Accionar puertas al accionar una palanca


palanPTAMURALLA=Levers.PlaceLever("PALANMURALLA",Levers.LeverType3,(641.072000,-1414.292000,-34677.489000),(0.707107,0.707107,0.0,0.0),1.0)

palanPTAMURALLA.mode=2




palanPTAMURALLA.OnTurnOnFunc=AbrePTAMURALLA
palanPTAMURALLA.OnTurnOnArgs=()

palanPTAMURALLA.OnTurnOffFunc=CierraPTAMURALLA
palanPTAMURALLA.OnTurnOffArgs=()



############################################################
#####---------------RASTRILLOS------ENTRADA AL GOLEM-------########################
############################################################


###1
sonidorastrillo4=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golperastrillo4=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

reja4=Bladex.CreateEntity("Reja4","Rastrillo",-20007.987000,-5309.224000,105746.593000)
reja4.Scale=0.685153
reja4.Orientation=0.5,0.5,0.5,-0.5
Sparks.SetSparkling("Reja4")

reja4din=Objects.CreateDinamicObject("Reja4")

##funciones abrir-cerrar##


##### Abrir el rastrillo al accionar una palanca


palanr4=Levers.PlaceLever("PalanR4",Levers.LeverType3,(-20639.726000,-4448.382000,108740.778000),(0.500000,0.500000,0.500000,-0.500000),1.0)
palanr4.mode=3


palanr4.OnTurnOnFunc=Abrereja4
palanr4.OnTurnOnArgs=()

palanr4.OnTurnOffFunc=Cierrareja4
palanr4.OnTurnOffArgs=()



###2
sonidorastrillo5=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golperastrillo5=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

reja5=Bladex.CreateEntity("Reja5","Rastrillo",-31760.124000,-5303.573000,105742.228000)
reja5.Scale=0.685153
reja5.Orientation=0.495618,0.495618,0.504344,-0.504344
Sparks.SetSparkling("Reja5")

reja5din=Objects.CreateDinamicObject("Reja5")

##funciones abrir-cerrar##


##### Abrir el rastrillo al accionar una palanca


palanr5=Levers.PlaceLever("PalanR5",Levers.LeverType3,(-30831.122000,-4488.526000,108945.922000),(0.500000,0.500000,-0.500000,0.500000),1.0)
palanr5.mode=3


palanr5.OnTurnOnFunc=Abrereja5
palanr5.OnTurnOnArgs=()

palanr5.OnTurnOffFunc=Cierrareja5
palanr5.OnTurnOffArgs=()

##########################################
#####-------PUERTA DOBLE--TEMPLO---#######
##########################################

#spuertaTemplo1D=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "MaderaDesliz")
#spuertaTemplo1D.MaxDistance=20000
#spuertaTemplo1D.MinDistance=10000
#spuertaTemplo1D.Volume=1.0
#
#
#spuertaTemplo1G=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "MaderaGolpe")
#spuertaTemplo1G.MaxDistance=20000
#spuertaTemplo1G.MinDistance=10000
#spuertaTemplo1G.Volume=1.0
#
#
#puertadobleTemplo1=Doors.CreateDoor("puertadobleTemplo1", (-23000,-6000,23500), (-1,0,0), 0, 2125, Doors.CLOSED)
#
#puertadobleTemplo1.opentype=Doors.UNIF
#puertadobleTemplo1.o_med_vel=-400
#puertadobleTemplo1.o_med_displ=2125
#
#puertadobleTemplo1.closetype=Doors.UNIF
#puertadobleTemplo1.c_med_displ=2125
#puertadobleTemplo1.c_med_vel=800
#
#
#puertadobleTemplo1.SetWhileOpenSound(spuertaTemplo1D)
#puertadobleTemplo1.SetEndOpenSound(spuertaTemplo1G)
#
#puertadobleTemplo1.SetWhileCloseSound(spuertaTemplo1D)
#puertadobleTemplo1.SetEndCloseSound(spuertaTemplo1G)
#
######
#
#puertadobleTemplo2=Doors.CreateDoor("puertadobleTemplo2", (-25000,-6000,23500), (1,0,0), 0, 2125, Doors.CLOSED)
#
#
#puertadobleTemplo2.opentype=Doors.UNIF
#puertadobleTemplo2.o_med_vel=-400
#puertadobleTemplo2.o_med_displ=2125
#
#puertadobleTemplo2.closetype=Doors.UNIF
#puertadobleTemplo2.c_med_displ=2125
#puertadobleTemplo2.c_med_vel=800
#
###### Accionar puertas
#
#def AbrepuertadobleTemplo():
#	puertadobleTemplo1.OpenDoor()
#	puertadobleTemplo2.OpenDoor()
#
#def CierrapuertadobleTemplo():
#	puertadobleTemplo1.CloseDoor()
#	puertadobleTemplo2.CloseDoor()
#

############################################################
#####---------------------------RASTRILLO-----------entrada--palacio--########################
############################################################

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

reja1=Bladex.CreateEntity("Reja1","Rastrillo",13308.381907,-5818.312674,19277.431262)
reja1.Static=1
reja1.Scale=0.795442
reja1.Orientation=0.500000,0.500000,-0.500000,0.500000
Sparks.SetSparkling("Reja1")

reja1din=Objects.CreateDinamicObject("Reja1")

###llave1 abrepuerta1###


cerradurp1=Locks.PlaceLock("cerradurp1","Cerraduracutre",(12015.212852,-4995.497349,21408.891701),(0.500000,0.500000,0.500000,-0.500000),2.54)
cerradurp1.key="llave1"


cerradurp1.OnUnLockFunc=Abrereja1
cerradurp1.OnUnLockArgs=()

cerradurp1.OnLockFunc=Cierrareja1
cerradurp1.OnLockArgs=()

darfuncs.SetHint(cerradurp1.obj,"Palace Lock")

o=Bladex.CreateEntity("llave1","Llavecutre",11364.532654,-3770.990875,20552.762869,"Physic")
o.Scale=1.0
o.Orientation=0.999603,0.020557,-0.019025,-0.002891
o.Data = 1
darfuncs.SetHint(o,"Palace Key")
Stars.Twinkle("llave1")



darfuncs. EnterSecEvent(-8750, 0, -127000,CierraPuertar6)
darfuncs. EnterSecEvent(-8750, 0, -127000,CierraPuertar7)
darfuncs. EnterSecEvent(-8750, 0, -127000,Cierracompuertas)