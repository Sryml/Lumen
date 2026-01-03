import EnemyTypes
import EnmGenRnd
import ConcenEf
import Traps_C
import Button
import Sounds
import Doors
import math
import B3DLib
import Actions
import AbreCam
import Scorer
import InitDataField
import AuxFuncs
import darfuncs


splinellave = 0


#char.Position = -30077.9218852, -1491.99454118, -38885.49


#######################################
###     Definiciones de particulas
#######################################

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
	a=150.0*aux
	size=300.0+200.0*saux
	Bladex.SetParticleGVal("Flame",i,r,g,b,a,size)


### Llave blanca -> efectos verde-azulados

Bladex.AddParticleGType("FlameCabezon","FireParticle",B_PARTICLE_GTYPE_ADD,21)

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
	r=20.0*3.0*caux
	g=100.0*3.0*caux
	b=255.0*3.0*caux
	a=240.0*aux
	size=300.0+200.0*saux
	Bladex.SetParticleGVal("FlameCabezon",i,r,g,b,a,size)


Bladex.AddParticleGType("EnergyKeyBlanca","GenericParticle2",B_PARTICLE_GTYPE_ADD,60)

for i in range(60):
	if i>10:
		traux=(60.0-i)/50.0 #va de 0 a 1
	else:
		traux=i/10.0 #va de 1 a 0
	r=50
	g=255
	b=230
	a=150.0*traux
	size=225.0*(1-i/60.0)**2.0
	Bladex.SetParticleGVal("EnergyKeyBlanca",i,r,g,b,a,size)


Bladex.AddParticleGType("EnergyRingBlanca","GenericParticle2",B_PARTICLE_GTYPE_ADD,60)

for i in range(60):
	if i>50:
		traux=(60.0-i)/10.0 #va de 0 a 1
	else:
		traux=i/50.0 #va de 1 a 0
	r=50
	g=255
	b=230
	a=150.0*traux
	size=60.0*(1-(1-i/60.0)**0.5)
	Bladex.SetParticleGVal("EnergyRingBlanca",i,r,g,b,a,size)


### Llave amarilla -> efectos naranjas

Bladex.AddParticleGType("FlameCabezon1","FireParticle",B_PARTICLE_GTYPE_ADD,21)

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
	r=90.0*3.0*caux
	g=120.0*3.0*caux
	b=140.0*3.0*caux
	a=200.0*aux
	size=300.0+200.0*saux
	Bladex.SetParticleGVal("FlameCabezon1",i,r,g,b,a,size)


Bladex.AddParticleGType("EnergyKeyAmarilla","GenericParticle2",B_PARTICLE_GTYPE_ADD,60)

for i in range(60):
	if i>10:
		traux=(60.0-i)/50.0 #va de 0 a 1
	else:
		traux=i/10.0 #va de 1 a 0
	r=255
	g=170
	b=50
	a=170.0*traux
	size=225.0*(1-i/60.0)**2.0
	Bladex.SetParticleGVal("EnergyKeyAmarilla",i,r,g,b,a,size)


Bladex.AddParticleGType("EnergyRingAmarilla","GenericParticle2",B_PARTICLE_GTYPE_ADD,60)

for i in range(60):
	if i>50:
		traux=(60.0-i)/10.0 #va de 0 a 1
	else:
		traux=i/50.0 #va de 1 a 0
	r=255
	g=170
	b=50
	a=170.0*traux
	size=60.0*(1-(1-i/60.0)**0.5)
	Bladex.SetParticleGVal("EnergyRingAmarilla",i,r,g,b,a,size)


### Llave azul -> efectos azules

Bladex.AddParticleGType("FlameCabezon2","FireParticle",B_PARTICLE_GTYPE_ADD,21)

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
	r=25.0
	g=50.0
	b=255.0
	a=255.0*aux
	size=300.0+200.0*saux
	Bladex.SetParticleGVal("FlameCabezon2",i,r,g,b,a,size)


Bladex.AddParticleGType("EnergyKeyAzul","GenericParticle2",B_PARTICLE_GTYPE_ADD,60)

for i in range(60):
	if i>10:
		traux=(60.0-i)/50.0 #va de 0 a 1
	else:
		traux=i/10.0 #va de 1 a 0
	r=70
	g=80
	b=255
	a=255.0*traux
	size=225.0*(1-i/60.0)**2.0
	Bladex.SetParticleGVal("EnergyKeyAzul",i,r,g,b,a,size)


Bladex.AddParticleGType("EnergyRingAzul","GenericParticle2",B_PARTICLE_GTYPE_ADD,60)

for i in range(60):
	if i>50:
		traux=(60.0-i)/10.0 #va de 0 a 1
	else:
		traux=i/50.0 #va de 1 a 0
	r=70
	g=80
	b=255
	a=255.0*traux
	size=60.0*(1-(1-i/60.0)**0.5)
	Bladex.SetParticleGVal("EnergyRingAzul",i,r,g,b,a,size)


### Llave negra -> efectos rojos

Bladex.AddParticleGType("FlameCabezon3","FireParticle",B_PARTICLE_GTYPE_ADD,21)

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
	r=180.0*3.0*caux
	g=min(255*(1.0-2.0*caux), 255.0)
	b=210.0*3.0*caux
	a=150.0*aux
	size=300.0+200.0*saux
	Bladex.SetParticleGVal("FlameCabezon3",i,r,g,b,a,size)


Bladex.AddParticleGType("EnergyKeyNegra","GenericParticle2",B_PARTICLE_GTYPE_ADD,60)

for i in range(60):
	if i>10:
		traux=(60.0-i)/50.0 #va de 0 a 1
	else:
		traux=i/10.0 #va de 1 a 0
	r=255
	g=50
	b=40
	a=255.0*traux
	size=225.0*(1-i/60.0)**2.0
	Bladex.SetParticleGVal("EnergyKeyNegra",i,r,g,b,a,size)


Bladex.AddParticleGType("EnergyRingNegra","GenericParticle2",B_PARTICLE_GTYPE_ADD,60)

for i in range(60):
	if i>50:
		traux=(60.0-i)/10.0 #va de 0 a 1
	else:
		traux=i/50.0 #va de 1 a 0
	r=255
	g=50
	b=40
	a=255.0*traux
	size=60.0*(1-(1-i/60.0)**0.5)
	Bladex.SetParticleGVal("EnergyRingNegra",i,r,g,b,a,size)






piedradesliz1=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "PiedraDesliz1")
piedragolpe1=Sounds.CreateEntitySound("../../Sounds/golpe-piedra-pesada.wav", "PiedraGolpe1")

pedestaldesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "PedestalDesliz")
pedestalgolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "PedestalGolpe")
pedestaldesliz.Volume=pedestalgolpe.Volume=0.6

piedradesliz2=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "PiedraDesliz2")
piedragolpe2=Sounds.CreateEntitySound("../../Sounds/golpe-piedra-pesada.wav", "PiedraGolpe2")

desprendimiento=Sounds.CreateEntitySound("../../Sounds/drawbridge-door-close.wav", "GolpeDesprendimiento")
desprendimiento.Volume=1
desprendimiento.MinDistance=10000
desprendimiento.MaxDistance=90000

soundenergy=Sounds.CreateEntitySound("../../Sounds/powerpotion-loop.wav", "Energia")
soundenergy.Volume=1
soundenergy.MinDistance=10000
soundenergy.MaxDistance=90000

sndflash=Sounds.CreateEntitySound("../../Sounds/llave-estrella.wav", "SndFlash")
sndflash.Volume=0.7
sndflash.MinDistance=4000
sndflash.MaxDistance=20000



puerta111=Doors.CreateDoor("Puerta111", (-27250,-2000,93250), (1,0,0), 0, 4250, Doors.CLOSED)
puerta222=Doors.CreateDoor("Puerta222", (-21000,-2000,93250), (-1,0,0), 0, 4250, Doors.CLOSED)

puerta111.opentype=Doors.UNIF
puerta111.o_med_vel=-500
puerta111.o_med_displ=4250
puerta111.closetype=Doors.UNIF
puerta111.c_med_vel=900
puerta111.c_med_displ=4250

puerta222.opentype=Doors.UNIF
puerta222.o_med_vel=-500
puerta222.o_med_displ=4250
puerta222.closetype=Doors.UNIF
puerta222.c_med_vel=800
puerta222.c_med_displ=4250


start_time_key = 0


o=Bladex.CreateEntity("Cabezon","CabezaFernando",78395,-372,129142)
o.Static=1
o.Scale=1.0
o.Orientation=0.707107,0.707107,0.000000,0.000000

ao=Bladex.CreateEntity("AroCabezon","AroMagico",0,0,820)
ao.Static=1
ao.Scale=1.0
ao.Orientation=0.707107,0.707107,0.000000,0.000000
ao.CastShadows=0
ao.Alpha=0.0
o.Link(ao)
CreateRingPS(ao.Name, "Blanca")


o=Bladex.CreateEntity("Cabezon1","CabezaFernando",-80958.545000,-826.080000,70255.704000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000

ao=Bladex.CreateEntity("AroCabezon1","AroMagico",0,0,820)
ao.Static=1
ao.Scale=1.0
ao.Orientation=0.707107,0.707107,0.000000,0.000000
ao.CastShadows=0
ao.Alpha=0.0
o.Link(ao)
CreateRingPS(ao.Name, "Amarilla")


o=Bladex.CreateEntity("Cabezon2","CabezaFernando",29418.259000,-6563.854000,73235.474000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000

ao=Bladex.CreateEntity("AroCabezon2","AroMagico",0,0,820)
ao.Static=1
ao.Scale=1.0
ao.Orientation=0.707107,0.707107,0.000000,0.000000
ao.CastShadows=0
ao.Alpha=0.0
o.Link(ao)
CreateRingPS(ao.Name, "Azul")


o=Bladex.CreateEntity("Cabezon3","CabezaFernando",-91314.628000,-6317.566000,174950.716000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000

ao=Bladex.CreateEntity("AroCabezon3","AroMagico",0,0,820)
ao.Static=1
ao.Scale=1.0
ao.Orientation=0.707107,0.707107,0.000000,0.000000
ao.CastShadows=0
ao.Alpha=0.0
o.Link(ao)
CreateRingPS(ao.Name, "Negra")


puente_llave1=Doors.CreateDoor("PuenteLlave1", (78250,2500,137250), (0,0, 1),  0, 7500,Doors.OPENED)
puente_llave2=Doors.CreateDoor("PuenteLlave2", (78000,2500,121000), (0,0,-1),  0, 7500,Doors.CLOSED)

pedestal1=Doors.CreateDoor("PedestalLlave",  ( 78250, 2000,129250), (0,-1,0),  0, 2100,Doors.CLOSED)
pedestal2=Doors.CreateDoor("PedestalLlave1", (-80958, 1000, 70255), (0,-1,0),  0, 2000,Doors.CLOSED)
pedestal3=Doors.CreateDoor("PedestalLlave2", ( 29418,-4563, 73235), (0,-1,0),  0, 2000,Doors.CLOSED)
pedestal4=Doors.CreateDoor("PedestalLlave3", (-91314,-4317,174950), (0,-1,0),  0, 2000,Doors.CLOSED)


puente_llave1.opentype=Doors.UNIF
puente_llave1.o_med_vel=-450
puente_llave1.o_med_displ=7500
puente_llave1.OnEndCloseFunc=PuenteSacado
puente_llave1.OnEndOpenFunc=ResetButtons
puente_llave1.closetype=Doors.AC
puente_llave1.c_init_displ=7500
puente_llave1.c_med_vel=450
puente_llave1.SetWhileOpenSound(piedradesliz1)
#puente_llave1.SetEndOpenSound(piedragolpe1)
puente_llave1.SetWhileCloseSound(piedradesliz1)
puente_llave1.SetEndCloseSound(piedragolpe1)

puente_llave2.opentype=Doors.UNIF
puente_llave2.o_med_vel=-450
puente_llave2.o_med_displ=7500
puente_llave2.closetype=Doors.AC
puente_llave2.c_init_displ=7500
puente_llave2.c_med_vel=450
puente_llave2.SetWhileOpenSound(piedradesliz2)
#puente_llave2.SetEndOpenSound(piedragolpe2)
puente_llave2.SetWhileCloseSound(piedradesliz2)
puente_llave2.SetEndCloseSound(piedragolpe2)

pedestal1.opentype=Doors.UNIF
pedestal1.o_med_vel=-400
pedestal1.o_med_displ=1700
pedestal1.OnEndOpenFunc=EndConcentrationEffect
pedestal1.closetype=Doors.AC
pedestal1.c_init_displ=2100
pedestal1.c_med_vel=2000
pedestal1.SetWhileOpenSound(pedestaldesliz)
pedestal1.SetEndOpenSound(pedestalgolpe)

pedestal2.opentype=Doors.UNIF
pedestal2.o_med_vel=-400
pedestal2.o_med_displ=1600
pedestal2.OnEndOpenFunc=EndConcentrationEffect
pedestal2.closetype=Doors.AC
pedestal2.c_init_displ=2100
pedestal2.c_med_vel=2000
pedestal2.SetWhileOpenSound(pedestaldesliz)
pedestal2.SetEndOpenSound(pedestalgolpe)

pedestal3.opentype=Doors.UNIF
pedestal3.o_med_vel=-400
pedestal3.o_med_displ=1600
pedestal3.OnEndOpenFunc=EndConcentrationEffect
pedestal3.closetype=Doors.AC
pedestal3.c_init_displ=2100
pedestal3.c_med_vel=2000
pedestal3.SetWhileOpenSound(pedestaldesliz)
pedestal3.SetEndOpenSound(pedestalgolpe)

pedestal4.opentype=Doors.UNIF
pedestal4.o_med_vel=-400
pedestal4.o_med_displ=1600
pedestal4.OnEndOpenFunc=EndConcentrationEffect
pedestal4.closetype=Doors.AC
pedestal4.c_init_displ=2100
pedestal4.c_med_vel=2000
pedestal4.SetWhileOpenSound(pedestaldesliz)
pedestal4.SetEndOpenSound(pedestalgolpe)

blobut1=Bladex.CreateEntity("ButLlave1","Bloque",65251.589000,978.424000,125925.997000,"Physic")
blobut1.Orientation=0.500000,0.500000,0.500000,-0.500000
darfuncs.SetHint(blobut1,"Trigger")

blobut2=Bladex.CreateEntity("ButLlave2","Bloque",65250.151000,983.199000,132546.114000,"Physic")
blobut2.Orientation=0.500000,0.500000,0.500000,-0.500000
darfuncs.SetHint(blobut2,"Trigger")

ButLlave = Button.CreateButtonCombination(0,ActivatePuente,0)
b1 = ButLlave.AddButton("ButLlave1",2,(0,0,-1),800,0,0,0)
b2 = ButLlave.AddButton("ButLlave2",2,(0,0,1),800,0,0,0)

blobut1.Frozen=1
blobut2.Frozen=1

puerta_llave1=Bladex.GetSector(80000,0,111000)
puerta_llave1.Active=0

puerta_llave2=Bladex.GetSector(76000,0,111000)
puerta_llave2.Active=0

puerta_llave1.InitBreak((0.0, 0.0, 250.0), (1250.0, 100.0, 0.0), (200.0, 1250.0, 0.0))
puerta_llave2.InitBreak((0.0, 0.0, 250.0), (1750.0, 100.0, 0.0), (200.0, 1750.0, 0.0))


Disminution = 0
FadingOut = 0


PosFire = [0,0,0]
FireCamera = 0
pedestal = 0
cab = 0
LlaveLocated = [0,0,0,0]
key = 0
luzAura = 0
KeyOpenDoor = 0


inv=char.GetInventory()

key1=Bladex.GetEntity("STAR")

if not key1:
	key1=Bladex.CreateEntity("STAR","LlaveBlanca",0,0,0)
	inv.AddSpecialKey("STAR")

key2=Bladex.GetEntity("BEETLE")

if not key2:
	key2=Bladex.CreateEntity("BEETLE","LlaveAmarilla",0,0,0)
	inv.AddSpecialKey("BEETLE")

key3=Bladex.GetEntity("SHELL")

if not key3:
	key3=Bladex.CreateEntity("SHELL","LlaveAzul",0,0,0)
	inv.AddSpecialKey("SHELL")

key4=Bladex.GetEntity("SPIDER")

if not key4:
	key4=Bladex.CreateEntity("SPIDER","LlaveNegra",0,0,0)
	inv.AddSpecialKey("SPIDER")


key1.Orientation = 0.7,0.0,0.0,-0.7
key1.Scale = 0.1
key1.CastShadows=0
key1.Alpha=0.01
key1.SelfIlum=1

key2.Orientation = 0.0,-0.7,0.7,0.0
key2.Scale = 0.1
key2.CastShadows=0
key2.Alpha=0.01
key2.SelfIlum=1

key3.Orientation = 0.5,0.5,0.5,-0.5
key3.Scale = 0.1
key3.CastShadows=0
key3.Alpha=0.01
key3.SelfIlum=1

key4.Orientation = 0.7,0.0,0.0,-0.7
key4.Scale = 0.1
key4.CastShadows=0
key4.Alpha=0.01
key4.SelfIlum=1

Bladex.CreateTimer("Timer30",1.0/30.0)

aura_size=5
aura_var=4

thiskey = -1

sectorllave1 = Bladex.GetSector(78000,-1000,132000)
sectorllave1.OnLeave = StartCreateKey

sectorllave2 = Bladex.GetSector(-78000,0,70500 )
sectorllave2.OnEnter = StartCreateKey

sectorllave3 = Bladex.GetSector(26782, -5914, 73872)
sectorllave3.OnEnter = StartCreateKey

sectorllave4 = Bladex.GetSector(-88507, -5914, 174795)
sectorllave4.OnEnter = StartCreateKey

sectorbreak = Bladex.GetSector(78147, 965, 122361)
sectorbreak.OnEnter = BreakDoor

#CabezaEnm1 = EnmGenRnd.CreateEnemy((74250,0,102000),"GenHd_01", "Troll_Dark", "Garropin", 0, "Escudo1", 1)
#CabezaEnm2 = EnmGenRnd.CreateEnemy((80750,0,103500),"GenHd_02", "Troll_Dark", "Garropin", 0, "Escudo1", 1)

seccer1= Bladex.GetSector(-14000,0,73250)
seccer2= Bladex.GetSector(86800,-5000,186000)
seccer3= Bladex.GetSector(94250,-5000,186000)
seccer4= Bladex.GetSector(101750,-5000,186000)

seccer1.Active = 0
seccer2.Active = 0
seccer3.Active = 0
seccer4.Active = 0
