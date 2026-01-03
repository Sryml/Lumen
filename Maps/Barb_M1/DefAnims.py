import Bladex

def Bar():
	Bladex.LoadSampledAnimation("../../Anm/Bar_espiritus.BMV","Bar_espiritus",0,"Barbarian")
	Bladex.AddBipedAction("Bar","espiritus","Bar_espiritus",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Bar_totem_fall.BMV","Bar_totem_fall",0,"Barbarian")
	Bladex.AddBipedAction("Bar","totem_fall","Bar_totem_fall",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Bar_start_barbaros.BMV","Bar_start_barbaros",0,"Barbarian")
	Bladex.AddBipedAction("Bar","start_barbaros","Bar_start_barbaros",0.0,1.0,0)
