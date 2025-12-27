import Traps_C
import Bladex

MESSAGE_START_WEAPON			=	7
MESSAGE_STOP_WEAPON				=	8
B_PARTICLE_GTYPE_BLEND			=	1

Bladex.AddParticleGType("Dust1","SmokeParticle",B_PARTICLE_GTYPE_BLEND,15)

for i in range(15):
	aux=(15.0-i)/15.0
	r=255
	g=230
	b=210
	a=80.0*(1.0-aux)**0.5
	size=1.0+aux*350.0
	Bladex.SetParticleGVal("Dust1",i,r,g,b,a,size)

Bladex.AddParticleGType("Dust2","SmokeParticle",B_PARTICLE_GTYPE_BLEND,15)

for i in range(15):
	aux=(15.0-i)/15.0
	r=255
	g=230
	b=210
	a=80.0*(1.0-aux)**0.5
	size=1.0+aux*250.0
	Bladex.SetParticleGVal("Dust2",i,r,g,b,a,size)

Bladex.AddParticleGType("Dust3","SmokeParticle",B_PARTICLE_GTYPE_BLEND,15)

for i in range(15):
	aux=(15.0-i)/15.0
	r=255
	g=230
	b=210
	a=80.0*(1.0-aux)**0.5
	size=1.0+aux*150.0
	Bladex.SetParticleGVal("Dust3",i,r,g,b,a,size)


def PasoPolvo(polvoposition, paso, trampa):

	if paso:
		#if (trampa):
		despl=1150
		#else:
		#	despl=-1150
		polvoflecha=Bladex.CreateEntity("PolvoFlecha3", "Entity Particle System D1", polvoposition[0]+despl, polvoposition[1], polvoposition[2])
		polvoflecha.ParticleType="Dust3"
		polvoflecha.YGravity=0.0
		polvoflecha.Friction=0.2
		polvoflecha.PPS=60
		polvoflecha.Time2Live=15
		polvoflecha.DeathTime=Bladex.GetTime()+3.0/60.0
	else:
		#if (trampa):
		despl=950
		#else:
		#	despl=-950
		polvoflecha=Bladex.CreateEntity("PolvoFlecha2", "Entity Particle System D1", polvoposition[0]+despl, polvoposition[1], polvoposition[2])
		polvoflecha.ParticleType="Dust2"
		polvoflecha.YGravity=0.0
		polvoflecha.Friction=0.2
		polvoflecha.PPS=60
		polvoflecha.Time2Live=15
		polvoflecha.DeathTime=Bladex.GetTime()+3.0/60.0
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.0/60.0, PasoPolvo, (polvoposition, 1, trampa))


class FLECHA:
	Nombre = ""
	Lanzar = ""
	Flechas_Clavadas = 0
	Estado = 0
	Avance = 0
	Vel = [0,0,0]
	Gravity	= [0,0,0]
	Orientation = [0,0,0,0]
	Position = [0,0,0]
	Scale = 0
	Tiempo_Lanzamiento = 1.3
	Tiempo_Parada	   = 0.9
	Sound = 0

def PararFlecha(Arrow_P,Tiempo):
	Arrow = Bladex.GetEntity(Arrow_P.Lanzar)
	Arrow.MessageEvent(MESSAGE_STOP_WEAPON,0,0)
	Arrow.Orientation	= Arrow_P.Orientation
	Arrow.Position		= Arrow_P.Position
	Arrow.Scale			= Arrow_P.Scale
	#Arrow_P.Sound.Stop()


def LanzarFlecha(Arrow_P,Tiempo):
	Arrow = Bladex.GetEntity(Arrow_P.Lanzar)

	if (Arrow_P.Estado == 1):
		char=Bladex.GetEntity("Player1")

		Arrow.MessageEvent(MESSAGE_START_WEAPON,0,0)
		Arrow.Fly(Arrow_P.Vel[0],Arrow_P.Vel[1],Arrow_P.Vel[2])
		#Arrow_P.Ultimo_Lanzamiento = Bladex.GetTime()
		Arrow_P.Sound.Play(Arrow.Position[0],Arrow.Position[1],Arrow.Position[2],0)

		Bladex.AddScheduledFunc(Bladex.GetTime() + Arrow_P.Tiempo_Parada,PararFlecha,(Arrow_P,0))
		Bladex.AddScheduledFunc(Bladex.GetTime() + Arrow_P.Tiempo_Lanzamiento,LanzarFlecha,(Arrow_P,0))


def ActivateArrow(Name,Tiempo,Frecuencia):
	Arrow = Bladex.GetEntity(Name)
	#print(Arrow.Data.Lanzar," Activado")
	Arrow.Data.Estado = 1
	Arrow.Data.Tiempo_Lanzamiento = Frecuencia
	Arrow.Data.Tiempo_Parada = Frecuencia - 0.1

	Bladex.AddScheduledFunc(Tiempo,LanzarFlecha,(Arrow.Data,0))

def DeactivateArrow(Name):
	Arrow = Bladex.GetEntity(Name)
	#print(Arrow.Data.Lanzar," Desactivado")
	Arrow.Data.Estado = 0


def StickArrow(Sticker,Stick):
	#print (Sticker," Clavada en ",Stick)
	Arrow = Bladex.GetEntity(Sticker)
	Flecha = Arrow.Data
	NewArrow = Traps_C.Prueba(Flecha.Nombre,Flecha.Flechas_Clavadas)
	Flecha.Flechas_Clavadas = Flecha.Flechas_Clavadas + 1
	Arrow = Bladex.CreateEntity(NewArrow,"Flecha",Flecha.Position[0],Flecha.Position[1],Flecha.Position[2])
	Arrow.Orientation = Flecha.Orientation
	Arrow.Scale = Flecha.Scale
	Arrow.Arrow = 1
	Arrow.SendSectorMsgs = 0
	Arrow.Gravity = Flecha.Gravity
	Flecha.Lanzar = NewArrow
	Arrow.Data = Flecha
	Arrow.StickFunc = StickArrow


def InitArrow(Name,Vel,Grav):
	A = FLECHA()
	A.Vel = Vel
	A.Gravity = Grav
	Arrow = Bladex.GetEntity(Name)
	Arrow.Arrow = 1
	Arrow.SendSectorMsgs = 0
	Arrow.Gravity = Grav

	A.Sound = Bladex.CreateSound('../../Sounds/dart-shoot.wav', 'LaunchArrow')
	A.Sound.Volume=0.3
	A.Sound.MinDistance=7000
	A.Sound.MaxDistance=10000

	A.Nombre      = Name
	A.Lanzar	  = Name
	A.Position    = Arrow.Position
	A.Orientation = Arrow.Orientation
	A.Scale       = Arrow.Scale

	Arrow.Data = A
	Arrow.StickFunc = StickArrow