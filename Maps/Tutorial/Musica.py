import MusicTool
import Bladex
import ReadGSFile


res=ReadGSFile.ReadGhostSectorFile("musica.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])


#Bladex.ExeMusicEvent( Bladex.GetMusicEvent("MAPA2") )
#al llegar a la puerta
MusicTool.Music2Sector("sinicio","MAPA2")

#al llegar a la puerta
#MusicTool.Music2Sector("primerapuerta","empty")

MusicTool.Music2Sector("entrapasoel","empty")

#al entrar en la torre planta baja
MusicTool.Music2Sector("antorchas","atm28")

#en la cocina
MusicTool.AddPrelude("cocina","atm26")

#al entrar en las mazmorras
MusicTool.Music2Sector("salarmas","atm29")


#al entrar en la tablilla
MusicTool.Music2Sector("arco","atm5")
MusicTool.Music2Sector("alarco","empty")




#MusicTool.ModifyMusicEvent(<Sector que modifica>,<Sector a modificar>,[musica])



# mp3 argumentos : nombreinterno, nombredelfichero,fadein,fadeout,volume,priority,background,repeat


	
