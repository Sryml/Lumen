import MusicTool
import Bladex
import ReadGSFile

res=ReadGSFile.ReadGhostSectorFile("musica.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

## zona enemigos lokos +minorx

MusicTool.Music2Sector("ambiente1","Atmosfera6")
MusicTool.Music2Sector("ambiente3","Atmosfera1")
MusicTool.Music2Sector("ambiente5","sorpresa-1")
MusicTool.Music2Sector("ambiente6","Atmosfera7")
MusicTool.Music2Sector("ambiente7","Atmosfera6")
MusicTool.Music2Sector("ambiente8","Atmosfera1")
MusicTool.Music2Sector("ambiente9","Atmosfera1")
MusicTool.Music2Sector("ambiente11","Atmosfera7")
MusicTool.Music2Sector("ambiente12","Atmosfera7")
MusicTool.Music2Sector("ambiente13","Atmosfera1")
MusicTool.Music2Sector("ambiente15","Atmosfera5")
MusicTool.Music2Sector("ambiente16","Combate2")


## tras la ultima puerta

MusicTool.Music2Sector("ambiente17","Atmosfera8")
MusicTool.Music2Sector("ambiente19","emptyloquesea")
MusicTool.Music2Sector("ambiente20","Atmosfera8")
MusicTool.AddPrelude("ambiente21","Atm9mp3")
MusicTool.Music2Sector("ambiente21","atmosfera4")
MusicTool.Music2Sector("ambiente22","Combate6")
MusicTool.Music2Sector("ambiente23","Combate4")
MusicTool.Music2Sector("ambiente24","Combate4")
MusicTool.Music2Sector("ambiente25","Combate4")
MusicTool.AddPrelude("ambiente26","Coro1")
MusicTool.Music2Sector("ambiente27","emptyloquesea")
MusicTool.Music2Sector("ambiente28","emptyloquesea")
MusicTool.Music2Sector("ambiente29","Atmosfera3")


## modificaciones

MusicTool.ModifyMusicEvent("ambiente3","ambiente4","emptyloquesea")
MusicTool.ModifyMusicEvent("ambiente6","ambiente2",None)

