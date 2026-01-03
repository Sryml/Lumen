import Bladex

def qLoadAnims(Kind,Animation,AnimationFile,person):
	Bladex.LoadSampledAnimation("../../Anm/"+AnimationFile+".BMV",Kind+"_"+Animation,0,person)
	Bladex.AddBipedAction(Kind,Animation,Kind+"_"+Animation,0.0,1.0,0)


def Knight():
	qLoadAnims("Kgt","tke_orb","Kgt_tke_orb","Knight_N")
	qLoadAnims("Kgt","inicio_desfil","Kgt_inicio_desfil","Knight_N")
	qLoadAnims("Kgt","use_magic_key","Kgt_use_magic_key","Knight_N")
	qLoadAnims("Kgt","tke_key_orlok","Kgt_tke_key_orlok","Knight_N")

def Dwf():
	qLoadAnims("Dwf","tke_orb","Dwf_tke_orb","Dwarf_N")
	qLoadAnims("Dwf","inicio_desfil","Dwf_inicio_desfil","Dwarf_N")
	qLoadAnims("Dwf","use_magic_key","Kgt_use_magic_key","Dwarf_N")
	qLoadAnims("Dwf","tke_key_orlok","Dwf_tke_key_orlok","Dwarf_N")

def Bar():
	qLoadAnims("Bar","tke_orb","Bar_tke_orb","Barbarian_N")
	qLoadAnims("Bar","inicio_desfil","Bar_inicio_desfil","Barbarian_N")
	qLoadAnims("Bar","use_magic_key","Bar_use_magic_key","Barbarian_N")
	qLoadAnims("Bar","tke_key_orlok","Bar_tke_key_orlok","Barbarian_N")

def Amz():
	qLoadAnims("Amz","tke_orb","Amz_tke_orb","Amazon_N")
	qLoadAnims("Amz","inicio_desfil","Kgt_inicio_desfil","Amazon_N")
	qLoadAnims("Amz","use_magic_key","Kgt_use_magic_key","Amazon_N")
	qLoadAnims("Amz","tke_key_orlok","Kgt_tke_key_orlok","Amazon_N")

def Lch():
	qLoadAnims("Lch","appears1","Lch_appears1","Lich")

def Trl():
	qLoadAnims("Trl","orlok_brk_wll","Trl_orlok_brk_wll","Troll_Dark")

def Glm_st():
	qLoadAnims("Glm","raise_snow","Glm_raise_snow","Golem_stone")
