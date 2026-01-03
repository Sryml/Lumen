import Bladex
#import Traps_C
import AuxFuncs
import Sounds
import def_class
import InitDataField

MESSAGE_START_WEAPON         =7
MESSAGE_STOP_WEAPON          =8
B_SOLID_MASK_PERSON          =1

Bladex.AddParticleGType("Explode","FireParticle",B_PARTICLE_GTYPE_ADD,21)

for i in range(10):
	if i>7:
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
	a=150.0*aux
	size=300.0+300.0*saux
	Bladex.SetParticleGVal("Explode",i,r,g,b,a,size)


Trampa_Pendulos = 0
DesactivarPendulos = 0

#o=Bladex.CreateEntity("Pendulo","Pendulo",138120.319063,750,611.015784)
o=Bladex.CreateEntity("Pendulo","Pendulo",138120,-500,611,"Weapon")
o.Scale=2.20
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[46]
o.Lights=[ (10.000000,0.031250,(255,196,128)) ]
#o.Solid = 0
InitDataField.Initialise(o)

if o.ExclusionMask & B_SOLID_MASK_PERSON:
	o.ExclusionMask= o.ExclusionMask-B_SOLID_MASK_PERSON


P1 = CreatePendulo("Pendulo")
P1.Piv = [0,0,4000]
P1.Axi = [0,1,0]
P1.Angulo = -1.0
P1.Dir = 1

P1.Pendulo.RotateRel(P1.Piv[0],P1.Piv[1],P1.Piv[2],P1.Axi[0],P1.Axi[1],P1.Axi[2],-1.05)

ExHitFunc = 0



Pendulo_Sector1 = Bladex.GetSector(126500, 5000, 0)
Pendulo_Sector1.OnEnter = Activar_Pendulos
Pendulo_Sector2 =  Bladex.GetSector(145800, 5000, 0)
Pendulo_Sector2.OnEnter = Desactivar_Pendulos

Pendulo_Sector3 = Bladex.GetSector(119600, 3965, -8114)
Pendulo_Sector3.OnEnter = PararPendulos

