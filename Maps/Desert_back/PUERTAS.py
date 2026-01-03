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


############################################################
############################################################
####-----PUERTAS---GALERIA--------ENTRADA AL PALACIO----------------------------#####
####----------------------------------------------------------------------------#####
############################################################
############################################################
"""
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

"""

################################
###---PUERTA DE LA CRIPTA---------------------####
################################


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
"""
maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puertar6=Doors.CreateDoor("Puertar6", (1562,-11000,-14000), (0,1,0), 900, 4400, Doors.CLOSED)


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

"""
###########################################################################################################
##############################------------------------------------------------##############################
####---------------------------PUERTA----SALIDA---MURALLAS---------------------------------------------------#####
####---------------------------PUERTAS-PALANCA-----------------------------(se abre desde dentro)------#####
#############################-------------------------------------------------###############################
###########################################################################################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")

puertar7=Doors.CreateDoor("Puertar7", (11000,-13000,-1900), (0,1,0), 0, 4000, Doors.CLOSED)

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



############################################################################
#-PUERTA-12	@@@@@@@@@@@@@@@		ABRE LA PARTE ALTA DEL TEMPLO
############################################################################


##############################3
#-PUERTA-13	@@@@@@@@@@@@@@@		ABRE EL AGUA DEL MONOLITO
###############################


##########################################################################3

####	COMPUERTAS DEL TEMPLO



################################################################33333
####	BARROTES HORIZONTALES DE LA SALA DEL TRONO


##############################################################################
###
###	PUERTA DE LA MURALLA






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


############################################################
#####---------------------------RASTRILLO-----------entrada--palacio--########################
############################################################
