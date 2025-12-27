#####################################################
#													
#													
#													
#	         S E R V E R I N I T . P Y 				
#													
#													
#													
#													
#####################################################


import Bladex
import CharStats
import Reference

Bladex.OpenDebugChannel("Salida")


# Carga los recursos comunes de los mapas
import CommonResources
CommonResources.Init()
execfile("../../Scripts/NetworkResources.py")

# empaquetado de objetos
import BODInit
BODInit.Init()

#
import PickInit
PickInit.Init()

import SolidMask
SolidMask.Init()

import Material
Material.Init()


#
# Sounds
#
import AniSound



#
# Animation events (needed before the biped stuff)
#
import anm_def
anm_def.Init()

#
# Sound for steps (needed before the biped stuff)
#
execfile("../../Scripts/NetStepSounds.py")


#
# Different kind of enemies. Should be called b4 creating ANY PersonEntity!
#
import Enemies
Enemies.Init()



#
# New animation system (biped) 
#
import Biped
Biped.Init()


#
# The sharing of whole sets of animations
#
import anm_conv
anm_conv.Init()



#
# To modify flags of animations 
#
import Anm_Mdf
Anm_Mdf.Init()


#
# To modify the movements of the camera
#
import AnmCameras
AnmCameras.Init()


#
# Particle Systems init
#
# CUIDADO! Valores definidos tambien en InitParticleSystems.py.
B_PARTICLE_GTYPE_COPY=0
B_PARTICLE_GTYPE_BLEND=1
B_PARTICLE_GTYPE_ADD=2
B_PARTICLE_GTYPE_MUL=3

import InitParticleSystems
InitParticleSystems.Init()


#
# Procedural textures
#
execfile("../../Scripts/AutoGenTextures.py")






#
# PJ Init
#
execfile("../../Scripts/NetPj.py")


#
# Scorer Data init
#
import NetScorer
NetScorer.ActivateScorer()

# Inicio del personaje y sus marcadores
char=Bladex.GetEntity("Player1")  #Por si acaso
char.Level=0
char.PartialLevel=0


#
# Timers
#
Bladex.CreateTimer("Timer60",1.0/60.0)
Bladex.CreateTimer("Timer30",1.0/30.0)
Bladex.CreateTimer("Timer15",1.0/15.0)


#
# Controls ( keyborad,mouse...) stuff
#
execfile("../../Scripts/InputInit.py")
execfile("../../Scripts/NetMode.py")

import acts
acts.InitBindings("Player1")

try:
  execfile("../../Config/Control.py")
  print "BladeInit -> Executed Control.py"
except:
  execfile("../../Scripts/DefControl.py")
  print "BladeInit -> Executed DefControl.py"



#
# Menu
#

import Menu
Menu.InitMenuKeys()


print "ServerInit.py executed"
import DefaultSelectionData