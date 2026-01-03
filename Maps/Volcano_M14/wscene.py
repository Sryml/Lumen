#########################################################
#														#
# Minotauro haciendo prisioneros a la parilla			#
#														#
# (Yuio)												#
#														#
#########################################################

import Bladex
import Sounds

import Reference
import Select
import Change
import Actions
import Bladex
import Levers
import EnemyTypes
import AniSound
import Objects
import Scorer
import AbreCam
import darfuncs

GrupoMuerte = darfuncs.E_Grup()
GrupoMuerte.OnDeath = TerminanLasMuertes

# prisioneros_a_la_brasaCamera02.cam

################################# M I N O T A U R #################################################
################################# M I N O T A U R #################################################
################################# M I N O T A U R #################################################
mpalanca=Levers.PlaceLever("MPalanca", Levers.LeverType3, ( 10629.236000, 7008.117000, 18259.165000 ), (0.500000,0.500000,-0.500000,0.500000), 1.0)
mpalanca.mode=2



JMinA=CreateMinorx(12168.566,6963.063,15409.214,-3.14159,"JMinA")
JMinB=CreateMinorx(11882.421,7040.655,10077.036,-3.14159,"JMinB")




################################# R A S T R I L L O S #################################################
################################# R A S T R I L L O S #################################################
################################# R A S T R I L L O S #################################################
"""
sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

rast8=Bladex.CreateEntity("Rast8","Rastrillo",16886.268450,5782.605334,16127.205127)
rast8.Static=1
rast8.Scale=0.923483
rast8.Orientation=0.5,0.5,0.5,-0.5

rast8din=Objects.CreateDinamicObject("Rast8")

##Rastrillo 9.##

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

rast9=Bladex.CreateEntity("Rast9","Rastrillo",16881.388243,6055.719800,11025.728444)
rast9.Static=1
rast9.Scale=0.836017
rast9.Orientation=0.5,0.5,0.5,-0.5

rast9din=Objects.CreateDinamicObject("Rast9")
"""
##################################### J A U L A S #####################################################
##################################### J A U L A S #####################################################
##################################### J A U L A S #####################################################

fallSpeed=18.0

wjA=Bladex.CreateEntity("jaula1","Jaula",7007.476,5585.538,11462.973)
wjA.Static=0
wjA.Scale=1.6
wjA.Orientation=0.707107,0.707107,0.000000,0.000000

wjB=Bladex.CreateEntity("jaula2","Jaula",5013,2020,15141)
wjB.Static=0
wjB.Scale=1.6
wjB.Orientation=0.707107,0.707107,0.000000,0.000000

wjC=Bladex.CreateEntity("jaula3","Jaula",-431.065,3194.765,7736.838)
wjC.Static=0
wjC.Scale=1.6
wjC.Orientation=0.707107,0.707107,0.000000,0.000000

o=Bladex.CreateEntity("cuerda1","CuerdaLarguisima",7007.476,-6585.538,11462.973)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000

o=Bladex.CreateEntity("cuerda2","CuerdaLarguisima",5013,-10200,15141)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000

o=Bladex.CreateEntity("cuerda3","CuerdaLarguisima",-431.065,-9194.765,7736.838)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000

Bladex.AddParticleGType("PrisBurn","FireParticle",B_PARTICLE_GTYPE_ADD,21)
for i in range(21):
	if i>=14:
		aux=1.0/3.0+2*(21.0-i)/21.0 #va de 1/3 a 1
		caux=(21.0-i)/21.0 #va de 0 a 1/3
		saux=3.0*(21.0-i)/21.0 #va de 0 a 1
	elif i>7 and i<14:
		aux=1.0
		caux=1.0/3.0
		saux=1.0
	else:
		aux=1.0-((7.0-i)/7.0) #va de 1 a 0
		caux=1.0/3.0
		saux=1.0-2*((7.0-i)/7.0) #va de 1 a -1
	r=235.0*3.0*caux
	g=105.0*3.0*caux
	b=0.0
	a=200.0*aux
	size=200.0+200.0*saux
	Bladex.SetParticleGVal("PrisBurn",i,r,g,b,a,size)


BurnA=0
BurnB=0
BurnC=0

################################# P R I S O N E R #################################################
################################# P R I S O N E R #################################################
################################# P R I S O N E R #################################################


JPrisA=Bladex.CreateEntity("JPrisA","Prisoner_4",6966.004,6099.657,11428.789)
JPrisA.RotateRel(0,0,0,1,0,0,1.57)
JPrisB=Bladex.CreateEntity("JPrisB","Prisoner_5",5003.131,3043.779,15117.294)
JPrisB.RotateRel(0,0,0,1,0,0,1.57)
JPrisC=Bladex.CreateEntity("JPrisC","Prisoner_6",-472.472,3709.12,7702.817)
JPrisC.RotateRel(0,0,0,1,0,0,1.57)


################################################# S O N I D O S ##################################################
GritoBife1=Sounds.CreatePeriodicSound("../../Sounds/moan2.wav", "Bife1",10,5,(-472.472,3709.12,7702.817))
GritoBife1.Volume=1
GritoBife1.MinDistance=1000
GritoBife1.MaxDistance=20000
GritoBife1.Volume=1
GritoBife1.BaseVolume=1.0
GritoBife1.Scale=1.0
GritoBife1.SendNotify=0

GritoBife2=Sounds.CreatePeriodicSound("../../Sounds/moan2.wav", "Bife2",10,5,(5003.131,3043.779,15117.294))
GritoBife2.Volume=1
GritoBife2.MinDistance=1000
GritoBife2.MaxDistance=20000
GritoBife2.Volume=1
GritoBife2.BaseVolume=1.0
GritoBife2.Scale=1.0
GritoBife2.SendNotify=0

GritoBife3=Sounds.CreatePeriodicSound("../../Sounds/moan2.wav", "Bife3",10,5,(6966.004,6099.657,11428.789))
GritoBife3.Volume=1
GritoBife3.MinDistance=1000
GritoBife3.MaxDistance=20000
GritoBife3.Volume=1
GritoBife3.BaseVolume=1.0
GritoBife3.Scale=1.0
GritoBife3.SendNotify=0



SoundMuu=Sounds.CreateEntitySound('../../Sounds/esfuerzo-min.wav', 'SoundMuu')
SoundMuu.Volume=1.0
SoundMuu.MinDistance=50000
SoundMuu.MaxDistance=100000


SoundQueMeQuemo=[0,0,0,0]
iSoundQueMeQuemo = 0

SoundQueMeQuemo[0]=Sounds.CreateEntitySound('../../Sounds/grito-quemando1.wav', 'SoundQueMeQuemo1')
SoundQueMeQuemo[0].Volume=0.8
SoundQueMeQuemo[0].MinDistance=2000
SoundQueMeQuemo[0].MaxDistance=40000

SoundQueMeQuemo[1]=Sounds.CreateEntitySound('../../Sounds/grito-quemando2.wav', 'SoundQueMeQuemo1')
SoundQueMeQuemo[1].Volume=0.8
SoundQueMeQuemo[1].MinDistance=2000
SoundQueMeQuemo[1].MaxDistance=40000

SoundQueMeQuemo[2]=Sounds.CreateEntitySound('../../Sounds/grito-quemando3.wav', 'SoundQueMeQuemo2')
SoundQueMeQuemo[2].Volume=0.8
SoundQueMeQuemo[2].MinDistance=2000
SoundQueMeQuemo[2].MaxDistance=40000

SoundQueMeQuemo[3]=Sounds.CreateEntitySound('../../Sounds/grito-quemando4.wav', 'SoundQueMeQuemo3')
SoundQueMeQuemo[3].Volume=0.8
SoundQueMeQuemo[3].MinDistance=2000
SoundQueMeQuemo[3].MaxDistance=40000

SoundTrakaTraka=Sounds.CreateEntitySound('../../Sounds/M-BAJADLOOP.wav', 'SoundTrakaTraka')
SoundTrakaTraka.Volume=0.8
SoundTrakaTraka.MinDistance=2000
SoundTrakaTraka.MaxDistance=40000
##########################################/\/\/\/\/\/\/\/\/\/\/\/\##################################################

wScenePrisAnim()
wAct=0

tmsec=Bladex.GetSector(25000 , 6000 , 13000)
tmsec.OnEnter=triggerSecIn

# char.Position = (40361.0753787, 7386.74728305, 19627.8523058)