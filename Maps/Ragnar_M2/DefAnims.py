import Bladex

def Knight_Traitor():
	Bladex.LoadSampledAnimation("../../Anm/Tkn_sleep2.BMV","Tkn_sleep2",1,"Knight_Traitor")
	Bladex.AddBipedAction("Knight_Traitor","sleep2","Tkn_sleep2",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Tkn_sleep_wall.BMV","Tkn_sleep_wall",1,"Knight_Traitor")
	Bladex.AddBipedAction("Knight_Traitor","sleep_wall","Tkn_sleep_wall",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Tkn_speak01.bmv","Tkn_speak01",0,"Knight_Traitor")
	Bladex.AddBipedAction("Knight_Traitor","speak01","Tkn_speak01",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Tkn_speak02.bmv","Tkn_speak02",0,"Knight_Traitor")
	Bladex.AddBipedAction("Knight_Traitor","speak02","Tkn_speak02",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Tkn_burn.bmv","Tkn_burn",1,"Knight_Traitor")
	Bladex.AddBipedAction("Knight_Traitor","burn","Tkn_burn",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Tkn_dth_burn.bmv","Tkn_dth_burn",0,"Knight_Traitor")
	Bladex.AddBipedAction("Knight_Traitor","dth_burn","Tkn_dth_burn",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Tkn_sleep.bmv","Tkn_sleep",1,"Knight_Traitor")
	Bladex.AddBipedAction("Knight_Traitor","sleep","Tkn_sleep",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Tkn_sleep_hit.bmv","Tkn_sleep_hit",1,"Knight_Traitor")
	Bladex.AddBipedAction("Knight_Traitor","sleep_hit","Tkn_sleep_hit",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Tkn_dth_sleep.bmv","Tkn_dth_sleep",0,"Knight_Traitor")
	Bladex.AddBipedAction("Knight_Traitor","dth_sleep","Tkn_dth_sleep",0.0,1.0,0)

def _Player1(biped_name, Kind):
	Bladex.LoadSampledAnimation("../../Anm/Kgt_inicio_ragnar.BMV","Kgt_inicio_ragnar",0, Kind)
	Bladex.AddBipedAction(biped_name,"inicio_ragnar","Kgt_inicio_ragnar",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_end_ragnar.BMV","Kgt_end_ragnar",0, Kind)
	Bladex.AddBipedAction(biped_name,"end_ragnar","Kgt_end_ragnar",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hit_r.bmv","Kgt_dth_penr",1, Kind)
	Bladex.AddBipedAction(biped_name,"dth_penr","Kgt_dth_penr",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hit_l.bmv","Kgt_dth_penl",1, Kind)
	Bladex.AddBipedAction(biped_name,"dth_penl","Kgt_dth_penl",0.0,1.0,0)
     
	Bladex.LoadSampledAnimation("../../Anm/Kgt_push_wall.bmv","Kgt_push_wall",0, Kind)
	Bladex.AddBipedAction(biped_name,"push_wall","Kgt_push_wall",0.0,1.0,0)

def Knight():
    _Player1("Knight", "Knight_N")


def Dwf():
    _Player1("Dwf", "Dwarf_N")


def Amz():
    _Player1("Amz", "Amazon_N")


def Bar():
    _Player1("Bar", "Barbarian_N")


# folllowing should not be necessary, or should be in animation sets
#Bladex.LoadSampledAnimation("../../Anm/Rgn_rlx_1h.bmv","Rgn_rlx_1h",1,"Ragnar")
#Bladex.LoadSampledAnimation("../../Anm/Tkn_rlx_f.bmv","Tkn_rlx_f",1,"Knight_Traitor")
#Bladex.LoadSampledAnimation("../../Anm/Rgn_rlx_f.bmv","Rgn_rlx_f",1,"Ragnar")
