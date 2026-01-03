#########################################################
#														#
# Escena inicial (volcano)								#
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
import AuxFuncs
import GameText
import Scorer



AuxFuncs.SingleFrameFade()
Scorer.SetVisible(0)





Bladex.AddScheduledFunc(Bladex.GetTime(),ParchePrecarga,())
#Bladex.AddScheduledFunc(Bladex.GetTime(), iSceneStart, ())


