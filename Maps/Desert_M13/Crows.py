cuervo1_sound=Bladex.CreateSound('../../Sounds/cuervo-graznido.wav', 'SonidoCuervo1')
cuervo1_sound.Volume=1.0
cuervo1_sound.MinDistance=3000
cuervo1_sound.MaxDistance=40000

cuervo2_sound=Bladex.CreateSound('../../Sounds/cuervo-graznido.wav', 'SonidoCuervo2')
cuervo2_sound.Volume=1.0
cuervo2_sound.MinDistance=3000
cuervo2_sound.MaxDistance=40000

crow1=Bladex.CreateEntity("Crow1","Pio",-3100,7050,-125000)
crow1.Orientation=0.7,0.7,0,0
crow1.Rotate(0,-1,0,1.8)
crow1.Actor=1
crow1.Animation="Crw_pic"
crow1.FPS=20.0
crow1.SendSectorMsgs=0
crow1.TurnOn()

crow2=Bladex.CreateEntity("Crow2","Pio",-3180,6980,-125800)
crow2.Orientation=0.7,0.7,0,0
crow2.Rotate(0,-1,0,3)
crow2.Actor=1
crow2.Animation="Crw_pic"
crow2.FPS=20.0
crow2.SendSectorMsgs=0
crow2.TurnOn()

corpse1=Bladex.CreateEntity("Corpse1","Skeleton",-3000,7150,-126000)
corpse1.Orientation=0.7,0.7,0,0
corpse1.Actor=1
corpse1.Animation="Bar_corpse0"
corpse1.FPS=30.0

Bladex.CreateTimer("TimerCuervos",0.01)



CuervosStatus=0

#Status=0 comiendo
#Status=1 huyendo
#Status=2 volviendo
#Status=3 escondidos


timer1=0.0



corpse1.TimerFunc=AsustarCuervos



SectorCuervos=Bladex.GetSector(0,5000,-120000)
SectorCuervos.OnEnter=ActivarCuervos1
