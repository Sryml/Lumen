
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

despA1=Bladex.GetSector(-27500,4350,-12000)


despA1.Active=0


despA1.InitBreak((0.0, 1100.0, 0.0), (700.0, 0.0, -1100.0), (1200.0, 0.0, 2650.0) ,'madera pesada')


despABreak=0



Bladex.SetTriggerSectorFunc("derr", "OnEnter", runDespA )
