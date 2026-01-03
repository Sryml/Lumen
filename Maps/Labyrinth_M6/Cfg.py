import Bladex
import LoadBar
LoadBar.LanguageProgressBar(356,"Blade_progress.jpg")



execfile("../../Scripts/sys_init.py")


Bladex.ReadLevel("labyr.lvl")


execfile("../../Scripts/BladeInit.py")

execfile("DefFuncs.py")

execfile("MusicEvents.py")

execfile("TextureMaterials.py")

execfile("labyr.py")

execfile("objs.py")

execfile("spobjs.py")

execfile("Stones.py")

execfile("Stones2.py")

execfile("Inicio.py")

execfile("Final.py")

execfile("cadaveres.py")

execfile("Puertas.py")		# Debe estar cargado el Final.py

execfile("Elevadores.py")

execfile("Agonia.py")		# Debe estar cargado el Puertas.py

execfile("Sonidos.py")

execfile("Enemigos.py")

execfile("Tablilla.py")

execfile("Musica.py")


import Reference

if Reference.PYTHON_DEBUG >= 1:
	execfile("Positions.py")
