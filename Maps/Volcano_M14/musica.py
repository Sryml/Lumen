import MusicTool
import Bladex
import ReadGSFile

res=ReadGSFile.ReadGhostSectorFile("musica.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

## principio hasta minorx + kab negros

MusicTool.Music2Sector("ambiente1","Atmosfera18")
MusicTool.Music2Sector("ambiente2","Combate4")
MusicTool.Music2Sector("ambiente4","Atmosfera18")
MusicTool.AddPrelude("ambiente5","emptyloquesea")


## desde gargolas soplete hasta lichs post minorx torturadores

MusicTool.Music2Sector("ambiente6","Atmosfera20a")
MusicTool.ModifyMusicEvent("ambiente6","ambiente7","emptyloquesea")

## desde lichs postminorx torturadores hasta el final

MusicTool.Music2Sector("ambiente9","Atmosfera1")
MusicTool.Music2Sector("ambiente10","Atmosfera3")
