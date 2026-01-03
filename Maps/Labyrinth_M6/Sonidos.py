import Bladex
import Sounds
import ReadGSFile



ReadGSFile.ProcessGhostSectorFile("sonidos.sf")




############ SONIDOS AMBIENTE AGUA


gotalc1=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-1.wav", "Gotalc1",6,3,(5500, 5000, -15500))
gotalc1.sound.Volume=0.7
gotalc1.sound.MinDistance=500
gotalc1.sound.MaxDistance=5000
gotalc1.sound.BaseVolume=1.0
gotalc1.sound.SendNotify=0
gotalc1.PlayPeriodic()


gotalc2=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-2.wav", "Gotalc2",8,4,(1500, 5000, -18000))
gotalc2.sound.Volume=0.9
gotalc2.sound.MinDistance=500
gotalc2.sound.MaxDistance=5000
gotalc2.sound.BaseVolume=1.0
gotalc2.sound.SendNotify=0
gotalc2.PlayPeriodic()


gotalc3=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-3.wav", "Gotalc3",6,3,(-2000, 5000, -21000))
gotalc3.sound.Volume=0.9
gotalc3.sound.MinDistance=500
gotalc3.sound.MaxDistance=5000
gotalc3.sound.BaseVolume=1.0
gotalc3.sound.SendNotify=0
gotalc3.PlayPeriodic()


gotalc4=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-1.wav", "Gotalc4",8,4,(1500, 5000, -25500))
gotalc4.sound.Volume=0.7
gotalc4.sound.MinDistance=500
gotalc4.sound.MaxDistance=5000
gotalc4.sound.BaseVolume=1.0
gotalc4.sound.SendNotify=0
gotalc4.PlayPeriodic()


gotalc5=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-2.wav", "Gotalc5",6,3,(-2500, 5000, -29000))
gotalc5.sound.Volume=0.9
gotalc5.sound.MinDistance=500
gotalc5.sound.MaxDistance=5000
gotalc5.sound.BaseVolume=1.0
gotalc5.sound.SendNotify=0
gotalc5.PlayPeriodic()


gotalc6=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-3.wav", "Gotalc6",8,4,(2000, 5000, -33500))
gotalc6.sound.Volume=0.9
gotalc6.sound.MinDistance=500
gotalc6.sound.MaxDistance=5000
gotalc6.sound.BaseVolume=1.0
gotalc6.sound.SendNotify=0
gotalc6.PlayPeriodic()


gotalc7=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-1.wav", "Gotalc7",6,3,(5500, 5000, -29000))
gotalc7.sound.Volume=0.7
gotalc7.sound.MinDistance=500
gotalc7.sound.MaxDistance=5000
gotalc7.sound.BaseVolume=1.0
gotalc7.sound.SendNotify=0
gotalc7.PlayPeriodic()


gotalc8=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-2.wav", "Gotalc8",8,4,(11500, 5000, -26000))
gotalc8.sound.Volume=0.9
gotalc8.sound.MinDistance=500
gotalc8.sound.MaxDistance=5000
gotalc8.sound.BaseVolume=1.0
gotalc8.sound.SendNotify=0
gotalc8.PlayPeriodic()


gotalc9=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-3.wav", "Gotalc9",6,3,(13500, 11250, -24000))
gotalc9.sound.Volume=1
gotalc9.sound.MinDistance=500
gotalc9.sound.MaxDistance=5000
gotalc9.sound.BaseVolume=1.0
gotalc9.sound.SendNotify=0
gotalc9.PlayPeriodic()


gotalc10=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-1.wav", "Gotalc10",4,2,(14500, 11250, -25500))
gotalc10.sound.Volume=1
gotalc10.sound.MinDistance=500
gotalc10.sound.MaxDistance=5000
gotalc10.sound.BaseVolume=1.0
gotalc10.sound.SendNotify=0
gotalc10.PlayPeriodic()


gotalc10=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-2.wav", "Gotalc10",6,3,(-1000, 5000, -37000))
gotalc10.sound.Volume=0.9
gotalc10.sound.MinDistance=500
gotalc10.sound.MaxDistance=5000
gotalc10.sound.BaseVolume=1.0
gotalc10.sound.SendNotify=0
gotalc10.PlayPeriodic()


gotalc10=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-3.wav", "Gotalc10",8,4,(-1500, 5000, -40000))
gotalc10.sound.Volume=0.9
gotalc10.sound.MinDistance=500
gotalc10.sound.MaxDistance=5000
gotalc10.sound.BaseVolume=1.0
gotalc10.sound.SendNotify=0
gotalc10.PlayPeriodic()


gotalc10=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-1.wav", "Gotalc10",6,3,(-1000, 5000, -43500))
gotalc10.sound.Volume=0.7
gotalc10.sound.MinDistance=500
gotalc10.sound.MaxDistance=5000
gotalc10.sound.BaseVolume=1.0
gotalc10.sound.SendNotify=0
gotalc10.PlayPeriodic()


gotalc10=Sounds.CreatePeriodicSound("../../Sounds/gota-caverna-agua-2.wav", "Gotalc10",8,4,(1000, 5000, -48000))
gotalc10.sound.Volume=0.9
gotalc10.sound.MinDistance=500
gotalc10.sound.MaxDistance=5000
gotalc10.sound.BaseVolume=1.0
gotalc10.sound.SendNotify=0
gotalc10.PlayPeriodic()




############ SONIDOS AMBIENTE HALCONES


halcon1=Sounds.CreatePeriodicSound("../../Sounds/pajaro1.wav", "Halcon1",24,12,(-50000, -25000, 9000))
halcon1.sound.Volume=1
halcon1.sound.MinDistance=10000
halcon1.sound.MaxDistance=22000
halcon1.sound.BaseVolume=1.0
halcon1.sound.SendNotify=0
halcon1.PlayPeriodic()


halcon2=Sounds.CreatePeriodicSound("../../Sounds/pajaro2.wav", "Halcon2",30,15,(-13000, -38000, 29000))
halcon2.sound.Volume=1
halcon2.sound.MinDistance=10000
halcon2.sound.MaxDistance=30000
halcon2.sound.BaseVolume=1.0
halcon2.sound.SendNotify=0
halcon2.PlayPeriodic()


halcon3=Sounds.CreatePeriodicSound("../../Sounds/pajaro1.wav", "Halcon3",24,12,(29000, -38000, 13000))
halcon3.sound.Volume=1
halcon3.sound.MinDistance=10000
halcon3.sound.MaxDistance=30000
halcon3.sound.BaseVolume=1.0
halcon3.sound.SendNotify=0
halcon3.PlayPeriodic()


halcon4=Sounds.CreatePeriodicSound("../../Sounds/pajaro2.wav", "Halcon4",30,15,(-7000, -25000, -66000))
halcon4.sound.Volume=1
halcon4.sound.MinDistance=10000
halcon4.sound.MaxDistance=22000
halcon4.sound.BaseVolume=1.0
halcon4.sound.SendNotify=0
halcon4.PlayPeriodic()


halcon5=Sounds.CreatePeriodicSound("../../Sounds/pajaro1.wav", "Halcon5",24,12,(-19000, -25000, -24000))
halcon5.sound.Volume=1
halcon5.sound.MinDistance=10000
halcon5.sound.MaxDistance=22000
halcon5.sound.BaseVolume=1.0
halcon5.sound.SendNotify=0
halcon5.PlayPeriodic()


halcon6=Sounds.CreatePeriodicSound("../../Sounds/pajaro2.wav", "Halcon6",30,15,(30000, -25000, -32000))
halcon6.sound.Volume=1
halcon6.sound.MinDistance=10000
halcon6.sound.MaxDistance=22000
halcon6.sound.BaseVolume=1.0
halcon6.sound.SendNotify=0
halcon6.PlayPeriodic()
