
import LoadBar
LoadBar.LanguageProgressBar(371,"Blade_progress.jpg")

from library import *


execfile("DefFuncs.py")

execfile("ActorsInit.py")
execfile("MusicEvents.py")
execfile("objs.py")
execfile("objsbrk.py")
execfile("puertas.py")
execfile("Enemigos.py")
execfile("pinchos.py")
execfile("antorchas.py")
execfile("TextureMaterials.py")
execfile("sonidos.py")
execfile("Sonidospuntuales.py")
execfile("cascada.py")
execfile("agua.py")
execfile("escape.py")
execfile("ChaosKnight.py")
execfile("Musica.py")
execfile("pendulos.py")
execfile("trampa_pinchos.py")
execfile("pivotes.py")
execfile("trampa_flechas.py")
execfile("traps.py")
execfile("RagnarActions.py")
execfile("DrunkWarder.py")
execfile("levadizo.py")
execfile("elevador.py")
execfile("Prisoners.py")
execfile("Pocimas.py")
execfile("comestibles.py")
execfile("InicioScene.py")

import Reference

if Reference.PYTHON_DEBUG >= 1:
	execfile("Positions.py")


import Demo_Stuff

Demo_Stuff.OnEnterDemo=0
Demo_Stuff.OnExitDemo=0
