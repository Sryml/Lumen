import Bladex
import Objects
import Levers
import Sounds
import Button
import Actions
import FireCheck
import AuxFuncs
import Scorer
import InitDataField
import Doors
import Reference





Bladex.CreateTimer("Timer10",1.0/10.0)
Bladex.CreateTimer("Timer30",1.0/30.0)

MESSAGE_START_WEAPON=7
MESSAGE_STOP_WEAPON=8


############################
############################
###    Acceso secreto    ###
############################
############################


deslizpulruna=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-deslizando-2.wav", "DeslizaPulsadorRuna")
deslizpulruna.Volume=0.3
roturamuroruna=Sounds.CreateEntitySound("../../Sounds/single-boulder-impact.wav", "RoturaMuroRuna")
roturamuroruna.Position=3000, 4500, -27500
golpemuroagua=Sounds.CreateEntitySound("../../Sounds/high-watersplash.wav", "GolpeMuroAgua")
golpemuroagua.Position=3500, 4500, -27500

muroruna1=Bladex.GetSector(3000, 4500, -26375)
muroruna2=Bladex.GetSector(3000, 3750, -26375)
muroruna3=Bladex.GetSector(3000, 3000, -26375)
muroruna4=Bladex.GetSector(3000, 4500, -27500)
muroruna5=Bladex.GetSector(3000, 4500, -28375)
muroruna6=Bladex.GetSector(3000, 3500, -28375)
muroruna7=Bladex.GetSector(3000, 2750, -28375)
muroruna8=Bladex.GetSector(3000, 2250, -27000)
muroruna9=Bladex.GetSector(3000, 2000, -27500)
muroruna10=Bladex.GetSector(3000, 2400, -28000)

muroruna1.Active=0
muroruna2.Active=0
muroruna3.Active=0
muroruna4.Active=0
muroruna5.Active=0
muroruna6.Active=0
muroruna7.Active=0
muroruna8.Active=0
muroruna9.Active=0
muroruna10.Active=0

muroruna1.InitBreak((400.0, 0.0, 0.0), (0.0, 800.0, 0.0), (0.0, 0.0, 1000.0))
muroruna2.InitBreak((400.0, 0.0, 0.0), (0.0, 800.0, 0.0), (0.0, 0.0, 1000.0))
muroruna3.InitBreak((400.0, 0.0, 0.0), (0.0, 800.0, 0.0), (0.0, 0.0, 1000.0))
muroruna4.InitBreak((400.0, 0.0, 0.0), (0.0, 800.0, 0.0), (0.0, 0.0, 1000.0))
muroruna5.InitBreak((400.0, 0.0, 0.0), (0.0, 800.0, 0.0), (0.0, 0.0, 1000.0))
muroruna6.InitBreak((400.0, 0.0, 0.0), (0.0, 800.0, 0.0), (0.0, 0.0, 1000.0))
muroruna7.InitBreak((400.0, 0.0, 0.0), (0.0, 800.0, 0.0), (0.0, 0.0, 1000.0))
muroruna8.InitBreak((400.0, 0.0, 0.0), (0.0, 800.0, 0.0), (0.0, 0.0, 1000.0))
muroruna9.InitBreak((400.0, 0.0, 0.0), (0.0, 800.0, 0.0), (0.0, 0.0, 1000.0))
muroruna10.InitBreak((400.0, 0.0, 0.0), (0.0, 800.0, 0.0), (0.0, 0.0, 1000.0))

######## Funcion: CaidaMuroAgua()

######## Funcion: DisipaTemblor(ent_name, time)

######## Funcion: RompeMuroSecreto()

######## Funcion: EmpujaPulsadorRuna(ent_name, event)

######## Funcion: LanzaEmpujaPulsadorRuna(obj_name, use_from)

pulruna=Bladex.CreateEntity("PulsadorRuna","AdoquinRuna",2750.0,4670.0,-27350.0) # 2245.0,4670.0,-25850.0)
pulruna.Scale=1.2
pulruna.Orientation=0.707107,0.707107,0.000000,0.000000 # 0.500000,0.500000,-0.500000,0.500000
pulruna.UseFunc=LanzaEmpujaPulsadorRuna
import MenuText
Reference.EntitiesSelectionData[pulruna.Name]=(9.0,2000.0,MenuText.GetMenuText("Rune"))

pulrunadin=Objects.CreateDinamicObject("PulsadorRuna")

pulrunacaido=Bladex.CreateEntity("PulsadorRunaCaido","AdoquinRuna",2750.0,4670.0,-27350.0,"Physic") # 2245.0,4670.0,-25850.0)
pulrunacaido.Scale=1.2
pulrunacaido.Orientation=0.707107,0.707107,0.000000,0.000000 # 0.500000,0.500000,-0.500000,0.500000
Reference.EntitiesSelectionData[pulrunacaido.Name]=(0,0,"")
pulrunacaido.RemoveFromWorld()




####################
####################
###    Trampa    ###
####################
####################


### Preparacion ###

lp1=Bladex.CreateEntity("LP1","Lanzapivotes",20720.000000,12000.000000,-14750.000000)
lp1.Static=1
lp1.Scale=1.533978
lp1.Orientation=0.500000,0.500000,-0.500000,0.500000
lp1.CastShadows=0

lp2=Bladex.CreateEntity("LP2","Lanzapivotes",25036.000000,12000.000000,-9750.000000)
lp2.Static=1
lp2.Scale=1.533978
lp2.Orientation=0.500000,0.500000,0.500000,-0.500000
lp2.CastShadows=0

lp3=Bladex.CreateEntity("LP3","Lanzapivotes",20722.000000,12000.000000,-4750.000000)
lp3.Static=1
lp3.Scale=1.533978
lp3.Orientation=0.500000,0.500000,-0.500000,0.500000
lp3.CastShadows=0

pasarelaizq=Bladex.CreateEntity("PasarelaIzq","PasarelaLarga",21515.000000,11300.000000,-9750.000000)
pasarelaizq.Static=1
pasarelaizq.Scale=1.361327
pasarelaizq.Orientation=0.707107,0.707107,0.000000,0.000000
pasarelaizq.CastShadows=0

pasarelader=Bladex.CreateEntity("PasarelaDer","PasarelaLarga",24235.000000,11300.000000,-9750.000000)
pasarelader.Static=1
pasarelader.Scale=1.361327
pasarelader.Orientation=0.707107,0.707107,-0.000000,0.000000
pasarelader.CastShadows=0

cuchizq=Bladex.CreateEntity("CuchillaIzq","CuchillaFernando",18050.000000,10700.000000,-14250.000000,"Weapon")
cuchizq.Scale=1.160969
cuchizq.Orientation=0.000000,1.000000,0.000000,0.000000
cuchizq.Frozen=1
cuchizq.ContinuousDamage=1
cuchizq.Solid=0
cuchizq.CastShadows=0
InitDataField.Initialise(cuchizq)
cuchizq.Data.NoFXOnHit=1

cuchder=Bladex.CreateEntity("CuchillaDer","CuchillaFernando",27700.000000,10700.000000,-14250.000000,"Weapon")
cuchder.Scale=1.160969
cuchder.Orientation=0.000000,1.000000,0.000000,0.000000
cuchder.Frozen=1
cuchder.ContinuousDamage=1
cuchder.Solid=0
cuchder.CastShadows=0
InitDataField.Initialise(cuchder)
cuchder.Data.NoFXOnHit=1


pasarelaizqdin=Objects.CreateDinamicObject("PasarelaIzq")
pasareladerdin=Objects.CreateDinamicObject("PasarelaDer")
cuchizqdin=Objects.CreateDinamicObject("CuchillaIzq")
cuchderdin=Objects.CreateDinamicObject("CuchillaDer")
pasarelaizqdin.Timer="Timer30"
pasareladerdin.Timer="Timer30"
cuchizqdin.Timer="Timer30"
cuchderdin.Timer="Timer30"


luz1=Bladex.CreateEntity("Luz1", "Entity Spot", 22875.0, 12500.0, -14750.0)
luz1.Color=255, 140, 40
luz1.Intensity=0.0
luz1.Visible=0
luz1.CastShadows=0

luz2=Bladex.CreateEntity("Luz2", "Entity Spot", 22875.0, 12500.0, -9750.0)
luz2.Color=255, 140, 40
luz2.Intensity=0.0
luz2.Visible=0
luz2.CastShadows=0

luz3=Bladex.CreateEntity("Luz3", "Entity Spot", 22875.0, 12500.0, -4750.0)
luz3.Color=255, 140, 40
luz3.Intensity=0.0
luz3.Visible=0
luz3.CastShadows=0


deslizpasizq=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizPasIzq")
deslizpasizq.MinDistance=4000
deslizpasizq.MaxDistance=15000
golpepasizq=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe2.wav", "GolpePasIzq")
golpepasizq.MinDistance=4000
golpepasizq.MaxDistance=15000
deslizpasder=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizPasDer")
deslizpasder.MinDistance=4000
deslizpasder.MaxDistance=15000
golpepasder=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe2.wav", "GolpePasDer")
golpepasder.MinDistance=4000
golpepasder.MaxDistance=15000

sonidollamarada=Bladex.CreateSound("../../Sounds/surtidor-fuego.wav", "SonidoLlamarada")

sonido1cuchilla1=Sounds.CreateEntitySound('../../Sounds/blade-trap.wav', 'Sonido1Cuchilla1')
sonido1cuchilla2=Sounds.CreateEntitySound('../../Sounds/blade-trap.wav', 'Sonido1Cuchilla2')
sonido2cuchilla1=Sounds.CreateEntitySound('../../Sounds/woodenplatform-loop.wav', 'Sonido2Cuchilla1')
sonido2cuchilla2=Sounds.CreateEntitySound('../../Sounds/woodenplatform-loop.wav', 'Sonido2Cuchilla2')

sonidoactdes=Bladex.CreateSound('../../Sounds/trap-clicked.wav', 'SonidoActDes')

### Chequeadores

######## Funcion: FlameDamage(prtl_name,hit_entity,x,y,z,vx,vy,vz,wcx,wcy,wcz,wdx,wdy,wdz)

chllama1=FireCheck.createPSysChecker()
chllama1.precission=2
chllama1.onHitFunc=FlameDamage

chllama2=FireCheck.createPSysChecker()
chllama2.precission=2
chllama2.onHitFunc=FlameDamage

chllama3=FireCheck.createPSysChecker()
chllama3.precission=2
chllama3.onHitFunc=FlameDamage


### Funcionamiento ###

tractivada=0

######## Funcion: EnciendeLuzLlamGrad(ent_name, time)

######## Funcion: EnciendeLuzLlamarada(flame_n)

######## Funcion: ApagaLuzLlamGrad(ent_name, time)

######## Funcion: ApagaLuzLlamarada(flame_n)

######## Funcion: LanzaSurtidor(flame_n)

VUELTASDURANTE=100*(2*3.14159)
VUELTASINICIO=3*(2*3.14159)
VUELTASFIN=6*(2*3.14159)
VELGIRO=8.0

######## Funcion: GiraCuchillas()

######## Funcion: IniciaGiraCuchillas()

######## Funcion: TerminaGiraCuchillas()

######## Funcion: RecolocaCuchilla(ncuchilla)

######## Funcion: RecogeCuchilla(ncuchilla)

######## Funcion: DesplazaCuchilla(ncuchilla)

######## Funcion: LanzaCuchilla(ncuchilla)

sectorlanzatrampa=Bladex.GetSector(22000, 10000, 1000)
sectorparatrampa=Bladex.GetSector(22000, 10000, -20000)

######## Funcion: ParaTrampa(sec_index, ent_name)

######## Funcion: LanzaTrampa(sec_index, ent_name)

######## Funcion: AbreTrampa()

######## Funcion: CierraTrampa()




######################
######################
###    Tablilla    ###
######################
######################


Bladex.ReadAlphaBitMap("../../Data/Estrellita.bmp","Estrellita")

ls=Bladex.CreateEntity("LuzSolida","Entity Spot",33000.0, 6200.0, 1000.0)
ls.Color=10, 140, 255
ls.Intensity=8
ls.Precission=0.03125
ls.Visible=0

tab=Bladex.CreateEntity("Tablilla2", "Tablilla2", 33137.0674797, 9898.73625443, 910.410864308)
tab.Static=1
tab.Scale=2.0
tab.Orientation=0.61795938015, 0.329014241695, 0.620333433151, -0.353641480207

luztab=Bladex.CreateEntity("LuzTablilla", "Entity Spot", 32797.7392561, 9892.42437652, 910.410864308)
luztab.Color=100, 100, 255
luztab.Intensity=0.8
luztab.Precission=0.1
luztab.Visible=0
luztab.CastShadows=0
luztab.Flick=0


Bladex.AddParticleGType("Chispas","Estrellita",B_PARTICLE_GTYPE_ADD,60)

for i in range(60):
	if i>40:
		traux=(i-40.0)/20.0
	elif i>30:
		traux=0.0
	else:
		traux=(30.0-i)/30.0
	r=100.0
	g=100.0
	b=255.0
	a=200.0*(1.0-traux)
	size=40.0*(1.0-traux)
	Bladex.SetParticleGVal("Chispas",i,r,g,b,a,size)


Bladex.AddParticleGType("Polvillo","SmokeParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	aux=(60.0-i)/60.0
	r=180
	g=180
	b=255
	a=160.0*(1.0-aux)**2.0
	size=40.0+aux*400.0
	Bladex.SetParticleGVal("Polvillo",i,r,g,b,a,size)


Bladex.AddParticleGType("LuzSolida","SmokeParticle",B_PARTICLE_GTYPE_ADD,240)

for i in range(240):
	if i>120:
		aux=(i-120.0)/120.0 # 1->0
	else:
		aux=(120.0-i)/120.0 # 0->1
	r=160
	g=160
	b=255
	a=70.0*(1.0-aux)**2.0
	size=1400.0
	Bladex.SetParticleGVal("LuzSolida",i,r,g,b,a,size)


Bladex.AddParticleGType("LuzMagica","SmokeParticle",B_PARTICLE_GTYPE_ADD,120)

for i in range(120):
	if i>60:
		aux=(i-60.0)/60.0 # 1->0
	else:
		aux=(60.0-i)/60.0 # 0->1
	r=170
	g=170
	b=255
	a=180.0*(1.0-aux)**2.0
	size=1200.0
	Bladex.SetParticleGVal("LuzMagica",i,r,g,b,a,size)


Bladex.AddParticleGType("Energia","GenericParticle",B_PARTICLE_GTYPE_ADD,120)

for i in range(120):
	if i>90:
		traux=1-((i-90.0)/30.0) #va de 0 a 1
	elif i<20:
		traux=i/20.0 #va de 1 a 0
	else:
		traux=1.0
	r=80
	g=80
	b=255
	a=255.0*traux
	size=14.0
	Bladex.SetParticleGVal("Energia",i,r,g,b,a,size)


Bladex.AddParticleGType("Energia2","GenericParticle",B_PARTICLE_GTYPE_ADD,60)

for i in range(60):
	if i>57:
		aux=(i-57.0)/3.0 # 1->0
	else:
		aux=(57.0-i)/57.0 # 0->1
	r=120
	g=120
	b=255
	a=100.0*(1.0-aux)**2.0
	size=100.0
	Bladex.SetParticleGVal("Energia2",i,r,g,b,a,size)


######## Funcion: ParticulasTablilla()

ParticulasTablilla()

######## Funcion: Repite()



### Puerta y antorcha


antpaltab=Bladex.GetEntity("Ant2Trampa")
lantpaltab=AuxFuncs.GetSpot(antpaltab)
fantpaltab=AuxFuncs.GetFire(antpaltab)

#deslizhojaizq=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizHojaIzq")
#golpehojaizq=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe2.wav", "GolpeHojaIzq")
deslizhojader=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizHojaDer")
golpehojader=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe2.wav", "GolpeHojaDer")

hojaizq=Doors.CreateDoor("HojaIzq", (26750.0, 9000.0, 1500.0), (0,0,-1), 0, 1750, Doors.CLOSED)

hojaizq.opentype=Doors.AC_UNIF
hojaizq.o_init_vel=0
hojaizq.o_init_displ=250
hojaizq.o_med_vel=-350
hojaizq.o_med_displ=1500

hojaizq.closetype=Doors.UNIF
hojaizq.c_med_displ=1750
hojaizq.c_med_vel=450

#hojaizq.SetWhileOpenSound(deslizhojaizq)
#hojaizq.SetEndOpenSound(golpehojaizq)

#hojaizq.SetWhileCloseSound(deslizhojaizq)
#hojaizq.SetEndCloseSound(golpehojaizq)

hojader=Doors.CreateDoor("HojaDer", (26750.0, 9000.0, 500.0), (0,0,1), 0, 1750, Doors.CLOSED)

hojader.opentype=Doors.AC_UNIF
hojader.o_init_vel=0
hojader.o_init_displ=250
hojader.o_med_vel=-350
hojader.o_med_displ=1500

hojader.closetype=Doors.UNIF
hojader.c_med_displ=1750
hojader.c_med_vel=450

hojader.SetWhileOpenSound(deslizhojader)
hojader.SetEndOpenSound(golpehojader)

hojader.SetWhileCloseSound(deslizhojader)
hojader.SetEndCloseSound(golpehojader)


######## Funcion: AbrePuertaTablilla()

######## Funcion: CierraPuertaTablilla2()

######## Funcion: CierraPuertaTablilla()

hojaizq.OnEndCloseFunc=CierraPuertaTablilla2

fireint=0.0

######## Funcion: EnciendeLuzGrad(ent_name, time)

######## Funcion: EnciendeLuz()

######## Funcion: ReduceLuzGrad(ent_name, time)

######## Funcion: ReduceLuz()

######## Funcion: FinalEscenaTablilla(camera, frame)

######## Funcion: MueveLuz(ent_name, time)

######## Funcion: CogeTablilla(camera, frame)

######## Funcion: PolvoTablilla(camera, frame)

TABTRVAR=1.0/120.0
TABSCLVAR=2.0/120.0
TABINTVAR=0.8/120.0
TABESTTIME=2.5

######## Funcion: DesapareceTablillaGrad(ent_name, time)

######## Funcion: LanzaEstelaChispas(ent_name, time)

######## Funcion: Incandescencia(camera, frame)

######## Funcion: DesapareceTablilla(camera, frame)

######## Funcion: ContinuaEscenaTablilla()

######## Funcion: PreparaLocucion()

tablillacogida=0

######## Funcion: InicioEscenaTablilla()



paltablilla=Levers.PlaceLever("PalTablilla",Levers.LeverType3,(19640.776000,9650.000000,1000.000000),(0.500000,0.500000,-0.500000,0.500000),1.0)

paltablilla.mode=0

paltablilla.OnTurnOnFunc=InicioEscenaTablilla
paltablilla.OnTurnOnArgs=()

paltablilla.OnTurnOffFunc=CierraPuertaTablilla
paltablilla.OnTurnOffArgs=()
