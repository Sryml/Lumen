import Sounds
import Bladex


## CUERVOS


cuervos1=Sounds.CreatePeriodicSound("../../Sounds/cuervo-graznido.wav", "cuervos1",20,5,(-26000,-20000,28000))
cuervos1.Volume=0.05
cuervos1.MinDistance=500
cuervos1.MaxDistance=1000
cuervos1.BaseVolume=1.0
cuervos1.Scale=1.0
cuervos1.SendNotify=0
cuervos1.PlayPeriodic()


cuervos2=Sounds.CreatePeriodicSound("../../Sounds/cuervo-graznido.wav", "cuervos2",15,5,(-17000,-17000,27000))
cuervos2.Volume=0.05
cuervos2.MinDistance=500
cuervos2.MaxDistance=1000
cuervos2.BaseVolume=1.0
cuervos2.Scale=1.0
cuervos2.SendNotify=0
cuervos2.PlayPeriodic()


cuervos3=Sounds.CreatePeriodicSound("../../Sounds/cuervo-graznido.wav", "cuervos2",25,5,(-31000,-16000,26000))
cuervos3.Volume=0.05
cuervos3.MinDistance=500
cuervos3.MaxDistance=1000
cuervos3.BaseVolume=1.0
cuervos3.Scale=1.0
cuervos3.SendNotify=0
cuervos3.PlayPeriodic()
