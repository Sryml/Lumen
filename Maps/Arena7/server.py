# The dark tower
import Bladex
import netgame
import LoadBar
LoadBar.ECTSProgressBar(134,"Blade_progress.jpg")


# Modo de juego : Kombat
NET_MODE = "KOMBAT"

# posicion y angulo de los combatientes
PJInit = [(13864, -4067, 9776,3.1415/2),(9597, -4068, 10076,-3.1415/2)]

# Frames de la camara
CameraFrames = 60



netgame.AddPosition(0, -110000, 0)
netgame.AddPosition(0, -110000, -5000)
netgame.AddPosition(0, -110000, 5000)
netgame.AddPosition(0, -110000, -10000)
netgame.AddPosition(0, -110000, 10000)
netgame.AddPosition(0, -110000, -15000)
netgame.AddPosition(0, -110000, 15000)

execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("arena7.lvl")

execfile("../../Scripts/ServerInit.py")

char.Position = netgame.GetNextPosition()

netgame.SetServerState(0) # NO enviar por la red los datos siguientes

execfile("objs.py")
execfile("agua.py")

netgame.SetServerState(1) # SI enviar por la red los datos siguientes
