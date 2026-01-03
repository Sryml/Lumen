import Bladex
import netgame
import LoadBar
LoadBar.ECTSProgressBar(126,"Blade_progress.jpg")


# Modo de juego : Kombat
NET_MODE = "KOMBAT"

CameraFrames = 70

execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("castle.lvl")

execfile("../../Scripts/ClientInit.py")

execfile("Luces.py")
# Modo de juego : Kombat



def con_estilo():
	execfile("objetos.py")
Bladex.AddScheduledFunc(Bladex.GetTime()+10.0,con_estilo,())