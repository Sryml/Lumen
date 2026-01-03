import Sounds
import Bladex
import ReadGSFile



ReadGSFile.ProcessGhostSectorFile("ambiente.sf")


############ SONIDOS PUNTUALES AGUA EN CALMA


## AGUA PATIO ARCOS


patio1=Sounds.CreatePeriodicSound("../../Sounds/Swimstroke1.wav", "patio1",25,5,(352000, 1400, -172000))
patio1.Volume=0.05
patio1.MinDistance=500
patio1.MaxDistance=1000
patio1.BaseVolume=1.0
patio1.Scale=1.0
patio1.SendNotify=0
patio1.PlayPeriodic()



patio2=Sounds.CreatePeriodicSound("../../Sounds/Swimstroke1.wav", "patio2",15,10,(360000, 1400, -187000))
patio2.Volume=0.05
patio2.MinDistance=500
patio2.MaxDistance=1000
patio2.BaseVolume=1.0
patio2.Scale=1.0
patio2.SendNotify=0
patio2.PlayPeriodic()

patio3=Sounds.CreatePeriodicSound("../../Sounds/Swimstroke1.wav", "patio3",15,5,(350000, 1400, -183000))
patio3.Volume=0.05
patio3.MinDistance=500
patio3.MaxDistance=1000
patio3.BaseVolume=1.0
patio3.Scale=1.0
patio3.SendNotify=0
patio3.PlayPeriodic()


## AGUA BA�OS

termas=Sounds.CreatePeriodicSound("../../Sounds/Swimstroke1.wav", "termas",25,5,(364000, 1500, -204000))
termas.Volume=0.05
termas.MinDistance=500
termas.MaxDistance=1000
termas.BaseVolume=1.0
termas.Scale=1.0
termas.SendNotify=0
termas.PlayPeriodic()


## SONIDOS PUNTUALES RAFAGAS VIENTO EXTERIOR


rafaga1=Sounds.CreatePeriodicSound("../../Sounds/highalt-wind2.wav", "rafaga1",30,5,(326258,-2837,-202710))
rafaga1.sound.Volume=0.8
rafaga1.sound.MinDistance=1000
rafaga1.sound.MaxDistance=7000
rafaga1.sound.BaseVolume=1.0
rafaga1.sound.SendNotify=0
rafaga1.PlayPeriodic()




rafaga2=Sounds.CreatePeriodicSound("../../Sounds/highalt-wind2.wav", "rafaga2",40,5,(299785,4463,-225084))
rafaga2.sound.Volume=0.5
rafaga2.sound.MinDistance=5000
rafaga2.sound.MaxDistance=15000
rafaga2.sound.BaseVolume=1.0
rafaga2.sound.SendNotify=0
rafaga2.PlayPeriodic()



rafaga3=Sounds.CreatePeriodicSound("../../Sounds/highalt-wind2.wav", "rafaga3",30,5,(343822,-3881,-161421))
rafaga3.sound.Volume=0.7
rafaga3.sound.MinDistance=5000
rafaga3.sound.MaxDistance=15000
rafaga3.sound.BaseVolume=1.0
rafaga3.sound.SendNotify=0
rafaga3.PlayPeriodic()



rafaga4=Sounds.CreatePeriodicSound("../../Sounds/highalt-wind2.wav", "rafaga4",35,5,(317808,14261,-105096))
rafaga4.sound.Volume=0.7
rafaga4.sound.MinDistance=5000
rafaga4.sound.MaxDistance=15000
rafaga4.sound.BaseVolume=1.0
rafaga4.sound.SendNotify=0
rafaga4.PlayPeriodic()



rafaga5=Sounds.CreatePeriodicSound("../../Sounds/highalt-wind2.wav", "rafaga5",50,5,(317243,34107,-115705))
rafaga5.sound.Volume=0.7
rafaga5.sound.MinDistance=5000
rafaga5.sound.MaxDistance=15000
rafaga5.sound.BaseVolume=1.0
rafaga5.sound.SendNotify=0
rafaga5.PlayPeriodic()



rafaga6=Sounds.CreatePeriodicSound("../../Sounds/highalt-wind2.wav", "rafaga6",25,5,(375695,34090,41123))
rafaga6.sound.Volume=0.7
rafaga6.sound.MinDistance=5000
rafaga6.sound.MaxDistance=15000
rafaga6.sound.BaseVolume=1.0
rafaga6.sound.SendNotify=0
rafaga6.PlayPeriodic()



rafaga7=Sounds.CreatePeriodicSound("../../Sounds/highalt-wind2.wav", "rafaga7",35,5,(442902,46068,18026))
rafaga7.sound.Volume=0.7
rafaga7.sound.MinDistance=5000
rafaga7.sound.MaxDistance=10000
rafaga7.sound.BaseVolume=1.0
rafaga7.sound.SendNotify=0
rafaga7.PlayPeriodic()
