import nails
import Actions
import Doors
import GameText
import ReadGSFile
import Button
import Sounds
import Reference

trampa =   nails.NailTrap(5000,2000,15000)

ColorLuz = 255,255,255

flechazo=Sounds.CreateEntitySound('../../Sounds/dart-shoot.wav', 'LaunchArrow')
flechazo.Volume=0.7; flechazo.MinDistance=7000; flechazo.MaxDistance=10000;

########################  Particulas usadas  ########################

# Polvillo
Bladex.AddParticleGType("Polvillo","SmokeParticle",B_PARTICLE_GTYPE_BLEND,128)
for i in range(128):
	if i>64:
		traux=0.0
	else:
		traux=(64.0-i)/64.0
	aux  = (128.0-i)/128.0
	r    = ColorLuz[0]
	g    = ColorLuz[1]
	b    = ColorLuz[2]
	a    = 150.0*(1.0-traux)**0.5
	size = 4.0+aux*400.0
	Bladex.SetParticleGVal("Polvillo",i,r,g,b,a,size)

Bladex.AddParticleGType("Estrellitas","Estrellita",B_PARTICLE_GTYPE_BLEND,64)

for i in range(64):
	r=255.0
	g=255.0
	b=255.0
	a   = (i*255)/64
	size= (64-i)*2
	Bladex.SetParticleGVal("Estrellitas",i,r,g,b,a,size)


#------------------------------------------------------------------#

TrampaId = Bladex.GetSector(19027, 10085, -1514).Index
trampa.AddSector(        19058, 10085, -4519 )
trampa.AddSector(        19027, 10085, -1514 )
trampa.AddSector(        18521, 10085, 1049  )
trampa.ActivationSector( 19027, 10085, -1514 )

trampa.AddPincho("Pinch1")
trampa.AddPincho("Pinch2")
trampa.AddPincho("Pinch3")
trampa.AddPincho("Pinch4")
trampa.AddPincho("Pinch5")
trampa.AddPincho("Pinch6")
trampa.Active = 0
trampa = None





Puerta_Mala=Doors.CreateDoor("PuertaMala", (19114.5624157, 10085.2, 12428.3122301), (0,1,0), 50, 4000, Doors.CLOSED)

Puerta_Mala.SetWhileOpenSound(piedradesliz)
Puerta_Mala.SetEndOpenSound(piedragolpe)

Puerta_Mala.opentype       = Doors.UNIF
Puerta_Mala.o_med_vel      = -7000
Puerta_Mala.o_med_displ    =  5000


Puerta_Mala.closetype      = Doors.UNIF
Puerta_Mala.c_med_vel      =  7000
Puerta_Mala.c_med_displ    =  5000
Puerta_Mala.Squezze = 1



sectOut=Bladex.GetSector(19045, 10085, 6660)

nArrows = ["","","","","","","","","","","","","","",""]


res=ReadGSFile.ReadGhostSectorFile("Tablilla.sf")
for igs in res:
   Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

Bladex.SetTriggerSectorFunc("tablilla", "OnEnter", DropALotOffArrows )

char = Bladex.GetEntity("Player1")
char.SendTriggerSectorMsgs = 1





#---------------------------------#
#     Escena de la tablitrap      #
#---------------------------------#


tab=Bladex.CreateEntity("Tablilla5","Tablilla5",18997,9983,20448)
tab.Static=1
tab.Scale=2.0
tab.Orientation=0.939120,0.341812,-0.032795,0.011936
tab.Solid=0

luzta=Bladex.CreateEntity("LuzTab","Entity Spot",18997,9983,20448)
luzta.Color=ColorLuz
luzta.Intensity=10
luzta.Precission=0.1
luzta.CastShadows=0
luzta.Visible=1
luzta.Flick=0
luzta.AngVel=0.1
luzta.SizeFactor = 2

tab.Link(luzta)

# Achalay my brother!

PosX  = 0
PosY  = 0
PosZ  = 0
Tick  = 0


Bladex.CreateTimer("TablillaTimer",0.020)

#
# Todavia me da cosa decir cojer pero bueno
#------------------------------------------------------

piedrus=Bladex.CreateEntity("Piedra Loca","Bloque",19000.759009,9711.906213,-17137.943086,"Physic")
piedrus.Scale=1.488864
piedrus.Orientation=0.707107,0.707107,0.000000,0.000000
darfuncs.SetHint(piedrus,"Trigger")



TabillaSector = Bladex.GetSector(20950, 10145, 14186)
TabillaSector.OnEnter = ComienzaAnimacionTablilla

c_button1 = Button.CreateButtonCombination(2,tablix,"")
button1 = c_button1.AddButton("Piedra Loca",0.5,(0,0,-1),800,0,0,1)

piedrus.Frozen=1
