import math
import AbreCam
import dust
import whrandom
import AuxFuncs
import GameText
import Sounds
import Scorer
import B3DLib
import GotoMapVars
import GameText

SoundLlaveInn=Sounds.CreateEntitySound('../../Sounds/M-DESAPARICION-3.wav', 'SoundLlaveInn')
SoundLlaveInn.Volume=0.8
SoundLlaveInn.MinDistance=1000000
SoundLlaveInn.MaxDistance=5000000


SoundLlaveOn=Sounds.CreateEntitySound('../../Sounds/aparicion-arana-fuego.wav', 'SoundLlaveOn')
SoundLlaveOn.Volume=0.8
SoundLlaveOn.MinDistance=1000000
SoundLlaveOn.MaxDistance=5000000

SoundLlaveFUEGO=Sounds.CreateEntitySound('../../Sounds/M-GRANDES-FUEGOS-1.wav', 'SoundLlaveFUEGO')
SoundLlaveFUEGO.Volume=0.8
SoundLlaveFUEGO.MinDistance=1000000
SoundLlaveFUEGO.MaxDistance=5000000



Bladex.AddParticleGType("llavemier","SunFlare",2,32)
for i in range(32):
	aux=(32.0-i)/32.0
	saux = aux*aux*aux
	r=255
	g=64+saux*64.0
	b=0
	a=255*aux
	size=128+a*2
	Bladex.SetParticleGVal("llavemier",i,r,g,b,a,size)




Bladex.AddParticleGType("Roja2","SmokeParticle",2,32)

for i in range(32):
	aux=(32.0-i)/32.0
	r=255
	g=64
	b=0
	a=255*aux
	size=128+a*2
	Bladex.SetParticleGVal("Roja2",i,r,g,b,a,size)


Bladex.AddParticleGType("Roja1","SmokeParticle",2,16)

for i in range(16):
	aux=(16.0-i)/16.0
	r=255
	g=64
	b=0
	a=255.0*(aux)**0.5
	size=200
	Bladex.SetParticleGVal("Roja1",i,r,g,b,a,size)


#execfile("arania.py")
#
#a.Crea(char.Position)
#a.Borra()

#char.Position = (6161, 3000, -138449)

arxx = 0