import Bladex
import Doors
import Levers
import Locks
import Objects
import Sounds



######################

plataformaelevador2=Bladex.CreateEntity("PlataformaElevador2", "PlataformaRail", -50476.057000,-41321.818000,20173.998000)
plataformaelevador2.Static=0
plataformaelevador2.Scale=1.115668
plataformaelevador2.Orientation=0.707107,0.707107,0.000000,0.000000

plataformaelevador2movil=Objects.CreateDinamicObject("PlataformaElevador2")

loopelevador=Sounds.CreateEntitySound("../../Sounds/drawbridge-loop.wav", "LoopElevador")
golpeelevador=Sounds.CreateEntitySound("../../Sounds/metal-lever3.wav", "GolpeElevador")


columnaelevador2=Doors.CreateDoor("ColumnaElevador2", (-46500, -42000, 17000), (0, -1, 0), 0, 7250, Doors.CLOSED)

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


palanca1elevador2=Levers.PlaceLever("Palanca1Elevador2", Levers.LeverType3, (-47326.221669,-42528.108610,18215.632411), (0.0,0.0,0.707107,-0.707107), 1.0)
palanca1elevador2.mode=1

palanca1elevador2.OnTurnOnFunc=BajaElevador2
palanca1elevador2.OnTurnOnArgs=()


palanca2elevador2=Levers.PlaceLever("Palanca2Elevador2", Levers.LeverType3, (-47304.282807,-37760.310339,18208.929470), (0.0,0.0,0.707107,-0.707107), 1.0)
palanca2elevador2.mode=1

palanca2elevador2.OnTurnOnFunc=BajaElevador2
palanca2elevador2.OnTurnOnArgs=()
