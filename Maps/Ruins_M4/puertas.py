import Bladex
import Levers
import Objects
import Doors
import Sounds
import Locks
import Sparks
import Stars
import darfuncs



###############################################
#     Puerta de la piramide del principio     #
###############################################

### Esta puerta esta en el Pinchos.py



################################
#     Puerta del laberinto     #
################################

### Esta puerta esta en el pulsadores.py



##########################################
#     Puerta secreta del subterraneo     #
##########################################


deslizpuertasecretasub=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizPuertaSecretaSub")
golpepuertasecretasub=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe2.wav", "GolpePuertaSecretaSub")

puertasecretasub=Doors.CreateDoor("PuertaSecretaSub", (-57250,4500,5250), (0,1,0), 350, 3100, Doors.CLOSED)
puertasecretasub.Squezze=1

puertasecretasub.opentype=Doors.AC_UNIF
puertasecretasub.o_init_vel=0
puertasecretasub.o_init_displ=250
puertasecretasub.o_med_vel=-1000
puertasecretasub.o_med_displ=2500

puertasecretasub.closetype=Doors.AC
puertasecretasub.c_init_displ=2750
puertasecretasub.c_med_vel=5000

puertasecretasub.SetWhileOpenSound(deslizpuertasecretasub)
puertasecretasub.SetEndOpenSound(golpepuertasecretasub)

puertasecretasub.SetWhileCloseSound(deslizpuertasecretasub)
puertasecretasub.SetEndCloseSound(golpepuertasecretasub)

palancasecretasub=Levers.PlaceLever("PalancaSecretaSub",Levers.LeverType3,(-55750,5000,4600),(0.707107,0.707107,0.000000,0.000000),1.0)

palancasecretasub.mode=0

######## Funcion: ParaArenillaPuertaSecretaSub()

######## Funcion: AbrePuertaSecretaSub()

######## Funcion: CierraPuertaSecretaSub2()

######## Funcion: CierraPuertaSecretaSub()

puertasecretasub.OnEndOpenFunc=ParaArenillaPuertaSecretaSub
puertasecretasub.OnEndCloseFunc=CierraPuertaSecretaSub2

palancasecretasub.OnTurnOnFunc=AbrePuertaSecretaSub
palancasecretasub.OnTurnOnArgs=()

palancasecretasub.OnTurnOffFunc=CierraPuertaSecretaSub
palancasecretasub.OnTurnOffArgs=()



#################################
#     Puerta doble del pozo     #
#################################

puertapozodesliz=Sounds.CreateEntitySound("../../Sounds/puerta-pie-desliz-no-loop.wav", "PuertaPozoDesliz")
puertapozogolpe=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe2.wav", "PuertaPozoGolpe")

puertapozo1=Doors.CreateDoor("PuertaPozo1", (31750,8000,-53500), (0,0,-1), 0, 1875, Doors.CLOSED)
puertapozo1.Squezze=1

puertapozo1.opentype=Doors.AC_UNIF
puertapozo1.o_init_vel=0
puertapozo1.o_init_displ=175
puertapozo1.o_med_vel=-900
puertapozo1.o_med_displ=1700

puertapozo1.closetype=Doors.UNIF
puertapozo1.c_med_displ=1875
puertapozo1.c_med_vel=900

puertapozo1.SetWhileOpenSound(puertapozodesliz)
puertapozo1.SetEndOpenSound(puertapozogolpe)

puertapozo1.SetWhileCloseSound(puertapozodesliz)
puertapozo1.SetEndCloseSound(puertapozogolpe)

puertapozo2=Doors.CreateDoor("PuertaPozo2", (31750,8000,-54000), (0,0,1), 0, 1875, Doors.CLOSED)
puertapozo2.Squezze=1

puertapozo2.opentype=Doors.AC_UNIF
puertapozo2.o_init_vel=0
puertapozo2.o_init_displ=175
puertapozo2.o_med_vel=-900
puertapozo2.o_med_displ=1700

puertapozo2.closetype=Doors.UNIF
puertapozo2.c_med_displ=1875
puertapozo2.c_med_vel=900

llavepuertapozo=Bladex.CreateEntity("LlavePuertaPozo","Llavecutre",48500,1970,-47000,"Physic")
llavepuertapozo.Scale=1.4
llavepuertapozo.Orientation=0.998135,0.061049,0.000000,0.000000
darfuncs.SetHint(llavepuertapozo,"Well Key")
Stars.Twinkle("LlavePuertaPozo")

cerradurapozo=Locks.PlaceLock("CerraduraPozo","Cerraduracutre",(32300,8000,-51650),(0.707107,0.707107,0.000000,0.000000),3.0)
cerradurapozo.key="LlavePuertaPozo"
darfuncs.SetHint(cerradurapozo.obj,"Well Lock")

######## Funcion: AbrePuertaPozo()

######## Funcion: CierraPuertaPozo2()

######## Funcion: CierraPuertaPozo()

puertapozo1.OnEndCloseFunc=CierraPuertaPozo2

cerradurapozo.OnUnLockFunc=AbrePuertaPozo
cerradurapozo.OnUnLockArgs=()

cerradurapozo.OnLockFunc=CierraPuertaPozo
cerradurapozo.OnLockArgs=()



####################################
#     Rastrillo del cementerio     #
####################################

palancacementerio=Levers.PlaceLever("PalancaCementerio",Levers.LeverType3,(-22873.740000,-1500.000000,-31145.126000),(0.707107,0.707107,0.000000,0.000000),1.0)
palancacementerio.mode=2

rastrillocementerio=Bladex.CreateEntity("RastrilloCementerio","Rastrillo",-24033.181000,-2486.473000,-24021.323000,"Physic")
rastrillocementerio.Scale=0.878663
rastrillocementerio.Orientation=0.653282,0.653282,0.270598,-0.270598
rastrillocementerio=Sparks.SetMetalSparkling("RastrilloCementerio")
rastrillocementerio.Frozen=1

rastrillocementeriodin=Objects.CreateDinamicObject("RastrilloCementerio")
rastrillocementeriodin.Timer="Timer30"

sonidodeslizamientorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoDeslizamientoRastrillo")
sonidodeslizamientorastrillo.Volume=0.8
sonidodeslizamientorastrillo.MinDistance=5000
sonidodeslizamientorastrillo.MaxDistance=20000

sonidogolperastrillo=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "SonidoGolpeRastrillo")
sonidogolperastrillo.Volume=0.8
sonidogolperastrillo.MinDistance=5000
sonidogolperastrillo.MaxDistance=20000

######## Funcion: AbreRastrilloCementerio()

palancacementerio.OnTurnOnFunc=AbreRastrilloCementerio
palancacementerio.OnTurnOnArgs=()



##############################
#     Rastrillo del pozo     #
##############################

rastrpozo=Bladex.CreateEntity("RastrilloPozo","Rastrillo",24000.0,-2900.0,-24000.0,"Physic")
rastrpozo.Scale=0.96
rastrpozo.Orientation=0.653282,0.653282,-0.270598,0.270598
rastrpozo=Sparks.SetMetalSparkling("RastrilloPozo")
rastrpozo.Frozen=1

rastrpozodin=Objects.CreateDinamicObject("RastrilloPozo")
rastrpozodin.Timer="Timer30"

snddeslizrastrpozo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoDeslizRastrilloPozo")
snddeslizrastrpozo.Volume=0.8
snddeslizrastrpozo.MinDistance=5000
snddeslizrastrpozo.MaxDistance=20000

sndgolperastrpozo=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "SonidoGolpeRastrilloPozo")
sndgolperastrpozo.Volume=0.8
sndgolperastrpozo.MinDistance=5000
sndgolperastrpozo.MaxDistance=20000



############################
#     Puerta del final     #
############################

puertafinaldesliz=Sounds.CreateEntitySound("../../Sounds/puerta-pie-desliz-no-loop.wav", "PuertaFinalDesliz")
puertafinalgolpe=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe2.wav", "PuertaFinalGolpe")

puertafinal=Doors.CreateDoor("PuertaFinal", (-22250,5000,12750), (0,0,-1), 250, 2625, Doors.CLOSED)
puertafinal.Squezze=1

puertafinal.opentype=Doors.AC_UNIF
puertafinal.o_init_vel=0
puertafinal.o_init_displ=250
puertafinal.o_med_vel=-1000
puertafinal.o_med_displ=2125

puertafinal.closetype=Doors.AC_UNIF
puertafinal.c_init_vel=0
puertafinal.c_init_displ=250
puertafinal.c_med_vel=1000
puertafinal.c_med_displ=2125

puertafinal.SetWhileOpenSound(puertafinaldesliz)
puertafinal.SetEndOpenSound(puertafinalgolpe)

puertafinal.SetWhileCloseSound(puertafinaldesliz)
puertafinal.SetEndCloseSound(puertafinalgolpe)

llavepuertafinal=Bladex.CreateEntity("LlavePuertaFinal","Llavecobox",-46360.0,-1532.462543,46000.0,"Physic")
llavepuertafinal.Scale=1.4
llavepuertafinal.Orientation=0.975244,-0.000956,-0.221118,-0.002351
darfuncs.SetHint(llavepuertafinal,"Temple Key")
Stars.Twinkle("LlavePuertaFinal")

cerradurapuertafinal=Locks.PlaceLock("CerraduraPuertaFinal","Cerraduracobox",(-23020.0,5500.0,11150.0),(0.000000,0.000000,0.707107,-0.707107),2.0)
cerradurapuertafinal.key="LlavePuertaFinal"
darfuncs.SetHint(cerradurapuertafinal.obj,"Temple Lock")

######## Funcion: AbrePuertaFinal()

######## Funcion: CierraPuertaFinal()

######## Funcion: CierraPuertaFinal2()

puertafinal.OnEndCloseFunc=CierraPuertaFinal2

cerradurapuertafinal.OnUnLockFunc=AbrePuertaFinal
cerradurapuertafinal.OnUnLockArgs=()

cerradurapuertafinal.OnLockFunc=CierraPuertaFinal
cerradurapuertafinal.OnLockArgs=()



##########################################
#     Puerta de pinchos del mausoleo     #
##########################################

pinchopue1=Bladex.CreateEntity("PinchoPuerta1","PinchoManuel",-60000.0,-2000.0,-43000.0,"Physic")
pinchopue1.Scale=1.16
pinchopue1.Orientation=0.000000,0.000000,0.707107,-0.707107
pinchopue1=Sparks.SetMetalSparkling("PinchoPuerta1")
pinchopue1.Frozen=1

pinchopue2=Bladex.CreateEntity("PinchoPuerta2","PinchoManuel",-59650.0,-3000.0,-43000.0,"Physic")
pinchopue2.Scale=1.16
pinchopue2.Orientation=0.000000,0.000000,0.707107,-0.707107
pinchopue2=Sparks.SetMetalSparkling("PinchoPuerta2")
pinchopue2.Frozen=1

pinchopue3=Bladex.CreateEntity("PinchoPuerta3","PinchoManuel",-60000.0,-4000.0,-43000.0,"Physic")
pinchopue3.Scale=1.16
pinchopue3.Orientation=0.000000,0.000000,0.707107,-0.707107
pinchopue3=Sparks.SetMetalSparkling("PinchoPuerta3")
pinchopue3.Frozen=1

pinchopue1din=Objects.CreateDinamicObject("PinchoPuerta1")
pinchopue2din=Objects.CreateDinamicObject("PinchoPuerta2")
pinchopue3din=Objects.CreateDinamicObject("PinchoPuerta3")
pinchopue1din.Timer=pinchopue2din.Timer=pinchopue3din.Timer="Timer30"

sonidopalanca=Bladex.CreateSound("../../Sounds/metal-lever3.wav", "SonidoPalanca")
sonidopalanca.Volume=0.5

palancamausoleo=Levers.PlaceLever("PalancaMausoleo",Levers.LeverType3,(-57857.813000,-1250.000000,-27721.731000),(0.500000,0.500000,-0.500000,0.500000),1.0)
palancamausoleo.mode=0

pinchosmausyaabiertos=0


######## Funcion: AbrePinchosMausoleo()

######## Funcion: CierraPinchosMausoleo()


palancamausoleo.OnTurnOnFunc=AbrePinchosMausoleo
palancamausoleo.OnTurnOnArgs=()

palancamausoleo.OnTurnOffFunc=CierraPinchosMausoleo
palancamausoleo.OnTurnOffArgs=()




############################################
#     Puertas de estacas del laberinto     #
############################################

#
### Estacas A
#

est1a=Bladex.CreateEntity("Estaca1a","EstacaFernando",25437.500000,-2200.000000,41812.500000)
est1a.Scale=1.000000
est1a.Orientation=0.707107,0.707107,0.000000,0.000000

est2a=Bladex.CreateEntity("Estaca2a","EstacaFernando",25062.500000,-2050.000000,42187.500000)
est2a.Scale=1.000000
est2a.Orientation=0.612372,0.612372,-0.353553,0.353553

est3a=Bladex.CreateEntity("Estaca3a","EstacaFernando",24687.500000,-2100.000000,42562.500000)
est3a.Scale=1.000000
est3a.Orientation=0.500000,0.500000,0.500000,-0.500000

est4a=Bladex.CreateEntity("Estaca4a","EstacaFernando",24312.500000,-2200.000000,42937.500000)
est4a.Scale=1.000000
est4a.Orientation=0.707107,0.707107,0.000000,0.000000

est5a=Bladex.CreateEntity("Estaca5a","EstacaFernando",23937.500000,-2050.000000,43312.500000)
est5a.Scale=1.000000
est5a.Orientation=0.092296,0.092296,0.701057,-0.701057

est6a=Bladex.CreateEntity("Estaca6a","EstacaFernando",25812.500000,-2050.000000,41437.500000)
est6a.Scale=1.000000
est6a.Orientation=0.500000,0.500000,-0.500000,0.500000

est3adin=Objects.CreateDinamicObject("Estaca3a")
est3adin.Timer="Timer30"

yest3a=est3a.Position[1]

palancaestacasa=Levers.PlaceLever("PalancaEstacasA",Levers.LeverType3,(30353.322000,-1400.000000,46443.766000),(0.653282,0.653282,0.270598,-0.270598),1.0)
palancaestacasa.mode=2


######## Funcion: MueveEstacasA()

######## Funcion: AbreEstacasA()

palancaestacasa.OnTurnOnFunc=AbreEstacasA
palancaestacasa.OnTurnOnArgs=()


#
### Estacas B
#

est1b=Bladex.CreateEntity("Estaca1b","EstacaFernando",64125.000000,-2250.000000,31125.000000)
est1b.Scale=1.000000
est1b.Orientation=0.707107,0.707107,0.000000,0.000000

est2b=Bladex.CreateEntity("Estaca2b","EstacaFernando",63750.000000,-2100.000000,30750.000000)
est2b.Scale=1.000000
est2b.Orientation=0.560986,0.560986,0.430459,-0.430459

est3b=Bladex.CreateEntity("Estaca3b","EstacaFernando",63375.000000,-2200.000000,30375.000000)
est3b.Scale=1.000000
est3b.Orientation=0.270598,0.270598,0.653282,-0.653282

est4b=Bladex.CreateEntity("Estaca4b","EstacaFernando",63000.000000,-2250.000000,30000.000000)
est4b.Scale=1.000000
est4b.Orientation=0.707107,0.707107,0.000000,0.000000

est5b=Bladex.CreateEntity("Estaca5b","EstacaFernando",62625.000000,-2050.000000,29625.000000)
est5b.Scale=1.000000
est5b.Orientation=0.454519,0.454519,-0.541675,0.541675

est3bdin=Objects.CreateDinamicObject("Estaca3b")
est3bdin.Timer="Timer30"

yest3b=est3b.Position[1]

palancaestacasb=Levers.PlaceLever("PalancaEstacasB",Levers.LeverType3,(61656.134000,-400.000000,37377.551000),(0.500000,0.500000,-0.500000,0.500000),1.0)
palancaestacasb.mode=2


######## Funcion: MueveEstacasB()

######## Funcion: AbreEstacasB()

palancaestacasb.OnTurnOnFunc=AbreEstacasB
palancaestacasb.OnTurnOnArgs=()
