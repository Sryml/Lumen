import Bladex




### Animaciones ###


def _Player1(biped_name, Kind):
	Bladex.LoadSampledAnimation("../../Anm/Amz_darkbook.bmv","Amz_darkbook",0, Kind)
	Bladex.AddBipedAction(biped_name,"darkbook","Amz_darkbook",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Amz_ruinas_final.bmv","Amz_ruinas_final",0, Kind)
	Bladex.AddBipedAction(biped_name,"ruinas_final","Amz_ruinas_final",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Amz_start.bmv","Amz_start",0, Kind)
	Bladex.AddBipedAction(biped_name,"start","Amz_start",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Amz_push_sarcofa.bmv","Amz_push_sarcofa",0, Kind)
	Bladex.AddBipedAction(biped_name,"push_sarcofa","Amz_push_sarcofa",0.0,1.0,0)

def Knight():
    _Player1("Knight", "Knight_N")


def Dwf():
    _Player1("Dwf", "Dwarf_N")


def Amz():
    _Player1("Amz", "Amazon_N")


def Bar():
    _Player1("Bar", "Barbarian_N")
