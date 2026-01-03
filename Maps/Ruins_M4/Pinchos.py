import Bladex
import Doors
import Sounds
import Objects
import Levers
import InitDataField
import Sparks



MESSAGE_START_WEAPON=7
MESSAGE_STOP_WEAPON=8


###############################################################################
#     Trampa de pinchos asociada a la puerta de la piramide del principio     #
###############################################################################


clicktrampa=Bladex.CreateSound("../../Sounds/trap-clicked.wav", "ClickTrampa")
pinchosdeslizando1=Sounds.CreateEntitySound("../../Sounds/pincho-desliz.wav", "PinchosDeslizando1")
pinchosgolpeando1=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "PinchosGolpeando1")
pinchosdeslizando2=Sounds.CreateEntitySound("../../Sounds/pincho-desliz.wav", "PinchosDeslizando2")
pinchosgolpeando2=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "PinchosGolpeando2")

sectorpinchos12=Bladex.GetSector(40000.0, 750.0, 5000.0)
sectorpinchos34=Bladex.GetSector(40000.0, 750.0, -5000.0)


pinchopiramide1=Bladex.CreateEntity("PinchoPiramide1", "PinchoManuel", 42510.0, 1190.0, 7150.0,"Weapon")
pinchopiramide1.Scale=1.0
pinchopiramide1.Orientation=0.707107,0.707107,0.000000,0.000000
pinchopiramide1=Sparks.SetMetalSparkling("PinchoPiramide1")
pinchopiramide1.Frozen=1
InitDataField.Initialise(pinchopiramide1)
pinchopiramide1.Data.NoFXOnHit=1

pinchopiramide2=Bladex.CreateEntity("PinchoPiramide2", "PinchoManuel", 37470.0, 300.0, 7150.0,"Weapon")
pinchopiramide2.Scale=1.0
pinchopiramide2.Orientation=0.000000,0.000000,0.000000,1.000000
pinchopiramide2=Sparks.SetMetalSparkling("PinchoPiramide2")
pinchopiramide2.Frozen=1
InitDataField.Initialise(pinchopiramide2)
pinchopiramide2.Data.NoFXOnHit=1

pinchopiramide3=Bladex.CreateEntity("PinchoPiramide3", "PinchoManuel", 42510.0, 1190.0, -7150.0,"Weapon")
pinchopiramide3.Scale=1.0
pinchopiramide3.Orientation=0.707107,0.707107,0.000000,0.000000
pinchopiramide3=Sparks.SetMetalSparkling("PinchoPiramide3")
pinchopiramide3.Frozen=1
InitDataField.Initialise(pinchopiramide3)
pinchopiramide3.Data.NoFXOnHit=1

pinchopiramide4=Bladex.CreateEntity("PinchoPiramide4", "PinchoManuel", 37470.0, 300.0, -7150.0,"Weapon")
pinchopiramide4.Scale=1.0
pinchopiramide4.Orientation=0.000000,0.000000,0.000000,1.000000
pinchopiramide4=Sparks.SetMetalSparkling("PinchoPiramide4")
pinchopiramide4.Frozen=1
InitDataField.Initialise(pinchopiramide4)
pinchopiramide4.Data.NoFXOnHit=1


pinchopiramide1movil=Objects.CreateDinamicObject("PinchoPiramide1")
pinchopiramide2movil=Objects.CreateDinamicObject("PinchoPiramide2")
pinchopiramide3movil=Objects.CreateDinamicObject("PinchoPiramide3")
pinchopiramide4movil=Objects.CreateDinamicObject("PinchoPiramide4")
pinchopiramide1movil.Timer="Timer30"
pinchopiramide2movil.Timer="Timer30"
pinchopiramide3movil.Timer="Timer30"
pinchopiramide4movil.Timer="Timer30"

pinchopiramide1movil.Activado=0


######## Funcion: PinchoSolido(pinchos, n)


######## Funcion: LanzaPinchos12()


######## Funcion: LanzaPinchos34()



######## Funcion: LanzaTrampaPinchos12(sector, entity_name)


######## Funcion: LanzaTrampaPinchos34(sector, entity_name)


sectorpinchos12.OnEnter=LanzaTrampaPinchos12
sectorpinchos34.OnEnter=LanzaTrampaPinchos34


######## Funcion: otra()



###############################################
#     Puerta de la piramide del principio     #
###############################################


palancapiramide=Levers.PlaceLever("PalancaPiramide",Levers.LeverType2,(45763.0, 1100.0, 1722.0),(0.500000, 0.500000, 0.500000, -0.500000),1.0)
palancapiramide.mode=0


puertapiramide=Doors.CreateDoor("PuertaPiramide", (44300.0, 0.0, 0.0), (0, 1, 0), 350, 3600, Doors.CLOSED)
puertapiramide.Squezze=1

puertapiramide.closetype=Doors.AC


puertapiabr=Sounds.CreateEntitySound("../../Sounds/puerta-pie-desliz-no-loop.wav", "PuertaPiramideAbriendose")
puertapicerr=Sounds.CreateEntitySound("../../Sounds/puerta-pie-cerr-no-loop-rebote.wav", "PuertaPiramideCerrandose")


######## Funcion: ParaArenillaPuertaPiramide()


######## Funcion: AbrePuertaPiramide()


######## Funcion: CierraPuertaPiramide3()


######## Funcion: CierraPuertaPiramide2()


######## Funcion: CierraPuertaPiramide()


palancapiramide.OnTurnOnFunc=AbrePuertaPiramide
palancapiramide.OnTurnOnArgs=()

palancapiramide.OnTurnOffFunc=CierraPuertaPiramide
palancapiramide.OnTurnOffArgs=()



##########################################
#     Trampa de pincho del laberinto     #
##########################################


### Pinchos

pincholabizq=Bladex.CreateEntity("PinchoLaberintoIzq", "PinchoManuel", 65875.0, 2500.0, 20375.0,"Weapon")
pincholabizq.Scale=1.5
pincholabizq.Orientation=0.5, 0.5, 0.5, 0.5
pincholabizq.Frozen=1
pincholabizq.Solid=0

pincholabizqdin=Objects.CreateDinamicObject("PinchoLaberintoIzq")
pincholabizqdin.Timer="Timer30"

pincholabder=Bladex.CreateEntity("PinchoLaberintoDer", "PinchoManuel", 67000.0, 2500.0, 20375.0,"Weapon")
pincholabder.Scale=1.5
pincholabder.Orientation=0.5, 0.5, 0.5, 0.5
pincholabder.Frozen=1
pincholabder.Solid=0

pincholabderdin=Objects.CreateDinamicObject("PinchoLaberintoDer")
pincholabderdin.Timer="Timer30"

### Sectores

sector1pinizq=Bladex.GetSector(66125.0, 100.0, 20500.0)
sector2pinizq=Bladex.GetSector(65625.0, 100.0, 20375.0)
sector3pinizq=Bladex.GetSector(66000.0, 100.0, 20125.0)
sector1pinder=Bladex.GetSector(66875.0, 100.0, 20625.0)
sector2pinder=Bladex.GetSector(66750.0, 100.0, 20250.0)
sector3pinder=Bladex.GetSector(67250.0, 100.0, 20375.0)

sector1pinizq.Active=0
sector2pinizq.Active=0
sector3pinizq.Active=0
sector1pinder.Active=0
sector2pinder.Active=0
sector3pinder.Active=0

sector1pinizq.InitBreak((0.0, 250.0, 0.0), (300.0, 0.0, 0.0), (0.0, 0.0, 300.0))
sector2pinizq.InitBreak((0.0, 250.0, 0.0), (300.0, 0.0, 0.0), (0.0, 0.0, 300.0))
sector3pinizq.InitBreak((0.0, 250.0, 0.0), (300.0, 0.0, 0.0), (0.0, 0.0, 300.0))
sector1pinder.InitBreak((0.0, 250.0, 0.0), (300.0, 0.0, 0.0), (0.0, 0.0, 300.0))
sector2pinder.InitBreak((0.0, 250.0, 0.0), (300.0, 0.0, 0.0), (0.0, 0.0, 300.0))
sector3pinder.InitBreak((0.0, 250.0, 0.0), (300.0, 0.0, 0.0), (0.0, 0.0, 300.0))

sector1borpinizq=Bladex.GetSector(66062.5, 100.0, 20750.0)
sector2borpinizq=Bladex.GetSector(65625.0, 100.0, 20687.5)
sector3borpinizq=Bladex.GetSector(65500.0, 100.0, 20250.0)
sector4borpinizq=Bladex.GetSector(65875.0, 100.0, 19937.5)
sector5borpinizq=Bladex.GetSector(66250.0, 100.0, 20000.0)
sector1borpinder=Bladex.GetSector(66750.0, 100.0, 20000.0)
sector2borpinder=Bladex.GetSector(67312.5, 100.0, 20125.0)
sector3borpinder=Bladex.GetSector(67375.0, 100.0, 20562.5)
sector4borpinder=Bladex.GetSector(67000.0, 100.0, 20812.5)
sector5borpinder=Bladex.GetSector(66625.0, 100.0, 20750.0)

sector1borpinizq.Active=0
sector2borpinizq.Active=0
sector3borpinizq.Active=0
sector4borpinizq.Active=0
sector5borpinizq.Active=0
sector1borpinder.Active=0
sector2borpinder.Active=0
sector3borpinder.Active=0
sector4borpinder.Active=0
sector5borpinder.Active=0

sectorlanzapinchoslab=Bladex.GetSector(66500.0, -1000.0, 20000.0)
sector1guardapinchoslab=Bladex.GetSector(61000.0, -1000.0, 22000.0)
sector2guardapinchoslab=Bladex.GetSector(63000.0, -1000.0, 33000.0)

### Particulas

Bladex.AddParticleGType("Tierra","GenericParticle",B_PARTICLE_GTYPE_BLEND,120)

for i in range(120):
	if i>60:
		aux=0.0
	else:
		aux=(60-i)/60
	r=40
	g=30
	b=0
	a=255*(1.0-aux/2.0)
	size=40.0*(1.0-aux)
	Bladex.SetParticleGVal("Tierra",i,r,g,b,a,size)

### Sonidos

sonidoroturahueco=Bladex.CreateSound("../../Sounds/single-boulder-impact.wav", "SonidoRoturaHueco")
sonidopinchosaliendo=Sounds.CreateEntitySound("../../Sounds/blunt-impact3.wav", "SonidoPinchoSaliendo")

### Funcionamiento

huecopinchoslabcerrado=1

######## Funcion: SaltaTierra(x, y, z)

######## Funcion: RompeHuecoIzq()

######## Funcion: RompeHuecoDer()

######## Funcion: Solidifica(pincho)

######## Funcion: RecogePinchoIzq()

######## Funcion: LanzaPinchoIzq()

######## Funcion: RecogePinchoDer()

######## Funcion: LanzaPinchoDer()

######## Funcion: ParaPinchosLab(sector_index, entity_name)

######## Funcion: LanzaPinchosLab(sector_index, entity_name)

sectorlanzapinchoslab.OnWalkOn=LanzaPinchosLab
