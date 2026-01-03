import Bladex
import AuxFuncs
import Scorer

AuxFuncs.SingleFrameFade()
Scorer.SetVisible(0)



EXGRP_TOTALEXCLUSION=1



##################################################
##	Definicion de sistemas de particulas
##################################################


Bladex.AddParticleGType("Polvo","SmokeParticle2",B_PARTICLE_GTYPE_BLEND,120)

for i in range(120):
	if i>100:
		traux=1.0-(120.0-i)/20.0
	else:
		traux=(100.0-i)/100.0
	aux=(120.0-i)/120.0
	r=255
	g=255
	b=255
	a=255.0*(1.0-traux)**2.0
	size=1200.0+aux*600.0
	Bladex.SetParticleGVal("Polvo",i,r,g,b,a,size)

Bladex.AddParticleGType("Nieve","GenericParticle",B_PARTICLE_GTYPE_BLEND,120)

for i in range(120):
	aux=(120.0-i)/120.0
	r=255
	g=255
	b=255
	a=200.0*(1.0-aux)**2.0
	size=100.0-aux*80.0
	Bladex.SetParticleGVal("Nieve",i,r,g,b,a,size)

Bladex.AddParticleGType("PolvilloNieve","GenericParticle",B_PARTICLE_GTYPE_BLEND,120)

for i in range(120):
	if i<30:
		aux=(30.0-i)/30.0
	r=255
	g=255
	b=255
	a=120.0*(1.0-aux)
	size=12.0-aux*8.0
	Bladex.SetParticleGVal("PolvilloNieve",i,r,g,b,a,size)




#####################
##	Sectores
#####################


su1alud=Bladex.GetSector(-59000.0, -35000.0, -78000.0)
su1alud.Active=0

su2alud=Bladex.GetSector(-59000.0, -40000.0, -78000.0)
su2alud.Active=0


sd1alud=Bladex.GetSector(-62500.0, -29000.0, -75500.0)
sd1alud.Active=0

sd2alud=Bladex.GetSector(-60500.0, -29000.0, -75000.0)
sd2alud.Active=0

sd3alud=Bladex.GetSector(-59000.0, -29000.0, -73500.0)
sd3alud.Active=0


su1alud.InitBreak((0.0, 3000.0, 0.0), (2600.0, 0.0, -800.0), (500.0, 0.0, 2500.0))
su2alud.InitBreak((0.0, 4000.0, 0.0), (500.0, 0.0, 3000.0), (3200.0, 0.0, -800.0))

sd1alud.InitBreak((0.0, 500.0, 0.0), (3000.0, 0.0, -800.0), (500.0, 0.0, 2500.0))
sd2alud.InitBreak((0.0, 500.0, 0.0), (500.0, 0.0, 2500.0), (3000.0, 0.0, -800.0))
sd3alud.InitBreak((0.0, 500.0, 0.0), (3000.0, 0.0, -800.0), (500.0, 0.0, 2500.0))



######################
##	Sonidos
######################

golpepiedranieve1=Bladex.CreateSound("../../Sounds/golpe-nieve.wav", "GolpePiedraNieve1")
golpepiedranieve1.Volume=0.4
golpepiedranieve1.MinDistance=2000
golpepiedranieve1.MaxDistance=15000
golpepiedranieve1.Pitch=0.6

golpepiedranieve2=Bladex.CreateSound("../../Sounds/golpe-nieve.wav", "GolpePiedraNieve2")
golpepiedranieve2.Volume=0.4
golpepiedranieve2.MinDistance=2000
golpepiedranieve2.MaxDistance=15000
golpepiedranieve2.Pitch=1.2

cortinanieve=Bladex.CreateSound("../../Sounds/alud.wav", "CortinaNieve")
cortinanieve.Volume=1
cortinanieve.MinDistance=5000
cortinanieve.MaxDistance=30000

sonidoalud=Bladex.CreateSound("../../Sounds/alud2.wav", "SonidoAlud")
sonidoalud.Volume=1
sonidoalud.MinDistance=15000
sonidoalud.MaxDistance=40000



######################
##	Objetos
######################

piedra1=Bladex.CreateEntity("Piedra1","Piedra_09",-57250.0,-35000.000000,-75250.0, "Physic")
piedra1.Scale=0.3
piedra1.Orientation=0.707107,0.707107,0.000000,0.000000

piedra2=Bladex.CreateEntity("Piedra2","Piedra_07",-59500.0,-34000.000000,-75750.0, "Physic")
piedra2.Scale=0.15
piedra2.Orientation=0.707107,0.707107,0.000000,0.000000

piedra3=Bladex.CreateEntity("Piedra3","Piedra_09",-60250.0,-35000.000000,-76000.0, "Physic")
piedra3.Scale=0.25
piedra3.Orientation=0.707107,0.707107,0.000000,0.000000

piedra1.RemoveFromWorld()
piedra2.RemoveFromWorld()
piedra3.RemoveFromWorld()

piedra1.ExclusionGroup=EXGRP_TOTALEXCLUSION
piedra2.ExclusionGroup=EXGRP_TOTALEXCLUSION
piedra3.ExclusionGroup=EXGRP_TOTALEXCLUSION


roca1=Bladex.CreateEntity("Roca1","Piedra_04",-58286.723999,-27174.909513,-75285.960245)
roca1.Scale=3.793710
roca1.Orientation=0.793353,0.608761,0.000000,0.000000

roca2=Bladex.CreateEntity("Roca2","Piedra_04",-56250.192320,-33973.700687,-79275.187775)
roca2.Scale=6.177481
roca2.Orientation=0.906308,0.422618,0.000000,0.000000

roca3=Bladex.CreateEntity("Roca3","Piedra_04",-57559.639132,-28390.746268,-74618.056438)
roca3.Scale=2.497850
roca3.Orientation=0.596368,0.596368,-0.379928,0.379928

roca4=Bladex.CreateEntity("Roca4","Piedra_04",-60925.562286,-40507.429926,-80650.093516)
roca4.Scale=5.995802
roca4.Orientation=0.976296,0.216440,0.000000,0.000000

roca1.RemoveFromWorld()
roca2.RemoveFromWorld()
roca3.RemoveFromWorld()
roca4.RemoveFromWorld()




###########################
##	Funcionamiento
###########################


######## Funcion: Alud3()

######## Funcion: Alud2()

######## Funcion: Alud()

######## Funcion: ReiniciaCamaraInicio(camera, frame)

######## Funcion: Camara2(camera, frame)

######## Funcion: ReposicionaPlayerInicio(person)

######## Funcion: SueltaPiedra1()

######## Funcion: SueltaPiedras23()

######## Funcion: RegueroNieve1()

######## Funcion: RegueroNieve2()

######## Funcion: Comienza()

Bladex.AddScheduledFunc(Bladex.GetTime(), ComienzoPrevio, ())
