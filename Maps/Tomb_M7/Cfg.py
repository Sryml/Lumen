import LoadBar
LoadBar.ECTSProgressBar(386,"Blade_progress.jpg")

import Bladex

#BBLib.GetnOpenedInputFiles()

execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("tomb.lvl")

execfile("../../Scripts/BladeInit.py")


execfile("MusicEvents.py")
execfile("Musica.py")

execfile("ActorsInit.py")
execfile ("DefFuncs.py")
execfile ("TextureMaterials.py")
execfile ("sonidos.py")
execfile ("Sonidospuntuales.py")
import Reference

if Reference.PYTHON_DEBUG >= 1:
	execfile("Positions.py")

execfile ("comestibles.py")

execfile("Enemigos.py")

execfile ("sol.py")
execfile ("agua.py")

execfile ("objs.py")
execfile ("objrot.py")		#tiene que estar funcionando el objs.py
execfile ("pinchos.py")
execfile ("bloqueo.py")
execfile ("armas.py")

execfile ("luces.py")
execfile ("rejas.py")		#tiene que estar funcionando el objs.py

execfile("puertas.py")

# paredes que se rompen en zona tumbas esqueletos
execfile("bgates.py")

# esqueletos en muros
execfile("TwoSkel.py")		#tiene que estar funcionando el Enemigos.py

#esqueleto que sale de un nicho
execfile("wallSkel.py")	#tiene que estar funcionando el Enemigos.py



# En tablilla
execfile("pendulo.py")

## trampa suelo que se abre
execfile("suelo.py")

execfile("tumbarey.py")

execfile("Tablilla.py")

execfile("fetiche.py")

execfile("Golem.py")

## FINAL
execfile("tScene.py")


## esqueletos generados al final, antes de entrar en templo
execfile("generador.py")

# generador cementerio
execfile("cementerio.py")

execfile("templo.py")

execfile("King.py")

execfile("pergamino.py")		#tiene que estar funcionando el enemigos

execfile ("inicio.py")

execfile ("Genagua.py")

#Bladex.SetCallCheck(1)		#no descomentar
