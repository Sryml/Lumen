import Bladex
import LoadBar
LoadBar.ProgressBar(288,"Blade_progress.jpg")



execfile("../../Scripts/sys_init.py")


Bladex.ReadLevel("labyr_back.lvl")


execfile("../../Scripts/BladeInit.py")

execfile("DefFuncs.py")

execfile("MusicEvents.py")

execfile("TextureMaterials.py")

execfile("labyr_back.py")

execfile("objs.py")

execfile("spobjs.py")

execfile("Stones.py")

execfile("Stones2.py")

execfile("Stones3.py")

execfile("Puertas.py")

execfile("Sonidos.py")

execfile("Enemigos.py")

execfile("Tablilla.py")

execfile("Musica.py")

execfile("transportadores.py")


import Reference

if Reference.PYTHON_DEBUG >= 1:
	execfile("Positions.py")



char.Position=-37546, 871, 25352
char.Angle=2.3
