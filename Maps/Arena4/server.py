# The castle of doom
import Bladex
import netgame
import LoadBar
LoadBar.ECTSProgressBar(134,"Blade_progress.jpg")


# Modo de juego : Kombat
NET_MODE = "KOMBAT"

# posicion y angulo de los combatientes
CameraFrames = 70



PJInit = [(6644.45702224, 811, -1115.85213583,5.53840432281),(12897.3555635, 811, 5964.66307523,2.47032227269)]

netgame.AddPosition(0, -110000, 0)
netgame.AddPosition(0, -110000, -5000)
netgame.AddPosition(0, -110000, 5000)
netgame.AddPosition(0, -110000, -10000)
netgame.AddPosition(0, -110000, 10000)
netgame.AddPosition(0, -110000, -15000)
netgame.AddPosition(0, -110000, 15000)

execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("castle.lvl")


execfile("../../Scripts/ServerInit.py")

char.Position = netgame.GetNextPosition()

netgame.SetServerState(0) # NO enviar por la red los datos siguientes

execfile("Luces.py")


netgame.SetServerState(1) # SI enviar por la red los datos siguientes


execfile("objetos.py")
