import Bladex
import Doors
import Levers
import Locks
import Objects
import Sounds
import AuxFuncs
import Sparks
import darfuncs
import Stars

## puerta peazo golem inicial

puertapiedra= Sounds.CreateEntitySound("../../Sounds/puerta-piedra-deslizando-2.wav", "Puertapiedra")
puertapiedra.MaxDistance=50000
puertapiedra.MinDistance=13000
puertapiedra.Volume=1.0

puertagolem=Doors.CreateDoor("Puertagolem", (336000,32500,-40000), (0,1,0), 0, 6250, Doors.OPENED)




puertagolem.opentype=Doors.UNIF
puertagolem.o_med_vel=-700
puertagolem.o_med_displ=6250


puertagolem.closetype=Doors.UNIF
puertagolem.c_med_vel=700
puertagolem.c_med_displ=6250

puertagolem.SetWhileOpenSound(puertapiedra)
puertagolem.SetWhileCloseSound(puertapiedra)

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
sonidofinrastrillo=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

########
########


###Puerta rastrillo cuya llave tiene el orco que huye.

rastorc=Bladex.CreateEntity("Rastorc","Rastrillo",313857.921478,36336.620663,-63365.678680,"Physic")
rastorc.Scale=1.160969
rastorc.Orientation=0.707107,0.707107,0.000000,0.000000
rastorc.CastShadows=0
Sparks.SetMetalSparkling("Rastorc")

rastorcdin=Objects.CreateDinamicObject("Rastorc")



###cerradura y llave del rastrillo anterior


cerraduraorc=Locks.PlaceLock("cerradura1","Cerraduracobox",(316956.885340,38551.410726,-62481.104206),(0.500000,0.500000,-0.500000,0.500000),1.612226)
cerraduraorc.key="Llaveorc"
darfuncs.SetHint(cerraduraorc.obj,"Guardian Lock")


cerraduraorc.OnUnLockFunc=Abreorc
cerraduraorc.OnUnLockArgs=()

### nuevo rastrillo demonio saltarin

rastdem=Bladex.CreateEntity("Rastdem","Rastrillo",443314.263548,78006.793275,21747.834203,"Physic")
rastdem.Scale=1.000000
rastdem.Orientation=0.500000,0.500000,0.500000,-0.500000
Sparks.SetMetalSparkling("Rastdem")

rastdemdin=Objects.CreateDinamicObject("Rastdem")



###2 Barrotes en deposito de agua inicialmente cerrados que bajan al morir el monstruo guardian de la zona

sbarrote1= Sounds.CreateEntitySound("../../Sounds/puerta-piedra-deslizando.wav", "Sbarrote1")
sbarrote1.MaxDistance=500000
sbarrote1.MinDistance=250000
sbarrote1.Volume=0.2

barrote1=Doors.CreateDoor("Barrote1", (387000,60000,-37000), (0,-1,0), 0, 4000, Doors.OPENED)




barrote1.opentype=Doors.UNIF
barrote1.o_med_vel=-500
barrote1.o_med_displ=4000


barrote1.closetype=Doors.UNIF
barrote1.c_med_vel=500
barrote1.c_med_displ=4000

barrote1.SetWhileOpenSound(sbarrote1)




sbarrote2= Sounds.CreateEntitySound("../../Sounds/puerta-piedra-deslizando.wav", "Sbarrote2")
sbarrote2.MaxDistance=500000
sbarrote2.MinDistance=250000
sbarrote2.Volume=0.2

barrote2=Doors.CreateDoor("Barrote2", (387000,60000,-38000), (0,-1,0), 0, 4000, Doors.OPENED)


barrote2.opentype=Doors.UNIF
barrote2.o_med_vel=-500
barrote2.o_med_displ=4000


barrote2.closetype=Doors.UNIF
barrote2.c_med_vel=500
barrote2.c_med_displ=4000

barrote2.SetWhileOpenSound(sbarrote2)


## puerta de acceso a la zona del vampiro

# hoja izquierda


svampi= Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "Svampi")
svampi.MaxDistance=500000
svampi.MinDistance=250000
svampi.Volume=1.0

svampif= Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "Svampif")
svampif.MaxDistance=500000
svampif.MinDistance=250000
svampif.Volume=1.0

vampi=Doors.CreateDoor("Vampi", (421000,78000,-26000), (1,0,0), 0, 2500, Doors.CLOSED)


vampi.opentype=Doors.UNIF
vampi.o_med_vel=-500
vampi.o_med_displ=2500

vampi.SetWhileOpenSound(svampi)
vampi.SetEndOpenSound(svampif)


##hoja derecha

svampd= Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "Svampd")
svampd.MaxDistance=500000
svampd.MinDistance=250000
svampd.Volume=1.0

svampdf= Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "Svampdf")
svampdf.MaxDistance=500000
svampdf.MinDistance=250000
svampdf.Volume=1.0


vampd=Doors.CreateDoor("Vampd", (423000,78000,-26000), (-1,0,0), 0, 2500, Doors.CLOSED)


vampd.opentype=Doors.UNIF
vampd.o_med_vel=-500
vampd.o_med_displ=2500

vampd.SetWhileOpenSound(svampd)
vampd.SetEndOpenSound(svampdf)

## cerradura de la susodicha puerta

cerraduravamp=Locks.PlaceLock("Cerraduravamp","Cerraduracobox",(424900.759453,76934.600952,-27512.259550),(0.364187,0.364187,0.606109,-0.606109),1.661078)
cerraduravamp.key="Llavevamp"
darfuncs.SetHint(cerraduravamp.obj,"Vampire Lock")

cerraduravamp.OnUnLockFunc=Abrevamp
cerraduravampOnUnLockArgs=()

## llave que abre la puerta

Llavevamp=Bladex.CreateEntity("Llavevamp","Llavecobox",395364.454538,63471.701667,-35000,"Physic")
Llavevamp.Scale=1.000000
Llavevamp.Solid=0
Llavevamp.Orientation=0.980694,-0.003509,-0.195372,0.007601
darfuncs.SetHint(Llavevamp,"Vampire Key")
Stars.Twinkle(Llavevamp.Name) # dis funktion is cul !
# tuinquel tuinquel litel estar....

#########
#########
#########
########
########
#######






###PUERTAS ENORMES EN CAMINO CON ABISMO A AMBOS LADOS



## barrotes zona golem -quitar cuando est� hecho el script-



sbarrote1b= Sounds.CreateEntitySound("../../Sounds/puerta-piedra-deslizando.wav", "Sbarrote1b")
sbarrote1b.MaxDistance=500000
sbarrote1b.MinDistance=250000
sbarrote1b.Volume=0.2

barrote1b=Doors.CreateDoor("Barrote1b", (394500,60000,-29500), (0,-1,0), 0, 4000, Doors.OPENED)


barrote1b.opentype=Doors.UNIF
barrote1b.o_med_vel=-500
barrote1b.o_med_displ=4000


barrote1b.closetype=Doors.UNIF
barrote1b.c_med_vel=500
barrote1b.c_med_displ=4000

barrote1b.SetWhileOpenSound(sbarrote1b)




sbarrote2b= Sounds.CreateEntitySound("../../Sounds/puerta-piedra-deslizando.wav", "Sbarrote2b")
sbarrote2b.MaxDistance=500000
sbarrote2b.MinDistance=250000
sbarrote2b.Volume=0.2

barrote2b=Doors.CreateDoor("Barrote2b", (396000,60000,-29500), (0,-1,0), 0, 4000, Doors.OPENED)


barrote2b.opentype=Doors.UNIF
barrote2b.o_med_vel=-500
barrote2b.o_med_displ=4000


barrote2b.closetype=Doors.UNIF
barrote2b.c_med_vel=500
barrote2b.c_med_displ=4000

barrote2b.SetWhileOpenSound(sbarrote2b)
