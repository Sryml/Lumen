import Bladex

def qLoadAnims(Kind,Animation,AnimationFile,person,interp = 0,flag=0):
	Bladex.LoadSampledAnimation("../../Anm/"+AnimationFile+".BMV",Kind+"_"+Animation,flag,person,interp)
	Bladex.AddBipedAction(Kind,Animation,Kind+"_"+Animation,0.0,1.0,0)

def qLoadAct(Kind,Animation,AnimationFile,person):
	Bladex.LoadSampledAnimation("../../Anm/"+AnimationFile+".BMV",Kind+"_"+Animation,1,person)

def Knight():
	qLoadAnims("Kgt","start_volcan","Kgt_start_volcan","Knight_N")
	qLoadAnims("Kgt","aparecen_4_demonios","Kgt_aparecen_4_demonios","Knight_N")
	qLoadAnims("Kgt","cae_lava","Kgt_cae_lava","Knight_N")

def Amz():
	qLoadAnims("Amz","start_volcan","Kgt_start_volcan","Amazon_N")
	qLoadAnims("Amz","aparecen_4_demonios","Kgt_aparecen_4_demonios","Amazon_N")
	qLoadAnims("Amz","cae_lava","Kgt_cae_lava","Amazon_N")

def Dwf():
	qLoadAnims("Dwf","start_volcan","Dwf_start_volcan","Dwarf_N")
	qLoadAnims("Dwf","aparecen_4_demonios","Dwf_aparecen_4_demonios","Dwarf_N")
	qLoadAnims("Dwf","cae_lava","Dwf_cae_lava","Dwarf_N")

def Bar():
	qLoadAnims("Bar","start_volcan","Kgt_start_volcan","Barbarian_N")
	qLoadAnims("Bar","aparecen_4_demonios","Kgt_aparecen_4_demonios","Barbarian_N")
	qLoadAnims("Bar","cae_lava","Bar_cae_lava","Barbarian_N")

def Ldm():
	qLoadAnims("Ldm","appears","Ldm_appears","Little_Demon")

def Glm_lv():
	qLoadAnims("Glm","awake","Glm_awake","Golem_lava")

def Min():
	qLoadAnims("Min","1_escena01_volcan","Min_1_escena01_volcan","Minotaur")
