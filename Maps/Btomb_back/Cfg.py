import Bladex
import LoadBar
LoadBar.ECTSProgressBar(252,"Blade_progress.jpg")

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

execfile("armas.py")

execfile("sonidos.py")

execfile("collaps.py")

execfile("chaos.py")

execfile("transp.py")

execfile("hogueras.py")

execfile("musica.py")

char.Position=326140, -101, -212153
char.Angle=0.0