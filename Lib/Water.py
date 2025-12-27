########################################
###          Aguita asesina!         ###
########################################
import Bladex
import ReadGSFile
import Sounds
#B_PARTICLE_GTYPE_COPY=0
#B_PARTICLE_GTYPE_BLEND=1
#B_PARTICLE_GTYPE_ADD=2
#B_PARTICLE_GTYPE_MUL=3


SndSplash=Sounds.CreateEntitySound("../../Sounds/M-CHAPUZONCAIDAALTURA.wav", "Splash")
SndSplash.Volume=1
SndSplash.MinDistance=5000
SndSplash.MaxDistance=90000

SndGlubGlub=Sounds.CreateEntitySound("../../Sounds/M-agua-burbujas.wav", "GlubGlub")
SndGlubGlub.Volume=1
SndGlubGlub.MinDistance=5000
SndGlubGlub.MaxDistance=90000



Bladex.ReadBitMap("../../Data/Salpicadura.bmp","SplashParticle")

Bladex.AddParticleGType("Splash","SplashParticle",2,64)

for i in range(64):
	aux=(64.0-i)/64.0
	r=80
	g=100
	b=100
	a=64*(1.0-aux)**0.5
	size=aux*200
	Bladex.SetParticleGVal("Splash",i,r,g,b,a,size)

Bladex.ReadBitMap("../../Data/Bubble.bmp","BubbleParticle")

Bladex.AddParticleGType("Bubble","BubbleParticle",2,64)

for i in range(64):
	aux=(64.0-i)/64.0
	r=100
	g=100
	b=100
	a=128.0*(1.0-aux)**0.5
	size=50
	Bladex.SetParticleGVal("Bubble",i,r,g,b,a,size)

def SplashWater(x,y,z):
	Aguita=Bladex.CreateEntity("Cristales", "Entity Particle System D1", x, y, z)
	Aguita.ParticleType="Splash"
	Aguita.PPS=2048
	Aguita.YGravity=1000.0
	Aguita.Friction=0
	Aguita.Velocity=0,-1500,0
	Aguita.RandomVelocity=20.0
	Aguita.Time2Live=64
	Aguita.DeathTime=Bladex.GetTime()+0.3

	SndSplash.Position = x, y, z
	SndSplash.PlaySound(0)

	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, RemueveAgua,(x,y,z,1000,1000))
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, DropBubbles,(x,y,z))


def DropBubbles(x,y,z):
	Aguita=Bladex.CreateEntity("Cristales", "Entity Particle System D1", x, y, z)
	Aguita.ParticleType="Bubble"
	Aguita.PPS=10
	Aguita.YGravity=-1000.0
	Aguita.Friction=0.1
	Aguita.Velocity=0,1000,0
	Aguita.RandomVelocity=30.0
	Aguita.Time2Live=64
	Aguita.DeathTime=Bladex.GetTime()+5.0
	SndGlubGlub.Position = x, y, z
	SndGlubGlub.PlaySound(0)

def RemueveAgua(x,y,z   ,sx,sz):

	tierra1=Bladex.CreateEntity("TierraRemoviendose1", "Entity Particle System D3", x +sx, y, z + sz)
	tierra1.D1= -2*sx, 0, 0
	tierra1.D2= -2*sx, 0, - 2*sz
	tierra1.ParticleType="Splash"
	tierra1.PPS=64
	tierra1.YGravity=200.0
	tierra1.Friction=0.1
	tierra1.Velocity=0.0, -400.0, 0.0
	tierra1.RandomVelocity=15.0
	tierra1.Time2Live=64
	tierra1.DeathTime=Bladex.GetTime()+2.0


	tierra2=Bladex.CreateEntity("TierraRemoviendose2", "Entity Particle System D3", x + sx, y, z + sz)
	tierra2.D1= -2*sx, 0, - 2*sz
	tierra2.D2=     0, 0, - 2*sz
	tierra2.ParticleType="Splash"
	tierra2.PPS=64
	tierra2.YGravity=200.0
	tierra2.Friction=0.1
	tierra2.Velocity=0.0, -400.0, 0.0
	tierra2.RandomVelocity=15.0
	tierra2.Time2Live=64
	tierra2.DeathTime=Bladex.GetTime()+2.0

WaterHi = 24000

def matame(finado):
	finado.Life = 0

def OnGlubGlub(sectorindex,entityname):
	global WaterHi
	finado = Bladex.GetEntity(entityname)
	if finado.Person:
		SplashWater(finado.Position[0],WaterHi-1,finado.Position[2])
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, matame,(finado,))

		if(entityname=="Player1"):
			cam  = Bladex.GetEntity("Camera")
			cam.SType = 0
			cam.TType = 0


def SetGs(filename,sectorname):
	res=ReadGSFile.ReadGhostSectorFile(filename)
	for igs in res:
	   Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

	Bladex.SetTriggerSectorFunc(sectorname, "OnEnter", OnGlubGlub )

	char = Bladex.GetEntity("Player1")
	char.SendTriggerSectorMsgs = 1

# Water.SplashWater(char.Position[0],WaterHi-1,char.Position[2])