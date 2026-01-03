import def_class
from math import pow
import EnemyTypes
import Bladex
import pdb
import Reference
import Actions
import Sounds

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
weapon3=Bladex.CreateEntity("PerkinsWeapon","Gladius",0,0,0,"Weapon")
#torch3=Bladex.CreateEntity("PerkinsTorch","Antorcha",0,0,0)
#torch3.Static=0
#torch3.FiresIntensity=[ 10.000000 ]
#torch3.Lights=[ (6.0,0.031250,(255,150,100)) ]

#8850
knt3=Bladex.CreateEntity("Perkins","Knight_Traitor",-75975.0274434, -6102.01979969, 53688.6007,"Person")
knt3.Level=0
knt3.Angle=4.2
Actions.TakeObject(knt3.Name,"PerkinsWeapon")
#Actions.TakeObject(knt3.Name,"PerkinsTorch")
#Actions.TakeObject(knt3.Name,"PerkinsBow")
#Actions.TakeObject(knt3.Name,"PerkinsQuiver")
knt3.ActionAreaMin=pow(2,12)
knt3.ActionAreaMax=pow(2,13)
knt3.SetOnFloor()
knt3.Data = def_class.SleepingKnight (knt3)

#char.Position=-73245.6576222, -1809.85386667, 39920.5233

