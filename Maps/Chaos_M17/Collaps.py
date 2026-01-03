import Bladex
import AuxFuncs
import dust

Bladex.CreateTimer("Timer10",1.0/10.0)


derrumbesuelopiedra=Bladex.CreateSound("../../Sounds/ground-collapse.wav", "DerrumbeSueloPiedra")
derrumbesuelopiedra.Volume=1
derrumbesuelopiedra.MinDistance=10000
derrumbesuelopiedra.MaxDistance=40000

derrumbesuelopiedra2=Bladex.CreateSound("../../Sounds/CAIDAS-PIEDRAS-2.wav", "DerrumbeSueloPiedra2")
derrumbesuelopiedra2.Volume=1
derrumbesuelopiedra2.MinDistance=10000
derrumbesuelopiedra2.MaxDistance=40000

derrumbesuelopiedra3=Bladex.CreateSound("../../Sounds/terremoto-piedras.wav", "DerrumbeSueloPiedra3")
derrumbesuelopiedra3.Volume=1
derrumbesuelopiedra3.MinDistance=10000
derrumbesuelopiedra3.MaxDistance=40000

derrumbesuelopiedra4=Bladex.CreateSound("../../Sounds/ground-collapse.wav", "DerrumbeSueloPiedra4")
derrumbesuelopiedra4.Volume=1
derrumbesuelopiedra4.MinDistance=10000
derrumbesuelopiedra4.MaxDistance=40000

derrumbesuelopiedra5=Bladex.CreateSound("../../Sounds/ground-collapse.wav", "DerrumbeSueloPiedra5")
derrumbesuelopiedra5.Volume=1
derrumbesuelopiedra5.MinDistance=10000
derrumbesuelopiedra5.MaxDistance=40000


### derrumbamientos zona abierta primer tramo

derrumbe1=Bladex.GetSector(273850, -3000, -19750)
derrumbe1.Active=0


derrumbe1.InitBreak((0.0, 6000.0, 0.0), (4800.0, 0.0, 800.0), (500.0, 0.0, 4000.0),"",100.0,0)

sectorderrumbe1=Bladex.GetSector(278000, -7000, -17250)

sectorderrumbe1.OnEnter=Derrumbe1



derrumbe1b=Bladex.GetSector(270000,-2000,-37000)
derrumbe1b.Active=0


derrumbe1b.InitBreak((0.0, 6000.0, 0.0), (4800.0, 0.0, 800.0), (500.0, 0.0, 4000.0),"",100.0,0)

sectorderrumbe1b=Bladex.GetSector(282000,-7000,-17000)

sectorderrumbe1b.OnEnter=Derrumbe1b



## derrumbamientos cuevas

# derrumbe 2

derrumbe2=Bladex.GetSector(323000,41000,-12000)
derrumbe2.Active=0


derrumbe2.InitBreak((0.0, 3000.0, 0.0), (2500.0, 0.0, 800.0), (500.0, 0.0, 2000.0),"",100.0,0)

sectorderrumbe2=Bladex.GetSector(321005, 38709, -16116)

sectorderrumbe2.OnEnter=Derrumbe2


# derrumbe 3

derrumbe3=Bladex.GetSector(293000,44000,-2000)
derrumbe3.Active=0


derrumbe3.InitBreak((0.0, 3000.0, 0.0), (2500.0, 0.0, 800.0), (500.0, 0.0, 2000.0),"",100.0,0)

sectorderrumbe3=Bladex.GetSector(296446, 41881, -1914)

sectorderrumbe3.OnEnter=Derrumbe3



# derrumbe 4

derrumbe4=Bladex.GetSector(280000,46000,24000)
derrumbe4.Active=0


derrumbe4.InitBreak((0.0, 3000.0, 0.0), (2500.0, 0.0, 800.0), (500.0, 0.0, 2000.0),"",100.0,0)

sectorderrumbe4=Bladex.GetSector(285120, 42577, 14371)
sectorderrumbe4.OnEnter=Derrumbe4


# derrumbe 5

derrumbe5=Bladex.GetSector(320000,41000,8000)
derrumbe5.Active=0


derrumbe5.InitBreak((0.0, 3000.0, 0.0), (2500.0, 0.0, 800.0), (500.0, 0.0, 2000.0),"",100.0,0)

sectorderrumbe5=Bladex.GetSector(328989.89514, 38769.5216626, 6921.1217323)

sectorderrumbe5.OnEnter=Derrumbe5



# derrumbe 6

derrumbe6=Bladex.GetSector(285000,27000,-44000)
derrumbe6.Active=0


derrumbe6.InitBreak((0.0, 3000.0, 0.0), (2500.0, 0.0, 800.0), (500.0, 0.0, 2000.0),"",100.0,0)

sectorderrumbe6=Bladex.GetSector(286734.472189, 23275.5084068, -35677.1123514)
#sectorderrumbe6=Bladex.GetSector(285196.530526, 24722.7706468, -39957.7174235)
sectorderrumbe6.OnEnter=Derrumbe6

######## cueva multiples derrumbes


derrumbe7=Bladex.GetSector(283000,47000,32000)
derrumbe7.Active=0

derrumbe7.InitBreak((0.0, 3000.0, 0.0), (3000.0, 0.0, 800.0), (500.0, 0.0, 4000.0),"",100.0,0)

sectorderrumbe7=Bladex.GetSector(282000,45000,25750)

sectorderrumbe7.OnEnter=Derrumbe7

derrumbe8=Bladex.GetSector(290000,47000,28000)
derrumbe8.Active=0

derrumbe8.InitBreak((0.0, 4000.0, 0.0), (3000.0, 0.0, 800.0), (500.0, 0.0, 3500.0),"",100.0,0)

sectorderrumbe8=Bladex.GetSector(282500,45000,25750)
sectorderrumbe8.OnEnter=Derrumbe8


derrumbe9=Bladex.GetSector(290000,48000,24000)
derrumbe9.Active=0

derrumbe9.InitBreak((0.0, 3000.0, 0.0), (4000.0, 0.0, 800.0), (500.0, 0.0, 2000.0),"",100.0,0)

sectorderrumbe9=Bladex.GetSector(283000,45000,25750)
sectorderrumbe9.OnEnter=Derrumbe9


derrumbe10=Bladex.GetSector(300000,48000,25000)
derrumbe10.Active=0

derrumbe10.InitBreak((0.0, 3000.0, 0.0), (3000.0, 0.0, 800.0), (500.0, 0.0, 4000.0),"",100.0,0)

sectorderrumbe10=Bladex.GetSector(284000,45000,25750)

sectorderrumbe10.OnEnter=Derrumbe10




derrumbe11=Bladex.GetSector(302000,51000,22000)
derrumbe11.Active=0

derrumbe11.InitBreak((0.0, 3000.0, 0.0), (2500.0, 0.0, 800.0), (500.0, 0.0, 2000.0),"",100.0,0)

sectorderrumbe11=Bladex.GetSector(296000,47000,22000)
sectorderrumbe11.OnEnter=Derrumbe11

derrumbe12=Bladex.GetSector(304000,50000,25000)
derrumbe12.Active=0

derrumbe12.InitBreak((0.0, 3000.0, 0.0), (2500.0, 0.0, 800.0), (500.0, 0.0, 2000.0),"",100.0,0)

sectorderrumbe12=Bladex.GetSector(298000,47000,22000)
sectorderrumbe12.OnEnter=Derrumbe12
