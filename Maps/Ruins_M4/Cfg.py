import LoadBar
LoadBar.LanguageProgressBar(338,"Blade_progress.jpg")

import Bladex


execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("ruins.lvl")

execfile("../../Scripts/BladeInit.py")


import Flechas

execfile("DefFuncs.py")

execfile("TextureMaterials.py") # DefFuncs OK

execfile("ruins.py") # DefFuncs OK

execfile("objs.py") # DefFuncs OK

execfile("spobjs.py") # DefFuncs OK

execfile("trsectors.py") # DefFuncs OK

execfile("Generadores.py")	# Debe estar cargado trsectors.py # DefFuncs OK

execfile("pulsadores.py") # DefFuncs OK

execfile("puertas.py") # DefFuncs OK	# Debe estar cargado pulsadores.py

execfile("Collaps.py") # DefFuncs OK

execfile("Pivotes.py") # DefFuncs OK

execfile("BladeTraps.py") # DefFuncs OK

execfile("Pinchos.py") # DefFuncs OK

execfile("Flame.py") # DefFuncs OK

execfile("Pozo.py") # DefFuncs OK		# Debe estar cargado trsectors.py

execfile("Mausoleo.py") # DefFuncs OK		# Debe estar cargado Generadores.py

execfile("Cementerio.py") # DefFuncs OK	# Debe estar cargado Generadores.py

execfile("Inicio.py") # DefFuncs OK

execfile("Final.py") # DefFuncs OK		# Debe estar cargado Mausoleo.py

execfile("enemigos.py") # DefFuncs OK

execfile("sonidos.py") # DefFuncs OK

execfile("MusicEvents.py")

execfile("Musicas.py")


import Reference

if Reference.PYTHON_DEBUG >= 1:
	execfile("Positions.py") # DefFuncs OK


#Bladex.SetCallCheck(1)
