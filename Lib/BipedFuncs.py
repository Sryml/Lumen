import Bladex
import math

#
#
#
#

def AutoLinkAttack(biped_name,anm_name):
    Bladex.AddBipedAction(biped_name,anm_name[4:],anm_name,0.0,1.0,0)	
    Bladex.SetActionEventTable(biped_name,anm_name[4:],"ATTACKING")	





