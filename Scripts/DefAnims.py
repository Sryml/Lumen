# Override this file by placing a DefAnims.py in each map.
# must define specific biped animations to be preloaded for each map
# Divide into functions by  biped.

# For each biped type with animations to be preloaded, create a
# function here with the biped name, that loads the animations
# and creates appropriate actions
#
# EXAMPLE (from the Chaos map):

#import Bladex
#
#def Ank():
#	Bladex.LoadSampledAnimation("../../Anm/Ank_final_02.BMV","Ank_final_02",0,"DarkLord")
#	Bladex.AddBipedAction("Ank","final_02","Ank_final_02",0.0,1.0,0)
#   etc....
