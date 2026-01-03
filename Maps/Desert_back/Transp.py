import Bladex
import GenFX

res=ReadGSFile.ReadGhostSectorFile("transp.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])


Bladex.GetEntity("Player1").SendTriggerSectorMsgs=1

#inicio
GenFX.CreateMagicTransport("sfT1", (-41652.3, 5982.9, -118808.3))

#tras la tablilla
GenFX.CreateMagicTransport("sfT2", (-52559.8, 2379.7, 129942.1))


