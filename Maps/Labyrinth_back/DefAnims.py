import Bladex



def Bar():
	Bladex.LoadSampledAnimation("../../Anm/Bar_tablilla_laberinto.bmv","Bar_tablilla_laberinto",0,"Barbarian_N")
	Bladex.AddBipedAction("Bar","tablilla_laberinto","Bar_tablilla_laberinto",0.0,1.0,0)


def Knight():
	Bladex.LoadSampledAnimation("../../Anm/Kgt_tablilla_laberinto.bmv","Kgt_tablilla_laberinto",0,"Knight_N")
	Bladex.AddBipedAction("Knight","tablilla_laberinto","Kgt_tablilla_laberinto",0.0,1.0,0)


def Amz():
	Bladex.LoadSampledAnimation("../../Anm/Amz_tablilla_laberinto.bmv","Amz_tablilla_laberinto",0,"Amazon_L")
	Bladex.AddBipedAction("Amz","tablilla_laberinto","Amz_tablilla_laberinto",0.0,1.0,0)


def Dwf():
	Bladex.LoadSampledAnimation("../../Anm/Dwf_tablilla_laberinto.bmv","Dwf_tablilla_laberinto",0,"Dwarf_N")
	Bladex.AddBipedAction("Dwf","tablilla_laberinto","Dwf_tablilla_laberinto",0.0,1.0,0)
