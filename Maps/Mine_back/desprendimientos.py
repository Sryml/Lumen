
#########################################################
#														#
# Desprendimientos						(en 2 sitios)	#
#														#
# (Yuio)												#
#														#
#########################################################

import Reference
import Select
import Change
import Actions
#import AniSound
import Bladex
import ReadGSFile

derrumbesuelopiedra=Bladex.CreateSound("../../Sounds/M-CAIDA-PUENTE.WAV", "DerrumbeSueloPiedra")
derrumbesuelopiedra.Volume=1
derrumbesuelopiedra.MinDistance=5000
derrumbesuelopiedra.MaxDistance=40000

derrumbesuelopiedra2=Bladex.CreateSound("../../Sounds/M-CAIDA-PUENTE.WAV", "DerrumbeSueloPiedra2")
derrumbesuelopiedra2.Volume=1
derrumbesuelopiedra2.MinDistance=5000
derrumbesuelopiedra2.MaxDistance=40000

res=ReadGSFile.ReadGhostSectorFile("derr.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

char.SendTriggerSectorMsgs=1
#esp=Bladex.GetEntity("WeaponInvPrb1")
#esp.SendTriggerSectorMsgs=1

despA1=Bladex.GetSector(7500,-16350,-71000)
despA2=Bladex.GetSector(8750,-16350,-72750)
despA3=Bladex.GetSector(9750,-16350,-71250)

despB1=Bladex.GetSector(-32750,-28300,-65000)
despB2=Bladex.GetSector(-31500,-28300,-66250)
despB3=Bladex.GetSector(-30250,-28300,-65000)

despA1.Active=0
despA2.Active=0
despA3.Active=0
despB1.Active=0
despB2.Active=0
despB3.Active=0

despA1.InitBreak((0.0, 100.0, 0.0), (700.0, 0.0, -100.0), (200.0, 0.0, 1650.0) ,'madera pesada')
despA2.InitBreak((0.0, 100.0, 0.0), (625.0, 0.0, -100.0), (200.0, 0.0, 1920.0) ,'madera pesada')
despA3.InitBreak((0.0, 100.0, 0.0), (676.0, 0.0, -100.0), (200.0, 0.0, 1870.0) ,'madera pesada')

despB1.InitBreak((0.0, 100.0, 0.0), (664.0, 0.0, -70.0), (263.0, 0.0, 1780.0),'madera pesada')
despB2.InitBreak((0.0, 100.0, 0.0), (578.0, 0.0, -250.0), (224.0, 0.0, 1880.0),'madera pesada')
despB3.InitBreak((0.0, 100.0, 0.0), (476.0, 0.0, -130.0), (212.0, 0.0, 1900.0),'madera pesada')

despABreak=0


despBBreak=0


Bladex.SetTriggerSectorFunc("derr1", "OnEnter", runDespA )
Bladex.SetTriggerSectorFunc("derr2", "OnEnter", runDespB )

## sonido de madera chirriante
#woodSound=Sounds.CreateEntitySound("../../Sounds/drawbridge-loop.wav", "woodSound")
#woodSound.Volume=3
#woodSound.MinDistance=2000
#woodSound.MaxDistance=9000

#def playWoodSound(index, ent):
#	entity = Bladex.GetEntity(ent)
#	woodSound.Position =  entity.Position[0], entity.Position[1]+1000, entity.Position[2]
#	woodSound.PlaySound(1)
#
#despASector1=Bladex.GetSector(8750, -18000, -75750)
#despASector2=Bladex.GetSector(8750, -18000, -78500)
#despBSector=Bladex.GetSector(-31250, -30000 , -60250)
#despASector1.OnEnter=playWoodSound
#despASector2.OnEnter=playWoodSound
#despBSector.OnEnter=playWoodSound
