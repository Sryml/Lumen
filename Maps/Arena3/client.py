import Bladex
import netgame
import LoadBar
LoadBar.ECTSProgressBar(130,"Blade_progress.jpg")

#Bladex.SetCallCheck(1)

# Modo de juego : Kombat
NET_MODE = "KOMBAT"

# Frames de la camara
CameraFrames = 70



execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("3arena.lvl")

execfile("../../Scripts/ClientInit.py")

execfile("Objs.py")

#def RunOutCamera():
#	cam = Bladex.GetEntity("Camera")
#	cam.SType= 0
#	cam.TType= 0
#	cam.Position  =  (3818,-6835,-21883)
#	cam.TPos      =  (12080,-3880,-17087)
#
#Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, RunOutCamera,())