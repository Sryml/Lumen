import Bladex
import LoadBar
LoadBar.ECTSProgressBar(350,"Blade_progress.jpg")


### position  324784.643984, 29502.1252897, -92561.1774421

execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("btomb.lvl")

execfile("../../Scripts/BladeInit.py")

execfile("MusicEvents.py")

execfile("DefFuncs.py")
execfile("TextureMaterials.py")

execfile("sol.py")

execfile("luces.py")

execfile("agua.py")

execfile("objs.py")

if Reference.PYTHON_DEBUG >= 1:
	execfile("Positions.py")


execfile("rayos.py")


execfile("tablilla.py")

execfile("puertas.py")

execfile("rompibles.py")

execfile("plantas.py")

execfile("pocimas.py")

execfile("armas.py")

execfile("sonidos.py")

execfile("collaps.py")

execfile("lichs.py")

execfile("granfinal.py")

execfile("musica.py")

execfile("enemigos.py")

execfile("hogueras.py")

execfile("inicio.py")

execfile("gases.py")

char.Position=325982, -105, -221910
char.Angle=0.0


###char.Position=328187.076847, 1908.84311638, -86823.9787082