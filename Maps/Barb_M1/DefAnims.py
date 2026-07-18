import Bladex

def _Player1(biped_name, Kind):
	Bladex.LoadSampledAnimation("../../Anm/Bar_espiritus.BMV","Bar_espiritus",0,Kind)
	Bladex.AddBipedAction(biped_name,"espiritus","Bar_espiritus",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Bar_totem_fall.BMV","Bar_totem_fall",0,Kind)
	Bladex.AddBipedAction(biped_name,"totem_fall","Bar_totem_fall",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Bar_start_barbaros.BMV","Bar_start_barbaros",0,Kind)
	Bladex.AddBipedAction(biped_name,"start_barbaros","Bar_start_barbaros",0.0,1.0,0)

def Knight():
    _Player1("Knight", "Knight_N")


def Dwf():
    _Player1("Dwf", "Dwarf_N")


def Amz():
    _Player1("Amz", "Amazon_N")


def Bar():
    _Player1("Bar", "Barbarian_N")
