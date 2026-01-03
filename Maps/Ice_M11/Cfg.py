import Bladex

import LoadBar
LoadBar.ECTSProgressBar(375,"Blade_progress.jpg")

execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("ice.lvl")

execfile("../../Scripts/BladeInit.py")

execfile ("MusicEvents.py")

execfile ("ActorsInit.py")

execfile ("DefFuncs.py")

execfile ("musica.py")

execfile ("Gen.py")

execfile ("Gen2.py")

execfile ("Luces.py")

if Reference.PYTHON_DEBUG >= 1:
	execfile("Positions.py")

execfile ("TextureMaterials.py")

execfile ("puertice.py")

execfile ("objs.py")

execfile ("armas.py")

execfile ("objsbrk.py")

execfile ("propiedades.py")

execfile ("elevador.py")

execfile ("sol.py")

execfile ("blades.py")

execfile ("sonidos.py")

execfile ("sonidospuntuales.py")

execfile ("Enemigos.py")

execfile ("demonio.py")

execfile ("pinchos.py")

execfile ("Tablitrap.py")

execfile ("MinEat.py")

execfile ("jema.py")

execfile ("hogueras.py")

execfile ("inicio.py")




char.Position=-61936.6384469, 22902.952862, 85541.6398723
char.Angle=3.14149612446