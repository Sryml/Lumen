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
import Bladex
import stone
import Sounds
import heavyObjects
import darfuncs








p=34214.943107,-20636.895016,-40838.978828
r=0.707107,0.707107,0.000000,0.000000
o=heavyObjects.CreateHeavyObject("IJBolon1","BoladePiedra",p,r,1.0, heavyObjects.StoneHitEvent )
stone.lock( "IJBolon1", stone.DROPBROWNDUST, 0, 1100, 0.0, 0.2, 20.0, stone.STONESOUND, 0.1 ) 

stoneADropped=0
		
stoneASector=Bladex.GetSector(41000,-12000,-17500)
stoneASector.OnEnter=dropStoneA










p=87306.063982,-33471.519948,-62045.250521
r=0.707107,0.707107,0.000000,0.000000
o=heavyObjects.CreateHeavyObject("IJBolon2","BoladePiedra",p,r,1.0, heavyObjects.StoneHitEvent )
stone.lock( "IJBolon2", stone.DROPBROWNDUST, 0, 1100, 0.0, 0.2, 20.0, stone.STONESOUND, 0.1 ) 

stoneBDropped=0

stoneBSector=Bladex.GetSector(74000,-20000,-83000)
stoneBSector.OnEnter=dropStoneB

