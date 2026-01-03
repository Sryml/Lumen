import Bladex
import Sounds
import AuxFuncs
import Objects
import Actions
import Sparks



B_PARTICLE_GTYPE_BLEND=1
B_PARTICLE_GTYPE_ADD=2


##################
#     Varios     #
##################

Bladex.ReadBitMap("../../Data/espiritu.bmp","GlowSpirit")

Bladex.CreateTimer("Timer8",1.0/8.0)

Bladex.AddParticleGType("Voluta","SmokeParticle",B_PARTICLE_GTYPE_ADD,64)

for i in range(64):
	if i>50:
		traux=(i-50.0)/14.0 #va de 1 a 0
	else:
		traux=(50.0-i)/50.0 #va de 0 a 1
	aux=(64.0-i)/64.0 #va de 0 a 1
	r=180 #120
	g=255 #120
	b=120 #255
	a=75.0*(1.0-traux)
	size=400.0+aux*400.0
	Bladex.SetParticleGVal("Voluta",i,r,g,b,a,size)

Bladex.AddParticleGType("Volutilla","SmokeParticle",B_PARTICLE_GTYPE_ADD,32)

for i in range(32):
	if i>25:
		traux=0.0
	else:
		traux=(25.0-i)/25.0 #va de 0 a 1
	aux=(32.0-i)/32.0 #va de 0 a 1
	r=180 #120
	g=255 #120
	b=120 #255
	a=150.0*(1.0-traux)
	size=100.0+aux*600.0
	Bladex.SetParticleGVal("Volutilla",i,r,g,b,a,size)

Bladex.AddParticleGType("Energia","GenericParticle",B_PARTICLE_GTYPE_ADD,30)

for i in range(30):
	if i>10:
		traux=(i-10.0)/20.0 #va de 1 a 0
	else:
		traux=0.0
	r=180 #120
	g=255 #120
	b=120 #255
	a=255.0*(1.0-traux)
	size=30.0
	Bladex.SetParticleGVal("Energia",i,r,g,b,a,size)


###################
#     Objetos     #
###################

punterotumba=Bladex.CreateEntity("PunteroTumba","GhostPointer",-48825.0,-2750.0,-48250.0) # -48915.0,-2742.0,-48190.5)
punterotumba.Scale=1.000000
punterotumba.Orientation=0.000000,0.382683,0.000000,-0.923880

antmaus1=Bladex.CreateEntity("AntMaus1","AntorchaAtlante",-44908.918000,-2280.535000,-47604.007000)
antmaus1.Scale=1.000000
antmaus1.Orientation=0.270598,0.270598,0.653282,-0.653282
antmaus1=Sparks.SetStoneSparkling(antmaus1.Name)
antmaus1.FiresIntensity=[ 3 ]
antmaus1.Lights=[ (2.2,0.15,(255,170,80)) ]

antmaus2=Bladex.CreateEntity("AntMaus2","AntorchaAtlante",-49609.522000,-2280.265000,-42918.860000)
antmaus2.Scale=1.000000
antmaus2.Orientation=0.653282,0.653282,-0.270598,0.270598
antmaus2=Sparks.SetStoneSparkling(antmaus2.Name)
antmaus2.FiresIntensity=[ 3 ]
antmaus2.Lights=[ (2.2,0.15,(255,170,80)) ]

antmaus3=Bladex.CreateEntity("AntMaus3","AntorchaAtlante",-49383.959000,-2280.949000,-52092.334000)
antmaus3.Scale=1.000000
antmaus3.Orientation=0.270598,0.270598,0.653282,-0.653282
antmaus3=Sparks.SetStoneSparkling(antmaus3.Name)
antmaus3.FiresIntensity=[ 3 ]
antmaus3.Lights=[ (2.2,0.15,(255,170,80)) ]

antmaus4=Bladex.CreateEntity("AntMaus4","AntorchaAtlante",-54113.745000,-2280.702000,-47418.513000)
antmaus4.Scale=1.000000
antmaus4.Orientation=0.653282,0.653282,-0.270598,0.270598
antmaus4=Sparks.SetStoneSparkling(antmaus4.Name)
antmaus4.FiresIntensity=[ 3 ]
antmaus4.Lights=[ (2.2,0.15,(255,170,80)) ]

farolmaus=Bladex.CreateEntity("FarolMaus","Farol2",-44104.451000,-5740.405000,-42091.671000)
farolmaus.Scale=1.000000
farolmaus.Orientation=0.653282,0.653282,0.270598,-0.270598
farolmaus.FiresIntensity=[ 3 ]
farolmaus.Lights=[ (1.628895,0.1,(255,170,80)) ] #Precision original: 0.031250

lapida1=Bladex.CreateEntity("Lapida1","LapidaManuel",-43336.797000,-590.171000,-36082.811000)
lapida1.Scale=1.160969
lapida1.Orientation=0.326506,0.212631,-0.627211,0.674380
lapida1=Sparks.SetStoneSparkling(lapida1.Name)

lapida2=Bladex.CreateEntity("Lapida2","LapidaManuel",-45690.147000,-651.539000,-32107.332000)
lapida2.Scale=1.160969
lapida2.Orientation=0.270598,0.270598,-0.653282,0.653282
lapida2=Sparks.SetStoneSparkling(lapida2.Name)

lapida3=Bladex.CreateEntity("Lapida3","LapidaManuel",-42375.267000,-642.965000,-29584.274000)
lapida3.Scale=1.160969
lapida3.Orientation=0.681155,0.624164,0.282144,-0.258537
lapida3=Sparks.SetStoneSparkling(lapida3.Name)

lapida4=Bladex.CreateEntity("Lapida4","LapidaManuel",-37857.652000,-654.477000,-29631.080000)
lapida4.Scale=1.160969
lapida4.Orientation=0.270598,0.270598,-0.653282,0.653282
lapida4=Sparks.SetStoneSparkling(lapida4.Name)

lapida5=Bladex.CreateEntity("Lapida5","LapidaManuel",-31051.433000,-776.446000,-34819.847000)
lapida5.Scale=1.374941
lapida5.Orientation=0.270598,0.270598,-0.653282,0.653282
lapida5=Sparks.SetStoneSparkling(lapida5.Name)

lapida6=Bladex.CreateEntity("Lapida6","LapidaManuel",-31292.393000,-658.388000,-40121.996000)
lapida6.Scale=1.160969
lapida6.Orientation=0.270598,0.270598,-0.653282,0.653282
lapida6=Sparks.SetStoneSparkling(lapida6.Name)

lapida7=Bladex.CreateEntity("Lapida7","LapidaManuel",-34366.744000,-799.562000,-43251.460000)
lapida7.Scale=1.416603
lapida7.Orientation=0.270598,0.270598,-0.653282,0.653282
lapida7=Sparks.SetStoneSparkling(lapida7.Name)

lapida8=Bladex.CreateEntity("Lapida8","LapidaManuel",-38263.205000,-660.438000,-40855.057000)
lapida8.Scale=1.160969
lapida8.Orientation=0.653282,0.653282,0.270598,-0.270598
lapida8=Sparks.SetStoneSparkling(lapida8.Name)

lapida9=Bladex.CreateEntity("Lapida9","LapidaManuel",-40706.350000,-811.937000,-32884.466000)
lapida9.Scale=1.430769
lapida9.Orientation=0.270598,0.270598,-0.653282,0.653282
lapida9=Sparks.SetStoneSparkling(lapida9.Name)

lapida10=Bladex.CreateEntity("Lapida10","LapidaManuel",-35133.319000,-550.544000,-37773.891000)
lapida10.Scale=1.160969
lapida10.Orientation=0.313476,0.219498,-0.756798,0.529916
lapida10=Sparks.SetStoneSparkling(lapida10.Name)


####################
#     Sectores     #
####################

puertamau1=Bladex.GetSector(-46375.0, -3500.0, -42625.0)
puertamau1.Active=0

puertamau2=Bladex.GetSector(-46125.0, -3500.0, -42875.0)
puertamau2.Active=0

puertamau3=Bladex.GetSector(-45937.5, -3500.0, -43062.5)
puertamau3.Active=0

puertamau4=Bladex.GetSector(-45562.5, -3500.0, -43437.5)
puertamau4.Active=0

puertamau5=Bladex.GetSector(-45000.0, -3500.0, -44000.0)
puertamau5.Active=0

puertamau6=Bladex.GetSector(-44625.0, -3500.0, -44375.0)
puertamau6.Active=0

puertamau7=Bladex.GetSector(-44625.0, -2000.0, -44375.0)
puertamau7.Active=0


tumba1=Bladex.GetSector(-50000.0, -2750.0, -47750.0)
tumba1.Active=0

tumba2=Bladex.GetSector(-49250.0, -2750.0, -47500.0)
tumba2.Active=0

tumba3=Bladex.GetSector(-49750.0, -2750.0, -48125.0)
tumba3.Active=0

tumba4=Bladex.GetSector(-50500.0, -2750.0, -48375.0)
tumba4.Active=0


##########################
#     Luces y fuegos     #
##########################

luzantmaus1=AuxFuncs.GetSpot(antmaus1)
luzantmaus2=AuxFuncs.GetSpot(antmaus2)
luzantmaus3=AuxFuncs.GetSpot(antmaus3)
luzantmaus4=AuxFuncs.GetSpot(antmaus4)

fuegoantmaus1=AuxFuncs.GetFire(antmaus1)
fuegoantmaus2=AuxFuncs.GetFire(antmaus2)
fuegoantmaus3=AuxFuncs.GetFire(antmaus3)
fuegoantmaus4=AuxFuncs.GetFire(antmaus4)

luzfarolmaus=AuxFuncs.GetSpot(farolmaus)


####################
#     Espiritu     #
####################

spirit1=Bladex.CreateEntity("Spirit1", "Entity Spot", -49875.0, -2250.0, -47875.0)
spirit1.Color=180, 255, 128 #128, 128, 255
spirit1.Intensity=0.0
spirit1.Precission=0.06
#spirit1.Visible=1
spirit1.CastShadows=0
spirit1.GlowTexture="GlowSpirit"
#spirit1.GlowTestZ=1
spirit1.AngVel=3.14159
spirit1.SizeFactor=1.0

spirit2=Bladex.CreateEntity("Spirit2", "Entity Spot", -49875.0, -2250.0, -47875.0)
spirit2.Color=180, 255, 200 #200, 128, 255
spirit2.Intensity=0.0
spirit2.Precission=0.06
spirit2.CastShadows=0
spirit2.GlowTexture="GlowSpirit"
spirit2.AngVel=-3.14159
spirit2.SizeFactor=1.0

spirit1din=Objects.CreateDinamicObject("Spirit1")
spirit1din.Timer="Timer30"

estela=Bladex.CreateEntity("Estela", "Entity Particle System D1", -49875.0, -2250.0, -47875.0)
estela.ParticleType="Voluta"
estela.YGravity=500.0
estela.Friction=0.2
estela.PPS=32
estela.Velocity=0.0, 0.0, 0.0
estela.RandomVelocity=50.0
estela.Time2Live=64
estela.FollowFactor=0.4


###################
#     Sonidos     #
###################

sonidoroturamurofalso1=Bladex.CreateSound("../../Sounds/rotura-piedra.wav", "SonidoRoturaMuroFalso1") # single-boulder-impact.wav", "SonidoRoturaMuroFalso")
sonidoroturamurofalso1.Volume=1.0
sonidoroturamurofalso1.MinDistance=5000 #1000
sonidoroturamurofalso1.MaxDistance=50000 #25000

sonidoroturamurofalso2=Bladex.CreateSound("../../Sounds/derribo-puerta1.wav", "SonidoRoturaMuroFalso2") # single-boulder-impact.wav", "SonidoRoturaMuroFalso")
sonidoroturamurofalso2.Volume=1.0
sonidoroturamurofalso2.MinDistance=5000 #1000
sonidoroturamurofalso2.MaxDistance=50000 #25000

sndimplengua=Bladex.CreateSound("../../Sounds/energy-ball-impact.wav", "SonidoImpactoLengua")
sndimplengua.Volume=1.0
sndimplengua.MinDistance=5000 #1000
sndimplengua.MaxDistance=50000 #25000

sndespiritu=Bladex.CreateEntity("SonidoEspiritu", "Entity Sound", 0, 0, 0)
sndespiritu.SetSound("../../Sounds/Espiritus1.wav")
sndespiritu.Volume=1.0
sndespiritu.MinDistance=5000 #1000
sndespiritu.MaxDistance=50000 #25000
spirit1.Link(sndespiritu)

sndlengua=Bladex.CreateEntity("SonidoLengua", "Entity Sound", 0, 0, 0)
sndlengua.SetSound("../../Sounds/lanza-espiritu.wav")
sndlengua.Volume=1.0
sndlengua.MinDistance=5000 #1000
sndlengua.MaxDistance=50000 #25000
spirit1.Link(sndlengua)


#######################################
#     Preparacion derrumbamientos     #
#######################################

puertamau1.InitBreak((250.0, 0.0, 250.0), (600.0, 200.0, -600.0), (0.0, 1200.0, 0.0), "", 100.0, 0)
puertamau2.InitBreak((250.0, 0.0, 250.0), (600.0, 200.0, -600.0), (0.0, 1400.0, 0.0), "", 100.0, 0)
puertamau3.InitBreak((250.0, 0.0, 250.0), (600.0, 200.0, -600.0), (0.0, 1600.0, 0.0), "", 100.0, 0)
puertamau4.InitBreak((250.0, 0.0, 250.0), (600.0, 200.0, -600.0), (0.0, 1400.0, 0.0), "", 100.0, 0)
puertamau5.InitBreak((250.0, 0.0, 250.0), (600.0, 200.0, -600.0), (0.0, 1200.0, 0.0), "", 100.0, 0)
puertamau6.InitBreak((250.0, 0.0, 250.0), (600.0, 200.0, -600.0), (0.0, 1200.0, 0.0), "", 100.0, 0)
puertamau7.InitBreak((250.0, 0.0, 250.0), (600.0, 200.0, -600.0), (0.0, 1200.0, 0.0), "", 100.0, 0)

tumba1.InitBreak((0.0, 200.0, 0.0), (750.0, 0.0, 1050.0), (900.0, 0.0, -600.0), "", 100.0, 0)
tumba2.InitBreak((0.0, 200.0, 0.0), (1050.0, 0.0, 750.0), (600.0, 0.0, -900.0), "", 100.0, 0)
tumba3.InitBreak((0.0, 200.0, 0.0), (750.0, 0.0, 1050.0), (900.0, 0.0, -600.0), "", 100.0, 0)
tumba4.InitBreak((0.0, 200.0, 0.0), (1050.0, 0.0, 750.0), (600.0, 0.0, -900.0), "", 100.0, 0)

#puertamau1.InitBreak((250.0, 0.0, 250.0), (600.0, 50.0, -800.0), (50.0, 1200.0, 50.0), "", 100.0, 0)
#puertamau2.InitBreak((250.0, 0.0, 250.0), (600.0, 50.0, -800.0), (50.0, 1400.0, 50.0), "", 100.0, 0)
#puertamau3.InitBreak((250.0, 0.0, 250.0), (600.0, 50.0, -800.0), (50.0, 1600.0, 50.0), "", 100.0, 0)
#puertamau4.InitBreak((250.0, 0.0, 250.0), (600.0, 50.0, -800.0), (50.0, 1400.0, 50.0), "", 100.0, 0)
#puertamau5.InitBreak((250.0, 0.0, 250.0), (600.0, 50.0, -800.0), (50.0, 1200.0, 50.0), "", 100.0, 0)
#puertamau6.InitBreak((250.0, 0.0, 250.0), (600.0, 50.0, -800.0), (50.0, 1200.0, 50.0), "", 100.0, 0)
#puertamau7.InitBreak((250.0, 0.0, 250.0), (600.0, 50.0, -800.0), (50.0, 1200.0, 50.0), "", 100.0, 0)

#puertamau1.InitBreak((250.0, 100.0, 250.0), (300.0, 100.0, -300.0), (-100.0, 500.0, 100.0))
#puertamau2.InitBreak((250.0, -100.0, 250.0), (300.0, -100.0, -300.0), (100.0, 600.0, -100.0))
#puertamau3.InitBreak((250.0, 100.0, 250.0), (300.0, 100.0, -300.0), (-100.0, 700.0, 100.0))
#puertamau4.InitBreak((250.0, -100.0, 250.0), (300.0, -100.0, -300.0), (100.0, 600.0, -100.0))
#puertamau5.InitBreak((250.0, 100.0, 250.0), (300.0, 100.0, -300.0), (-100.0, 500.0, 100.0))
#puertamau6.InitBreak((250.0, -100.0, 250.0), (300.0, -100.0, -300.0), (100.0, 500.0, -100.0))
#puertamau7.InitBreak((250.0, 100.0, 250.0), (300.0, 100.0, -300.0), (-100.0, 500.0, 100.0))

#tumba1.InitBreak((0.0, 200.0, 0.0), (500.0, 0.0, 700.0), (600.0, 0.0, -400.0))
#tumba2.InitBreak((0.0, 200.0, 0.0), (700.0, 0.0, 500.0), (400.0, 0.0, -600.0))
#tumba3.InitBreak((0.0, 200.0, 0.0), (500.0, 0.0, 700.0), (600.0, 0.0, -400.0))
#tumba4.InitBreak((0.0, 200.0, 0.0), (700.0, 0.0, 500.0), (400.0, 0.0, -600.0))


##########################
#     Funcionamiento     #
##########################

######## Funcion: RompePuertaMaus()

######## Funcion: RompeLosa()

######## Funcion: ReiniciaCamaraMaus()

######## Funcion: MueveEstela()

######## Funcion: MueveEstelaYTarget()

######## Funcion: OcultaEspiritu()

######## Funcion: LanzaEspirituTemplo2()

######## Funcion: LanzaEspirituTemplo()

######## Funcion: CamaraExtTemplo()

######## Funcion: ImpactoLengua(lengua)

n_lengua=1

######## Funcion: LanzaLenguaEspiritu(lapida)

######## Funcion: EspirituPatio()

######## Funcion: LanzaEspirituPuerta()

######## Funcion: ElevaEspiritu()

######## Funcion: ApareceEspiritu()

######## Funcion: ComienzaCamaraMaus()

######## Funcion: BajaIntLuzMausGrad(ent_name, time)

######## Funcion: ApagaLucesMaus()

######## Funcion: EmpujaLosa2()

######## Funcion: EmpujaLosa()

######## Funcion: EnfilaYEmpuja(entity_name)

######## Funcion: Colocacion(obj_name, use_from)

punterotumba.UseFunc=Colocacion
