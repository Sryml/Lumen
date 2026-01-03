import Bladex



def Bar():
	Bladex.LoadSampledAnimation("../../Anm/Bar_inicio_laberinto.bmv","Bar_inicio_laberinto",0,"Barbarian_N")
	Bladex.LoadSampledAnimation("../../Anm/Kgt_final_laberinto.bmv","Bar_final_laberinto",0,"Barbarian_N")
	Bladex.LoadSampledAnimation("../../Anm/Bar_escena_agonia.bmv","Bar_escena_agonia",0,"Barbarian_N")
	Bladex.LoadSampledAnimation("../../Anm/Bar_tablilla_laberinto.bmv","Bar_tablilla_laberinto",0,"Barbarian_N")

	Bladex.AddBipedAction("Bar","inicio_laberinto","Bar_inicio_laberinto",0.0,1.0,0)
	Bladex.AddBipedAction("Bar","final_laberinto","Bar_final_laberinto",0.0,1.0,0)
	Bladex.AddBipedAction("Bar","escena_agonia","Bar_escena_agonia",0.0,1.0,0)
	Bladex.AddBipedAction("Bar","tablilla_laberinto","Bar_tablilla_laberinto",0.0,1.0,0)


def Knight():
	Bladex.LoadSampledAnimation("../../Anm/Kgt_inicio_laberinto.bmv","Kgt_inicio_laberinto",0,"Knight_N")
	Bladex.LoadSampledAnimation("../../Anm/Kgt_final_laberinto.bmv","Kgt_final_laberinto",0,"Knight_N")
	Bladex.LoadSampledAnimation("../../Anm/Kgt_escena_agonia.bmv","Kgt_escena_agonia",0,"Knight_N")
	Bladex.LoadSampledAnimation("../../Anm/Kgt_tablilla_laberinto.bmv","Kgt_tablilla_laberinto",0,"Knight_N")

	Bladex.AddBipedAction("Knight","inicio_laberinto","Kgt_inicio_laberinto",0.0,1.0,0)
	Bladex.AddBipedAction("Knight","final_laberinto","Kgt_final_laberinto",0.0,1.0,0)
	Bladex.AddBipedAction("Knight","escena_agonia","Kgt_escena_agonia",0.0,1.0,0)
	Bladex.AddBipedAction("Knight","tablilla_laberinto","Kgt_tablilla_laberinto",0.0,1.0,0)


def Amz():
	Bladex.LoadSampledAnimation("../../Anm/Amz_inicio_laberinto.bmv","Amz_inicio_laberinto",0,"Amazon_L")
	Bladex.LoadSampledAnimation("../../Anm/Kgt_final_laberinto.bmv","Amz_final_laberinto",0,"Amazon_L")
	Bladex.LoadSampledAnimation("../../Anm/Amz_escena_agonia.bmv","Amz_escena_agonia",0,"Amazon_L")
	Bladex.LoadSampledAnimation("../../Anm/Amz_tablilla_laberinto.bmv","Amz_tablilla_laberinto",0,"Amazon_L")

	Bladex.AddBipedAction("Amz","inicio_laberinto","Amz_inicio_laberinto",0.0,1.0,0)
	Bladex.AddBipedAction("Amz","final_laberinto","Amz_final_laberinto",0.0,1.0,0)
	Bladex.AddBipedAction("Amz","escena_agonia","Amz_escena_agonia",0.0,1.0,0)
	Bladex.AddBipedAction("Amz","tablilla_laberinto","Amz_tablilla_laberinto",0.0,1.0,0)


def Dwf():
	Bladex.LoadSampledAnimation("../../Anm/Dwf_inicio_laberinto.bmv","Dwf_inicio_laberinto",0,"Dwarf_N")
	Bladex.LoadSampledAnimation("../../Anm/Kgt_final_laberinto.bmv","Dwf_final_laberinto",0,"Dwarf_N")
	Bladex.LoadSampledAnimation("../../Anm/Dwf_escena_agonia.bmv","Dwf_escena_agonia",0,"Dwarf_N")
	Bladex.LoadSampledAnimation("../../Anm/Dwf_tablilla_laberinto.bmv","Dwf_tablilla_laberinto",0,"Dwarf_N")

	Bladex.AddBipedAction("Dwf","inicio_laberinto","Dwf_inicio_laberinto",0.0,1.0,0)
	Bladex.AddBipedAction("Dwf","final_laberinto","Dwf_final_laberinto",0.0,1.0,0)
	Bladex.AddBipedAction("Dwf","escena_agonia","Dwf_escena_agonia",0.0,1.0,0)
	Bladex.AddBipedAction("Dwf","tablilla_laberinto","Dwf_tablilla_laberinto",0.0,1.0,0)





def Knight_Traitor():
	Bladex.LoadSampledAnimation("../../Anm/Kgt_agonia.bmv","Tkn_agonia",1,"Knight_Traitor")
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_escena_agonia.bmv","Tkn_dth_escena_agonia",0,"Knight_Traitor")
	Bladex.LoadSampledAnimation("../../Anm/Tkn_dth_wall_for_manuel.bmv","Tkn_dth_wall_for_manuel",0,"Knight_Traitor")
	Bladex.LoadSampledAnimation("../../Anm/Tkn_dth_lying_for_manuel.bmv","Tkn_dth_lying_for_manuel",0,"Knight_Traitor")

	Bladex.AddBipedAction("Knight_Traitor","agonia","Tkn_agonia",0.0,1.0,0)
	Bladex.AddBipedAction("Knight_Traitor","dth_escena_agonia","Tkn_dth_escena_agonia",0.0,1.0,0)
	Bladex.AddBipedAction("Knight_Traitor","dth_wall_for_manuel","Tkn_dth_wall_for_manuel",0.0,1.0,0)
	Bladex.AddBipedAction("Knight_Traitor","dth_lying_for_manuel","Tkn_dth_lying_for_manuel",0.0,1.0,0)
