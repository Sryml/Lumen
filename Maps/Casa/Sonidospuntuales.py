import Sounds
import Bladex



########################################
###  RANAS                          ####
#######################################
###1
#sp1=Bladex.CreateSound("../../Sounds/frog-bg.wav","cricri")
#sp1.MaxDistance=20000
#sp1.MinDistance=3000
#sp1.Volume=0.7
#sp1.BaseVolume=1.0
#sp1.SendNotify=0
#sp1.Play(130000, 7000, -86000,-1)

###2
#sp2=Bladex.CreateSound("../../Sounds/bg-swamp-crickets.wav","crocro")
#sp2.MaxDistance=20000
#sp2.MinDistance=3000
#sp2.Volume=0.7
#sp2.BaseVolume=1.0
#sp2.SendNotify=0
#sp2.Play(121000, 10000, -67000,-1)


###2
##sp4=Sounds.CreatePeriodicSound("../../Sounds/creature-eerie2.wav", "grr2",11,5,(143300, 10000, -44000))
#sp4.Volume=1
#sp4.MinDistance=3000
#sp4.MaxDistance=100000
#sp4.Volume=1
#sp4.BaseVolume=1.0
#sp4.SendNotify=0

#sp4.PlayPeriodic()




#######################################
###  fuego dentro de la casa       ####
#######################################


###1
sff1=Bladex.CreateSound("../../Sounds/fuego-pequeno.wav","fff")
sff1.MaxDistance=11000
sff1.MinDistance=2000
sff1.Volume=0.7
sff1.BaseVolume=1.0
sff1.SendNotify=0
sff1.Play(15000,-100,11500,-1)


####################################
###cuervos
####################################

###2
sph2=Sounds.CreatePeriodicSound("../../Sounds/cuervo-graznido.wav", "bhuuh",8,4,(18000, -3000, 25000))
sph2.Volume=0.8
sph2.MinDistance=1000
sph2.MaxDistance=5000
sph2.BaseVolume=1.0
sph2.SendNotify=0
sph2.PlayPeriodic()

###3
sph3=Sounds.CreatePeriodicSound("../../Sounds/crow-fly1.wav", "bhuhh",10,5,(21000, -3000, 22000))
sph3.Volume=0.8
sph3.MinDistance=900
sph3.MaxDistance=6000
sph3.BaseVolume=1.0
sph3.SendNotify=0

sph3.PlayPeriodic()

###4
sp4=Sounds.CreatePeriodicSound("../../Sounds/crow-calls1.wav", "grr2",7,4,(12000, -3000, 20000))
sp4.Volume=1
sp4.MinDistance=1000
sp4.MaxDistance=60000
sp4.Volume=1
sp4.BaseVolume=1.0
sp4.SendNotify=0

sp4.PlayPeriodic()
