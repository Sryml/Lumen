####################################################################################################
#                                         La espada de BLADE                                       #
####################################################################################################

# TODO :
#            ( ) - Sonido
#            ( ) - Glow de la espada
#            ( ) - Efecto de rayo que golpea
#            ( ) - Asociar las escenas con las tablillas
#            ( ) - Hacer la espada Blade Activa en la ultima escena

import math
import whrandom
import Traps_C
import Scorer
import AuxFuncs
import InitDataField
import Objects
import Actions
import pdb
import ItemTypes
import GotoMapVars

Bladex.CreateTimer("Timer30",1.0/30.0)

TabliState                = [0,0,0,0,0,0]   # 0 : No hay Tablilla.    1 : Si hay Tablilla      2 : Tablilla puesta
BladeReady                = 1               # 0 : No tengo la espada  1 : Tengo la espada



B_PARTICLE_GTYPE_BLEND=1
B_PARTICLE_GTYPE_ADD=2

Bladex.ReadAlphaBitMap("../../Data/Tornado.bmp","Tornadux")


##### Disipacion energia azul

Bladex.AddParticleGType("BlueEnergyDis","GenericParticle2",B_PARTICLE_GTYPE_ADD,30)

for i in range(30):
	if i>25:
		traux=(30.0-i)/5.0 #va de 0 a 1
	else:
		traux=i/25.0 #va de 1 a 0
	r=70
	g=110
	b=255
	a=255.0*traux
	size=80.0*(1-(1-i/30.0)**0.5)
	Bladex.SetParticleGVal("BlueEnergyDis",i,r,g,b,a,size)

##### Disipacion energia azul2

Bladex.AddParticleGType("BlueEnergyDis2","GenericParticle2",B_PARTICLE_GTYPE_ADD,30)

for i in range(30):
	if i>25:
		traux=(30.0-i)/5.0 #va de 0 a 1
	elif (i<=25 and i>5):
		traux=1.0
	else:
		traux=i/5.0 #va de 1 a 0
	r=40
	g=90
	b=255
	a=255.0*traux*0.75
	size=160.0*(1-(1-i/30.0)**0.5)
	Bladex.SetParticleGVal("BlueEnergyDis2",i,r,g,b,a,size)

##### Disipacion energia azul3

Bladex.AddParticleGType("BlueEnergyDis3","GenericParticle2",B_PARTICLE_GTYPE_ADD,60)

for i in range(60):
	if i>50:
		traux=(60.0-i)/10.0 #va de 0 a 1
	elif (i<=50 and i>10):
		traux=1.0
	else:
		traux=i/10.0 #va de 1 a 0
	r=40
	g=90
	b=255
	a=255.0*traux*0.75
	size=400.0*(1-(1-i/60.0)**0.5)
	Bladex.SetParticleGVal("BlueEnergyDis3",i,r,g,b,a,size)

##### Concentracion energia azul

Bladex.AddParticleGType("BlueEnergyCon","GenericParticle2",B_PARTICLE_GTYPE_ADD,40)

for i in range(40):

	if i>5:
		saux=((40.0-i)/35.0)**2.0 #va de 0 a 1
	else:
		saux=1-(1-i/5.0)**0.5 #va de 1 a 0

	if i>35:
		traux=(40.0-i)/5.0 #va de 0 a 1
	elif (i<=35 and i>5):
		traux=1.0
	else:
		traux=i/5.0 #va de 1 a 0

	r=70
	g=110
	b=255
	a=255.0*traux
	size=10+60.0*saux
	Bladex.SetParticleGVal("BlueEnergyCon",i,r,g,b,a,size)

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

##### Concentracion media energia azul

Bladex.AddParticleGType("MediumBlueEnergyCon","GenericParticle2",B_PARTICLE_GTYPE_ADD,60)

for i in range(60):
	if i>10:
		traux=(60.0-i)/50.0 #va de 0 a 1
	else:
		traux=i/10.0 #va de 1 a 0
	r=100
	g=130
	b=255
	a=255.0*traux
	size=10.0+150.0*(1-i/60.0)**2.0
	Bladex.SetParticleGVal("MediumBlueEnergyCon",i,r,g,b,a,size)

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
	size=3000.0*aux**0.5
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
	size=2000.0*aux**0.5
	Bladex.SetParticleGVal("Tornado2",i,r,g,b,a,size)





GenR = whrandom.whrandom()
#nr=0
sndnumber=0

sndluztabl=Sounds.CreateEntitySound("../../Sounds/luz.wav", "SndLuzTabl")
sndluztabl.Volume=1.0
sndluztabl.MinDistance=4000
sndluztabl.MaxDistance=25000
sndluztabl.Position=94355.0, -3148.0, 172034.0

snddejatabl=Sounds.CreateEntitySound("../../Sounds/aparicion-escudo.wav", "SndDejaTabl")
snddejatabl.Volume=0.6
snddejatabl.Pitch=0.7
snddejatabl.MinDistance=4000
snddejatabl.MaxDistance=25000
snddejatabl.Position=94355.0, -3148.0, 172034.0

sndreapesp=Sounds.CreateEntitySound("../../Sounds/aparicion-espada.wav", "SndReapEsp")
sndreapesp.Volume=0.7
sndreapesp.Pitch=0.7
sndreapesp.MinDistance=4000
sndreapesp.MaxDistance=25000
sndreapesp.Position=94355.0, -3148.0, 172034.0

sndsacaespada=Sounds.CreateEntitySound("../../Sounds/M-DESENFUNDA-PIEDRA1.wav", "SndSacaEspada")
sndsacaespada.Volume=1.0
sndsacaespada.Pitch=0.9
sndsacaespada.MinDistance=4000
sndsacaespada.MaxDistance=25000
sndsacaespada.Position=94355.0, -3148.0, 172034.0

sndflash=Sounds.CreateEntitySound("../../Sounds/llave-estrella.wav", "SndFlash")
sndflash.Volume=0.7
sndflash.MinDistance=4000
sndflash.MaxDistance=20000


Tablist = {}



lista_tablillas_cambia_zbuffer=[]


aura_size_jugdejatabl=2
aura_var_jugdejatabl=2



CameraSecuence=[("",0,0, "")]
iCameraSecuence=0


CamaraTodasLasTablillas = []
CamaraTodasLasTablillas.append("Palacio_Camera_personaje.cam",          0,   81, "")
CamaraTodasLasTablillas.append("Palacio_Camara_segunda.cam",           82,  265, FullZBufferTablillas)
CamaraTodasLasTablillas.append("Palacio_Camera_espada.cam",           266,  470, ApagaLuzVerde)
CamaraTodasLasTablillas.append("Palacio_Camera_lejana.cam",           471,  608, ApareceTornado)
CamaraTodasLasTablillas.append("Palacio_Camara_segunda.cam",          609,  763, "")
CamaraTodasLasTablillas.append("Palacio_Camera_arriba.cam",           764,  915, "")
CamaraTodasLasTablillas.append("Palacio_Camera_lejana.cam",           916, 1057, AumentaFrecuenciaRayos)
CamaraTodasLasTablillas.append("Palacio_Camera_temblor_rayo.cam",    1058, 1147, Imprimelo)
CamaraTodasLasTablillas.append("Palacio_Camara_cara_diosa.cam",      1148, 1250, FadingCoolDeUnaAOtra)
CamaraTodasLasTablillas.append("Palacio_Camera_lejana2.cam",         1251, 1360, LanzaLenguas)
CamaraTodasLasTablillas.append("Palacio_Camera_segundo_impacto.cam", 1361, 1384, SegundoImpacto)
CamaraTodasLasTablillas.append("Palacio_Camera_agotamiento.cam",     1385, 1879, ContSegundoImpacto)




CamaraSoloTablillas = []
CamaraSoloTablillas.append("Palacio_Camera_personaje.cam",         0,   81, "")
CamaraSoloTablillas.append("Palacio_Camara_segunda5.cam",          82,  340, FullZBufferTablillas)



EspadaCamaraSoloTablillas = []
EspadaCamaraSoloTablillas.append("Palacio_Camera_personaje.cam",         0,   75, "")
EspadaCamaraSoloTablillas.append("Palacio_Camara_segunda3.cam",          76,  951, FullZBufferTablillas)

CamaraSuperPoder = []
CamaraSuperPoder.append("Palacio_Camera_personaje.cam",          0,   81, "")
CamaraSuperPoder.append("Palacio_Camara_segunda4.cam",           82,  351, FullZBufferTablillas)
CamaraSuperPoder.append("Palacio_Camera_arriba4.cam",           352,  493, ApagaLuzVerdeYApareceTornado)
CamaraSuperPoder.append("Palacio_Camera_lejana4.cam",           494,  655, AumentaFrecuenciaRayos)
CamaraSuperPoder.append("Palacio_Camera_temblor_rayo4.cam",     656,  732, Imprimelo)
CamaraSuperPoder.append("Palacio_Camara_cara_diosa4.cam",       733,  834, FadingCoolDeUnaAOtra)
CamaraSuperPoder.append("Palacio_Camera_lejana24.cam",          835,  950, LanzaLenguas)
CamaraSuperPoder.append("Palacio_Camera_segundo_impacto4.cam",  951,  974, SegundoImpacto)
CamaraSuperPoder.append("Palacio_Camera_agotamiento4.cam",      975, 1467, ContSegundoImpacto)


SectorInicial = Bladex.GetSector(94247, -3034, 191204)
SectorInicial.OnEnter = ComienzaLaHistoria




CreaEspadas()



CreaObjetosEnergeticos()



CreaTablillasX()


CreaHalosTablillasX()


CreaTornado()



CreaLuzFinal()



###
#######  Aparicion del personaje
###


import BackMisc


### Funcion: EnciendeMusicaInicio()

BackMisc.EXEC_IN_PLAYER_APPEARING = EnciendeMusicaInicio

Bladex.AddScheduledFunc(Bladex.GetTime(), BackMisc.PrevPlayerAppears, ())
