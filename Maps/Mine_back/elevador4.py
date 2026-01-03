import Doors
import Objects
import Sounds
import Levers


plataformaelevador4=Bladex.CreateEntity("PlataformaElevador4", "PlataformaRail", -4465.406832,-18250.118879,-101582.297355)
plataformaelevador4.Static=0
plataformaelevador4.Scale=1.8
plataformaelevador4.Orientation=0.707107,0.707107,0.000000,0.000000

plataformaelevador4movil=Objects.CreateDinamicObject("PlataformaElevador4")

loopelevador=Sounds.CreateEntitySound("../../Sounds/drawbridge-loop.wav", "LoopElevador")
golpeelevador=Sounds.CreateEntitySound("../../Sounds/metal-lever3.wav", "GolpeElevador")


columnaelevador4=Doors.CreateDoor("ColumnaElevador4", (-4500, -14500, -101500), (0, -1, 0), 0, 7000, Doors.CLOSED)

columnaelevador4.opentype=Doors.AC_UNIF_DEC
columnaelevador4.o_init_vel=0
columnaelevador4.o_init_displ=500
columnaelevador4.o_med_vel=-2000
columnaelevador4.o_med_displ=6000
columnaelevador4.o_end_vel=0
columnaelevador4.o_end_displ=500

columnaelevador4.closetype=Doors.AC_UNIF_DEC
columnaelevador4.c_init_vel=0
columnaelevador4.c_init_displ=500
columnaelevador4.c_med_vel=2000
columnaelevador4.c_med_displ=6000
columnaelevador4.c_end_vel=0
columnaelevador4.c_end_displ=500

enmarcha=0




columnaelevador4.OnEndOpenFunc=EsperaYSubeElevador4
columnaelevador4.OnEndCloseFunc=Elevador4Arriba


palanca1elevador4=Levers.PlaceLever("Palanca1Elevador4", Levers.LeverType3, (-1875.152293,-19597.211057,-101381.453645), (0.500000,0.500000,0.500000,-0.500000), 1.0)
palanca1elevador4.mode=1

palanca1elevador4.OnTurnOnFunc=BajaElevador4
palanca1elevador4.OnTurnOnArgs=()


palanca2elevador4=Levers.PlaceLever("Palanca2Elevador4", Levers.LeverType3, (-5865.306705,-12361.965601,-104891.370033), (0.500000,0.500000,-0.500000,0.500000), 1.0)
palanca2elevador4.mode=1

palanca2elevador4.OnTurnOnFunc=BajaElevador4
palanca2elevador4.OnTurnOnArgs=()
