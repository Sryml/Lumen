import Doors
import Objects
import Sounds
import Levers
import Scorer
import AuxFuncs
import ReadGSFile
import GameText

res=ReadGSFile.ReadGhostSectorFile("elevador.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])
char=Bladex.GetEntity("Player1")
char.SendTriggerSectorMsgs=1

#char.Position=11326.9777569, 53085.2, -2021.01304202

charInElevator=0


Bladex.SetTriggerSectorFunc("elevador", "OnEnter", charElevatorIn )
Bladex.SetTriggerSectorFunc("elevador", "OnLeave", charElevatorOut )

######################

plataformaelevador2=Bladex.CreateEntity("PlataformaElevador2", "PlataformaRail", 15779.274500,49033.906046,-1744.208425)
plataformaelevador2.Static=0
plataformaelevador2.Scale=1
plataformaelevador2.Orientation=0.707107,0.707107,0.000000,0.000000

plataformaelevador2movil=Objects.CreateDinamicObject("PlataformaElevador2")

loopelevador=Sounds.CreateEntitySound("../../Sounds/drawbridge-loop.wav", "LoopElevador")
golpeelevador=Sounds.CreateEntitySound("../../Sounds/metal-lever3.wav", "GolpeElevador")



columnaelevador2=Doors.CreateDoor("ColumnaElevador2", (15750, 52000, -1750), (0, -1, 0), 0, 5250, Doors.CLOSED)

columnaelevador2.opentype=Doors.AC_UNIF_DEC
columnaelevador2.o_init_vel=0
columnaelevador2.o_init_displ=500
columnaelevador2.o_med_vel=-2000
columnaelevador2.o_med_displ=4250
columnaelevador2.o_end_vel=0
columnaelevador2.o_end_displ=500

columnaelevador2.closetype=Doors.AC_UNIF_DEC
columnaelevador2.c_init_vel=0
columnaelevador2.c_init_displ=500
columnaelevador2.c_med_vel=2000
columnaelevador2.c_med_displ=4250
columnaelevador2.c_end_vel=0
columnaelevador2.c_end_displ=500
columnaelevador2.OnEndCloseFunc = SetScorer


enmarcha=0




columnaelevador2.OnEndOpenFunc=EsperaYSubeElevador2
columnaelevador2.OnEndCloseFunc=Elevador2Arriba


palanca1elevador2=Levers.PlaceLever("Palanca1Elevador2", Levers.LeverType3, (11827.158921,53364.420208,-4873.968236), (0.000000,0.000000,0.707107,-0.707107), 1.0)
palanca1elevador2.mode=1

palanca1elevador2.OnTurnOnFunc=BajaElevador2
palanca1elevador2.OnTurnOnArgs=()
