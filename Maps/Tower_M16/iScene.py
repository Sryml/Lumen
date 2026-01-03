#########################################################
#														#
# TORRE											#
#														#
# escenita del inicio									#
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

# char.Position = 124966.34 , 12381.45 , 52814.45

AuxFuncs.SingleFrameFade()
Scorer.SetVisible(0)


iCharPosition	        = 124966 , 13077 , 52814
iCharAngle		= 3.14159  # correcion del angulo inicial

char.Freeze()
Bladex.AddScheduledFunc(Bladex.GetTime(), ParchePrecarga, ())
