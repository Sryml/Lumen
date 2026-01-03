import Bladex
import BackMisc
import darfuncs
import ReadGSFile




res=ReadGSFile.ReadGhostSectorFile("enemigos.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])


Bladex.GetEntity("Player1").SendTriggerSectorMsgs=1



################
# CHAOS KNIGHT #
################

### Funcion: EnciendeMusicaInicio()

### Funcion: EnciendeMusicaApChaos()


BackMisc.CHAOS_KNIGHT_LEVEL             = 9
BackMisc.CHAOS_KNIGHT_POSITION          = -2000, 0, -48000
BackMisc.CHAOS_KNIGHT_ANGLE             = 0
BackMisc.TIME_BEFORE_PLAYER_APPEARING   = 4.0
BackMisc.EXEC_IN_PLAYER_APPEARING       = EnciendeMusicaInicio
BackMisc.EXEC_IN_CHAOS_KNIGHT_APPEARING = EnciendeMusicaApChaos

BackMisc.AddChaosAppearsTSector("ApChaosKnight")

BackMisc.AddChaosDisappearsTSector("DesChaosKnight1")
BackMisc.AddChaosDisappearsTSector("DesChaosKnight2")
BackMisc.AddChaosDisappearsTSector("DesChaosKnight3")
BackMisc.AddChaosDisappearsTSector("DesChaosKnight4")
BackMisc.AddChaosDisappearsTSector("DesChaosKnight5")

BackMisc.PrepareChaosAppears()



#######################
# DEMONIOS Y VAMPIROS #
#######################


BackMisc.AddDemons  (3,(0, -19000, 11000),3)	# 12 demonios
BackMisc.AddDemons  (3,(0, -19000, 11000),6)
BackMisc.AddDemons  (6,(0, -19000, 11000),8)
BackMisc.AddVampires(2,(0, -19000, 11000),3)	# 14 vampiros
BackMisc.AddVampires(2,(0, -19000, 11000),5)
BackMisc.AddVampires(2,(0, -19000, 11000),7)
BackMisc.AddVampires(4,(0, -19000, 11000),10)
BackMisc.AddVampires(4,(0, -19000, 11000),14)

BackMisc.HideEnemiesSector("Hide1")
BackMisc.HideEnemiesSector("Hide2")
BackMisc.HideEnemiesSector("Hide3")
BackMisc.HideEnemiesSector("Hide4")
BackMisc.HideEnemiesSector("Hide5")
BackMisc.HideEnemiesSector("Hide6")
BackMisc.HideEnemiesSector("Hide7")
BackMisc.HideEnemiesSector("Hide8")
BackMisc.HideEnemiesSector("Hide9")
BackMisc.HideEnemiesSector("Hide10")
BackMisc.HideEnemiesSector("Hide11")
BackMisc.HideEnemiesSector("Hide12")
BackMisc.HideEnemiesSector("Hide13")
BackMisc.HideEnemiesSector("Hide14")
BackMisc.HideEnemiesSector("Hide15")
BackMisc.HideEnemiesSector("Hide16")
BackMisc.HideEnemiesSector("Hide17")
BackMisc.HideEnemiesSector("Hide18")
BackMisc.HideEnemiesSector("Hide19")
BackMisc.HideEnemiesSector("Hide20")
BackMisc.HideEnemiesSector("Hide21")
BackMisc.HideEnemiesSector("Hide22")
BackMisc.HideEnemiesSector("Hide23")
BackMisc.HideEnemiesSector("Hide24")
BackMisc.HideEnemiesSector("Hide25")
BackMisc.HideEnemiesSector("Hide26")
BackMisc.HideEnemiesSector("Hide27")
BackMisc.HideEnemiesSector("Hide28")
BackMisc.HideEnemiesSector("Hide29")
BackMisc.HideEnemiesSector("Hide30")
BackMisc.HideEnemiesSector("Hide31")
BackMisc.HideEnemiesSector("ApLdm3")
BackMisc.HideEnemiesSector("ApLdm4")
BackMisc.HideEnemiesSector("ApLdm5")
BackMisc.HideEnemiesSector("ApLdm6")

BackMisc.AddDemonAppears  ("ApLdm1", (-42500,0,0), 0.1)
BackMisc.AddSectorCount   ("ApLdm1", 2, 0)
BackMisc.AddSectorDelete  ("ApLdm1", "ApLdm1")
BackMisc.AddSectorDelete  ("ApLdm1", "Hide6")
BackMisc.AddSectorDelete  ("ApLdm1", "Hide19")

BackMisc.AddDemonAppears  ("ApLdm2", (43000,0,5000), 0.1)
BackMisc.AddSectorCount   ("ApLdm2", 2, 0)
BackMisc.AddSectorDelete  ("ApLdm2", "ApLdm2")
BackMisc.AddSectorDelete  ("ApLdm2", "Hide7")
BackMisc.AddSectorDelete  ("ApLdm2", "Hide20")

BackMisc.AddDemonAppears  ("ApLdm3", (-39500,0,-23000), 0.1)
BackMisc.AddSectorCount   ("ApLdm3", 2, 0)
BackMisc.AddSectorDelete  ("ApLdm3", "ApLdm3")
BackMisc.AddSectorDelete  ("ApLdm3", "Hide21")

BackMisc.AddDemonAppears  ("ApLdm4", (-34500,0,-27500), 0.1)
BackMisc.AddSectorCount   ("ApLdm4", 2, 0)
BackMisc.AddSectorDelete  ("ApLdm4", "ApLdm4")
BackMisc.AddSectorDelete  ("ApLdm4", "Hide23")

BackMisc.AddDemonAppears  ("ApLdm5", (43500,0,-18500), 0.1)
BackMisc.AddSectorCount   ("ApLdm5", 2, 0)
BackMisc.AddSectorDelete  ("ApLdm5", "ApLdm5")
BackMisc.AddSectorDelete  ("ApLdm5", "Hide22")

BackMisc.AddDemonAppears  ("ApLdm6", (38500,0,-25000), 0.1)
BackMisc.AddSectorCount   ("ApLdm6", 2, 0)
BackMisc.AddSectorDelete  ("ApLdm6", "ApLdm6")
BackMisc.AddSectorDelete  ("ApLdm6", "Hide24")

BackMisc.AddVampireAppears("ApVmp1", (-10500,0,44500), 0.1)
BackMisc.AddSectorCount   ("ApVmp1", 2, 0)
BackMisc.AddSectorDelete  ("ApVmp1", "ApVmp1")
BackMisc.AddSectorDelete  ("ApVmp1", "Hide4")

BackMisc.AddVampireAppears("ApVmp2", (10500,0,44500), 0.1)
BackMisc.AddSectorCount   ("ApVmp2", 2, 0)
BackMisc.AddSectorDelete  ("ApVmp2", "ApVmp2")
BackMisc.AddSectorDelete  ("ApVmp2", "Hide5")

BackMisc.AddVampireAppears("ApVmp3", (-57000,-8000,0), 0.1)
BackMisc.AddSectorCount   ("ApVmp3", 2, 0)
BackMisc.AddSectorDelete  ("ApVmp3", "ApVmp3")

BackMisc.AddVampireAppears("ApVmp4", (57000,-8000,0), 0.1)
BackMisc.AddSectorCount   ("ApVmp4", 2, 0)
BackMisc.AddSectorDelete  ("ApVmp4", "ApVmp4")

BackMisc.AddVampireAppears("ApVmp5", (-18500,0,-55500), 0.1)
BackMisc.AddSectorCount   ("ApVmp5", 3, 0)
BackMisc.AddSectorDelete  ("ApVmp5", "ApVmp5")

BackMisc.AddVampireAppears("ApVmp6", (18500,0,-55500), 0.1)
BackMisc.AddSectorCount   ("ApVmp6", 3, 0)
BackMisc.AddSectorDelete  ("ApVmp6", "ApVmp6")


BackMisc.ActivateSectorProcs()
