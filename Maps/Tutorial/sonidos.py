

import Sounds



import ReadGSFile
res=ReadGSFile.ReadGhostSectorFile("tutorial.sf")
for igs in res:
  Bladex.AddGhostSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])
  Bladex.SetGhostSectorSound(igs["Name"],igs["Sonido"],igs["Volumen"],igs["VolumenBase"],
                             igs["DistanciaMinima"],igs["DistanciaMaxima"],igs["Escala"])




vent0=Bladex.CreateSound("../../Sounds/Light-Wind-bg.wav","vent0")
vent0.MaxDistance=20000
vent0.MinDistance=5000
vent0.Volume=1.0
vent0.BaseVolume=1.0
vent0.SendNotify=0
vent0.Play(208758.946676, -3462.02926818, 64710.10398,-1)

vent10=Bladex.CreateSound("../../Sounds/Light-Wind-bg.wav","vent10")
vent10.MaxDistance=15000
vent10.MinDistance=4000
vent10.Volume=1.0
vent10.BaseVolume=1.0
vent10.SendNotify=0
vent10.Play(209722.927298, -2135.08653425, 98949.7578,-1)

vent11=Bladex.CreateSound("../../Sounds/Light-Wind-bg.wav","vent11")
vent11.MaxDistance=15000
vent11.MinDistance=4000
vent11.Volume=1.0
vent11.BaseVolume=1.0
vent11.SendNotify=0
vent11.Play(251081.325638, -5105.543030808, 126317.682,-1)

chorrillo1=Bladex.CreateSound("../../Sounds/agua-canal.wav","chorrillo11111")
chorrillo1.MaxDistance=10000
chorrillo1.MinDistance=3000
chorrillo1.Volume=1.0
chorrillo1.BaseVolume=1.0
chorrillo1.SendNotify=0
chorrillo1.Play(336000, -6000, 126000,-1)

vent1=Bladex.CreateSound("../../Sounds/Light-Wind-bg.wav","vent1")
vent1.MaxDistance=10000
vent1.MinDistance=3000
vent1.Volume=1.0
vent1.BaseVolume=1.0
vent1.SendNotify=0
vent1.Play(339750, -1000, 79250,-1)


# Increase distance sound travels for throwing objects
gmetlig=Bladex.GetSound("GolpeMetalLigero")
gmetlig.MaxDistance=31000

gmetmed=Bladex.GetSound("GolpeMetalMediano")
gmetmed.MaxDistance=31000
