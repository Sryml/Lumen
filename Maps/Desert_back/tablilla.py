import GameText
import Reference

# Posicion del personaje
SectorInicioPos   = -63200.575000,1376.411000,124172.607000#-76559.2759695, 2335.2, 127218.943987
TablStartPosition = -63300.9804522, 1385.39213602, 124078.883426
AnglStartPosition = 3.1415
AnimationName     = "tablilla_tumba"

# Camara
CameraName        = "tablilla_desiertoCamera01.cam"
CameraNumFrames   = 380

# Eventos de la camara
Event_CogeLaTablilla     = 32
Event_tTablillaDust1     =  92
Event_tTablillaDust2     = 104
Event_DesapareceTablilla = 330

ColorLuz = 249,174,0

# Manueladas
Fog_Height = 9200

# tablilla
tab=Bladex.CreateEntity("Tablilla6","Tablilla6",-62454.575000,1376.411000,124172.607000)
tab.Static=0
tab.Scale=2.
tab.Orientation=0.408968,-0.606320,0.381369,0.565402
tab.Solid=0
tab.CastShadows=0
#tab.SelfIlum = -2

# luz de la tablilla
luzta             = Bladex.CreateEntity("Luz2","Entity Spot",-62154.575000,1376.411000,124172.607000)
luzta.Color       = ColorLuz 
luzta.Intensity   = 18
luzta.Precission  = 0.09
luzta.Visible     = 0
luzta.CastShadows = 0
luzta.SizeFactor  = 2
luzta.Flick       = 0
tab.Link(luzta) 



#---------------------------------#
#     Escena de la tablilla       #
#---------------------------------#

Bladex.ReadAlphaBitMap("../../Data/Estrellita.bmp","Estrellita")

Bladex.AddParticleGType("Chispas","Estrellita",B_PARTICLE_GTYPE_ADD,64)

for i in range(64):
	if i>40:
		traux=(i-40.0)/20.0
	elif i>30:
		traux=0.0
	else:
		traux=(30.0-i)/30.0
	r=249.0
	g=174.0
	b=0.0
	a=200.0*(1.0-traux)
	size=40.0*(1.0-traux)
	Bladex.SetParticleGVal("Chispas",i,r,g,b,a,size)


Bladex.AddParticleGType("Polvillo","SmokeParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	aux=(60.0-i)/60.0
	r=180
	g=180
	b=0
	a=160.0*(1.0-aux)**2.0
	size=40.0+aux*400.0
	Bladex.SetParticleGVal("Polvillo",i,r,g,b,a,size)

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


##LUZ DEL HUECO DEL TECHO

Bladex.AddParticleGType("LuzMagica","SmokeParticle",B_PARTICLE_GTYPE_ADD,120)

for i in range(120):
	if i>60:
		aux=(i-60.0)/60.0 # 1->0
	else:
		aux=(60.0-i)/60.0 # 0->1
	r=170
	g=170
	b=170
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
	r=180
	g=180
	b=10
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
	b=25
	a=100.0*(1.0-aux)**2.0
	size=100.0
	Bladex.SetParticleGVal("Energia2",i,r,g,b,a,size)



luzsolida=Bladex.CreateEntity("LuzSolidaTablilla", "Entity Particle System D2", tab.Position[0], tab.Position[1], tab.Position[2])
luzsolida.D = 0, -Fog_Height, 0
luzsolida.ParticleType="LuzSolida"
luzsolida.YGravity=0.0
luzsolida.Friction=0.01
luzsolida.PPS=Fog_Height/500
luzsolida.Velocity=-100.0, 0.0, 0.0
luzsolida.RandomVelocity=5.0
luzsolida.Time2Live=240


luzmagica=Bladex.CreateEntity("LuzMagicaTablilla", "Entity Particle System D1", tab.Position[0], tab.Position[1]-Fog_Height, tab.Position[2])
luzmagica.ParticleType="LuzMagica"
luzmagica.YGravity=0.0
luzmagica.Friction=0.01
luzmagica.PPS=35
luzmagica.Velocity=0.0, 100.0, 0.0
luzmagica.RandomVelocity=6.0
luzmagica.Time2Live=120

PosX  = 0
PosY  = 0
PosZ  = 0
Tick  = 0

  
Bladex.CreateTimer("TablillaTimer",0.020)


  
TabillaSector = Bladex.GetSector(SectorInicioPos[0], SectorInicioPos[1], SectorInicioPos[2])
TabillaSector.OnEnter = ComienzaAnimacionTablilla