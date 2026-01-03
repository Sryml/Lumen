import Bladex
import GenFX

res=ReadGSFile.ReadGhostSectorFile("transp.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])


Bladex.GetEntity("Player1").SendTriggerSectorMsgs=1

#inicio
GenFX.CreateMagicTransport("transp1", (326000,-150,-221000))

#en plaza exterior media
GenFX.CreateMagicTransport("transp2", (348000,8850,-222000))

#en plaza exterior inferior
GenFX.CreateMagicTransport("transp3", (372750,20950,-228000))

#en plaza inferior 2
GenFX.CreateMagicTransport("transp4", (311000,9100,-213750))

#en puente inferior
GenFX.CreateMagicTransport("transp5", (325000,43850,-111000))

#junto a elevador gordo
GenFX.CreateMagicTransport("transp7", (325000,13600,-71000))
