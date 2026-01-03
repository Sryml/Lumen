#########################################################
#														#
# PALACE												#
#														#
# escenita del ejercito 1								#
#														#
# (Yuio)												#
#														#
#########################################################

import Bladex
import Sounds
import Reference
import Select
import Actions
import AuxFuncs
import GameText
import Scorer
import Sparks
import EnemyTypes
import math
import darfuncs

# B: char.Position = -23392.016, -1953.069, 153216.797-3400

#Bladex.LoadSampledAnimation("../../Anm/Gor_ejer3.BMV","Gor_ejer3",1,"Great_Ork")
#Bladex.LoadSampledAnimation("../../Anm/Ork_ejer_bow.BMV","Ork_ejer_bow",1,"Ork")
#Bladex.LoadSampledAnimation("../../Anm/Ork_ejer1.BMV","Ork_ejer1",1,"Ork")
#Bladex.LoadSampledAnimation("../../Anm/Ork_ejer2.BMV","Ork_ejer2",1,"Ork")
#Bladex.LoadSampledAnimation("../../Anm/Ork_ejer4.BMV","Ork_ejer4",1,"Ork")
#Bladex.LoadSampledAnimation("../../Anm/Ork_ejer5.BMV","Ork_ejer5",1,"Ork")

essDoor = Bladex.GetSector(-25033.562409, -2034.6, 152298.68074)
essDoor.Active = 0
essDoor.InitBreak( (0.0, 0.0,200.0), (0.0, 700.0, 150.0), (650.0, 130.0, 580.0) ,'piedra pesada')

Bladex.AddParticleGType("essSceneDust","SmokeParticle",B_PARTICLE_GTYPE_BLEND,128)
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
	size=17.0+aux*400.0
	Bladex.SetParticleGVal("essSceneDust",i,r,g,b,a,size)


essSceneBCreateX()



essSceneBLaunched=0

#essSceneBSector =  Bladex.GetSector(78183,965,119600)
#essSceneBSector.OnEnter = essSceneBLaunch
