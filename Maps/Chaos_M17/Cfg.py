import Bladex
import LoadBar
LoadBar.ECTSProgressBar(368,"Blade_progress.jpg")


execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("chaos.lvl")

execfile("../../Scripts/BladeInit.py")

import Scorer

execfile("ActorsInit.py")

execfile("MusicEvents.py")

execfile("DefFuncs.py")

# part 1
execfile("enemigos.py")

#part 1
execfile("orcos.py")

execfile("TextureMaterials.py")

if Reference.PYTHON_DEBUG >= 1:
	execfile("Positions.py")

#part 2
execfile("demonio.py")

#part 2
execfile("tropa.py")

execfile("chaos_luces.py")

execfile("puertas.py")

# part 1
execfile("puente.py")

execfile("Breaks.py")

execfile("luces.py")

#part 2
execfile("transp.py")

#part 2
execfile("elevator.py")

#part 2
execfile("final.py")

#part 2
execfile("FirsArenaScene.py")

execfile("Sonidos.py")

execfile("sonidospuntuales.py")

execfile("collaps.py")

# part 2
execfile("golem.py")

#part 2
execfile("chaos.py")

#part 2
execfile("Chaos_Death.py")

execfile("temblores.py")

execfile("pocimas.py")

execfile("armas.py")

execfile("agua.py")

execfile("StartTime.py")

char.Position=326125.081178, -1276.36920221, -327.538538204
char.Angle=0.0

### posicion malo maloso final  char.Position=902922, 342369, 169758