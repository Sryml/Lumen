import Bladex
import LoadBar
LoadBar.ECTSProgressBar(353,"Blade_progress.jpg")

execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("ice.lvl")

execfile("../../Scripts/BladeInit.py")

execfile ("MusicEvents.py")

execfile ("ActorsInit.py")

execfile ("DefFuncs.py")

execfile ("Luces.py")

if Reference.PYTHON_DEBUG >= 1:
	execfile("Positions.py")

execfile ("TextureMaterials.py")

execfile ("puertice.py")

execfile ("objs.py")

execfile ("propiedades.py")

execfile ("sol.py")

execfile ("sonidos.py")

execfile ("sonidospuntuales.py")

execfile ("pinchos.py")

execfile ("Tablitrap.py")

execfile ("transp.py")

execfile ("chaos.py")

execfile ("armas.py")

execfile ("hogueras.py")

execfile ("musica.py")

char.Position=-54975.3882617, 19868.1799422, 49743.7583998
char.Angle=4.64830009024