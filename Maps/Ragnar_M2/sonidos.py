
import ReadGSFile
res=ReadGSFile.ReadGhostSectorFile("ragnar.sf")
for igs in res:
  Bladex.AddGhostSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])
  Bladex.SetGhostSectorSound(igs["Name"],igs["Sonido"],igs["Volumen"],igs["VolumenBase"],
                             igs["DistanciaMinima"],igs["DistanciaMaxima"],igs["DistMaximaVertical"],igs["Escala"])
