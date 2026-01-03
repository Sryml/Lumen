#########################################################
#														#
# ISLA												#
#														#
# escenita del mural						#
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
import OnInitTake
import GameText
import Scorer

# char.Position = -27602.893,-57360.297,40259.102

tCharAngle=((180.0+172.378)*3.14*2.0)/360.0


tLaunched = 0

tSector = Bladex.GetSector(-28000,-60000,42000)
tSector.OnEnter = tLaunch
