#############################################################################################
#
#								Script para la trampa de pinchos
#
#
#############################################################################################

import Doors
import Bladex

CLOSED=0
OPENED=1
AC_UNIF_DEC=4

MESSAGE_START_WEAPON         =7
MESSAGE_STOP_WEAPON          =8

Trampa_Estado = 1
Trampa_Pulsadores_Activados = 0
Trampa_Puerta_Abandonada = 0

Bladex.AddParticleGType("SpDust","SmokeParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	if i>30:
		traux=0.0
	else:
		traux=((30.0-i)/30.0)**0.5
	aux=((60.0-i)/60.0)**0.5
	r=255
	g=230
	b=210
	a=60.0*(1.0-traux)
	size=7.0+aux*700.0
	Bladex.SetParticleGVal("SpDust",i,r,g,b,a,size)


#############################################################################################
#
#										SONIDOS
#
#############################################################################################

Sonido_Trampa_Activada = Bladex.CreateSound('../../Sounds/trap-clicked.wav', 'SonidoActivacion')
Sonido_Trampa_Activada.Volume=1
Sonido_Trampa_Activada.MinDistance=15000
Sonido_Trampa_Activada.MaxDistance=20000

Sonido_Trampa_Bajando1 = Bladex.CreateSound('../../Sounds/trap-trigger1.wav', 'SonidoCadena')
Sonido_Trampa_Bajando1.Volume=1
Sonido_Trampa_Bajando1.MinDistance=15000
Sonido_Trampa_Bajando1.MaxDistance=20000

Sonido_Trampa_Bajando2 = Bladex.CreateSound('../../Sounds/stone-slide-and-hit.wav', 'SonidoPiedra')
Sonido_Trampa_Bajando2.Volume=0.5
Sonido_Trampa_Bajando2.MinDistance=15000
Sonido_Trampa_Bajando2.MaxDistance=20000

Sonido_Trampa_Subiendo1 = Bladex.CreateSound('../../Sounds/drawbridge-loop.wav', 'SonidoCadena1')
Sonido_Trampa_Subiendo1.Volume=0.5
Sonido_Trampa_Subiendo1.MinDistance=15000
Sonido_Trampa_Subiendo1.MaxDistance=20000

Sonido_Trampa_Subiendo2 = Bladex.CreateSound('../../Sounds/ceiling-come-down.wav', 'SonidoPiedra1')
Sonido_Trampa_Subiendo2.Volume=1
Sonido_Trampa_Subiendo2.MinDistance=15000
Sonido_Trampa_Subiendo2.MaxDistance=20000

Sonido_Trampa_Reactivada = Bladex.CreateSound('../../Sounds/metal-lever3.wav', 'SonidoReactivacion')
Sonido_Trampa_Reactivada.Volume=1
Sonido_Trampa_Reactivada.MinDistance=15000
Sonido_Trampa_Reactivada.MaxDistance=20000

Sonido_Hit1 = Bladex.CreateSound('../../Sounds/Door-kick.wav', 'Hit1')
Sonido_Hit1.Volume=1
Sonido_Hit1.MinDistance=15000
Sonido_Hit1.MaxDistance=20000

Sonido_Hit2 = Bladex.CreateSound('../../Sounds/Stone-door-shut.wav', 'Hit2')
Sonido_Hit2.Volume=1
Sonido_Hit2.MinDistance=15000
Sonido_Hit2.MaxDistance=20000



#Activador_Pinchos = Doors.CreateDoor("ActivadorPinchos",   (-124000,-24000,-100000), (0,-1,0),  500, 2000, OPENED)
Techo_Pinchos1 = Doors.CreateDoor("TechoPinchos",   (-124000,-25000,-100000), (0,1,0),  0, 2000, OPENED)
Techo_Pinchos1.Squezze = 1
Techo_Pinchos2 = Doors.CreateDoor("TechoPinchos1",   (-124000,-25000,-97000), (0,1,0),  0, 2000, OPENED)
Techo_Pinchos2.Squezze = 1
Techo_Pinchos3 = Doors.CreateDoor("TechoPinchos2",   (-124000,-25000,-103000), (0,1,0),  0, 2000, OPENED)
Techo_Pinchos3.Squezze = 1


SectorEntradaTrampa = Bladex.GetSector(-124000,-24000,-100000)
SectorEntradaTrampa.OnEnter = ActivarTrampaPinchos

#char = Bladex.GetEntity("Player1")
#char.Position = 125465.104071, -23248.5, -109325.45176
