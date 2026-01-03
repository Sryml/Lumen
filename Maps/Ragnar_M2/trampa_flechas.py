import def_class
import Traps_C

MESSAGE_START_WEAPON         =7
MESSAGE_STOP_WEAPON          =8


B_PARTICLE_GTYPE_COPY=0
B_PARTICLE_GTYPE_BLEND=1
B_PARTICLE_GTYPE_ADD=2
B_PARTICLE_GTYPE_MUL=3


Bladex.AddParticleGType("Dust1","SmokeParticle",B_PARTICLE_GTYPE_BLEND,15)

for i in range(15):
#	if i>15:
#		traux=0.0
#	else:
#		traux=(15.0-i)/15.0
	aux=(15.0-i)/15.0
	r=255
	g=230
	b=210
	a=80.0*(1.0-aux)**0.5
	size=1.0+aux*350.0
	Bladex.SetParticleGVal("Dust1",i,r,g,b,a,size)

Bladex.AddParticleGType("Dust2","SmokeParticle",B_PARTICLE_GTYPE_BLEND,15)

for i in range(15):
#	if i>15:
#		traux=0.0
#	else:
#		traux=(15.0-i)/15.0
	aux=(15.0-i)/15.0
	r=255
	g=230
	b=210
	a=80.0*(1.0-aux)**0.5
	size=1.0+aux*250.0
	Bladex.SetParticleGVal("Dust2",i,r,g,b,a,size)

Bladex.AddParticleGType("Dust3","SmokeParticle",B_PARTICLE_GTYPE_BLEND,15)

for i in range(15):
#	if i>15:
#		traux=0.0
#	else:
#		traux=(15.0-i)/15.0
	aux=(15.0-i)/15.0
	r=255
	g=230
	b=210
	a=80.0*(1.0-aux)**0.5
	size=1.0+aux*150.0
	Bladex.SetParticleGVal("Dust3",i,r,g,b,a,size)


Tiempo_DesactivacionFlechas1 = 0
Tiempo_DesactivacionFlechas2 = 0
Trampa_Flechas_Activada1 = 0
Trampa_Flechas_Activada2 = 0
Trampa_Flechas = 0
Player_Intro1 = 0
Player_Intro2 = 0


Sonido_Flechas_Activadas = Bladex.CreateSound('../../Sounds/trap-clicked.wav', 'ActivadoFlechas')
Sonido_Flechas_Activadas.Volume=0.7
Sonido_Flechas_Activadas.MinDistance=7000
Sonido_Flechas_Activadas.MaxDistance=60000

Sonido_Flechas_Desactivadas = Bladex.CreateSound('../../Sounds/metal-lever3.wav', 'ActivadoFlechas')
Sonido_Flechas_Desactivadas.Volume=0.7
Sonido_Flechas_Desactivadas.MinDistance=7000
Sonido_Flechas_Desactivadas.MaxDistance=60000


Entrada1_1 = Bladex.GetSector(-141250,-7000,-104500)
Entrada2_1 = Bladex.GetSector(-141000,-7000,-94500)
Habitaci_1 = Bladex.GetSector(-141000,-7000,-100500)

Entrada1_1.OnEnter = ActivarTrampaFlechas
Entrada2_1.OnEnter = ActivarTrampaFlechas
Habitaci_1.OnEnter = ActivarTrampaFlechas
Entrada1_1.OnLeave = DesactivarTrampaFlechas
Entrada2_1.OnLeave = DesactivarTrampaFlechas
Habitaci_1.OnLeave = DesactivarTrampaFlechas

Entrada1_2 = Bladex.GetSector(-125250,-7000,-104500)
Entrada2_2 = Bladex.GetSector(-125250,-7000,-94500)
Habitaci_2 = Bladex.GetSector(-125250,-7000,-100500)

Entrada1_2.OnEnter = ActivarTrampaFlechas2
Entrada2_2.OnEnter = ActivarTrampaFlechas2
Habitaci_2.OnEnter = ActivarTrampaFlechas2
Entrada1_2.OnLeave = DesactivarTrampaFlechas2
Entrada2_2.OnLeave = DesactivarTrampaFlechas2
Habitaci_2.OnLeave = DesactivarTrampaFlechas2


InitArrow("Pivote10",1)
InitArrow("Pivote11",1)
InitArrow("Pivote12",1)
InitArrow("Pivote13",1)

InitArrow("Pivote0",-1)
InitArrow("Pivote1",-1)
InitArrow("Pivote2",-1)
InitArrow("Pivote3",-1)