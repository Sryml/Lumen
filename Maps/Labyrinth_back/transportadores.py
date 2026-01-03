import Bladex
import ReadGSFile
import GenFX





res=ReadGSFile.ReadGhostSectorFile("transportadores.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])



GenFX.CreateMagicTransport("transp1", (-33000, 850, 43000))
GenFX.CreateMagicTransport("transp2", (0, -8150, 58500))
GenFX.CreateMagicTransport("transp3", (53500, -650, 25000))
GenFX.CreateMagicTransport("transp4", (65000, -6900, -19500))
GenFX.CreateMagicTransport("transp5", (-38500, -7150, 0))
GenFX.CreateMagicTransport("transp6", (-63500, -650, -14000))
GenFX.CreateMagicTransport("transp7", (-19000, -8150, -54500))
GenFX.CreateMagicTransport("transp8", (19000, -8150, -54500))

# Transportadores adicionales en el DefFuncs.py
