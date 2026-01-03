import Doors
import Objects
import Sounds
import Levers


plataformaelevador=Bladex.CreateEntity("PlataformaElevador", "Plataforma", -122004.455927, -5511.732215, 40902.346632,"Physic")
plataformaelevador.Scale=5.5
plataformaelevador.Orientation=0.707107,0.707107,0.000000,0.000000
plataformaelevador.Frozen=1

plataformaelevadormovil=Objects.CreateDinamicObject("PlataformaElevador")

loopelevador=Sounds.CreateEntitySound("../../Sounds/drawbridge-loop.wav", "LoopElevador")
golpeelevador=Sounds.CreateEntitySound("../../Sounds/metal-lever3.wav", "GolpeElevador")


columnaelevador=Doors.CreateDoor("ColumnaElevador", (-122000, -5200, 40750), (0, -1, 0), 0, 6850, Doors.OPENED)

columnaelevador.opentype=Doors.AC_UNIF_DEC
columnaelevador.o_init_vel=0
columnaelevador.o_init_displ=500
columnaelevador.o_med_vel=-2000
columnaelevador.o_med_displ=5850
columnaelevador.o_end_vel=0
columnaelevador.o_end_displ=500

columnaelevador.closetype=Doors.AC_UNIF_DEC
columnaelevador.c_init_vel=0
columnaelevador.c_init_displ=500
columnaelevador.c_med_vel=2000
columnaelevador.c_med_displ=5850
columnaelevador.c_end_vel=0
columnaelevador.c_end_displ=500



columnaelevador.OnEndCloseFunc=EsperaYBajaElevador

columnaelevador.OnEndOpenFunc=ElevadorArriba

palancaelevador=Levers.PlaceLever("PalancaElevador", Levers.LeverType3, (-118613.991158, -6739.418632, 39250.360666), (0.491198, 0.491198, 0.508650, -0.508650), 1.0)
palancaelevador.mode=1

palancaelevador.OnTurnOnFunc=SubeElevador
palancaelevador.OnTurnOnArgs=()

palanca2elevador=Levers.PlaceLever("Palanca2Elevador", Levers.LeverType3, (-117372.139014,-12865.361372,37346.626051), (0.500000,0.500000,-0.500000,0.500000), 1.0)
palanca2elevador.mode=1

palanca2elevador.OnTurnOnFunc=SubeElevador
palanca2elevador.OnTurnOnArgs=()


######################

plataformaelevador2=Bladex.CreateEntity("PlataformaElevador2", "Plataforma", -123681.339188, 2300.325085, 57285.883093,"Physic")
plataformaelevador2.Scale=3.733391
plataformaelevador2.Orientation=0.707107,0.707107,0.000000,0.000000
plataformaelevador2.Frozen=1

plataformaelevador2movil=Objects.CreateDinamicObject("PlataformaElevador2")

loopelevador=Sounds.CreateEntitySound("../../Sounds/drawbridge-loop.wav", "LoopElevador")
golpeelevador=Sounds.CreateEntitySound("../../Sounds/metal-lever3.wav", "GolpeElevador")


columnaelevador2=Doors.CreateDoor("ColumnaElevador2", (-123500, 6000, 57200), (0, -1, 0), 0, 7250, Doors.CLOSED)

columnaelevador2.opentype=Doors.AC_UNIF_DEC
columnaelevador2.o_init_vel=0
columnaelevador2.o_init_displ=500
columnaelevador2.o_med_vel=-2000
columnaelevador2.o_med_displ=6250
columnaelevador2.o_end_vel=0
columnaelevador2.o_end_displ=500

columnaelevador2.closetype=Doors.AC_UNIF_DEC
columnaelevador2.c_init_vel=0
columnaelevador2.c_init_displ=500
columnaelevador2.c_med_vel=2000
columnaelevador2.c_med_displ=6250
columnaelevador2.c_end_vel=0
columnaelevador2.c_end_displ=500

enmarcha=0



columnaelevador2.OnEndOpenFunc=EsperaYSubeElevador2
columnaelevador2.OnEndCloseFunc=Elevador2Arriba


palanca1elevador2=Levers.PlaceLever("Palanca1Elevador2", Levers.LeverType3, (-121661.640207, 1139.483907, 57538.172715), (0.504344, 0.504344, 0.495618, -0.495618), 1.0)
palanca1elevador2.mode=1

palanca1elevador2.OnTurnOnFunc=BajaElevador2
palanca1elevador2.OnTurnOnArgs=()


palanca2elevador2=Levers.PlaceLever("Palanca2Elevador2", Levers.LeverType3, (-121672.601876, 8669.148758, 54322.933958), (0.504344, 0.504344, 0.495618, -0.495618), 1.0)
palanca2elevador2.mode=1

palanca2elevador2.OnTurnOnFunc=BajaElevador2
palanca2elevador2.OnTurnOnArgs=()
