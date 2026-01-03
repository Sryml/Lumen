import Bladex
import ReadGSFile



res=ReadGSFile.ReadGhostSectorFile("ruinstsgen.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])
