#
#
# File to create the specific behaviour related to the race the character belongs to
#
#

import Bladex


#
# Orc
#
def AuxTranOrc(EntityName):
	me=Bladex.GetEntity(EntityName)
	"""
	if me.Gof and me.Slow and me.BayRoute:
		if me.StatL(me.Name)==1:
			me.LaunchAnmnType("patrol_wlk_t")
		else:
			me.LaunchAnmType("patrol_wlk_1h")
	"""

#
# KightLivingDead
#
def AuxTranKnightLivingDead(EntityName):
	me=Bladex.GetEntity(EntityName)
	"""
	if me.Gof and me.Slow and me.BayRoute:
		if me.StatL==1:
			me.LaunchAnmnType("patrol_wlk_t")
		else:
			me.LaunchAnmType("patrol_wlk_1h")
	"""
