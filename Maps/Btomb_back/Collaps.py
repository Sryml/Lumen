import Bladex


MESSAGE_START_WEAPON=7
MESSAGE_STOP_WEAPON=8
MESSAGE_SETSTATICWEPONMODE=13

Bladex.CreateTimer("Timer10",1.0/10.0)



### Sonidos

derrumbesuelopiedra=Bladex.CreateSound("../../Sounds/ground-collapse.wav", "DerrumbeSueloPiedra")
derrumbesuelopiedra.Volume=1
derrumbesuelopiedra.MinDistance=10000
derrumbesuelopiedra.MaxDistance=40000


## barrote 1

derrumbe1=Bladex.GetSector(318000,27000,-10000)
derrumbe1.Active=0


derrumbe1.InitBreak((0.0, 6000.0, 0.0), (4800.0, 0.0, 800.0), (500.0, 0.0, 4000.0),"",100.0,0)

sectorderrumbe1=Bladex.GetSector(318000,19000,-10000)

sectorderrumbe1.OnEnter=Derrumbe1


## barrote 2

derrumbe2=Bladex.GetSector(325000,37000,-15000)
derrumbe2.Active=0


derrumbe2.InitBreak((0.0, 6000.0, 0.0), (4800.0, 0.0, 800.0), (500.0, 0.0, 4000.0),"",100.0,0)

sectorderrumbe2=Bladex.GetSector(325000,30000,-15000)

sectorderrumbe2.OnEnter=Derrumbe2