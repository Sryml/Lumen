
import LoadBar
LoadBar.ECTSProgressBar(378,"Blade_progress.jpg")



import Bladex

execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("defile.lvl")

execfile("../../Scripts/BladeInit.py")



execfile("DefFuncs.py")

execfile("MusicEvents.py")

execfile("TextureMaterials.py")

execfile("defile.py")

execfile("objs.py")

execfile("spobjs.py")

execfile("Sonidos.py")

execfile("Inicio.py")

execfile("trsectors.py")

execfile("Generadores.py")	# Debe estar cargado trsectors.py

execfile("Puente.py")

execfile("Enemigos.py")

execfile("Collaps.py")

execfile("Pinchos.py")

execfile("Guarida.py")

execfile("Orbe.py")

execfile("SpKey.py")		# Debe estar cargado Orbe.py

execfile("Final.py")		# Debe estar cargado trsectors.py

execfile("Golem.py")		# Debe estar cargado Generadores.py

execfile("Musica.py")


import Reference

if Reference.PYTHON_DEBUG >= 1:
	execfile("Positions.py")
