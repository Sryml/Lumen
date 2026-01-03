import Bladex
import Doors
import Objects
import Levers
import Locks
import Sounds
import Sparks
import darfuncs
import Stars




##########################################
#   Puertas de las torres perimetrales   #
##########################################


### Puerta inferior ROTA torre este-norte

o=Bladex.CreateEntity("PuertaInfTorreEN","puertapeque1",53289.871570,48.021142,14154.610247)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Solid=0

palpuitoen=Levers.PlaceLever("PalPuitoen",Levers.LeverType3,(53039.079000,500.000000,11414.938000),(0.270598,0.270598,-0.653282,0.653282),1.0)

palpuitoen.mode=0


### Puerta superior torre este-norte

deslizpustoen=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizPustoen")
golpepustoen=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe2.wav", "GolpePustoen")

pustoen=Doors.CreateDoor("Pustoen", (57750, -8000, 9375), (1,0,0), 0, 2000, Doors.CLOSED)
pustoen.Squezze=1

pustoen.opentype=Doors.AC_UNIF
pustoen.o_init_vel=0
pustoen.o_init_displ=250
pustoen.o_med_vel=-1000
pustoen.o_med_displ=1750

pustoen.closetype=Doors.AC_UNIF
pustoen.c_init_vel=0
pustoen.c_init_displ=250
pustoen.c_med_vel=1000
pustoen.c_med_displ=1750

pustoen.SetWhileOpenSound(deslizpustoen)
pustoen.SetEndOpenSound(golpepustoen)

pustoen.SetWhileCloseSound(deslizpustoen)
pustoen.SetEndCloseSound(golpepustoen)

palpustoen=Levers.PlaceLever("PalPustoen",Levers.LeverType3,(56150.486000,-7250.000000,10019.453000),(0.000000,0.000000,0.707107,-0.707107),1.0)

palpustoen.mode=0

######## Funcion: AbrePuertaSupTorreEN()

palpustoen.OnTurnOnFunc=AbrePuertaSupTorreEN
palpustoen.OnTurnOnArgs=()

palpustoen.OnTurnOffFunc=pustoen.CloseDoor
palpustoen.OnTurnOffArgs=()


### Puerta superior ROTA torre este-sur

o=Bladex.CreateEntity("PuertaSupTorreES","puertapeque3", 57110.849386, -7607.166057, -11979.152451)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Solid=0

palpustoes=Levers.PlaceLever("PalPustoes",Levers.LeverType3,(59366.613000,-7250.000000,-10019.810000),(0.707107,0.707107,0.000000,0.000000),1.0)

palpustoes.mode=0


### Puerta inferior torre este-sur

deslizpuitoes=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizPuitoes")
golpepuitoes=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe2.wav", "GolpePuitoes")

puitoes=Doors.CreateDoor("Puitoes", (51375, 0, -12375), (-1,0,-1), 0, 2121.320, Doors.CLOSED)
puitoes.Squezze=1

puitoes.opentype=Doors.AC_UNIF
puitoes.o_init_vel=0
puitoes.o_init_displ=250
puitoes.o_med_vel=-1000
puitoes.o_med_displ=1871.32

puitoes.closetype=Doors.AC_UNIF
puitoes.c_init_vel=0
puitoes.c_init_displ=250
puitoes.c_med_vel=1000
puitoes.c_med_displ=1871.32

puitoes.SetWhileOpenSound(deslizpuitoes)
puitoes.SetEndOpenSound(golpepuitoes)

puitoes.SetWhileCloseSound(deslizpuitoes)
puitoes.SetEndCloseSound(golpepuitoes)

palpuitoes=Levers.PlaceLever("PalPuitoes",Levers.LeverType3,(53039.725000,500.000000,-11414.736000),(0.653282,0.653282,-0.270598,0.270598),1.0)

palpuitoes.mode=0

palpuitoes.OnTurnOnFunc=puitoes.OpenDoor
palpuitoes.OnTurnOnArgs=()

palpuitoes.OnTurnOffFunc=puitoes.CloseDoor
palpuitoes.OnTurnOffArgs=()


### Puerta inferior ROTA torre oeste-sur

o=Bladex.CreateEntity("PuertaInfTorreOS","puertapeque2",-53469.400685,11.888771,-13876.593838)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Solid=0

palpuitoos=Levers.PlaceLever("PalPuitoos",Levers.LeverType3,(-53057.903000,500.000000,-11400.373000),(0.653282,0.653282,0.270598,-0.270598),1.0)

palpuitoos.mode=0


### Puerta superior torre oeste-sur

deslizpustoos=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizPustoos")
golpepustoos=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe2.wav", "GolpePustoos")

pustoos=Doors.CreateDoor("Pustoos", (-57750, -8000, -9375), (-1,0,0), 0, 2000, Doors.CLOSED)
pustoos.Squezze=1

pustoos.opentype=Doors.AC_UNIF
pustoos.o_init_vel=0
pustoos.o_init_displ=250
pustoos.o_med_vel=-1000
pustoos.o_med_displ=1750

pustoos.closetype=Doors.AC_UNIF
pustoos.c_init_vel=0
pustoos.c_init_displ=250
pustoos.c_med_vel=1000
pustoos.c_med_displ=1750

pustoos.SetWhileOpenSound(deslizpustoos)
pustoos.SetEndOpenSound(golpepustoos)

pustoos.SetWhileCloseSound(deslizpustoos)
pustoos.SetEndCloseSound(golpepustoos)

palpustoos=Levers.PlaceLever("PalPustoos",Levers.LeverType3,(-56133.426000,-7250.000000,-10017.178000),(0.707107,0.707107,0.000000,0.000000),1.0)

palpustoos.mode=0

palpustoos.OnTurnOnFunc=pustoos.OpenDoor
palpustoos.OnTurnOnArgs=()

palpustoos.OnTurnOffFunc=pustoos.CloseDoor
palpustoos.OnTurnOffArgs=()


### Puerta superior ROTA torre oeste-norte

o=Bladex.CreateEntity("PuertaSupTorreON","puertapeque4", -57986.069731, -7599.837764, 12473.36055)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Solid=0

palpustoon=Levers.PlaceLever("PalPustoon",Levers.LeverType3,(-59369.350000,-7250.000000,10024.769000),(0.000000,0.000000,0.707107,-0.707107),1.0)

palpustoon.mode=0


### Puerta inferior torre oeste-norte

deslizpuitoon=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizPuitoon")
golpepuitoon=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe2.wav", "GolpePuitoon")

puitoon=Doors.CreateDoor("Puitoon", (-51375, 0, 12375), (1,0,1), 0, 2121.320, Doors.CLOSED)
puitoon.Squezze=1

puitoon.opentype=Doors.AC_UNIF
puitoon.o_init_vel=0
puitoon.o_init_displ=250
puitoon.o_med_vel=-1000
puitoon.o_med_displ=1871.32

puitoon.closetype=Doors.AC_UNIF
puitoon.c_init_vel=0
puitoon.c_init_displ=250
puitoon.c_med_vel=1000
puitoon.c_med_displ=1871.32

puitoon.SetWhileOpenSound(deslizpuitoon)
puitoon.SetEndOpenSound(golpepuitoon)

puitoon.SetWhileCloseSound(deslizpuitoon)
puitoon.SetEndCloseSound(golpepuitoon)

palpuitoon=Levers.PlaceLever("PalPuitoon",Levers.LeverType3,(-53048.358000,500.000000,11407.381000),(0.270598,0.270598,0.653282,-0.653282),1.0)

palpuitoon.mode=0

palpuitoon.OnTurnOnFunc=puitoon.OpenDoor
palpuitoon.OnTurnOnArgs=()

palpuitoon.OnTurnOffFunc=puitoon.CloseDoor
palpuitoon.OnTurnOffArgs=()



########################################
#    Rastrillos del anillo exterior    #
########################################


### Rastrillo oeste

rasanexo=Bladex.CreateEntity("Rasanexo","Rastrillo",-42750.000000,-650.000000,0.000000,"Physic")
rasanexo.Scale=0.905287
rasanexo.Orientation=0.707107,0.707107,0.000000,0.000000
rasanexo=Sparks.SetMetalSparkling("Rasanexo")
rasanexo.Frozen=1

rasanexodin=Objects.CreateDinamicObject("Rasanexo")

deslizrasanexo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "DeslizRasanexo")
deslizrasanexo.Volume=0.8
deslizrasanexo.MinDistance=5000
deslizrasanexo.MaxDistance=20000

golperasanexo=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeRasanexo")
golperasanexo.Volume=0.8
golperasanexo.MinDistance=5000
golperasanexo.MaxDistance=20000

######## Funcion: AbreRasanexo()

######## Funcion: CierraRasanexo()

palrasanexo=Levers.PlaceLever("PalRasanexo",Levers.LeverType3,(-38398.588000,750.000000,-3077.173000),(0.504344,0.504344,0.495618,-0.495618),1.0)

palrasanexo.mode=0

palrasanexo.OnTurnOnFunc=AbreRasanexo
palrasanexo.OnTurnOnArgs=()

palrasanexo.OnTurnOffFunc=CierraRasanexo
palrasanexo.OnTurnOffArgs=()


### Rastrillo este

rasanexe=Bladex.CreateEntity("Rasanexe","Rastrillo",42750.000000,-650.000000,0.000000,"Physic")
rasanexe.Scale=0.905287
rasanexe.Orientation=0.707107,0.707107,0.000000,0.000000
rasanexe=Sparks.SetMetalSparkling("Rasanexe")
rasanexe.Frozen=1

rasanexedin=Objects.CreateDinamicObject("Rasanexe")

deslizrasanexe=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "DeslizRasanexe")
deslizrasanexe.Volume=0.8
deslizrasanexe.MinDistance=5000
deslizrasanexe.MaxDistance=20000

golperasanexe=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeRasanexe")
golperasanexe.Volume=0.8
golperasanexe.MinDistance=5000
golperasanexe.MaxDistance=20000

######## Funcion: AbreRasanexe()

######## Funcion: CierraRasanexe()

palrasanexe=Levers.PlaceLever("PalRasanexe",Levers.LeverType3,(38397.539000,750.000000,-3066.075000),(0.495618,0.495618,-0.504344,0.504344),1.0)

palrasanexe.mode=0

palrasanexe.OnTurnOnFunc=AbreRasanexe
palrasanexe.OnTurnOnArgs=()

palrasanexe.OnTurnOffFunc=CierraRasanexe
palrasanexe.OnTurnOffArgs=()



########################################
#    Rastrillos del anillo interior    #
########################################


### Rastrillo oeste

rasanino=Bladex.CreateEntity("Rasanino","Rastrillo",-21375.000000,-2875.000000,21375.000000,"Physic")
rasanino.Scale=1.000000
rasanino.Orientation=0.653282,0.653282,0.270598,-0.270598
rasanino=Sparks.SetMetalSparkling("Rasanino")
rasanino.Frozen=1

rasaninodin=Objects.CreateDinamicObject("Rasanino")

deslizrasanino=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "DeslizRasanino")
deslizrasanino.Volume=0.8
deslizrasanino.MinDistance=5000
deslizrasanino.MaxDistance=20000

golperasanino=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeRasanino")
golperasanino.Volume=0.8
golperasanino.MinDistance=5000
golperasanino.MaxDistance=20000

######## Funcion: AbreRasanino()

######## Funcion: CierraRasanino()

palrasanino=Levers.PlaceLever("PalRasanino",Levers.LeverType3,(-18145.000000,-1250.000000,19605.000000),(0.270598,0.270598,-0.653282,0.653282),1.0)

palrasanino.mode=0

palrasanino.OnTurnOnFunc=AbreRasanino
palrasanino.OnTurnOnArgs=()

palrasanino.OnTurnOffFunc=CierraRasanino
palrasanino.OnTurnOffArgs=()


### Rastrillo este

rasanine=Bladex.CreateEntity("Rasanine","Rastrillo",21375.000000,-2875.000000,21375.000000,"Physic")
rasanine.Scale=1.000000
rasanine.Orientation=0.653282,0.653282,-0.270598,0.270598
rasanine=Sparks.SetMetalSparkling("Rasanine")
rasanine.Frozen=1

rasaninedin=Objects.CreateDinamicObject("Rasanine")

deslizrasanine=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "DeslizRasanine")
deslizrasanine.Volume=0.8
deslizrasanine.MinDistance=5000
deslizrasanine.MaxDistance=20000

golperasanine=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeRasanine")
golperasanine.Volume=0.8
golperasanine.MinDistance=5000
golperasanine.MaxDistance=20000

######## Funcion: AbreRasanine()

######## Funcion: CierraRasanine()

palrasanine=Levers.PlaceLever("PalRasanine",Levers.LeverType3,(18145.000000,-1250.000000,19605.000000),(0.270598,0.270598,0.653282,-0.653282),1.0)

palrasanine.mode=0

palrasanine.OnTurnOnFunc=AbreRasanine
palrasanine.OnTurnOnArgs=()

palrasanine.OnTurnOffFunc=CierraRasanine
palrasanine.OnTurnOffArgs=()

palrasanine.TurnOn()


##############################################
#    Puertas de acceso al anillo interior    #
##############################################


### Puerta este

deslizpuaine=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizPuaine")
golpepuaine=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe2.wav", "GolpePuaine")

puaine=Doors.CreateDoor("Puaine", (36500, -8000, 0), (0,0,-1), 0, 3000, Doors.CLOSED)
puaine.Squezze=1

puaine.opentype=Doors.AC_UNIF
puaine.o_init_vel=0
puaine.o_init_displ=250
puaine.o_med_vel=-1000
puaine.o_med_displ=2750

puaine.closetype=Doors.AC_UNIF
puaine.c_init_vel=0
puaine.c_init_displ=250
puaine.c_med_vel=1000
puaine.c_med_displ=2750

puaine.SetWhileOpenSound(deslizpuaine)
puaine.SetEndOpenSound(golpepuaine)

puaine.SetWhileCloseSound(deslizpuaine)
puaine.SetEndCloseSound(golpepuaine)

palpuaine=Levers.PlaceLever("PalPuaine",Levers.LeverType3,(34605.285000,-7500.000000,-3243.591000),(0.500000,0.500000,0.500000,-0.500000),1.0)

palpuaine.mode=0

palpuaine.OnTurnOnFunc=puaine.OpenDoor
palpuaine.OnTurnOnArgs=()

palpuaine.OnTurnOffFunc=puaine.CloseDoor
palpuaine.OnTurnOffArgs=()


### Puerta ROTA oeste

o=Bladex.CreateEntity("PuertaAnIntO","puertamed", -34423.161150, -7927.328868, 26.447982)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Solid=0

palpuaino=Levers.PlaceLever("PalPuaino",Levers.LeverType3,(-34606.201000,-7500.000000,-3069.064000),(0.500000,0.500000,-0.500000,0.500000),1.0)

palpuaino.mode=0



#########################################
#    Puerta ROTA de la torre central    #
#########################################


o=Bladex.CreateEntity("PuertaTorreCen","puertagran", 304.162701, -2858.710629, 21782.357871)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
#o.Solid=0



########################################
#    Rastrillos de la torre central    #
########################################


### Rastrillo exterior este

rasextocene=Bladex.CreateEntity("Rasextocene","Rastrillo2",10900.000000,-10000.000000,13150.000000,"Physic")
rasextocene.Scale=0.905287
rasextocene.Orientation=0.653282,0.653282,-0.270598,0.270598
rasextocene=Sparks.SetMetalSparkling("Rasextocene")
rasextocene.Frozen=1

rasextocenedin=Objects.CreateDinamicObject("Rasextocene")

deslizrasextocene=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "DeslizRasextocene")
deslizrasextocene.Volume=0.8
deslizrasextocene.MinDistance=5000
deslizrasextocene.MaxDistance=20000

golperasextocene=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeRasextocene")
golperasextocene.Volume=0.8
golperasextocene.MinDistance=5000
golperasextocene.MaxDistance=20000

######## Funcion: AbreRasextocene()

######## Funcion: CierraRasextocene()

palrasextocene=Levers.PlaceLever("PalRasextocene",Levers.LeverType3,(3774.238000,-12250.000000,17942.009000),(0.270598,0.270598,-0.653282,0.653282),1.0)

palrasextocene.mode=0

palrasextocene.OnTurnOnFunc=AbreRasextocene
palrasextocene.OnTurnOnArgs=()

palrasextocene.OnTurnOffFunc=CierraRasextocene
palrasextocene.OnTurnOffArgs=()


### Rastrillo exterior oeste

rasextoceno=Bladex.CreateEntity("Rasextoceno","Rastrillo2",-10900.000000,-10000.000000,13150.000000,"Physic")
rasextoceno.Scale=0.905287
rasextoceno.Orientation=0.653282,0.653282,0.270598,-0.270598
rasextoceno=Sparks.SetMetalSparkling("Rasextoceno")
rasextoceno.Frozen=1

rasextocenodin=Objects.CreateDinamicObject("Rasextoceno")

deslizrasextoceno=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "DeslizRasextoceno")
deslizrasextoceno.Volume=0.8
deslizrasextoceno.MinDistance=5000
deslizrasextoceno.MaxDistance=20000

golperasextoceno=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeRasextoceno")
golperasextoceno.Volume=0.8
golperasextoceno.MinDistance=5000
golperasextoceno.MaxDistance=20000

######## Funcion: AbreRasextoceno()

######## Funcion: CierraRasextoceno()

palrasextoceno=Levers.PlaceLever("PalRasextoceno",Levers.LeverType3,(-3746.210000,-12250.000000,17956.732000),(0.270598,0.270598,0.653282,-0.653282),1.0)

palrasextoceno.mode=0

palrasextoceno.OnTurnOnFunc=AbreRasextoceno
palrasextoceno.OnTurnOnArgs=()

palrasextoceno.OnTurnOffFunc=CierraRasextoceno
palrasextoceno.OnTurnOffArgs=()


### Rastrillo interior este

rasintocene=Bladex.CreateEntity("Rasintocene","Rastrillo2",20290.000000,-10040.000000,-4010.000000,"Physic")
rasintocene.Scale=0.905287
rasintocene.Orientation=0.653282,0.653282,0.270598,-0.270598
rasintocene=Sparks.SetMetalSparkling("Rasintocene")
rasintocene.Frozen=1

rasintocenedin=Objects.CreateDinamicObject("Rasintocene")

deslizrasintocene=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "DeslizRasintocene")
deslizrasintocene.Volume=0.8
deslizrasintocene.MinDistance=5000
deslizrasintocene.MaxDistance=20000

golperasintocene=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeRasintocene")
golperasintocene.Volume=0.8
golperasintocene.MinDistance=5000
golperasintocene.MaxDistance=20000

######## Funcion: AbreRasintocene()

######## Funcion: CierraRasintocene()

palrasintocene=Levers.PlaceLever("PalRasintocene",Levers.LeverType3,(17374.469, -9910.0, -7351.462),(0.0, 0.0, -0.707106769085, 0.707106769085),1.0)

palrasintocene.mode=0

palrasintocene.OnTurnOnFunc=AbreRasintocene
palrasintocene.OnTurnOnArgs=()

palrasintocene.OnTurnOffFunc=CierraRasintocene
palrasintocene.OnTurnOffArgs=()


### Rastrillo interior oeste

rasintoceno=Bladex.CreateEntity("Rasintoceno","Rastrillo2",-20280.000000,-10050.000000,-4020.000000,"Physic")
rasintoceno.Scale=0.905287
rasintoceno.Orientation=0.653282,0.653282,-0.270598,0.270598
rasintoceno=Sparks.SetMetalSparkling("Rasintoceno")
rasintoceno.Frozen=1

rasintocenodin=Objects.CreateDinamicObject("Rasintoceno")

deslizrasintoceno=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "DeslizRasintoceno")
deslizrasintoceno.Volume=0.8
deslizrasintoceno.MinDistance=5000
deslizrasintoceno.MaxDistance=20000

golperasintoceno=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeRasintoceno")
golperasintoceno.Volume=0.8
golperasintoceno.MinDistance=5000
golperasintoceno.MaxDistance=20000

######## Funcion: AbreRasintoceno()

######## Funcion: CierraRasintoceno()

palrasintoceno=Levers.PlaceLever("PalRasintoceno",Levers.LeverType3,(-17374.469, -9910.0, -7351.462),(0.0, 0.0, 0.707106769085, -0.707106769085),1.0)

palrasintoceno.mode=0

palrasintoceno.OnTurnOnFunc=AbreRasintoceno
palrasintoceno.OnTurnOnArgs=()

palrasintoceno.OnTurnOffFunc=CierraRasintoceno
palrasintoceno.OnTurnOffArgs=()


##################################################
#    Puertas pasaje habitacion-sala del trono    #
##################################################


### Puerta secreta habitacion

deslizpusehab=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizPusehab")
golpepusehab=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe2.wav", "GolpePusehab")

pusehab=Doors.CreateDoor("Pusehab", (7875, -28000, -7875), (0,0,-1), 0, 2000, Doors.CLOSED)
pusehab.Squezze=1

pusehab.opentype=Doors.AC_UNIF
pusehab.o_init_vel=0
pusehab.o_init_displ=250
pusehab.o_med_vel=-1000
pusehab.o_med_displ=1750

pusehab.closetype=Doors.AC_UNIF
pusehab.c_init_vel=0
pusehab.c_init_displ=250
pusehab.c_med_vel=1000
pusehab.c_med_displ=1750

pusehab.SetWhileOpenSound(deslizpusehab)
pusehab.SetEndOpenSound(golpepusehab)

pusehab.SetWhileCloseSound(deslizpusehab)
pusehab.SetEndCloseSound(golpepusehab)

palpusehab=Levers.PlaceLever("PalPusehab",Levers.LeverType3,(7125.383000,-27500.000000,-6652.370000),(0.707107,0.707107,0.000000,0.000000),1.0)

palpusehab.mode=0

palpusehab.OnTurnOnFunc=pusehab.OpenDoor
palpusehab.OnTurnOnArgs=()

palpusehab.OnTurnOffFunc=pusehab.CloseDoor
palpusehab.OnTurnOffArgs=()


### Puerta secreta superior sala del trono

deslizpusesuptro=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizPusesuptro")
golpepusesuptro=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe2.wav", "GolpePusesuptro")

pusesuptro=Doors.CreateDoor("Pusesuptro", (10250, -8000, -12375), (0,0,1), 0, 2250, Doors.CLOSED)
pusesuptro.Squezze=1

pusesuptro.opentype=Doors.AC_UNIF
pusesuptro.o_init_vel=0
pusesuptro.o_init_displ=250
pusesuptro.o_med_vel=-1000
pusesuptro.o_med_displ=2000

pusesuptro.closetype=Doors.AC_UNIF
pusesuptro.c_init_vel=0
pusesuptro.c_init_displ=250
pusesuptro.c_med_vel=1000
pusesuptro.c_med_displ=2000

pusesuptro.SetWhileOpenSound(deslizpusesuptro)
pusesuptro.SetEndOpenSound(golpepusesuptro)

pusesuptro.SetWhileCloseSound(deslizpusesuptro)
pusesuptro.SetEndCloseSound(golpepusesuptro)

palpusesuptro=Levers.PlaceLever("PalPusesuptro",Levers.LeverType3,(12257.600000,-7250.000000,-13606.080000),(0.000000,0.000000,0.707107,-0.707107),1.0)

palpusesuptro.mode=0

palpusesuptro.OnTurnOnFunc=pusesuptro.OpenDoor
palpusesuptro.OnTurnOnArgs=()

palpusesuptro.OnTurnOffFunc=pusesuptro.CloseDoor
palpusesuptro.OnTurnOffArgs=()



################################################
#    Puertas pasaje sala del trono-estanque    #
################################################


### Puerta secreta inferior sala del trono

deslizpuseinftro=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizPuseinftro")
golpepuseinftro=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe2.wav", "GolpePuseinftro")

puseinftro=Doors.CreateDoor("Puseinftro", (8250, -3000, -15375), (-1,0,0), 0, 2000, Doors.CLOSED)
puseinftro.Squezze=1

puseinftro.opentype=Doors.AC_UNIF
puseinftro.o_init_vel=0
puseinftro.o_init_displ=250
puseinftro.o_med_vel=-1000
puseinftro.o_med_displ=1750

puseinftro.closetype=Doors.AC_UNIF
puseinftro.c_init_vel=0
puseinftro.c_init_displ=250
puseinftro.c_med_vel=1000
puseinftro.c_med_displ=1750

puseinftro.SetWhileOpenSound(deslizpuseinftro)
puseinftro.SetEndOpenSound(golpepuseinftro)

puseinftro.SetWhileCloseSound(deslizpuseinftro)
puseinftro.SetEndCloseSound(golpepuseinftro)

llavepuertaesc=Bladex.CreateEntity("LlavePuertaEsc","Llavecutre",0,-2000,-15000,"Physic")
llavepuertaesc.Scale=1.4
llavepuertaesc.Orientation=0.707107,0.707107,0.000000,0.000000
llavepuertaesc.RemoveFromWorld()

cerradurapuertaesc=Locks.PlaceLock("CerraduraPuertaEsc","Cerraduracutre",(6518.932000,-2500.000000,-13315.816000),(0.707107,0.707107,0.000000,0.000000),2.0)
cerradurapuertaesc.key="LlavePuertaEsc"

cerradurapuertaesc.OnUnLockFunc=puseinftro.OpenDoor
cerradurapuertaesc.OnUnLockArgs=()

cerradurapuertaesc.OnLockFunc=puseinftro.CloseDoor
cerradurapuertaesc.OnLockArgs=()


### Puerta secreta estanque

deslizpuseest=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizPuseest")
golpepuseest=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe2.wav", "GolpePuseest")

puseest=Doors.CreateDoor("Puseest", (0, 3000, -61750), (0,-1,0), 200, 3450, Doors.CLOSED)
puseest.Squezze=1

puseest.opentype=Doors.AC_UNIF
puseest.o_init_vel=0
puseest.o_init_displ=250
puseest.o_med_vel=-1000
puseest.o_med_displ=3000

puseest.closetype=Doors.AC_UNIF
puseest.c_init_vel=0
puseest.c_init_displ=250
puseest.c_med_vel=1000
puseest.c_med_displ=3000

puseest.SetWhileOpenSound(deslizpuseest)
#puseest.SetEndOpenSound(golpepuseest)

puseest.SetWhileCloseSound(deslizpuseest)
#puseest.SetEndCloseSound(golpepuseest)


### Rastrillo alcantarilla

rasalc=Bladex.CreateEntity("Rasalc","Rastrillo",0.0,3735.147682,-36745.144377,"Physic")
rasalc.Scale=0.772048
rasalc.Orientation=0.707107,0.707107,0.000000,0.000000
rasalc=Sparks.SetMetalSparkling("Rasalc")
rasalc.Frozen=1

rasalcdin=Objects.CreateDinamicObject("Rasalc")

deslizrasalc=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "DeslizRasalc")
deslizrasalc.Volume=0.8
deslizrasalc.MinDistance=5000
deslizrasalc.MaxDistance=20000

golperasalc=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeRasalc")
golperasalc.Volume=0.8
golperasalc.MinDistance=5000
golperasalc.MaxDistance=20000

######## Funcion: AbreRasalc()

######## Funcion: CierraRasalc()


### Palanca que abre las dos puertas anteriores

palesc=Levers.PlaceLever("PalEsc",Levers.LeverType3,(-2098.782000,4500.000000,-34002.989000),(0.500000,0.500000,-0.500000,0.500000),1.0)

palesc.mode=0

######## Funcion: ReiniciaCamaraEstanque()

######## Funcion: CamaraEstanque()

######## Funcion: AbreViaEscape()

######## Funcion: CierraViaEscape()

palesc.OnTurnOnFunc=AbreViaEscape
palesc.OnTurnOnArgs=()

palesc.OnTurnOffFunc=CierraViaEscape
palesc.OnTurnOffArgs=()



#####################################
#    Puerta habitacion del duque    #
#####################################


deslizpuhadu=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizPuhadu")
golpepuhadu=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe2.wav", "GolpePuhadu")

puhadu=Doors.CreateDoor("Puhadu", (0, -28000, -5625), (1,0,0), 0, 2500, Doors.CLOSED)
puhadu.Squezze=1

puhadu.opentype=Doors.AC_UNIF
puhadu.o_init_vel=0
puhadu.o_init_displ=250
puhadu.o_med_vel=-1000
puhadu.o_med_displ=2250

puhadu.closetype=Doors.AC_UNIF
puhadu.c_init_vel=0
puhadu.c_init_displ=250
puhadu.c_med_vel=1000
puhadu.c_med_displ=2250

puhadu.SetWhileOpenSound(deslizpuhadu)
puhadu.SetEndOpenSound(golpepuhadu)

puhadu.SetWhileCloseSound(deslizpuhadu)
puhadu.SetEndCloseSound(golpepuhadu)

llavepuhadu=Bladex.CreateEntity("LlavePuhadu","Llavedor",-742.189118,-11032.723702,20253.750242,"Physic")
llavepuhadu.Scale=1.416603
llavepuhadu.Orientation=0.005434,-0.811375,0.005442,0.584475
darfuncs.SetHint(llavepuhadu,"Duke's Bedroom Key")
Stars.Twinkle("LlavePuhadu")

cerradurapuhadu=Locks.PlaceLock("CerraduraPuhadu","Cerradurdor",(-1500.000000,-27100.000000,-4730.000000),(0.500000,0.500000,-0.500000,0.500000),1.728525)
cerradurapuhadu.key="LlavePuhadu"
darfuncs.SetHint(cerradurapuhadu.obj,"Duke's Bedroom Lock")

habitacionduquevista=0

### Funcion: AbrePuertaHabitacionDuque()

cerradurapuhadu.OnUnLockFunc=AbrePuertaHabitacionDuque
cerradurapuhadu.OnUnLockArgs=()

cerradurapuhadu.OnLockFunc=puhadu.CloseDoor
cerradurapuhadu.OnLockArgs=()
