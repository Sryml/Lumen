import Bladex
import netgame
import LoadBar
LoadBar.ECTSProgressBar(120,"Blade_progress.jpg")


# Modo de juego : Kombat
NET_MODE = "KOMBAT"

# Frames de la camara
CameraFrames = 60

execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("arena7.lvl")

execfile("../../Scripts/ClientInit.py")

execfile("Objs.py")
execfile("agua.py")
