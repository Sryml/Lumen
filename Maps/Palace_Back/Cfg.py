import LoadBar
LoadBar.ECTSProgressBar(238,"Blade_progress.jpg")

import Bladex

execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("palace.lvl")

execfile("../../Scripts/BladeInit.py")


execfile ("DefFuncs.py")
execfile ("ActorsInit.py")
execfile ("MusicEvents.py")

execfile ("TextureMaterials.py")
execfile ("objs.py")
execfile ("sol.py")
execfile ("agua.py")
execfile ("sonidos.py")
execfile ("puertas.py")
execfile ("fuegos.py")

execfile ("Espada.py")

import Reference

if Reference.PYTHON_DEBUG >= 1:
	execfile("positions.py")


char.Position = 94000, -3000, 219000
char.InitPos = 94000, -3000, 219000
char.Angle=3.14159
char.SetOnFloor()

#char.Level=12


###194154.105059, -3002.99780547, 218865.809592
