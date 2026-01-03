#########################################################
#														#
# Escena del mural de los orcos#
#														#
# (Fernando)												#
#														#
#########################################################

import Bladex
import Sounds

import Reference
import Select
import Change
import Actions
import Bladex
import AuxFuncs
import GameText
import Scorer

esceneOrientation = 3.14*0.5
eScenePlayed=0

############### funcion que utiliza ghpointer ###################3
muralleido=0
	
############## ghost pointer ########################3
p=Bladex.CreateEntity("Ghpmural","GhostPointer",-19500,35800,20250)
p.Static=0
p.Scale=0.100000
p.Orientation=0.681583,0.038276,-0.023801,-0.730351
p.UseFunc = useInGhostMural	# cambiar funcion 
darfuncs.SetHint(p,"Mural")


#s = Bladex.GetSector(-5500,17000, 36750)
#s.OnEnter=eScenePrepare

