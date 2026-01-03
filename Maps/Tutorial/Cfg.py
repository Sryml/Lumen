import Bladex
import LoadBar
LoadBar.ECTSProgressBar(652,"Blade_progress.jpg")

execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("tutorial.lvl")

execfile("../../Scripts/BladeInit.py")


import darfuncs



execfile ("MusicEvents.py")
execfile ("Musica.py")
execfile ("TextureMaterials.py")
execfile ("sonidos.py")
execfile ("objs.py")
execfile ("sol.py")
execfile ("agua.py")
execfile ("propiedades.py")
execfile ("puertas.py")



execfile ("tutor0.py")
execfile ("tutor1.py")
execfile ("tutor2.py")
execfile ("tutor3.py")
execfile ("tutor4.py")
execfile ("tutor5.py")
execfile ("tutor6.py")


import Reference

if Reference.PYTHON_DEBUG >= 1:
	execfile("Positions.py")


Bladex.SetListenerPosition(1)
