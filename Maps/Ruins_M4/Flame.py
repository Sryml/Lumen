import Bladex
import FireCheck



B_PARTICLE_GTYPE_ADD=2


### Definicion de sistemas de particulas

Bladex.AddParticleGType("Flame","FireParticle",B_PARTICLE_GTYPE_ADD,21)

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
	a=100.0*aux
	size=300.0+200.0*saux
	Bladex.SetParticleGVal("Flame",i,r,g,b,a,size)


### Sectores

sectorllamaradas=Bladex.GetSector(41000.0, -3000.0, -33500.0)


### Luces

luzllamarada1=Bladex.CreateEntity("LuzLlamarada1", "Entity Spot", 46000.0, -3500.0, -33000.0)
luzllamarada1.Color=255, 140, 40
luzllamarada1.Intensity=0.0
luzllamarada1.Visible=0
luzllamarada1.CastShadows=0

luzllamarada2=Bladex.CreateEntity("LuzLlamarada2", "Entity Spot", 51000.0, -3500.0, -33000.0)
luzllamarada2.Color=255, 140, 40
luzllamarada2.Intensity=0.0
luzllamarada2.Visible=0
luzllamarada2.CastShadows=0


### Sonidos

sonidoactivacionllamaradas=Bladex.CreateSound('../../Sounds/trap-clicked.wav', 'SonidoActivacionLlamaradas')
sonidoactivacionllamaradas.SendNotify=1

sonidollamarada=Bladex.CreateSound('../../Sounds/surtidor-fuego.wav', 'SonidoLlamarada')
sonidollamarada.SendNotify=1


### Funcionamiento

des=0

######## Funcion: EnciendeLuzLlamGrad(ent_name, time)

######## Funcion: EnciendeLuzLlamarada(flame_n)

######## Funcion: ApagaLuzLlamGrad(ent_name, time)

######## Funcion: ApagaLuzLlamarada(flame_n)

######## Funcion: LanzaSurtidor(flame_n)

######## Funcion: LanzaTrampaLlamas(sec_index, ent_name)

######## Funcion: ParaTrampaLlamas(sec_index, ent_name)

sectorllamaradas.OnEnter=LanzaTrampaLlamas
sectorllamaradas.OnLeave=ParaTrampaLlamas


### Chequeadores

######## Funcion: FlameDamage(prtl_name,hit_entity,x,y,z,vx,vy,vz,wcx,wcy,wcz,wdx,wdy,wdz)

chllama1=FireCheck.createPSysChecker()
chllama1.precission=2
chllama1.onHitFunc=FlameDamage

chllama2=FireCheck.createPSysChecker()
chllama2.precission=2
chllama2.onHitFunc=FlameDamage
