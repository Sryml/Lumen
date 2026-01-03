
import Bladex
import LoadBar
LoadBar.ECTSProgressBar(368,"Blade_progress.jpg")

execfile("../../Scripts/sys_init.py")

#BBLib.GetnOpenedInputFiles()

Bladex.ReadLevel("Desert.lvl")

execfile("../../Scripts/BladeInit.py")
execfile ("MusicEvents.py")
execfile ("Musica.py")
execfile ("DefFuncs.py")
#char.Level=12
execfile ("TextureMaterials.py")
import Reference

if Reference.PYTHON_DEBUG >= 1:
	execfile("Positions.py")

execfile ("luces.py")
execfile ("efectos.py")
execfile ("chorritos.py")
execfile ("fuego.py")
execfile ("sonidos.py")
execfile ("polvo.py")

execfile("DesprendimientoSuelo.py")
execfile ("gemaray.py")
execfile("PUERTAS.py")
execfile("bastonptatemplo.py")
execfile("Puertasdeltemplo.py")

execfile ("objs.py")
execfile ("objrot.py")		# tiene que estar cargado el obj.py
execfile ("pociones.py")
execfile ("antorchas.py")		# tiene que estar cargado el obj.py
execfile ("rejas.py")		# tiene que estar cargado el obj.py
execfile ("armas.py")
execfile ("telaran.py")

execfile ("tablilla.py")
execfile ("bgates.py")
execfile ("cripta.py")
execfile ("LlaveMagica.py")


execfile ("GolemSleep.py")
execfile ("Enemigos.py")
execfile ("FinalScene.py")
execfile ("MuralScene.py")
execfile ("trikytorch.py")

#Bladex.SetCallCheck(1)
