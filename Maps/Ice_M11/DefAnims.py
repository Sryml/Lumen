import Bladex

def qLoadAnims(Kind,Animation,AnimationFile,person):
	Bladex.LoadSampledAnimation("../../Anm/"+AnimationFile+".BMV",Kind+"_"+Animation,0,person)
	Bladex.AddBipedAction(Kind,Animation,Kind+"_"+Animation,0.0,1.0,0)

def Min():
	qLoadAnims("Min","standup","Min_standup","Minotaur")
	qLoadAnims("Min","eat","Min_eat","Minotaur")
	qLoadAnims("Min","escena_hielo","Min_escena_hielo","Minotaur")

def Ldm():
	qLoadAnims("Ldm","window","Ldm_window","Little_Demon")

def Tkn():
	qLoadAnims("Tkn","sleep_wall","Tkn_sleep_wall","Traitor_Knight")
	qLoadAnims("Tkn","alarm01","Tkn_alarm01","Traitor_Knight")

def Knight():
	qLoadAnims("Kgt","tablilla_hielo","Kgt_tablilla_hielo","Knight_N")
	qLoadAnims("Kgt","start_ice","Kgt_start_ice","Knight_N")
	qLoadAnims("Kgt","tke_key","Kgt_tke_key","Knight_N")
	qLoadAnims("Kgt","window","Kgt_window","Knight_N")

def Amz():
	qLoadAnims("Amz","tablilla_hielo","Amz_tablilla_hielo","Amazon_N")
	qLoadAnims("Amz","start_ice","Amz_start_ice","Amazon_N")
	qLoadAnims("Amz","tke_key","Amz_tke_key","Amazon_N")
	qLoadAnims("Amz","window","Kgt_window","Amazon_N")

def Dwf():
	qLoadAnims("Dwf","tablilla_hielo","Dwf_tablilla_hielo","Dwarf_N")
	qLoadAnims("Dwf","start_ice","Dwf_start_ice","Dwarf_N")
	qLoadAnims("Dwf","tke_key","Dwf_tke_key","Dwarf_N")
	qLoadAnims("Dwf","window","Kgt_window","Dwarf_N")

def Bar():
	qLoadAnims("Bar","tablilla_hielo","Bar_tablilla_hielo","Barbarian_N")
	qLoadAnims("Bar","start_ice","Bar_start_ice","Barbarian_N")
	qLoadAnims("Bar","tke_key","Bar_tke_key","Barbarian_N")
	qLoadAnims("Bar","window","Kgt_window","Barbarian_N")
