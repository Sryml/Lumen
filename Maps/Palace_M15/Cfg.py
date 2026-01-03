import LoadBar
LoadBar.ECTSProgressBar(367,"Blade_progress.jpg")

import Bladex

execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("palace.lvl")

execfile("../../Scripts/BladeInit.py")



execfile ("DefFuncs.py")

execfile ("ActorsInit.py")

execfile ("MusicEvents.py")

execfile ("GEnems.py")

execfile ("TextureMaterials.py")

execfile ("objs.py")

execfile ("flechas_yo.py")

execfile ("sol.py")

execfile ("agua.py")

execfile ("cripta.py")

execfile ("sonidos.py")

execfile ("paguas.py")

execfile ("propiedades.py")

execfile ("generadores.py")

execfile ("Espada.py")

execfile ("rollonA.py")

execfile ("rollonB.py")

execfile ("ChaosKnight.py")

execfile ("LlaveCabeza.py")

execfile ("Trampa_Laser.py")

execfile ("iScene.py")

execfile ("Musica.py")


import Reference

if Reference.PYTHON_DEBUG >= 1:
	execfile("Positions.py")
