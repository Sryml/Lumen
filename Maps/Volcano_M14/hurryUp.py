#########################################################
#														#
# VOLCANO												#
#														#
# lava que sube y hay que escapar en el elevador		#
#														#
# (Yuio)												#
#														#
#########################################################

import Bladex
import Sounds
import Reference
import Select
import Change
import Actions
import Bladex
import AuxFuncs
import ReadGSFile
import LavaDefDamage
import Doors
import Levers

res=ReadGSFile.ReadGhostSectorFile("subelava.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

char=Bladex.GetEntity("Player1")
char.SendTriggerSectorMsgs=1

hpSector=Bladex.GetSector(-36000,-1500,31000)
hpSector.InitBreak((0,500,0),(2140,0,50),(100,0,1274),'piedra pesada')
hpSector.Active=0

hderrumbamiento	=Sounds.CreateEntitySound("../../Sounds/derrumbamiento-roca.wav", "Derrumbamiento")
hderrumbamiento.Volume=0.5
hderrumbamiento.MinDistance=10000
hderrumbamiento.MaxDistance=20000

hlavasubelooper	=Sounds.CreateEntitySound("../../Sounds/M-loop-lavahervidero-1.wav", "LoopLava")
hlavasubelooper.Volume=1.0
hlavasubelooper.MinDistance=10000
hlavasubelooper.MaxDistance=20000

hploopelevador	=Sounds.CreateEntitySound("../../Sounds/ember-crackle.wav", "LoopElevador")
hpgolpeelevador	=Sounds.CreateEntitySound("../../Sounds/metal-lever3.wav", "GolpeElevador")


hpcolumnaelevador=Doors.CreateDoor("hpElevador", (-36250, 1000, 25250), (0, -1, 0), 0, 6650, Doors.OPENED)

hpLavaStart=8953.2
hpLavaStop=-1100
hpLavaFloodTime=30.0
hpLavaPosition=-55175.9094803, 25799.462466
hpLavaDM=LavaDefDamage.LAVA_AREA()
hpLavaDM.CreateLava("hpLava",hpLavaPosition[0], hpLavaStart, hpLavaPosition[1],"cala2",0.02)
#hpLava=Bladex.CreateEntity("hpLava","Entity Water", hpLavaPosition[0], hpLavaStart, hpLavaPosition[1] )
hpLava = Bladex.GetEntity("hpLava")

hpLavaFloodStartTime=0
Bladex.CreateTimer("hpFlood",0.020)
hpFloorBroken=0

hpElevadorArriba=0


hppalanca1elevador=Levers.PlaceLever("Palanca1Elevador", Levers.LeverType3, (-60100.890235,6219.444938,25427.275882), (0.500000,0.500000,-0.500000,0.500000), 1.0)
hppalanca1elevador.mode=1

hppalanca1elevador.OnTurnOnFunc=hpSubeElevador
hppalanca1elevador.OnTurnOnArgs=()

Bladex.SetTriggerSectorFunc("Tmp", "OnEnter", hpBreakFloor )

# char.Position= -35444.6502912, -3446.8, 38842.9353899
