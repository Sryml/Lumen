import Bladex
import darfuncs
import EnemyTypes
import Actions
import Language

ORCO_GORDO_TYPE = "Dark_Knight"
###########################################

language = Language.CheckFallback()

# primera posicion en sala inicial
CreaOrcoGordo(2,320061.510878, 27835.2, -58719.1381545)
CreaOrco(0,315824.89281, 28177.1, -52532.6053606)
CreaOrco(1,315668.605542, 28177.1, -57424.4808521)


_GritaOrco=Bladex.CreateSound("../../Sounds/"+language+"/comeon.wav","GritaOrco")
_GritaOrco.MaxDistance=1000000.0
	
	

StartSceneOrcos = Bladex.GetSector(284507, 26192, -49571)
StartSceneOrcos.OnEnter = IniciaOrcos

StartSceneOrcos3 = Bladex.GetSector(316837.279884, 38821.6, -4892.73207079)
StartSceneOrcos3.OnEnter = IniciaOrcos3


StartSceneOrcos2 = Bladex.GetSector(308029, 38276, -60536)
StartSceneOrcos2.OnEnter = IniciaOrcos2
