import MusicTool
import Bladex
import ReadGSFile


res=ReadGSFile.ReadGhostSectorFile("musica.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])


#al entrar en el cuerpo de guardia
MusicTool.AddPrelude(("entraguardia"),"sorpresa7")

#al entrar en el primer recinto
MusicTool.Music2Sector(("entrarecinto1"),"atm29")
MusicTool.Music2Sector(("entrarecinto2"),"atm29")
MusicTool.Music2Sector(("patio2"),"empty")

#al entrar en la torre
MusicTool.Music2Sector(("entratorre"),"atm22")

MusicTool.Music2Sector(("salecositas"),"atm5")


#al entrar en el segundo recinto
MusicTool.AddPrelude(("entrozonadeath"),"atm7")

MusicTool.ModifyMusicEvent(("entrozonadeath"),("salezonadeath"),"atm5")

#al entrar en el templo
MusicTool.AddPrelude(("centrotemplo"),"templolindo")

#al entrar en la zona de los zombies
MusicTool.AddPrelude(("misteriozombie"),"incomb3")

MusicTool.Music2Sector(("entrazombies"),"atm18")

MusicTool.Music2Sector(("salezombies"),"empty")



#delante del pendulo
MusicTool.AddPrelude(("entropendulo"),"incomb6")
MusicTool.Music2Sector(("entropendulo"),"empty")


#al entrar en la tablilla
#MusicTool.Music2Sector(("stablilla1"),"atm10")

#MusicTool.ModifyMusicEvent(("stablilla1"),("stablilla2"),"empty")



#al entrar en el cementerio
#MusicTool.Music2Sector(("entracementerio"),"empty2")
MusicTool.AddPrelude(("entracementerio"),"incomb33")
MusicTool.ModifyMusicEvent(("entroking"),("entracementerio"),"empty")

#al entrar en la zona del rey
#MusicTool.AddPrelude(("entracementerio"),"incomb33")
MusicTool.Music2Sector(("entroking"),"atm1")

MusicTool.ModifyMusicEvent(("entroking"),("saleking"),"empty2")
MusicTool.ModifyMusicEvent(("saleking"),("entroking"),"atm3")
MusicTool.ModifyMusicEvent("king","entroking")


#al entrar en la zona del reyna
#MusicTool.AddPrelude(("entracementerio"),"incomb33")
MusicTool.Music2Sector(("entroreina"),"atm4")

MusicTool.ModifyMusicEvent(("entroreina"),("salereina1"),"empty")
MusicTool.ModifyMusicEvent(("entroreina"),("salereina2"),"empty")
MusicTool.ModifyMusicEvent(("salereina1"),("entroking"),"atm4")
MusicTool.ModifyMusicEvent(("salereina2"),("entroking"),"atm4")

MusicTool.Music2Sector(("entragua"),"empty")
MusicTool.Music2Sector(("pasarejareina"),"empty")


#MusicTool.ModifyMusicEvent(<Sector que modifica>,<Sector a modificar>,[musica])



# mp3 argumentos : nombreinterno, nombredelfichero,fadein,fadeout,volume,priority,background,repeat


	
