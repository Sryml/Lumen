import BackMisc
import darfuncs

res=ReadGSFile.ReadGhostSectorFile("back.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

res=ReadGSFile.ReadGhostSectorFile("tablilla.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])


Bladex.GetEntity("Player1").SendTriggerSectorMsgs=1

#
# CHAOS KNIGHT
#

BackMisc.CHAOS_KNIGHT_LEVEL       = 9
BackMisc.CHAOS_KNIGHT_POSITION    = 63877, -17870, -164579
BackMisc.CHAOS_KNIGHT_ANGLE       = 0

BackMisc.EXEC_IN_PLAYER_APPEARING       = EnciendeMusicaInicio
BackMisc.EXEC_IN_CHAOS_KNIGHT_APPEARING = EnciendeMusicaApChaos

BackMisc.AddChaosDisappearsSector(-20456, -17633, -161477)
BackMisc.AddChaosDisappearsSector(117537, -4884, -133142)


BackMisc.AddChaosAppearsSector(56570, -17876, -164781)
BackMisc.AddChaosAppearsSector(68561, -17880, -164103)

BackMisc.PrepareChaosAppears()

BackMisc.AddChaosDeactivationTs("tablilla")

darfuncs.EnterSecIdEvent("tablilla",TieneTablilla)

## DEMONIOS Y VAMPIROS

BackMisc.AddVampires(2,(-20456, -17633, -161477),3)
BackMisc.AddVampires(2,(-20456, -17633, -161477),3)
BackMisc.AddVampires(4,(-20456, -17633, -161477),6)
BackMisc.AddVampires(4,(-20456, -17633, -161477),10)
BackMisc.AddVampires(4,(-20456, -17633, -161477),14)
BackMisc.AddDemons  (3,(-20456, -17633, -161477),3)
BackMisc.AddDemons  (4,(-20456, -17633, -161477),8)

## DEMONIO INICIAL FRENTE A TERCER RECORRIDO

BackMisc.HideEnemiesSector ((-29097, -31139, -5496))
BackMisc.HideEnemiesSector ((-31000,-30000,-64000))


BackMisc.AddDemonAppears   ((-31373, -31127, -36959),(-31373, -31127, -36959),0.1)
idx = BackMisc.AddSectorCount((-31373, -31127, -36959),3,0)
BackMisc.AddSectorDelete(idx, (-31373, -31127, -36959))

## VAMPIRO ANTES DE ELEVADORES


BackMisc.HideEnemiesSector ((-31000,-20000,-100000))

BackMisc.AddVampireAppears   ((-31559, -26132, -94418),(-31559, -26132, -94418),0.1)
idx = BackMisc.AddSectorCount((-31559, -26132, -94418),3,0)
BackMisc.AddSectorDelete(idx, (-31559, -26132, -94418))


## VAMPIRO SIGUIENTE

BackMisc.HideEnemiesSector ((-31500,-17000,-159875))

BackMisc.HideEnemiesSector    ((-31486, -18868, -130601))
BackMisc.AddVampireAppears    ((-31486, -18868, -130601),(-31486, -18868, -130601),0.1)
idx = BackMisc.AddSectorCount ((-31486, -18868, -130601),0,2)
BackMisc.AddSectorDelete(idx,  (-31486, -18868, -130601))


## GRUPO PRIMERO DE VAMPIROS Y DEMONIOS CERCA CABALLERO KAOS


BackMisc.HideEnemiesSector ((-21000,-18000,-161000))
BackMisc.HideEnemiesSector ((56570, -17876, -164781))

BackMisc.HideEnemiesSector ("back1")
BackMisc.AddDemonAppears   ("back1",(-4000,-17535,-150000),0.1)
BackMisc.AddDemonAppears   ("back1",(0,-17535,-150000),0.3)
BackMisc.AddSectorCount("back1",  3,0)
BackMisc.AddSectorDelete("back1", "back1")

##GRUPO SEGUNDO DE BLA BLA BLA


BackMisc.HideEnemiesSector ("back2")
BackMisc.AddDemonAppears   ("back2",(16000,-17535,-158000),0.1)
BackMisc.AddDemonAppears   ("back2",(22000,-17535,-161000),0.3)
BackMisc.AddSectorCount("back2",  3,0)
BackMisc.AddSectorDelete("back2", "back2")

BackMisc.ActivateSectorProcs()
