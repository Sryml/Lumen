# char.Position=55514.5788226+3000, -2164.7999851, 56740.8058736

#########################################################
#														#
# WALLSKEL.PY           								#
#														#
# esqueleto que sale de un muro     					#
#														#
# (Yuio)												#
#														#
#########################################################

import Bladex
import Sounds
import Reference
import Select
import Change
import Actions
import Bladex
import AuxFuncs


################################################# PARTICULAS ###########################################
Bladex.AddParticleGType("wsarenadust","SmokeParticle",B_PARTICLE_GTYPE_BLEND,128)
for i in range(128):
	if i>64:
		traux=0.0
	else:
		traux=(64.0-i)/64.0
	aux=(128.0-i)/128.0
	r=200
	g=170
	b=140
	a=150.0*(1.0-traux)**0.5
	size=4.0+aux*300.0
	Bladex.SetParticleGVal("wsarenadust",i,r,g,b,a,size)


################################# TABLAS ############################################
wsWall=Bladex.GetSector( 56375, -2500, 56625 )
wsWall.Active=0
wsWall.InitBreak((150,0,0),(0,0,500),(0, 500, 0),'piedra pesada')

sword=Bladex.CreateEntity("TombwsAxe","Hacha",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)



shield=Bladex.CreateEntity("TombwsShield","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)

 
wsSkeleton=Bladex.CreateEntity("wsSkeleton","Skeleton",55500, -1200, 56625,"Person" )
wsSkeleton.Level=5
wsSkeleton.Angle=4.9
wsSkeleton.SetOnFloor()
wsSkeleton.ActionAreaMin=pow(2,2)
wsSkeleton.ActionAreaMax=pow(2,3)
Actions.TakeObject("wsSkeleton",shield.Name)
Actions.TakeObject("wsSkeleton",sword.Name)
EnemyTypes.EnemyDefaultFuncs(wsSkeleton)
wsSkeleton.Blind=1
wsSkeleton.Deaf=1


wsStarted = 0



################################# SKELETON #########################################

wsStartSector = Bladex.GetSector(70000,-4000,57000)
wsStartSector.OnEnter = wsStart
