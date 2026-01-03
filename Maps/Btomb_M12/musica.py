import MusicTool
import Bladex
import ReadGSFile

res=ReadGSFile.ReadGhostSectorFile("musica.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

## primera parte mapa

MusicTool.Music2Sector("ambiente1","Atmosfera5")

MusicTool.Music2Sector("ambiente3","Atmosfera7")
MusicTool.Music2Sector("ambiente4","emptyloquesea")
MusicTool.Music2Sector("ambiente5","Atmosfera7")

MusicTool.Music2Sector("ambiente7","emptyloquesea")
MusicTool.Music2Sector("ambiente8","Atmosfera7")
MusicTool.Music2Sector("ambiente9","Atmosfera1")
MusicTool.Music2Sector("ambiente10","Atmosfera7")
MusicTool.Music2Sector("ambiente11","Atmosfera7")
MusicTool.Music2Sector("ambiente12","emptyloquesea")
MusicTool.Music2Sector("ambiente14","Atmosfera7")
MusicTool.Music2Sector("ambiente15","Atmosfera1")
MusicTool.Music2Sector("ambiente16","Atmosfera7")
MusicTool.Music2Sector("ambiente19","Atmosfera5")
MusicTool.Music2Sector("ambiente20","Combate2")

#### segunda parte

MusicTool.Music2Sector("ambiente21","emptyloquesea")
MusicTool.Music2Sector("ambiente22","Atmosfera1")
MusicTool.Music2Sector("ambiente23","Combate4")
MusicTool.Music2Sector("ambiente24","Atmosfera1")
MusicTool.Music2Sector("ambiente25","sorpresa-1")
MusicTool.Music2Sector("ambiente26","Atmosfera7")
MusicTool.Music2Sector("ambiente27","Atmosfera1")

MusicTool.AddPrelude("ambiente28","coro1")
MusicTool.Music2Sector("ambiente29","emptyloquesea")

MusicTool.Music2Sector("ambiente28","Atmosfera4")

MusicTool.Music2Sector("ambiente35","emptyloquesea")

### tablilla


MusicTool.AddPrelude("ambiente31","Atm12mp3")
MusicTool.Music2Sector("ambiente31","Atmosfera3")

## tras tablilla

MusicTool.Music2Sector("ambiente33","Combate3")


## modificaciones

MusicTool.ModifyMusicEvent("ambiente26","ambiente23")
MusicTool.ModifyMusicEvent("ambiente33","ambiente31")
