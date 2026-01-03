#   _______  _ _____ __     __  __    __        _   _____
#  /\__  __\| /  . / \   /\ \/\ \  /\ \     /| \ /   __\
#  \/_/\ \_/| ./   /_\ \    \ \ \ \ \ \ \    || ./____  \
#     \ \ \ |   /  . / \___ \ \ \ \_\ \ \___||   \ __/\  \
#      \ \_\|_|\_/____/____\ \_\ \____/____\|_|\_/_____/ (PUNTO PI!)
#       \/_//_//_//____//____/ /_/ /____//____//_//_//____/


########################################################################################################################
import Reference
import Select
import Change
import Actions
import Doors
import Bladex
import FireCheck
#import AniSound
import GameText
import Scorer
import Sounds
import LavaDefDamage

######################################################################################################################

#aqui el tiempo que tarda el acido en subir
aguaSUBE1LevfloodTime=60


################# F U N C I O N E S   C O M P A R T I D A S   P O R   L A S   P A R T E S  ########################

Bladex.AddParticleGType("dustAcidDoor","SmokeParticle",B_PARTICLE_GTYPE_BLEND,128)
for i in range(128):
	if i>64:
		traux=0.0
	else:
		traux=(64.0-i)/64.0
	aux=(128.0-i)/128.0
	r=200
	g=170
	b=140
	a=150.0*(1.0-traux)**0.5
	size=10.0+aux*600.0
	Bladex.SetParticleGVal("dustAcidDoor",i,r,g,b,a,size)

imax=101
Bladex.AddParticleGType("acidF","WaterParticle",B_PARTICLE_GTYPE_BLEND,imax)
for i in range(imax):
	r=109
	g=185
	b=30
	a=55
	size=400-(i/imax)*400
	Bladex.SetParticleGVal("acidF",i,r,g,b,a,size)


###################################################################################################################


############################## O B J E T O S ########################################################################

acidfalltarget=139177.808000,-12214.978000,-164601.817000
acidfallsource=140263.968000,-18597.363000,-165080.312000

gargaacidtarget=105300,-7427.629000,-176550
gargaacidsource=104300,-8827.629000,-177550
gargaacidDust  =104700, 5572, -177150
aAcidDust = ""

gargbacidtarget=104750,-6027.629000,-154800
gargbacidsource=102950,-8927.629000,-153000
gargbacidDust  =104250, 5472, -154200
bAcidDust = ""

tgargA=Bladex.CreateEntity("gar4","GargolaFernando",103546.062000,-9112.656000,-178381.937000)
tgargA.Static=0
tgargA.Scale=2.329790
tgargA.Orientation=0.264887,0.264887,-0.655618,0.655618

tgargB=Bladex.CreateEntity("gar1","GargolaFernando",102099.846000,-9265.797000,-152363.306000)
tgargB.Static=0
tgargB.Scale=2.194768
tgargB.Orientation=0.638224,0.638224,-0.304417,0.304417

tacidDamage = LavaDefDamage.LAVA_AREA()
tacidDamage.CreateLava ("agua2",139177.808000,-12014.978000,-164601.817000, "lava", 0.03 )
tacid=Bladex.GetEntity("agua2")
#tacid.Reflection=0.1
#tacid.Color=2,57,3

aguaSUBE1LevEnd= -10020
aguaSUBE1LevStart= 5900
aguaSUBE1Lev=aguaSUBE1LevStart
aguaSUBE1P=129750,-170000

aguaSUBE1Damage = LavaDefDamage.LAVA_AREA()
aguaSUBE1Damage.CreateLava ("aguaSUBE1",aguaSUBE1P[0],aguaSUBE1Lev,aguaSUBE1P[1] , "lava", 0.03 )
aguaSUBE1=Bladex.GetEntity("aguaSUBE1")
#aguaSUBE1.Reflection=0.1
#aguaSUBE1.Color=1,57,1


aguaSUBE2LevfloodTime=4.0
aguaSUBE2LevEnd= -12020
aguaSUBE2LevStart= -11520
aguaSUBE2Lev=aguaSUBE2LevStart
aguaSUBE2P=136250,-164750

aguaSUBE2Damage = LavaDefDamage.LAVA_AREA()
aguaSUBE2Damage.CreateLava ("aguaSUBE2" ,aguaSUBE2P[0],aguaSUBE2Lev,aguaSUBE2P[1] , "lava", 0.03 )
aguaSUBE2=Bladex.GetEntity("aguaSUBE2")
#aguaSUBE2.Reflection=0.1
#aguaSUBE2.Color=1,57,1

luztab1P=123000,-178500
luztab2P=131000,-173000
luztab3P=120250,-148500
luztab4P=129500,-156000
luztab5P=104500,-176000

luztab1=Bladex.CreateEntity("Luztab1","Entity Spot",luztab1P[0],aguaSUBE1Lev-2000,luztab1P[1])
luztab1.Color=91,166,64
luztab1.Intensity=83
luztab1.CastShadows=0
luztab1.Precission=0.5
luztab1.Visible=0
luztab1.Flick=0

luztab2=Bladex.CreateEntity("Luztab2","Entity Spot",luztab2P[0],aguaSUBE1Lev-2000,luztab2P[1])
luztab2.Color=101,176,54
luztab2.Intensity=39
luztab2.CastShadows=0
luztab2.Precission=0.1
luztab2.Visible=0
luztab2.Flick=0

luztab3=Bladex.CreateEntity("Luztab3","Entity Spot",luztab3P[0],aguaSUBE1Lev-2000,luztab3P[1])
luztab3.Color=91,166,94
luztab3.Intensity=83
luztab3.CastShadows=0
luztab3.Precission=0.5
luztab3.Visible=0
luztab3.Flick=0

luztab4=Bladex.CreateEntity("Luztab4","Entity Spot",luztab4P[0],aguaSUBE1Lev-2000,luztab4P[1])
luztab4.Color=101,176,54
luztab4.Intensity=39
luztab4.CastShadows=0
luztab4.Precission=0.1
luztab4.Visible=0
luztab4.Flick=0

luztab5=Bladex.CreateEntity("Luztab5","Entity Spot",luztab5P[0],aguaSUBE1Lev-2000,luztab5P[1])
luztab5.Color=101,176,94
luztab5.Intensity=39
luztab5.CastShadows=0
luztab5.Precission=0.1
luztab5.Visible=0
luztab5.Flick=0

rtablilla=Bladex.CreateEntity("Tablilla1","Tablilla1",115637.000000,-18396.000000-300,-164322.000000)
rtablilla.Static=0
rtablilla.Scale=2.026831 #+0.3 #ajuste a pelo
rtablilla.Orientation=0.312668,0.641065,0.307258,-0.629973
rtablilla.Solid=0


luztablillaintensity=15
luztablilla=Bladex.CreateEntity("Luztablilla","Entity Spot",115638.0, -19045.0, -164321.0)
luztablilla.Color=230,200,230
luztablilla.Intensity=luztablillaintensity
luztablilla.CastShadows=0
luztablilla.Precission=0.06
luztablilla.Visible=1
luztablilla.Flick=0
luztablilla.SizeFactor=0
rtablilla.Link(luztablilla)  # FIXME (link con offset)





aguaSUBE2FloodStartTime=0.0
stopSUBE1Flood=0
aguaSUBE1FloodStartTime=0.0
Bladex.CreateTimer("aguaSUBE2Flood",0.020)


tSceneAStartFlag=0
tSceneASector=Bladex.GetSector(135255.283397, 4043.8792931, -164508.132456)
#tSceneASector=Bladex.GetSector(130628.827126, 3683.39310035, -164315.243467)
tSceneASector.OnEnter=tSceneAStart

tablillaFadeStartTime=0.0
tablillafadetime=1.0
Bladex.CreateTimer("tablillaFadeTimer",0.1 )


tSceneBStartFlag=0

ChauLavaActivado = 0
tSceneBSector=Bladex.GetSector(115000,-21000,-164000)
tSceneBSector.OnEnter=tSceneBStart

###################################################################################################################
# char.Position = (168337.566523, 433.22650898, -162886.842062)
# aguaSUBE1Lev
# char.Move(1,1,1)
#

#######################################################
################# Efectos de tablilla #################
#######################################################

Bladex.ReadAlphaBitMap("../../Data/Estrellita.bmp","Estrellita")

Bladex.AddParticleGType("Chispas","Estrellita",B_PARTICLE_GTYPE_ADD,60)

for i in range(60):
	traux=(i)/60.0
	r=249.0
	g=249.0
	b=249.0
	a=255.0*(traux)
	size=80.0*(1.0-traux)
	Bladex.SetParticleGVal("Chispas",i,r,g,b,a,size)


#columna de particulas gordas

Bladex.AddParticleGType("LuzSolida","SmokeParticle",B_PARTICLE_GTYPE_ADD,240)

for i in range(240):
	if i>120:
		aux=(i-120.0)/120.0 # 1->0
	else:
		aux=(120.0-i)/120.0 # 0->1
	r=160
	g=120
	b=80
	a=70.0*(1.0-aux)**2.0
	size=1400.0
	Bladex.SetParticleGVal("LuzSolida",i,r,g,b,a,size)


luzsolida=Bladex.CreateEntity("LuzSolidaTablilla", "Entity Particle System D2", 115637,-18596,-164322)
luzsolida.D = 0, -3000, 0
luzsolida.ParticleType="LuzSolida"
luzsolida.YGravity=0.0
luzsolida.Friction=0.01
luzsolida.PPS=3000/500
luzsolida.Velocity=-100.0, 0.0, 0.0
luzsolida.RandomVelocity=5.0
luzsolida.Time2Live=240
