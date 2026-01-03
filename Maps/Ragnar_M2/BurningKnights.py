import def_class
from math import pow
import EnemyTypes
import Actions
import Bladex
import pdb
import Reference
import Breakings
import AniSound
import math
import AuxFuncs
import Torchs

BoxBurnTime = 6						# in Seconds
BoxDestroyTime = 12					# in Seconds


#######################################################
# Define the boxes
#######################################################
o=Bladex.CreateEntity("BKBox1","Caja_i_r",-89323.669384,-3260.840067,20582.370714)
o.Static=0
o.Scale=1.282432
o.Orientation=0.425547,0.425547,0.564721,-0.564721
o.CastShadows=0
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n
Actions.SetBurnable(o.Name, BoxBurnTime, BoxDestroyTime)
o.UseFunc = SetFireToBoxes
#Breakings.SetBreakable("BKBox1", BoxDestroyTime, BoxDestroyTime+20.0)


o=Bladex.CreateEntity("BKBox2","Caja_i_r",-90078.813308,-3274.676501,18282.632015)
o.Static=0
o.Scale=1.295256
o.Orientation=0.615434,0.615434,0.348196,-0.348196
o.CastShadows=0
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n
Actions.SetBurnable(o.Name, BoxBurnTime, BoxDestroyTime)
o.UseFunc = SetFireToBoxes
#Breakings.SetBreakable("BKBox2", BoxDestroyTime, BoxDestroyTime+20.0)


o=Bladex.CreateEntity("BKBox3","Caja_i_r",-89433.118286,-4693.084370,20301.464450)
o.Static=0
o.Scale=1.257163
o.Orientation=0.410191,0.401885,0.574209,-0.583536
o.CastShadows=0
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n
Actions.SetBurnable(o.Name, BoxBurnTime, BoxDestroyTime)
o.UseFunc = SetFireToBoxes
#Breakings.SetBreakable("BKBox3", BoxDestroyTime, BoxDestroyTime+20.0)


o=Bladex.CreateEntity("BKBox4","Caja_i_r",-89856.102240,-6069.592918,20357.480459)
o.Static=0
o.Scale=1.220190
o.Orientation=0.426344,0.416480,0.562629,-0.572909
o.CastShadows=0
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n
Actions.SetBurnable(o.Name, BoxBurnTime, BoxDestroyTime)
o.UseFunc = SetFireToBoxes
#Breakings.SetBreakable("BKBox4", BoxDestroyTime, BoxDestroyTime+20.0)


o=Bladex.CreateEntity("BKBox5","Caja_i_r",-90309.379150,-5241.130677,18348.379159)
o.Static=0
o.Scale=1.596263
o.Orientation=0.567310,0.422235,-0.417931,-0.570273
o.CastShadows=0
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n
Actions.SetBurnable(o.Name, BoxBurnTime, BoxDestroyTime)
o.UseFunc = SetFireToBoxes
#Breakings.SetBreakable("BKBox5", BoxDestroyTime, BoxDestroyTime+20.0)


###################
# Particle system #
###################

B_PARTICLE_GTYPE_BLEND=1

Bladex.AddParticleGType("LightDarkSmoke","SmokeParticle2",B_PARTICLE_GTYPE_BLEND,96)

for i in range(96):
	if(i>96/2):
		aux=0.0
	else:
		aux=(96/2.0-i)/(96/2.0)
	r=17
	g=17
	b=17
	a=255.0*math.sqrt(1.0-aux)
	size=1000.0-(aux**2.0)*400.0
	Bladex.SetParticleGVal("LightDarkSmoke",i,r,g,b,a,size)



#######################################################
# Define the burning knight class
#######################################################


Bladex.AddCombustionDataFor("Knight_Traitor", "Fire", 250, 400, 4, 0.5, 1, 25)

#Bladex.LoadSampledAnimation("../../Anm/Tkn_burn.bmv","Tkn_burn",1,"Knight_Traitor")
#Bladex.LoadSampledAnimation("../../Anm/Tkn_dth_burn.bmv","Tkn_dth_burn",0,"Knight_Traitor")



#######################################################
# Create the burning knight
# (named after 'brave' Sir Robin of the Holy Grail)
#######################################################
"""
MINSTREL:  [singing]  Bravely bold Sir Robin rode forth from Camelot.
    He was not afraid to die, O brave Sir Robin.
    He was not at all afraid to be killed in nasty ways,
    Brave, brave, brave, brave Sir Robin!

    He was not in the least bit scared to be mashed into a pulp,
    Or to have his eyes gouged out and his elbows broken,
    To have his kneecaps split and his body burned away
    And his limbs all hacked and mangled, brave Sir Robin!

    His head smashed in and his heart cut out
    And his liver removed and his bowels unplugged
    And his nostrils raped and his bottom burned off
    And his pen--
SIR ROBIN:  That's-- that's, uh-- that's enough music for now, lads.  Heh.
    Looks like there's dirty work afoot.
"""

BKnightScream=Bladex.CreateSound('../../sounds/grito-quemando1.wav', 'BurningKnightScream')
BKnightScream.SendNotify=1
BKnightScream.Volume=1
BKnightScream.MinDistance =  5000
BKnightScream.MaxDistance = 10000

enric=Bladex.CreateEntity("Robin","Knight_Traitor",-86250, -3800, 19000,"Person")
enric.Angle=1.2
#enric.ActionAreaMin=0
#enric.ActionAreaMax=0
enric.Data = def_class.BurningKnight (enric)
#enric.AddAnimSound('Tkn_dth_burn', BKnightScream, 10)
enric.SetOnFloor()
