import MusicTool
import Bladex
import ReadGSFile
import darfuncs

res=ReadGSFile.ReadGhostSectorFile("musica.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])


#al principio del nivel

#MusicTool.Music2Sector("entrarecinto","atm12")

MusicTool.Music2Sector("entrarecinto","atm24")
MusicTool.Music2Sector("entrarecinto2","atm18")

MusicTool.Music2Sector("entrafuego","atm24")
MusicTool.Music2Sector("salefuego","atm18")


#entra zona torres
#MusicTool.Music2Sector("entratorres1","atm19")
#MusicTool.Music2Sector("entratorres2","atm19")
#MusicTool.Music2Sector("saletorres1","empty")
#MusicTool.Music2Sector("saletorres2","empty")


MusicTool.Music2Sector("entraltaragua","atm19")
MusicTool.Music2Sector("salealtaragua","atm18")
MusicTool.Music2Sector("entraltarfuego","atm19")
MusicTool.Music2Sector("salealtarfuego","atm18")


#entra sala a tablillas

MusicTool.Music2Sector("entrasalaatablillas","empty")
MusicTool.Music2Sector("trampatablilla","atm1")
MusicTool.Music2Sector("delantetablilla","empty")

MusicTool.ModifyMusicEvent("delantetablilla","trampatablilla","empty")


#entra sala hipostila
MusicTool.AddPrelude("entrahipostila","sorpresa6")
MusicTool.Music2Sector("entrahipostila","atm19")


chaoscaller = darfuncs.E_Grup()
chaoscaller.AddGuy("ChaosKnightBak")
chaoscaller.OnDeath = ApagaMusicaCaos




#MusicTool.ModifyMusicEvent(<Sector que modifica>,<Sector a modificar>,[musica])



# mp3 argumentos : nombreinterno, nombredelfichero,fadein,fadeout,volume,priority,background,repeat


	
