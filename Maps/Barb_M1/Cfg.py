import LoadBar
LoadBar.LanguageProgressBar(328,"Blade_progress.jpg")


#BBLib.GetnOpenedInputFiles()

import Bladex

execfile("../../Scripts/sys_init.py")


Bladex.ReadLevel("barb.lvl")

execfile("../../Scripts/BladeInit.py")


#char=Bladex.GetEntity("Player1")
#char.Position= -108000,7000,-95000

execfile("ActorsInit.py")
execfile("DefFuncs.py")
execfile("MusicEvents.py")
execfile("TextureMaterials.py")

execfile("Musica.py")

execfile("totem.py")
import Reference

if Reference.PYTHON_DEBUG >= 1:
	execfile("Positions.py")

execfile("Trampa_pinchos.py")
execfile("pinchos3.py")



execfile("luces.py")
execfile ("sol.py")
execfile("cascada.py")
execfile("cascadaint.py")
execfile("cascadapint.py")

execfile ("Enemigos.py")

execfile ("objs.py")
execfile ("bloqueo.py")
execfile ("OBJETOS.py")
execfile ("barriles.py")
execfile ("antorchas.py")
execfile ("rastrillo.py")
execfile ("comestibles.py")
execfile ("armas.py")
execfile ("cosas.py")
execfile ("puente.py")

execfile ("agua.py")

execfile ("bolas.py")

execfile ("cadaveres.py")
execfile ("gentrampa.py")


execfile("deslz.py")
execfile("derr.py")
execfile("BreakDoors.py")
execfile("pinchos1.py")
execfile("pinchos2.py")


execfile("puertas.py")


execfile("Sonidos.py")
execfile("Sonidospuntuales.py")

execfile("InicioScene.py")
execfile("FinalScene.py")


import Demo_Stuff
Demo_Stuff.OnEnterDemo=0
Demo_Stuff.OnExitDemo=0

