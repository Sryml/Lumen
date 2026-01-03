

import Sounds



import ReadGSFile

ReadGSFile.ProcessGhostSectorFile("desert.sf")

#lobo=Sounds.CreatePeriodicSound("../../Sounds/wolf-howl2.wav", "lobo", 10, 5, (-85000, -3000, -116000))
#lobo.Volume=1
#lobo.MinDistance=1000
#lobo.MaxDistance=20000
#lobo.Volumen=1
#lobo.DistanciaMinima=100
#lobo.DistanciaMaxima=20000
#lobo.Escala=2

"""
res=ReadGSFile.ReadGhostSectorFile("desert.sf")
for igs in res:
  Bladex.AddGhostSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

Bladex.SetGhostSectorGroupSound("viento","../../Sounds/Light-wind-bg.wav",0.5,1,1000,30000,0.8)
Bladex.SetGhostSectorGroupSound("agua","../../Sounds/waterlap-light-loop.wav",0.5,0.5,1000,10000,0.8)
Bladex.SetGhostSectorGroupSound("arroyo","../../Sounds/water-flowing-canals.wav",0.5,0.5,2000,30000,0.8)
Bladex.SetGhostSectorGroupSound("cascada","../../Sounds/small-waterfall.wav",1,1,1000,40000,0.5)
Bladex.SetGhostSectorGroupSound("gruta","../../Sounds/Water-drips(int).wav",1,1,1000,30000,0.8)
Bladex.SetGhostSectorGroupSound("pajaro","../../Sounds/Rainforest-bird4.wav",1,1,1000,30000,0.8)
Bladex.SetGhostSectorGroupSound("fuente","../../Sounds/water-gush-loop2.wav",2,1,1000,40000,0.8)

"""
