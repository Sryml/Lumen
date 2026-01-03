import MusicTool
import Bladex
import ReadGSFile

res=ReadGSFile.ReadGhostSectorFile("musica.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])




#al entrar en LA CIUDAD
MusicTool.Music2Sector(("entracity1"),"tambores_Orc2")
MusicTool.Music2Sector(("entracity2"),"tambores_Orc2")

MusicTool.Music2Sector(("salecity"),"empty")


MusicTool.ModifyMusicEvent(("salecity"),("entracity1"),"tambores_Orc2")
MusicTool.ModifyMusicEvent(("salecity"),("entracity2"),"tambores_Orc2")


#tras pasar la puerta con llave
MusicTool.Music2Sector(("traslapuerta"),"empty")

MusicTool.ModifyMusicEvent(("traslapuerta"),("entracity1"),"tambores_Orc1")
MusicTool.ModifyMusicEvent(("traslapuerta"),("entracity2"),"tambores_Orc1")

#entrando en zona  pulsadores
MusicTool.AddPrelude(("entrazpulsadores"),"empty2")


MusicTool.ModifyMusicEvent(("vueltapasillos"),("vueltapasillos2"),"tambores_Orc1")
MusicTool.ModifyMusicEvent("vueltapasillos","traslapuerta")


#al entrar en el secreto de los pulsadores
MusicTool.AddPrelude(("sorpresasecreto"),"sorpresa3")

MusicTool.Music2Sector(("entrasecreto"),"secreto1")
#MusicTool.Music2Sector(("salesecreto"),"empty")

MusicTool.ModifyMusicEvent(("entrasecreto"),("salesecreto"),"empty")
MusicTool.ModifyMusicEvent(("salesecreto"),("entrasecreto"),"secreto1")

#al entrar en la zona de las grutas
MusicTool.Music2Sector(("entrazonacaverna"),"misterio_Orc")

MusicTool.ModifyMusicEvent(("entrazonacaverna"),("salezonacaverna"),"empty")
MusicTool.ModifyMusicEvent(("salezonacaverna"),("entrazonacaverna"),"misterio_Orc")


#tras pasar la puerta de barrotes
MusicTool.Music2Sector(("entragrotgrande"),"grutas")

MusicTool.ModifyMusicEvent(("entragrotgrande"),("salegrotgrande"),"misterio_Orc")
MusicTool.ModifyMusicEvent(("salegrotgrande"),("entragrotgrande"),"grutas")

#orcos en grutas
MusicTool.Music2Sector(("entgrutorc"),"tambores_Orc1")
MusicTool.Music2Sector(("salgrutorc"),"empty")

#llegada al puente
MusicTool.AddPrelude(("entrapuente"),"sorpresa3")

MusicTool.ModifyMusicEvent(("entrapuente"),("salgrutorc"),"tambores_Orc1")

#entra en la sala del troll
MusicTool.AddPrelude(("entrasalatroll"),"sorpresa3")
MusicTool.Music2Sector(("entrasalatroll"),"grutas")


MusicTool.ModifyMusicEvent(("entrasalatroll"),("salesalatroll1"),"tambores_Orc1")
MusicTool.ModifyMusicEvent(("salesalatroll1"),("entrasalatroll"),"grutas")

#escaleras palacio
MusicTool.AddPrelude(("salesalatroll2"),"coro6")
MusicTool.Music2Sector(("salesalatroll2"),"empty")

#Biblioteca
MusicTool.AddPrelude(("entrabiblio"),"biblio2")
MusicTool.Music2Sector(("entrabiblio"),"secreto1")
MusicTool.Music2Sector(("entrabiblio2"),"grutas")
MusicTool.Music2Sector(("entrabiblio3"),"empty")

MusicTool.ModifyMusicEvent(("entrabiblio"),("salebiblio"),"tambores_Orc1")
MusicTool.ModifyMusicEvent(("salebiblio"),("entrabiblio"),"secreto1")
MusicTool.ModifyMusicEvent("entrabiblio","salesalatroll2")
MusicTool.ModifyMusicEvent("entrabiblio3","entrabiblio2")
MusicTool.ModifyMusicEvent("entrabiblio2","entrabiblio")
MusicTool.ModifyMusicEvent("salebiblio","entrasalatroll")
MusicTool.ModifyMusicEvent("salebiblio","salesalatroll2")


#MusicTool.ModifyMusicEvent(<Sector que modifica>,<Sector a modificar>,[musica])
# mp3 argumentos : nombreinterno, nombredelfichero,fadein,fadeout,volume,priority,background,repeat

