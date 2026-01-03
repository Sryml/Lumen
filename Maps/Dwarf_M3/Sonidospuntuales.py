

import Sounds
import Bladex



########################################
###  RANAS                          ####
#######################################
###1
sp1=Bladex.CreateSound("../../Sounds/frog-bg.wav","cricri")
sp1.MaxDistance=20000
sp1.MinDistance=3000
sp1.Volume=0.9
sp1.BaseVolume=1.0
sp1.SendNotify=0
sp1.Play(130000, 7000, -86000,-1)

###2
#sp2=Bladex.CreateSound("../../Sounds/bg-swamp-crickets.wav","crocro")
sp2=Bladex.CreateSound("../../Sounds/frog-bg.wav","crocro")
sp2.MaxDistance=20000
sp2.MinDistance=3000
sp2.Volume=0.9
sp2.BaseVolume=1.0
sp2.SendNotify=0
sp2.Play(121000, 9000, -67000,-1)

#######################
###--bicho-raro---#####
#######################
###1
sp3=Sounds.CreatePeriodicSound("../../Sounds/creature-eerie.wav", "grr",10,5,(143000, 9500, -42000))
sp3.sound.Volume=1
sp3.sound.MinDistance=6000
sp3.sound.MaxDistance=40000
sp3.sound.Volume=1
sp3.sound.BaseVolume=1.0
sp3.sound.SendNotify=0

sp3.PlayPeriodic()

###2
sp4=Sounds.CreatePeriodicSound("../../Sounds/creature-eerie2.wav", "grr2",11,5,(143300, 9500, -44000))
sp4.sound.Volume=1
sp4.sound.MinDistance=6000
sp4.sound.MaxDistance=40000
sp4.sound.Volume=1
sp4.sound.BaseVolume=1.0
sp4.sound.SendNotify=0

sp4.PlayPeriodic()

###2
sp4=Sounds.CreatePeriodicSound("../../Sounds/creature-eerie.wav", "grr2",11,7,(143300, 9500, -22000))
sp4.sound.Volume=1
sp4.sound.MinDistance=5000
sp4.sound.MaxDistance=50000
sp4.sound.Volume=1
sp4.sound.BaseVolume=1.0
sp4.sound.SendNotify=0

sp4.PlayPeriodic()




####################################
####    ROTURAS                 ####
####################################

####   en-galeria-antes-de-la-sala-rota   ####
"""
blam=Sounds.CreatePeriodicSound("../../Sounds/Rock-floor-collapse.wav", "blam",15,8,(-40000, -10000, -24500))
blam.sound.Volume=1
blam.sound.MinDistance=10000
blam.sound.MaxDistance=100000
blam.sound.Volume=1
blam.sound.BaseVolume=1.0
blam.sound.sound.Scale=10.0
blam.sound.SendNotify=0
blam.PlayPeriodic()
"""

#######################################
###  fuego primera pira            ####
#######################################
###1
sff1=Bladex.CreateSound("../../Sounds/Fire-curtains.wav","fff")
sff1.MaxDistance=20000
sff1.MinDistance=2000
sff1.Volume=0.9
sff1.BaseVolume=1.0
sff1.SendNotify=0
sff1.Play(67104.489334,-600,-51714,-1)


"""
#######################################
###  fuego pira sala final         ####
#######################################
###1
sff2=Bladex.CreateSound("../../Sounds/Fire-curtains.wav","fff1")
sff2.MaxDistance=20000
sff2.MinDistance=2000
sff2.Volume=0.9
sff2.BaseVolume=1.0
sff2.SendNotify=0
sff2.Play(-210000,-15800,14500,-1)

#######################################
###  fuego pira sala ROTA  1       ####
#######################################
###1
sff3=Bladex.CreateSound("../../Sounds/Fire-curtains.wav","fff2")
sff3.MaxDistance=10000
sff3.MinDistance=2000
sff3.Volume=0.8
sff3.BaseVolume=1.0
sff3.SendNotify=0
sff3.Play(-48500,-11500,-43000,-1)

#######################################
###  fuego pira sala ROTA  2       ####
#######################################
###1
sff4=Bladex.CreateSound("../../Sounds/Fire-curtains.wav","fff3")
sff4.MaxDistance=16000
sff4.MinDistance=1500
sff4.Volume=0.8
sff4.BaseVolume=1.0
sff4.Scale=1.0
sff4.SendNotify=0
sff4.Play(-66500,-16000,-8800,-1)
"""

##########################################
####------sonidos-salon-de-reyes-----#####
##########################################

###1
sph1=Sounds.CreatePeriodicSound("../../Sounds/spirits.wav", "bhuuu",11,7,(-55000, -13000, -118500))
sph1.sound.Volume=1
sph1.sound.MinDistance=3000
sph1.sound.MaxDistance=15000
sph1.sound.BaseVolume=1
sph1.sound.SendNotify=0

sph1.PlayPeriodic()


###2
#sph2=Sounds.CreatePeriodicSound("../../Sounds/small-waterfall.wav", "bhuuh",11,7,(-36200, -13000, -112500))
sph2=Sounds.CreatePeriodicSound("../../Sounds/spirits.wav", "bhuuh",11,7,(-36200, -13000, -112500))
sph2.sound.Volume=1
sph2.sound.MinDistance=3300
sph2.sound.MaxDistance=15000
sph2.sound.BaseVolume=1.0
sph2.sound.SendNotify=0

sph2.PlayPeriodic()

###3
sph3=Sounds.CreatePeriodicSound("../../Sounds/spirits2.wav", "bhuhh",11,7,(-66000, -13000, -113000))
sph3.sound.Volume=1
sph3.sound.MinDistance=3000
sph3.sound.MaxDistance=15000
sph3.sound.BaseVolume=1.0
sph3.sound.SendNotify=0

sph3.PlayPeriodic()

###################################################
###---CONDUCTOS-DE-VENTILACION-SALA-SECRETA----####
###################################################
###1
sV1=Bladex.CreateSound("../../Sounds/viento-ventana.wav","ffsHH")
sV1.MaxDistance=15000
sV1.MinDistance=1000
sV1.Volume=1
sV1.BaseVolume=1.0
sV1.SendNotify=0
sV1.Play(-38200,-8100,7500,-1)

###2
sV2=Bladex.CreateSound("../../Sounds/viento-ventana.wav","ffssHH")
sV2.MaxDistance=15000
sV2.MinDistance=1000
sV2.Volume=1
sV2.BaseVolume=1.0
sV2.SendNotify=0
sV2.Play(-38200,-8100,500,-1)

###################################################
###---CONDUCTOS-DE-VENTILACION-PASILLO---------####
###################################################

###1
sV3=Bladex.CreateSound("../../Sounds/whistlingwind-thruconduit.wav","fsssHH")
sV3.MaxDistance=20000
sV3.MinDistance=1000
sV3.Volume=1
sV3.BaseVolume=1.0
sV3.SendNotify=0

sV3.Play(-72750,-10200,13500,-1)

###2
sV4=Bladex.CreateSound("../../Sounds/whistlingwind-thruconduit.wav","ffssssH")
sV4.MaxDistance=20000
sV4.MinDistance=3000
sV4.Volume=1
sV4.BaseVolume=1.0
sV4.SendNotify=0
sV4.Play(-80000,-10200,13500,-1)

###################################################
###---------------fuente inicio----------------####
###################################################

###1
sV5=Bladex.CreateSound("../../Sounds/small-waterfall.wav","fgfgfgfgHH")
sV5.MaxDistance=20000
sV5.MinDistance=1000
sV5.Volume=0.3
sV5.BaseVolume=1
sV5.SendNotify=0

sV5.Play(53000,4000,-114000,-1)

################################################################################################
#
###	SONIDOS MISTERIO POR EL CAMINO
#1
blam2=Sounds.CreatePeriodicSound("../../Sounds/rocas-eco.wav", "blam",15,8,(33000, -3000, -50000))
blam2.sound.Volume=1
blam2.sound.MinDistance=7000
blam2.sound.MaxDistance=40000
blam2.sound.Volume=1
blam2.sound.BaseVolume=1.0
blam2.sound.SendNotify=0

blam2.PlayPeriodic()

#2
blam3=Sounds.CreatePeriodicSound("../../Sounds/Rock-crack.wav", "blam",15,8,(-44000, -10000, 6000))
blam3.sound.Volume=1
blam3.sound.MinDistance=7000
blam3.sound.MaxDistance=40000
blam3.sound.Volume=1
blam3.sound.BaseVolume=1.0
blam3.sound.SendNotify=0

blam3.PlayPeriodic()

#3
blam4=Sounds.CreatePeriodicSound("../../Sounds/rocas-eco.wav", "blam",15,8,(-122000, -6000, -47000))
blam4.sound.Volume=1
blam4.sound.MinDistance=7000
blam4.sound.MaxDistance=40000
blam4.sound.Volume=1
blam4.sound.BaseVolume=1.0
blam4.sound.SendNotify=0

blam4.PlayPeriodic()


#4
blam5=Sounds.CreatePeriodicSound("../../Sounds/Rock-crack.wav", "blam",15,8,(-95000, -8000, -71000))
blam5.sound.Volume=1
blam5.sound.MinDistance=7000
blam5.sound.MaxDistance=40000
blam5.sound.Volume=1
blam5.sound.BaseVolume=1.0
blam5.sound.SendNotify=0

blam5.PlayPeriodic()