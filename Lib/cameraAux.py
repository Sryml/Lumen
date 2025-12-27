##########################################################
#
#	SCRIPT	: libreria para coger los vectores de la camara
#
#	AUTH	: Yuio
#
#
##########################################################

import math
import Bladex
import B3DLib

n= 0.0, 0.0, 0.0
u= 0.0, 0.0, 0.0
v= 0.0, 0.0, 0.0

def updateInfo():
	global n, u , v

	cam = Bladex.GetEntity("Camera")
	opos=cam.Position
	tpos=cam.TPos
	v=tpos[0]-opos[0], tpos[1]-opos[1], tpos[2]-opos[2]

	aux				= 0.0 , -1.0 , 0.0
	n				= B3DLib.Normalize(v)
	u				= aux[1]*n[2] - aux[2]*n[1] , aux[2]*n[0] - aux[0]*n[2] , aux[0]*n[1] - aux[1]*n[0]
	v				= u[1]*n[2] - u[2]*n[1] , u[2]*n[0] - u[0]*n[2] , u[0]*n[1] - u[1]*n[0]
