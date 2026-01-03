import Bladex
import LoadBar
LoadBar.ECTSProgressBar(296,"Blade_progress.jpg")

#BBLib.GetnOpenedInputFiles()

execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("tomb.lvl")

execfile("../../Scripts/BladeInit.py")

#char.Level=12

execfile ("MusicEvents.py")

execfile ("DefFuncs.py")

execfile ("TextureMaterials.py")
execfile ("sonidos.py")
execfile ("Sonidospuntuales.py")
execfile ("luces.py")
import Reference

if Reference.PYTHON_DEBUG >= 1:
	execfile("Positions.py")

execfile ("objs.py")
execfile("rejas.py")
execfile ("hogueras.py")
execfile("puertas.py")
execfile ("bloqueo.py")


# En tablilla
execfile("pendulo.py")

execfile("Tablilla.py")

execfile("Tchaos.py")

execfile ("Musica.py")

execfile("Transp.py")


char.Position= -35389.2052674, 5927.78341018, -33507.7013751

#Bladex.SetCallCheck(1)		#no descomentar



AuxFuncs.SingleFrameFade()
Scorer.SetVisible(0)
