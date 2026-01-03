import math
import whrandom
import Sounds
import Objects
import dust
import Reference
import Ontake

#if Bladex.GetEntity(Bladex.GetEntity("Player1").GetInventory().GetSelectedQuiver()).Data.NumberOfArrows()==0:
#	if Bladex.GetEntity("QuiverInvPrb1_Arrow_5"):
#

# Sector de activacion
__SECTOR_FLECHA__  =  9165, -1116, 71245

# Flecha Central
__POSI_FLECHA__    =  5603,-1136,77922

# Delta de distancia
__DELTA_FLECHA__ =  3000

__FLECHA_KIND__ = "FlechaEnvenenada"

InsideTrapArrow=0


GolpeFuegoMaldito=Sounds.CreateEntitySound('../../Sounds/fireball-swing.wav', 'GolpeFuegoMaldito')
GolpeFuegoMaldito.Volume=1.0; GolpeFuegoMaldito.MinDistance=17000; GolpeFuegoMaldito.MaxDistance=30000

flechazo=Sounds.CreateEntitySound('../../Sounds/dart-shoot.wav', 'LaunchArrow')
flechazo.Volume=0.5; flechazo.MinDistance=7000; flechazo.MaxDistance=10000



SActivaTFlecha = Bladex.GetSector(__SECTOR_FLECHA__[0],__SECTOR_FLECHA__[1],__SECTOR_FLECHA__[2])
SActivaTFlecha.OnEnter = Entrampa
SActivaTFlecha.OnLeave = Saltrampa



#######################################################################################################################


MagickSull=Bladex.CreateEntity("MagickSull","Skull",18673.453447,-8792.544384,73086.349312)
MagickSull.Static=0
MagickSull.Scale=5
MagickSull.Orientation=0.319105,0.651398,0.301813,-0.618677
MagickSull.HitFunc = HitFuncSkull

luzAKalaVera=Bladex.CreateEntity("Ojera","Entity Spot",18223.0, -8532.0, 73256.0)
luzAKalaVera.Color=255,0,0
luzAKalaVera.Intensity=0.00001
luzAKalaVera.Precission=1
luzAKalaVera.CastShadows=0
luzAKalaVera.GlowTexture="MagicFlare128"
luzAKalaVera.GlowTestZ=1
luzAKalaVera.AngVel=0.5
luzAKalaVera.SizeFactor=0.5

luzBKalaVera=Bladex.CreateEntity("Ojera","Entity Spot",18223.0, -8532.0, 72886.0)
luzBKalaVera.Color=255,0,0
luzBKalaVera.Intensity=0.00001
luzBKalaVera.Precission=1
luzBKalaVera.CastShadows=0
luzBKalaVera.GlowTexture="MagicFlare128"
luzBKalaVera.GlowTestZ=1
luzBKalaVera.AngVel=-0.5
luzBKalaVera.SizeFactor=0.5

###### Definici�n de los sonidos de todas las puertas -incluyendo las objeto-

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")


##### Reja de la trampa de flechas #####

##definici�n rastrillos

rastmaz1=Bladex.CreateEntity("RastMaz1","Rastrillo2",24465.003183,-6463.061042,73199.368670)
rastmaz1.Static=0
rastmaz1.Scale=0.756836
rastmaz1.Orientation=0.504344,0.504344,0.495618,-0.495618
Sparks.SetMetalSparkling("RastMaz1")

rastmaz1din=Objects.CreateDinamicObject("RastMaz1")

CerradaTFPuerta = 1



SActivaCierraTF         = Bladex.GetSector(16379.1548412, -2099.84287386, 73390.9627987)
SActivaCierraTF.OnEnter = CierrTrampa

SActivaAbreTF         = Bladex.GetSector(-2077.97540751, -1116.36291412, 71039.7338797)
SActivaAbreTF.OnEnter = AbreTrampa



CreaSuperFlecha()




#char.Position = (-18608.2214689, 383.950073024, 73570.2600459)
#execfile("flechas_yo.py")