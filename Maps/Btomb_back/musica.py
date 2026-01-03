import MusicTool
import Bladex
import ReadGSFile

res=ReadGSFile.ReadGhostSectorFile("musica.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

MusicTool.Music2Sector("ambiente1","Atmosfera18")
MusicTool.Music2Sector("ambiente2","Atmosfera18")
MusicTool.Music2Sector("ambiente3","Atmosfera24")
MusicTool.Music2Sector("ambiente4","Atmosfera24")
MusicTool.Music2Sector("ambiente5","Atmosfera18")
MusicTool.Music2Sector("ambiente6","Atmosfera24")
MusicTool.Music2Sector("ambiente7","Atmosfera4")
MusicTool.Music2Sector("ambiente8","Atmosfera18")
MusicTool.AddPrelude("ambiente9","Coro5")
MusicTool.Music2Sector("ambiente9","Atmosfera3")
MusicTool.Music2Sector("ambiente10","Atmosfera24")
MusicTool.Music2Sector("ambiente11","Atmosfera24")
