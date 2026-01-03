import Bladex

def qLoadAnims(Kind,Animation,AnimationFile,person,interp = 0):
	Bladex.LoadSampledAnimation("../../Anm/"+AnimationFile+".BMV",Kind+"_"+Animation,0,person,interp)
	Bladex.AddBipedAction(Kind,Animation,Kind+"_"+Animation,0.0,1.0,0)


def Knight():
	qLoadAnims("Kgt","demonio_kaos","Kgt_demonio_kaos","Knight_N")
	qLoadAnims("Kgt","final_02","Kgt_final_02","Knight_N")
	qLoadAnims("Kgt","final_01","Kgt_final_01","Knight_N")

def Amz():
	qLoadAnims("Amz","demonio_kaos","Kgt_demonio_kaos","Amazon_N")
	qLoadAnims("Amz","final_02","Kgt_final_02","Amazon_N")
	qLoadAnims("Amz","final_01","Kgt_final_01","Amazon_N")

def Dwf():
	qLoadAnims("Dwf","demonio_kaos","Kgt_demonio_kaos","Dwarf_N")
	qLoadAnims("Dwf","final_02","Kgt_final_02","Dwarf_N")
	qLoadAnims("Dwf","final_01","Kgt_final_01","Dwarf_N")

def Bar():
	qLoadAnims("Bar","final_01","Kgt_final_01","Barbarian_N")
	qLoadAnims("Bar","final_02","Kgt_final_02","Barbarian_N")
	qLoadAnims("Bar","demonio_kaos","Kgt_demonio_kaos","Barbarian_N")

def Skl():
	Bladex.LoadSampledAnimation("../../Anm/Skl_jog_kaos01.BMV","Skl_jog_kaos01",0)
	Bladex.AddBipedAction("Skl","jog_kaos01","Skl_jog_kaos01",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Skl_jog_kaos02.BMV","Skl_jog_kaos02",0)
	Bladex.AddBipedAction("Skl","jog_kaos02","Skl_jog_kaos02",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Skl_jog_kaos03.BMV","Skl_jog_kaos03",0)
	Bladex.AddBipedAction("Skl","jog_kaos03","Skl_jog_kaos03",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Skl_jog_kaos04.BMV","Skl_jog_kaos04",0)
	Bladex.AddBipedAction("Skl","jog_kaos04","Skl_jog_kaos04",0.0,1.0,0)

def Glm_lv():
	Bladex.LoadSampledAnimation("../../Anm/Glm_fall_kaos.BMV","Glm_fall_kaos",0)
	Bladex.AddBipedAction("Glm_lv","fall_kaos","Glm_fall_kaos",0.0,1.0,0)

def Gdm():
	Bladex.LoadSampledAnimation("../../Anm/Gdm_sombra.BMV","Gdm_sombra",0)
	Bladex.AddBipedAction("Gdm","sombra","Gdm_sombra",0.0,1.0,0)

def Ldm():
	Bladex.LoadSampledAnimation("../../Anm/Ldm_saltarin_enric.BMV","Ldm_saltarin_enric",0)
	Bladex.AddBipedAction("Ldm","saltarin_enric","Ldm_saltarin_enric",0.0,1.0,0)

def Ank():
	Bladex.LoadSampledAnimation("../../Anm/Ank_final_02.BMV","Ank_final_02",0,"DarkLord")
	Bladex.AddBipedAction("Ank","final_02","Ank_final_02",0.0,1.0,0)

	Bladex.LoadSampledAnimation("../../Anm/Ank_pincha_viejo.BMV","Ank_pincha_viejo",0,"DarkLord")
	Bladex.AddBipedAction("Ank","pincha_viejo","Ank_pincha_viejo",0.0,1.0,0)
