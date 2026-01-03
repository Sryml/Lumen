import Bladex
import dust
import darfuncs
import ReadGSFile





##########################################################################################3
##
##		para que quemen los fuegos


import darfuncs
import ReadGSFile
# leer los sectores fantasma

res=ReadGSFile.ReadGhostSectorFile("fuegos.sf")
for igs in res:
   Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

# asignarles el fuego
darfuncs.FireOnGS("Fuego1")
darfuncs.FireOnGS("Fuego2")
darfuncs.FireOnGS("Fuego3")
darfuncs.FireOnGS("Fuego4")
