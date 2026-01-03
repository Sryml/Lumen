# Vulcano's hell

import Bladex
import netgame
import ReadGSFile
import LoadBar
LoadBar.ECTSProgressBar(122,"Blade_progress.jpg")

# Modo de juego : Kombat
NET_MODE = "KOMBAT"

PJInit = [(-1060.49388999, -3200, 2567.27016586,3.1415),(435.383479117, -3160, -6083.23985774,0.0)]
CameraFrames = 60




netgame.AddPosition(0, -110000, 0)
netgame.AddPosition(0, -110000, -5000)
netgame.AddPosition(0, -110000, 5000)
netgame.AddPosition(0, -110000, -10000)
netgame.AddPosition(0, -110000, 10000)
netgame.AddPosition(0, -110000, -15000)
netgame.AddPosition(0, -110000, 15000)

execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("king.lvl")


execfile("../../Scripts/ServerInit.py")


char.Position = netgame.GetNextPosition()

netgame.SetServerState(1) # SI enviar por la red los datos siguientes

execfile("traps.py")

ReadGSFile.ProcessGhostSectorFile("terremoto.sf")