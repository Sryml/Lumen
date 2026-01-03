import Torchs
import Reference



####ANTORCHAS EN LA CRIPTA


###ANTORCHAS EN PATIO TRASERO Y CRIPTA

Torchs.SetUsable("antorcha1",3,3,50)
Torchs.SetUsable("antorcha2",3,3,60)
Torchs.SetUsable("antorcha3",3,3,90)


Torchs.SetUsable("antorchaen1",3,3,-1)
Torchs.SetUsable("antorchaen2",3,3,-1)
#Torchs.SetUsable("antorchaen3",3,3,-1)
#Torchs.SetUsable("antorchaen4",3,3,-1)
#Torchs.SetUsable("antorchaen5",3,3,-1)
Torchs.SetUsable("antorchaen6",3,3,-1)
Torchs.SetUsable("antorchaen7",3,3,-1)
Torchs.SetUsable("antorchaen8",3,3,-1)
Torchs.SetUsable("antorchaen9",3,3,-1)
Torchs.SetUsable("antorchaen10",3,3,-1)
Torchs.SetUsable("antorchaen11",3,3,-1)
Torchs.SetUsable("antorchaen12",3,3,-1)
Torchs.SetUsable("antorchaen13",3,3,-1)
Torchs.SetUsable("antorchaen14",3,3,-1)
Torchs.SetUsable("antorchaen15",3,3,-1)
Torchs.SetUsable("antorchaen16",3,3,-1)
Torchs.SetUsable("antorchaen17",3,3,-1)
Torchs.SetUsable("antorchaen18",3,3,-1)
Torchs.SetUsable("antorchaen19",3,3,-1)



######en la primera caseta

Apagala1Sec = Bladex.GetSector(-160000, -20000, 130000)
Apagala1Sec.OnEnter = Apagala

Apagala2Sec = Bladex.GetSector(-134000, -10000, 97000)
Apagala2Sec.OnEnter = Apagala

Apagala3Sec = Bladex.GetSector(-113000, -10000, 90000)
Apagala3Sec.OnEnter = Apagala

Apagala4Sec = Bladex.GetSector(-119000, -20000, -32000)
Apagala4Sec.OnEnter = Apagala

import darfuncs
import ReadGSFile
# leer los sectores fantasma

res=ReadGSFile.ReadGhostSectorFile("HOGUERAS.sf")
for igs in res:
   Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

# asignarles el fuego
darfuncs.FireOnGS("fuego1")
darfuncs.FireOnGS("fuego2")
darfuncs.FireOnGS("fuego3")
darfuncs.FireOnGS("fuego4")
darfuncs.FireOnGS("fuego5")
darfuncs.FireOnGS("fuego6")
darfuncs.FireOnGS("fuego7")
darfuncs.FireOnGS("fuego8")
darfuncs.FireOnGS("fuego9")





#######################################################
#para no seleccionar la antorcha de la trampa
#######################################################




Reference.EntitiesSelectionData['torchatran1']=         [0, 0,  " kk"]



Sparks.SetMetalSparkling("metalo1")
Sparks.SetMetalSparkling("metalo2")

Sparks.SetMetalSparkling("rastrillo2")


Sparks.SetWoodenSparkling("madero1")
Sparks.SetWoodenSparkling("madero2")
Sparks.SetWoodenSparkling("madero3")
Sparks.SetWoodenSparkling("madero4")
Sparks.SetWoodenSparkling("madero5")
Sparks.SetWoodenSparkling("madero6")
Sparks.SetWoodenSparkling("madero7")
Sparks.SetWoodenSparkling("madero8")
Sparks.SetWoodenSparkling("madero9")
Sparks.SetWoodenSparkling("madero10")
Sparks.SetWoodenSparkling("madero11")
Sparks.SetWoodenSparkling("madero12")
Sparks.SetWoodenSparkling("madero13")
Sparks.SetWoodenSparkling("madero14")
Sparks.SetWoodenSparkling("madero15")


Sparks.SetStoneSparkling("pedrolo1")
Sparks.SetStoneSparkling("pedrolo2")
Sparks.SetStoneSparkling("pedrolo3")
Sparks.SetStoneSparkling("pedrolo4")
Sparks.SetStoneSparkling("pedrolo5")
Sparks.SetStoneSparkling("pedrolo6")
Sparks.SetStoneSparkling("pedrolo7")
Sparks.SetStoneSparkling("pedrolo8")
Sparks.SetStoneSparkling("pedrolo9")
Sparks.SetStoneSparkling("pedrolo10")
Sparks.SetStoneSparkling("pedrolo11")
Sparks.SetStoneSparkling("pedrolo12")
Sparks.SetStoneSparkling("pedrolo13")
Sparks.SetStoneSparkling("pedrolo14")
Sparks.SetStoneSparkling("pedrolo15")
Sparks.SetStoneSparkling("pedrolo16")
Sparks.SetStoneSparkling("pedrolo17")
Sparks.SetStoneSparkling("pedrolo18")
Sparks.SetStoneSparkling("pedrolo19")
Sparks.SetStoneSparkling("pedrolo20")
Sparks.SetStoneSparkling("pedrolo21")
Sparks.SetStoneSparkling("pedrolo22")
Sparks.SetStoneSparkling("pedrolo23")
Sparks.SetStoneSparkling("pedrolo24")
Sparks.SetStoneSparkling("pedrolo25")
Sparks.SetStoneSparkling("pedrolo26")
Sparks.SetStoneSparkling("pedrolo27")
Sparks.SetStoneSparkling("pedrolo28")
Sparks.SetStoneSparkling("pedrolo29")
Sparks.SetStoneSparkling("pedrolo30")
Sparks.SetStoneSparkling("pedrolo31")
Sparks.SetStoneSparkling("pedrolo32")
Sparks.SetStoneSparkling("pedrolo33")
Sparks.SetStoneSparkling("pedrolo34")
Sparks.SetStoneSparkling("pedrolo35")
Sparks.SetStoneSparkling("pedrolo36")
Sparks.SetStoneSparkling("pedrolo37")
Sparks.SetStoneSparkling("pedrolo38")
Sparks.SetStoneSparkling("pedrolo39")
Sparks.SetStoneSparkling("pedrolo40")
Sparks.SetStoneSparkling("pedrolo41")
Sparks.SetStoneSparkling("pedrolo42")
Sparks.SetStoneSparkling("pedrolo43")
Sparks.SetStoneSparkling("pedrolo44")
Sparks.SetStoneSparkling("pedrolo45")
Sparks.SetStoneSparkling("pedrolo46")
Sparks.SetStoneSparkling("pedrolo47")
Sparks.SetStoneSparkling("pedrolo48")
Sparks.SetStoneSparkling("pedrolo49")
Sparks.SetStoneSparkling("pedrolo50")
Sparks.SetStoneSparkling("pedrolo51")
Sparks.SetStoneSparkling("pedrolo52")
#Sparks.SetStoneSparkling("pedrolo53")
Sparks.SetStoneSparkling("pedrolo54")
Sparks.SetStoneSparkling("pedrolo55")
Sparks.SetStoneSparkling("pedrolo56")
Sparks.SetStoneSparkling("pedrolo57")
Sparks.SetStoneSparkling("pedrolo58")
Sparks.SetStoneSparkling("pedrolo59")
Sparks.SetStoneSparkling("pedrolo60")
Sparks.SetStoneSparkling("pedrolo61")
Sparks.SetStoneSparkling("pedrolo62")
Sparks.SetStoneSparkling("pedrolo63")
Sparks.SetStoneSparkling("pedrolo64")
Sparks.SetStoneSparkling("pedrolo65")
