import EnmGenRnd
import darfuncs
import LevelFuncs

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 7
expected_player_lvl_max= 16

lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)

generadorT2 = EnmGenRnd.CreateEnemiesGenerator(10, 2)
generadorT2.VirGenPos = 1006.22407132, -1105.16892958, 7012.1725020

generadorT2.AddPoint((27700,500 ,32800),("Gen1Skl_11", "Skeleton", "Maza2", 0, "Escudo2", 1), "Skl_appears1",lvl_control.GiveLevel(9,11))
generadorT2.AddPoint((27900,500 ,40500),  ("Gen1Skl_22", "Skeleton", "Martillo", 0, "Escudo1", 1), "Skl_appears1", lvl_control.GiveLevel(10,12))
generadorT2.AddPoint((4000,500 ,33300),("Gen1Skl_33", "Skeleton", "HookSword", 0, "Escudo4", 1), "Skl_appears1", lvl_control.GiveLevel(11,13))
generadorT2.AddPoint((11000,500 ,34050),("Gen1Skl_44", "Skeleton", "HookSword", 0, "Escudo4", 1), "Skl_appears1", lvl_control.GiveLevel(12,14))
generadorT2.AddPoint((8400,500,40000),("Gen1Skl_45", "Skeleton", "Maza2", 0, "Escudo2", 1), "Skl_appears1", lvl_control.GiveLevel(12,14))
generadorT2.AddPoint((32000,500,35000),("Gen1Skl_46", "Skeleton", "Martillo", 0, "Escudo1", 1), "Skl_appears1", lvl_control.GiveLevel(12,14))



generadorT2.InitGenFunc=SaltaNieveGen
generadorT2.DifTime = 0.6

generadorT2.Activate()

darfuncs.EnterSecEvent(12700.3411219, -1000.75921151, 30000.773186,generadorT2.GenerateEnemy)