import Sounds
import Bladex
import ReadGSFile



res=ReadGSFile.ReadGhostSectorFile("exterior.sf")
for igs in res:
  Bladex.AddGhostSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])
  Bladex.SetGhostSectorSound(igs["Name"],igs["Sonido"],igs["Volumen"],igs["VolumenBase"],
                             igs["DistanciaMinima"],igs["DistanciaMaxima"],igs["DistMaximaVertical"],igs["Escala"])


viento1=Bladex.CreateSound("../../Sounds/mountain-ice-wind.wav","Viento1")
viento1.Volume=1
viento1.MinDistance=500
viento1.MaxDistance=1000
viento1.BaseVolume=1.0


######## Funcion: SuenaViento1(sectorindex,entityname)

z1=Bladex.GetSector(-35000,-31000,-24000)
z1.OnEnter=SuenaViento1
