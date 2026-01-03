#############################################################################################
#
#								Script para la trampa de pinchos
#
#
#############################################################################################

import Doors
import Bladex
import darfuncs
import Button
import Sounds
import Traps_C

TrampaEstado = 1
TrampaPuerta_Abandonada = 0


#----------------------- PUERTAS-TRAMPA DE PINCHOS --------------------------
SonidoClack = Sounds.CreateEntitySound('../../Sounds/mechanism-operated-2.wav', 'SonidoClack')
SonidoClack.Volume=1.0
SonidoClack.MinDistance=5000
SonidoClack.MaxDistance=20000

SonidoClack2 = Sounds.CreateEntitySound('../../Sounds/metal-lever2.wav', 'SonidoClack2')
SonidoClack2.Volume=0.5
SonidoClack2.MinDistance=5000
SonidoClack2.MaxDistance=20000

Techo_sound=Sounds.CreateEntitySound('../../Sounds/ceiling-come-downL.wav', 'SonidoPuerta')
Techo_sound.Volume=0.5
Techo_sound.MinDistance=5000
Techo_sound.MaxDistance=20000

Puerta1_sound=Sounds.CreateEntitySound('../../Sounds/puerta-madera-deslizando.wav', 'SonidoPuerta')
Puerta1_sound.Volume=1
Puerta1_sound.MinDistance=10000
Puerta1_sound.MaxDistance=20000

Puerta1_sound_end=Sounds.CreateEntitySound('../../Sounds/Blade-menu-hit.wav', 'SonidoFinalPuerta')
Puerta1_sound_end.Volume=1
Puerta1_sound_end.MinDistance=10000
Puerta1_sound_end.MaxDistance=20000

Puerta2_sound=Sounds.CreateEntitySound('../../Sounds/puerta-madera-deslizando.wav', 'SonidoPuerta')
Puerta2_sound.Volume=1
Puerta2_sound.MinDistance=10000
Puerta2_sound.MaxDistance=20000

Puerta2_sound_end=Sounds.CreateEntitySound('../../Sounds/Blade-menu-hit.wav', 'SonidoFinalPuerta')
Puerta2_sound_end.Volume=1
Puerta2_sound_end.MinDistance=10000
Puerta2_sound_end.MaxDistance=20000

Bladex.AddParticleGType("DarkSand","GenericParticle",B_PARTICLE_GTYPE_BLEND,64)

for i in range(64):
	if(i>64):
		aux=0.0
	else:
		aux=(64.0-i)/32.0
	r=22
	g=20
	b=15
	size=100.0*(1.0-aux)

	Bladex.SetParticleGVal("DarkSand",i,r,g,b,255,size)


Bladex.AddParticleGType("DustDoor","SmokeParticle",B_PARTICLE_GTYPE_BLEND,128)

for i in range(128):
	if i>64:
		traux=0.0
	else:
		traux=(64.0-i)/64.0
	aux=(64.0-i)/64.0
	r=90
	g=70
	b=75
	a=255.0*(1.0-traux)**0.5
	size=10.0+aux*1700.0
	Bladex.SetParticleGVal("DustDoor",i,r,g,b,a,size)

#############################################################################################
#
#										PUERTAS Y PINCHOS
#
#############################################################################################


Puerta_Pinchos1=Doors.CreateDoor("PuertaPinchos1", (-48000,-30000,171500), (0,1,0), 0, 2800, Doors.OPENED)
Puerta_Pinchos2=Doors.CreateDoor("PuertaPinchos2", (-48000,-30000,183500), (0,1,0), 0, 2800, Doors.OPENED)
Techo_Pinchos  =Doors.CreateDoor("TechoPinchos",   (-48000,-30000,174000), (0,1,0),  0, 6000, Doors.OPENED)

Puerta_Pinchos2.Squezze = 0
Puerta_Pinchos1.Squezze = 0
Techo_Pinchos.Squezze = 1

##############	PUERTA 1 ############

Puerta_Pinchos1.opentype=Doors.AC_UNIF_DEC
Puerta_Pinchos1.o_init_vel=0
Puerta_Pinchos1.o_init_displ=200
Puerta_Pinchos1.o_med_vel=-500
Puerta_Pinchos1.o_med_displ=2400
Puerta_Pinchos1.o_end_vel=0
Puerta_Pinchos1.o_end_displ=200

Puerta_Pinchos1.closetype=Doors.AC_UNIF_DEC
Puerta_Pinchos1.c_init_vel=2000
Puerta_Pinchos1.c_init_displ=200
Puerta_Pinchos1.c_med_vel=5000
Puerta_Pinchos1.c_med_displ=2400
Puerta_Pinchos1.c_end_vel=3000
Puerta_Pinchos1.c_end_displ=200
Puerta_Pinchos1.OnEndCloseFunc=LineaPolvo1

Puerta_Pinchos1.SetWhileOpenSound(Puerta1_sound)
Puerta_Pinchos1.SetEndOpenSound(Puerta1_sound_end)
Puerta_Pinchos1.SetWhileCloseSound(Puerta1_sound)
Puerta_Pinchos1.SetEndCloseSound(Puerta1_sound_end)


##############	PUERTA 2 ############

Puerta_Pinchos2.opentype=Doors.AC_UNIF_DEC
Puerta_Pinchos2.o_init_vel=0
Puerta_Pinchos2.o_init_displ=200
Puerta_Pinchos2.o_med_vel=-500
Puerta_Pinchos2.o_med_displ=2400
Puerta_Pinchos2.o_end_vel=0
Puerta_Pinchos2.o_end_displ=200

Puerta_Pinchos2.closetype=Doors.AC_UNIF_DEC
Puerta_Pinchos2.c_init_vel=2000
Puerta_Pinchos2.c_init_displ=200
Puerta_Pinchos2.c_med_vel=5000
Puerta_Pinchos2.c_med_displ=2400
Puerta_Pinchos2.c_end_vel=3000
Puerta_Pinchos2.c_end_displ=200
Puerta_Pinchos2.OnEndCloseFunc=LineaPolvo2

Puerta_Pinchos2.SetWhileOpenSound(Puerta2_sound)
Puerta_Pinchos2.SetEndOpenSound(Puerta2_sound_end)
Puerta_Pinchos2.SetWhileCloseSound(Puerta2_sound)
Puerta_Pinchos2.SetEndCloseSound(Puerta2_sound_end)


##############	TECHO ############

Techo_Pinchos.opentype=Doors.AC_UNIF_DEC
Techo_Pinchos.o_init_vel=0
Techo_Pinchos.o_init_displ=1
Techo_Pinchos.o_med_vel=50
Techo_Pinchos.o_med_displ=800
Techo_Pinchos.o_end_vel=2100
Techo_Pinchos.o_end_displ=5300
Techo_Pinchos.OnEndOpenFunc=TrampaBajada

Techo_Pinchos.closetype=Doors.AC_UNIF_DEC
Techo_Pinchos.c_init_vel=1
Techo_Pinchos.c_init_displ=4000
Techo_Pinchos.c_med_vel=50
Techo_Pinchos.c_med_displ=100
Techo_Pinchos.c_end_vel=8000
Techo_Pinchos.c_end_displ=10
Techo_Pinchos.OnEndCloseFunc=TrampaBajada


#############################################################################################
#
#									PULSADORES
#
#############################################################################################

o=Bladex.CreateEntity("ButPin1","Bloque",-50888.151627,-29768.677280,176005.951040)
o.Orientation=0.707107,0.707107,0.000000,0.000000
darfuncs.SetHint(o,"Trigger")


o=Bladex.CreateEntity("ButPin2","Bloque",-50862.191879,-29777.715255,178993.731678)
o.Orientation=0.707107,0.707107,0.000000,0.000000
darfuncs.SetHint(o,"Trigger")


o=Bladex.CreateEntity("ButPin3","Bloque",-44547.667321,-29773.414521,176004.115576)
o.Orientation=0.707107,0.707107,0.000000,0.000000
darfuncs.SetHint(o,"Trigger")


o=Bladex.CreateEntity("ButPin4","Bloque",-44519.634504,-29780.624997,178997.289461)
o.Orientation=0.707107,0.707107,0.000000,0.000000
darfuncs.SetHint(o,"Trigger")


ButPin = Button.CreateButtonCombination(0,DesactivarTrampaPinchos,0)

bp1 = ButPin.AddButton("ButPin1",2,(-1,0,0),800,0,0,0)
bp2 = ButPin.AddButton("ButPin2",2,(-1,0,0),800,0,0,0)
bp3 = ButPin.AddButton("ButPin3",2,( 1,0,0),800,0,0,0)
bp4 = ButPin.AddButton("ButPin4",2,( 1,0,0),800,0,0,0)

darfuncs.EnterSecEvent(-48000,-30000,176000,ActivarTrampaPinchos)

#-48049.6053072, -29725.8403029, 168805.534932