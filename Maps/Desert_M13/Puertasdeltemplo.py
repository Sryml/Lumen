import Reference
import Select
import Actions
import Torchs
import Doors
import math
import Change
import Sounds
import darfuncs

soundllenarbotella=Sounds.CreateEntitySound('../../Sounds/agua-llenar-botella-b.wav', 'SoundLLenarBotella')
soundllenarbotella.Volume=0.5
soundllenarbotella.MinDistance=100000
soundllenarbotella.MaxDistance=200000

soundvaciarbotella=Sounds.CreateEntitySound('../../Sounds/agua-vaciar-botella-a.wav', 'SoundVaciarBotella')
soundvaciarbotella.Volume=0.5
soundvaciarbotella.MinDistance=100000
soundvaciarbotella.MaxDistance=200000

water_altar_completed = 0
fire_altar_completed = 0



BottelHand = 0
BottelOHand = None

EMPTY	= 0
FULL	= 1
USED	= 2

B_PARTICLE_GTYPE_ADD=2

bottel_state = EMPTY


spuerta4D=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
spuerta4D.MaxDistance=20000
spuerta4D.MinDistance=10000
spuerta4D.Volume=1.0

spuerta4G=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
spuerta4G.MaxDistance=20000
spuerta4G.MinDistance=10000
spuerta4G.Volume=1.0

spuerta5D=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
spuerta5D.MaxDistance=20000
spuerta5D.MinDistance=10000
spuerta5D.Volume=1.0

spuerta5G=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
spuerta5G.MaxDistance=20000
spuerta5G.MinDistance=10000
spuerta5G.Volume=1.0

puerta4=Doors.CreateDoor("BaldosaBaston", (-24500,-600,16600), (0,0,-1), 0, 2750, Doors.CLOSED)
puerta5=Doors.CreateDoor("PlataformaBaston", (-24500,0,16600), (0,-1,0), 0, 1500, Doors.OPENED)

puerta4.opentype=Doors.UNIF
puerta4.o_med_vel=-1800
puerta4.o_med_displ=2750
#puerta4.OnEndOpenFunc=PuertaAbierta
puerta4.closetype=Doors.UNIF
puerta4.c_med_displ=2750
puerta4.c_med_vel=1800
#puerta4.OnEndCloseFunc=PuertaAbierta
puerta4.SetWhileOpenSound(spuerta4D)
puerta4.SetEndOpenSound(spuerta4G)
puerta4.SetWhileCloseSound(spuerta4D)
puerta4.SetEndCloseSound(spuerta4G)

puerta5.opentype=Doors.UNIF
puerta5.o_med_vel=-400
puerta5.o_med_displ=1500
#puerta5.OnEndOpenFunc=PuertaAbierta
puerta5.closetype=Doors.UNIF
puerta5.c_med_displ=1400
puerta5.c_med_vel=400
puerta5.SetWhileOpenSound(spuerta5D)
puerta5.SetEndOpenSound(spuerta5G)
puerta5.SetWhileCloseSound(spuerta5D)
puerta5.SetEndCloseSound(spuerta5G)



n_pool_water = 0


#al lado del altar
#o=Bladex.CreateEntity("BotellaTemplo","BotellaVerde",1779.679002,-3152.050625,42447.595478)
#o.Static=0
#o.Scale=1.000000
#o.Orientation=0.015588,0.802498,-0.570109,-0.175300
#o.UseFunc = UseBotellaVerde

#en la fuente
#o=Bladex.CreateEntity("BotellaTemplo","BotellaSagrada",1864.378000,-1264.322000,-25120.728000)
#o.Static=0
#o.Scale=1.000000
#o.Orientation=0.545621,0.545621,-0.449775,0.449775
#darfuncs.SetHint(o,"Empty bottle")
#o.UseFunc = UseBotellaVerde


#en la torreta de atras
o=Bladex.CreateEntity("BotellaTemplo","BotellaSagrada",-6229.356804,-6094.916888,89171.321544,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
darfuncs.SetHint(o,"Empty Bottle")

#o.UseFunc = UseBotellaVerde

#o=Bladex.CreateEntity("ant","Antorcha",1779.679002,-3152.050625,42447.595478)
#o.Static=0
#o.Scale=0.932718

#o.Orientation=0.508650,0.508650,-0.491198,0.491198
#o.FiresIntensity=[ 0 ]
#o.Lights=[ (4.000000,0.031250,(255,154,43)) ]
#Torchs.SetUsable("ant",3,3,50)


#######AGUA PARA LLENAR LA BOTELLA.

punterowater=Bladex.CreateEntity("PunteroAgua","GhostPointer", 8000,0,-24000)
punterowater.Static=1
punterowater.Scale=0.300000
punterowater.Orientation=0.504344,0.504344,-0.495618,0.495618
punterowater.UseFunc = UseBotellaVerde
darfuncs.SetHint(punterowater,"Sacred Water")

banio_octogonal=Bladex.CreateEntity("ba�o_octogonal","Entity Water",8000,300,-24000)
banio_octogonal.Reflection=0.5
banio_octogonal.Color=0,9,13

oil_altar=Bladex.CreateEntity("oil_altar","Entity Water",-60000,-3300,41500)
oil_altar.Reflection=0
oil_altar.Color=0,0,0

punterowater=Bladex.CreateEntity("PunteroWater","GhostPointer", 3300,-4000,42500)
punterowater.Static=1
punterowater.Scale=0.100000
punterowater.Orientation=0.504344,0.504344,-0.495618,0.495618
punterowater.UseFunc=UseWaterAltar
darfuncs.SetHint(punterowater,"Water Altar")

punterofire=Bladex.CreateEntity("PunteroFire","GhostPointer", -60000,-3300,41500)
punterofire.Static=1
punterofire.Scale=0.10000
punterofire.Orientation=0.504344,0.504344,-0.495618,0.495618
punterofire.UseFunc=UseFireAltar
darfuncs.SetHint(punterofire,"Fire Altar")

### Definicion de sistemas de particulas

Bladex.AddParticleGType("Flame","FireParticle",B_PARTICLE_GTYPE_ADD,21)

for i in range(21):
	if i>=14:
		aux=1.0/3.0+2*(21.0-i)/21.0 #va de 1/3 a 1
		caux=(21.0-i)/21.0 #va de 0 a 1/3
		saux=3.0*(21.0-i)/21.0 #va de 0 a 1
	elif i>7 and i<14:
		aux=1.0
		caux=1.0/3.0
		saux=1.0
	else:
		aux=1.0-((7.0-i)/7.0) #va de 1 a 0
		caux=1.0/3.0
		saux=1.0-2*((7.0-i)/7.0) #va de 1 a -1

	r=155.0*3.0*caux
	g=155.0*3.0*caux
	b=min(255*(1.0-2.0*caux), 255.0)
	#r=200.0*2.0*caux
	#g=100.0*3.0*caux
	#b=20
	a=150.0*aux
	size=300.0+200.0*saux
	Bladex.SetParticleGVal("Flame",i,r,g,b,a,size)

Bladex.AddParticleGType("Water","GenericParticle",B_PARTICLE_GTYPE_ADD,32)

for i in range(32):
	if(i>16):
		aux=0.0
	else:
		aux=(16.0-i)/16.0
	r=50
	g=110
	b=115
	a=60
	size=10.0*(1.0-aux)+2.0
	Bladex.SetParticleGVal("Water",i,r,g,b,a,size)



#char.Position = 1779.679002,-3152.050625,42447.595478
#char.Position = 8000,300,-24000


############## ghost pointer fetiche ########################3


p=Bladex.CreateEntity("leeagua","PiedraInformativa",5470.825000,-3109.147000,42549.338000)
p.Scale=1.308209
p.Orientation=0.504344,0.504344,-0.495618,0.495618
p.UseFunc = useInGhostAgua	# cambiar funcion
darfuncs.SetHint(p,"Water Oracle")


p=Bladex.CreateEntity("leefuego","PiedraInformativa",-64466.023000,-2549.868000,41861.157000)
p.Scale=1.549318
p.Orientation=0.495618,0.495618,0.504344,-0.504344
p.UseFunc = useInGhostFuego	# cambiar funcion
darfuncs.SetHint(p,"Fire Oracle")


p=Bladex.CreateEntity("leebaston","PiedraInformativa",-24252.197000,-831.667000,11867.282000)
p.Scale=1.967222
p.Orientation=0.694659,0.719340,0.000000,0.000000
p.UseFunc = useInGhostPuerta	# cambiar funcion
darfuncs.SetHint(p,"Door Oracle")




p = Bladex.GetEntity("PBaston")
p.RemoveFromWorld()

#char.Position = 1779.679002,-3152.050625,42447.595478
#char.Position = 8000,300,-24000

#####################################
#     El rollo de fuego sagrado     #
#####################################
o=Bladex.CreateEntity("SacredTorch","Palangana",-54336.199379,-1080.569305,757.290202)
o.Scale=1.000000
o.Orientation=0.748956,0.662620,0.000000,0.000000
o.FiresIntensity=[ 0 ]
o.Lights=[ (4.000000,0.090000,(255,141,15)) ]
o.Alpha = 0
darfuncs.SetHint(o,"Sacred Fire")
Torchs.SetUsable("SacredTorch",3,3,-1)
o.FiresIntensity=[ 40 ]
o.Lights=[ (0.000000,0.090000,(255,141,15)) ]



Torchs.UseFunc = UseSacredFireTorch
SacredTorchActive = None
