import Doors
import Objects
import Sounds
import Levers


plataformaelevador2=Bladex.CreateEntity("PlataformaElevador2", "Plataforma", -6693.432363,3883.371850,14346.470783)
plataformaelevador2.Static=0
plataformaelevador2.Scale=2.824389
plataformaelevador2.Orientation=0.707107,0.707107,0.000000,0.000000

plataformaelevador2movil=Objects.CreateDinamicObject("PlataformaElevador2")

loopelevador=Sounds.CreateEntitySound("../../Sounds/drawbridge-loop.wav", "LoopElevador")
golpeelevador=Sounds.CreateEntitySound("../../Sounds/metal-lever3.wav", "GolpeElevador")


columnaelevador2=Doors.CreateDoor("ColumnaElevador2", (-6750, 6000, 14250), (0, -1, 0), 0, 3500, Doors.CLOSED)

columnaelevador2.opentype=Doors.AC_UNIF_DEC
columnaelevador2.o_init_vel=0
columnaelevador2.o_init_displ=500
columnaelevador2.o_med_vel=-2000
columnaelevador2.o_med_displ=2500
columnaelevador2.o_end_vel=0
columnaelevador2.o_end_displ=500

columnaelevador2.closetype=Doors.AC_UNIF_DEC
columnaelevador2.c_init_vel=0
columnaelevador2.c_init_displ=500
columnaelevador2.c_med_vel=2000
columnaelevador2.c_med_displ=2500
columnaelevador2.c_end_vel=0
columnaelevador2.c_end_displ=500

enmarcha=0




columnaelevador2.OnEndOpenFunc=EsperaYSubeElevador2
columnaelevador2.OnEndCloseFunc=Elevador2Arriba


palanca1elevador2=Levers.PlaceLever("Palanca1Elevador2", Levers.LeverType3, (-6665.674031,2980.065753,15785.683435), (0.707107,0.707107,0.000000,0.000000), 1.0)
palanca1elevador2.mode=1

palanca1elevador2.OnTurnOnFunc=BajaElevador2
palanca1elevador2.OnTurnOnArgs=()
