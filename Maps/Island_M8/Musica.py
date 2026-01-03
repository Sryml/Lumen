import MusicTool
import Bladex
import ReadGSFile


res=ReadGSFile.ReadGhostSectorFile("musica.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])


#al entrar en la isla
MusicTool.AddPrelude("entraisla","incomb1")
MusicTool.Music2Sector("entraisla","atm8")

MusicTool.Music2Sector("primerapuerta","empty")

MusicTool.Music2Sector("entrapasoel","empty")

#al entrar en la torre planta baja
MusicTool.Music2Sector("entratorre","atm22")
MusicTool.Music2Sector("salesalatrono","empty")
#MusicTool.Music2Sector("entrapuentecito","atm22")

#en la armadura
MusicTool.AddPrelude("entrarmadura","sorpresarmadura")

MusicTool.Music2Sector("entrasalachimenea","atm29")

#al entrar en las mazmorras
MusicTool.Music2Sector("entramazmext","atm4")
MusicTool.Music2Sector("entrabanios","atm4")


#al entrar en la tablilla
MusicTool.Music2Sector("entratablilla","atm10")
MusicTool.Music2Sector("entratablilla2","empty")


MusicTool.ModifyMusicEvent("entratablilla2","entratablilla")
MusicTool.ModifyMusicEvent("entratablilla","saletablilla","empty")


#en el amuleto secreto
MusicTool.AddPrelude("entrasecreto","sorpresa8")

MusicTool.Music2Sector("antesdeldeposito","empty")
MusicTool.AddPrelude("antesdeldeposito","sorpresa3")

MusicTool.Music2Sector("saledeposito","atm11")
MusicTool.ModifyMusicEvent("saledeposito","entraenmazmorra","atm18")

MusicTool.Music2Sector("entradungeon","empty")

#al entrar en la 2ª planta de la torre
MusicTool.Music2Sector("entrasegundopiso","atm16")
MusicTool.Music2Sector("salesegundopiso","empty")

#al entrar en la 3ª planta de la torre
MusicTool.Music2Sector("entrasombra","atm9")
#MusicTool.Music2Sector("entratorreoscura","empty")


MusicTool.Music2Sector("salezonaoscura1","empty")
MusicTool.Music2Sector("salezonaoscura2","empty")


#al entrar en la planta de los esqueletos
MusicTool.Music2Sector("entrazonaskl1","combate6skl")
MusicTool.Music2Sector("entrazonaskl2","combate6skl")

MusicTool.ModifyMusicEvent("entrazonaskl1","entrazonaoscura2","atm9")
MusicTool.ModifyMusicEvent("entrazonaskl1","entrazonaoscura3","atm9")
MusicTool.ModifyMusicEvent("entrazonaskl2","entrazonaoscura2","atm9")
MusicTool.ModifyMusicEvent("entrazonaskl2","entrazonaoscura3","atm9")



#al entrar en el vampiro
MusicTool.Music2Sector("entrademonio","atm19")
#MusicTool.Music2Sector("saledemonio","atm19")

#MusicTool.Music2Sector("saledemonio","empty")


MusicTool.Music2Sector("pasalmural","empty")


#MusicTool.ModifyMusicEvent(<Sector que modifica>,<Sector a modificar>,[musica])



# mp3 argumentos : nombreinterno, nombredelfichero,fadein,fadeout,volume,priority,background,repeat


	
