import Breakings
import Actions
import netgame

if netgame.GetNetState() == 1:
	o=Bladex.CreateEntity("lamparaegipto","Lamparaegipto",-6009.626000,44.064000,-4813.343000,"Physic")
	o.Scale=1.000000
	o.Orientation=0.707107,0.707107,0.000000,0.000000
else:
	o=Bladex.GetEntity("lamparaegipto")
o.FiresIntensity=[ 0 ]
o.Lights=[ (20.000000,0.100000,(255,157,60)) ]




if netgame.GetNetState() == 1:

	o=Bladex.CreateEntity("meson","Meson",14648.703000,1137.911000,11633.907000,"Physic")
	o.Scale=1.000000
	o.Orientation=0.707080,0.707080,0.006171,-0.006171
	Breakings.SetBreakable("meson",12,100)

	o=Bladex.CreateEntity("banco1","Banco",13229.634000,1360.864000,11888.930000,"Physic")
	o.Scale=1.000000
	o.Orientation=0.706676,0.706676,-0.024678,0.024678
	Breakings.SetBreakable("banco1",12,100)
	
	
	o=Bladex.CreateEntity("banco2","Banco",16007.498000,1362.751000,11436.288000,"Physic")
	o.Scale=1.000000
	o.Orientation=0.706434,0.706434,-0.030844,0.030844
	Breakings.SetBreakable("banco2",12,100)
	
	
	
