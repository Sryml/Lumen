import Sounds
import Bladex

#####--pajarico delante de la primera caseta---######

s=Bladex.CreateSound("../../Sounds/Rainforest-bird4.wav","pipi1")
s.MaxDistance=20000
s.MinDistance=2000
s.Volume=1.0
s.BaseVolume=1.0
s.SendNotify=0

s.Play(-148000, -4000, -20000,-1)


#####--cascada + pequenia en la primera cascada---######

s2=Bladex.CreateSound("../../Sounds/small-waterfall.wav","cascada1")
s2.MaxDistance=40000
s2.MinDistance=600
s2.Volume=1.0
s2.BaseVolume=1.0
s2.SendNotify=0

s2.Play(-165000, -100, -77000,-1)


#####-pipi grande al principio del nivel-#####

eagle=Sounds.CreatePeriodicSound("../../Sounds/eagle-screech.wav", "pipi2",15,8,(-150000, 9000, -94000))
eagle.sound.Volume=1
eagle.sound.MinDistance=1000
eagle.sound.MaxDistance=50000
eagle.sound.Volume=1
eagle.sound.BaseVolume=1.0
eagle.sound.SendNotify=0

eagle.PlayPeriodic()


#####-cuervos en nido en acantilado-#####

crow1=Sounds.CreatePeriodicSound("../../Sounds/cuervo-graznido.wav", "pipi3",15,9,(320000, -26000, 61000))
crow1.sound.Volume=1
crow1.sound.MinDistance=100
crow1.sound.MaxDistance=40000
crow1.sound.Volume=1
crow1.sound.BaseVolume=1.0
crow1.sound.SendNotify=0

crow1.PlayPeriodic()



s3=Bladex.CreateSound("../../Sounds/ext-bg-crows.wav","pipis1")
s3.MaxDistance=28000
s3.MinDistance=2000
s3.Volume=1.0
s3.BaseVolume=1.0
s3.SendNotify=0

s3.Play(38000, -25000, 60000,-1)


########################################
###  grillos                        ####
#######################################


#s4=Bladex.CreateSound("../../Sounds/bg-swamp-crickets.wav","cricri")
s4=Bladex.CreateSound("../../Sounds/frog-bg.wav","cricri")
s4.MaxDistance=29000
s4.MinDistance=2000
s4.Volume=0.9
s4.BaseVolume=1.0
s4.SendNotify=0

s4.Play(-83000, -9500, 84000,-1)

#######################################
###  viento gruta interior        ####
#######################################

s5=Bladex.CreateSound("../../Sounds/Light-clifftop-wind.wav","gluglu")
s5.MaxDistance=50000
s5.MinDistance=2000
s5.Volume=0.8
s5.BaseVolume=1.0
s5.SendNotify=0

s5.Play(9000, -25000, -114000,-1)
