import BackMisc
import darfuncs

res=ReadGSFile.ReadGhostSectorFile("back.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

res=ReadGSFile.ReadGhostSectorFile("xtablilla.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

Bladex.GetEntity("Player1").SendTriggerSectorMsgs=1


# CHAOS KNIGHT


BackMisc.CHAOS_KNIGHT_LEVEL       = 9
BackMisc.CHAOS_KNIGHT_POSITION    = 35721, -1121, 21827
BackMisc.CHAOS_KNIGHT_ANGLE       = 0

BackMisc.EXEC_IN_PLAYER_APPEARING       = EnciendeMusicaInicio
BackMisc.EXEC_IN_CHAOS_KNIGHT_APPEARING = EnciendeMusicaApChaos


BackMisc.AddChaosDisappearsSector(44630, -5866, 38163)
BackMisc.AddChaosDisappearsSector(-6745, -819, 21629)
BackMisc.AddChaosDisappearsTSector("xtablilla")

BackMisc.AddChaosAppearsTSector("back5")

BackMisc.PrepareChaosAppears()

BackMisc.AddChaosDeactivationTs("xtablilla")

darfuncs.EnterSecIdEvent("xtablilla",TieneTablilla)

## DEMONIOS Y VAMPIROS

BackMisc.AddVampires(2,(18874,-3447,54971),3)
BackMisc.AddVampires(4,(18874,-3447,54971),6)
BackMisc.AddVampires(4,(18874,-3447,54971),10)
BackMisc.AddVampires(4,(18874,-3447,54971),14)
BackMisc.AddDemons  (3,(18874,-3447,54971),3)
BackMisc.AddDemons  (4,(18874,-3447,54971),8)

## DEMONIO INICIAL
BackMisc.HideEnemiesSector  ("back0")
BackMisc.HideEnemiesSector ((8130, -1318, 75651))
BackMisc.HideEnemiesSector ("back00")
BackMisc.AddDemonAppears   ("back00",(-18670, 493, 75768),0.0)
BackMisc.AddSectorCount("back00",3,0)
BackMisc.AddSectorDelete("back00", "back00")

## DEMONIO 2



BackMisc.HideEnemiesSector("back2")
BackMisc.HideEnemiesSector("back1")
BackMisc.AddDemonAppears("back1",(-18580, 490, 62500),0.0)
BackMisc.AddSectorCount("back1",  3,0)
BackMisc.AddSectorDelete("back1", "back1")

## DEMONIO 3


BackMisc.HideEnemiesSector ((-18670, 493, 75768))

BackMisc.AddDemonAppears   ("back2",(-18595, 484, 39505),0.0)
BackMisc.AddSectorCount("back2",  3,0)
BackMisc.AddSectorDelete("back2", "back2")


## VAMPIRO 1 EN PUERTA


BackMisc.HideEnemiesSector ("back3")
BackMisc.AddVampireAppears   ("back3",(-12810, -419, 21936),0.0)
BackMisc.AddSectorCount("back3",  3,0)
BackMisc.AddSectorDelete("back3", "back3")


## VAMPIROS 2 Y 3 EN PUERTA

BackMisc.HideEnemiesSector ("back5")
BackMisc.HideEnemiesSector ("back4")
BackMisc.AddVampireAppears   ("back4",(7000, -1136, 21000),0.0)
BackMisc.AddVampireAppears   ("back4",(9000, -1117, 23000),0.2)
BackMisc.AddSectorCount("back4",  3,0)
BackMisc.AddSectorDelete("back4", "back4")






## DEMONIO AL OTRO LADO DE LA PUERTA


BackMisc.HideEnemiesSector ("back7")
BackMisc.AddDemonAppears   ("back6",(-18550, -615, 6321),0.0)
BackMisc.AddSectorCount("back6",  3,0)
BackMisc.AddSectorDelete("back6", "back6")


## ULTIMO DEMONIO

BackMisc.HideEnemiesSector ("back8")
BackMisc.AddDemonAppears   ("back7",(-15765, -600, -13532),0.0)
BackMisc.AddSectorCount("back7",  3,0)
BackMisc.AddSectorDelete("back7", "back7")

BackMisc.ActivateSectorProcs()
