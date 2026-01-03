import MusicTool
import Bladex
import ReadGSFile
import darfuncs

res=ReadGSFile.ReadGhostSectorFile("musica.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])



#al entrar en el primer recinto

MusicTool.Music2Sector(("principio"),"atm24")

MusicTool.Music2Sector(("entrozonadeath"),"atm16")

MusicTool.Music2Sector(("entracositas"),"atm16")

MusicTool.Music2Sector(("salecositas"),"atm24")


MusicTool.Music2Sector(("patio2"),"atm16")




#delante del pendulo
MusicTool.AddPrelude(("entropendulo"),"sorpresa1")
MusicTool.Music2Sector(("entropendulo"),"atm1")


#al entrar en la tablilla

MusicTool.AddPrelude(("entrotrampa"),"coro6")
MusicTool.Music2Sector(("entrotrampa"),"atm1")

MusicTool.ModifyMusicEvent(("stablilla1"),("stablilla2"),"empty")



#al entrar en el cementerio
MusicTool.Music2Sector(("salecementerio"),"atm16")
MusicTool.Music2Sector(("salecementerio2"),"atm16")

MusicTool.Music2Sector(("cementerio"),"atm19")



#al entrar en la zona del rey
MusicTool.Music2Sector(("saleking"),"empty")


chaoscaller = darfuncs.E_Grup()
chaoscaller.AddGuy("ChaosKnightBak")
chaoscaller.OnDeath = ApagaMusicaCaos





