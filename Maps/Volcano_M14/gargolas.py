GARGULUS_FIRE_DAMAGE = 50



import Reference
import Select
import Change
import Actions
import Bladex
import Bladex
import FireCheck
#import AniSound
import ReadGSFile
import whrandom
import dust

_SndFogonazo=Bladex.CreateSound("../../Sounds/fireball-swing.wav","SndFogonazo")
_SndFogonazo.MaxDistance=15000.0
_SndFogonazo.MinDistance=10000.0
_SndFogonazoPos = 0,0,0


########### ghost sectors

res=ReadGSFile.ReadGhostSectorFile("gargolas.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

res=ReadGSFile.ReadGhostSectorFile("llamas.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

char=Bladex.GetEntity("Player1")
char.SendTriggerSectorMsgs=1


##################################### tipo de fuego de gas #############

B_PARTICLE_GTYPE_ADD=2

Bladex.AddParticleGType("GargFlame","FireParticle",B_PARTICLE_GTYPE_ADD,21)
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
	r=155.0*3.0*caux
	g=155.0*3.0*caux
	b=min(255*(1.0-2.0*caux), 255.0)
	a=200.0*aux
	size=300.0+200.0*saux
	Bladex.SetParticleGVal("GargFlame",i,r,g,b,a,size)


Bladex.AddParticleGType("Hoguera","FireParticle",B_PARTICLE_GTYPE_ADD,21)
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
	size=300.0+200.0*saux
	Bladex.SetParticleGVal("Hoguera",i,r,g,b,a,size)

##################################### firehit ###########################

killed=0


##################################### gargolas #######################################
##################################### gargolas #######################################
##################################### gargolas #######################################
##################################### gargolas #######################################

o=Bladex.CreateEntity("garx1","GargolaFernando",-1217.379000,-2365.313000,-19277.231000)
o.Static=1
o.Scale=1.184304
o.Orientation=0.495618,0.495618,-0.504344,0.504344


o=Bladex.CreateEntity("garx2","GargolaFernando",-1173.053000,-2142.568000,-24040.887000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.495618,0.495618,-0.504344,0.504344


o=Bladex.CreateEntity("garx3","GargolaFernando",8138.854000,-711.563000,-27031.143000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.036956,-0.000051,-0.708075,0.705170


o=Bladex.CreateEntity("garx4","GargolaFernando",12989.605000,-146.463000,-27008.375000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.006164,0.006171,-0.707080,0.707080


o=Bladex.CreateEntity("garx6","GargolaFernando",17553.365000,542.133000,-18891.584000)
o.Static=1
o.Scale=1.208109
o.Orientation=0.482246,0.482246,0.517145,-0.517145


o=Bladex.CreateEntity("garx7","GargolaFernando",17777.842000,1020.841000,-14337.183000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.473147,0.473147,0.525483,-0.525483


o=Bladex.CreateEntity("garx5","GargolaFernando",17687.464000,42.303000,-24073.773000)
o.Static=1
o.Scale=1.208109
o.Orientation=0.508650,0.508650,0.491198,-0.491198


o=Bladex.CreateEntity("garx8","GargolaFernando",12834.794000,3823.537000,2647.213000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("garx9","GargolaFernando",7706.850000,4267.964000,2680.824000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000

PSCheckerA = FireCheck.createPSysChecker()
PSCheckerA.onHitFunc = gfireHit
PSCheckerB = FireCheck.createPSysChecker()
PSCheckerB.onHitFunc = gfireHit
PSCheckerC = FireCheck.createPSysChecker()
PSCheckerC.onHitFunc = gfireHit
PSCheckerD = FireCheck.createPSysChecker()
PSCheckerD.onHitFunc = gfireHit
PSCheckerE = FireCheck.createPSysChecker()
PSCheckerE.onHitFunc = gfireHit
PSCheckerF = FireCheck.createPSysChecker()
PSCheckerF.onHitFunc = gfireHit
PSCheckerG = FireCheck.createPSysChecker()
PSCheckerG.onHitFunc = gfireHit
PSCheckerH = FireCheck.createPSysChecker()
PSCheckerH.onHitFunc = gfireHit
PSCheckerI = FireCheck.createPSysChecker()
PSCheckerI.onHitFunc = gfireHit
gfperiod=4.0
gfstop=0


Bladex.SetTriggerSectorFunc("garg", "OnEnter", gFireSectorIn )
Bladex.SetTriggerSectorFunc("garg", "OnLeave", gFireSectorOut )

##################################### foso #######################################
##################################### foso #######################################
##################################### foso #######################################
##################################### foso #######################################

fosofirestop=0
fosofireperiod=6.1

generator = whrandom.whrandom()

PSCheckerFosoA = FireCheck.createPSysChecker()
PSCheckerFosoA.onHitFunc = gfireHit
PSCheckerFosoA.precission=1
PSCheckerFosoB = FireCheck.createPSysChecker()
PSCheckerFosoB.onHitFunc = gfireHit
PSCheckerFosoB.precission=1
PSCheckerFosoC = FireCheck.createPSysChecker()
PSCheckerFosoC.onHitFunc = gfireHit
PSCheckerFosoC.precission=1

Bladex.SetTriggerSectorFunc("foso", "OnEnter", fosoFireSectorIn )
Bladex.SetTriggerSectorFunc("foso", "OnLeave", fosoFireSectorOut )
