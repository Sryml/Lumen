#########################################################
#														#
# Escena del final de la mina							#
#														#
# (Yuio)												#
#														#
#########################################################

import Bladex
import Sounds
import Scorer
import Reference
import Select
import Change
import Actions
import Bladex
import AuxFuncs
import GameText



esceneOrientation = 3.14*1.5
eScenePlayed=0


#char.Position = 79930.477, 23898.885, 33351.977



s = Bladex.GetSector(200000,30000, 8000)
s.OnEnter=eScenePrepare

