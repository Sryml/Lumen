import GameText

# Posicion del personaje
SectorInicioPos   = 163513.810757,6570.088476,584.177792
TablStartPosition = 163800, 6398,577
AnglStartPosition = -3.141592
AnimationName     = "tablilla_tumba"

# Camara
CameraName        = "tablilla_tumbaCamera01.cam"
CameraNumFrames   = 380

# Eventos de la camara
Event_CogeLaTablilla     = 32
Event_tTablillaDust1     =  92
Event_tTablillaDust2     = 104
Event_DesapareceTablilla = 330

ColorLuz = 108,139,220

# tablilla
tab=Bladex.CreateEntity("Tablilla3","Tablilla3",164491.810757,6570.088476,584.177792)
tab.Static=0
tab.Scale=2.006763
tab.Orientation=0.619804,0.365093,0.598538,-0.352566
tab.CastShadows=0
tab.Solid=0

# luz de la tablilla
luzta             = Bladex.CreateEntity("Luz2","Entity Spot",164214.623000,6010.844000,586.605000)
luzta.Color       = ColorLuz 
luzta.Intensity   = 18
luzta.Precission  = 0.09
luzta.CastShadows = 0
luzta.SizeFactor  = 2
luzta.Flick       = 0
tab.Link(luzta) 

#---------------------------------#
#     Escena de la tablilla       #
#---------------------------------#

Bladex.ReadAlphaBitMap("../../Data/Estrellita.bmp","Estrellita")

# Estrellitas y duendes
Bladex.AddParticleGType("Estrellitas","Estrellita",B_PARTICLE_GTYPE_BLEND,64)
for i in range(64):
	r=255.0
	g=255.0
	b=255.0
	a   = (i*255)/64
	size= (64-i)*2
	Bladex.SetParticleGVal("Estrellitas",i,r,g,b,a,size)


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


# Achalay my brother!

  
PosX  = 0
PosY  = 0
PosZ  = 0
Tick  = 0


  
Bladex.CreateTimer("TablillaTimer",0.020)

#
# Todavia me da cosa decir cojer pero bueno
#------------------------------------------------------
  
TabillaSector = Bladex.GetSector(SectorInicioPos[0], SectorInicioPos[1], SectorInicioPos[2])
TabillaSector.OnEnter = ComienzaAnimacionTablilla
#Bladex.SetCallCheck(1)