#############################################################
#															#
#	Bolas de la cueva que hay despues de las gemas			#
#															#
#############################################################

import stone
import heavyObjects
import darfuncs



###### Bola A

p=-39572,-23265,-38478
r=0.707107,0.707107,0.000000,0.000000
o=heavyObjects.CreateHeavyObject("UBolo1","BoladePiedra",p,r,1.0, heavyObjects.StoneHitEvent )
stone.lock( o.Name, stone.DROPBROWNDUST, 0, 1100, 0.0, 0.6, 20.0, stone.STONESOUND, 0.1 )






###### Bola B

p=-32287.947000,-17875.277000,-41247.597000
r=0.707107,0.707107,0.000000,0.000000
o=heavyObjects.CreateHeavyObject("UBolo2","BoladePiedra",p,r,1.0, heavyObjects.StoneHitEvent )
stone.lock( o.Name, stone.DROPBROWNDUST, 0, 1100, 0.0, 0.6, 20.0, stone.STONESOUND, 0.1 )



###### Bola A & B

bolasDropped=0

uDropSector=Bladex.GetSector(-28348.8001574, -248.598722686, -14807.511)
uDropSector.OnEnter=uDrop

TemblorMalditoTerror=Bladex.CreateSound("../../Sounds/Stone-floor-collapse.wav", "TemblorMalditoTerror")
TemblorMalditoTerror.Volume=1
TemblorMalditoTerror.MinDistance=10000
TemblorMalditoTerror.MaxDistance=40000
