# Vertigo
import Bladex
import netgame
import LoadBar
LoadBar.ECTSProgressBar(132,"Blade_progress.jpg")


# Modo de juego : Kombat
NET_MODE = "KOMBAT"

# posicion y angulo de los combatientes

PJInit = [(-24367.7965624, -11239, 28623.8075263,3.14),(-24311.0501099, -11239, 22515.2320036,0.0)]

CameraFrames = 60



netgame.AddPosition(0, -110000, 0)
netgame.AddPosition(0, -110000, -5000)
netgame.AddPosition(0, -110000, 5000)
netgame.AddPosition(0, -110000, -10000)
netgame.AddPosition(0, -110000, 10000)
netgame.AddPosition(0, -110000, -15000)
netgame.AddPosition(0, -110000, 15000)

execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("Arena5.lvl")


execfile("../../Scripts/ServerInit.py")

char.Position = netgame.GetNextPosition()

netgame.SetServerState(0) # NO enviar por la red los datos siguientes

execfile("Luces.py")
execfile("Objs.py")
execfile("cuervos.py")
execfile("sonidos.py")
netgame.SetServerState(1) # SI enviar por la red los datos siguientes
