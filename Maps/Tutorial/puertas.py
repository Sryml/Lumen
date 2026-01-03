
import Doors
import Levers
import Locks
import Objects
import Sounds
import Button
import darfuncs
import Stars


sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

rejasi=Bladex.CreateEntity("Rejasi1","Rastrillo2",267745.124107,-2160.644748,126189.465221)
rejasi.Static=1
rejasi.Scale=1.416603
rejasi.Orientation=0.500000,0.500000,0.500000,-0.500000
Sparks.SetSparkling("Rejasi1")

rejasi1din=Objects.CreateDinamicObject("Rejasi1")

rejasi=Bladex.CreateEntity("Rejasi2","Rastrillo2",267755.124107,-2160.644748,128589.465221)
rejasi.Static=1
rejasi.Scale=1.416603
rejasi.Orientation=0.500000,0.500000,0.500000,-0.500000
Sparks.SetSparkling("Rejasi2")

rejasi2din=Objects.CreateDinamicObject("Rejasi2")

##funciones abrir-cerrar##

def Abrerejasi1():

	desplazamientos=(2000.0, 1010.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto reja1din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rejasi1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Abrerejasi2():

	desplazamientos=(2000.0, 1010.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto reja1din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rejasi2din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Abrerejas():
	Abrerejasi1()
	Abrerejasi2()

def Cierrarejasi1():

	desplazamientos=(2000.0, 1010.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)

	#sonidos asociados a la puerta-objeto rejasi1din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(rejasi1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Cierrarejasi2():

	desplazamientos=(2000.0, 1010.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)

	#sonidos asociados a la puerta-objeto rejasi1din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(rejasi2din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Cierrarejas():
	Cierrarejasi1()
	Cierrarejasi2()

ladosCerrados=0
def Cierralados():
	global ladosCerrados
	if (ladosCerrados==0) :
		Cierrarejasi1()
		Cierrarejasi2()
		ladosCerrados=1






########################################

##### Puerta de la cocina #####


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta2=Doors.CreateDoor("Puerta2", (325500,-7000,105000), (0,1,0), 1250, 5000, Doors.CLOSED)
puerta2.Squezze = 1

puerta2.opentype=Doors.UNIF
puerta2.o_med_vel=-800
puerta2.o_med_displ=3750


puerta2.closetype=Doors.AC
puerta2.c_init_displ=3750
puerta2.c_med_vel=8000


puerta2.SetWhileOpenSound(maderadesliz)
puerta2.SetEndOpenSound(maderagolpe)

puerta2.SetWhileCloseSound(maderadesliz)
puerta2.SetEndCloseSound(maderagolpe)

###llave2 abrepuerta de la cocina###


cerradurp2=Locks.PlaceLock("cerradurp2","Cerraduracutre",(321799.109927,-6027.134912,108215.095530),(0.707107,0.707107,0.000000,0.000000),3.0)

def AbrePuertaLlave2():
	puerta2.OpenDoor()

def CierraPuertaLlave2():
	puerta2.CloseDoor()

cerradurp2.OnUnLockFunc=AbrePuertaLlave2
cerradurp2.OnUnLockArgs=()

cerradurp2.OnLockFunc=CierraPuertaLlave2
cerradurp2.OnLockArgs=()
cerradurp2.key = None

darfuncs.SetHint(cerradurp2.obj,"Iron Lock")






############
############################
############entrada de la puerta de madera#######
#################
#######################

#escalon 1a
puertasub1=Doors.CreateDoor("Puertasub1", (288500,0,128000), (0,1,0), 1000, 6000, Doors.CLOSED)

puertasub1.opentype=Doors.UNIF
puertasub1.o_med_vel=-500
puertasub1.o_med_displ=5000

puertasub1.closetype=Doors.UNIF
puertasub1.c_med_vel=4000
puertasub1.c_med_displ=5000

puertasub1.SetWhileOpenSound(maderadesliz)
puertasub1.SetEndOpenSound(maderagolpe)

puertasub1.SetWhileCloseSound(maderadesliz)
puertasub1.SetEndCloseSound(maderagolpe)


def Abresub():
	global LAST_ACTION
	LAST_ACTION = "burn"

	Bladex.GetEntity("blosu1").SelfIlum = 0
	Bladex.GetEntity("blosu2").SelfIlum = 0
	TutorialScorer.ShowBC("Exelent",0)

	Bladex.AddScheduledFunc(Bladex.GetTime() + 3, puertasub1.OpenDoor, ())


o=Bladex.CreateEntity("blosu1","Bloque",286481.384055,-287.546265,123334.955606)
o.Static=0
o.Scale=1.000000
o.Orientation=0.504344,0.504344,0.495618,-0.495618
darfuncs.SetHint(Bladex.GetEntity("blosu1"),"Trigger")


o=Bladex.CreateEntity("blosu2","Bloque",286501.812864,-274.852997,131775.106847)
o.Static=0
o.Scale=1.000000
o.Orientation=0.500000,0.500000,0.500000,-0.500000
darfuncs.SetHint(Bladex.GetEntity("blosu2"),"Trigger")


button=Button.CreateButtonCombination(0,Abresub,"")
button.AddButton("blosu1",2,(0,0,-1),500,0,0,1)
button.AddButton("blosu2",2,(0,0,1),500,0,0,1)
#####




#####
##### Puerta despues de la caja que se quema #####

puerta1=Doors.CreateDoor("Puerta1", (311000,0,127000), (0,1,0), 1250, 5550, Doors.CLOSED)
puerta1.Squezze = 1

puerta1.opentype=Doors.UNIF
puerta1.o_med_vel=-500
puerta1.o_med_displ=4300


puerta1.closetype=Doors.AC
puerta1.c_init_displ=4300
puerta1.c_med_vel=16000


puerta1.SetWhileOpenSound(maderadesliz)
puerta1.SetEndOpenSound(maderagolpe)

puerta1.SetWhileCloseSound(maderadesliz)
puerta1.SetEndCloseSound(maderagolpe)

##### Accionar puertas al accionar una palanca

palancap1=Levers.PlaceLever("PalancaP1",Levers.LeverType3,(306965.427987,-346.662523,123792.994783),(0.006171,0.006171,-0.707080,0.707080),1.0)

palancap1.mode=1


def AbrePuerta1():
	puerta1.OpenDoor()


def CierraPuerta1():
	puerta1.CloseDoor()


palancap1.OnTurnOnFunc=AbrePuerta1
palancap1.OnTurnOnArgs=()

palancap1.OnTurnOffFunc=CierraPuerta1
palancap1.OnTurnOffArgs=()

##########################################
##### Puerta antes del caballero1 que escucha y explora #####

puerta11=Doors.CreateDoor("Puerta11", (330250,0,85875), (0,1,0), 550, 4550, Doors.OPENED)
puerta11.Squezze = 1

puerta11.opentype=Doors.UNIF
puerta11.o_med_vel=-6000
puerta11.o_med_displ=4000

puerta11.closetype=Doors.AC
puerta11.c_init_displ=4000
puerta11.c_med_vel=16000

puerta11.SetWhileCloseSound(maderadesliz)
puerta11.SetEndCloseSound(maderagolpe)


###########################
###########################
#####
##### Puerta despues del caballero que explora. Se abre con palanca y se cierra sola #####

puerta121=Doors.CreateDoor("Puerta121", (346500,0,86750), (0,1,0), 0, 4500, Doors.CLOSED)
puerta121.Squezze = 1

puerta121.opentype=Doors.UNIF
puerta121.o_med_vel=-500
puerta121.o_med_displ=4500

puerta121.closetype=Doors.AC
puerta121.c_init_displ=4500
puerta121.c_med_vel=16000

puerta121.SetWhileOpenSound(maderadesliz)
puerta121.SetEndOpenSound(maderagolpe)
puerta121.SetWhileCloseSound(maderadesliz)
puerta121.SetEndCloseSound(maderagolpe)

def CierraPuerta121(sectorindex,entityname):
	if entityname == "Player1":
		puerta121.CloseDoor()
		se121=Bladex.GetSector(354000,0,86000)
		se121.OnEnter=""


se121=Bladex.GetSector(354000,0,86000)
se121.OnEnter=CierraPuerta121


########## se cierra sola despues del caballero que se despista con sigilo.
################################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")


puertasig=Doors.CreateDoor("Puertasig", (355000,0,57125), (0,1,0), 0, 4750, Doors.OPENED)
puertasig.Squezze = 1



puertasig.closetype=Doors.AC
puertasig.c_init_displ=4750
puertasig.c_med_vel=8000


puertasig.SetWhileCloseSound(maderadesliz)
puertasig.SetEndCloseSound(maderagolpe)

def CierraPuertasig(sectorindex,entityname):
	if entityname == "Player1":
		puertasig.CloseDoor()
		sensig=Bladex.GetSector(354761.391515, -376.440863578, 53990.796)
		sensig.OnEnter=""


sensig=Bladex.GetSector(354761.391515, -376.440863578, 53990.796)
sensig.OnEnter=CierraPuertasig

#############
#############
############# RASTRILLO DE LOS TIOS QUE PATRULLAN

#######################################


sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")


RASS1=Bladex.CreateEntity("RASS1","Rastrillo2",411869.570755,-2329.543454,44544.699098)
RASS1.Static=1
RASS1.Scale=1.474123
RASS1.Orientation=0.504344,0.504344,0.495618,-0.495618
Sparks.SetSparkling("RASS1")

puertaRASS1din=Objects.CreateDinamicObject("RASS1")

##funciones abrir-cerrar##

def AbreRASS1():

	desplazamientos=(1750.0, 1750.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto puerta1
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(puertaRASS1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


def CierraRASS1(sectorindex,entityname):

	if entityname=='Player1':

		desplazamientos=(1750.0, 1750.0, 700.0, 700.0, 250.0, 250.0)
		vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
		vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
		vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)

		#sonidos asociados a la puerta-objeto rastfin
		son_iniciales=("", "", "", "", "", "")
		son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
		son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
		Objects.NDisplaceObject(puertaRASS1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
		s1.OnEnter=""

s1=Bladex.GetSector(415417.089555, -341.343872917, 42378.4290)
s1.OnEnter=CierraRASS1




###cerradura rastrillos###

##cerradura ##

cerraduraRASS1=Locks.PlaceLock("cerraduraRASS1","Cerraduracutre",(409055.192000,-233.627000,41522.598000),(0.508650,0.508650,-0.491198,0.491198),3.0)
cerraduraRASS1.key="llaveRASS1"


cerraduraRASS1.OnUnLockFunc=AbreRASS1
cerraduraRASS1.OnUnLockArgs=()


darfuncs.SetHint(cerraduraRASS1.obj,"Ruins Lock")

##Llave 1##
#
#o=Bladex.CreateEntity("llaveRASS1","Llavecutre",381403.204000,184.258000,44895.929000)
#o.Static=0
#o.Scale=1.0
#o.Orientation=0.998472,0.033209,-0.044139,-0.001303
#darfuncs.SetHint(o,"Ruins Key")


Bladex.GetSector(426336.174123, 4725.36069508, 71128.5809957).Active = 0

##################
########## FINAL,SE CIERRA SOLA.
################################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")


puertaen=Doors.CreateDoor("Puertaen", (455000,3000,45500), (0,1,0), 0, 9500, Doors.OPENED)
puertaen.Squezze = 1

puertaen.opentype=Doors.UNIF
puertaen.o_med_vel=-5000
puertaen.o_med_displ=9500

puertaen.closetype=Doors.AC
puertaen.c_init_displ=9500
puertaen.c_med_vel=8000


puertaen.SetWhileCloseSound(maderadesliz)
puertaen.SetEndCloseSound(maderagolpe)

def AbrePuertaen():
	puertaen.OpenDoor()

def CierraPuertaLlaveen(sectorindex,entityname):
	if entityname == "Player1":
		puertaen.CloseDoor()
		sen=Bladex.GetSector(465000,0,45550)
		sen.OnEnter=""


sen=Bladex.GetSector(465000,0,45550)
sen.OnEnter=CierraPuertaLlaveen





############################
##### Puerta del patio #####
############################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta222=Doors.CreateDoor("Puerta222", (482000,8000,51500), (0,0,1), 0, 4500, Doors.CLOSED)
puerta222.Squezze = 1

puerta222.opentype=Doors.UNIF
puerta222.o_med_vel=-800
puerta222.o_med_displ=4500



puerta222.SetWhileOpenSound(maderadesliz)
puerta222.SetEndOpenSound(maderagolpe)



###llave222 abrepuerta de la sala final del arco###


cerradurp222=Locks.PlaceLock("cerradurp222","Cerraduracutre",(480988.814588,9159.791805,54400.385198),(0.006171,0.006171,-0.707080,0.707080),3.0)
cerradurp222.key="Llavep222"

def AbrePuertaLlave222():
	puerta222.OpenDoor()



cerradurp222.OnUnLockFunc=AbrePuertaLlave222
cerradurp222.OnUnLockArgs=()


darfuncs.SetHint(cerradurp222.obj,"Courtyard Lock")


#llavep222=Bladex.CreateEntity("Llavep222","Llavecutre",479831.770376,9271.125219,54327.696790)
#llavep222.Static=0
#llavep222.Scale=1.05
#llavep222.Orientation=0.998865,-0.001117,-0.047581,-0.002111
#darfuncs.SetHint(llavep222,"Courtyard Key")





##################
########## FINAL,SE abre al matar a los enemigos.
################################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")


puertafinen=Doors.CreateDoor("Puertafinen", (468000,8000,30500), (1,0,0), 0, 7500, Doors.CLOSED)
puertafinen.Squezze = 1

puertafinen.opentype=Doors.UNIF
puertafinen.o_med_vel=-800
puertafinen.o_med_displ=7500

puertafinen.SetWhileOpenSound(maderadesliz)
puertafinen.SetEndOpenSound(maderagolpe)

def AbrePuertaLlavefinen():
	puertafinen.OpenDoor()







################################ PUERTA DEL PELELE


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")


puertaPELE=Doors.CreateDoor("puertaPELE", (445000,4000,45000), (0,0,1), 0, 7500, Doors.CLOSED)
puertaPELE.Squezze = 1

puertaPELE.opentype=Doors.UNIF
puertaPELE.o_med_vel=-800
puertaPELE.o_med_displ=7500

puertaPELE.SetWhileOpenSound(maderadesliz)
puertaPELE.SetEndOpenSound(maderagolpe)

def AbrePuertaPELE():
	puertaPELE.OpenDoor()