#########################################################
#														#
# DIOSA													#
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

AuxFuncs.SingleFrameFade()
Scorer.SetVisible(0)


# char.Position = 7385.668, 4181.109,-59097.988

iCharPosition	= 7385.668, 4181.109,-59097.988
iCharAngle=2.00
#iCharAngle		= -59.154	# viva rollon!! que no me ha dado el angulo y luego me lo ha dado mal
#iCharAngle		= ((180.0+tCharAngle)*3.14*2.0)/360.0  # correcion del angulo inicial


iLaunched = 0

Bladex.AddScheduledFunc(Bladex.GetTime(), ParchePrecarga, ())
#Bladex.AddScheduledFunc(Bladex.GetTime(), iLaunch, ())
