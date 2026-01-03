import EnmGenRnd
import Levers
import Sounds
import B3DLib
import math

Bladex.CreateTimer("Timer60",1.0/60.0)

soundvaciado=Sounds.CreateEntitySound('../../Sounds/Agua-Desague.wav', 'SoundVaciado')
soundvaciado.Volume=1.0
soundvaciado.MinDistance=5000
soundvaciado.MaxDistance=14000

soundchorro=Sounds.CreateEntitySound('../../Sounds/agua-canal.wav', 'SoundChorro')
soundchorro.Volume=1.0
soundchorro.MinDistance=5000
soundchorro.MaxDistance=15000



Bladex.AddParticleGType("AguaC","WaterParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	r=80
	g=35
	b=4
	a=100
	size=160.0
	Bladex.SetParticleGVal("AguaC",i,r,g,b,a,size)

Bladex.AddParticleGType("Espuma","SmokeParticle",B_PARTICLE_GTYPE_BLEND,10)

for i in range(10):
	aux=(10.0-i)/10.0
	r=80
	g=40
	b=2
	#a=255*math.sqrt(1.0-aux)
	a=255
	size=600.0*math.sqrt(1.0-aux)
	Bladex.SetParticleGVal("Espuma",i,r,g,b,a,size)



#FUENTE VENENO

#-2477.56478994, 6310.83184338, -9904.25667495

###chorro1
CreateCascada("chorro1",(-3935.6,2165.2,-23713.9),(0.0, 0.0, 250.0),(0.0, 0.0, 1000.0),(-3935.6,3600,-23113.9),16)

###chorro2
CreateCascada("chorro2",(-6346.2,2188.1,-20235.0),(0.0, 0.0, 250.0),(1500.0, 0.0, 0.0),(-5800,3600,-20235.0),16)


###chorro3
CreateCascada("chorro3",(-6346.2,2188.1,-10850),(0.0, 0.0, 250.0),(1500.0, 0.0, 0.0),(-5800.2,3388.1,-10850),16)


chorritospalanca=Levers.PlaceLever("ChoritosPalanca", Levers.LeverType3, (1388,1695,-14555), (0.5,0.5,-0.5,0.5), 1.0)
chorritospalanca.mode=1
chorritospalanca.OnTurnOnFunc=UsePalancaChorritos
chorritospalanca.OnTurnOnArgs=()


Bladex.ReadAlphaBitMap("../../Data/Bubble.bmp","BubbleParticle")


CreateParticle(80,70,60)


Esp = 0

DespWater = 2400.0 / (20.0 * 60.0)
DespWater2 = 2250.0 / (20.0 * 60.0)

AlturaWater = 3600.0





N_Lich_Gen = 0
Point_Gen = 0
GenActivated = 2

PosLichGen = [(-4000,3500 + 1000,-16500),(-4000,3500 + 1000,-20500)]
PlaySound(soundchorro,"chorro2",-1)

#char.Position = (-4000,3500,-16500)