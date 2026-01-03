import MusicTool
import Bladex
import ReadGSFile


res=ReadGSFile.ReadGhostSectorFile("musica.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])


#al principio del nivel
MusicTool.Music2Sector("inicioto","atm29")



#al entrar en el puente
#MusicTool.AddPrelude("entrapuente","sorpresa8")
MusicTool.Music2Sector("entrapuente","atm11")



#entra lago acido
MusicTool.Music2Sector("entracido","atm21")
MusicTool.Music2Sector("saleacido","empty")

#entra grutas bichitos
MusicTool.Music2Sector("entracositas","atm4")
MusicTool.Music2Sector("entralmacen","empty")

MusicTool.ModifyMusicEvent("entracositas","salecositas","empty")

#entra en armeria
MusicTool.Music2Sector("entrarmeria","atm27")

MusicTool.ModifyMusicEvent("entrarmeria","salearmeria","atm29")

#entra zona de caballeros arqueros
MusicTool.Music2Sector("entragaleria","atm16")
MusicTool.Music2Sector("salecaballeros","empty")

#al entrar en la sala de los golems
MusicTool.AddPrelude("antesdelosgolems","inatm2")
#MusicTool.Music2Sector("antesdelosgolems","empty")


#entra zona al subir por el ascensor
MusicTool.Music2Sector("trasascensor","atm29")


#entra zona oscura
#MusicTool.AddPrelude("entrazonaoscura","sorpresa8")
MusicTool.Music2Sector("entrazonaoscura","atm30")

MusicTool.Music2Sector("salezonaoscura","empty")



#entra zona esqueletos calientes
MusicTool.Music2Sector("saledelgolemla","atm444")

#entra zona demonios
MusicTool.Music2Sector("entravapores","empty")

#entra zona demonios
MusicTool.Music2Sector("trastrampalava","atm19")



"""
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
"""
#MusicTool.ModifyMusicEvent(<Sector que modifica>,<Sector a modificar>,[musica])



# mp3 argumentos : nombreinterno, nombredelfichero,fadein,fadeout,volume,priority,background,repeat


	
