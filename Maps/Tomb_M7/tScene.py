
##########################################################
#
#                      T O M B
#
#		 Escenita de la Reina
#
#		 (Yuio)
#
##########################################################


import Bladex
import Sounds
import Reference
import Select
import Change
import Actions
import Bladex
import AuxFuncs
import OnInitTake
import GameText
import Ontake
import Scorer
import Reference
import darfuncs
import ItemTypes

#Reference.DefaultSelectionData['Lapidareina']=(3.0,5000.0,"Gravestone")

# char.Position = 19286.461 , 6356.724, 416.216

_SndPiedra=Bladex.CreateSound("../../Sounds/m-mov-lapida.wav","Piedrus")
_SndPiedra.MaxDistance=1000000.0

_SndPiedraHit=Bladex.CreateSound("../../Sounds/caida-lapida.wav","SndPiedraHit")
_SndPiedraHit.MaxDistance=1000000.0

TUMBA_ESFUERZO1 = 182.0/20.0
TUMBA_ESFUERZO2 = 239.0/20.0

#tLapida=Bladex.CreateEntity( "tLapida","Lapidareina",19001.373, 6538, -1468.783 )
#darfuncs.SetHint(tLapida,"Gravestone")
#Reference.EntitiesSelectionData["Lapidareina"]=(9,5000.0,"Gravestone")

#tLapida.RotateRel(0,0,0,0,1,0,1.57)
#tLapida.RotateRel(0,0,0,0,1,0,-1.57)

#tLapida.RotateRel(0,0,0,1,0,0,1.57)
#tLapida.Static=1
#tLapida.Scale=1.220190


tCharAngle=((180.0+0)*3.14*2.0)/360.0



#tGPointerUsed=0

#tLapida.UseFunc = tGPointerInUse

Qo=Bladex.CreateEntity("Qo","QueenSword",19124.809000,7393.641000,-1478.599000,"Weapon")
Qo.Orientation=0.708658,-0.024863,-0.698539,-0.096066
ItemTypes.ItemDefaultFuncs (Qo)
Ontake.AddOnTakeEvent("Qo",fundido)
