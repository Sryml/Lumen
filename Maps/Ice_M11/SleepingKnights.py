import def_class
from math import pow
import EnemyTypes
import Bladex
import pdb
import Reference
import Actions
import Sounds
import LevelFuncs

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 12
expected_player_lvl_max= 16

lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)

TRUE = 1==1
FALSE = not TRUE


	
#######################################################
# Create a  sleeping Knight
# (named after PERKINS in Meaning of Life, who gets his leg bitten off by mosquitos while he sleeps)
#######################################################
#bow3=Bladex.CreateEntity("PerkinsBow","Arco",0,0,0)
#bow3.Weapon=1
#quiver3=Bladex.CreateEntity("PerkinsQuiver","Carcaj",0,0,0)
#quiver3.Weapon=1
weapon3=Bladex.CreateEntity("IcePerkinsWeapon","Maza2",0,0,0)
weapon3.Weapon=1


#8850
knt3=Bladex.CreateEntity("Perkins","Knight_Traitor",-1165.91968748, -1112.39664744, 110137.42,"Person")
knt3.Angle=4.2
knt3.Level=lvl_control.GiveLevel(7,10)
Actions.TakeObject(knt3.Name,"IcePerkinsWeapon")
#knt3.ActionAreaMin=4
#knt3.ActionAreaMax=5
knt3.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(knt3)
knt3.Data = def_class.SleepingKnight (knt3)

#char.Position=-73245.6576222, -1809.85386667, 39920.5233

