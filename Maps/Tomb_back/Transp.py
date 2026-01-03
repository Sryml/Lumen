import Bladex
import darfuncs
import GenFX

res=ReadGSFile.ReadGhostSectorFile("transp.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])


Bladex.GetEntity("Player1").SendTriggerSectorMsgs=1

#inicio
GenFX.CreateMagicTransport("sfT3", (-31750,6850,-50750))


darfuncs.EnterSecIdEvent("sfT1",ActivaDespuesTablilla)




