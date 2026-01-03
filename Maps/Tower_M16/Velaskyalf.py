import Reference
import Bladex
###################################################################
#####  K N O C K I N G   O N                                  #####
#####     |      |  /--- |    /\  ---- | | |  /  /\  |   |--  #####
#####     |      |  |--- |   |  | |__  |/  |/   |  | |   |__  #####
#####      \    /   |    |   |--|    | |\  |    |--| |   |    #####
#####        \/     \--- \-- |  | ---- | | |    |  | |__ |    #####
#####                                                         #####
#####                                           D O O R S     #####
###################################################################

# char.Position =  -13211, -113033, 10966
# char.Position = -113211, -113033, 10966
# PolvoQueEntra(0.5)


##### Dark Smoke Particle definition ######
Bladex.AddParticleGType("VsSmoke","SmokeParticle",B_PARTICLE_GTYPE_BLEND,64)
for i in range(64):
	aux = i/64.0
	a=255.0*(1-(1-aux)**10) * (1-(aux**10))
	size=(2-aux)*600.0
	Bladex.SetParticleGVal("VsSmoke",i,90,90,100,a,size)


TimeToOpenDoors = 3.0
	
#
# PuertaMiguelIzquierda
#
# PuertaMiguelDerecha
#
# PMiguel.MMP
#
# execfile("velaskyalf.py")

