#########################################################
#														#
# VOLCANO												#
#														#
# minotauro que esta zampando y luego ataca				#
#														#
# (Yuio)												#
#														#
#########################################################

import Bladex
import Sounds
import Reference
import Select
import Change
import Actions
import Bladex
import AuxFuncs

#char.Position = -36412, 3000, 25200

minOut=0
minInAttack=0


mzInitSector = Bladex.GetSector(-17338,-13164,18999)
mzInitSector.OnEnter= mzMinAppears

mzAttackSector = Bladex.GetSector(-27000,-13900,5800)
mzAttackSector.OnEnter= mzMinAttacks
