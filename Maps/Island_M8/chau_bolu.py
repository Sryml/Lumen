import AuxFuncs
import dust
import GameText




soundwyvscream=Sounds.CreateEntitySound('../../Sounds/Wyvern.wav', 'SoundWyvernScream')
soundwyvscream.Volume=0.7
soundwyvscream.MinDistance=10000
soundwyvscream.MaxDistance=100000


soundwyvflap=Sounds.CreateEntitySound('../../Sounds/Wingflap-L.wav', 'SoundWyvernFlap')
soundwyvflap.Volume=1.0
soundwyvflap.MinDistance=10000
soundwyvflap.MaxDistance=100000

soundwyvHit=Sounds.CreateEntitySound('../../Sounds/hit-wall1.wav', 'SoundWyvernHit')
soundwyvHit.Volume=0.3
soundwyvHit.MinDistance=10000
soundwyvHit.MaxDistance=100000

soundwyvJump=Sounds.CreateEntitySound('../../Sounds/rugido-wyverna.wav', 'SoundWyvernJump')
soundwyvJump.Volume=0.5
soundwyvJump.MinDistance=10000
soundwyvJump.MaxDistance=100000


soundVmpSalta=Sounds.CreateEntitySound('../../Sounds/M-SALTO-VAMP.wav', 'VampSalta')
soundVmpSalta.Volume=0.5
soundVmpSalta.MinDistance=10000
soundVmpSalta.MaxDistance=100000

soundVmpMonta=Sounds.CreateEntitySound('../../Sounds/M-MOVCADENARN.wav', 'VampMonta')
soundVmpMonta.Volume=0.5
soundVmpMonta.MinDistance=10000
soundVmpMonta.MaxDistance=100000

soundCupWind=Sounds.CreateEntitySound('../../Sounds/Mountain-ice-wind.wav', 'CupWind')
soundCupWind.Volume=1.0
soundCupWind.MinDistance=100000
soundCupWind.MaxDistance=1000000

soundCupOpen=Sounds.CreateEntitySound('../../Sounds/M-APERTURA-CUPULA.WAV', 'CupOpen')
soundCupOpen.Volume=0.5
soundCupOpen.MinDistance=100000
soundCupOpen.MaxDistance=1000000







wyv = Bladex.CreateEntity("Wyv","Wyvern",-41595.875,-64726.145,53651.363)
wyv.RotateRel(0,0,0,1,0,0,1.57)
wyv.Static = 1

Bladex.CreateTimer("TimerCupula",1.0/40.0)

c1=Bladex.CreateEntity("Cup1","Cupula",-42461.008000,-75002.606000,24855.853000)
c1.Static=1
c1.Scale=1.000000
c1.Orientation=0.707107,0.707107,0.000000,0.000000

c2=Bladex.CreateEntity("Cup2","Cupula",-42461.008000,-75002.606000,24855.853000)
c2.Static=1
c2.Scale=1.000000
c2.Orientation=0.707107,0.707107,0.000000,0.000000
c2.RotateRel(0,0,0,0,0,1,0.785)

c3=Bladex.CreateEntity("Cup3","Cupula",-42461.008000,-75002.606000,24855.853000)
c3.Static=1
c3.Scale=1.000000
c3.Orientation=0.707107,0.707107,0.000000,0.000000
c3.RotateRel(0,0,0,0,0,1,-0.785)

c4=Bladex.CreateEntity("Cup4","Cupula",-42461.008000,-75002.606000,24855.853000)
c4.Static=1
c4.Scale=1.000000
c4.Orientation=0.707107,0.707107,0.000000,0.000000
c4.RotateRel(0,0,0,0,0,1,1.57)

c5=Bladex.CreateEntity("Cup5","Cupula",-42461.008000,-75002.606000,24855.853000)
c5.Static=1
c5.Scale=1.000000
c5.Orientation=0.707107,0.707107,0.000000,0.000000
c5.RotateRel(0,0,0,0,0,1,-1.57)

c6=Bladex.CreateEntity("Cup6","Cupula",-42461.008000,-75002.606000,24855.853000)
c6.Static=1
c6.Scale=1.000000
c6.Orientation=0.707107,0.707107,0.000000,0.000000
c6.RotateRel(0,0,0,0,0,1,2.355)

c7=Bladex.CreateEntity("Cup7","Cupula",-42461.008000,-75002.606000,24855.853000)
c7.Static=1
c7.Scale=1.000000
c7.Orientation=0.707107,0.707107,0.000000,0.000000
c7.RotateRel(0,0,0,0,0,1,-2.355)

c8=Bladex.CreateEntity("Cup8","Cupula",-42461.008000,-75002.606000,24855.853000)
c8.Static=1
c8.Scale=1.000000
c8.Orientation=0.707107,0.707107,0.000000,0.000000
c8.RotateRel(0,0,0,0,0,1,3.14)


FPS = 30.0





############### Nubes de la Wiverna ###############


Bladex.AddParticleGType("Coulds","SmokeParticle",2,300)

for i in range(300):
	aux=(64.0-i)/64.0
	r=100
	g=30
	b=30
	a=255
	size=12000
	Bladex.SetParticleGVal("Coulds",i,r,g,b,a,size)

for i in range(50):
	aux=i/50.0
	r=100
	g=30
	b=30
	a=255.0*aux
	size=12000
	Bladex.SetParticleGVal("Coulds",i,r,g,b,a,size)
	Bladex.SetParticleGVal("Coulds",300-i,r,g,b,a,size)




CreaNubes(-41666, -60000-21000, 56216+15000,50000,10000,10)
# dust.RemueveTierraGen(-42000, -55000, 25064,2500,2500,1024,"FastDust",16,0.1)