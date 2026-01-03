import MusicTool
import Bladex
import ReadGSFile

res=ReadGSFile.ReadGhostSectorFile("musica.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

## inicio mapa

MusicTool.Music2Sector("ambiente2","emptyloquesea")
MusicTool.Music2Sector("ambiente3","Atmosfera18")


MusicTool.Music2Sector("ambiente4","Atmosfera6")


MusicTool.Music2Sector("ambiente5","Atmosfera7")
MusicTool.Music2Sector("ambiente6","Atmosfera6")
MusicTool.Music2Sector("ambiente7","emptyloquesea")
MusicTool.Music2Sector("ambiente8","Atmosfera7")

## templo

MusicTool.AddPrelude("ambiente11","coro1")
MusicTool.Music2Sector("ambiente12","emptyloquesea")

## modificaciones

MusicTool.ModifyMusicEvent("ambiente5","ambiente6","Atmosfera18")
MusicTool.ModifyMusicEvent("ambiente5","ambiente4")


## ruta emboscada orcos

MusicTool.Music2Sector("ambiente9","emptyloquesea")
MusicTool.Music2Sector("ambiente10","Atmosfera7")
MusicTool.Music2Sector("ambiente14","Atmosfera7")
MusicTool.Music2Sector("ambiente15","emptyloquesea")
MusicTool.Music2Sector("ambiente16","Atmosfera7")

## ruta bicho zampon

MusicTool.Music2Sector("ambiente18","emptyloquesea")
MusicTool.Music2Sector("ambiente19","Atmosfera7")
MusicTool.Music2Sector("ambiente20","Atmosfera17")
MusicTool.Music2Sector("ambiente21","Atmosfera17")
MusicTool.Music2Sector("ambiente23","emptyloquesea")
MusicTool.Music2Sector("ambiente24","Atmosfera7")
MusicTool.Music2Sector("ambiente25","emptyloquesea")
MusicTool.Music2Sector("ambiente26","Atmosfera7")

## modificaciones

MusicTool.ModifyMusicEvent("ambiente23","ambiente22","Atmosfera7")
MusicTool.ModifyMusicEvent("ambiente23","ambiente20")
MusicTool.ModifyMusicEvent("ambiente23","ambiente21")
MusicTool.ModifyMusicEvent("ambiente24","ambiente23")


## ultima ruta
MusicTool.Music2Sector("ambiente34","Atmosfera7")
MusicTool.Music2Sector("ambiente35","Atmosfera7")
MusicTool.Music2Sector("ambiente27","Atmosfera18")
MusicTool.Music2Sector("ambiente28","emptyloquesea")
MusicTool.Music2Sector("ambiente29","Atmosfera18")
MusicTool.Music2Sector("ambiente30","Atmosfera1")
MusicTool.Music2Sector("ambiente31","Atmosfera1")
MusicTool.Music2Sector("ambiente32","emptyloquesea")


## modificaciones en deffuncs    MusicTool.Music2Sector("ambiente33","Atmosfera18")


### the very end

MusicTool.Music2Sector("ambiente36","Atmosfera4")
MusicTool.Music2Sector("ambiente37","Atmosfera27")
MusicTool.Music2Sector("ambiente38","emptyloquesea")