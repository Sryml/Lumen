import Bladex
import ReadGSFile



res=ReadGSFile.ReadGhostSectorFile("defilets.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])
