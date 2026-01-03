import Sounds
import Bladex





chorrillo1=Bladex.CreateSound("../../Sounds/agua-canal.wav","chorrillo11111")
chorrillo1.MaxDistance=7000
chorrillo1.MinDistance=2000
chorrillo1.Volume=1.0
chorrillo1.BaseVolume=1.0
#chorrillo1.Scale=1.0
chorrillo1.SendNotify=0
chorrillo1.Play(-78536.7672903, 14378.6115015, 60657.4405,-1)



#####--quejidos de las mazmorras--######

quejido1=Sounds.CreatePeriodicSound("../../Sounds/torture-scream2.wav", "quejido1",30,5,(-123500,7000,85500))
quejido1.sound.Volume=1
quejido1.sound.MinDistance=100
quejido1.sound.MaxDistance=20000
quejido1.sound.Volume=1
quejido1.sound.BaseVolume=1.0

quejido1.sound.SendNotify=0

quejido1.PlayPeriodic()



quejido2=Sounds.CreatePeriodicSound("../../Sounds/torture-scream2.wav", "quejido2",25,5,(-107000,13000,89500))
quejido2.sound.Volume=1
quejido2.sound.MinDistance=5000
quejido2.sound.MaxDistance=20000
quejido2.sound.Volume=1
quejido2.sound.BaseVolume=1.0

quejido2.sound.SendNotify=0

quejido2.PlayPeriodic()



quejido3=Sounds.CreatePeriodicSound("../../Sounds/torture-scream2.wav", "quejido3",25,5,(-104000,12000,88000))
quejido3.sound.Volume=1
quejido3.sound.MinDistance=1000
quejido3.sound.MaxDistance=20000
quejido3.sound.Volume=1
quejido3.sound.BaseVolume=1.0

quejido3.sound.SendNotify=0

quejido3.PlayPeriodic()






#####--lobo del 1er patio--######




lobo1=Sounds.CreatePeriodicSound("../../Sounds/wolf-howl2.wav", "lobo1",20,5,(-61000,-5000,56000))
lobo1.sound.Volume=1
lobo1.sound.MinDistance=1000
lobo1.sound.MaxDistance=20000
lobo1.sound.Volume=1
lobo1.sound.BaseVolume=1.0

lobo1.sound.SendNotify=0

lobo1.PlayPeriodic()




lobo2=Sounds.CreatePeriodicSound("../../Sounds/wolf-howl2.wav", "lobo2",10,5,(-63000,-5000,57000))
lobo2.sound.Volume=1
lobo2.sound.MinDistance=1000
lobo2.sound.MaxDistance=20000
lobo2.sound.Volume=1
lobo2.sound.BaseVolume=1.0

lobo2.sound.SendNotify=0

lobo2.PlayPeriodic()

########lobos antes del puente levadizo#############



lobo3=Sounds.CreatePeriodicSound("../../Sounds/wolf-howl2.wav", "lobo3",10,5,(-139500,-8000,-24500))
lobo3.sound.Volume=1
lobo3.sound.MinDistance=1000
lobo3.sound.MaxDistance=20000
lobo3.sound.Volume=0.5
lobo3.sound.BaseVolume=1.0

lobo3.sound.SendNotify=0

lobo3.PlayPeriodic()

#########
lobo4=Sounds.CreatePeriodicSound("../../Sounds/wolf-howl2.wav", "lobo4",10,5,(-139000,-8000,-24000))
lobo4.sound.Volume=1
lobo4.sound.MinDistance=1000
lobo4.sound.MaxDistance=20000
lobo4.sound.Volume=0.6
lobo4.sound.BaseVolume=1.0

lobo4.sound.SendNotify=0

lobo4.PlayPeriodic()

###al otro lado######

lobo5=Sounds.CreatePeriodicSound("../../Sounds/wolf-howl2.wav", "lobo5",15,2,(-67000,-8000,-15000))
lobo5.sound.Volume=1
lobo5.sound.MinDistance=1000
lobo5.sound.MaxDistance=20000
lobo5.sound.Volume=0.5
lobo5.sound.BaseVolume=1.0

lobo5.sound.SendNotify=0

lobo5.PlayPeriodic()

#########
lobo6=Sounds.CreatePeriodicSound("../../Sounds/wolf-howl2.wav", "lobo6",10,5,(-67000,-9000,-15500))
lobo6.sound.Volume=1
lobo6.sound.MinDistance=1000
lobo6.sound.MaxDistance=20000
lobo6.sound.Volume=0.6
lobo6.sound.BaseVolume=1.0

lobo6.sound.SendNotify=0

lobo6.PlayPeriodic()

#########Lobos del puente levadizo##############

lobo7=Sounds.CreatePeriodicSound("../../Sounds/wolf-howl2.wav", "lobo7",10,5,(-119000,0,-65000))
lobo7.sound.Volume=1
lobo7.sound.MinDistance=1000
lobo7.sound.MaxDistance=20000
lobo7.sound.Volume=0.6
lobo7.sound.BaseVolume=1.0

lobo7.sound.SendNotify=0

lobo7.PlayPeriodic()

#########

#lobo8=Sounds.CreatePeriodicSound("../../Sounds/wolf-howl2.wav", "lobo8",10,5,(-119500,0,-65500))
#lobo8.sound.Volume=0.6
#lobo8.sound.MinDistance=1000
#lobo8.sound.MaxDistance=20000
#lobo8.sound.Volume=1
#lobo8.sound.BaseVolume=1.0
#lobo8.sound.Scale=1.0
#lobo8.sound.SendNotify=0

#lobo8.PlayPeriodic()