import darfuncs
import ReadGSFile

res=ReadGSFile.ReadGhostSectorFile("hogueras.sf")
for igs in res:
   Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

darfuncs.FireOnGS("hoguera1")
darfuncs.FireOnGS("hoguera2")
darfuncs.FireOnGS("hoguera3")
