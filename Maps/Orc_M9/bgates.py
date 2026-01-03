##################################################################
# Puertas que se rompen
#
# YUio
##################################################################

import Reference
import Select
import Change
import Actions
#import AniSound

derrumbebgate1=Bladex.CreateSound("../../Sounds/M-CAIDA-PUENTE.WAV", "DerrumbeBgate1")
derrumbebgate1.Volume=1
derrumbebgate1.MinDistance=5000
derrumbebgate1.MaxDistance=40000



bgateA1=Bladex.GetSector(-29125,35000,22000)
bgateA2=Bladex.GetSector(-29125,35500,20875)
bgateA1.Active=0
bgateA2.Active=0
bgateA1.InitBreak( (20.0, 0.0, -10.0), (0.0, 800.0, 0.0), (200.0, 0.0, 850.0) ,'madera pesada')
bgateA2.InitBreak( (20.0, 0.0, -10.0), (0.0, 300.0, 0.0), (200.0, 0.0, 250.0) ,'madera pesada')



puertaReventadaA=0

#char.Position = -123000,-15000,10250 -2000


bgateA=Bladex.GetSector(-29500, 34000, 22250)

bgateA.ActiveSurface= -1.0, 0.0, 0.0
bgateA.OnHit=revientaPuertaA
