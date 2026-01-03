import MusicTool
import Bladex
import ReadGSFile

res=ReadGSFile.ReadGhostSectorFile("musica.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])



MusicTool.Music2Sector("ambiente1","Atmosfera18")
MusicTool.Music2Sector("ambiente2","Atmosfera6")
MusicTool.ModifyMusicEvent("ambiente2","ambiente1",None)
MusicTool.Music2Sector("ambiente3","Combate4")
MusicTool.Music2Sector("ambiente4","Atmosfera7")
MusicTool.ModifyMusicEvent("ambiente4","ambiente3",None)
MusicTool.Music2Sector("ambiente5","atmosfera21")
MusicTool.ModifyMusicEvent("ambiente3","ambiente6","Atmosfera7")