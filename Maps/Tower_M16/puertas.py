import Doors
import Levers
import Locks
import Objects
import Sounds
import Sparks
import AuxFuncs
import darfuncs
import Stars
import Bladex




############################################################
#####---------------------------RASTRILLO--------SALON DE ARMAS--########################
############################################################

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

reja1=Bladex.CreateEntity("Reja1","Rastrillo",-21861.287165,-20088.447078,9148.222492)
reja1.Static=1
reja1.Scale=0.712973
reja1.Orientation=0.500000,0.500000,-0.500000,0.500000
Sparks.SetMetalSparkling("Reja1")

reja1din=Objects.CreateDinamicObject("Reja1")

###llave1 abrepuerta1###


cerradurp1=Locks.PlaceLock("cerradurp1","Cerraduracutre",(-22934.672654,-19294.869724,7375.371122),(0.0,0.0,0.707107,-0.707107),2.0)
cerradurp1.key="llave1"


cerradurp1.OnUnLockFunc=Abrereja1
cerradurp1.OnUnLockArgs=()

#cerradurp1.OnLockFunc=Cierrareja1
#cerradurp1.OnLockArgs=()

darfuncs.SetHint(cerradurp1.obj,"Armoury Lock")

o=Bladex.CreateEntity("llave1","Llavecutre",-35144.998049,-5023.708410,1653.921607,"Physic")
o.Scale=1.0
o.Orientation=0.002644,-0.727183,-0.017076,-0.686226
o.Data = 1
darfuncs.SetHint(o,"Armoury Key")
Stars.Twinkle("llave1")



#########
#########

########################################################################
###trampa de los orcos que salen para putear
########################################################################

spta1d=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
spta1d.MaxDistance=20000
spta1d.MinDistance=2000
spta1d.Volume=1.0


spta1g=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
spta1g.MaxDistance=20000
spta1g.MinDistance=2000
spta1g.Volume=1.0

#pta 1a
pta1a=Doors.CreateDoor("pta1a", (-18500,-7000,-13500), (0,1,0), 0, 4000, Doors.CLOSED)

pta1a.opentype=Doors.UNIF
pta1a.o_med_vel=-2000
pta1a.o_med_displ=4000

pta1a.closetype=Doors.UNIF
pta1a.c_med_vel=1000
pta1a.c_med_displ=4000

#pta 2a
pta2a=Doors.CreateDoor("pta2a", (-10900,-7000,-13500), (0,1,0), 0, 4000, Doors.CLOSED)

pta2a.opentype=Doors.UNIF
pta2a.o_med_vel=-2000
pta2a.o_med_displ=4000

pta2a.closetype=Doors.UNIF
pta2a.c_med_vel=2000
pta2a.c_med_displ=4000

#pta 3a
pta3a=Doors.CreateDoor("pta3a", (-3400,-7000,-13500), (0,1,0), 0, 4000, Doors.CLOSED)

pta3a.opentype=Doors.UNIF
pta3a.o_med_vel=-2000
pta3a.o_med_displ=4000

pta3a.closetype=Doors.UNIF
pta3a.c_med_vel=1000
pta3a.c_med_displ=4000

#pta 4a
pta4a=Doors.CreateDoor("pta4a", (-10900,-8000,-1625), (0,1,0), 0, 4000, Doors.CLOSED)
pta4a.Squezze = 1

pta4a.opentype=Doors.UNIF
pta4a.o_med_vel=-2000
pta4a.o_med_displ=4000

pta4a.closetype=Doors.UNIF
pta4a.c_med_vel=8000
pta4a.c_med_displ=4000

#funci�n que sube y baja las puertas al unisono

pta1a.SetWhileOpenSound(spta1d)
pta1a.SetEndOpenSound(spta1g)

pta1a.SetWhileCloseSound(spta1d)
pta1a.SetEndCloseSound(spta1g)

#pta 1B
spta1b=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
spta1b.MaxDistance=20000
spta1b.MinDistance=2000
spta1b.Volume=1.0


spta1bg=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
spta1bg.MaxDistance=20000
spta1bg.MinDistance=2000
spta1bg.Volume=1.0


pta1B=Doors.CreateDoor("pta1B", (400,-7000,-8500), (0,1,0), 500, 4500, Doors.OPENED)
pta1B.Squezze = 1


pta1B.opentype=Doors.UNIF
pta1B.o_med_vel=-3000
pta1B.o_med_displ=4000

pta1B.closetype=Doors.UNIF
pta1B.c_med_vel=5000
pta1B.c_med_displ=4000

pta1B.SetWhileOpenSound(spta1b)
pta1B.SetEndOpenSound(spta1bg)

pta1B.SetWhileCloseSound(spta1b)
pta1B.SetEndCloseSound(spta1bg)

############################################################
####### PUERTA QUE SE ABRE AL MORIR EL PRIMER GOLEM  #######

spuerta1d=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
spuerta1d.MaxDistance=20000
spuerta1d.MinDistance=4000
spuerta1d.Volume=1.0

spuerta1g=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
spuerta1g.MaxDistance=20000
spuerta1g.MinDistance=4000
spuerta1g.Volume=1.0

puerta1=Doors.CreateDoor("Puerta1", (-3000,-8000,20300), (0,1,0), 500, 4000, Doors.CLOSED)


puerta1.opentype=Doors.UNIF
puerta1.o_med_vel=-500
puerta1.o_med_displ=3500


puerta1.closetype=Doors.AC
puerta1.c_init_displ=3500
puerta1.c_med_vel=8000


puerta1.SetWhileOpenSound(spuerta1d)
puerta1.SetEndOpenSound(spuerta1g)

puerta1.SetWhileCloseSound(spuerta1d)
puerta1.SetEndCloseSound(spuerta1g)



#######################################################################
####### PUERTA QUE SE ABRE AL MORIR EL GRAN DEMONIO MESKALANDUG #######

spuerta2d=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
spuerta2d.MaxDistance=30000
spuerta2d.MinDistance=4000
spuerta2d.Volume=1.0

spuerta2g=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
spuerta2g.MaxDistance=30000
spuerta2g.MinDistance=4000
spuerta2g.Volume=1.0

puerta2=Doors.CreateDoor("Puerta2", (5200,-93000,9000), (0,1,0), 1000, 5000, Doors.OPENED)
puerta2.Squezze = 1

puerta2.opentype=Doors.UNIF
puerta2.o_med_vel=-500
puerta2.o_med_displ=4000


puerta2.closetype=Doors.AC
puerta2.c_init_displ=4000
puerta2.c_med_vel=8000


puerta2.SetWhileOpenSound(spuerta2d)
puerta2.SetEndOpenSound(spuerta2g)

puerta2.SetWhileCloseSound(spuerta2d)
puerta2.SetEndCloseSound(spuerta2g)

#########################################################################
####### PUERTA QUE ABRE EL CAMINO DE LA ENTRADA SECRETA		  #######

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta3=Doors.CreateDoor("Puerta3", (-22530,-7000,-9000), (0,1,0), 250, 4250, Doors.CLOSED)
puerta3.Squezze = 1

puerta3.opentype=Doors.UNIF
puerta3.o_med_vel=-3500
puerta3.o_med_displ=4000


puerta3.closetype=Doors.AC
puerta3.c_init_displ=4000
puerta3.c_med_vel=8000


puerta3.SetWhileOpenSound(maderadesliz)
puerta3.SetEndOpenSound(maderagolpe)

puerta3.SetWhileCloseSound(maderadesliz)
puerta3.SetEndCloseSound(maderagolpe)

##### Accionar puertas al accionar una palanca


palan3=Levers.PlaceLever("PALAP3",Levers.LeverType3,(-23553.036989,-5725.015027,-11539.557722),(0.50,0.50,0.50,-0.50),1.0)

palan3.mode=1

palan3.OnTurnOnFunc=AbrePuerta3
palan3.OnTurnOnArgs=()

palan3.OnTurnOffFunc=CierraPuerta3
palan3.OnTurnOffArgs=()


###################################################################
####### PUERTA QUE SE ABRE AL MORIR EL esqueleto en llamas  #######
"""
spuerta4d=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
spuerta4d.MaxDistance=30000
spuerta4d.MinDistance=2000
spuerta4d.Volume=1.0

spuerta4g=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
spuerta4g.MaxDistance=30000
spuerta4g.MinDistance=2000
spuerta4g.Volume=1.0


puerta4=Doors.CreateDoor("Puerta4", (-15900,-48000,-8000), (0,1,0), 750, 4750, Doors.CLOSED)


puerta4.opentype=Doors.UNIF
puerta4.o_med_vel=-500
puerta4.o_med_displ=4000


puerta4.closetype=Doors.AC
puerta4.c_init_displ=4000
puerta4.c_med_vel=8000


puerta4.SetWhileOpenSound(spuerta4d)
puerta4.SetEndOpenSound(spuerta4g)

puerta4.SetWhileCloseSound(spuerta4d)
puerta4.SetEndCloseSound(spuerta4g)

def AbrePuerta4():
	puerta4.OpenDoor()

def CierraPuerta4():
	puerta4.CloseDoor()

"""
#####################################################
####### PUERTAS DE LA SALA DE LOS DOS GOLEMS  #######
#####################################################

###Puerta de entrada
spuerta5d=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
spuerta5d.MaxDistance=30000
spuerta5d.MinDistance=3000
spuerta5d.Volume=0.7

spuerta5g=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
spuerta5g.MaxDistance=30000
spuerta5g.MinDistance=3000
spuerta5g.Volume=0.7


puerta5=Doors.CreateDoor("Puerta5", (0,-28000,9500), (0,1,0), 750, 4750, Doors.OPENED)
puerta5.Squezze = 1


puerta5.opentype=Doors.UNIF
puerta5.o_med_vel=-500
puerta5.o_med_displ=4000

puerta5.closetype=Doors.AC
puerta5.c_init_displ=4000
puerta5.c_med_vel=8000

puerta5.SetWhileOpenSound(spuerta5d)
puerta5.SetEndOpenSound(spuerta5g)

puerta5.SetWhileCloseSound(spuerta5d)
puerta5.SetEndCloseSound(spuerta5g)


###Puerta de salida
spuerta6d=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
spuerta6d.MaxDistance=30000
spuerta6d.MinDistance=4000
spuerta6d.Volume=1.0

spuerta6g=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
spuerta6g.MaxDistance=30000
spuerta6g.MinDistance=4000
spuerta6g.Volume=1.0


puerta6=Doors.CreateDoor("Puerta6", (-11000,-28000,-1500), (0,1,0), 750, 4750, Doors.CLOSED)


puerta6.opentype=Doors.UNIF
puerta6.o_med_vel=-500
puerta6.o_med_displ=4000


puerta6.closetype=Doors.AC
puerta6.c_init_displ=4000
puerta6.c_med_vel=8000


puerta6.SetWhileOpenSound(spuerta6d)
puerta6.SetEndOpenSound(spuerta6g)

puerta6.SetWhileCloseSound(spuerta6d)
puerta6.SetEndCloseSound(spuerta6g)

#######################################################################
####### PUERTA QUE ABRE EL CAMINO DE LA ESCALERA DE CARACOLLLL  #######

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta7=Doors.CreateDoor("Puerta7", (59250,17000,6250), (0,1,0), 0, 3800, Doors.CLOSED)
puerta7.Squezze = 1

puerta7.opentype=Doors.UNIF
puerta7.o_med_vel=-1000
puerta7.o_med_displ=3800


puerta7.closetype=Doors.AC
puerta7.c_init_displ=3800
puerta7.c_med_vel=8000


puerta7.SetWhileOpenSound(maderadesliz)
puerta7.SetEndOpenSound(maderagolpe)

puerta7.SetWhileCloseSound(maderadesliz)
puerta7.SetEndCloseSound(maderagolpe)

##### Accionar puertas al accionar una palanca


palan7=Levers.PlaceLever("PALAP7",Levers.LeverType3,(61173.631059,18158.496068,9705.850983),(0.707107,0.707107,0.000000,0.000000),1.0)

palan7.mode=1


palan7.OnTurnOnFunc=AbrePuerta7
palan7.OnTurnOnArgs=()

palan7.OnTurnOffFunc=CierraPuerta7
palan7.OnTurnOffArgs=()


#######################################################################
#######         PUERTA SALA DEL FINAL CON DAL-GURAK             #######

Bladex.AddParticleGType("DustDoor","SmokeParticle",B_PARTICLE_GTYPE_BLEND,128)

for i in range(128):
	if i>64:
		traux=0.0
	else:
		traux=(64.0-i)/64.0
	aux=(64.0-i)/64.0
	r=90
	g=70
	b=75
	a=255.0*(1.0-traux)**0.5
	size=10.0+aux*1700.0
	Bladex.SetParticleGVal("DustDoor",i,r,g,b,a,size)


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta9=Doors.CreateDoor("Puerta9", (-9000,-115500,9000), (0,1,0), 1000, 5500, Doors.OPENED)


puerta9.opentype=Doors.UNIF
puerta9.o_med_vel=-500
puerta9.o_med_displ=4500


puerta9.closetype=Doors.AC
puerta9.c_init_displ=4500
puerta9.c_med_vel=8000
puerta9.OnEndCloseFunc=LineaPolvo


puerta9.SetWhileOpenSound(maderadesliz)
puerta9.SetEndOpenSound(maderagolpe)

puerta9.SetWhileCloseSound(maderadesliz)
puerta9.SetEndCloseSound(maderagolpe)


###	PUERTAS ZONA PUENTE

###1	a las escaleras
maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta10=Doors.CreateDoor("Puerta10", (86500,-3000,16500), (0,1,0), 500, 5000, Doors.OPENED)
puerta10.Squezze = 1

puerta10.opentype=Doors.UNIF
puerta10.o_med_vel=-1800
puerta10.o_med_displ=4500

puerta10.closetype=Doors.AC
puerta10.c_init_displ=4500
puerta10.c_med_vel=8000

puerta10.SetWhileOpenSound(maderadesliz)
puerta10.SetEndOpenSound(maderagolpe)

puerta10.SetWhileCloseSound(maderadesliz)
puerta10.SetEndCloseSound(maderagolpe)


###1	la del puente
maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta11=Doors.CreateDoor("Puerta11", (58300,-4000,24000), (0,1,0), 1000, 5250, Doors.OPENED)
puerta11.Squezze = 1

puerta11.opentype=Doors.UNIF
puerta11.o_med_vel=-1800
puerta11.o_med_displ=4250

puerta11.closetype=Doors.AC
puerta11.c_init_displ=4250
puerta11.c_med_vel=5000

puerta11.SetWhileOpenSound(maderadesliz)
puerta11.SetEndOpenSound(maderagolpe)



##### Accionar puertas al accionar una palanca


palan11=Levers.PlaceLever("PALAP11",Levers.LeverType3,(60936.416188,-5068.777100,18462.109237),(0.270598,0.270598,-0.653282,0.653282),1.0)
palan11.mode=1

palan11.OnTurnOnFunc=AbrePuerta11
palan11.OnTurnOnArgs=()

palan11.OnTurnOffFunc=CierraPuerta11
palan11.OnTurnOffArgs=()


darfuncs. EnterSecEvent(52662.9, -1195.4, 24248.5,CierraPuerta11)

##########################################################################
###
###	PUERTAS ZONA A OSCURAS
###
##########################################################################

###0
maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


ptasector0=Doors.CreateDoor("ptasector0", (-29500,-34000,19500), (0,1,0), 0, 3750, Doors.OPENED)
ptasector0.Squezze = 1

ptasector0.opentype=Doors.UNIF
ptasector0.o_med_vel=-1800
ptasector0.o_med_displ=3750

ptasector0.closetype=Doors.AC
ptasector0.c_init_displ=3750
ptasector0.c_med_vel=5000

ptasector0.SetWhileOpenSound(maderadesliz)
ptasector0.SetEndOpenSound(maderagolpe)

ptasector0.SetWhileCloseSound(maderadesliz)
ptasector0.SetEndCloseSound(maderagolpe)

###00
maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


ptasector00=Doors.CreateDoor("ptasector00", (-25000,-34000,19500), (0,1,0), 0, 3750, Doors.OPENED)
ptasector00.Squezze = 1

ptasector00.opentype=Doors.UNIF
ptasector00.o_med_vel=-1800
ptasector00.o_med_displ=3750

ptasector00.closetype=Doors.AC
ptasector00.c_init_displ=3750
ptasector00.c_med_vel=5000

ptasector00.SetWhileOpenSound(maderadesliz)
ptasector00.SetEndOpenSound(maderagolpe)

ptasector00.SetWhileCloseSound(maderadesliz)
ptasector00.SetEndCloseSound(maderagolpe)


###1
maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


ptasector1=Doors.CreateDoor("ptasector1", (-13500,-34000,22000), (0,0,-1), 0, 3000, Doors.OPENED)
ptasector1.Squezze = 1

ptasector1.opentype=Doors.UNIF
ptasector1.o_med_vel=-1800
ptasector1.o_med_displ=3000

ptasector1.closetype=Doors.AC
ptasector1.c_init_displ=3000
ptasector1.c_med_vel=5000

ptasector1.SetWhileOpenSound(maderadesliz)
ptasector1.SetEndOpenSound(maderagolpe)

ptasector1.SetWhileCloseSound(maderadesliz)
ptasector1.SetEndCloseSound(maderagolpe)


###2
maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


ptasector2=Doors.CreateDoor("ptasector2", (-6500,-33000,27000), (0,0,1), 0, 3000, Doors.OPENED)
ptasector2.Squezze = 1

ptasector2.opentype=Doors.UNIF
ptasector2.o_med_vel=-1800
ptasector2.o_med_displ=3000

ptasector2.closetype=Doors.AC
ptasector2.c_init_displ=3000
ptasector2.c_med_vel=5000

ptasector2.SetWhileOpenSound(maderadesliz)
ptasector2.SetEndOpenSound(maderagolpe)

ptasector2.SetWhileCloseSound(maderadesliz)
ptasector2.SetEndCloseSound(maderagolpe)


###3
maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


ptasector3=Doors.CreateDoor("ptasector3", (-500,-34000,22000), (0,0,-1), 0, 3500, Doors.OPENED)
ptasector3.Squezze = 1

ptasector3.opentype=Doors.UNIF
ptasector3.o_med_vel=-1800
ptasector3.o_med_displ=3500

ptasector3.closetype=Doors.AC
ptasector3.c_init_displ=3500
ptasector3.c_med_vel=5000

ptasector3.SetWhileOpenSound(maderadesliz)
ptasector3.SetEndOpenSound(maderagolpe)

ptasector3.SetWhileCloseSound(maderadesliz)
ptasector3.SetEndCloseSound(maderagolpe)


###4
maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


ptasector4=Doors.CreateDoor("ptasector4", (7000,-34000,19000), (1,0,0), 0, 3000, Doors.OPENED)
ptasector4.Squezze = 1

ptasector4.opentype=Doors.UNIF
ptasector4.o_med_vel=-1800
ptasector4.o_med_displ=3000

ptasector4.closetype=Doors.AC
ptasector4.c_init_displ=3000
ptasector4.c_med_vel=5000

ptasector4.SetWhileOpenSound(maderadesliz)
ptasector4.SetEndOpenSound(maderagolpe)

ptasector4.SetWhileCloseSound(maderadesliz)
ptasector4.SetEndCloseSound(maderagolpe)


###5
maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


ptasector5=Doors.CreateDoor("ptasector5", (7000,-39000,-2000), (0,1,0), 750, 5750, Doors.CLOSED)
ptasector5.Squezze = 1

ptasector5.opentype=Doors.UNIF
ptasector5.o_med_vel=-1800
ptasector5.o_med_displ=5000

ptasector5.closetype=Doors.AC
ptasector5.c_init_displ=5000
ptasector5.c_med_vel=5000

ptasector5.SetWhileOpenSound(maderadesliz)
ptasector5.SetEndOpenSound(maderagolpe)

ptasector5.SetWhileCloseSound(maderadesliz)
ptasector5.SetEndCloseSound(maderagolpe)

######################################
###PUERTA DE LA SALA A OSCURAS
###
######################################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta12=Doors.CreateDoor("puerta12", (-2500,-40000,-6000), (0,1,0), 500, 5500, Doors.CLOSED)
puerta12.Squezze = 1

puerta12.opentype=Doors.UNIF
puerta12.o_med_vel=-1800
puerta12.o_med_displ=5000

puerta12.closetype=Doors.AC
puerta12.c_init_displ=5000
puerta12.c_med_vel=5000

puerta12.SetWhileOpenSound(maderadesliz)
puerta12.SetEndOpenSound(maderagolpe)

puerta12.SetWhileCloseSound(maderadesliz)
puerta12.SetEndCloseSound(maderagolpe)



######################################
###
###PUERTA DE LA SALA DEL GOLEM DE LAVA
###
######################################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta13=Doors.CreateDoor("puerta13", (-500,-51000,9000), (0,1,0), 500, 5500, Doors.OPENED)
puerta13.Squezze = 1

puerta13.opentype=Doors.UNIF
puerta13.o_med_vel=-1800
puerta13.o_med_displ=5000

puerta13.closetype=Doors.AC
puerta13.c_init_displ=5000
puerta13.c_med_vel=9000

puerta13.SetWhileOpenSound(maderadesliz)
puerta13.SetEndOpenSound(maderagolpe)

puerta13.SetWhileCloseSound(maderadesliz)
puerta13.SetEndCloseSound(maderagolpe)


######################################
###
###PUERTA DEL GOLEM DE LAVA
###
######################################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta14=Doors.CreateDoor("puerta14", (-21000,-51000,9000), (0,1,0), 0, 5000, Doors.CLOSED)
puerta14.Squezze = 1

puerta14.opentype=Doors.UNIF
puerta14.o_med_vel=-1800
puerta14.o_med_displ=5000

puerta14.closetype=Doors.AC
puerta14.c_init_displ=5000
puerta14.c_med_vel=5000

puerta14.SetWhileOpenSound(maderadesliz)
puerta14.SetEndOpenSound(maderagolpe)

puerta14.SetWhileCloseSound(maderadesliz)
puerta14.SetEndCloseSound(maderagolpe)


######################################
###
###PUERTA DE LAS PASARELAS DE LAVA
###
######################################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta15=Doors.CreateDoor("puerta15", (4500,-59000,-1700), (0,1,0), 0, 5000, Doors.CLOSED)
puerta15.Squezze = 1

puerta15.opentype=Doors.UNIF
puerta15.o_med_vel=-1800
puerta15.o_med_displ=5000

puerta15.closetype=Doors.AC
puerta15.c_init_displ=5000
puerta15.c_med_vel=5000

puerta15.SetWhileOpenSound(maderadesliz)
puerta15.SetEndOpenSound(maderagolpe)

puerta15.SetWhileCloseSound(maderadesliz)
puerta15.SetEndCloseSound(maderagolpe)


######################################
###
###PUERTA DEL PASO DE TREPAR
###
######################################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta16=Doors.CreateDoor("puerta16", (4500,-58000,19400), (0,1,0), 0, 4500, Doors.CLOSED)
puerta16.Squezze = 1

puerta16.opentype=Doors.UNIF
puerta16.o_med_vel=-1800
puerta16.o_med_displ=4500

puerta16.closetype=Doors.AC
puerta16.c_init_displ=4500
puerta16.c_med_vel=5000

puerta16.SetWhileOpenSound(maderadesliz)
puerta16.SetEndOpenSound(maderagolpe)

puerta16.SetWhileCloseSound(maderadesliz)
puerta16.SetEndCloseSound(maderagolpe)


######################################
###
###PUERTA DEL arquero del puente
###
######################################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta17=Doors.CreateDoor("puerta17", (71125,-2500,17750), (0,1,0), 500, 4000, Doors.CLOSED)
puerta17.Squezze = 1

puerta17.opentype=Doors.UNIF
puerta17.o_med_vel=-1800
puerta17.o_med_displ=3500

puerta17.closetype=Doors.AC
puerta17.c_init_displ=3500
puerta17.c_med_vel=5000

puerta17.SetWhileOpenSound(maderadesliz)
puerta17.SetEndOpenSound(maderagolpe)

puerta17.SetWhileCloseSound(maderadesliz)
puerta17.SetEndCloseSound(maderagolpe)


######################################
###
###PUERTA DEL segundo piso de la torre
###
######################################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta18=Doors.CreateDoor("puerta18", (0,-15000,-6000), (0,0,-1),0, 3500, Doors.CLOSED)
puerta18.Squezze = 1

puerta18.opentype=Doors.UNIF
puerta18.o_med_vel=-1800
puerta18.o_med_displ=3500

puerta18.closetype=Doors.AC
puerta18.c_init_displ=3500
puerta18.c_med_vel=5000

puerta18.SetWhileOpenSound(maderadesliz)
puerta18.SetEndOpenSound(maderagolpe)

puerta18.SetWhileCloseSound(maderadesliz)
puerta18.SetEndCloseSound(maderagolpe)
