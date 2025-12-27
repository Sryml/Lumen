#####################################################
#
#
#
#	         B L A D E I N I T . P Y
#
#
#
#
#####################################################


import Bladex
import CharStats


Bladex.OpenDebugChannel("Salida")


# Carga los recursos comunes de los mapas
#execfile("../../Scripts/CommonResources.py") intento
Bladex.BodInspector()

##execfile("../../Scripts/PickInit.py")
#import PickInit intento
#PickInit.Init() intento

#execfile("../../Scripts/SolidMask.py")
#execfile("../../Scripts/material.py")


#
# Sounds
#
#execfile("../../Scripts/anisound.py")
# Player Races
from AniSoundKgt import *
from AniSoundBar import *
from AniSoundAmz import *
from AniSoundDwf import *



#
# Animation events (needed before the biped stuff)
#
execfile("../../Scripts/anm_def.py")


#
# Sound for steps (needed before the biped stuff)
#
#execfile("../../Scripts/StepSounds.py") intento2


#
# Different kind of enemies. Should be called b4 creating ANY PersonEntity!
#
#execfile("../../Scripts/enemies.py")



#
# New animation system (biped)
#
#execfile("../../Scripts/KgtBAct.py")
execfile("../../Scripts/Biped/Biped.py")


#
# The sharing of whole sets of animations
#
execfile("../../Scripts/anm_conv.py")




#
# To modify flags of animations
#
execfile("../../Scripts/anm_mdf.py")

#
# To modify the movements of the camera
#
execfile("../../Scripts/AnmCameras.py")



#
# Particle Systems init
#
execfile("../../Scripts/InitParticleSystems.py")


#
# Procedural textures
#
#execfile("../../Scripts/AutoGenTextures.py")






#
# PJ Init
#
execfile("pj.py")


#
# Scorer Data init
#
import Scorer
Scorer.ActivateScorer()

import CharStats

import PowDefWidgets
PowDefWidgets.CreateWidgest()
PowDefWidgets.Activate()

#import GameText
#GameText.SetLanguage("Spanish")

execfile("../../Scripts/DefaultScorerData.py")

# Inicio del personaje y sus marcadores
char=Bladex.GetEntity("Player1")  #Por si acaso
char.Level=0
char.PartialLevel=0
#Scorer.SetLevelLimits(0,CharStats.GetCharExperienceCost(char.CharType,0))
#Scorer.SetLevelBarValue(0)
#Scorer.SetLevelValue(0)


#
# Timers
#
Bladex.CreateTimer("Timer60",1.0/60.0)
Bladex.CreateTimer("Timer30",1.0/30.0)
Bladex.CreateTimer("Timer15",1.0/15.0)

#import pywin.debugger
#pywin.debugger.set_trace()


#
# Controls ( keyboard,mouse...) stuff
#
execfile("../../Scripts/InputInit.py")

import acts
acts.InitBindings("Player1")


try:
  execfile("../../Scripts/Control.py")
  print "BladeInit -> Executed Control.py"
except:
  execfile("../../Scripts/DefControl.py")
  print "BladeInit -> Executed DefControl.py"



#
# Menu
#
#execfile("../../Scripts/Menu.py")
import Menu
Menu.InitMenuKeys()
