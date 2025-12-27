################################################################################
# LevelFuncs.py                                                                #
################################################################################
import Bladex
import CharStats

class EnemyLevelControl:
	"""Enemy Level Control Class \
	Used for adjusting enemy levels, based on how well the player is doing \
	against designer expectations for this map.  Normally to be instantiated \
	during map creation, all further enemies created can have their level \
	adjusted according to how well the player was doing in the moment of the \
	control creation.  Syntax for creation is: \
		lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max) \
	then later replace calls like... \
		enemy.Level= 9 \
	with \
		enemy.Level= lvl_control.GiveLevel (8, 10) \
	"""
	
	progression_factor= 0.0
	     
	def __init__(self, expected_player_lvl_min, expected_player_lvl_max):		
		player= Bladex.GetEntity ("Player1")
		try:
			LevelLimit= 1.0*CharStats.GetCharExperienceCost(player.CharType, player.Level)
			adjusted_player_lvl= player.Level + player.PartialLevel/LevelLimit
			adjusted_player_lvl= max (adjusted_player_lvl, 1.0*expected_player_lvl_min)
			adjusted_player_lvl= min (adjusted_player_lvl, 1.0*expected_player_lvl_max)
			self.progression_factor= (adjusted_player_lvl-expected_player_lvl_min) / (expected_player_lvl_max-expected_player_lvl_min)
		except:
			print "!!!Error!!! initializing EnemyLevelControl.  Probable cause: Player1 not accessible"

	def GiveLevel (self, enemy_lvl_min, enemy_lvl_max):
		return round ((enemy_lvl_max-enemy_lvl_min)*self.progression_factor+enemy_lvl_min)
