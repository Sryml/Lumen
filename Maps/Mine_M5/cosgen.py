
#
##      GENERADOR DE COSITAS
###                                 BY RAS
######################################################################
import EnmGenRnd


generadorT1 = EnmGenRnd.CreateEnemiesGenerator(6, 2)
generadorT1.CallBak = CreaGremilinDichoso

generadorT1.VirGenPos = [53485.5408249, -888.477554527, -15539.0935718]

generadorT1.AddPoint((26995, 9222, -200062), ("Cosita", "Cos", ""	, 0, "", 0))
generadorT1.AddPoint((17038, 9222, -196650), ("Cosita", "Cos", ""	, 0, "", 0))
generadorT1.AddPoint(( 4697, 9222, -197451), ("Cosita", "Cos", ""	, 0, "", 0))

generadorT1.AddPoint((26995, 9222, -200062), ("Cosita", "Cos", ""	, 0, "", 0))
generadorT1.AddPoint((17038, 9222, -196650), ("Cosita", "Cos", ""	, 0, "", 0))
generadorT1.AddPoint(( 4697, 9222, -197451), ("Cosita", "Cos", ""	, 0, "", 0))

generadorT1.DifTime = 1.6
generadorT1.Activate()

generadorT1.InitGenFunc=SaltaTierraGen

RodEnemyGen1         = Bladex.GetSector(20198, 9109, -208554)
RodEnemyGen1.OnEnter = ActivateCositaEnemyGenerator


