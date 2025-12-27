

# Carga los recursos comunes de los mapas
import CommonResources
CommonResources.Init()

import InitParticleSystems
InitParticleSystems.Init()


import BODInit
BODInit.Init()


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
import StepSounds
StepSounds.Init()
