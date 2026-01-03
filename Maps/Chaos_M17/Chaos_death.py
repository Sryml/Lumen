import Bladex
import EnemyTypes
import Reference
import Scorer
import AuxFuncs
import Objects
import InitDataField
import Damage
import whrandom




Bladex.CreateTimer("Timer30",1.0/30.0)
Bladex.CreateTimer("Timer10",1.0/10.0)


#############################################
#     Definicion sistemas de particulas     #
#############################################


B_PARTICLE_GTYPE_BLEND=1
B_PARTICLE_GTYPE_ADD=2

Bladex.ReadAlphaBitMap("../../Data/Tornado.bmp","Tornadux")


##### Particulas tornado

Bladex.AddParticleGType("Tornado1","Tornadux",B_PARTICLE_GTYPE_BLEND,90)

for i in range(90):
	if i>65:
		aux=traux=(90.0-i)/25.0 #va de 0 a 1
	elif (i<=65 and i>15):
		aux=traux=1.0
	else:
		traux=i/15.0 #va de 1 a 0
		aux=traux+(1.0-traux)/2.0 # = (traux+1.0)/2.0
	r=255
	g=255
	b=255
	a=100.0*traux
	size=4000.0*aux**0.5
	Bladex.SetParticleGVal("Tornado1",i,r,g,b,a,size)


Bladex.AddParticleGType("Tornado2","Tornadux",B_PARTICLE_GTYPE_BLEND,90)

for i in range(90):
	if i>65:
		aux=traux=(90.0-i)/25.0 #va de 0 a 1
	elif (i<=65 and i>15):
		aux=traux=1.0
	else:
		traux=i/15.0 #va de 1 a 0
		aux=traux+(1.0-traux)/2.0 # = (traux+1.0)/2.0
	r=225
	g=225
	b=225
	a=100.0*traux
	size=3000.0*aux**0.5
	Bladex.SetParticleGVal("Tornado2",i,r,g,b,a,size)


##### Red Missile concentration

Bladex.AddParticleGType("RedMissileConc","GenericParticle2",B_PARTICLE_GTYPE_ADD,60)

for i in range(60):
	if i>10:
		traux=(60.0-i)/50.0 #va de 0 a 1
	else:
		traux=i/10.0 #va de 1 a 0
	r=255
	g=40
	b=30
	a=255.0*traux
	size=250.0*(1-i/60.0)**2.0
	Bladex.SetParticleGVal("RedMissileConc",i,r,g,b,a,size)


##### Red Missile dissipation

Bladex.AddParticleGType("RedMissileDissip","GenericParticle2",B_PARTICLE_GTYPE_ADD,60)

for i in range(60):
	if i>50:
		traux=(60.0-i)/10.0 #va de 0 a 1
	else:
		traux=i/50.0 #va de 1 a 0
	r=255
	g=40
	b=30
	a=255.0*traux
	size=200.0*(1-(1-i/60.0)**0.5)
	Bladex.SetParticleGVal("RedMissileDissip",i,r,g,b,a,size)


##### Concentracion grande energia azul

Bladex.AddParticleGType("BigBlueEnergyCon","GenericParticle2",B_PARTICLE_GTYPE_ADD,60)

for i in range(60):
	if i>10:
		traux=(60.0-i)/50.0 #va de 0 a 1
	else:
		traux=i/10.0 #va de 1 a 0
	r=80
	g=120
	b=255
	a=255.0*traux
	size=20.0+800.0*(1-i/60.0)**2.0
	Bladex.SetParticleGVal("BigBlueEnergyCon",i,r,g,b,a,size)


##### Desintegracion energia

Bladex.AddParticleGType("EnergyDisint","GenericParticle2",B_PARTICLE_GTYPE_ADD,60)

for i in range(60):
	if i>50:
		traux=(60.0-i)/10.0 #va de 0 a 1
	elif i>10:
		traux=1.0
	else:
		traux=i/10.0 #va de 1 a 0
	r=100
	g=130
	b=255
	a=255.0*traux
	size=400.0*(1-(1-i/60.0)**0.5)
	Bladex.SetParticleGVal("EnergyDisint",i,r,g,b,a,size)




#########              #########
################################
####     Funcionamiento     ####
################################
#########              #########



#####################################
#     Funciones comunes tornado     #
#####################################

GenR = whrandom.whrandom()
#nr=0
sndnumber=0

###########################################################
#     Creacion de objetos, carga de animaciones, etc.     #
###########################################################


CreaObjetosEnergeticos()
CreaTornado()


"""


###############
#    Luces    #
###############

o=Bladex.CreateEntity("Lucero0","LamparaNegra",667279.222034,310713.171522,181006.346340)
o.Static=1
o.Scale=1.000000
o.Orientation=0.589646,0.589646,0.390278,-0.390278
o.FiresIntensity=[ 20 ]
o.Lights=[ (200,0.1,(255,164,62)) ]

o=Bladex.CreateEntity("Lucero1","Lamparaegipto",690270.430000,322797.196000,176064.219000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 20 ]
o.Lights=[ (200,0.1,(255,164,62)) ]

o=Bladex.CreateEntity("Lucero2","Lamparaegipto",735975.900000,332763.469000,161432.534000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 20 ]
o.Lights=[ (200,0.1,(255,164,62)) ]

o=Bladex.CreateEntity("Lucero3","Lamparaegipto",812297.009000,334794.295000,156548.813000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707080,0.707080,-0.006171,0.006171
o.FiresIntensity=[ 20 ]
o.Lights=[ (200,0.1,(221,116,0)) ]

o=Bladex.CreateEntity("Lucero4","Lamparaegipto",812317.160000,334795.139000,184153.103000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707080,0.707080,-0.006171,0.006171
o.FiresIntensity=[ 20 ]
o.Lights=[ (200,0.1,(221,116,0)) ]

o=Bladex.CreateEntity("Lucero5","Lamparaegipto",822570.506000,334798.220000,170180.512000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 20 ]
o.Lights=[ (200,0.1,(221,116,0)) ]

o=Bladex.CreateEntity("Lucero6","LamparaNegra",817815.339000,330625.335000,138558.978000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.508650,0.508650,-0.491198,0.491198
o.FiresIntensity=[ 20 ]
o.Lights=[ (200,0.1,(221,116,0)) ]

o=Bladex.CreateEntity("Lucero7","LamparaNegra",817018.970000,329782.296000,201953.303000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.500000,0.500000,0.500000,-0.500000
o.FiresIntensity=[ 20 ]
o.Lights=[ (200,0.1,(221,116,0)) ]

o=Bladex.CreateEntity("Lucero8","LamparaNegra",848738.355000,329843.762000,189102.957000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.006164,0.006171,-0.707080,0.707080
o.FiresIntensity=[ 20 ]
o.Lights=[ (200,0.1,(221,116,0)) ]

o=Bladex.CreateEntity("Lucero9","LamparaNegra",848728.004000,329882.792000,151418.563000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.000000,0.000000,0.707107,-0.707107
o.FiresIntensity=[ 20 ]
o.Lights=[ (200,0.1,(221,116,0)) ]

o=Bladex.CreateEntity("Lucero10","LamparaNegra",876461.326000,323047.094000,163799.092000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.495618,0.495618,-0.504344,0.504344
o.FiresIntensity=[ 20 ]
o.Lights=[ (200,0.1,(221,116,0)) ]

o=Bladex.CreateEntity("Lucero11","LamparaNegra",892987.584000,323812.575000,176618.534000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.517145,0.517145,0.482246,-0.482246
o.FiresIntensity=[ 20 ]
o.Lights=[ (200,0.1,(221,116,0)) ]

o=Bladex.CreateEntity("Lucero12","Lamparaegipto",920859.661000,342046.119000,150183.986000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 20 ]
o.Lights=[ (200,0.1,(221,116,0)) ]

o=Bladex.CreateEntity("Lucero13","Lamparaegipto",921078.109000,342068.374000,190790.010000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 20 ]
o.Lights=[ (200,0.1,(221,116,0)) ]



############################
#    Creacion ChaosLord    #
############################

AnAhkard=Bladex.CreateEntity("AnAhkard","DarkLord",945000.0, 341146.0, 170250.0,"Person")
AnAhkard.Angle=3.14159/2.0
EnemyTypes.EnemyDefaultFuncs(AnAhkard)
AnAhkard.Blind=1
AnAhkard.Deaf=1

"""


AnAhkard.ImDeadFunc=MuereElBichoMalo

VejeteF=Bladex.CreateEntity("VejeteFinal","Vejete",942824.188, 346730.531, 169709.609,"Actor")
VejeteF.Orientation = 0.707107,0.707107,0.000000,0.000000

Ank2F=Bladex.CreateEntity("Ank2Final","Ank2",942974.437575, 347570.40625, 169642.280646,"Actor")
Ank2F.Orientation = 0.707107,0.707107,0.000000,0.000000
Ank2F.SelfIlum=0.5
