import Bladex
import Doors
import Objects
import Sounds
import Levers



### Elevador duke nukem

plataformaelevador=Bladex.CreateEntity("PlataformaElevador", "Plataforma", 11838.693000,-26150.000000,-7874.940000,"Physic")
plataformaelevador.Scale=2.473119
plataformaelevador.Orientation=0.707107,0.707107,0.000000,0.000000
plataformaelevador.Frozen=1

plataformaelevadormovil=Objects.CreateDinamicObject("PlataformaElevador")

loopelevador=Sounds.CreateEntitySound("../../Sounds/drawbridge-loop.wav", "LoopElevador")
golpeelevador=Sounds.CreateEntitySound("../../Sounds/metal-lever3.wav", "GolpeElevador")


columnaelevador=Doors.CreateDoor("ColumnaElevador", (12000, -25000, -8000), (0, -1, 0), 500, 20500, Doors.CLOSED)

columnaelevador.opentype=Doors.AC_UNIF_DEC
columnaelevador.o_init_vel=0
columnaelevador.o_init_displ=2000
columnaelevador.o_med_vel=-2000
columnaelevador.o_med_displ=16000
columnaelevador.o_end_vel=0
columnaelevador.o_end_displ=2000

columnaelevador.closetype=Doors.AC_UNIF_DEC
columnaelevador.c_init_vel=0
columnaelevador.c_init_displ=2000
columnaelevador.c_med_vel=2000
columnaelevador.c_med_displ=16000
columnaelevador.c_end_vel=0
columnaelevador.c_end_displ=2000


######## Funcion: SubeElevador()

######## Funcion: BajaElevador()




palancaelevador=Levers.PlaceLever("PalancaElevador", Levers.LeverType3, (13477.348000,-27250.000000,-7835.533000), (0.500000,0.500000,0.500000,-0.500000), 1.0)
palancaelevador.mode=1

palancaelevador.OnTurnOnFunc=AccionaElevadorArriba
palancaelevador.OnTurnOnArgs=()


palanca2elevador=Levers.PlaceLever("Palanca2Elevador", Levers.LeverType3, (11894.265000,-7250.000000,-6271.608000), (0.707107,0.707107,0.000000,0.000000), 1.0)
palanca2elevador.mode=1

palanca2elevador.OnTurnOnFunc=AccionaElevadorAbajo
palanca2elevador.OnTurnOnArgs=()



########
#######
#####
####



plataformaelevador2=Bladex.CreateEntity("PlataformaElevador2", "Plataforma", 8255.0,-1090.0,-16689.0,"Physic")
plataformaelevador2.Scale=1.86 # 1.763268
plataformaelevador2.Orientation=0.707107,0.707107,0.000000,0.000000
plataformaelevador2.Frozen=1

plataformaelevador2movil=Objects.CreateDinamicObject("PlataformaElevador2")

loopelevador2=Sounds.CreateEntitySound("../../Sounds/drawbridge-loop.wav", "LoopElevador2")
golpeelevador2=Sounds.CreateEntitySound("../../Sounds/metal-lever3.wav", "GolpeElevador2")


columnaelevador2=Doors.CreateDoor("ColumnaElevador2", (8000,0,-17000), (0, -1, 0), 1250, 7000, Doors.CLOSED)



columnaelevador2.opentype=Doors.AC_UNIF_DEC
columnaelevador2.o_init_vel=0
columnaelevador2.o_init_displ=1000
columnaelevador2.o_med_vel=-2000
columnaelevador2.o_med_displ=3750
columnaelevador2.o_end_vel=0
columnaelevador2.o_end_displ=1000

columnaelevador2.closetype=Doors.AC_UNIF_DEC
columnaelevador2.c_init_vel=0
columnaelevador2.c_init_displ=1000
columnaelevador2.c_med_vel=2000
columnaelevador2.c_med_displ=3750
columnaelevador2.c_end_vel=0
columnaelevador2.c_end_displ=1000


######## Funcion: SubeElevador2()

######## Funcion: BajaElevador2()


palancaelevador2=Levers.PlaceLever("PalancaElevador", Levers.LeverType3, (8248.197, 3500.0, -18103.873), (0.000000,0.000000,0.707107,-0.707107), 1.0)
palancaelevador2.mode=1

palancaelevador2.OnTurnOnFunc=AccionaElevador2Abajo
palancaelevador2.OnTurnOnArgs=()






palanca2elevador2=Levers.PlaceLever("Palanca2Elevador", Levers.LeverType3, (9729.849, -2250.0, -16687.019), (0.500000,0.500000,0.500000,-0.500000), 1.0)
palanca2elevador2.mode=1

palanca2elevador2.OnTurnOnFunc=AccionaElevador2Arriba
palanca2elevador2.OnTurnOnArgs=()
