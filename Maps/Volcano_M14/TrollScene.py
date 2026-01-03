import EnemyTypes
import Bladex
import Sounds
import Reference
import Actions
import AuxFuncs
import EnmGenRnd
import darfuncs
import AbreCam
import LevelFuncs

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 12
expected_player_lvl_max= 16

lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)

trollga=Bladex.CreateEntity("VolcaGarrote","Hachacarnicero",0,0,0,"Weapon")
trollazo=Bladex.CreateEntity("TrollMarica","Troll_Dark",-35219,-9475,43378,"Person")
trollazo.Angle = 3.1415/2
trollazo.Level=lvl_control.GiveLevel(6,10)
Actions.TakeObject(trollazo.Name,trollga.Name)
EnemyTypes.EnemyDefaultFuncs(trollazo)
darfuncs.HideBadGuy(trollazo.Name)

darfuncs.EnterSecEvent(-42100,-9600,32600,IniciaTrollScene)