import Bladex
import netgame
import ReadGSFile
import LoadBar
LoadBar.ECTSProgressBar(103,"Blade_progress.jpg")

# Modo de juego : Kombat
NET_MODE = "KOMBAT"

CameraFrames = 60


execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("King.lvl")

execfile("../../Scripts/ClientInit.py")

# Modo de juego : Kombat



execfile("traps.py")

ReadGSFile.ProcessGhostSectorFile("terremoto.sf")