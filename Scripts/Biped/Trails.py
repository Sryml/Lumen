
def DefaultTrail(Name):
	import Bladex
	trail=Bladex.GetTrailType(Name)
	trail.Time2Live=0.3
	trail.Color=40,40,40
	trail.Transparency=0.7
	trail.ShrinkFactor=1.0
	


def Init():
	import Bladex
	import netgame
	
	if netgame.GetNetState() == 1:
		DefaultTrail("Default")
		DefaultTrail("EstelaGris1")
		DefaultTrail("EstelaRoja1")
		DefaultTrail("EstelaAmarilla1")
		DefaultTrail("EstelaAzul1")
	else:
		trail=Bladex.GetTrailType("Default")
		trail.Time2Live=0.3
		trail.Color=40,40,40
		trail.Transparency=0.7
		trail.ShrinkFactor=1.0
		
		trail=Bladex.GetTrailType("EstelaGris1")
		trail.Time2Live=0.4
		trail.Color=40,40,40
		trail.Transparency=0.6
		trail.ShrinkFactor=1.0
		
		trail=Bladex.GetTrailType("EstelaRoja1")
		trail.Time2Live=0.6
		trail.Color=70,0,0
		trail.Transparency=0.5
		trail.ShrinkFactor=1.0
		
		trail=Bladex.GetTrailType("EstelaAmarilla1")
		trail.Time2Live=0.6
		trail.Color=40,40,0
		trail.Transparency=0.7
		trail.ShrinkFactor=1.0
		
		trail=Bladex.GetTrailType("EstelaAzul1")
		trail.Time2Live=0.6
		trail.Color=0,0,40
		trail.Transparency=0.7
		trail.ShrinkFactor=1.0

print "Done Trails.Init()"













