import Bladex
import Doors
import Levers
import Locks
import Objects
import Sounds
import Button
import ReadGSFile
import AuxFuncs
import darfuncs
import Stars

###########################################
###-----PUERTA---PRINCIPAL---TORRE------###
###########################################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta1=Doors.CreateDoor("Puerta1", (-39000,-7000,59125), (0,1,0), 1000, 4800, Doors.CLOSED)


puerta1.opentype=Doors.UNIF
puerta1.o_med_vel=-1300
puerta1.o_med_displ=3800


puerta1.closetype=Doors.AC
puerta1.c_init_displ=3800
puerta1.c_med_vel=8000


puerta1.SetWhileOpenSound(maderadesliz)
puerta1.SetEndOpenSound(maderagolpe)

puerta1.SetWhileCloseSound(maderadesliz)
puerta1.SetEndCloseSound(maderagolpe)


###########################################


cerradurp1=Locks.PlaceLock("cerradurp1","Cerraduracutre",(-40796.623959,-5480.649313,59840.403234),(0.704469,0.692280,-0.109646,0.111577),2.573538)
cerradurp1.key="llave1"


cerradurp1.OnUnLockFunc=AbrePuertaLlave1
cerradurp1.OnUnLockArgs=()

cerradurp1.OnLockFunc=CierraPuertaLlave1
cerradurp1.OnLockArgs=()

darfuncs.SetHint(cerradurp1.obj,"Iron Lock")


# delante de la puerta
#o=Bladex.CreateEntity("llave1","Llavecutre",-38026.289440,-4222.975507,60002.963203,"Physic")
#o.Scale=1.0
#o.Orientation=0.012447,-0.999707,-0.004202,0.020323

# sobre la mesa de las murallas
o=Bladex.CreateEntity("llave1","Llavecutre",-71263.520572,-7783.743090,11658.672014,"Physic")
o.Data=2
o.Scale=1.000000
o.Orientation=0.002454,0.990471,-0.002736,0.137672
darfuncs.SetHint(o,"Iron Key")
Stars.Twinkle("llave1")

############################################################
####---------------------------------------------------------------------------------------------#####
####--------------------------PUERTA---PALANCA---AL PATIO DEL ALJIVE-----------------------------#####
############################################################

maderadesliz2=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe2=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta2=Doors.CreateDoor("Puerta2", (-20500,0,-24000), (1,0,0), 0, 4000, Doors.CLOSED)


puerta2.opentype=Doors.UNIF
puerta2.o_med_vel=-800
puerta2.o_med_displ=4000


puerta2.closetype=Doors.AC
puerta2.c_init_displ=4000
puerta2.c_med_vel=8000


puerta2.SetWhileOpenSound(maderadesliz2)
puerta2.SetEndOpenSound(maderagolpe2)

puerta2.SetWhileCloseSound(maderadesliz2)
puerta2.SetEndCloseSound(maderagolpe2)

##### Accionar puertas al accionar una palanca


palan2=Levers.PlaceLever("PALAP2",Levers.LeverType3,(-23296.483840,92.536693,-25078.864131),(0.707107,0.707107,0.0,0.0),1.0)

palan2.mode=1



palan2.OnTurnOnFunc=AbrePuerta2
palan2.OnTurnOnArgs=()

palan2.OnTurnOffFunc=CierraPuerta2
palan2.OnTurnOffArgs=()




###########################################################
###-----PUERTA---LLAVE--PARA--SUBIR--A--LA---TORRE------###
###########################################################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-metal .wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/golpe-metal-pesado.wav", "MaderaGolpe")


puerta3=Doors.CreateDoor("Puerta3", (-18500,0,7600), (-1,0,0), 0, 2500, Doors.CLOSED)


puerta3.opentype=Doors.UNIF
puerta3.o_med_vel=-500
puerta3.o_med_displ=2500


puerta3.closetype=Doors.AC
puerta3.c_init_displ=2500
puerta3.c_med_vel=8000


puerta3.SetWhileOpenSound(maderadesliz)
puerta3.SetEndOpenSound(maderagolpe)

puerta3.SetWhileCloseSound(maderadesliz)
puerta3.SetEndCloseSound(maderagolpe)


###########################################


cerradurp3=Locks.PlaceLock("cerradurp3","Cerraduracutre",(-16130.806449,1290.759416,6535.902211),(0.500000,0.500000,0.500000,-0.500000),2.54)
cerradurp3.key="llave"


cerradurp3.OnUnLockFunc=AbrePuertaLlave3
cerradurp3.OnUnLockArgs=()

cerradurp3.OnLockFunc=CierraPuertaLlave3
cerradurp3.OnLockArgs=()

darfuncs.SetHint(cerradurp3.obj,"Dungeon Lock")


# delante de la puerta
#o=Bladex.CreateEntity("llave","Llavecutre",-19920.842241,2477.744425,5534.983546,"Physic")

# en el altar
o=Bladex.CreateEntity("llave","Llavecutre",-34804.570288,7831.057706,-43280.420052,"Physic")
o.Data=3
o.Scale=1.0
o.Orientation=0.015279,0.995222,-0.000219,-0.096430
darfuncs.SetHint(o,"Dungeon Key")
Stars.Twinkle("llave")




############################################################
####-----------------------------------------------------#####
####----------PUERTA---PALANCA---2�---PLANTA-------------#####
############################################################

maderadesliz4=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe4=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta4=Doors.CreateDoor("Puerta4", (-14500,-13000,30750), (0,1,0), 500, 3500, Doors.CLOSED)


puerta4.opentype=Doors.UNIF
puerta4.o_med_vel=-800
puerta4.o_med_displ=3000


puerta4.closetype=Doors.AC
puerta4.c_init_displ=3000
puerta4.c_med_vel=8000


puerta4.SetWhileOpenSound(maderadesliz4)
puerta4.SetEndOpenSound(maderagolpe4)

puerta4.SetWhileCloseSound(maderadesliz4)
puerta4.SetEndCloseSound(maderagolpe4)

##### Accionar puertas al accionar una palanca


palan4=Levers.PlaceLever("PALAP4",Levers.LeverType3,(-13746.282100,-11256.881440,34447.926772),(0.5,0.5,-0.5,0.5),1.0)

palan4.mode=0


puerta4.OnEndOpenFunc=ParaArenillaPuerta4
puerta4.OnEndCloseFunc=CierraPuerta4_2


palan4.OnTurnOnFunc=AbrePuerta4
palan4.OnTurnOnArgs=()

palan4.OnTurnOffFunc=CierraPuerta4
palan4.OnTurnOffArgs=()

############################################################
####--------------------------------------------------------------------------------------------#####
####------PUERTA---PALANCA---TORRE---3�-PLANTA--------------------------------------------------#####
############################################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta5=Doors.CreateDoor("Puerta5", (-14750,-18000,31000), (0,1,0), 500, 4000, Doors.CLOSED)


puerta5.opentype=Doors.UNIF
puerta5.o_med_vel=-800
puerta5.o_med_displ=3500


puerta5.closetype=Doors.AC
puerta5.c_init_displ=3500
puerta5.c_med_vel=8000


puerta5.SetWhileOpenSound(maderadesliz)
puerta5.SetEndOpenSound(maderagolpe)

puerta5.SetWhileCloseSound(maderadesliz)
puerta5.SetEndCloseSound(maderagolpe)

##### Accionar puertas al accionar una palanca


palan5=Levers.PlaceLever("PALAP5",Levers.LeverType3,(-26017.148373,-17595.593834,28858.211272),(0.500000,0.500000,0.500000,-0.500000),1.0)

palan5.mode=1






palan5.OnTurnOnFunc=AbrePuerta5
palan5.OnTurnOnArgs=()

palan5.OnTurnOffFunc=CierraPuerta5
palan5.OnTurnOffArgs=()


##############################################################################
##############################################################################

###### Definici�n de los sonidos de todas las puertas -incluyendo las objeto-

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")




#################################################
##### rastrillo a la segunda parte 	    #####

rast91=Bladex.CreateEntity("reja35","Rastrillo",-6286.455000,-6311.651000,30820.320000)
rast91.Scale=0.665003
rast91.Orientation=0.504344,0.504344,-0.495618,0.495618


rast91din=Objects.CreateDinamicObject("reja35")




############################################################
####-------------------------------------------------------------------#####
####------PUERTA---PALANCA---GALERIA----PLANTA---BAJ-------------------#####
############################################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta7=Doors.CreateDoor("Puerta7", (2000,-8000,-24930), (0,1,0), 500, 4000, Doors.CLOSED)


puerta7.opentype=Doors.UNIF
puerta7.o_med_vel=-800
puerta7.o_med_displ=3500


puerta7.closetype=Doors.AC
puerta7.c_init_displ=3500
puerta7.c_med_vel=8000


puerta7.SetWhileOpenSound(maderadesliz)
puerta7.SetEndOpenSound(maderagolpe)

puerta7.SetWhileCloseSound(maderadesliz)
puerta7.SetEndCloseSound(maderagolpe)

##### Accionar puertas al accionar una palanca


palan7=Levers.PlaceLever("PALAP7",Levers.LeverType3,(6774.627107,-6083.664079,-24652.429113),(0.0,0.0,0.707107,-0.707107),1.0)

palan7.mode=1






palan7.OnTurnOnFunc=AbrePuerta7
palan7.OnTurnOnArgs=()

palan7.OnTurnOffFunc=CierraPuerta7
palan7.OnTurnOffArgs=()

##############################################################################################################
####################################################

###---PUERTA---TORRE--3�-PLANTA--Y--SIGUIENTES------------------------------------###

####################################################
##############################################################################################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta8=Doors.CreateDoor("Puerta8", (-14750,-26000,31000), (0,1,0), 1000, 4500, Doors.CLOSED)


puerta8.opentype=Doors.UNIF
puerta8.o_med_vel=-500
puerta8.o_med_displ=3500


puerta8.closetype=Doors.AC
puerta8.c_init_displ=3500
puerta8.c_med_vel=8000


puerta8.SetWhileOpenSound(maderadesliz)
puerta8.SetEndOpenSound(maderagolpe)

puerta8.SetWhileCloseSound(maderadesliz)
puerta8.SetEndCloseSound(maderagolpe)


###########################################


cerradurp8=Locks.PlaceLock("cerradurp8","Cerraduracutre",(-13848.165294,-23522.101741,32405.821862),(0.707080,0.707080,-0.006,-0.006),2.54)
cerradurp8.key="llave8"


cerradurp8.OnUnLockFunc=AbrePuertaLlave8
cerradurp8.OnUnLockArgs=()

cerradurp8.OnLockFunc=CierraPuertaLlave8
cerradurp8.OnLockArgs=()

darfuncs.SetHint(cerradurp8.obj,"Tower Lock")

o=Bladex.CreateEntity("llave8","Llavecutre",-12628.242792,-22272.365901,31232.800632)
o.Static=0
o.Scale=1.0
darfuncs.SetHint(o,"Tower Key")
o.Orientation=0.006559,-0.975726,-0.006481,-0.218802


############################################################
####---------------------------------------------------------------------------#####
####--------PUERTA---PALANCA------------DOBLE--ESCALERA-1----------------------#####
############################################################

############################################################
####---------------------------------------------------------------------------#####
####--------PUERTA---PALANCA-----------------------DOBLE---ESCALERA-2----------#####
############################################################

###########################################
########-----------------------PUERTAS--MAGICAS---PUENTE-------###
###########################################

###1
maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta12=Doors.CreateDoor("Puerta12", (-144375,1000,38000), (0,1,0), 2000, 6000, Doors.CLOSED)


puerta12.opentype=Doors.UNIF
puerta12.o_med_vel=-1600
puerta12.o_med_displ=4000


puerta12.SetWhileOpenSound(maderadesliz)
puerta12.SetEndOpenSound(maderagolpe)



s12=Bladex.GetSector(-147000,-2000,38000)
s12.OnEnter=AbrePuerta12


###2,3

res=ReadGSFile.ReadGhostSectorFile("patra.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

char.SendTriggerSectorMsgs=1

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta13=Doors.CreateDoor("Puerta13", (-124625,-3000,38000), (0,1,0), 2000, 6000, Doors.CLOSED)

puerta13.opentype=Doors.UNIF
puerta13.o_med_vel=-1600
puerta13.o_med_displ=4000

puerta13.closetype=Doors.AC
puerta13.c_init_displ=4000
puerta13.c_med_vel=8000


puerta13.SetWhileOpenSound(maderadesliz)
puerta13.SetEndOpenSound(maderagolpe)

puerta13.SetWhileCloseSound(maderadesliz)
puerta13.SetEndCloseSound(maderagolpe)


puerta14=Doors.CreateDoor("Puerta14", (-119375,-3000,38000), (0,1,0), 2000, 6000, Doors.CLOSED)


puerta14.opentype=Doors.UNIF
puerta14.o_med_vel=-1000
puerta14.o_med_displ=4000


puerta14.closetype=Doors.AC
puerta14.c_init_displ=4000
puerta14.c_med_vel=8000

ladoABIERTO=0

print("poniendo el trigger sector")
Bladex.SetTriggerSectorFunc("patra", "OnEnter", EntroEnTriggerSector)


###4
maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta15=Doors.CreateDoor("Puerta15", (-100625,-3000,38000), (0,1,0), 2000, 6000, Doors.CLOSED)


puerta15.opentype=Doors.UNIF
puerta15.o_med_vel=-1000
puerta15.o_med_displ=4000


puerta15.closetype=Doors.AC
puerta15.c_init_displ=4000
puerta15.c_med_vel=8000


puerta15.SetWhileOpenSound(maderadesliz)
puerta15.SetEndOpenSound(maderagolpe)

puerta15.SetWhileCloseSound(maderadesliz)
puerta15.SetEndCloseSound(maderagolpe)


s15=Bladex.GetSector(-110000,-5000,38000)
s15.OnEnter=AbrePuerta15


###5
maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta16=Doors.CreateDoor("Puerta16", (-90875,-2000,30500), (0,1,0), 2000, 6000, Doors.OPENED)


puerta16.opentype=Doors.UNIF
puerta16.o_med_vel=-800
puerta16.o_med_displ=4000
puerta16.closetype=Doors.AC
puerta16.c_init_displ=4000
puerta16.c_med_vel=8000


puerta16.SetWhileOpenSound(maderadesliz)
puerta16.SetEndOpenSound(maderagolpe)

puerta16.SetWhileCloseSound(maderadesliz)
puerta16.SetEndCloseSound(maderagolpe)


s16=Bladex.GetSector(-78500,-4000,30500)
s16.OnEnter=CierraPuerta16



###########################################
###----------------PUERTAS---DEMONIO---TORRE------------------------###
###########################################


#1 se abre al matar a los esqueletos
maderadesliz17=Sounds.CreateEntitySound("../../Sounds/puerta-metal .wav", "MaderaDesliz")
maderadesliz17.MaxDistance=20000
maderadesliz17.MinDistance=2000
maderadesliz17.Volume=1.0

maderagolpe17=Sounds.CreateEntitySound("../../Sounds/golpe-metal-pesado.wav", "MaderaGolpe")
maderagolpe17.MaxDistance=20000
maderagolpe17.MinDistance=2000
maderagolpe17.Volume=1.0

puerta17=Doors.CreateDoor("Puerta17", (-49500,-52000,34437), (0,1,0), 2000, 5000, Doors.CLOSED)

puerta17.opentype=Doors.UNIF
puerta17.o_med_vel=-500
puerta17.o_med_displ=3000

puerta17.closetype=Doors.AC
puerta17.c_init_displ=3000
puerta17.c_med_vel=6000

puerta17.SetWhileOpenSound(maderadesliz17)
puerta17.SetEndOpenSound(maderagolpe17)

puerta17.SetWhileCloseSound(maderadesliz17)
puerta17.SetEndCloseSound(maderagolpe17)

s17=Bladex.GetSector(-49000,-51000,29000)
s17.OnEnter=CierraPuerta17

puerta17.Squezze = 1

#2
maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-metal .wav", "MaderaDesliz")
maderadesliz.MaxDistance=20000
maderadesliz.MinDistance=2000
maderadesliz.Volume=1.0

maderagolpe=Sounds.CreateEntitySound("../../Sounds/golpe-metal-pesado.wav", "MaderaGolpe")
maderagolpe.MaxDistance=20000
maderagolpe.MinDistance=2000
maderagolpe.Volume=1.0

puerta18=Doors.CreateDoor("Puerta18", (-49500,-51000,26437), (0,1,0), 1000, 4000, Doors.OPENED)


puerta18.opentype=Doors.UNIF
puerta18.o_med_vel=-500
puerta18.o_med_displ=3000


puerta18.closetype=Doors.AC
puerta18.c_init_displ=3000
puerta18.c_med_vel=6000
puerta18.Squezze = 1

puerta18.SetWhileOpenSound(maderadesliz)
puerta18.SetEndOpenSound(maderagolpe)

puerta18.SetWhileCloseSound(maderadesliz)
puerta18.SetEndCloseSound(maderagolpe)


s18=Bladex.GetSector(-49000,-50000,22000)
s18.OnEnter=CierraPuerta18

#3
maderadesliz19=Sounds.CreateEntitySound("../../Sounds/puerta-metal .wav", "MaderaDesliz")
maderadesliz19.MaxDistance=20000
maderadesliz19.MinDistance=2000
maderadesliz19.Volume=1.0

maderagolpe19=Sounds.CreateEntitySound("../../Sounds/golpe-metal-pesado.wav", "MaderaGolpe")
maderagolpe19.MaxDistance=20000
maderagolpe19.MinDistance=2000
maderagolpe19.Volume=1.0


puerta19=Doors.CreateDoor("Puerta19", (-44750,-51000,21000), (0,1,0), 1000, 4000, Doors.OPENED)


puerta19.opentype=Doors.UNIF
puerta19.o_med_vel=-500
puerta19.o_med_displ=3000


puerta19.closetype=Doors.AC
puerta19.c_init_displ=3000
puerta19.c_med_vel=6000
puerta19.Squezze = 1

puerta19.SetWhileOpenSound(maderadesliz19)
puerta19.SetEndOpenSound(maderagolpe19)

puerta19.SetWhileCloseSound(maderadesliz19)
puerta19.SetEndCloseSound(maderagolpe19)


####-----PUERTA DEL DEMONIO---(se abre al morir el demonio)

maderadesliz20=Sounds.CreateEntitySound("../../Sounds/puerta-metal .wav", "MaderaDesliz")
maderadesliz20.MaxDistance=20000
maderadesliz20.MinDistance=2000
maderadesliz20.Volume=1.0

maderagolpe20=Sounds.CreateEntitySound("../../Sounds/golpe-metal-pesado.wav", "MaderaGolpe")
maderagolpe20.MaxDistance=20000
maderagolpe20.MinDistance=2000
maderagolpe20.Volume=1.0

puerta20=Doors.CreateDoor("Puerta20", (-29000,-50000,34900), (1,0,0), 0, 2000, Doors.CLOSED)
puertai20=Doors.CreateDoor("Puertai20", (-28000,-50000,34900), (-1,0,0), 0, 2000, Doors.CLOSED)

#
puerta20.opentype=Doors.UNIF
puerta20.o_med_vel=-500
puerta20.o_med_displ=2000

puerta20.closetype=Doors.AC
puerta20.c_init_displ=2000
puerta20.c_med_vel=7000

#
puertai20.opentype=Doors.UNIF
puertai20.o_med_vel=-500
puertai20.o_med_displ=2000

puertai20.closetype=Doors.AC
puertai20.c_init_displ=2000
puertai20.c_med_vel=7000


puerta20.SetWhileOpenSound(maderadesliz20)
puerta20.SetEndOpenSound(maderagolpe20)

puerta20.SetWhileCloseSound(maderadesliz20)
puerta20.SetEndCloseSound(maderagolpe20)


############################################################
####---------------------------------------------------#####
####--------PUERTA---PALANCA---ALJIVE------------------#####
############################################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta21=Doors.CreateDoor("Puerta21", (-49000,-1000,-34000), (1,0,0), 0, 2750, Doors.CLOSED)


puerta21.opentype=Doors.UNIF
puerta21.o_med_vel=-800
puerta21.o_med_displ=2750


puerta21.closetype=Doors.AC
puerta21.c_init_displ=2750
puerta21.c_med_vel=800


puerta21.SetWhileOpenSound(maderadesliz)
puerta21.SetEndOpenSound(maderagolpe)

puerta21.SetWhileCloseSound(maderadesliz)
puerta21.SetEndCloseSound(maderagolpe)

##### Accionar puertas al accionar una palanca


palan21=Levers.PlaceLever("PALAP21",Levers.LeverType3,(-52883.027796,1019.507283,-34770.791629),(0.707107,0.707107,0.000000,0.000000),1.0)

palan21.mode=1


palan21.OnTurnOnFunc=AbrePuerta21
palan21.OnTurnOnArgs=()

palan21.OnTurnOffFunc=CierraPuerta21
palan21.OnTurnOffArgs=()


###########################################
###-----PUERTA---puente---con---llave1------###
###########################################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta22=Doors.CreateDoor("Puerta22", (-66875,-8000,-17500), (0,0,1), 0, 2250, Doors.CLOSED)


puerta22.opentype=Doors.UNIF
puerta22.o_med_vel=-700
puerta22.o_med_displ=2250


puerta22.closetype=Doors.UNIF
puerta22.c_init_displ=2250
puerta22.c_med_vel=-700


puerta22.SetWhileOpenSound(maderadesliz)
puerta22.SetEndOpenSound(maderagolpe)

puerta22.SetWhileCloseSound(maderadesliz)
puerta22.SetEndCloseSound(maderagolpe)


###########################################


cerradurp22=Locks.PlaceLock("cerradurp22","Cerraduracutre",(-67779.620560,-7582.727474,-18925.874878),(0.006171,0.006171,-0.707080,0.707080),2.573538)
cerradurp22.key="llave1"


cerradurp22.OnUnLockFunc=AbrePuertaLlave22
cerradurp22.OnUnLockArgs=()

cerradurp22.OnLockFunc=CierraPuertaLlave22
cerradurp22.OnLockArgs=()


####################	PUERTA DE REJA DEL MINORX


rast23=Bladex.CreateEntity("Rast23","Rastrillo",-50163.231738,-13037.350157,30808.235967)
rast23.Static=1
rast23.Scale=0.685153
rast23.Orientation=0.500000,0.500000,-0.500000,0.500000

rast23din=Objects.CreateDinamicObject("Rast23")


##funciones abrir-cerrar##

############################################################
####---------------------------------------------------#####
####--------PUERTAS---PALANCA---SALA--CHIMENEA---------#####
############################################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta24=Doors.CreateDoor("Puerta24", (750,-8000,-1200), (0,1,0), 600, 4600, Doors.CLOSED)

puerta24.opentype=Doors.UNIF
puerta24.o_med_vel=-800
puerta24.o_med_displ=4000

puerta24.closetype=Doors.AC
puerta24.c_init_displ=4000
puerta24.c_med_vel=800


puerta25=Doors.CreateDoor("Puerta25", (7750,-8000,-1200), (0,1,0), 600, 4600, Doors.CLOSED)

puerta25.opentype=Doors.UNIF
puerta25.o_med_vel=-800
puerta25.o_med_displ=4000

puerta25.closetype=Doors.AC
puerta25.c_init_displ=4000
puerta25.c_med_vel=800


puerta24.SetWhileOpenSound(maderadesliz)
puerta24.SetEndOpenSound(maderagolpe)

puerta24.SetWhileCloseSound(maderadesliz)
puerta24.SetEndCloseSound(maderagolpe)

##### Accionar puertas al accionar una palanca


palan24=Levers.PlaceLever("PALAP24",Levers.LeverType3,(4238.100816,-5850.063631,-1964.587692),(0.707107,0.707107,0.000000,0.000000),1.0)

palan24.mode=3


palan24.OnTurnOnFunc=AbrePuertaCHI
palan24.OnTurnOnArgs=()

palan24.OnTurnOffFunc=CierraPuertaCHI
palan24.OnTurnOffArgs=()



############################################################
####---------------------------------------------------#####
####--------PUERTAS---SALA---TRONO---------------------#####
############################################################

maderadesliz1=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz1")
maderagolpe1=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe1")

maderadesliz2=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz2")
maderagolpe2=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe2")

maderadesliz3=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz3")
maderagolpe3=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe3")

maderadesliz4=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz4")
maderagolpe4=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe4")

maderadesliz5=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz5")
maderagolpe5=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe5")

maderadesliz6=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz6")
maderagolpe6=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe6")

#1
puerta26=Doors.CreateDoor("Puerta26", (-45500,-7000,45500), (0,1,0), 0, 4000, Doors.CLOSED)

puerta26.opentype=Doors.UNIF
puerta26.o_med_vel=-800
puerta26.o_med_displ=4000

puerta26.SetWhileOpenSound(maderadesliz1)
puerta26.SetEndOpenSound(maderagolpe1)

#2
puerta27=Doors.CreateDoor("Puerta27", (-31000,-7000,45500), (0,1,0), 600, 4600, Doors.CLOSED)

puerta27.opentype=Doors.UNIF
puerta27.o_med_vel=-800
puerta27.o_med_displ=4000

puerta27.SetWhileOpenSound(maderadesliz2)
puerta27.SetEndOpenSound(maderagolpe2)

#3
puerta28=Doors.CreateDoor("Puerta28", (-26125,-7000,40000), (0,1,0), 400, 3600, Doors.CLOSED)

puerta28.opentype=Doors.UNIF
puerta28.o_med_vel=-800
puerta28.o_med_displ=3200

puerta28.SetWhileOpenSound(maderadesliz3)
puerta28.SetEndOpenSound(maderagolpe3)

#4
puerta29=Doors.CreateDoor("Puerta29", (-26125,-7000,22000), (0,1,0), 400, 3600, Doors.CLOSED)

puerta29.opentype=Doors.UNIF
puerta29.o_med_vel=-800
puerta29.o_med_displ=3200

puerta29.SetWhileOpenSound(maderadesliz4)
puerta29.SetEndOpenSound(maderagolpe4)


#5
puerta30=Doors.CreateDoor("Puerta30", (-50000,-7000,22000), (0,1,0), 400, 3600, Doors.CLOSED)

puerta30.opentype=Doors.UNIF
puerta30.o_med_vel=-800
puerta30.o_med_displ=3200

puerta30.SetWhileOpenSound(maderadesliz5)
puerta30.SetEndOpenSound(maderagolpe5)

#6
puerta31=Doors.CreateDoor("Puerta31", (-50000,-7000,40000), (0,1,0), 400, 3600, Doors.CLOSED)

puerta31.opentype=Doors.UNIF
puerta31.o_med_vel=-800
puerta31.o_med_displ=3200

puerta31.SetWhileOpenSound(maderadesliz5)
puerta31.SetEndOpenSound(maderagolpe5)


############################################################
####---------------------------------------------------#####
####--------PUERTA----SALA--DETRAS--DEL--TRONO---------#####
############################################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta32=Doors.CreateDoor("Puerta32", (-38000,-7000,16700), (-1,0,0), 0, 3500, Doors.CLOSED)

puerta32.opentype=Doors.UNIF
puerta32.o_med_vel=-800
puerta32.o_med_displ=3500

puerta32.closetype=Doors.AC
puerta32.c_init_displ=3500
puerta32.c_med_vel=800


puerta32.SetWhileOpenSound(maderadesliz)
puerta32.SetEndOpenSound(maderagolpe)

puerta32.SetWhileCloseSound(maderadesliz)
puerta32.SetEndCloseSound(maderagolpe)

##### Accionar puertas al accionar una palanca


palan32=Levers.PlaceLever("PALAP32",Levers.LeverType2,(-35877.520028,-5819.527669,17083.289688),(0.707107,0.000000,-0.707107,-0.000000),1.0)

palan32.mode=2


palan32.OnTurnOnFunc=AbrePuertaTRO
palan32.OnTurnOnArgs=()

palan32.OnTurnOffFunc=CierraPuertaTRO
palan32.OnTurnOffArgs=()



############################################################
####---------------------------------------------------#####
####--------PUERTA--DEPOSITO--LLENO--DE--LICH----------#####
############################################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta33=Doors.CreateDoor("Puerta33", (-28000,5000,-37500), (0,1,0), 0, 3250, Doors.OPENED)

puerta33.opentype=Doors.UNIF
puerta33.o_med_vel=-1800
puerta33.o_med_displ=3250

puerta33.closetype=Doors.AC
puerta33.c_init_displ=3250
puerta33.c_med_vel=1800


puerta33.SetWhileOpenSound(maderadesliz)
puerta33.SetEndOpenSound(maderagolpe)

puerta33.SetWhileCloseSound(maderadesliz)
puerta33.SetEndCloseSound(maderagolpe)


####################	PUERTA DE REJA DEL GENERADOR


rast34=Bladex.CreateEntity("Rast34","Rastrillo",-46636.549576,5454.853643,-45878.704341)
rast34.Scale=0.685153
rast34.Orientation=0.500000,0.500000,-0.500000,0.500000

rast34din=Objects.CreateDinamicObject("Rast34")


############################################################
####---------------------------------------------------#####
####--------PUERTA--DEPOSITO--LLENO--DE--LICH----------#####
############################################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta35=Doors.CreateDoor("Puerta35", (-45500,-57000,37750), (0,1,0), 0, 3500, Doors.OPENED)

puerta35.opentype=Doors.UNIF
puerta35.o_med_vel=-1800
puerta35.o_med_displ=3500

puerta35.closetype=Doors.AC
puerta35.c_init_displ=3500
puerta35.c_med_vel=1800