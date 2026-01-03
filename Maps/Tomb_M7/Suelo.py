import Button
import Bladex
import Doors
import Sounds

Bladex.AddParticleGType("DustDoor","SmokeParticle",B_PARTICLE_GTYPE_BLEND,128)

for i in range(128):
	if i>64:
		traux=0.0
	else:
		traux=(64.0-i)/64.0
	aux=(64.0-i)/64.0
	r=90
	g=70
	b=75
	a=200.0*(1.0-traux)**0.5
	size=10.0+aux*1000.0
	Bladex.SetParticleGVal("DustDoor",i,r,g,b,a,size)


o=Bladex.CreateEntity("SButton1","Bloque",31316.183428,3970.627453,15118.052787)
o.Static=0
o.Scale=1.000000
o.Orientation=0.500000,0.500000,-0.500000,0.500000
darfuncs.SetHint(o,"Trigger")


o=Bladex.CreateEntity("SButton2","Bloque",4050.077149,4483.486306,14545.672230)
o.Static=0
o.Scale=1.000000
o.Orientation=0.495618,0.495618,-0.504344,0.504344
darfuncs.SetHint(o,"Trigger")

c_button1 = Button.CreateButtonCombination(0,PushButtonTrampus)
c_button1.Cycle = 1
button1 = c_button1.AddButton("SButton1",2,(0,0,1),800,0,0,0)
button1.sound = Bladex.CreateSound('../../Sounds/block-sliding.wav', 'Sound_Button1')
button1.sound.Volume=0.4
button1.sound.MinDistance=1000
button1.sound.MaxDistance=8000

c_button2 = Button.CreateButtonCombination(0,PushButtonTrampus)
c_button2.Cycle = 1
button2 = c_button2.AddButton("SButton2",2,(0,0,1),800,0,0,0)
button2.sound = Bladex.CreateSound('../../Sounds/block-sliding.wav', 'Sound_Button2')
button2.sound.Volume=0.4
button2.sound.MinDistance=1000
button2.sound.MaxDistance=8000

trampadesliz1=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-deslizando-2.wav", "trampadesliz1")
trampadesliz1.MaxDistance=20000
trampadesliz1.MinDistance=2000
trampadesliz1.Volume=1.0

trampadesliz1c=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-deslizando-2.wav", "PiedraDesliz2")
trampagolpe1=Sounds.CreateEntitySound("../../Sounds/M-CIERRE-GATE.wav", "PiedraGolpe")
trampagolpe1.MaxDistance=35000
trampagolpe1.MinDistance=5000
trampagolpe1.Volume=1.0




suelo1=Doors.CreateDoor("Suelo1", (20000,5500,13000), (0,0,-1),  0, 3500,Doors.CLOSED)
suelo2=Doors.CreateDoor("Suelo2", (20000,5500,10000), (0,0, 1),  0, 3500,Doors.CLOSED)

suelo1.opentype=Doors.UNIF
suelo1.o_med_vel=-300
suelo1.o_med_displ=3500
suelo1.closetype=Doors.AC
suelo1.c_init_displ=3500
suelo1.c_med_vel=2800
suelo1.OnEndCloseFunc = SueloCerrado
suelo1.OnEndOpenFunc = SueloAbierto

suelo1.SetWhileOpenSound(trampadesliz1)
suelo1.SetEndOpenSound(trampagolpe1)
suelo1.SetWhileCloseSound(trampadesliz1c)
suelo1.SetEndCloseSound(trampagolpe1)

suelo2.opentype=Doors.UNIF
suelo2.o_med_vel=-300
suelo2.o_med_displ=3500
suelo2.closetype=Doors.AC
suelo2.c_init_displ=3500
suelo2.c_med_vel=2800

suelo_state = 0

Button.Turn("SButton1")
Button.Turn("SButton2")

Entrada1 = Bladex.GetSector(20000,3000,13000)
Entrada2 = Bladex.GetSector(20000,3000,10000)

Entrada1.OnEnter = ActivateSuelo
Entrada2.OnEnter = ActivateSuelo

Suelo1 = Bladex.GetSector(20000,5500,13000)
Suelo2 = Bladex.GetSector(20000,5500,10000)