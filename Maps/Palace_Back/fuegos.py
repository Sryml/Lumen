import Bladex
import AuxFuncs
import Scorer



AuxFuncs.SingleFrameFade()
Scorer.SetVisible(0)





Bladex.AddParticleGType("FlameCabezon","FireParticle",B_PARTICLE_GTYPE_ADD,21)

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
	r=20.0*3.0*caux
	g=100.0*3.0*caux
	b=255.0*3.0*caux
	a=240.0*aux
	size=300.0+200.0*saux
	Bladex.SetParticleGVal("FlameCabezon",i,r,g,b,a,size)


Bladex.AddParticleGType("FlameCabezon1","FireParticle",B_PARTICLE_GTYPE_ADD,21)

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
	r=90.0*3.0*caux
	g=120.0*3.0*caux
	b=140.0*3.0*caux
	a=200.0*aux
	size=300.0+200.0*saux
	Bladex.SetParticleGVal("FlameCabezon1",i,r,g,b,a,size)


Bladex.AddParticleGType("FlameCabezon2","FireParticle",B_PARTICLE_GTYPE_ADD,21)

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
	r=25.0
	g=50.0
	b=255.0
	a=255.0*aux
	size=300.0+200.0*saux
	Bladex.SetParticleGVal("FlameCabezon2",i,r,g,b,a,size)


Bladex.AddParticleGType("FlameCabezon3","FireParticle",B_PARTICLE_GTYPE_ADD,21)

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
	r=180.0*3.0*caux
	g=min(255*(1.0-2.0*caux), 255.0)
	b=210.0*3.0*caux
	a=150.0*aux
	size=300.0+200.0*saux
	Bladex.SetParticleGVal("FlameCabezon3",i,r,g,b,a,size)



CreateFires()
