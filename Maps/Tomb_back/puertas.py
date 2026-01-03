import Doors
import Levers
import Locks
import Objects
import Sounds
import Sparks
import ReadGSFile
import Button
import Bladex
import AuxFuncs
import darfuncs
import Stars


############################################################
#####--RASTRILLO---CEMENTERIO--SALIDA---------##############
############################################################

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

reja1=Bladex.CreateEntity("Reja1","Rastrillo",47092.596500,-2339.457184,8579.180533)
reja1.Scale=1.232392
reja1.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetSparkling("Reja1")

reja1din=Objects.CreateDinamicObject("Reja1")

##funciones abrir-cerrar##


##### Abrir el rastrillo al accionar una palanca

palance1=Levers.PlaceLever("Palance1",Levers.LeverType3,(44246.871592,-268.947068,6970.200829),(0.707107,0.707107,0.000000,0.000000),1.0)

palance1.mode=3


palance1.OnTurnOnFunc=Abrereja1
palance1.OnTurnOnArgs=()

palance1.OnTurnOffFunc=Cierrareja1
palance1.OnTurnOffArgs=()

############################################################
#####------------------ANTES-RASTRILLO---TORRE-----AHORA-PUERTA-BRONCE-------------########
############################################################



###########################################
###-------------llave-segundo--recinto--abre--puerta1--------------------###
###########################################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderadesliz.MaxDistance=20000
maderadesliz.MinDistance=2000
maderadesliz.Volume=1.0

maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
maderadesliz.MaxDistance=20000
maderadesliz.MinDistance=2000
maderadesliz.Volume=1.0



Lorenzo1=Doors.CreateDoor("Lorenzo", (2687,-1500,30000), (0,1,0), 1000, 5000, Doors.OPENED)


Lorenzo1.opentype=Doors.UNIF
Lorenzo1.o_med_vel=-700
Lorenzo1.o_med_displ=4000


Lorenzo1.closetype=Doors.AC
Lorenzo1.c_init_displ=4000
Lorenzo1.c_med_vel=8000


Lorenzo1.SetWhileOpenSound(maderadesliz)
Lorenzo1.SetEndOpenSound(maderagolpe)

Lorenzo1.SetWhileCloseSound(maderadesliz)
Lorenzo1.SetEndCloseSound(maderagolpe)


###########################################


cerradurp1=Locks.PlaceLock("cerradurp1","Cerraduracutre",(1528.580957,-179.875893,34186.648470),(0.000000,0.000000,0.707107,-0.707107),2.5)
cerradurp1.key="llave1"

cerradurp1.OnUnLockFunc=AbrePuertaLlave1
cerradurp1.OnUnLockArgs=()

cerradurp1.OnLockFunc=CierraPuertaLlave1
cerradurp1.OnLockArgs=()

#en la puerta
#o=Bladex.CreateEntity("llave1","Llavecutre",-155.479212,978.895795,27418.445363)
#o.Static=0
#o.Scale=1.0
#o.Orientation=0.003416,0.981379,0.002321,0.192038

#en la torre
#o=Bladex.CreateEntity("llave1","Llavecutre",68681.759000,-3067.986000,-13844.493000)
#o.Static=0
#o.Scale=1.000000
#o.Orientation=0.998924,0.016785,-0.043168,-0.002390
#Stars.Twinkle("llave1")

######################################################
###-------------PUERTA DEL TEMPLO---se cierra al entrar con el fetiche--------------------###
######################################################


###########################################
###----------------------------llave-cementerio--------------------------------###
###########################################



############################################################
############################################################
####----------------.......................,,,,,,,,,,,--#####
####----PUERTA-ACCESO AL PISO SUPERIOR DEL TEMPLO-------#####
############################################################
############################################################




############################################################
############################################################
####----------------------------------------------------------------------------------------------------------------#####
####---------------------------PUERTA--SALA--TABLILLA---------------------------------------#####
############################################################
############################################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puertaz4=Doors.CreateDoor("Puertaz4", (154875,2000,625), (0,1,0), 1000, 7000, Doors.CLOSED)


puertaz4.opentype=Doors.UNIF
puertaz4.o_med_vel=-800
puertaz4.o_med_displ=6000


puertaz4.closetype=Doors.AC
puertaz4.c_init_displ=6000
puertaz4.c_med_vel=8000


puertaz4.SetWhileOpenSound(maderadesliz)
puertaz4.SetEndOpenSound(maderagolpe)

puertaz4.SetWhileCloseSound(maderadesliz)
puertaz4.SetEndCloseSound(maderagolpe)

##### Accionar puerta al pasar por un sector


serT=Bladex.GetSector(151000,0,1000)

serT.OnEnter=AbrePuertaz4

############################################################
#####------------------------------RASTRILLO---ENTRADA-AL RECINTO----------------------#########
############################################################


###########################################
###      puerta sala tablillas          ###
###########################################


sptaDesliz1=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-deslizando-2.wav", "sptaDesliz1")
sptaDesliz1.MaxDistance=20000
sptaDesliz1.MinDistance=2000
sptaDesliz1.Volume=1.0

sptaGolpe1=Sounds.CreateEntitySound("../../Sounds/M-CIERRE-GATE.wav", "sptaGolpe1")
sptaGolpe1.MaxDistance=20000
sptaGolpe1.MinDistance=2000
sptaGolpe1.Volume=1.0

sptaDesliz2=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-deslizando-2.wav", "sptaDesliz2")
sptaDesliz2.MaxDistance=20000
sptaDesliz2.MinDistance=2000
sptaDesliz2.Volume=1.0

sptaGolpe2=Sounds.CreateEntitySound("../../Sounds/M-CIERRE-GATE.wav", "sptaGolpe2")
sptaGolpe2.MaxDistance=20000
sptaGolpe2.MinDistance=2000
sptaGolpe2.Volume=1.0

#1
puertata1=Doors.CreateDoor("puertata1", (114600,-1500,625), (-1,0,0), 0, 600, Doors.CLOSED)

puertata1.opentype=Doors.UNIF
puertata1.o_med_vel=-800
puertata1.o_med_displ=600

puertata1.closetype=Doors.AC
puertata1.c_init_displ=600
puertata1.c_med_vel=800

#2
puertata2=Doors.CreateDoor("puertata2", (115200,0,625), (0,-1,0), 0, 3800, Doors.CLOSED)

puertata2.opentype=Doors.UNIF
puertata2.o_med_vel=-800
puertata2.o_med_displ=3800

puertata2.closetype=Doors.AC
puertata2.c_init_displ=3800
puertata2.c_med_vel=800


puertata1.SetWhileOpenSound(sptaDesliz1)
puertata1.SetEndOpenSound(sptaGolpe1)

puertata1.SetWhileCloseSound(sptaDesliz1)
puertata1.SetEndCloseSound(sptaGolpe1)

puertata2.SetWhileOpenSound(sptaDesliz2)
puertata2.SetEndOpenSound(sptaGolpe1)

puertata2.SetWhileCloseSound(sptaDesliz2)
puertata2.SetEndCloseSound(sptaGolpe2)


o=Bladex.CreateEntity("bloqueta","AdoquinRuna",114850.331751,-2147.724669,569.486034)
o.Static=0
o.Scale=1.661078
o.Orientation=0.000000,0.000000,0.707107,-0.707107


###de adorno
o=Bladex.CreateEntity("sss","AdoquinRuna",173458.487969,6241.802718,554.232000)
o.Static=0
o.Scale=1.853212
o.Orientation=0.006171,0.006171,-0.707080,0.707080



buttonta=Button.CreateButtonCombination(0,AbrePuertata,"")
xx = buttonta.AddButton("bloqueta",3,(1,0,0),20,0,0,1)
xx.sound = Bladex.CreateSound('../../Sounds/block-sliding.wav', 'Sound pta')
xx.sound.Volume=0.4
xx.sound.MinDistance=1000
xx.sound.MaxDistance=10000

############################################################
#####--RASTRILLO---CRIPTA---FINAL-------------##############
############################################################


###################################
#####-------PUERTA DOBLE-DEL TEMPLO----#######
###################################



########################################################################3
####	puerta de LAS COSITAS





########################################################################3
####	puerta DEL CUERPO DE GUARDIA
"""

spuertag2d=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
spuertag2d.MaxDistance=20000
spuertag2d.MinDistance=1000
spuertag2d.Volume=1.0


spuertag2g=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
spuertag2g.MaxDistance=20000
spuertag2g.MinDistance=2000
spuertag2g.Volume=1.0

puertag2=Doors.CreateDoor("Puertag2", (-27500,-7000,-2375), (1,0,0), 0, 2000, Doors.CLOSED)


puertag2.opentype=Doors.UNIF
puertag2.o_med_vel=-800
puertag2.o_med_displ=2000


puertag2.closetype=Doors.AC
puertag2.c_init_displ=2000
puertag2.c_med_vel=8000


puertag2.SetWhileOpenSound(spuertag2d)
puertag2.SetEndOpenSound(spuertag2g)

puertag2.SetWhileCloseSound(spuertag2d)
puertag2.SetEndCloseSound(spuertag2g)

##### Accionar puertas al accionar una palanca


palang2=Levers.PlaceLever("PALAPg2",Levers.LeverType3,(-29504.066889,-5593.354723,-3388.334217),(0.707107,0.707107,0.000000,0.000000),1.0)

palang2.mode=1


#def AbrePuertag2():
#	puertag2.OpenDoor()

#def CierraPuertag2():
#	puertag2.CloseDoor()




palang2.OnTurnOnFunc=AbrePuertag2
palang2.OnTurnOnArgs=()

palang2.OnTurnOffFunc=CierraPuertag2
palang2.OnTurnOffArgs=()

"""
#####################	SARCOFAGO




##################################################################################
#####	PUERTA QUE SE ABRE DE SALIDA DEL CEMENTERIO
