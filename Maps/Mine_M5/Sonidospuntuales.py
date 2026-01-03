

import Sounds
import Bladex

#####--cuervos del acantilado--######




cuervo1=Sounds.CreatePeriodicSound("../../Sounds/raven-call.wav", "cuervo1",20,5,(58000,-15000,-15000))
cuervo1.sound.Volume=1
cuervo1.sound.MinDistance=5000
cuervo1.sound.MaxDistance=20000
cuervo1.sound.Volume=1
cuervo1.sound.BaseVolume=1.0

cuervo1.sound.SendNotify=0

cuervo1.PlayPeriodic()

###############

cuervo2=Sounds.CreatePeriodicSound("../../Sounds/raven-call.wav", "cuervo2",10,5,(58500,-14500,-15000))
cuervo2.sound.Volume=1
cuervo2.sound.MinDistance=5000
cuervo2.sound.MaxDistance=20000
cuervo2.sound.Volume=1
cuervo2.sound.BaseVolume=1.0

cuervo2.sound.SendNotify=0

cuervo2.PlayPeriodic()

###############

cuervo3=Sounds.CreatePeriodicSound("../../Sounds/raven-call.wav", "cuervo3",15,5,(57500,-17500,-15500))
cuervo3.sound.Volume=1
cuervo3.sound.MinDistance=5000
cuervo3.sound.MaxDistance=20000
cuervo3.sound.Volume=1
cuervo3.sound.BaseVolume=1.0

cuervo3.sound.SendNotify=0

cuervo3.PlayPeriodic()

###############

cuervo4=Sounds.CreatePeriodicSound("../../Sounds/eagle-screech.wav", "cuervo4",10,5,(39500,-17500,-64500))
cuervo4.sound.Volume=1
cuervo4.sound.MinDistance=5000
cuervo4.sound.MaxDistance=20000
cuervo4.sound.Volume=1
cuervo4.sound.BaseVolume=1.0

cuervo4.sound.SendNotify=0

cuervo4.PlayPeriodic()

###############

cuervo5=Sounds.CreatePeriodicSound("../../Sounds/raven-call.wav", "cuervo5",10,5,(39000,-15500,-60500))
cuervo5.sound.Volume=1
cuervo5.sound.MinDistance=5000
cuervo5.sound.MaxDistance=20000
cuervo5.sound.Volume=1
cuervo5.sound.BaseVolume=1.0

cuervo5.sound.SendNotify=0

cuervo5.PlayPeriodic()

####################
########## VIENTOS PUNTUALES
#############

v1=Bladex.CreateSound("../../Sounds/whistlingwind-thruconduit.wav","v1")
v1.MaxDistance=20000
v1.MinDistance=10000
v1.Volume=1.0
v1.BaseVolume=1.0
#v1.Scale=1.0
v1.SendNotify=0
v1.Play(28000, -18000, -64750,-1)

v2=Bladex.CreateSound("../../Sounds/whistlingwind-thruconduit.wav","v2")
v2.MaxDistance=20000
v2.MinDistance=10000
v2.Volume=1.0
v2.BaseVolume=1.0
#v2.Scale=1.0
v2.SendNotify=0
v2.Play(33000, -18000, -89000,-1)

v3=Bladex.CreateSound("../../Sounds/whistlingwind-thruconduit.wav","v3")
v3.MaxDistance=20000
v3.MinDistance=10000
v3.Volume=1.0
v3.BaseVolume=1.0
#v3.Scale=1.0
v3.SendNotify=0
v3.Play(56000, -18000, -83750,-1)

v4=Bladex.CreateSound("../../Sounds/int-open-wind.wav","v4")
v4.MaxDistance=20000
v4.MinDistance=10000
v4.Volume=1.0
v4.BaseVolume=1.0
#v4.Scale=1.0
v4.SendNotify=0
v4.Play(38000, -18000, -88550,-1)

v5=Bladex.CreateSound("../../Sounds/int-open-wind.wav","v5")
v5.MaxDistance=20000
v5.MinDistance=12000
v5.Volume=1.0
v5.BaseVolume=1.0
#v5.Scale=1.0
v5.SendNotify=0
v5.Play(-45000, -22000, 1000,-1)

v6=Bladex.CreateSound("../../Sounds/int-open-wind.wav","v6")
v6.MaxDistance=20000
v6.MinDistance=10000
v6.Volume=1.0
v6.BaseVolume=1.0
#v6.Scale=1.0
v6.SendNotify=0
v6.Play(-20000, -25000, 2000,-1)

v7=Bladex.CreateSound("../../Sounds/int-open-wind.wav","v7")
v7.MaxDistance=20000
v7.MinDistance=10000
v7.Volume=1.0
v7.BaseVolume=1.0
#v7.Scale=1.0
v7.SendNotify=0
v7.Play(-13700, -26000, 20000,-1)

v8=Bladex.CreateSound("../../Sounds/whistlingwind-thruconduit.wav","v8")
v8.MaxDistance=20000
v8.MinDistance=10000
v8.Volume=1.0
v8.BaseVolume=1.0
#v8.Scale=1.0
v8.SendNotify=0
v8.Play(-34250, -31000, 26500,-1)

##############################
###############Criaturas en el tunel de la antorcha################
############################################################
#############################################

criat1=Sounds.CreatePeriodicSound("../../Sounds/creature-eerie.wav", "criat1",10,5,(-22750,-25000,17300))
criat1.sound.Volume=1
criat1.sound.MinDistance=10000
criat1.sound.MaxDistance=20000
criat1.sound.Volume=1
criat1.sound.BaseVolume=1.0

criat1.sound.SendNotify=0

criat1.PlayPeriodic()

#############################################

criat2=Sounds.CreatePeriodicSound("../../Sounds/bug-laugh.wav", "criat2",10,5,(-23750,-27000,17300))
criat2.sound.Volume=1
criat2.sound.MinDistance=10000
criat2.sound.MaxDistance=20000
criat2.sound.Volume=1
criat2.sound.BaseVolume=1.0

criat2.sound.SendNotify=0

criat2.PlayPeriodic()

#############################################

criat3=Sounds.CreatePeriodicSound("../../Sounds/creature-eerie.wav", "criat3",15,5,(-21750,-26000,17300))
criat3.sound.Volume=1
criat3.sound.MinDistance=10000
criat3.sound.MaxDistance=20000
criat3.sound.Volume=1
criat3.sound.BaseVolume=1.0

criat3.sound.SendNotify=0

criat3.PlayPeriodic()

#############################################
########Recorrido 1. Derrumbamientos#########
#############################################

derr1=Sounds.CreatePeriodicSound("../../Sounds/Stone-floor-collapse.wav", "derr1",15,5,(-154000,-10000,9750))
derr1.sound.Volume=1
derr1.sound.MinDistance=10000
derr1.sound.MaxDistance=20000
derr1.sound.Volume=1
derr1.sound.BaseVolume=1.0

derr1.sound.SendNotify=0

derr1.PlayPeriodic()
#############################################

derr2=Sounds.CreatePeriodicSound("../../Sounds/Stone-floor-collapse.wav", "derr2",10,5,(-159000,-10000,17000))
derr2.sound.Volume=1
derr2.sound.MinDistance=10000
derr2.sound.MaxDistance=20000
derr2.sound.Volume=1
derr2.sound.BaseVolume=1.0

derr2.sound.SendNotify=0

derr2.PlayPeriodic()






###############Recorrido 3. Torre.###############


prec31=Sounds.CreatePeriodicSound("../../Sounds/dist-dungeon-door2.wav", "prec31",10,5,(-20000,-36000,-113000))
prec31.sound.Volume=1
prec31.sound.MinDistance=20000
prec31.sound.MaxDistance=40000
prec31.sound.Volume=1
prec31.sound.BaseVolume=1.0

prec31.sound.SendNotify=0

prec31.PlayPeriodic()

prec32=Sounds.CreatePeriodicSound("../../Sounds/dist-dungeon-door2.wav", "prec32",10,5,(-21000,-25000,-113500))
prec32.sound.Volume=1
prec32.sound.MinDistance=20000
prec32.sound.MaxDistance=40000
prec32.sound.Volume=1
prec32.sound.BaseVolume=1.0

prec32.sound.SendNotify=0

prec32.PlayPeriodic()


###############
######### PRIMER RECORRIDO
#######################

PRIM1=Bladex.CreateSound("../../Sounds/earthquake-loopx.wav","PRIM1")
PRIM1.MaxDistance=40000
PRIM1.MinDistance=30000
PRIM1.Volume=1.0
PRIM1.BaseVolume=1.0
#PRIM1.Scale=1.0
PRIM1.SendNotify=0
PRIM1.Play(-117000, -6000, -28000,-1)

PRIM2=Bladex.CreateSound("../../Sounds/earthquake-loopx.wav","PRIM2")
PRIM2.MaxDistance=40000
PRIM2.MinDistance=30000
PRIM2.Volume=1.0
PRIM2.BaseVolume=1.0
#PRIM2.Scale=1.0
PRIM2.SendNotify=0
PRIM2.Play(-141000, -8000, -20000,-1)

PRIM3=Bladex.CreateSound("../../Sounds/earthquake-loopx.wav","PRIM3")
PRIM3.MaxDistance=40000
PRIM3.MinDistance=30000
PRIM3.Volume=1.0
PRIM3.BaseVolume=1.0
#PRIM3.Scale=1.0
PRIM3.SendNotify=0
PRIM3.Play(-180000, -11000, 47500,-1)

PRIM4=Bladex.CreateSound("../../Sounds/earthquake-loopx.wav","PRIM3")
PRIM4.MaxDistance=40000
PRIM4.MinDistance=30000
PRIM4.Volume=1.0
PRIM4.BaseVolume=1.0
#PRIM4.Scale=1.0
PRIM4.SendNotify=0
PRIM4.Play(-162000, -19000, 16250,-1)


PRIM6=Bladex.CreateSound("../../Sounds/int-open-wind.wav","PRIM6")
PRIM6.MaxDistance=40000
PRIM6.MinDistance=30000
PRIM6.Volume=1.0
PRIM6.BaseVolume=1.0
#PRIM6.Scale=1.0
PRIM6.SendNotify=0
PRIM6.Play(-138000, -10000, 62000,-1)

PRIM7=Bladex.CreateSound("../../Sounds/int-open-wind.wav","PRIM7")
PRIM7.MaxDistance=40000
PRIM7.MinDistance=30000
PRIM7.Volume=1.0
PRIM7.BaseVolume=1.0
#PRIM7.Scale=1.0
PRIM7.SendNotify=0
PRIM7.Play(-124500, -15000, 37500,-1)





PRIM9=Bladex.CreateSound("../../Sounds/whistlingwind-thruconduit.wav","PRIM9")
PRIM9.MaxDistance=40000
PRIM9.MinDistance=30000
PRIM9.Volume=1.0
PRIM9.BaseVolume=1.0
#PRIM9.Scale=1.0
PRIM9.SendNotify=0
PRIM9.Play(-96000, -17000, 9500,-1)


###############
######### MAQUINARIAS DEL SEGUNDO RECORRIDO
#######################


MAQ1=Sounds.CreatePeriodicSound("../../Sounds/creature-eerie.wav", "MAQ1",10,5,(-122000, -21000, -141000))
MAQ1.sound.Volume=1
MAQ1.sound.MinDistance=10000
MAQ1.sound.MaxDistance=30000
MAQ1.sound.Volume=1
MAQ1.sound.BaseVolume=1.0

MAQ1.sound.SendNotify=0

MAQ1.PlayPeriodic()


MAQ2=Bladex.CreateSound("../../Sounds/woodenplatform-loop.wav","MAQ2")
MAQ2.MaxDistance=40000
MAQ2.MinDistance=10000
MAQ2.Volume=0.5
MAQ2.BaseVolume=1.0
#MAQ2.Scale=1.0
MAQ2.SendNotify=0
MAQ2.Play(-133000, -21000, -136000,-1)


MAQ7=Bladex.CreateSound("../../Sounds/int-open-wind.wav","MAQ7")
MAQ7.MaxDistance=40000
MAQ7.MinDistance=10000
MAQ7.Volume=0.5
MAQ7.BaseVolume=1.0
#MAQ7.Scale=1.0
MAQ7.SendNotify=0
MAQ7.Play(-69000, -21000, -127000,-1)


MAQ8=Bladex.CreateSound("../../Sounds/int-open-wind.wav","MAQ8")
MAQ8.MaxDistance=20000
MAQ8.MinDistance=15000
MAQ8.Volume=0.5
MAQ8.BaseVolume=1.0
#MAQ8.Scale=1.0
MAQ8.SendNotify=0
MAQ8.Play(-97500, -21000, -131000,-1)

#######################
############# TERCER RECORRIDO
#####################



TER2=Bladex.CreateSound("../../Sounds/whistlingwind-thruconduit.wav","TER2")
TER2.MaxDistance=40000
TER2.MinDistance=20000
TER2.Volume=1.0
TER2.BaseVolume=1.0
#TER2.Scale=1.0
TER2.SendNotify=0
TER2.Play(-31500, -18000, -151500,-1)


TER3=Bladex.CreateSound("../../Sounds/whistlingwind-thruconduit.wav","TER3")
TER3.MaxDistance=40000
TER3.MinDistance=20000
TER3.Volume=1.0
TER3.BaseVolume=1.0
#TER3.Scale=1.0
TER3.SendNotify=0
TER3.Play(-31500, -19000, -129500,-1)


TER4=Bladex.CreateSound("../../Sounds/whistlingwind-thruconduit.wav","TER4")
TER4.MaxDistance=40000
TER4.MinDistance=20000
TER4.Volume=1.0
TER4.BaseVolume=1.0
#TER4.Scale=1.0
TER4.SendNotify=0
TER4.Play(17500, -18000, -158500,-1)


TER5=Bladex.CreateSound("../../Sounds/earthquake-loopx.wav","TER5")
TER5.MaxDistance=40000
TER5.MinDistance=20000
TER5.Volume=1.0
TER5.BaseVolume=1.0
#TER5.Scale=1.0
TER5.SendNotify=0
TER5.Play(21000, -18000, -172500,-1)


TER6=Bladex.CreateSound("../../Sounds/earthquake-loopx.wav","TER6")
TER6.MaxDistance=40000
TER6.MinDistance=20000
TER6.Volume=1.0
TER6.BaseVolume=1.0
#TER6.Scale=1.0
TER6.SendNotify=0
TER6.Play(12700, -18000, -144000,-1)

############
###### TERCER RECORRIDO ACIDO


TERAC1=Bladex.CreateSound("../../Sounds/underwater-atmos1.wav","TERAC1")
TERAC1.MaxDistance=40000
TERAC1.MinDistance=20000
TERAC1.Volume=1.0
TERAC1.BaseVolume=1.0
#TERAC1.Scale=1.0
TERAC1.SendNotify=0
TERAC1.Play(128700, 5000, -159000,-1)

TERAC2=Bladex.CreateSound("../../Sounds/underwater-atmos1.wav","TERAC2")
TERAC2.MaxDistance=40000
TERAC2.MinDistance=20000
TERAC2.Volume=1.0
TERAC2.BaseVolume=1.0
#TERAC2.Scale=1.0
TERAC2.SendNotify=0
TERAC2.Play(146700, 1000, -164000,-1)




#############################final,final,final
#############################
#############################

fina1=Bladex.CreateSound("../../Sounds/whistlingwind-thruconduit.wav","fina1")
fina1.MaxDistance=40000
fina1.MinDistance=20000
fina1.Volume=1.0
fina1.BaseVolume=1.0
#fina1.Scale=1.0
fina1.SendNotify=0
fina1.Play(98839.6208093, 22382.9929808, 27611.554,-1)

#############################

fina2=Bladex.CreateSound("../../Sounds/whistlingwind-thruconduit.wav","fina2")
fina2.MaxDistance=40000
fina2.MinDistance=20000
fina2.Volume=1.0
fina2.BaseVolume=1.0
#fina2.Scale=1.0
fina2.SendNotify=0
fina2.Play(133748.92239, 16226.7648847, 28690.93995,-1)