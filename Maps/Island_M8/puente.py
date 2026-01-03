import dust
import Bladex
import Sounds

pte=Bladex.CreateEntity("puente","PuenteFernando",-80728.454000,-4556.012000,30535.204000)
pte.Static=1
pte.Scale=0.645445
pte.Orientation=0.706434,0.030844,0.706434,-0.030844

p_num_frames = 128
p_counter = 130



looppuentelevadizo=Sounds.CreateEntitySound("../../Sounds/drawbridge-loop.wav", "LoopPuenteLevadizo")
looppuentelevadizo.Volume=1
looppuentelevadizo.MinDistance=10000
looppuentelevadizo.MaxDistance=90000
looppuentelevadizo.Position = (-85989.1491419, -1058.56934322, 30598.7661143)

golpepuentelevadizo=Sounds.CreateEntitySound("../../Sounds/drawbridge-door-close.wav", "GolpePuenteLevadizo")
golpepuentelevadizo.Volume=1
golpepuentelevadizo.MinDistance=10000
golpepuentelevadizo.MaxDistance=90000
golpepuentelevadizo.Position = (-85989.1491419, -1058.56934322, 30598.7661143)

atranquepuentelevadizo=Sounds.CreateEntitySound("../../Sounds/metal-lever3.wav", "AtranquePuenteLevadizo")
atranquepuentelevadizo.Volume=1
atranquepuentelevadizo.MinDistance=10000
atranquepuentelevadizo.MaxDistance=90000
atranquepuentelevadizo.Position = (-85989.1491419, -1058.56934322, 30598.7661143)





sopen=Bladex.GetSector(-95000,-3000,30000)
sopen.OnEnter=AbrePuente

sclose=Bladex.GetSector(-69618.3756445, -964.8, 30576.1316363)
sclose.OnEnter=CierraPuente
