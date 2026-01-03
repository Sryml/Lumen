
import Bladex
import LoadBar
LoadBar.ECTSProgressBar(293,"Blade_progress.jpg")

execfile("../../Scripts/sys_init.py")

#BBLib.GetnOpenedInputFiles()

Bladex.ReadLevel("Desert.lvl")

execfile("../../Scripts/BladeInit.py")
execfile ("MusicEvents.py")
execfile ("DefFuncs.py")

execfile ("TextureMaterials.py")

import Reference

if Reference.PYTHON_DEBUG >= 1:
	execfile("Positions.py")

execfile ("luces.py")
execfile ("efectos.py")
execfile ("chorritos.py")
execfile ("sonidos.py")
execfile ("polvo.py")
execfile ("fuego.py")

execfile("DesprendimientoSuelo.py")

execfile("PUERTAS.py")


execfile ("objs.py")
execfile ("bloqueo.py")
#execfile ("antorchas.py")		# tiene que estar cargado el obj.py
execfile ("armas.py")
execfile ("rejas.py")		# tiene que estar cargado el obj.py


execfile ("tablilla.py")
#execfile ("bgates.py")
execfile ("Dchaos.py")

execfile ("Transp.py")

execfile ("Musica.py")

char.Position= -39470.2676505, 9416.69076738, -136953.2

#Bladex.SetCallCheck(1)

AuxFuncs.SingleFrameFade()
Scorer.SetVisible(0)
