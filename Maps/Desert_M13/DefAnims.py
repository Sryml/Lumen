import Bladex

def qLoadAnims(Kind,Animation,AnimationFile,person):
	Bladex.LoadSampledAnimation("../../Anm/"+AnimationFile+".BMV",Kind+"_"+Animation,0,person)
	Bladex.AddBipedAction(Kind,Animation,Kind+"_"+Animation,0.0,1.0,0)

def Knight():
	qLoadAnims("Kgt","tke_key","Kgt_tke_key","Knight_N")
	qLoadAnims("Kgt","start_desierto","Kgt_start_desierto","Knight_N")
	qLoadAnims("Kgt","bag","Kgt_bag","Knight_N")
	qLoadAnims("Kgt","pour","Kgt_pour","Knight_N")
	qLoadAnims("Kgt","tablilla_tumba","Kgt_tablilla_tumba","Knight_N")

def Amz():
	qLoadAnims("Amz","tke_key","Amz_tke_key","Amazon_N")
	qLoadAnims("Amz","start_desierto","Amz_start_desierto","Amazon_N")
	qLoadAnims("Amz","bag","Kgt_bag","Amazon_N")
	qLoadAnims("Amz","pour","Kgt_pour","Amazon_N")
	qLoadAnims("Amz","tablilla_tumba","Amz_tablilla_tumba","Amazon_N")

def Dwf():
	qLoadAnims("Dwf","tke_key","Dwf_tke_key","Dwarf_N")
	qLoadAnims("Dwf","start_desierto","Dwf_start_desierto","Dwarf_N")
	qLoadAnims("Dwf","bag","Dwf_bag","Dwarf_N")
	qLoadAnims("Dwf","pour","Kgt_pour","Dwarf_N")
	qLoadAnims("Dwf","tablilla_tumba","Dwf_tablilla_tumba","Dwarf_N")

def Bar():
	qLoadAnims("Bar","tke_key","Bar_tke_key","Barbarian_N")
	qLoadAnims("Bar","start_desierto","Bar_start_desierto","Barbarian_N")
	qLoadAnims("Bar","bag","Kgt_bag","Barbarian_N")
	qLoadAnims("Bar","pour","Kgt_pour","Barbarian_N")
	qLoadAnims("Bar","tablilla_tumba","Bar_tablilla_tumba","Barbarian_N")
