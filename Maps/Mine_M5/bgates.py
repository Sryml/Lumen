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

derrumbebgate2=Bladex.CreateSound("../../Sounds/M-CAIDA-PUENTE.WAV", "DerrumbeBgate2")
derrumbebgate2.Volume=1
derrumbebgate2.MinDistance=5000
derrumbebgate2.MaxDistance=40000

bgateA1=Bladex.GetSector(86000,-11000,-158000)
bgateA2=Bladex.GetSector(86000,-11000,-159250)
bgateB1=Bladex.GetSector(-123000,-15000,10250)
bgateB2=Bladex.GetSector(-124000,-15000,10250)
bgateA1.Active=0
bgateA2.Active=0
bgateB1.Active=0
bgateB2.Active=0
bgateA1.InitBreak( (20.0, 0.0, -10.0), (0.0, 2000.0, 0.0), (200.0, 0.0, 850.0) ,'madera pesada')
bgateA2.InitBreak( (20.0, 0.0, -10.0), (0.0, 2000.0, 0.0), (200.0, 0.0, 850.0) ,'madera pesada')
bgateB1.InitBreak( (-10.0, 0.0, 20.0), (0.0, 2000.0, 0.0), (650.0, 0.0, 200.0) ,'madera pesada')
bgateB2.InitBreak( (-10.0, 0.0, 20.0), (0.0, 2000.0, 0.0), (650.0, 0.0, 200.0) ,'madera pesada')


#char.Position = 86000-2000,-11000,-158000
puertaReventadaA=0

#char.Position = -123000,-15000,10250 -2000
puertaReventadaB=0

bgateA=Bladex.GetSector(84000,-11000,-158000)
bgateB=Bladex.GetSector(-123000,-15000,11250)

bgateA.ActiveSurface= -1.0, 0.0, 0.0
bgateA.OnHit=revientaPuertaA
bgateB.ActiveSurface= 0.0, 0.0, -1.0
bgateB.OnHit=revientaPuertaB
