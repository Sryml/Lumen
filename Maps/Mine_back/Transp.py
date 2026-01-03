import Bladex
import GenFX

res=ReadGSFile.ReadGhostSectorFile("transp.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])


Bladex.GetEntity("Player1").SendTriggerSectorMsgs=1

#inicio
GenFX.CreateMagicTransport("transp1", (-52000,-21150,-28000))

#antes de plaza exterior superior
GenFX.CreateMagicTransport("transp2", (-27000,-31150,10000))

#en zona elevadores tercer recorrido
GenFX.CreateMagicTransport("transp3", (-22000,-8150,-101000))

#en cruce de railes antes del final
GenFX.CreateMagicTransport("transp4", (-33000,-17900,-194000))

