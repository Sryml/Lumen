#########################################################
#														#
# PALACE												#
#														#
# escenita del ejercito 1								#
#														#
# (Yuio)												#
#														#
#########################################################

import Bladex
import Sounds
import Reference
import Select
import Actions
import AuxFuncs
import GameText
import Scorer
import Sparks
import EnemyTypes
import math
import darfuncs
palaceSecA = Bladex.GetSector(-16858,2481,58976)
palaceSecB = Bladex.GetSector(-16862,2831,56691)

palaceSecA.Active=0
palaceSecB.Active=0

# A: char.Position = 69703.2091799, 2453.2, 48054.4921726

#Bladex.LoadSampledAnimation("../../Anm/Ork_ejercito4.BMV","Ork_ejercito4",1,"Ork")
#Bladex.LoadSampledAnimation("../../Anm/Ork_ejercito5.BMV","Ork_ejercito5",1,"Ork")
#Bladex.LoadSampledAnimation("../../Anm/Gor_ejercito6.BMV","Gor_ejercito6",1,"Great_Ork")
#Bladex.LoadSampledAnimation("../../Anm/Ork_ejercito7.BMV","Ork_ejercito7",1,"Ork")
#Bladex.LoadSampledAnimation("../../Anm/Ork_ejercito8.BMV","Ork_ejercito8",1,"Ork")


essSceneACreateX()


essSceneALaunched=0
