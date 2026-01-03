import Bladex
import Actions
import EnemyTypes
import ItemTypes
import AniSound
import Reference
import Damage
import Scorer
import GameText


LifeLimit = 250
tLaunched = 0

	
	
Drakula=""
	

CreateDrakula("X")
CreateDrakula()

import pdb

"""
# interface con la huida
def Chau_Bolu():
	print "Huye el cabron."
"""



# execfile("vamp_cool.py")
# execfile("objs.py")
# char.Position = (-41000,-58000,25000)
# tLaunched = 1


VampSector = Bladex.GetSector(-41000,-58000,25000)
VampSector.OnEnter = AparicionVampiro