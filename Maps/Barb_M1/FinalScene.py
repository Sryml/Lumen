import ReadGSFile
import Traps_C
import GameText
import AuxFuncs
import Scorer
import Sounds

startspirittime = 0


##### Spirits Particle definition ######

Bladex.AddParticleGType("Spirit0","FireParticle",B_PARTICLE_GTYPE_ADD,8)
Bladex.AddParticleGType("Spirit1","FireParticle",B_PARTICLE_GTYPE_ADD,8)
Bladex.AddParticleGType("Spirit2","FireParticle",B_PARTICLE_GTYPE_ADD,8)
Bladex.AddParticleGType("Spirit3","FireParticle",B_PARTICLE_GTYPE_ADD,8)
Bladex.AddParticleGType("Spirit4","FireParticle",B_PARTICLE_GTYPE_ADD,8)
Bladex.AddParticleGType("Spirit5","FireParticle",B_PARTICLE_GTYPE_ADD,8)
Bladex.AddParticleGType("Spirit6","FireParticle",B_PARTICLE_GTYPE_ADD,8)
Bladex.AddParticleGType("Spirit7","FireParticle",B_PARTICLE_GTYPE_ADD,8)
Bladex.AddParticleGType("Spirit8","FireParticle",B_PARTICLE_GTYPE_ADD,8)
Bladex.AddParticleGType("Spirit9","FireParticle",B_PARTICLE_GTYPE_ADD,8)

for i in range(8):
	size=1000.0 + i * 30
	r=20
	b=225
	g=50

	a0=225.0
	a1=200.0
	a2=175.0
	a3=150.0
	a4=125.0
	a5=100.0
	a6= 75.0
	a7= 50.0
	a8= 25.0
	a9=  0.0

	Bladex.SetParticleGVal("Spirit0",i,r,g,b,a0,size)
	Bladex.SetParticleGVal("Spirit1",i,r,g,b,a1,size)
	Bladex.SetParticleGVal("Spirit2",i,r,g,b,a2,size)
	Bladex.SetParticleGVal("Spirit3",i,r,g,b,a3,size)
	Bladex.SetParticleGVal("Spirit4",i,r,g,b,a4,size)
	Bladex.SetParticleGVal("Spirit5",i,r,g,b,a5,size)
	Bladex.SetParticleGVal("Spirit6",i,r,g,b,a6,size)
	Bladex.SetParticleGVal("Spirit7",i,r,g,b,a7,size)
	Bladex.SetParticleGVal("Spirit8",i,r,g,b,a8,size)
	Bladex.SetParticleGVal("Spirit9",i,r,g,b,a9,size)

particle = 0
avanceparticle = 0

res=ReadGSFile.ReadGhostSectorFile("GNSA.sf")

for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

char.SendTriggerSectorMsgs=1

Bladex.SetTriggerSectorFunc("GNSA", "OnEnter", StartScene)

#char.Position=113547.374771, -55494.0580892, 194332.2985