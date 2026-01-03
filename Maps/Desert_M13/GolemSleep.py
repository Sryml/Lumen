import ReadGSFile
import EnmGenRnd
import AuxFuncs
import darfuncs
import LevelFuncs

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 9
expected_player_lvl_max= 16

lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)

o=Bladex.CreateEntity("WaterGolem","Entity Water",-25000,10500,54000)
o.Reflection=-1
o.Color=0,0,0

DespWater = 3000.0 / (20.0 * 60.0)
DespReja = 3000.0 / (15.0 * 60.0)
AlturaWater = 11500
golem_sleep = 1


generadorCueva = EnmGenRnd.CreateEnemiesGenerator(4, 1)



Bladex.AddCombustionDataFor("Skeleton", "Fire", 250, 400, 4, 1, 3, 144000) # se extingira en 40 horas!	

generadorCueva.CallBak = CreaSkeletoLlamarada
generadorCueva.VirGenPos = -25191, 9323, 39929
generadorCueva.AddPoint((-25174, 10300, 40135), ("M13Gen666Skl__5", "Skeleton", "HookSword"	, 0, "Escudo4", 1, lvl_control.GiveLevel(10,12)), "Skl_appears1")
generadorCueva.AddPoint((-25174, 10300, 40135), ("M13Gen666Skl__6", "Skeleton", "HookSword"	, 0, "Escudo4", 1, lvl_control.GiveLevel(11,13)), "Skl_appears1")
generadorCueva.AddPoint((-25174, 10300, 40135), ("M13Gen666Skl__7", "Skeleton", "Martillo"	, 0, "Escudo4", 1, lvl_control.GiveLevel(12,14)), "Skl_appears1")
generadorCueva.AddPoint((-25174, 10300, 40135), ("M13Gen666Skl__8", "Skeleton", "Espadacurva"	, 0, "Escudo4", 1, lvl_control.GiveLevel(13,15)), "Skl_appears1")


generadorCueva.InitGenFunc = SaltaTierraGen
generadorCueva.DifTime = 1.6
generadorCueva.Activate()
generadorCueva.OnEnd = GolemMuerto

GolemSector1 = Bladex.GetSector(-25000,5000,44500)
GolemSector1.OnEnter = GolemWakeUp

GolemSector2 = Bladex.GetSector(-25000,5000,48000)
GolemSector2.OnEnter = GolemWakeUp