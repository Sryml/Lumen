import Bladex
import LoadBar
LoadBar.ECTSProgressBar(411,"Blade_progress.jpg")

execfile("../../Scripts/sys_init.py")

#BBLib.GetnOpenedInputFiles()

Bladex.ReadLevel("island.lvl")

execfile("../../Scripts/BladeInit.py")


execfile("ActorsInit.py")
execfile("DefFuncs.py")
execfile("MusicEvents.py")
execfile("Musica.py")
execfile ("TextureMaterials.py")
###INICIO-DEL-NIVEL

execfile ("Puertas.py")
execfile ("bgates.py")
execfile("Enemigos.py")
execfile("BreakDoors.py")
execfile ("objs.py")
execfile ("rejas.py")		# tiene que estar cargado el objs.py
execfile ("objrot.py")		# tiene que estar cargado el objs.py

execfile ("cajas.py")		# tiene que estar cargado el objrot.py
execfile ("antorchas.py")	# tiene que estar cargado el objs.py
execfile ("rocas.py")

execfile ("pociones.py")
execfile ("armas.py")

execfile ("luces.py")
execfile ("agua.py")
execfile("chorritos.py")
execfile ("fuentes.py")
execfile ("Sonidos.py")

execfile ("Puente.py")
execfile ("elevator2.py")


execfile ("ShadowVamp.py")

import Reference

if Reference.PYTHON_DEBUG >= 1:
	execfile("Positions.py")
execfile ("celdas.py")

execfile("demonio.py")

execfile("Prisoners.py")


execfile("cadaveres.py")
execfile("generadores.py")

execfile("historia.py")

#execfile("deslz.py")

execfile("MScene.py")
execfile ("WyvCiclica.py")
execfile ("vamp_cool.py")
execfile("chau_bolu.py")
execfile("RASTRILLO.py")
execfile("InicioScene.py")
execfile ("ptatabl.py")

#Bladex.SetCallCheck(1)
