import Bladex
import GenFX

res=ReadGSFile.ReadGhostSectorFile("transp.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])


Bladex.GetEntity("Player1").SendTriggerSectorMsgs=1

#inicio
GenFX.CreateMagicTransport("transp1", (-66375,22850,49875))

#justo despues inicio
GenFX.CreateMagicTransport("transp2", (-32000,9850,-12000))

#frente a puerta cerrada
GenFX.CreateMagicTransport("transp3", (45875,-1350,94000))

#cerca zona minorx
GenFX.CreateMagicTransport("transp4", (37000,150,-12000))

## final
GenFX.CreateMagicTransport("transp5", (19000,-9150,48000))

