#
# Todo: * Optimizar la inicializacion
#       * Rutina de botones
#
#  Dario.

import def_class
import Reference
#import Select
import Change
import Actions
import Doors
import Levers
import Locks
import Objects
import Sounds
import Bladex
import ReadGSFile
import Button
import AuxFuncs
#import AniSound


######################
## Game play Values ##
######################
TimerSecuence = 0.05  # secuence click every...

# Estrellitas y duendes
Bladex.AddParticleGType("Chispitas","Estrellita",B_PARTICLE_GTYPE_BLEND,64)
for i in range(64):
	r=0.0#255.0
	g=255.0
	b=255.0
	a   = (i*255)/64
	size= (64-i)*2
	Bladex.SetParticleGVal("Chispitas",i,r,g,b,a,size)



  ################
##### Energiza  ####
  ################

# particula de los ojos
Bladex.AddParticleGType("Energiza","GenericParticle",B_PARTICLE_GTYPE_BLEND,50)


# Polvillo de las paredes
##Bladex.AddParticleGType("Pedacillos","GenericParticle",B_PARTICLE_GTYPE_BLEND,1)
##Bladex.SetParticleGVal("Pedacillos",1,255,255,255,60,10)


Colu1=Bladex.GetSector(324000,6000,15000)
Colu2=Bladex.GetSector(326000,6000,15000)

Colu1.InitBreak((0,0,70),(0,1000,0),(700, 200,0),'piedra pesada')
Colu2.InitBreak((0,0,70),(0, 900,0),(800,-300,0),'piedra pesada')

Colu1.Active=0
Colu2.Active=0

#  cosa linda 1  (334136,-2409,-12271)  T(326670,975,-6542)
#  cosa linda 2  (315969,756,-12011)    T(324293,1070,-6479)
#  cosa linda 3  (325025,4524,3082)     T(324682,4083,13066)






### Adds a concentration particule time in a position



  ################
##### Energiza  ####
  ################


#maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta madera deslizando.wav", "MaderaDesliz")
#maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


########
########





###PLATAFORMA TABLILLA

mecanismo1=Sounds.CreateEntitySound("../../Sounds/mechanism3.wav", "Mecanismo1")
madera=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "Madera")

plat1=Doors.CreateDoor("Plat1", (324000,8000,10000), (0,0,1), 0, 12000, Doors.CLOSED)



plat1.opentype=Doors.UNIF
plat1.o_med_vel=-2300
plat1.o_med_displ=12000


plat1.closetype=Doors.UNIF
plat1.c_med_vel=2300
plat1.c_med_displ=12000

plat1.SetWhileCloseSound(madera)
plat1.SetWhileOpenSound(madera)
plat1.SetEndCloseSound(mecanismo1)
plat1.SetEndOpenSound(mecanismo1)


mecanismo2=Sounds.CreateEntitySound("../../Sounds/mechanism3.wav", "Mecanismo2")
madera2=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "Madera2")




plat2=Doors.CreateDoor("Plat2", (324000,8000,-20000), (0,0,-1), 0, 12000, Doors.OPENED)



plat2.opentype=Doors.UNIF
plat2.o_med_vel=-2300
plat2.o_med_displ=12000


plat2.closetype=Doors.UNIF
plat2.c_med_vel=2300
plat2.c_med_displ=12000

plat2.SetWhileCloseSound(madera2)
plat2.SetWhileOpenSound(madera2)
plat2.SetEndCloseSound(mecanismo2)
plat2.SetEndOpenSound(mecanismo2)








s1=Bladex.GetSector(325000,7000,-22000)
s1.OnEnter=Pasa


###trampa zona tablilla

granpiedradeslizando=Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav", "Granpiedradeslizando")
granpiedradeslizando.MaxDistance=50000
granpiedradeslizando.MinDistance=13000
granpiedradeslizando.Volume=1.0

cierrepiedra=Sounds.CreateEntitySound("../../Sounds/Stone-door-shut.wav", "Cierrepiedra")
cierrepiedra.MaxDistance=50000
cierrepiedra.MinDistance=13000
cierrepiedra.Volume=1.0

granpiedradeslizando2=Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav", "Granpiedradeslizando2")
granpiedradeslizando2.MaxDistance=50000
granpiedradeslizando2.MinDistance=13000
granpiedradeslizando2.Volume=1.0

cierrepiedra2=Sounds.CreateEntitySound("../../Sounds/Stone-door-shut.wav", "Cierrepiedra2")
cierrepiedra2.MaxDistance=50000
cierrepiedra2.MinDistance=13000
cierrepiedra2.Volume=1.0

granpiedradeslizando3=Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav", "Granpiedradeslizando3")
granpiedradeslizando3.MaxDistance=50000
granpiedradeslizando3.MinDistance=13000
granpiedradeslizando3.Volume=1.0

cierrepiedra3=Sounds.CreateEntitySound("../../Sounds/Stone-door-shut.wav", "Cierrepiedra3")
cierrepiedra3.MaxDistance=50000
cierrepiedra3.MinDistance=13000
cierrepiedra3.Volume=1.0

granpiedradeslizando4=Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav", "Granpiedradeslizando4")
granpiedradeslizando4.MaxDistance=50000
granpiedradeslizando4.MinDistance=13000
granpiedradeslizando4.Volume=1.0

cierrepiedra4=Sounds.CreateEntitySound("../../Sounds/Stone-door-shut.wav", "Cierrepiedra4")
cierrepiedra4.MaxDistance=50000
cierrepiedra4.MinDistance=13000
cierrepiedra4.Volume=1.0

granpiedradeslizando5=Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav", "Granpiedradeslizando5")
granpiedradeslizando5.MaxDistance=50000
granpiedradeslizando5.MinDistance=13000
granpiedradeslizando5.Volume=1.0

cierrepiedra5=Sounds.CreateEntitySound("../../Sounds/Stone-door-shut.wav", "Cierrepiedra5")
cierrepiedra5.MaxDistance=50000
cierrepiedra5.MinDistance=13000
cierrepiedra5.Volume=1.0


granpiedradeslizando6=Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav", "Granpiedradeslizando6")
granpiedradeslizando6.MaxDistance=50000
granpiedradeslizando6.MinDistance=13000
granpiedradeslizando6.Volume=1.0

cierrepiedra6=Sounds.CreateEntitySound("../../Sounds/Stone-door-shut.wav", "Cierrepiedra6")
cierrepiedra6.MaxDistance=50000
cierrepiedra6.MinDistance=13000
cierrepiedra6.Volume=1.0



EstaAbierta = 0


VelcidadDeLasPuertas=1000
##parte izquierda

izquierda1=Doors.CreateDoor("Izquierda1", (305500,10000,-3000), (0,-1,0), 0, 7500, Doors.CLOSED)


izquierda1.opentype=Doors.UNIF
izquierda1.o_med_vel=-VelcidadDeLasPuertas
izquierda1.o_med_displ=7500


izquierda1.closetype=Doors.UNIF
izquierda1.c_med_vel=VelcidadDeLasPuertas
izquierda1.c_med_displ=7500

izquierda1.SetWhileOpenSound(granpiedradeslizando)
izquierda1.SetEndOpenSound(cierrepiedra)

izquierda2=Doors.CreateDoor("Izquierda2", (305500,0,-3000), (0,1,0), 0, 7500, Doors.CLOSED)


izquierda2.opentype=Doors.UNIF
izquierda2.o_med_vel=-VelcidadDeLasPuertas
izquierda2.o_med_displ=7500


izquierda2.closetype=Doors.UNIF
izquierda2.c_med_vel=VelcidadDeLasPuertas
izquierda2.c_med_displ=7500

izquierda2.SetWhileOpenSound(granpiedradeslizando2)
izquierda2.SetEndOpenSound(cierrepiedra2)

izquierda2.OnEndOpenFunc = FuncionQueDiceSiEstaAbierta



##parte derecha


derecha1=Doors.CreateDoor("derecha1", (344000,10000,-3000), (0,-1,0), 0, 7500, Doors.CLOSED)

derecha1.opentype=Doors.UNIF
derecha1.o_med_vel=-VelcidadDeLasPuertas
derecha1.o_med_displ=7500


derecha1.closetype=Doors.UNIF
derecha1.c_med_vel=VelcidadDeLasPuertas
derecha1.c_med_displ=7500

derecha1.SetWhileOpenSound(granpiedradeslizando3)
derecha1.SetEndOpenSound(cierrepiedra3)


derecha2=Doors.CreateDoor("derecha2", (344000,0,-3000), (0,1,0), 0, 7500, Doors.CLOSED)


derecha2.opentype=Doors.UNIF
derecha2.o_med_vel=-VelcidadDeLasPuertas
derecha2.o_med_displ=7500


derecha2.closetype=Doors.UNIF
derecha2.c_med_vel=VelcidadDeLasPuertas
derecha2.c_med_displ=7500

derecha2.SetWhileOpenSound(granpiedradeslizando4)
derecha2.SetEndOpenSound(cierrepiedra4)




#
## Luz roja
#

LuzA = 0



###         Botones        ###
bt1=Bladex.CreateEntity("Boton0","Bloque",311051.763100,5539.629399,10702.106787)
bt1.Static=1
bt1.Scale=2.473119
bt1.Orientation=0.655618,0.655618,0.264887,-0.264887
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n


bt2=Bladex.CreateEntity("Boton1","Bloque",339147.054516,5438.314977,10703.875421)
bt2.Static=1
bt2.Scale=2.497850
bt2.Orientation=0.655618,0.655618,-0.264887,0.264887
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n


bt3=Bladex.CreateEntity("Boton2","Bloque",310926.011386,5458.236271,-17419.170970)
bt3.Static=1
bt3.Scale=2.448633
bt3.Orientation=0.653282,0.653282,-0.270598,0.270598
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n


bt4=Bladex.CreateEntity("Boton3","Bloque",338987.398192,5494.566093,-17424.841138)
bt4.Static=1
bt4.Scale=2.448633
bt4.Orientation=0.648459,0.648459,0.281958,-0.281958
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n



#
#  Rutina de los botones
##############################

#  bt1
#  ===
#
#  Cerrado   (311051,5539,10702)
#  Abierto   (313036,5528,8550)

btv1=1
btv2=1
btv3=1
btv4=1
SecActive=0

#########################################
#
# Sectores de botones
#
#  (1)->  311517,5454,10045
#  (2)->  311517,5454,10045
#
#########################################
sonido_clank=Bladex.CreateSound("../../Sounds/metal-lever3.wav","FIGHT")
sonido_clank.MaxDistance=1000000.0
sonido_clank.Volume     = 0.8


bts1         = Bladex.GetSector(311517,5454,10045)
#bts1.OnEnter = Button1Hit


bts2         = Bladex.GetSector(338828,5232,9985)
#bts2.OnEnter = Button2Hit

bts3         = Bladex.GetSector(311695,5196,-17137)
#bts3.OnEnter = Button3Hit


bts4         = Bladex.GetSector(338175,5011,-16527)
#bts4.OnEnter = Button4Hit







#----------------------------------------------------------------



Bladex.CreateTimer("OjoTimer",TimerSecuence)





# rayo electrico asesino!
##MAX_AMP= #800.0
#MIN_LEN= #200000.0

rayo1=Bladex.CreateEntity("Rayo1", "Entity ElectricBolt",345700.0, 3081.0, -1462.0)
rayo1.Target = 326229, 3678, 14665
rayo1.MaxAmplitude=400.0
rayo1.MinSectorLength=1000000.0
rayo1.Active=0
rayo1.Damage=0

rayo2=Bladex.CreateEntity("Rayo2", "Entity ElectricBolt",345700.0, 3081.0, -5062.0)
rayo2.Target=326229, 3678, 14665
rayo2.MaxAmplitude=400.0
rayo2.MinSectorLength=1000000.0
rayo2.Active=0
rayo2.Damage=0

rayo3=Bladex.CreateEntity("Rayo3", "Entity ElectricBolt",304300.0, 3081.0, -1462.0)
rayo3.Target= 323626, 3599, 14615
rayo3.MaxAmplitude=400.0
rayo3.MinSectorLength=1000000.0
rayo3.Active=0
rayo3.Damage=0

rayo4=Bladex.CreateEntity("Rayo4", "Entity ElectricBolt",304300.0, 3081.0, -5062.0 )
rayo4.Target= 323626, 3599, 14615
rayo4.MaxAmplitude=400.0
rayo4.MinSectorLength=1000000.0
rayo4.Active=0
rayo4.Damage=0






Ojo1A = def_class.ENERGIZA_EF(345700.0, 3081.0, -1462.0)
Ojo1B = def_class.ENERGIZA_EF(345700.0, 3081.0, -5062.0)
Ojo2A = def_class.ENERGIZA_EF(304300.0, 3081.0, -1462.0)
Ojo2B = def_class.ENERGIZA_EF(304300.0, 3081.0, -5062.0)

#
##
### Plataforma central
#############################
#def DesactivaSecuencia():


#def ActivaSecuencia():


central             = Doors.CreateDoor("central", (325000,7250,-3000), (0,-1,0), 0, 400, Doors.CLOSED)


central.opentype      = Doors.UNIF
central.o_med_vel     = 1
central.o_med_displ   = 300
#central.OnEndOpenFunc = ActivaSecuencia



central.closetype     = Doors.UNIF
central.c_med_vel     = -1
central.c_med_displ   = 300
#central.OnEndCloseFunc = DesactivaSecuencia








res=ReadGSFile.ReadGhostSectorFile("trampas.sf")
for igs in res:
   Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

Bladex.SetTriggerSectorFunc("tablilla", "OnEnter", PisaTrap )
Bladex.SetTriggerSectorFunc("tablilla", "OnLeave", Arruga )

char = Bladex.GetEntity("Player1")
char.SendTriggerSectorMsgs = 1

_SndConcentRay=Bladex.CreateSound("../../Sounds/M-CAMPO-MAG.wav","SndConcentRay")
_SndConcentRay.MinDistance=100000.0
_SndConcentRay.MaxDistance=1000000.0

_SndConcentTunder=Bladex.CreateSound("../../Sounds/energy-ball.wav","SndConcentTunder")
_SndConcentTunder.MinDistance=100000.0
_SndConcentTunder.MaxDistance=1000000.0

#_SndConcentRay.Play(324843.784557, 6403.39003147, -4043.70232667,-1)

_SndTunderRay=Bladex.CreateSound("../../Sounds/M-IMPACTO-FUEGO.wav","SndTunderRay")
_SndTunderRay.MinDistance=100000.0
_SndTunderRay.MaxDistance=1000000.0
