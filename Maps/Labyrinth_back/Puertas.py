import Bladex
import Doors
import Objects
import Levers
import Locks
import Sounds
import Sparks
import darfuncs




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

palpustoen.OnTurnOnFunc=pustoen.OpenDoor
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

palrasanexo.TurnOn()


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

palrasanexe.TurnOn()



#########################################
#    Puerta ROTA de la torre central    #
#########################################


o=Bladex.CreateEntity("PuertaTorreCen","puertagran", 304.162701, -2858.710629, 21782.357871)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Solid=0



########################################
#    Rastrillos de la torre central    #
########################################


### Rastrillo exterior este

rasextocene=Bladex.CreateEntity("Rasextocene","Rastrillo2",10900.000000,-10000.000000,13150.000000,"Physic")
rasextocene.Scale=0.905287
rasextocene.Orientation=0.653282,0.653282,-0.270598,0.270598
rasextocene=Sparks.SetMetalSparkling("Rasextocene")

palrasextocene=Levers.PlaceLever("PalRasextocene",Levers.LeverType3,(3774.238000,-12250.000000,17942.009000),(0.270598,0.270598,-0.653282,0.653282),1.0)

palrasextocene.mode=0


### Rastrillo exterior oeste

rasextoceno=Bladex.CreateEntity("Rasextoceno","Rastrillo2",-10900.000000,-10000.000000,13150.000000,"Physic")
rasextoceno.Scale=0.905287
rasextoceno.Orientation=0.653282,0.653282,0.270598,-0.270598
rasextoceno=Sparks.SetMetalSparkling("Rasextoceno")

palrasextoceno=Levers.PlaceLever("PalRasextoceno",Levers.LeverType3,(-3746.210000,-12250.000000,17956.732000),(0.270598,0.270598,0.653282,-0.653282),1.0)

palrasextoceno.mode=0


### Rastrillo interior este

rasintocene=Bladex.CreateEntity("Rasintocene","Rastrillo2",20290.000000,-10040.000000,-4010.000000,"Physic")
rasintocene.Scale=0.905287
rasintocene.Orientation=0.653282,0.653282,0.270598,-0.270598
rasintocene=Sparks.SetMetalSparkling("Rasintocene")

palrasintocene=Levers.PlaceLever("PalRasintocene",Levers.LeverType3,(17374.469, -9910.0, -7351.462),(0.0, 0.0, -0.707106769085, 0.707106769085),1.0)

palrasintocene.mode=0


### Rastrillo interior oeste

rasintoceno=Bladex.CreateEntity("Rasintoceno","Rastrillo2",-20280.000000,-10050.000000,-4020.000000,"Physic")
rasintoceno.Scale=0.905287
rasintoceno.Orientation=0.653282,0.653282,-0.270598,0.270598
rasintoceno=Sparks.SetMetalSparkling("Rasintoceno")

palrasintoceno=Levers.PlaceLever("PalRasintoceno",Levers.LeverType3,(-17374.469, -9910.0, -7351.462),(0.0, 0.0, 0.707106769085, -0.707106769085),1.0)

palrasintoceno.mode=0



################################################
#    Puertas pasaje sala del trono-estanque    #
################################################


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

palesc=Levers.PlaceLever("PalEsc",Levers.LeverType3,(-2098.782000,4500.000000,-34002.989000),(0.500000,0.500000,-0.500000,0.500000),1.0)

palesc.mode=0

palesc.OnTurnOnFunc=AbreRasalc
palesc.OnTurnOnArgs=()

palesc.OnTurnOffFunc=CierraRasalc
palesc.OnTurnOffArgs=()

palesc.TurnOn()
