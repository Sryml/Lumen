import MusicTool
import Bladex
import ReadGSFile
import darfuncs

res=ReadGSFile.ReadGhostSectorFile("musica.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])



#al principio del nivel
MusicTool.Music2Sector((-149000, 0, -66000),"tambores_Orc")




#al entrar en grutas con cascadas
#MusicTool.Music2Sector((-85000, 0, 0),"grutas")
MusicTool.Music2Sector(("sfgruta2"),"empty")
MusicTool.Music2Sector(("sfgruta1"),"grutas")

MusicTool.ModifyMusicEvent(("sfgruta2"),("sfgruta1"),"grutas")
MusicTool.ModifyMusicEvent(("sfgruta1"),("sfgruta2"),"tambores_Orc")


#al llegar desde las grutas a los dos orcos
MusicTool.Music2Sector((-65000, -22000, -94000),"tambores_Orc")


#al subir por las rocas zona natural
MusicTool.Music2Sector(("rocasup1"),"tambores_Orc2")

#al llegar al pueblo
MusicTool.Music2Sector(("delantepuertapu"),"empty")

#al llegar a la casa del agua

MusicTool.AddPrelude(("casaguagua"),"Casaguagua")

#MusicTool.Music2Sector(("casaguagua"),"Casaguagua")
#MusicTool.ModifyMusicEvent(("subpueblo2"),("casaguagua"),"tambores_Orc")

#al entrar en el pueblo1	por el rio
MusicTool.Music2Sector(("subpueblo2"),"tambores_pueblo")

MusicTool.ModifyMusicEvent(("subpueblo2"),("subpueblo1"))
MusicTool.ModifyMusicEvent(("subpueblo2"),(-179579.3, -9145.0, 142951.3),"tambores_Orc")

#al entrar en el pueblo2	por el roto
MusicTool.Music2Sector(("subpueblo1"),"tambores_pueblo")
MusicTool.AddPrelude(("subpueblo1"),"inicombate6")


#plataforma casa jefe
MusicTool.AddPrelude(("platjefe"),"ABREPTAFINAL")
MusicTool.Music2Sector(("platjefe"),"empty")


#al entrar en la casa del jefe
MusicTool.AddPrelude(("entracasaj"),"ENTRACASA_J")
MusicTool.Music2Sector(("entracasaj"),"casa_jefe")


MusicTool.ModifyMusicEvent(("entracasaj"),("platjefe"),"tambores_pueblo")

MusicTool.ModifyMusicEvent(("platjefe"),("entracasaj"),"casa_jefe")



MusicTool.Music2Sector(("entratrampa"),"empty")





#las grutas tras la casa del jefe
MusicTool.Music2Sector((-47029.5762814, -29474.7108145, 184462.6),"grutas")

#salida de las grutas
MusicTool.Music2Sector((39081.277379, -52401.8418144, 116234.5),"empty")

#exterior sagrado
MusicTool.Music2Sector(("extsagrado"),"ATMOSFERA32")

MusicTool.ModifyMusicEvent(("extsagrado"),("dolmen"),"grutas")
MusicTool.ModifyMusicEvent(("dolmen"),("extsagrado"),"ATMOSFERA32")




#MusicTool.ModifyMusicEvent(<Sector que modifica>,<Sector a modificar>,[musica])







"""
#######################################################################################
import Bladex
import DMusic
import darfuncs


# mp3 argumentos : nombreinterno, nombredelfichero,fadein,fadeout,volume,priority,background,repeat


	
"""