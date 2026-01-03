# Gates of Karum
import Bladex
import netgame
import LoadBar
LoadBar.ECTSProgressBar(132,"Blade_progress.jpg")


# Modo de juego : Kombat
NET_MODE = "KOMBAT"

# posicion y angulo de los combatientes
PJInit = [(12728.4462419, -1544, -394.431831518,3.1530),(13274.3161181, -938, -13617.5324408,6.24956)]

# Frames de la camara
CameraFrames = 70




netgame.AddPosition(0, -100000, 0)
netgame.AddPosition(0, -100000, -5000)
netgame.AddPosition(0, -100000, 5000)
netgame.AddPosition(0, -100000, -10000)
netgame.AddPosition(0, -100000, 10000)
netgame.AddPosition(0, -100000, -15000)
netgame.AddPosition(0, -100000, 15000)

execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("3arena.lvl")

execfile("../../Scripts/ServerInit.py")

char.Position = netgame.GetNextPosition()

netgame.SetServerState(0) # NO enviar por la red los datos siguientes

execfile("Objs.py")

netgame.SetServerState(1) # SI enviar por la red los datos siguientes
