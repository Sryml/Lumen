import Bladex
import netgame
import LoadBar
LoadBar.ECTSProgressBar(118,"Blade_progress.jpg")


# Modo de juego : Kombat
NET_MODE = "KOMBAT"

CameraFrames = 60


execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("Arena5.lvl")

execfile("../../Scripts/ClientInit.py")
# Modo de juego : Kombat
execfile("../../Scripts/kombat.py")


execfile("Luces.py")

execfile("Objs.py")

execfile("cuervos.py")

execfile("sonidos.py")