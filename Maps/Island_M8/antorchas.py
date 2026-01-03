import Torchs
import Reference
import darfuncs

####ANTORCHAS EN LA CRIPTA


###ANTORCHAS EN PATIO TRASERO Y CRIPTA


Torchs.SetUsable("tantorcha",13,3,-1)
Torchs.SetUsable("antorcha1",3,3,50)
Torchs.SetUsable("antorcha2",3,3,60)
Torchs.SetUsable("antorcha3",3,3,50)
Torchs.SetUsable("antorcha4",3,3,50)
Torchs.SetUsable("antorcha5",3,3,30)
Torchs.SetUsable("antorcha6",3,3,40)


Torchs.SetUsable("tantorchaen",3,3,-1)
Torchs.SetUsable("antorchaen1",3,3,-1)
Torchs.SetUsable("antorchaen2",3,3,-1)
Torchs.SetUsable("antorchaen3",3,3,-1)
Torchs.SetUsable("antorchaen4",3,3,-1)
Torchs.SetUsable("antorchaen5",3,3,-1)
Torchs.SetUsable("antorchaen6",3,3,-1)
Torchs.SetUsable("antorchaen7",3,3,-1)


Torchs.SetUsable("palangana1",3,3,-1)

#Reference.EntitiesSelectionData["palangana1"]=(9,4000.0,"Bowl")
darfuncs.SetHint(Bladex.GetEntity("palangana1"),"Bowl","",9.0,4000.0)



Apagala1Sec = Bladex.GetSector(-44000, -38000, 37000)
Apagala1Sec.OnEnter = Apagala

############################################

Apagala2Sec = Bladex.GetSector(-43000, -44000, 43000)
Apagala2Sec.OnEnter = Apagala


######en la parte inferior

Apagala3Sec = Bladex.GetSector(21000, 8000, -34000)
Apagala3Sec.OnEnter = Apagala

Apagala4Sec = Bladex.GetSector(15500, 8000, -29000)
Apagala4Sec.OnEnter = Apagala


#######en arcos delante de la piscina con acido

Apagala5Sec = Bladex.GetSector(13000, 0, -4000)
Apagala5Sec.OnEnter = Apagala

Apagala6Sec = Bladex.GetSector(14000, 0, -11000)
Apagala6Sec.OnEnter = Apagala

Apagala7Sec = Bladex.GetSector(16000, 0, -19000)
Apagala7Sec.OnEnter = Apagala


Apagala8Sec = Bladex.GetSector(15000, 0, -35000)
Apagala8Sec.OnEnter = Apagala

#######en deposito de los lich

Apagala9Sec = Bladex.GetSector(-28600, 5000, -37500)
Apagala9Sec.OnEnter = Apagala


import darfuncs
import ReadGSFile
# leer los sectores fantasma

res=ReadGSFile.ReadGhostSectorFile("hogueras.sf")
for igs in res:
   Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

# asignarles el fuego
darfuncs.FireOnGS("fuego1")
darfuncs.FireOnGS("fuego2")
