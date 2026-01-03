import MusicTool
import Bladex
import ReadGSFile


res=ReadGSFile.ReadGhostSectorFile("musica.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])


#al principio del nivel
MusicTool.AddPrelude("pipio","coro1")

MusicTool.Music2Sector("inicioempty","empty")
MusicTool.Music2Sector("iniciorc","atm5")
#MusicTool.Music2Sector("entrarecinto","atm6")

#entra aguasagrada
MusicTool.AddPrelude("entragua","sorpresa8")
MusicTool.Music2Sector("entragua","empty")

MusicTool.Music2Sector("saleagua","atm5")
#MusicTool.ModifyMusicEvent("entragua","saleagua","atm5")


#entra fuego sagrado
MusicTool.AddPrelude("entrafuego","sorpresa8")
MusicTool.Music2Sector("entrafuego","empty")

MusicTool.Music2Sector("salefuego","atm5")
#MusicTool.ModifyMusicEvent("entrafuego","salefuego","atm5")


#entraltar fuego sagrado
MusicTool.Music2Sector("entraltarfuego","empty")
#MusicTool.ModifyMusicEvent("entraltarfuego","salealtarfuego","atm5")
MusicTool.Music2Sector("salealtarfuego","atm5")

#entraltar agua sagrada
MusicTool.Music2Sector("entraltaragua","empty")
#MusicTool.ModifyMusicEvent("entraltaragua","salealtaragua","atm5")
MusicTool.Music2Sector("salealtaragua","atm5")

#entra zona torres
MusicTool.Music2Sector("entratorres1","atm6")
MusicTool.Music2Sector("entratorres2","atm6")
MusicTool.Music2Sector("saletorres1","empty")
MusicTool.Music2Sector("saletorres2","empty")


#al entrar en la sala central del golem
MusicTool.AddPrelude("entrakeygolem","sorpresa4")


#entra sala a tablillas

MusicTool.Music2Sector("entrasalaatablillas","empty")
MusicTool.Music2Sector("trampatablilla","atm7")
MusicTool.Music2Sector("delantetablilla","empty")

MusicTool.ModifyMusicEvent("delantetablilla","trampatablilla","empty")


#entra sala hipostila
MusicTool.AddPrelude("entrahipostila","coro1")

MusicTool.Music2Sector("salehipostila","atm6")
MusicTool.Music2Sector("hipostila","empty2")
MusicTool.Music2Sector("hipostila2","empty2")

#entra palacio
MusicTool.Music2Sector("entrapalacio","atm16")

MusicTool.ModifyMusicEvent("entrapalacio","salepalacio","empty")
MusicTool.ModifyMusicEvent("entrapalacio","salepalacio2","empty")
MusicTool.ModifyMusicEvent("salepalacio2","entrapalacio")

#entra murallas
MusicTool.Music2Sector("entramurallas","atm16")

MusicTool.Music2Sector("salemurallas","empty")
MusicTool.Music2Sector("salemurallas2","empty")
MusicTool.Music2Sector("salemurallas3","empty")
MusicTool.Music2Sector("salemurallas4","empty")



#entra sala a crypta

MusicTool.Music2Sector("entracrypta","atm18")
MusicTool.Music2Sector("entracrypta2","atm8")

MusicTool.ModifyMusicEvent("entracrypta2","entracrypta")
MusicTool.ModifyMusicEvent("entracrypta","entrapalacio")


MusicTool.Music2Sector("cojebaston","atm8")
MusicTool.ModifyMusicEvent("cojebaston","entracrypta2")

#al entrar en el templo
MusicTool.Music2Sector("entratemploa","atm2")
MusicTool.Music2Sector("entratemplob","atm2")
MusicTool.Music2Sector("entratemplof","atm2")

MusicTool.ModifyMusicEvent("entratemploa","saletemploa","empty")
MusicTool.ModifyMusicEvent("entratemploa","saletemplob","empty")
MusicTool.ModifyMusicEvent("entratemploa","saletemplof","empty")

MusicTool.ModifyMusicEvent("entratemplob","saletemploa","empty")
MusicTool.ModifyMusicEvent("entratemplob","saletemplob","empty")
MusicTool.ModifyMusicEvent("entratemplob","saletemplof","empty")

MusicTool.ModifyMusicEvent("entratemplof","saletemploa","empty")
MusicTool.ModifyMusicEvent("entratemplof","saletemplob","empty")
MusicTool.ModifyMusicEvent("entratemplof","saletemplof","empty")

#al entrar en el templo subterraneo

MusicTool.Music2Sector("entratemplosub","atm19")


#al entrar en el charco de la llave
MusicTool.AddPrelude("delantekey","sorpresa8")
MusicTool.Music2Sector("delantekey","empty")

MusicTool.Music2Sector("trasptakey","atm19")
MusicTool.ModifyMusicEvent("trasptakey","delantekey")



#salida
MusicTool.AddPrelude("delantesalida","coro6")
MusicTool.Music2Sector("delantesalida","empty")

#MusicTool.ModifyMusicEvent(<Sector que modifica>,<Sector a modificar>,[musica])



# mp3 argumentos : nombreinterno, nombredelfichero,fadein,fadeout,volume,priority,background,repeat


	
