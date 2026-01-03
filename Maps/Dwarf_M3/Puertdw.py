import Doors
import Levers
import Locks
import Objects
import Sounds
import Sparks
import Button
import ReadGSFile
import AuxFuncs
import darfuncs
import Stars

#-PUERTA-LLAVE-1


maderadesliz1=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderadesliz1.MaxDistance=25000
maderadesliz1.MinDistance=2000
maderadesliz1.Volume=1.0

maderagolpe1=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
maderagolpe1.MaxDistance=25000
maderagolpe1.MinDistance=2000
maderagolpe1.Volume=1.0


puerta1=Doors.CreateDoor("Puerta1", (2560,-2750,-41930), (0,1,0), 500, 5000, Doors.CLOSED)


puerta1.opentype=Doors.UNIF
puerta1.o_med_vel=-500
puerta1.o_med_displ=4500


puerta1.closetype=Doors.AC
puerta1.c_init_displ=4500
puerta1.c_med_vel=8000


puerta1.SetWhileOpenSound(maderadesliz1)
puerta1.SetEndOpenSound(maderagolpe1)

puerta1.SetWhileCloseSound(maderadesliz1)
puerta1.SetEndCloseSound(maderagolpe1)

###llave1 abrepuerta1###


cerradurp1=Locks.PlaceLock("cerradurp1","Cerraduracutre",(4078.681964,-1146.465318,-39429.670386),(0.707107,0.707107,0.000000,0.000000),3.0)
cerradurp1.key="llave1"


cerradurp1.OnUnLockFunc=AbrePuertaLlave1
cerradurp1.OnUnLockArgs=()

cerradurp1.OnLockFunc=CierraPuertaLlave1
cerradurp1.OnLockArgs=()

darfuncs.SetHint(cerradurp1.obj,"Rusted Lock")

o=Bladex.CreateEntity("llave1","Llavecutre",34118.433737,-1024.213967,-14881.109188)
o.Static=0
o.Scale=1.0
o.Orientation=0.005994,0.998093,0.004829,-0.061254
darfuncs.SetHint(o,"Rusted Key")
#Stars.Twinkle("llavemaz")


##########################
#-PUERTA-LLAVE-2
##########################

maderadesliz2=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderadesliz2.MaxDistance=25000
maderadesliz2.MinDistance=2000
maderadesliz2.Volume=1.0

maderagolpe2=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
maderagolpe2.MaxDistance=25000
maderagolpe2.MinDistance=3000
maderagolpe2.Volume=1.0

puerta2=Doors.CreateDoor("Puerta2", (-78000,-10000,-39500), (0,1,0), 2000, 7000, Doors.CLOSED)


puerta2.opentype=Doors.UNIF
puerta2.o_med_vel=-500
puerta2.o_med_displ=5000


puerta2.closetype=Doors.AC
puerta2.c_init_displ=5000
puerta2.c_med_vel=8000


puerta2.SetWhileOpenSound(maderadesliz2)
puerta2.SetEndOpenSound(maderagolpe2)

puerta2.SetWhileCloseSound(maderadesliz2)
puerta2.SetEndCloseSound(maderagolpe2)

###llave2 abrepuerta2###


cerradurp2=Locks.PlaceLock("cerradurp2","Cerraduracutre",(-75450.511670,-10163.771105,-35228.949950),(0.707107,0.707107,0.000000,0.000000),2.5)
cerradurp2.key="llave2"

cerradurp2.OnUnLockFunc=AbrePuertaLlave2
cerradurp2.OnUnLockArgs=()

cerradurp2.OnLockFunc=CierraPuertaLlave2
cerradurp2.OnLockArgs=()

darfuncs.SetHint(cerradurp2.obj,"Iron Lock")


o=Bladex.CreateEntity("llave2","Llavecutre",-55289.975223,-7821.702465,-75108.874982)
o.Static=0
o.Scale=1.0
o.Orientation=0.000000,0.997662,0.004525,-0.068190

darfuncs.SetHint(o,"Iron Key")

##########################
#-PUERTA-LLAVE-4
##########################

maderadesliz4=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderadesliz4.MaxDistance=25000
maderadesliz4.MinDistance=1500
maderadesliz4.Volume=1.0

maderagolpe4=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
maderagolpe4.MaxDistance=25000
maderagolpe4.MinDistance=1500
maderagolpe4.Volume=1.0


puerta4=Doors.CreateDoor("Puerta4", (-5500,-8000,-15200), (0,1,0), 500, 4800, Doors.CLOSED)


puerta4.opentype=Doors.UNIF
puerta4.o_med_vel=-500
puerta4.o_med_displ=4300


puerta4.closetype=Doors.AC
puerta4.c_init_displ=4300
puerta4.c_med_vel=8000


puerta4.SetWhileOpenSound(maderadesliz4)
puerta4.SetEndOpenSound(maderagolpe4)

puerta4.SetWhileCloseSound(maderadesliz4)
puerta4.SetEndCloseSound(maderagolpe4)

###llave4 abrepuerta4###


cerradurp4=Locks.PlaceLock("cerradurp4","Cerraduracutre",(-7910,-5982.376483,-16386.744945),(0.707107,0.707107,0.000000,0.000000),2.5)
cerradurp4.key="llave4"


cerradurp4.OnUnLockFunc=AbrePuertaLlave4
cerradurp4.OnUnLockArgs=()

cerradurp4.OnLockFunc=CierraPuertaLlave4
cerradurp4.OnLockArgs=()

darfuncs.SetHint(cerradurp4.obj,"Store Lock")

o=Bladex.CreateEntity("llave4","Llavecutre",-28310.136572,-8422.846753,-60724.986230)
o.Static=0
o.Scale=1.0
o.Orientation=0.999346,-0.024014,-0.027028,0.000765
darfuncs.SetHint(o,"Store Key")
Stars.Twinkle("llave4")


############################################################
####--------------------------------------------------------------------------------------------#####
####----------------------PUERTA-PALANCA-1-------------(se abre desde dentro)-------------------#####
####--------------------------------------------------------------------------------------------#####
############################################################

res=ReadGSFile.ReadGhostSectorFile("PTAOCT.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

char.SendTriggerSectorMsgs=1

#char.Position=13397.7188947, -1034.64840183, -35059.538

maderadesliz3=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderadesliz3.MaxDistance=35000
maderadesliz3.MinDistance=5000
maderadesliz3.Volume=1.0

maderagolpe3=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
maderagolpe3.MaxDistance=35000
maderagolpe3.MinDistance=5000
maderagolpe3.Volume=1.0

puertar1=Doors.CreateDoor("Puertar1", (14060,-2750,-30430), (0,1,0), 500, 5000, Doors.CLOSED)


puertar1.opentype=Doors.UNIF
puertar1.o_med_vel=-800
puertar1.o_med_displ=4500


puertar1.closetype=Doors.AC
puertar1.c_init_displ=4500
puertar1.c_med_vel=8000


puertar1.SetWhileOpenSound(maderadesliz3)
puertar1.SetEndOpenSound(maderagolpe3)

puertar1.SetWhileCloseSound(maderadesliz3)
puertar1.SetEndCloseSound(maderagolpe3)

##### Accionar puertas al accionar una palanca


#palanr1=Levers.PlaceLever("PALAP1",Levers.LeverType3,(10430,-1000.0,-27610.0),(0.500,0.500,-0.500000,0.50),1.0)

#palanr1.mode=1

ladoABIERTO=0




#palanr1.OnTurnOnFunc=AbrePuertar1
#palanr1.OnTurnOnArgs=()

#palanr1.OnTurnOffFunc=CierraPuertar1
#palanr1.OnTurnOffArgs=()



print("poniendo el trigger sector")
Bladex.SetTriggerSectorFunc("PTAOCT", "OnEnter", EntroEnTriggerSector)



##########################################################
####### PUERTA A LA SEGUNDA PARTE DE LA BIBLIOTECA    ####
##########################################################

piedesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
piedesliz.MaxDistance=25000
piedesliz.MinDistance=2000
piedesliz.Volume=1.0

piedgolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
piedgolpe.MaxDistance=25000
piedgolpe.MinDistance=2000
piedgolpe.Volume=1.0


ptatrampa1=Doors.CreateDoor("ptatrampa1", (-256000,-32000,67000), (1,0,0), 0, 3750, Doors.CLOSED)
ptatrampa2=Doors.CreateDoor("ptatrampa2", (-253000,-32000,67000), (-1,0,0), 0, 3750, Doors.CLOSED)

ptatrampa1.opentype=Doors.UNIF
ptatrampa1.o_med_vel=-1000
ptatrampa1.o_med_displ=3750

ptatrampa1.closetype=Doors.AC
ptatrampa1.c_init_displ=3750
ptatrampa1.c_med_vel=5000

ptatrampa2.opentype=Doors.UNIF
ptatrampa2.o_med_vel=-1000
ptatrampa2.o_med_displ=3750


ptatrampa2.closetype=Doors.AC
ptatrampa2.c_init_displ=3750
ptatrampa2.c_med_vel=5000


ptatrampa1.SetWhileOpenSound(piedesliz)
ptatrampa1.SetEndOpenSound(piedgolpe)

ptatrampa1.SetWhileCloseSound(piedesliz)
ptatrampa1.SetEndCloseSound(piedgolpe)



###llave3 abrepta###


#cerradurpta=Locks.PlaceLock("cerradurpta","Cerraduracobox",(-278892.561909,-26903.411289,68078.942891),(0.500,0.500,-0.500,0.500),1.5)
cerradurpta=Locks.PlaceLock("cerradurpta","Cerraduracobox",(-258482.290382,-27138.719921,70549.289048),(0.687569,0.687569,-0.165071,0.165071),1.5)
cerradurpta.key="llave3"


cerradurpta.OnUnLockFunc=Abrepta
cerradurpta.OnUnLockArgs=()

cerradurpta.OnLockFunc=Cierrapta
cerradurpta.OnLockArgs=()

darfuncs.SetHint(cerradurpta.obj,"Bronze Lock")

#o=Bladex.CreateEntity("llave3","Llavecobox",-263277.340255,-28286.140124,63048.495143)
#o.Static=0
#o.Scale=1.0
#o.Orientation=0.008806,0.997496,-0.001779,-0.070155



###################################################################
#######
####### PUERTA SECRETA FINAL DE LA BIBLIOTECA CON PULSADORES   ####
#######
###################################################################




piedesliz2=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-deslizando-2.wav", "MadDesliz")
piedesliz2.MaxDistance=25000
piedesliz2.MinDistance=2000
piedesliz2.Volume=1.0

piedgolpe2=Sounds.CreateEntitySound("../../Sounds/mechanism8.wav", "MadGolpe")
piedesliz2.MaxDistance=25000
piedesliz2.MinDistance=2000
piedesliz2.Volume=1.0

ptatrampa3=Doors.CreateDoor("ptatrampa3", (-269250,-32000,57500), (0,-1,0), 0, 4500, Doors.CLOSED)
ptatrampa4=Doors.CreateDoor("ptatrampa4", (-269750,-32000,57500), (0,-1,0), 0, 4750, Doors.CLOSED)

ptatrampa3.opentype=Doors.UNIF
ptatrampa3.o_med_vel=-1000
ptatrampa3.o_med_displ=4500


ptatrampa4.opentype=Doors.UNIF
ptatrampa4.o_med_vel=-1000
ptatrampa4.o_med_displ=4750




ptatrampa3.SetWhileOpenSound(piedesliz2)
ptatrampa3.SetEndOpenSound(piedgolpe2)




oto1=Bladex.CreateEntity("blosu1","AdoquinRuna",-269196.294385,-32236.744500,61817.478086)
oto1.Static=0
oto1.Scale=1.000000
oto1.Orientation=0.707107,0.707107,0.000000,0.000000
darfuncs.SetHint(oto1,"Trigger")

oto2=Bladex.CreateEntity("blosu2","AdoquinRuna",-269114.653081,-32245.583494,53325.440237)
oto2.Static=0
oto2.Scale=1.000000
oto2.Orientation=0.707107,0.707107,0.000000,0.000000
darfuncs.SetHint(oto2,"Trigger")

button=Button.CreateButtonCombination(0,Abresub,"")
button.AddButton("blosu1",2,(0,1,0),400,0,0,1)
button.AddButton("blosu2",2,(0,1,0),400,0,0,1)

####################################################
########    PUERTAS SALA GRANDE
####################################################


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


maderadeslizg=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderadeslizg.MaxDistance=25000
maderadeslizg.MinDistance=5000
maderadeslizg.Volume=1.0

maderagolpeg=Sounds.CreateEntitySound("../../Sounds/golpe-metal-pesado.wav", "MaderaGolpe")
maderagolpeg.MaxDistance=28000
maderagolpeg.MinDistance=5000
maderagolpeg.Volume=1.0

maderadeslizg2=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderadeslizg2.MaxDistance=25000
maderadeslizg2.MinDistance=5000
maderadeslizg2.Volume=1.0

maderagolpeg2=Sounds.CreateEntitySound("../../Sounds/golpe-metal-pesado.wav", "MaderaGolpe")
maderagolpeg2.MaxDistance=28000
maderagolpeg2.MinDistance=5000
maderagolpeg2.Volume=1.0

#1	la que se cierra
puertasag1=Doors.CreateDoor("Puertasag1", (-199000,-16000,30500), (0,1,0), 500, 5000, Doors.OPENED)
puertasag1.opentype=Doors.UNIF
puertasag1.o_med_vel=-500
puertasag1.o_med_displ=4500

puertasag1.closetype=Doors.AC
puertasag1.c_init_displ=4500
puertasag1.c_med_vel=8000
puertasag1.OnEndCloseFunc=LineaPolvo

puertasag1.SetWhileCloseSound(maderadeslizg)
puertasag1.SetEndCloseSound(maderagolpeg)

#2	la que se abre
puertasag2=Doors.CreateDoor("Puertasag2", (-229000,-16000,-1562), (0,1,0), 500, 4000, Doors.OPENED)
puertasag2.opentype=Doors.UNIF
puertasag2.o_med_vel=-500
puertasag2.o_med_displ=3500

puertasag2.closetype=Doors.AC
puertasag2.c_init_displ=3500
puertasag2.c_med_vel=8000

puertasag2.SetWhileOpenSound(maderadeslizg2)
puertasag2.SetEndOpenSound(maderagolpeg2)





#####



serr1=Bladex.GetSector(-207000,-16000,30500)
serr1.OnEnter=CierraPuertasag

serr2=Bladex.GetSector(-206000,-16000,37500)
serr2.OnEnter=CierraPuertasag

serr3=Bladex.GetSector(-206000,-16000,23500)
serr3.OnEnter=CierraPuertasag