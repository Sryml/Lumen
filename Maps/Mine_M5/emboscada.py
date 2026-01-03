import EnmGenRnd
import Actions
import Scorer
import LevelFuncs

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 1
expected_player_lvl_max= 6
lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)

SoundSalto=Sounds.CreateEntitySound('../../sounds/salto-inicio-orco.wav', 'SoundSalto')
SoundSalto.Volume = 1.0
SoundSalto.MinDistance=2000
SoundSalto.MaxDistance=30000

ambushork1 = EnmGenRnd.CreateEnemy((-122000,-14224,50904),"MineAmbushOrk1", "Ork", "Maza", 0, "Escudo2", 1, lvl_control.GiveLevel(3,5))
ambushork2 = EnmGenRnd.CreateEnemy((-115790,-15398,73057),"MineAmbushOrk2", "Ork", "Hacha", 0, "Escudo5", 1, lvl_control.GiveLevel(2,5))
ambushork3 = EnmGenRnd.CreateEnemy((-104955,-11495,77370),"MineAmbushOrk3", "Ork", "Gladius", 0, "Escudo1", 1, lvl_control.GiveLevel(4,6))







EmboscadaSec = Bladex.GetSector(-122215.932547,-10553.301563,63282.984978)
EmboscadaSec.OnEnter = StartEmboscada
