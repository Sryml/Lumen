import BackMisc
import darfuncs


res=ReadGSFile.ReadGhostSectorFile("tablilla.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])


res=ReadGSFile.ReadGhostSectorFile("kaos.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])


Bladex.GetEntity("Player1").SendTriggerSectorMsgs=1



#
# CHAOS KNIGHT
#

BackMisc.CHAOS_KNIGHT_LEVEL       = 9
BackMisc.CHAOS_KNIGHT_POSITION    = 324859.027793, 2618.63785687, -40057.5148478
BackMisc.CHAOS_KNIGHT_ANGLE       = 0

BackMisc.EXEC_IN_PLAYER_APPEARING       = EnciendeMusicaInicio
BackMisc.EXEC_IN_CHAOS_KNIGHT_APPEARING = EnciendeMusicaApChaos

BackMisc.AddChaosDisappearsSector(295954, 6647, -56925)
BackMisc.AddChaosDisappearsSector(353808, 6632, -56742)

BackMisc.AddChaosDisappearsSector(325287, 1873, -87734)

BackMisc.AddChaosAppearsSector(316482.459967, 2613.94910583, -40013.2879891)
BackMisc.AddChaosAppearsSector(332144.315316, 2606.00047682, -39185.5481095)

BackMisc.PrepareChaosAppears()

darfuncs.EnterSecIdEvent("kaos",JodeteCaballeroDelCaosHijoDePuta)
darfuncs.EnterSecIdEvent("xtablilla",TieneTablilla)




## DEMONIOS Y VAMPIROS

BackMisc.AddVampires(2,(325499, -67, -169925),3)
BackMisc.AddVampires(2,(325499, -67, -169925),3)
BackMisc.AddVampires(4,(325499, -67, -169925),6)
BackMisc.AddVampires(4,(325499, -67, -169925),10)
BackMisc.AddVampires(4,(325499, -67, -169925),14)
BackMisc.AddDemons  (3,(325499, -67, -169925),3)
BackMisc.AddDemons  (4,(325499, -67, -169925),8)

## TWIN DEMONS IN THE SKY WITH DIAMONDS

BackMisc.HideEnemiesSector ((310083, -48, -188339))
BackMisc.HideEnemiesSector ((330976, 141, -180974))
BackMisc.HideEnemiesSector ((316618, -159, -167904))

BackMisc.HideEnemiesSector ((325375, 9, -173845))
BackMisc.AddDemonAppears   ((325375, 9, -173845),(325282, -118, -170968),0.0)
idx = BackMisc.AddSectorCount((325375, 9, -173845),3,0)
BackMisc.AddSectorDelete(idx, (325375, 9, -173845))
BackMisc.AddSectorDelete(idx, (325334, -69, -181620))


BackMisc.HideEnemiesSector ((325334, -69, -181620))
BackMisc.AddDemonAppears   ((325334, -69, -181620),(325779, -50, -183422),0.0)
idx = BackMisc.AddSectorCount((325334, -69, -181620),3,0)
BackMisc.AddSectorDelete(idx, (325375, 9, -173845))
BackMisc.AddSectorDelete(idx, (325334, -69, -181620))


## VAMPIRO EN LO ALTO DEL MINICASTILLO FUMANDOSE UN PETARDO

BackMisc.HideEnemiesSector ((335003, -2871, -165972))
BackMisc.HideEnemiesSector ((334870, -6109, -159000))
BackMisc.HideEnemiesSector ((313480, -6123, -155704))


BackMisc.HideEnemiesSector ((323782, 1657, -152604))
BackMisc.AddVampireAppears    ((321743, -6101, -161455),(321743, -6101, -161455),0.2)
idx = BackMisc.AddSectorCount ((321743, -6101, -161455),0,2)
BackMisc.AddSectorDelete(idx,  (321743, -6101, -161455))



## DEMONIOS EN PLAZA EXTERIOR EXIN CASTILLOS

# Sector de aparicion

BackMisc.HideEnemiesSector    ((325287, 1873, -87734))

BackMisc.HideEnemiesSector    ((342799, 2685, -156925))
BackMisc.HideEnemiesSector    ((319374, 1628, -146649))
BackMisc.AddDemonAppears      ((319374, 1628, -146649),(322388, 1688, -144453),0.0)
BackMisc.AddDemonAppears      ((319374, 1628, -146649),(325012, 1683, -149004),0.2)
idx = BackMisc.AddSectorCount ((319374, 1628, -146649),4,0)
BackMisc.AddSectorDelete(idx,  (319374, 1628, -146649))


##2 VAMPIROS MUY CERCA DEL ELEVADOR SECRETO.

BackMisc.HideEnemiesSector    ((349878, 1429, -148584))
BackMisc.HideEnemiesSector    ((354037, 8454, -129715))
BackMisc.AddVampireAppears    ((349878, 1429, -148584),(355132, 1440, -150242),0.0)
BackMisc.AddVampireAppears    ((349878, 1429, -148584),(344014, 1442, -148367),0.0)
idx = BackMisc.AddSectorCount ((349878, 1429, -148584),0,4)
BackMisc.AddSectorDelete(idx,  (349878, 1429, -148584))


## VAMPIROS CERCA DE CABALLERO KAOS 


BackMisc.HideEnemiesSector    ((317292, 2681, -39856))
BackMisc.HideEnemiesSector    ((333043, 2668, -40073))

BackMisc.HideEnemiesSector    ((338144, 13630, -39856))
BackMisc.HideEnemiesSector    ((313292, 13631, -39363))

BackMisc.AddVampireAppears    ((325287, 1873, -87734),(332446, 1904, -86061),0.0)
BackMisc.AddVampireAppears    ((325287, 1873, -87734),(317005, 1896, -85754),0.2)
idx = BackMisc.AddSectorCount ((325287, 1873, -87734),0,4)
BackMisc.AddSectorDelete(idx,  (325287, 1873, -87734))



BackMisc.ActivateSectorProcs()
