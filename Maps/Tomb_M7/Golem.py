import Actions
import EnemyTypes
import Sounds

_Golemalo=Bladex.CreateSound("../../Sounds/M-caida.wav","Golemalo")
_Golemalo.MaxDistance=1000000.0
_Golemalo.MinDistance=900000.0

Golempaso1=Sounds.CreateEntitySound("../../Sounds/paso-golem-4.wav","Golempaso1")
Golempaso1.Volume = 0.7
Golempaso1.MaxDistance=1000000.0
Golempaso1.MinDistance=900000.0

Golempaso2=Sounds.CreateEntitySound("../../Sounds/paso-golem-5.wav","Golempaso2")
Golempaso2.Volume = 0.7
Golempaso2.MaxDistance=1000000.0
Golempaso2.MinDistance=900000.0

Golempaso3=Sounds.CreateEntitySound("../../Sounds/paso-golem-6.wav","Golempaso3")
Golempaso3.Volume = 0.7
Golempaso3.MaxDistance=1000000.0
Golempaso3.MinDistance=900000.0

FPASO1 = 1.0 # Patada
FPASO2 = 2.0
FPASO3 = 4.0
FPASO4 = 7
FPASO5 = 7.2

ParedGolem=Bladex.GetSector(9750, 4000, -1500)
ParedGolem.InitBreak((350,0,0),(0,1000,0),(0, 200,1500),'piedra pesada')
ParedGolem.Active = 0

"""
Bladex.AddParticleGType("Tierrax","SmokeParticle",B_PARTICLE_GTYPE_BLEND,64)

for i in range(64):
	aux=(64.0-i)/64.0
	r=100
	g=100
	b=100
	a=255.0*(1.0-aux)**0.5
	size=80.0+aux*400.0
	Bladex.SetParticleGVal("Tierrax",i,r,g,b,a,size)
"""
"""
Bladex.AddParticleGType("DustGolem","SmokeParticle",B_PARTICLE_GTYPE_BLEND,64)

for i in range(64):
	if i>32:
		traux=0.0
	else:
		traux=(32.0-i)/32.0
	aux=(64.0-i)/64.0
	r=190
	g=150
	b=160
	a=100.0*(1.0-traux)**0.5
	size=1.0+aux*450.0
	Bladex.SetParticleGVal("DustGolem",i,r,g,b,a,size)
"""

def CreateDustGolemParticle(sized = 700):
	Bladex.AddParticleGType("DustGolem","SmokeParticle",B_PARTICLE_GTYPE_BLEND,128)

	for i in range(128):
		if i>64:
			traux=0.0
		else:
			traux=(64.0-i)/64.0
		aux=(64.0-i)/64.0
		r=90
		g=70
		b=75
		a=255.0*(1.0-traux)**0.5
		size=10.0+aux*sized
		Bladex.SetParticleGVal("DustGolem",i,r,g,b,a,size)



"""
	Bladex.AddParticleGType("DustGolem","SmokeParticle",B_PARTICLE_GTYPE_BLEND,128)

	for i in range(128):
		if i>64:
			traux=0.0
		else:
			traux=(64.0-i)/64.0
		aux=(128.0-i)/128.0
		r=255
		g=230
		b=210
		a=150.0*(1.0-traux)**0.5
		size=4.0+aux*400.0
		Bladex.SetParticleGVal("DustGolem",i,r,g,b,a,size)
"""
CreateDustGolemParticle()

troll          = Bladex.CreateEntity("GolemFinal", "Golem_stone", 9027, 5775,-1203,"Person")



ParedGolemSectInit1=Bladex.GetSector(21501.3071344, 6335.2, -8021.87488872)
ParedGolemSectInit1.OnEnter = IniciaEscenaGolem

#char.Position = (19777.9006661, 5541.20230103, -16234.8925243)
#IniciaEscenaGolem(0,"Player1")
#GolemSmoke("GolemFinal")