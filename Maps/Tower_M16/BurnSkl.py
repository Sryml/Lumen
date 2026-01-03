import EnmGenRnd
import AuxFuncs
import OnOff
	
Bladex.AddCombustionDataFor("Skeleton", "Fire", 250, 400, 4, 1, 3, 144000) # se extingira en 40 horas!

generadorBrnSkl = EnmGenRnd.CreateEnemiesGenerator(6, 2)
generadorBrnSkl.Level = 11

generadorBrnSkl.AddPoint((-14000, -35500 , 3700),("BrnSkl1", "Skeleton", "HookSword", 0, "Escudo4", 1), "Skl_appears1")
generadorBrnSkl.AddPoint((-14000, -35500 , 7900),("BrnSkl2", "Skeleton", "HookSword", 0, "Escudo4", 1), "Skl_appears1")

generadorBrnSkl.InitGenFunc=GenerateBurnSkl
generadorBrnSkl.DifTime = 0.6
#generadorBrnSkl.VirGenPos = -7000,-40000,0
generadorBrnSkl.FinishGenFunc = finGeneraFuego
generadorBrnSkl.Activate()


BrnSklSec2 = Bladex.GetSector(-7000,-40000,0)
BrnSklSec2.OnEnter = StartBurnSkl2
