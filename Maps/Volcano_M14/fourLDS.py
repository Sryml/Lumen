#########################################################
#														#
# VOLCANO												#
#														#
# 4 demonios antes del final							#
#														#
# (Yuio)												#
#														#
#########################################################

import EnemyTypes
import Sounds
import Scorer

RugidoDemonio=Sounds.CreateEntitySound("../../Sounds/M-rugido-demon.wav", "RugidoDemonio")
RugidoDemonio.Volume=1
RugidoDemonio.MinDistance=10000
RugidoDemonio.MaxDistance=90000

FireBallCool=Sounds.CreateEntitySound("../../Sounds/aparicion-fuego.wav","Fireball")
FireBallCool.Volume=1
FireBallCool.MinDistance=10000
FireBallCool.MaxDistance=90000

o=Bladex.CreateEntity("NoName3","Gargola",-9750,-12000,-140750)
o.Static=1
o.Scale=6.055760
o.Orientation=0.687569,0.687569,-0.7,0.7

o=Bladex.CreateEntity("NoName4","Gargola",21000,-12000,-140750)
o.Static=1
o.Scale=6.055760
o.Orientation=0.687569,0.687569,0.7,-0.7

ldsDeads=0




demA=Bladex.CreateEntity("ftDemonA", "Little_Demon", 26786.484769, -7322.9, -141817.233351,"Person" )
demA.Blind=1
demA.Deaf=1
demA.Alpha=0.0
demA.Level=lvl_control.GiveLevel(5,10)
EnemyTypes.EnemyDefaultFuncs(demA)
darfuncs.HideBadGuy(demA.Name)



demC=Bladex.CreateEntity("ftDemonC", "Little_Demon", 26786.484769, -7322.9, -141817.233351,"Person" )
demC.Blind=1
demC.Deaf=1
demC.Alpha=0.0
demC.Level=lvl_control.GiveLevel(5,10)
EnemyTypes.EnemyDefaultFuncs(demC)
darfuncs.HideBadGuy(demC.Name)


Bladex.AddParticleGType("ftManuelChispa","GenericParticle",B_PARTICLE_GTYPE_ADD,80)
for i in range(80):
	if i>60:
		traux=1-((i-60.0)/20.0) #va de 0 a 1
	elif i<20:
		traux=i/20.0 #va de 1 a 0
	else:
		traux=1.0
	r=255
	g=80
	b=100
	a=255.0*traux
	size=20.0
	Bladex.SetParticleGVal("ftManuelChispa",i,r,g,b,a,size)

Bladex.AddParticleGType("ftManuelFire","FireParticle",B_PARTICLE_GTYPE_ADD,120)
for i in range(120):
	if i<40:
		traux=i/40.0 #va de 1 a 0
	else:
		traux=1.0
	r=150
	g=100
	b=255
	a=255.0*traux
	size=400.0
	Bladex.SetParticleGVal("ftManuelFire",i,r,g,b,a,size)


ftSceneStarted=0

ftTrigSector = Bladex.GetSector(6562.63229014, -5588.2, -97086.0581351)
ftTrigSector.OnEnter = ftSceneStart
