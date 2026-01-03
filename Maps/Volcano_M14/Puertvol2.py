import Doors
import Levers
import Locks
import Objects
import Sounds
import Button
import Sparks
import darfuncs
import Stars

############################################################
##########-PUERTA-6. Bajo. Sale a por la jaula de la primera torre.
############################################################
############################################################
############################################################
############################################################

"""
##Rastrillo.  con la palanca##

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

rast6=Bladex.CreateEntity("Rast6","Rastrillo",47937.273502,6133.562328,20766.335102)
rast6.Static=1
rast6.Scale=0.803396
rast6.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Rast6")

rast6din=Objects.CreateDinamicObject("Rast6")

##funciones abrir-cerrar##

def Abrerast6():

	desplazamientos=(1550.0, 1500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto rast6
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rast6din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Cierrarast6():

	desplazamientos=(1550.0, 1500.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)

	#sonidos asociados a la puerta-objeto rast6
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(rast6din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

##### Abrir el rastrillo al accionar una palanca


palanc6=Levers.PlaceLever("Palanc6",Levers.LeverType3,(50752.758412,7332.079709,17254.874558),(0.707107,0.707107,0.000000,0.000000),1.0)

palanc6.mode=3


palanc6.OnTurnOnFunc=Abrerast6
palanc6.OnTurnOnArgs=()

palanc6.OnTurnOffFunc=Cierrarast6
palanc6.OnTurnOffArgs=()



#######################################
#######################################
####### PUERTAS 5 #####################
#########REJA Y METALICA###############

########REJA########
##Rastrillo.  con la palanca##

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

rast5=Bladex.CreateEntity("Rast5","Rastrillo",-17250.875753,7079.460563,-6124.335298)
rast5.Static=1
rast5.Scale=0.741923
rast5.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Rast5")

rast5din=Objects.CreateDinamicObject("Rast5")

##funciones abrir-cerrar##

def Abrerast5():

	desplazamientos=(1550.0, 1700.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto rast6
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rast5din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Cierrarast5():

	desplazamientos=(1550.0, 1700.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)

	#sonidos asociados a la puerta-objeto rast5
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(rast5din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

##### Abrir el rastrillo al accionar una palanca


palanc5=Levers.PlaceLever("Palanc5",Levers.LeverType3,(-19379.715795,8262.105290,-7144.357494),(0.688984,0.688984,-0.159064,0.159064),1.0)

palanc5.mode=3


palanc5.OnTurnOnFunc=Abrerast5
palanc5.OnTurnOnArgs=()

palanc5.OnTurnOffFunc=Cierrarast5
palanc5.OnTurnOffArgs=()
"""

###################
##### Puerta  #####
###################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")

puerta5=Doors.CreateDoor("Puerta5", (-17250,5000,2750), (0,1,0), 1250, 6250, Doors.CLOSED)
puerta5.Squezze = 1

puerta5.opentype=Doors.UNIF
puerta5.o_med_vel=-500
puerta5.o_med_displ=5000


puerta5.closetype=Doors.AC
puerta5.c_init_displ=5000
puerta5.c_med_vel=16000


puerta5.SetWhileOpenSound(maderadesliz)
puerta5.SetEndOpenSound(maderagolpe)

puerta5.SetWhileCloseSound(maderadesliz)
puerta5.SetEndCloseSound(maderagolpe)

##### Accionar puertas al accionar una palanca


palancap5=Levers.PlaceLever("PalancaP5",Levers.LeverType3,(-15315.610239,8280.278640,-7122.525406),(0.676210,0.676210,0.206738,-0.206738),1.0)

palancap5.mode=2


palancap5.OnTurnOnFunc=AbrePuerta5
palancap5.OnTurnOnArgs=()

palancap5.OnTurnOffFunc=CierraPuerta5
palancap5.OnTurnOffArgs=()


###################################
##### Puerta 21 22. Se abren con la misma palanca. #####
###################################
##Rastrillo 21.##

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

rast21=Bladex.CreateEntity("Rast21","Rastrillo",34529.946242,-2825.309330,20122.104902)
rast21.Static=1
rast21.Scale=0.827740
rast21.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Rast21")

rast21din=Objects.CreateDinamicObject("Rast21")


##### Abrir el rastrillo al accionar una palanca


palanc2=Levers.PlaceLever("Palanc2",Levers.LeverType3,(36278.223657,-1078.505824,17871.397098),(0.707107,0.707107,0.000000,0.000000),1.0)

palanc2.mode=2

palanc2.OnTurnOnFunc=Abrerast2
palanc2.OnTurnOnArgs=()


#######################################
##### puerta 4 sala del minotauro #####
#######################################


puerta4=Bladex.CreateEntity("Puerta4","Rastrillo",-17205.481421,-15153.388106,2656.54690)
puerta4.Static=1
puerta4.Scale=0.905287
puerta4.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Puerta4")

puerta4din=Objects.CreateDinamicObject("Puerta4")

##funciones abrir-cerrar##



###cerradura rastrillos###

##cerradura ##

cerradura4=Locks.PlaceLock("cerradura4","Cerraduracutre",(-20102.403369,-12902.718428,4250.609346),(0.512917,0.512917,-0.486740,0.486740),2.5)
cerradura4.key="llave4"


cerradura4.OnUnLockFunc=Abrepuerta4
cerradura4.OnUnLockArgs=()

cerradura4.OnLockFunc=Cierrapuerta4
cerradura4.OnLockArgs=()

darfuncs.SetHint(cerradura4.obj,"Tower Lock")


s1=Bladex.GetSector(-17250,-15000,-8250)
s1.OnEnter=Cierrarastfin


##Llave 4##

o=Bladex.CreateEntity("llave4","Llavecutre",-45000,-12000,12000)
o.Static=0
o.Scale=1.0
o.Orientation=0.707107,0.707107,0.000000,0.000000
darfuncs.SetHint(o,"Tower Key")


NoSeAbrioNuncaLaPuerta = 1


#######################################
##### puerta 4b sala del que tira flechas#####
#######################################


puerta4b=Bladex.CreateEntity("Puerta4b","Rastrillo",-23653.119300,-15354.268650,-11965.684007)
puerta4b.Static=1
puerta4b.Scale=0.698925
puerta4b.Orientation=0.491198,0.491198,0.508650,-0.508650
Sparks.SetMetalSparkling("Puerta4b")

puerta4bdin=Objects.CreateDinamicObject("Puerta4b")

##funciones abrir-cerrar##



###cerradura rastrillos###

##cerradura4b1 ##

#cerradura4b1=Locks.PlaceLock("cerradura4b1","Cerraduracutre",(-22697.137404,-14403.694633,-14302.879875),(0.627211,0.627211,-0.326506,0.326506),2.5)
#cerradura4b1.key="llave4b"


#cerradura4b1.OnUnLockFunc=Abrepuerta4b
#cerradura4b1.OnUnLockArgs=()

#cerradura4b1.OnLockFunc=Cierrapuerta4b
#cerradura4b1.OnLockArgs=()

##cerradura4b2 ##

cerradura4b2=Locks.PlaceLock("cerradura4b2","Cerraduracutre",(-24025.942257,-13941.891524,-10118.184452),(0.012341,0.012341,-0.706999,0.706999),2.5)
cerradura4b2.key="llave4"


cerradura4b2.OnUnLockFunc=Abrepuerta4b
cerradura4b2.OnUnLockArgs=()

cerradura4b2.OnLockFunc=Cierrapuerta4b
cerradura4b2.OnLockArgs=()

darfuncs.SetHint(cerradura4b2.obj,"Tower Lock")



#######################
##################
######################
######## PUERTA CON 2 PULSADORES
##################



#maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
#maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


#escalon 2a
puerta2a=Doors.CreateDoor("Puerta2a", (-1750,0,38000), (1,0,0), 0, 4000, Doors.CLOSED)

puerta2a.opentype=Doors.UNIF
puerta2a.o_med_vel=500
puerta2a.o_med_displ=4000



o=Bladex.CreateEntity("bloque1","Bloque",4810.202887,575.098896,54299.570412)
o.Static=0
o.Scale=1.000000
o.Orientation=0.500000,0.500000,0.500000,-0.500000
darfuncs.SetHint(o,"Trigger")

o=Bladex.CreateEntity("bloque2","Bloque",10308.565315,572.687797,54385.628357)
o.Static=0
o.Scale=1.000000
o.Orientation=0.500000,0.500000,0.500000,-0.500000
darfuncs.SetHint(o,"Trigger")

button=Button.CreateButtonCombination(0,Abrep1,"")
button.AddButton("bloque1",3,(0,0,1),400,0,0,1)
button.AddButton("bloque2",3,(0,0,1),400,0,0,1)





#######RASTRILLO SECRETO SALA SECRETA TIENE LA LLAVE EL TROLL


sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

rastrag=Bladex.CreateEntity("RastRag","Rastrillo",-30642.147383,705.269755,-12231.006249)
rastrag.Static=0
rastrag.Scale=0.596058
rastrag.Orientation=0.500000,0.500000,0.500000,-0.500000
Sparks.SetMetalSparkling("RastRag")

rastragdin=Objects.CreateDinamicObject("RastRag")

##funciones abrir-cerrar##

###llave que abre el rastrillo ragnar


cerradurfin=Locks.PlaceLock("cerradurfin","Cerraduracutre",(-29796.936594,1671.820989,-10268.698800),(0.707107,0.707107,0.000000,0.000000),3)
cerradurfin.key="llaverag"


cerradurfin.OnUnLockFunc=Abrerastrag
cerradurfin.OnUnLockArgs=()



o=Bladex.CreateEntity("llaverag","Llavecutre",-27722.708798,1443.267281,-10645.579019)
o.Static=0
o.Scale=1.0
o.Orientation=0.999453,-0.016495,-0.028670,0.000210






###########################################################################
################## PUERTA DEL TEMPLO FINAL QUE SE ABRE Y SE CIERRA AL PASAR
###########################################################################


#maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
#maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


#escalon 2a
puertaTEM=Doors.CreateDoor("PuertaTEM", (5240,-9360,-67760), (0,1,0), 1000, 6750, Doors.CLOSED)
puertaTEM.Squezze = 1

puertaTEM.opentype=Doors.UNIF
puertaTEM.o_med_vel=-1000
puertaTEM.o_med_displ=5750


puertaTEM.closetype=Doors.AC
puertaTEM.c_init_displ=5750
puertaTEM.c_med_vel=16000

stem2=Bladex.GetSector(6432.30595735, -9365.20014088, -79176.233)
stem2.OnEnter=CierrapuertaTEM


#################
###########PUERTA DE LA ARMERIA
###############################
sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")


puerta1=Bladex.CreateEntity("Puerta1","Rastrillo",-25189.670124,6040.914204,18490.049319,"Physic")
puerta1.Scale=0.665003
puerta1.Orientation=0.495618,0.495618,0.504344,-0.504344
Sparks.SetMetalSparkling("Puerta1")

puerta1din=Objects.CreateDinamicObject("Puerta1")

##funciones abrir-cerrar##


###cerradura rastrillos###

##cerradura ##

cerradura1=Locks.PlaceLock("cerradura1","Cerraduracutre",(-24491.190354,7197.879557,16685.104736),(0.707107,0.707107,0.000000,0.000000),3.0)
cerradura1.key="llave1"


cerradura1.OnUnLockFunc=Abrepuerta1
cerradura1.OnUnLockArgs=()

cerradura1.OnLockFunc=Cierrapuerta1
cerradura1.OnLockArgs=()

darfuncs.SetHint(cerradura1.obj,"Weapon Store Lock")

##Llave 1##

o=Bladex.CreateEntity("llave1","Llavecutre",-22551.379175,7016.070526,16618.196600,"Physic")
o.Scale=1.0
o.Orientation=0.997457,-0.008145,-0.070589,-0.005438
darfuncs.SetHint(o,"Weapon Store Key")


########### PUERTA DE ANTES DEL FINAL QUE SE CIERRA SOLA


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")


puertaen=Doors.CreateDoor("Puertaen", (6000,-9000,-29000), (0,1,0), 4000, 7000, Doors.CLOSED)
puertaen.Squezze = 1

puertaen.opentype=Doors.UNIF
puertaen.o_med_vel=-500
puertaen.o_med_displ=6000


puertaen.closetype=Doors.AC
puertaen.c_init_displ=3000
puertaen.c_med_vel=10000


puertaen.SetWhileOpenSound(maderadesliz)
puertaen.SetEndOpenSound(maderagolpe)


cerraduren=Locks.PlaceLock("cerraduren","Cerraduracutre",(4516.311003,-7842.876522,-28107.322643),(0.707107,0.707107,0.000000,0.000000),3.0)
cerraduren.key="llavemaz"

cerraduren.OnUnLockFunc=AbrePuertaLlaveen
cerraduren.OnUnLockArgs=()

darfuncs.SetHint(cerraduren.obj,"Dungeon Lock")

puertaen.SetWhileCloseSound(maderadesliz)
puertaen.SetEndCloseSound(maderagolpe)


sen=Bladex.GetSector(5655, -8654, -31592)
sen.OnEnter=CierraPuertaLlaveen

o=Bladex.CreateEntity("llavemaz","Llavecutre",4756.311003,-7842.876522,-28007.322643)
o.Static=0
o.Scale=1.0
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.Data = 4
darfuncs.SetHint(o,"Dungeon Key")




########################PUERTAS DE LOS MINOTAUROS

puertaP=Doors.CreateDoor("PuertaP", (36500,6000,15500), (0,0,-1), 0, 4000, Doors.CLOSED)

puertaP.opentype=Doors.UNIF
puertaP.o_med_vel=-500
puertaP.o_med_displ=4000




puertaPP=Doors.CreateDoor("PuertaPP", (36500,6000,11000), (0,0,1), 0, 4000, Doors.CLOSED)

puertaPP.opentype=Doors.UNIF
puertaPP.o_med_vel=-500
puertaPP.o_med_displ=4000
