import darfuncs
import EnmGenRnd
import LevelFuncs

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 7
expected_player_lvl_max= 16

lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)

generadorT1 = EnmGenRnd.CreateEnemiesGenerator(10, 2)
generadorT1.VirGenPos = 1006.22407132, -1105.16892958, 7012.1725020

generadorT1.AddPoint((10000,500 ,13500),("Gen1Skl_1", "Skeleton", "Hacha4", 0, "Escudo2", 1), "Skl_appears1", lvl_control.GiveLevel(8,11))
generadorT1.AddPoint((10000,500 ,250),  ("Gen1Skl_2", "Skeleton", "Hacha3", 0, "Escudo1", 1), "Skl_appears1", lvl_control.GiveLevel(9,12))
generadorT1.AddPoint((27500,500 ,13000),("Gen1Skl_3", "Skeleton", "Martillo", 0, "Escudo1", 1), "Skl_appears1", lvl_control.GiveLevel(10,13))
generadorT1.AddPoint((23000,500 ,3950),("Gen1Skl_4", "Skeleton", "HookSword", 0, "Escudo4", 1), "Skl_appears1", lvl_control.GiveLevel(12,14))
generadorT1.AddPoint((25000,500,12000),("Gen1Skl_5", "Skeleton", "Hacha4", 0, "Escudo2", 1), "Skl_appears1", lvl_control.GiveLevel(12,14))
generadorT1.AddPoint((15000,500,12000),("Gen1Skl_6", "Skeleton", "Hacha3", 0, "Escudo1", 1), "Skl_appears1", lvl_control.GiveLevel(12,14))


generadorT1.InitGenFunc=SaltaNieveGen
generadorT1.FinishGenFunc=Abrepuerta11
generadorT1.DifTime = 0.6

generadorT1.Activate()

darfuncs.EnterSecEvent(22700.3411219, -1000.75921151, -200.773186,generadorT1.GenerateEnemy)