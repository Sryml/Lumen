import Doors
import Objects
import Sounds
import Levers

plataformaelevador3=Bladex.CreateEntity("PlataformaElevador3", "PlataformaRail", -25451.254426,11096.729652,64712.498501)
plataformaelevador3.Static=0
plataformaelevador3.Scale=1.172579
plataformaelevador3.Orientation=0.707107,0.707107,0.000000,0.000000

plataformaelevador3movil=Objects.CreateDinamicObject("PlataformaElevador3")

loopelevador=Sounds.CreateEntitySound("../../Sounds/drawbridge-loop.wav", "LoopElevador")
golpeelevador=Sounds.CreateEntitySound("../../Sounds/metal-lever3.wav", "GolpeElevador")


columnaelevador3=Doors.CreateDoor("ColumnaElevador", (-25250, 6000, 64750), (0, -1, 0), 0, 9600, Doors.OPENED)

columnaelevador3.opentype=Doors.AC_UNIF_DEC
columnaelevador3.o_init_vel=0
columnaelevador3.o_init_displ=500
columnaelevador3.o_med_vel=-2000
columnaelevador3.o_med_displ=8600
columnaelevador3.o_end_vel=0
columnaelevador3.o_end_displ=500

columnaelevador3.closetype=Doors.AC_UNIF_DEC
columnaelevador3.c_init_vel=0
columnaelevador3.c_init_displ=500
columnaelevador3.c_med_vel=2000
columnaelevador3.c_med_displ=8600
columnaelevador3.c_end_vel=0
columnaelevador3.c_end_displ=500



enmarcha=0


palanca1elevador3=Levers.PlaceLever("Palanca1Elevador3", Levers.LeverType3, (-22903.882923,10116.045268,64733.018136), (0.500000,0.500000,0.500000,-0.500000), 1.0)

palanca1elevador3.mode=1

palanca1elevador3.OnTurnOnFunc=SubeElevador3
palanca1elevador3.OnTurnOnArgs=()