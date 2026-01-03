import Bladex
import Levers
import AuxFuncs
import math
import ReadGSFile
import Doors
import Locks
import EnemyTypes
import Sounds
import pocimac
import Actions
import Scorer



B_PARTICLE_GTYPE_BLEND=1
B_PARTICLE_GTYPE_ADD=2


###########################
#     Puerta fuente 3     #
###########################

puertaf3desliz=Sounds.CreateEntitySound("../../Sounds/puerta-pie-desliz-no-loop.wav", "PuertaF3Desliz")
puertaf3golpe=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe2.wav", "PuertaF3Golpe")

puertaf3=Doors.CreateDoor("PuertaF3", (59500,-4000,-26000), (0,0,-1), 0, 2125, Doors.CLOSED)
puertaf3.Squezze=1

puertaf3.opentype=Doors.AC_UNIF
puertaf3.o_init_vel=0
puertaf3.o_init_displ=250
puertaf3.o_med_vel=-1000
puertaf3.o_med_displ=1875

puertaf3.closetype=Doors.AC_UNIF
puertaf3.c_init_vel=0
puertaf3.c_init_displ=250
puertaf3.c_med_vel=1000
puertaf3.c_med_displ=1875

puertaf3.SetWhileOpenSound(puertaf3desliz)
puertaf3.SetEndOpenSound(puertaf3golpe)

puertaf3.SetWhileCloseSound(puertaf3desliz)
puertaf3.SetEndCloseSound(puertaf3golpe)

llavepuertaf3=Bladex.CreateEntity("LlavePuertaF3","Llavecutre",0,0,0,"Physic")
llavepuertaf3.Solid=0
llavepuertaf3.Scale=1.4

cerradurapuertaf3=Locks.PlaceLock("CerraduraPuertaF3","Cerraduracutre",(58980.0,-3250.0,-27650.0),(0.000000,0.000000,0.707107,-0.707107),2.0)
cerradurapuertaf3.key="LlavePuertaF3"

######## Funcion: AbrePuertaF3()

######## Funcion: CierraPuertaF3()

cerradurapuertaf3.OnUnLockFunc=AbrePuertaF3
cerradurapuertaf3.OnUnLockArgs=()

cerradurapuertaf3.OnLockFunc=CierraPuertaF3
cerradurapuertaf3.OnLockArgs=()



############################
#     Orcos en la zona     #
############################

### Jefe orco guardando la puerta de acceso a la fuente 3. Areas 1 y 2.

potion=Bladex.CreateEntity("RuinsPotionOrkF3","Pocima50",0,0,0,"Physic")
potion.Solid=0
potion.Scale=1.220190
pocimac.CreatePotion("RuinsPotionOrkF3")

Gladius=Bladex.CreateEntity("RuinsSwordOrkF3","Hacha",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("RuinsEscOrkF3","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
ItemTypes.ItemDefaultFuncs(escudo)


pers=Bladex.CreateEntity("OrkF3","Great_Ork", 57000.0, -3109.0, -26000.0, "Person")
pers.Angle=3.0*3.14159/4.0
pers.Level=0
Actions.TakeObject(pers.Name,"RuinsSwordOrkF3")
Actions.TakeObject(pers.Name,"RuinsEscOrkF3")
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
Actions.TakeObject(pers.Name,"LlavePuertaF3")
Actions.TakeObject(pers.Name,"RuinsPotionOrkF3")
pers.SetOnFloor()

pers.Freeze()


### Dos orcos que aparecen cuando activamos las fuentes 1 y 2. Areas 17 y 18.

Gladius=Bladex.CreateEntity("RuinsGladiusOrk1F12","Garrote",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("RuinsEscOrk1F12","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("Ork1F12","Ork",34000,-1682,-24000, "Person")
pers.Angle=3.14159
pers.Level=2
Actions.TakeObject(pers.Name,"RuinsGladiusOrk1F12")
Actions.TakeObject(pers.Name,"RuinsEscOrk1F12")
pers.ActionAreaMin=pow(2,16)
pers.ActionAreaMax=pow(2,17)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Freeze()
pers.RemoveFromWorldWithChilds()


Gladius=Bladex.CreateEntity("RuinsGladiusOrk2F12","Gladius",0,0,0,"Weapon")
escudo=Bladex.CreateEntity("RuinsEscOrk2F12","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Gladius)
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("Ork2F12","Ork",24000,-1682,-34000, "Person")
pers.Angle=-3.14159/2.0
pers.Level=2
Actions.TakeObject(pers.Name,"RuinsGladiusOrk2F12")
Actions.TakeObject(pers.Name,"RuinsEscOrk2F12")
pers.ActionAreaMin=pow(2,16)
pers.ActionAreaMax=pow(2,17)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Freeze()
pers.RemoveFromWorldWithChilds()



###################
#     Objetos     #
###################

gema1=Bladex.CreateEntity("Gema1","Gemaazul",41645.0, -970.0, -43030.0)
gema1.Scale=2.000000
gema1.Orientation=0.500000,0.500000,-0.500000,-0.500000

gema2=Bladex.CreateEntity("Gema2","Gemaazul",41645.0, -1970.0, -43030.0)
gema2.Scale=2.000000
gema2.Orientation=0.500000,0.500000,-0.500000,-0.500000

gema3=Bladex.CreateEntity("Gema3","Gemaazul",41605.0, -1030.0, -55020.0)
gema3.Scale=2.000000
gema3.Orientation=0.500000,0.500000,0.500000,0.500000

gema4=Bladex.CreateEntity("Gema4","Gemaazul",41605.0, -2030.0, -55020.0)
gema4.Scale=2.000000
gema4.Orientation=0.500000,0.500000,0.500000,0.500000

gema5=Bladex.CreateEntity("Gema5","Gemaazul",42230.0, -1030.0, -55980.0)
gema5.Scale=2.000000
gema5.Orientation=0.000000,0.707107,0.707107,0.000000

gema6=Bladex.CreateEntity("Gema6","Gemaazul",42230.0, -2030.0, -55980.0)
gema6.Scale=2.000000
gema6.Orientation=0.000000,0.707107,0.707107,0.000000

gema7=Bladex.CreateEntity("Gema7","Gemaazul",54720.0, -970.0, -56020.0)
gema7.Scale=2.000000
gema7.Orientation=0.707107,-0.000000,0.000000,-0.707107

gema8=Bladex.CreateEntity("Gema8","Gemaazul",54720.0, -1970.0, -56020.0)
gema8.Scale=2.000000
gema8.Orientation=0.707107,-0.000000,0.000000,-0.707107

gema9=Bladex.CreateEntity("Gema9","Gemaazul",55355.0, -1030.0, -55020.0)
gema9.Scale=2.000000
gema9.Orientation=0.500000,0.500000,0.500000,0.500000

gema10=Bladex.CreateEntity("Gema10","Gemaazul",55355.0, -2030.0, -55020.0)
gema10.Scale=2.000000
gema10.Orientation=0.500000,0.500000,0.500000,0.500000

gema11=Bladex.CreateEntity("Gema11","Gemaazul",55395.0, -970.0, -43030.0)
gema11.Scale=2.000000
gema11.Orientation=0.500000,0.500000,-0.500000,-0.500000

gema12=Bladex.CreateEntity("Gema12","Gemaazul",55395.0, -1970.0, -43030.0)
gema12.Scale=2.000000
gema12.Orientation=0.500000,0.500000,-0.500000,-0.500000

gema13=Bladex.CreateEntity("Gema13","Gemaazul",54720.0, -970.0, -42020.0)
gema13.Scale=2.000000
gema13.Orientation=0.707107,-0.000000,0.000000,-0.707107

gema14=Bladex.CreateEntity("Gema14","Gemaazul",54720.0, -1970.0, -42020.0)
gema14.Scale=2.000000
gema14.Orientation=0.707107,-0.000000,0.000000,-0.707107

gema15=Bladex.CreateEntity("Gema15","Gemaazul",42230.0, -1030.0, -41980.0)
gema15.Scale=2.000000
gema15.Orientation=0.000000,0.707107,0.707107,0.000000

gema16=Bladex.CreateEntity("Gema16","Gemaazul",42230.0, -2030.0, -41980.0)
gema16.Scale=2.000000
gema16.Orientation=0.000000,0.707107,0.707107,0.000000


###################
#     Sonidos     #
###################

res=ReadGSFile.ReadGhostSectorFile("pozosnd.sf")
for igs in res:
  Bladex.AddGhostSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])
  Bladex.SetGhostSectorSound(igs["Name"],igs["Sonido"],igs["Volumen"],igs["VolumenBase"],
                             igs["DistanciaMinima"],igs["DistanciaMaxima"],igs["DistMaximaVertical"],igs["Escala"])

aguafuente1=Bladex.CreateSound("../../Sounds/agua-fuente-sobre-agua.wav", "AguaFuente1")
aguafuente2=Bladex.CreateSound("../../Sounds/agua-fuente-sobre-agua.wav", "AguaFuente2")
aguafuente3=Bladex.CreateSound("../../Sounds/agua-fuente-sobre-agua.wav", "AguaFuente3")

sonidopalanca=Bladex.CreateSound("../../Sounds/metal-lever3.wav", "SonidoPalanca")
sonidopalanca.Volume=0.5

sonidocanal12=Bladex.GetGhostSectorSound("Canal12")
sonidocanal3=Bladex.GetGhostSectorSound("Canal3")
sonidocascada12=Bladex.GetGhostSectorSound("Cascada12")
sonidocascada3=Bladex.GetGhostSectorSound("Cascada3")
sonidoringpozo=Bladex.GetGhostSectorSound("ringpozo")


####################
#     Palancas     #
####################

palancafuentes12=Levers.PlaceLever("PalancaFuentes12",Levers.LeverType2,(24020.0,-2250.0,-49000.0),(0.707107,0.707107,0.000000,0.000000),1.0)
palancafuentes12.mode=2

palancafuente3=Levers.PlaceLever("PalancaFuente3",Levers.LeverType2,(64116.415,-3250.0,-55104.836),(0.270598,0.270598,-0.653282,0.653282),1.0)
palancafuente3.mode=2

palancapozo12=Levers.PlaceLever("PalancaPozo12",Levers.LeverType3,(46150.0,2500.0,-48980.0),(0.500000,0.500000,-0.500000,0.500000),1.0)
palancapozo12.mode=2

palancapozo3=Levers.PlaceLever("PalancaPozo3",Levers.LeverType3,(50850.0,2500.0,-48980.0),(0.500000,0.500000,0.500000,-0.500000),1.0)
palancapozo3.mode=2


##########################
#     Barrera magica     #
##########################

MAX_AMP=400.0 #800.0
MIN_LEN=1000000.0 #200000.0

rayo1=Bladex.CreateEntity("Rayo1", "Entity ElectricBolt", 41625.0, -1000.0, -43000.0)
rayo1.Position=41625.0, -1000.0, -43000.0
rayo1.Target=41625.0, -1000.0, -55000.0
#rayo1.CoreGlowColor=
#rayo1.InnerGlowColor=
#rayo1.OuterGlowColor=
rayo1.MaxAmplitude=MAX_AMP
rayo1.MinSectorLength=MIN_LEN
rayo1.Active=1

rayo2=Bladex.CreateEntity("Rayo2", "Entity ElectricBolt", 41625.0, -2000.0, -43000.0)
rayo2.Position=41625.0, -2000.0, -43000.0
rayo2.Target=41625.0, -2000.0, -55000.0
rayo2.MaxAmplitude=MAX_AMP
rayo2.MinSectorLength=MIN_LEN
rayo2.Active=1

rayo3=Bladex.CreateEntity("Rayo3", "Entity ElectricBolt", 42250.0, -1000.0, -56000.0)
rayo3.Position=42250.0, -1000.0, -56000.0
rayo3.Target=54750.0, -1000.0, -56000.0
rayo3.MaxAmplitude=MAX_AMP
rayo3.MinSectorLength=MIN_LEN
rayo3.Active=1

rayo4=Bladex.CreateEntity("Rayo4", "Entity ElectricBolt", 42250.0, -2000.0, -56000.0)
rayo4.Position=42250.0, -2000.0, -56000.0
rayo4.Target=54750.0, -2000.0, -56000.0
rayo4.MaxAmplitude=MAX_AMP
rayo4.MinSectorLength=MIN_LEN
rayo4.Active=1

rayo5=Bladex.CreateEntity("Rayo5", "Entity ElectricBolt", 55375.0, -1000.0, -43000.0)
rayo5.Position=55375.0, -1000.0, -43000.0
rayo5.Target=55375.0, -1000.0, -55000.0
rayo5.MaxAmplitude=MAX_AMP
rayo5.MinSectorLength=MIN_LEN
rayo5.Active=1

rayo6=Bladex.CreateEntity("Rayo6", "Entity ElectricBolt", 55375.0, -2000.0, -43000.0)
rayo6.Position=55375.0, -2000.0, -43000.0
rayo6.Target=55375.0, -2000.0, -55000.0
rayo6.MaxAmplitude=MAX_AMP
rayo6.MinSectorLength=MIN_LEN
rayo6.Active=1

rayo7=Bladex.CreateEntity("Rayo7", "Entity ElectricBolt", 42250.0, -1000.0, -42000.0)
rayo7.Position=42250.0, -1000.0, -42000.0
rayo7.Target=54750.0, -1000.0, -42000.0
rayo7.MaxAmplitude=MAX_AMP
rayo7.MinSectorLength=MIN_LEN
rayo7.Active=1

rayo8=Bladex.CreateEntity("Rayo8", "Entity ElectricBolt", 42250.0, -2000.0, -42000.0)
rayo8.Position=42250.0, -2000.0, -42000.0
rayo8.Target=54750.0, -2000.0, -42000.0
rayo8.MaxAmplitude=MAX_AMP
rayo8.MinSectorLength=MIN_LEN
rayo8.Active=1

######## Funcion: LucesRayos()

LucesRayos()


### Muerte al tocar barrera magica

######## Funcion: MuerteBarreraMagica(trsector_name, entity_name)

Bladex.SetTriggerSectorFunc("BarreraMagica", "OnEnter", MuerteBarreraMagica)



################################################
#     Definicion de sistemas de particulas     #
################################################

Bladex.AddParticleGType("Agua","WaterParticle2",B_PARTICLE_GTYPE_BLEND,30)

for i in range(30):
	r=160
	g=160
	b=180
	a=20
	size=100.0
	Bladex.SetParticleGVal("Agua",i,r,g,b,a,size)


Bladex.AddParticleGType("AguaC","WaterParticle2",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	r=160
	g=160
	b=180
	a=60
	size=180.0
	Bladex.SetParticleGVal("AguaC",i,r,g,b,a,size)


Bladex.AddParticleGType("Espuma","SmokeParticle",B_PARTICLE_GTYPE_BLEND,10)

for i in range(10):
	aux=(10.0-i)/10.0
	r=160
	g=160
	b=180
	a=255*math.sqrt(1.0-aux)
	size=700.0*math.sqrt(1.0-aux)
	Bladex.SetParticleGVal("Espuma",i,r,g,b,a,size)


Bladex.AddParticleGType("Salpique","GenericParticle",B_PARTICLE_GTYPE_BLEND,30)

for i in range(30):
	aux=(30.0-i)/30.0
	r=160
	g=160
	b=180
	a=100*math.sqrt(1.0-aux)
	size=30.0*math.sqrt(1.0-aux)
	Bladex.SetParticleGVal("Salpique",i,r,g,b,a,size)


Bladex.AddParticleGType("Chispas","GenericParticle",B_PARTICLE_GTYPE_ADD,30)

for i in range(30):
	if i>10:
		aux=0.0
	else:
		aux=(10.0-i)/10.0
	r=100
	g=100
	b=255
	a=255*math.sqrt(1.0-aux)
	size=30.0*math.sqrt(1.0-aux)
	Bladex.SetParticleGVal("Chispas",i,r,g,b,a,size)


Bladex.AddParticleGType("ChispasM","GenericParticle",B_PARTICLE_GTYPE_ADD,20)

for i in range(20):
	if i>10:
		aux=0.0
	else:
		aux=(10.0-i)/10.0
	r=100
	g=100
	b=255
	a=255*math.sqrt(1.0-aux)
	size=15.0*math.sqrt(1.0-aux)
	Bladex.SetParticleGVal("ChispasM",i,r,g,b,a,size)



#######################################
#     Camara acceso inferior pozo     #
#######################################


######## Funcion: ReiniciaCamaraInfPozo()

######## Funcion: LanzaCamaraInfPozo(sector_index, entity_name)

######## Funcion: DesactivaCamaraInfPozo(sector_index, entity_name)

secdesactcamara=Bladex.GetSector(48500, 7000, -42000)
secactcamara=Bladex.GetSector(48500, 7000, -41000)

secdesactcamara.OnEnter=DesactivaCamaraInfPozo
secactcamara.OnEnter=LanzaCamaraInfPozo



##########################
#     Funcionamiento     #
##########################


### Funciones y variables comunes ###

palancasactivadas=0
despiertaorcos=0

######## Funcion: ReiniciaCamara()

######## Funcion: ActivaPalancaPozo(n)

######## Funcion: EspumaCascada(n)

######## Funcion: SalpiquePalanca(n)


### Barrera magica ###

######## Funcion: SaltaChispas(n)

######## Funcion: QuitaLuzGradual(ent_name, time)

######## Funcion: QuitaRayo(n)

######## Funcion: QuitaBarreraMagica()

### Fuentes 1 y 2 ###

######## Funcion: ArranqueFuentes12()

######## Funcion: CaidaFuentes12()

nivelagua12=-401.0

######## Funcion: SubeAguaFuentes12(ent_name, time)

######## Funcion: AguaFuentes12()

######## Funcion: IniciaCamara12()

######## Funcion: TravellingCamara12()

######## Funcion: CaidaCascada12()

######## Funcion: SubeSonidoCascada12Gradual(ent_name, time)

nivelaguacanal12=380.0

######## Funcion: SubeAguaCanal12(ent_name, time)

######## Funcion: AguaCanal12()

######## Funcion: LanzaFuentes12()


### Fuente 3 ###

######## Funcion: ArranqueFuente3()

######## Funcion: CaidaFuente3()

nivelagua3=-1651.0

######## Funcion: SubeAguaFuente3(ent_name, time)

######## Funcion: AguaFuente3()

######## Funcion: IniciaCamara3()

######## Funcion: TravellingCamara3()

######## Funcion: CaidaCascada3()

######## Funcion: SubeSonidoCascada3Gradual(ent_name, time)

nivelaguacanal3=380.0

######## Funcion: SubeAguaCanal3(ent_name, time)

######## Funcion: AguaCanal3()

######## Funcion: LanzaFuente3()


palancafuentes12.OnTurnOnFunc=LanzaFuentes12
palancafuentes12.OnTurnOnArgs=()

palancafuente3.OnTurnOnFunc=LanzaFuente3
palancafuente3.OnTurnOnArgs=()
