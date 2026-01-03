import Bladex

def qLoadAnims(Kind,Animation,AnimationFile,person):
	Bladex.LoadSampledAnimation("../../Anm/"+AnimationFile+".BMV",Kind+"_"+Animation,0,person)
	Bladex.AddBipedAction(Kind,Animation,Kind+"_"+Animation,0.0,1.0,0)


def Knight():
	qLoadAnims("Kgt","start_oasis","Kgt_start_oasis","Knight_N")
	qLoadAnims("Kgt","oasis_muraldoble","Kgt_oasis_muraldoble","Knight_N")
	qLoadAnims("Kgt","tablilla_btomb","Kgt_tablilla_btomb","Knight_N")


def Amz():
	qLoadAnims("Amz","start_oasis","Kgt_start_oasis","Amazon_N")
	qLoadAnims("Amz","oasis_muraldoble","Kgt_oasis_muraldoble","Amazon_N")
	qLoadAnims("Amz","tablilla_btomb","Amz_tablilla_btomb","Amazon_N")

def Dwf():
	qLoadAnims("Dwf","start_oasis","Dwf_start_oasis","Dwarf_N")
	qLoadAnims("Dwf","oasis_muraldoble","Kgt_oasis_muraldoble","Dwarf_N")
	qLoadAnims("Dwf","tablilla_btomb","Dwf_tablilla_btomb","Dwarf_N")

def Bar():
	qLoadAnims("Bar","start_oasis","Kgt_start_oasis","Barbarian_N")
	qLoadAnims("Bar","oasis_muraldoble","Kgt_oasis_muraldoble","Barbarian_N")
	qLoadAnims("Bar","tablilla_btomb","Bar_tablilla_btomb","Barbarian_N")


def Vmp():
	qLoadAnims("Vmp","oasis_muraldoble","Vmp_oasis_muraldoble","Vamp")

def Ork():
	qLoadAnims("Ork","laughing1","Ork_laughing1","Ork")
	qLoadAnims("Ork","laughing2","Ork_laughing2","Ork")

def Tkn():
	qLoadAnims("Tkn","death_btomb","Tkn_death_btomb","Knight_Traitor")
