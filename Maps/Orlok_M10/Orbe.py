import Bladex
import AuxFuncs
import OnInitTake
import Objects
import Actions
import Doors
import Sounds




##################################
###     Sistemas de particulas
##################################

Bladex.ReadAlphaBitMap("../../Data/Estrellita.bmp","Estrellita")

Bladex.AddParticleGType("ChispaOrbe","Estrellita",B_PARTICLE_GTYPE_ADD,60)

for i in range(60):
	if i>40:
		traux=(i-40.0)/20.0
	elif i>30:
		traux=0.0
	else:
		traux=(30.0-i)/30.0
	r=255.0
	g=180.0
	b=90.0
	a=200.0*(1.0-traux)
	size=40.0*(1.0-traux)
	Bladex.SetParticleGVal("ChispaOrbe",i,r,g,b,a,size)

Bladex.AddParticleGType("ChispaElectrica","Estrellita",B_PARTICLE_GTYPE_ADD,60)

for i in range(60):
	if i>40:
		traux=(i-40.0)/20.0
	elif i>30:
		traux=0.0
	else:
		traux=(30.0-i)/30.0
	r=80.0
	g=110.0
	b=255.0
	a=200.0*(1.0-traux)
	size=40.0*(1.0-traux)
	Bladex.SetParticleGVal("ChispaElectrica",i,r,g,b,a,size)

Bladex.AddParticleGType("ChispaObelisco","Estrellita",B_PARTICLE_GTYPE_ADD,60)

for i in range(60):
	if i>40:
		traux=(i-40.0)/20.0
	elif i>30:
		traux=0.0
	else:
		traux=(30.0-i)/30.0
	r=80.0
	g=100.0
	b=255.0
	a=200.0*(1.0-traux)
	size=140.0*(1.0-traux)
	Bladex.SetParticleGVal("ChispaObelisco",i,r,g,b,a,size)




#####################
###     Sonidos
#####################

sndrayo1=Bladex.CreateSound("../../Sounds/RAYOS-ELECTRICOS.wav", "SonidoRayo1")
sndrayo1.Volume=1
sndrayo1.MinDistance=5000
sndrayo1.MaxDistance=30000
sndrayo1.Pitch=0.6

sndrayo2=Bladex.CreateSound("../../Sounds/RAYOS-ELECTRICOS.wav", "SonidoRayo2")
sndrayo2.Volume=1
sndrayo2.MinDistance=5000
sndrayo2.MaxDistance=30000
sndrayo2.Pitch=1.0

sndrayo3=Bladex.CreateSound("../../Sounds/RAYOS-ELECTRICOS.wav", "SonidoRayo3")
sndrayo3.Volume=1
sndrayo3.MinDistance=5000
sndrayo3.MaxDistance=30000
sndrayo3.Pitch=1.6




#################################################
###     Objetos, particulas, luces, rayos...
#################################################

orbe=Bladex.CreateEntity("Orbe", "Orbe", 43500.0, -41900.0, 61500.0, "Physic")
orbe.Scale=1.000000
orbe.Orientation=0.707107,0.707107,0.000000,0.000000
orbe.Lights=[ (0.5,0.03125,(255,180,96)) ]
orbe.Alpha=0.2
orbe.Solid=0

lorbe=AuxFuncs.GetSpot(orbe)
lorbe.SizeFactor=1.0

orbedin=Objects.CreateDinamicObject("Orbe")

chorbe=Bladex.CreateEntity("ChispasOrbe", "Entity Particle System D1", 0.0, 0.0, 0.0)
chorbe.Position=orbe.Position
chorbe.ParticleType="ChispaOrbe"
chorbe.YGravity=0.0
chorbe.Friction=0.0
chorbe.PPS=50
chorbe.Velocity=0.0, 0.0, 0.0
chorbe.RandomVelocity=-4.0
chorbe.Time2Live=60

soporbe=Bladex.CreateEntity("SoporteOrbe", "SoporteOrbe", 16750.0, -32265.0, 69000.0)
soporbe.Static=1
soporbe.Scale=1.5
soporbe.Orientation=0.000000,0.000000,0.707107,-0.707107

luzob1=Bladex.CreateEntity("LuzOb1", "Entity Spot", 18225.0, -32825.0, 69000.0)
luzob1.Intensity=0.0
luzob1.Color=80, 100, 255
luzob1.CastShadows=0

luzob2=Bladex.CreateEntity("LuzOb2", "Entity Spot", 18710.0, -37600.0, 68980.0)
luzob2.Intensity=0.0
luzob2.Color=80, 100, 255
luzob2.CastShadows=0

luzg1=Bladex.CreateEntity("LuzG1", "Entity Spot", 16800.0, -38400.0, 66070.0)
luzg1.Intensity=0.0
luzg1.Color=80, 100, 255
luzg1.CastShadows=0

luzg2=Bladex.CreateEntity("LuzG2", "Entity Spot", 16840.0, -38400.0, 71930.0)
luzg2.Intensity=0.0
luzg2.Color=80, 100, 255
luzg2.CastShadows=0

rayoob=Bladex.CreateEntity("RayoObelisco", "Entity ElectricBolt", 16810.0, -32615.0, 69000.0)
rayoob.Target=18325.0, -32825.0, 69000.0
rayoob.Position=16810.0, -32615.0, 69000.0
#rayoob.CoreGlowColor=
#rayoob.InnerGlowColor=
#rayoob.OuterGlowColor=
rayoob.MaxAmplitude=200
rayoob.MinSectorLength=30000

rayog1=Bladex.CreateEntity("RayoG1", "Entity ElectricBolt", 18710.0, -37600.0, 68980.0)
rayog1.Target=16800.0, -38400.0, 66070.0
rayog1.Position=18710.0, -37600.0, 68980.0
#rayog1.CoreGlowColor=
#rayog1.InnerGlowColor=
#rayog1.OuterGlowColor=
rayog1.MaxAmplitude=300
rayog1.MinSectorLength=30000

rayog2=Bladex.CreateEntity("RayoG2", "Entity ElectricBolt", 18710.0, -37600.0, 68980.0)
rayog2.Target=16840.0, -38400.0, 71930.0
rayog2.Position=18710.0, -37600.0, 68980.0
#rayog2.CoreGlowColor=
#rayog2.InnerGlowColor=
#rayog2.OuterGlowColor=
rayog2.MaxAmplitude=300
rayog2.MinSectorLength=30000



####################
###     Puertas
####################

deslizpuerta1=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizPuerta1")
golpepuerta1=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "GolpePuerta1")
deslizpuerta2=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizPuerta2")
golpepuerta2=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "GolpePuerta2")
deslizpuerta3=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizPuerta3")
golpepuerta3=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "GolpePuerta3")
deslizpuerta4=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizPuerta4")
golpepuerta4=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "GolpePuerta4")

deslizpuerta1.Volume=0.5
golpepuerta1.Volume=0.5
deslizpuerta2.Volume=0.5
golpepuerta2.Volume=0.5
deslizpuerta3.Volume=0.5
golpepuerta3.Volume=0.5
deslizpuerta4.Volume=0.5
golpepuerta4.Volume=0.5

puerta1=Doors.CreateDoor("Puerta1", (28250, -34000, 63000), (0, 1, 0), 250, 3100, Doors.CLOSED)
puerta2=Doors.CreateDoor("Puerta2", (21750, -34000, 63000), (0, 1, 0), 250, 3100, Doors.CLOSED)
puerta3=Doors.CreateDoor("Puerta3", (21750, -34000, 75000), (0, 1, 0), 250, 3100, Doors.CLOSED)
puerta4=Doors.CreateDoor("Puerta4", (28250, -34000, 75000), (0, 1, 0), 250, 3100, Doors.CLOSED)

puerta1.opentype=Doors.AC_UNIF
puerta1.o_init_vel=0
puerta1.o_init_displ=250
puerta1.o_med_vel=-310
puerta1.o_med_displ=2600
puerta1.closetype=Doors.AC_UNIF
puerta1.c_init_vel=0
puerta1.c_init_displ=250
puerta1.c_med_vel=800
puerta1.c_med_displ=2600
puerta2.opentype=Doors.AC_UNIF
puerta2.o_init_vel=0
puerta2.o_init_displ=250
puerta2.o_med_vel=-310
puerta2.o_med_displ=2600
puerta2.closetype=Doors.AC_UNIF
puerta2.c_init_vel=0
puerta2.c_init_displ=250
puerta2.c_med_vel=800
puerta2.c_med_displ=2600
puerta3.opentype=Doors.AC_UNIF
puerta3.o_init_vel=0
puerta3.o_init_displ=250
puerta3.o_med_vel=-310
puerta3.o_med_displ=2600
puerta3.closetype=Doors.AC_UNIF
puerta3.c_init_vel=0
puerta3.c_init_displ=250
puerta3.c_med_vel=800
puerta3.c_med_displ=2600
puerta4.opentype=Doors.AC_UNIF
puerta4.o_init_vel=0
puerta4.o_init_displ=250
puerta4.o_med_vel=-310
puerta4.o_med_displ=2600
puerta4.closetype=Doors.AC_UNIF
puerta4.c_init_vel=0
puerta4.c_init_displ=250
puerta4.c_med_vel=800
puerta4.c_med_displ=2600

puerta1.SetWhileOpenSound(deslizpuerta1)
puerta1.SetEndOpenSound(golpepuerta1)
puerta1.SetWhileCloseSound(deslizpuerta1)
puerta1.SetEndCloseSound(golpepuerta1)
puerta2.SetWhileOpenSound(deslizpuerta2)
puerta2.SetEndOpenSound(golpepuerta2)
puerta2.SetWhileCloseSound(deslizpuerta2)
puerta2.SetEndCloseSound(golpepuerta2)
puerta3.SetWhileOpenSound(deslizpuerta3)
puerta3.SetEndOpenSound(golpepuerta3)
puerta3.SetWhileCloseSound(deslizpuerta3)
puerta3.SetEndCloseSound(golpepuerta3)
puerta4.SetWhileOpenSound(deslizpuerta4)
puerta4.SetEndOpenSound(golpepuerta4)
puerta4.SetWhileCloseSound(deslizpuerta4)
puerta4.SetEndCloseSound(golpepuerta4)


#######################################
###     Funcionamiento previo orbe
#######################################

###
# Variables y constantes
###

TRVAR=0.2/90.0
SCLVAR=1.0/90.0
INTVAR=0.5/90.0
SIZEVAR=1.0/90.0
ESTTIME=2.0

ejey=(0.0, 1.0, 0.0)
ejeyn=(0.0, -1.0, 0.0)

######## Funcion: ReseteaCamaraOrbe()

######## Funcion: MueveChispasOrbe(psys)

######## Funcion: FlotaOrbe()

######## Funcion: ParaFlotacionOrbe(tr_sector, ent_name)

######## Funcion: LanzaFlotacionOrbe(tr_sector, ent_name)

Bladex.SetTriggerSectorFunc("ZonaOrbe", "OnEnter", LanzaFlotacionOrbe)
Bladex.SetTriggerSectorFunc("ZonaOrbe", "OnLeave", ParaFlotacionOrbe)



#########################################
###     Funcionamiento pedestal orbe
#########################################

espob_step=0
TOTAL_ESPOB_TIME=6.0
TOTAL_ESPOB_STEPS=TOTAL_ESPOB_TIME*60.0
ESPOB_ANGLE=12.0*3.14159
ESPOB_ANGLE_VARIATION=ESPOB_ANGLE/TOTAL_ESPOB_STEPS
ESPOB_HEIGHT=4100.0
ESPOB_HEIGHT_VARIATION=ESPOB_HEIGHT/TOTAL_ESPOB_STEPS
ESPOB_INIT_VEL=4000.0
ESPOB_END_VEL=1200.0
ESPOB_VEL_VARIATION=(ESPOB_INIT_VEL-ESPOB_END_VEL)/TOTAL_ESPOB_STEPS
ESPOB_INIT_RVEL=7.0
ESPOB_END_RVEL=3.0
ESPOB_RVEL_VARIATION=(ESPOB_INIT_RVEL-ESPOB_END_RVEL)/TOTAL_ESPOB_STEPS
initespobdir=-1.0, 0.0, 0.0

######## Funcion: ApagaRayos()

######## Funcion: ParaCamaraPuertas(camera, frame)

######## Funcion: AbrePuertas()

######## Funcion: RayosObeliscoGargolas()

######## Funcion: ElevaEspiralObelisco(ent_name, time)

######## Funcion: EspiralObelisco()

######## Funcion: LanzaRayoObelisco()

######## Funcion: MueveOrbePedestal()

######## Funcion: ReapareceOrbeGradual(ent_name, time)

######## Funcion: ReapareceOrbe()

######## Funcion: ConcentraEnergiaOrbe()

######## Funcion: UsaPedestal()

######## Funcion: GuardaArmas(person)

######## Funcion: SituaPersonajePedestal(obj_name, use_from)

soporbe.UseFunc=SituaPersonajePedestal



################################
###     Funcionamiento orbe
################################

######## Funcion: DesapareceOrbeGradual(ent_name, time)

######## Funcion: LanzaEstelaChispas(ent_name, time)

######## Funcion: DesapareceOrbe()

######## Funcion: ElevaOrbe()

######## Funcion: CogeOrbe()

######## Funcion: SituaPersonajeOrbe()

OnInitTake.AddOnInitTakeEvent("Orbe", SituaPersonajeOrbe)
