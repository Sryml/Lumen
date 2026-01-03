import MusicTool
import Bladex
import ReadGSFile

res=ReadGSFile.ReadGhostSectorFile("musica.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

MusicTool.Music2Sector("ambiente1","Atmosfera18")
MusicTool.Music2Sector("ambiente2","Atmosfera18")
MusicTool.Music2Sector("ambiente3","Atmosfera4")
