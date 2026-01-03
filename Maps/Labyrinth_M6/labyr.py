import Bladex
import math
import NetSounds
import whrandom



### Sol

#Bladex.SetSun(1,100,77,0)


### Agua

aguafuente=Bladex.CreateEntity("AguaFuente","Entity Water",0.0,1400.0,39000.0) #1300.0,39000.0)
aguafuente.Reflection=-1.0
aguafuente.Color=0,6,12

aguacanal=Bladex.CreateEntity("AguaCanal","Entity Water",0.0,2500.0,39000.0) #2150.0,39000.0)
aguacanal.Reflection=-1.0
aguacanal.Color=0,6,12

aguaestablo1=Bladex.CreateEntity("AguaEstablo1","Entity Water",-18750.0,1200.0,59750.0)
aguaestablo1.Reflection=-1.0
aguaestablo1.Color=0,6,12

aguaestablo2=Bladex.CreateEntity("AguaEstablo2","Entity Water",18750.0,1200.0,59750.0)
aguaestablo2.Reflection=-1.0
aguaestablo2.Color=0,6,12

aguaestanque=Bladex.CreateEntity("AguaEstanque","Entity Water",0.0,5000.0,-55000.0)
aguaestanque.Reflection=-1.0
aguaestanque.Color=0,6,12

aguapozo=Bladex.CreateEntity("AguaPozo","Entity Water",13500.0,11250.0,-25000.0)
aguapozo.Reflection=-1.0
aguapozo.Color=0,6,12


##############################################
### Definiciones de sistemas de particulas ###
##############################################

B_PARTICLE_GTYPE_BLEND=1
B_PARTICLE_GTYPE_ADD=2

Bladex.AddParticleGType("Agua","WaterParticle2",B_PARTICLE_GTYPE_BLEND,30)

for i in range(30):
	r=160
	g=160
	b=180
	a=40
	size=120.0
	Bladex.SetParticleGVal("Agua",i,r,g,b,a,size)

Bladex.AddParticleGType("AguaC","WaterParticle2",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	r=160
	g=160
	b=180
	a=60
	size=280.0
	Bladex.SetParticleGVal("AguaC",i,r,g,b,a,size)

Bladex.AddParticleGType("Espuma","SmokeParticle",B_PARTICLE_GTYPE_BLEND,10)

for i in range(10):
	aux=(10.0-i)/10.0
	r=160
	g=160
	b=180
	a=255*math.sqrt(1.0-aux)
	size=700.0*math.sqrt(1.0-aux)
	Bladex.SetParticleGVal("Espuma",i,r,g,b,a,size)

Bladex.AddParticleGType("Espuma2","SmokeParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	aux=(60.0-i)/60.0
	r=160
	g=160
	b=180
	a=255*math.sqrt(1.0-aux)
	size=400.0+aux*400.0
	Bladex.SetParticleGVal("Espuma2",i,r,g,b,a,size)

Bladex.AddParticleGType("Salpique","GenericParticle",B_PARTICLE_GTYPE_BLEND,30)

for i in range(30):
	aux=(30.0-i)/30.0
	r=160
	g=160
	b=180
	a=100*math.sqrt(1.0-aux)
	size=30.0*math.sqrt(1.0-aux)
	Bladex.SetParticleGVal("Salpique",i,r,g,b,a,size)

Bladex.AddParticleGType("Flame","FireParticle",B_PARTICLE_GTYPE_ADD,21)

for i in range(21):
	if i>=14:
		aux=1.0/3.0+2*(21.0-i)/21.0
		caux=(21.0-i)/21.0
		saux=3.0*(21.0-i)/21.0
	elif i>7 and i<14:
		aux=1.0
		caux=1.0/3.0
		saux=1.0
	else:
		aux=1.0-((7.0-i)/7.0)
		caux=1.0/3.0
		saux=1.0-2*((7.0-i)/7.0)
	r=155.0*3.0*caux
	g=155.0*3.0*caux
	b=min(255*(1.0-2.0*caux), 255.0)
	a=100.0*aux
	size=300.0+200.0*saux
	Bladex.SetParticleGVal("Flame",i,r,g,b,a,size)


### Surtidores ###

######## Funcion: Fuentes()

######## Funcion: Cascadas()


Fuentes()
Cascadas()



### Animaciones ###

Bladex.AddWatchAnim("agonia")


#######################################
### Pasos en animaciones scriptadas ###
#######################################

labyrpasopie1=Bladex.CreateSound('../../sounds/paso-piedra-1.wav', 'LabyrPasoPie1')
labyrpasopie1.MinDistance=1000
labyrpasopie1.MaxDistance=10000
labyrpasopie2=Bladex.CreateSound('../../sounds/paso-piedra-2.wav', 'LabyrPasoPie2')
labyrpasopie2.MinDistance=1000
labyrpasopie2.MaxDistance=10000
labyrpasopie3=Bladex.CreateSound('../../sounds/paso-piedra-3.wav', 'LabyrPasoPie3')
labyrpasopie3.MinDistance=1000
labyrpasopie3.MaxDistance=10000

labyrpasoagua1=Bladex.CreateSound('../../sounds/M-MOVENAGUAL1.wav', 'LabyrPasoAgua1')
labyrpasoagua1.MinDistance=1000
labyrpasoagua1.MaxDistance=10000
labyrpasoagua2=Bladex.CreateSound('../../sounds/M-MOVENAGUAL2.wav', 'LabyrPasoAgua2')
labyrpasoagua2.MinDistance=1000
labyrpasoagua2.MaxDistance=10000

if char.CharTypeExt[:3]=="Kgt":
	esfname='../../sounds/esfuerzo-caballero4.wav'
elif char.CharTypeExt[:3]=="Dwf":
	esfname='../../sounds/enano-esfuerzo6.wav'
elif char.CharTypeExt[:3]=="Amz":
	esfname='../../sounds/esfuerzo-corto-amz2.wav'
else:
	esfname='../../sounds/esfuerzos_barb_corto_5.wav'

labyresf=Bladex.CreateSound(esfname, 'LabyrEsf')
labyresf.MinDistance=1000
labyresf.MaxDistance=10000


# Animacion inicio

# Animacion agonia

# Animacion final

# Animacion tablilla
