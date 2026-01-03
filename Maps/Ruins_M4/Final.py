import Bladex
import AuxFuncs
import B3DLib
import Objects
import math
import EnemyTypes
import Reference
import OnInitTake
import GameState
import GotoMapVars




### Sonidos

golpeescalon1=Bladex.CreateSound("../../Sounds/golpe-piedra-mediana.wav", "GolpeEscalon1")
golpeescalon1.Volume=0.4
golpeescalon1.MinDistance=5000 #1000
golpeescalon1.MaxDistance=50000 #25000

golpeescalon2=Bladex.CreateSound("../../Sounds/golpe-piedra-mediana.wav", "GolpeEscalon2")
golpeescalon2.Volume=0.4
golpeescalon2.MinDistance=5000 #1000
golpeescalon2.MaxDistance=50000 #25000

golpeescalonfinal=Bladex.CreateSound("../../Sounds/golpe-piedra-pesada.wav", "GolpeEscalonFinal")
golpeescalonfinal.Volume=1.0
golpeescalonfinal.MinDistance=5000 #1000
golpeescalonfinal.MaxDistance=50000 #25000

sndimplibro=Bladex.CreateEntity("SonidoImpLibro", "Entity Sound", 0, 0, 0)
sndimplibro.SetSound("../../Sounds/M-IMPACTO-FUEGO.wav")
sndimplibro.Volume=0.7
sndimplibro.MinDistance=5000 #1000
sndimplibro.MaxDistance=50000 #25000

sndimpdemonsello=Bladex.CreateEntity("SonidoImpDemonioSello", "Entity Sound", 0, 0, 0)
sndimpdemonsello.SetSound("../../Sounds/fireball-impact.wav")
sndimpdemonsello.Volume=1.0
sndimpdemonsello.MinDistance=5000 #1000
sndimpdemonsello.MaxDistance=50000 #25000

expldemonruins=Bladex.CreateEntity("ExplosionDemonRuins", "Entity Sound", 0, 0, 0)
expldemonruins.SetSound("../../Sounds/Fireball-Fire.wav")
expldemonruins.Volume=1.0
expldemonruins.MinDistance=5000 #1000
expldemonruins.MaxDistance=50000 #25000

sndchispaslibro=Bladex.CreateEntity("SonidoChispasLibro", "Entity Sound", 0, 0, 0)
sndchispaslibro.SetSound("../../Sounds/efecto-ruina-bucle1.wav")
sndchispaslibro.Volume=0.0
sndchispaslibro.MinDistance=5000 #1000
sndchispaslibro.MaxDistance=50000 #25000

sndfuegodemon=Bladex.CreateEntity("SonidoFuegoDemon", "Entity Sound", 0, 0, 0)
sndfuegodemon.SetSound("../../Sounds/fuego-loop.wav")
sndfuegodemon.Volume=0.0
sndfuegodemon.MinDistance=5000 #1000
sndfuegodemon.MaxDistance=50000 #25000


### Objetos y enemigos

anttempl1=Bladex.CreateEntity("AntorchaTemplo1","AntorchaAtlante",8429.102000,-2443.754000,7215.651000)
anttempl1.Scale=1.196147
anttempl1.Orientation=0.653282,0.653282,0.270598,-0.270598
anttempl1.FiresIntensity=[ 3 ]
anttempl1.Lights=[ (6.0,0.1,(255,170,80)) ]
anttempl2=Bladex.CreateEntity("AntorchaTemplo2","AntorchaAtlante",-7318.772000,-2444.282000,-7337.385000)
anttempl2.Scale=1.196147
anttempl2.Orientation=0.270598,0.270598,-0.653282,0.653282
anttempl2.FiresIntensity=[ 3 ]
anttempl2.Lights=[ (6.0,0.1,(255,170,80)) ]
anttempl3=Bladex.CreateEntity("AntorchaTemplo3","AntorchaAtlante",-7334.367000,-2440.177000,7324.560000)
anttempl3.Scale=1.196147
anttempl3.Orientation=0.653282,0.653282,-0.270598,0.270598
anttempl3.FiresIntensity=[ 3 ]
anttempl3.Lights=[ (6.0,0.1,(255,170,80)) ]
anttempl4=Bladex.CreateEntity("AntorchaTemplo4","AntorchaAtlante",8434.451000,-2442.171000,-7219.694000)
anttempl4.Scale=1.196147
anttempl4.Orientation=0.270598,0.270598,0.653282,-0.653282
anttempl4.FiresIntensity=[ 3 ]
anttempl4.Lights=[ (6.0,0.1,(255,170,80)) ]

lamptemplo=Bladex.CreateEntity("LamparaTemplo","Lampcolg",-6.549000,-15008.504000,5.468000)
lamptemplo.Scale=1.220190
lamptemplo.Orientation=0.707107,0.707107,0.000000,0.000000
lamptemplo.FiresIntensity=[ 3 ]
lamptemplo.Lights=[ (6.0,0.05,(255,90,30)) ]

o=Bladex.CreateEntity("NoName209","Varilla",-5.752000,-17079.011000,0.240000)
o.Scale=1.000000
o.Orientation=0.500000,0.500000,-0.500000,-0.500000

velonaltar=Bladex.CreateEntity("VelonAltar","Velon",5605.033000,-2923.215000,-793.175000)
velonaltar.Scale=1.160969
velonaltar.Orientation=0.707107,0.707107,0.000000,0.000000
velonaltar.FiresIntensity=[ 10 ]
velonaltar.Lights=[ (0.4,0.05,(255,170,80)) ]

libromag=Bladex.CreateEntity("LibroMagico","Libroabierto",6000.0,-2795.0,0.0,"Physic")
libromag.Scale=1.5
libromag.Orientation=0.5,0.5,-0.5,0.5
import MenuText
Reference.EntitiesSelectionData["LibroMagico"]=(4.0, 3000.0 , MenuText.GetMenuText("Book of Txaulapatok"))

libromagdin=Objects.CreateDinamicObject("LibroMagico")
libromagdin.Timer="Timer60"

librocer=Bladex.CreateEntity("LibroCerrado","Libro2",5641.465000,-2835.000000,853.852000)
librocer.Scale=1.5
librocer.Orientation=0.766044,0.000000,-0.642788,0.000000

demonio=Bladex.CreateEntity("DemonioDojo", "Little_Demon", 0.0, 0.0, 0.0, "Person")
EnemyTypes.EnemyDefaultFuncs(demonio)
demonio.Blind=1
demonio.Deaf=1
demonio.Alpha=0.0
demonio.RasterMode="Full"
demonio.Freeze()
demonio.RemoveFromWorld()


### Luces y fuegos

luzlibro=Bladex.CreateEntity("LuzLibro", "Entity Spot", 0.0, -4000.0, 0.0)
luzlibro.Color=80, 40, 255
luzlibro.Intensity=0.0
luzlibro.Precission=0.03125
luzlibro.Visible=0
luzlibro.CastShadows=0

lvelonaltar=AuxFuncs.GetSpot(velonaltar)
lvelonaltar.CastShadows=0

luzdemonio=Bladex.CreateEntity("LuzDemonio", "Entity Spot", 0.0, -1750.0, 0.0)
luzdemonio.Color=255, 50, 40
luzdemonio.Intensity=0.0
luzdemonio.Precission=0.03125
luzdemonio.Visible=0
luzdemonio.CastShadows=0

luzexpldemonio=Bladex.CreateEntity("LuzExplDemonio", "Entity Spot", 1500.0, -2750.0, 0.0)
luzexpldemonio.Color=255, 100, 80
luzexpldemonio.Intensity=0.0
luzexpldemonio.Precission=0.03125
luzexpldemonio.Visible=0
luzexpldemonio.CastShadows=0

luzexpldemoniodin=Objects.CreateDinamicObject("LuzExplDemonio")
luzexpldemoniodin.Timer="Timer30"

lanttempl1=AuxFuncs.GetSpot(anttempl1)
lanttempl2=AuxFuncs.GetSpot(anttempl2)
lanttempl3=AuxFuncs.GetSpot(anttempl3)
lanttempl4=AuxFuncs.GetSpot(anttempl4)

lanttempl1.CastShadows=0
lanttempl2.CastShadows=0
lanttempl3.CastShadows=0
lanttempl4.CastShadows=0

luzlamptemplo=AuxFuncs.GetSpot(lamptemplo)
fuelamptemplo=AuxFuncs.GetFire(lamptemplo)

fanttempl1=AuxFuncs.GetFire(anttempl1)
fanttempl2=AuxFuncs.GetFire(anttempl2)
fanttempl3=AuxFuncs.GetFire(anttempl3)
fanttempl4=AuxFuncs.GetFire(anttempl4)

lanttempl1.Move(0.0, 250.0, 0.0)
lanttempl2.Move(0.0, 250.0, 0.0)
lanttempl3.Move(0.0, 250.0, 0.0)
lanttempl4.Move(0.0, 250.0, 0.0)

lanttempl1.SizeFactor=0.75
lanttempl2.SizeFactor=0.75
lanttempl3.SizeFactor=0.75
lanttempl4.SizeFactor=0.75

lvelonaltar.SizeFactor=0.65


### Definicion de sistemas de particulas

Bladex.AddParticleGType("PolvoMedio","SmokeParticle",B_PARTICLE_GTYPE_BLEND,128)

for i in range(128):
	if i>64:
		traux=0.0
	else:
		traux=(64.0-i)/64.0
	aux=(128.0-i)/128.0
	r=255
	g=210
	b=190
	a=100.0*(1.0-traux)**0.5
	size=4.0+aux*400.0
	Bladex.SetParticleGVal("PolvoMedio",i,r,g,b,a,size)


Bladex.AddParticleGType("PolvoLigero","SmokeParticle",B_PARTICLE_GTYPE_BLEND,128)

for i in range(128):
	if i>64:
		traux=0.0
	else:
		traux=(64.0-i)/64.0
	aux=(128.0-i)/128.0
	r=255
	g=210
	b=190
	a=100.0*(1.0-traux)**0.5
	size=3.0+aux*300.0
	Bladex.SetParticleGVal("PolvoLigero",i,r,g,b,a,size)


Bladex.AddParticleGType("Polvillo","SmokeParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	aux=(60.0-i)/60.0
	r=255
	g=230
	b=210
	a=80.0*(1.0-aux)**2.0
	size=40.0+aux*200.0
	Bladex.SetParticleGVal("Polvillo",i,r,g,b,a,size)


Bladex.AddParticleGType("Energia2","GenericParticle",B_PARTICLE_GTYPE_ADD,120)

for i in range(120):
	if i>90:
		traux=1-((i-90.0)/30.0) #va de 0 a 1
	elif i<20:
		traux=i/20.0 #va de 1 a 0
	else:
		traux=1.0
	r=100
	g=100
	b=255
	a=255.0*traux
	size=20.0
	Bladex.SetParticleGVal("Energia2",i,r,g,b,a,size)





### Sectores y entidades deslizantes

#sectoresctemplo=Bladex.GetSector(8000.0, -500.0, 1000.0)

sectoresctemplo=Bladex.GetSector(8000.0, 0.0, 8000.0)

escalon1=Bladex.CreateEntity("Escalon1", "Entity Sliding Area", 8000.0, -800.0, 5000.0)
escalon2=Bladex.CreateEntity("Escalon2", "Entity Sliding Area", 8000.0, -800.0, 4500.0)
escalon3=Bladex.CreateEntity("Escalon3", "Entity Sliding Area", 8000.0, -800.0, 4000.0)
escalon4=Bladex.CreateEntity("Escalon4", "Entity Sliding Area", 8000.0, -1150.0, 3500.0)
escalon5=Bladex.CreateEntity("Escalon5", "Entity Sliding Area", 8000.0, -1150.0, 3000.0)
escalon6=Bladex.CreateEntity("Escalon6", "Entity Sliding Area", 8000.0, -1150.0, 2500.0)
escalon7=Bladex.CreateEntity("Escalon7", "Entity Sliding Area", 8000.0, -1150.0, 2000.0)
escalon8=Bladex.CreateEntity("Escalon8", "Entity Sliding Area", 8000.0, -1150.0, 1500.0)
escalon9=Bladex.CreateEntity("Escalon9", "Entity Sliding Area", 8000.0, -1150.0, 1000.0)
escalon10=Bladex.CreateEntity("Escalon10", "Entity Sliding Area", 8000.0, -1150.0, 500.0)
escalon11=Bladex.CreateEntity("Escalon11", "Entity Sliding Area", 8000.0, -1150.0, 0.0)
escalon12=Bladex.CreateEntity("Escalon12", "Entity Sliding Area", 8000.0, -1150.0, -500.0)

escalon1.SlidingSurface=0.0, -1.0, 0.0
escalon2.SlidingSurface=0.0, -1.0, 0.0
escalon3.SlidingSurface=0.0, -1.0, 0.0
escalon4.SlidingSurface=0.0, -1.0, 0.0
escalon5.SlidingSurface=0.0, -1.0, 0.0
escalon6.SlidingSurface=0.0, -1.0, 0.0
escalon7.SlidingSurface=0.0, -1.0, 0.0
escalon8.SlidingSurface=0.0, -1.0, 0.0
escalon9.SlidingSurface=0.0, -1.0, 0.0
escalon10.SlidingSurface=0.0, -1.0, 0.0
escalon11.SlidingSurface=0.0, -1.0, 0.0
escalon12.SlidingSurface=0.0, -1.0, 0.0



######################
### Funcionamiento ###
######################


###
# Variables y constantes
###

PI32=3.14159/32.0
PI24=3.14159/24.0
PI16=3.14159/16.0
PI12=3.14159/12.0
PI8=3.14159/8.0
PI=3.14159
_2PI=2*3.14159
_4PI=4*3.14159
orig=(0, 0, 0)
ejexy=(1.0/math.sqrt(2.0), 1.0/math.sqrt(2.0), 0)
ejeyz=(0, 1.0/math.sqrt(2.0), 1.0/math.sqrt(2.0))
ejexyz=(1.0/math.sqrt(3.0), 1.0/math.sqrt(3.0), 1.0/math.sqrt(3.0))
ejey=(0.0, 1.0, 0.0)
ejeyn=(0.0, -1.0, 0.0)

curr_fire_int=3.0

spcam_step=0
TOTAL_SPCAM_TIME=17.35
TOTAL_SPCAM_STEPS=TOTAL_SPCAM_TIME*60.0
SPCAM_ANGLE_VARIATION=2.0*3.14159/TOTAL_SPCAM_STEPS
SPCAM_HEIGHT_VARIATION=4500.0/TOTAL_SPCAM_STEPS
SPCAM_RADIUS=3000.0
vposplcamnorm=1.0/math.sqrt(2.0), 0.0, 1.0/math.sqrt(2.0)
initspcampos=vposplcamnorm[0]*SPCAM_RADIUS, -7000.0, vposplcamnorm[2]*SPCAM_RADIUS

dmcam_step=0
TOTAL_DMCAM_TIME=5.5 #6.5
TOTAL_DMCAM_STEPS=TOTAL_DMCAM_TIME*60.0
DEC_TIME=4.0 #5.0
DEC_STEPS=DEC_TIME*60.0
DMCAM_ANGLE=(5.0/4.0)*3.14159
DMCAM_ANGLE_VARIATION=DMCAM_ANGLE/TOTAL_DMCAM_STEPS
ANG_VEL=DMCAM_ANGLE/TOTAL_DMCAM_TIME
ANG_DEC=-ANG_VEL/DEC_TIME
DMCAM_HEIGHT=2500.0
DMCAM_HEIGHT_VARIATION=DMCAM_HEIGHT/TOTAL_DMCAM_STEPS
HGT_VEL=DMCAM_HEIGHT/TOTAL_DMCAM_TIME
HGT_DEC=-HGT_VEL/DEC_TIME
DMTRG_HEIGHT=-200.0
DMTRG_HEIGHT_VARIATION=DMTRG_HEIGHT/TOTAL_DMCAM_STEPS
TRG_VEL=DMTRG_HEIGHT/TOTAL_DMCAM_TIME
TRG_DEC=-TRG_VEL/DEC_TIME
DMCAM_INIT_RADIUS=6000.0
DMCAM_RADIUS=-3000.0
DMCAM_RADIUS_VARIATION=DMCAM_RADIUS/TOTAL_DMCAM_STEPS
RAD_VEL=DMCAM_RADIUS/TOTAL_DMCAM_TIME
RAD_DEC=-RAD_VEL/DEC_TIME
initdmcampos=vposplcamnorm[0]*DMCAM_INIT_RADIUS, -5000.0, vposplcamnorm[2]*DMCAM_INIT_RADIUS

sp_step=0
TOTAL_SP_TIME=7.5
TOTAL_SP_STEPS=TOTAL_SP_TIME*60.0
SP_ANGLE_VARIATION=-5.0*3.14159/TOTAL_SP_STEPS
SP_HEIGHT_VARIATION=-3500.0/TOTAL_SP_STEPS
SP_RADIUS=1800.0
SP_RADIUS_VARIATION=-1800.0/TOTAL_SP_STEPS
vposplspnorm=1.0/math.sqrt(2.0), 0.0, 1.0/math.sqrt(2.0)
initsppos=vposplspnorm[0]*SP_RADIUS, -1350.0, vposplspnorm[2]*SP_RADIUS


###
# Final con fundido
###

######## Funcion: FundidoFin():

OnInitTake.AddOnInitTakeEvent("LibroMagico",FundidoFin)


###
# Muerte demoniooo dojoooooo!!
###

######## Funcion: ReseteaCamaraFinal2():

######## Funcion: SubeIntLuzTemploGrad(ent_name, time):

######## Funcion: ApagaLuzBolaFuego(ent_name, time)

######## Funcion: ReapareceLibro()

######## Funcion: BolaSigueLuz()

######## Funcion: BolaPicado()

######## Funcion: BolaArriba()

######## Funcion: CamaraSigueBolaFuego(ent_name, time)

######## Funcion: CamaraMuerteDemonio()

######## Funcion: DesmaterializaDemonio(ent_name, time)

######## Funcion: BajaIntLuzLampara(ent_name, time)

######## Funcion: SubeLuzBolaFuego(ent_name, time)

######## Funcion: BolaFuegoMagico()

######## Funcion: MuerteDemonio(ent_name)


demonio.ImDeadFunc=MuerteDemonio

######## Funcion: m2()

######## Funcion: m()


###
# Aparicion demoniooo dojoooooo!!
###

######## Funcion: ReseteaCamaraFinal()

######## Funcion: SubeIntLuzLampara(ent_name, time)

######## Funcion: DespiertaDemonio2()

######## Funcion: DespiertaDemonio(ent_name)

######## Funcion: ApagaLuzDemonio(ent_name, time)

######## Funcion: MaterializaDemonio(ent_name, time)

######## Funcion: EnciendeLuzDemonio(ent_name, time)

######## Funcion: ReduceMegaSurtidor()

######## Funcion: LanzaMegaSurtidor2(v1, v2, v3)

######## Funcion: LanzaMegaSurtidor(v1, v2, v3)

######## Funcion: CortinaMagica2()

######## Funcion: ApagaExplosionLuzDemonio(ent_name, time)

######## Funcion: ExplosionLuzDemonio(ent_name, time)

######## Funcion: ExplosionDemonio()

######## Funcion: AparicionDemonio()

######## Funcion: CamaraEspiralDemonio(ent_name, time)

######## Funcion: CamaraAparicionDemonio()


###
# Magia
###

######## Funcion: CaeLibroSello()

######## Funcion: ApagaLuzLibroGrad(ent_name, time)

######## Funcion: ApagaLuzLibro()

lcol80_255=80.0
lcol40_20=40.0
lcol255_10=255.0
lcol80_255_var=(255.0-80.0)/60.0
lcol40_20_var=(40.0-20.0)/60.0
lcol255_10_var=(255.0-10.0)/60.0

######## Funcion: TornaLuzLibroRojaGrad(ent_name, time)

######## Funcion: TornaLuzLibroRoja()

######## Funcion: ExplosionLibro()

######## Funcion: ArrojaEspirituLibro()

######## Funcion: ElevaLibroSello()

######## Funcion: ElevaEspirituEspiral(ent_name, time)

spcol0_128=0.0
spcol0_180=0.0
spcol0_200=0.0
spcol0_255=0.0
spcol0_128_var=128.0/180.0
spcol0_180_var=180.0/180.0
spcol0_200_var=200.0/180.0
spcol0_255_var=255.0/180.0

######## Funcion: TranspEspiritu(ent_name, time)

######## Funcion: ReapareceEspiritu()

######## Funcion: SubeIntLuzLibroGrad(ent_name, time)

######## Funcion: EnciendeLuzLibro()

######## Funcion: DesciendeCamaraEspiral(ent_name, time)

######## Funcion: CortinaMagica()

######## Funcion: BajaIntLuzTemploGrad(ent_name, time)

######## Funcion: BajaLucesTemplo()

######## Funcion: FinPosaLibroSello()

######## Funcion: PosaLibroSello(ent_name, time)

######## Funcion: LlevaLibroSello()

######## Funcion: ElevaLibroAltar()


###
# Puerta de escalones
###

######## Funcion: SubeEscalon(sld_name)

escalon1.OnStopFunc=SubeEscalon


###
# Entrada jugador
###

######## Funcion: Gira(ent_name)

######## Funcion: SubeEscaleras()

######## Funcion: EncaraEscaleras(ent_name)

######## Funcion: EntrandoAlTemplo(sector_index, entity_name)

sectoresctemplo.OnEnter=EntrandoAlTemplo
