#########################################################
#														#
# Bolones a lo Indiana Jones			(en 2 sitios)	#
#														#
# (Yuio)												#
#														#
#########################################################

import Reference
import Select
import Change
import Actions
#import AniSound
import Sounds
import stone
import heavyObjects


p=36539.218000,36733.727000,12312.250000
r=0.707107,0.707107,0.000000,0.000000
o=heavyObjects.CreateHeavyObject("IJBolon1","BoladePiedra",p,r,0.960980, heavyObjects.StoneHitEvent )
stone.lock( "IJBolon1", stone.DROPBROWNDUST, 0, 960, 0.0, 0.6, 20.0, stone.STONESOUND, 0.1 ) 

stoneADropped=0

stoneASector=Bladex.GetSector(40000,0,38500) ; stoneASector.OnEnter=dropStoneA
