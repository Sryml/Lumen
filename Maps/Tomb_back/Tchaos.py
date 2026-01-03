import BackMisc
import darfuncs



res=ReadGSFile.ReadGhostSectorFile("Tchaos.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])


Bladex.GetEntity("Player1").SendTriggerSectorMsgs=1


##################################################################
#
# CHAOS KNIGHT
#
##################################################################

BackMisc.CHAOS_KNIGHT_LEVEL       = 4
BackMisc.CHAOS_KNIGHT_POSITION    = 99266.1, 1631.5, 820.4
BackMisc.CHAOS_KNIGHT_ANGLE       = 0


BackMisc.AddChaosDisappearsTSector("sale1")
BackMisc.AddChaosDisappearsTSector("sale2")
BackMisc.AddChaosDisappearsTSector("sale3")
BackMisc.AddChaosDisappearsTSector("sale4")
		
BackMisc.EXEC_IN_PLAYER_APPEARING       = EnciendeMusicaInicio
BackMisc.EXEC_IN_CHAOS_KNIGHT_APPEARING = EnciendeMusicaApChaos

BackMisc.AddChaosAppearsTSector	("secF5")
BackMisc.AddChaosAppearsTSector("entra1")

BackMisc.PrepareChaosAppears()



## DEMONIOS Y VAMPIROS 13 TOTAL

BackMisc.AddVampires(8,(-20247.0040704, 5070.92786693, -8937.1),3)
BackMisc.AddDemons  (9,(-20247.0040704, 5070.92786693, -8937.1),6)



BackMisc.HideEnemiesSector ((-20247.0040704, 5070.92786693, -8937.1))
BackMisc.HideEnemiesSector ((-17554.2795507, -424.940860578, 29111.9))

## DEMONIOS EN SALA LARGA UNO

BackMisc.HideEnemiesSector   (("secf1"))
BackMisc.AddDemonAppears     (("secf1"),(22424.7016321, 4930.50127191, -34427.6),0.1)
idx = BackMisc.AddSectorCount(("secf1"),3,0)
BackMisc.AddSectorDelete(idx, ("secf1"))


## DEMONIOS EN SALA LARGA DOS

BackMisc.HideEnemiesSector   (("secf2"))
BackMisc.AddDemonAppears     (("secf2"),(37365.2469091, 4883.59750842, -37195.1),0.1)
BackMisc.AddDemonAppears     (("secf2"),(38573.4265491, 4896.47929387, -31274.2),0.1)
idx = BackMisc.AddSectorCount(("secf2"),3,0)
BackMisc.AddSectorDelete(idx, ("secf2"))


#EN PLATAFORMA DCHA
BackMisc.HideEnemiesSector   (("secf4"))
BackMisc.AddDemonAppears     (("secf4"),(21158.073518, -119.809281987, -23398.9),0.1)
idx = BackMisc.AddSectorCount(("secf4"),3,0)
BackMisc.AddSectorDelete(idx, ("secf4"))


#PATIO DCHA DOS
BackMisc.HideEnemiesSector ((57774.4341481, 5326.21882639, -24000.7))
BackMisc.AddDemonAppears   ((57774.4341481, 5326.21882639, -24000.7),(57774.4341481, 5326.21882639, -24000.7),0.1)
BackMisc.AddDemonAppears   ((57774.4341481, 5326.21882639, -24000.7),(57063.9832935, 5290.04775234, -16889.5),0.3)
idx = BackMisc.AddSectorCount((9283.0, -3812.1, 27657.8),3,0)
BackMisc.AddSectorDelete(idx, (9283.0, -3812.1, 27657.8))



#PLATAFORMA IZDA
BackMisc.HideEnemiesSector ((-5283.12068075, -132.025781421, 32038.2))
BackMisc.AddDemonAppears   ((-5283.12068075, -132.025781421, 32038.2),(-5283.12068075, -132.025781421, 32038.2),0.1)
idx = BackMisc.AddSectorCount((-5283.12068075, -132.025781421, 32038.2),3,0)
BackMisc.AddSectorDelete(idx, (-5283.12068075, -132.025781421, 32038.2))


#GALERIA IZDA
BackMisc.HideEnemiesSector 	(("SECF3"))
BackMisc.AddDemonAppears   	(("SECF3"),(22630.8960466, 156.321289536, 24633.6),0.1)
BackMisc.AddDemonAppears   	(("SECF3"),(34380.5150865, 189.567073158, 24381.9),0.3)
idx = BackMisc.AddSectorCount	(("SECF3"),3,0)
BackMisc.AddSectorDelete(idx, ("SECF3"))

#AL LADO CEMENTERIO
BackMisc.HideEnemiesSector ((62897.0555496, 5174.61166272, 20900.5))
BackMisc.AddDemonAppears   ((62897.0555496, 5174.61166272, 20900.5),(70998.4798149, 5176.31390615, 24601.1),0.6)



#VAMPIRO
#BackMisc.AddVampireAppears   ((62897.0555496, 5174.61166272, 20900.5),(62897.0555496, 5174.61166272, 20900.5),0.2)
#idx = BackMisc.AddSectorCount((62897.0555496, 5174.61166272, 20900.5),2,0)
#BackMisc.AddSectorDelete(idx, (62897.0555496, 5174.61166272, 20900.5))




#	VAMPIROS EN EL CEMENTERIO



BackMisc.HideEnemiesSector   ((66680.1315536, 4876.22838548, 3829.4))

BackMisc.AddVampireAppears   ((66680.1315536, 4876.22838548, 3829.4),(66680.1315536, 4876.22838548, 3829.4),0.1)
BackMisc.AddVampireAppears   ((66680.1315536, 4876.22838548, 3829.4),(65862.6529247, 4867.6954753, -3381.9),0.5)
#idx = BackMisc.AddSectorCount((66680.1315536, 4876.22838548, 3829.4),3,0)
#BackMisc.AddSectorDelete(idx, (66680.1315536, 4876.22838548, 3829.4))
#BackMisc.AddSectorDelete(idx, (66680.1315536, 4876.22838548, 3829.4))


BackMisc.HideEnemiesSector ((87452.5, 3930.7, 3064.0))
BackMisc.HideEnemiesSector ((87097.1, 3932.8, -2957.5))


BackMisc.ActivateSectorProcs()