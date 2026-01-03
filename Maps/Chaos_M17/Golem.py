import darfuncs
import dust
import Actions
import Ontake
#############	Golem fall to kaos   ###########
#
#
#Glm_fall_kaos.bmv	(394936,-41304,-28343)
#
#
#/Dario\Public\Glm_fall_kaoscamera01	frames 0-165
#
#
#impacto en el suelo	Frame 39   (394876,-41250,-63480)
#

_OstiaGolem=Bladex.CreateSound("../../Sounds/deputamadre.wav","OstiaGolem")
_OstiaGolem.Volume=1
_OstiaGolem.MinDistance=20000
_OstiaGolem.MaxDistance=60000

Ontake.AddOnTakeEvent("Llavevamp", GolemVomitoso)

TheChapuzaSolution()
