import Bladex

def qLoadAnims(Kind,Animation,AnimationFile,person,interp = 0):
	Bladex.LoadSampledAnimation("../../Anm/"+AnimationFile+".BMV",Kind+"_"+Animation,0,person,interp)
	Bladex.AddBipedAction(Kind,Animation,Kind+"_"+Animation,0.0,1.0,0)

def Knight():
	qLoadAnims("Kgt","inicio_torre","Kgt_inicio_torre","Knight_N")
	qLoadAnims("Kgt","demoniogurak","Kgt_demoniogurak","Knight_N")
	qLoadAnims("Kgt","dalgurak_appears3","Kgt_dalgurak_appears3","Knight_N")

def Amz():
	qLoadAnims("Amz","inicio_torre","Kgt_inicio_torre","Amazon_N")
	qLoadAnims("Amz","demoniogurak","Kgt_demoniogurak","Amazon_N")
	qLoadAnims("Amz","dalgurak_appears3","Kgt_dalgurak_appears3","Amazon_N")

def Dwf():
	qLoadAnims("Dwf","inicio_torre","Dwf_inicio_torre","Dwarf_N")
	qLoadAnims("Dwf","demoniogurak","Kgt_demoniogurak","Dwarf_N")
	qLoadAnims("Dwf","dalgurak_appears3","Dwf_dalgurak_appears3","Dwarf_N")


def Bar():
	qLoadAnims("Bar","inicio_torre","Kgt_inicio_torre","Barbarian_N")
	qLoadAnims("Bar","demoniogurak","Kgt_demoniogurak","Barbarian_N")
	qLoadAnims("Bar","dalgurak_appears3","Bar_dalgurak_appears3","Barbarian_N")


def Ldm():
	qLoadAnims("Ldm","_appears","Ldm_appears","Little_Demon")

def Gdm():
	qLoadAnims("Gdm","demoniogurak","Gdm_demoniogurak","Great_Demon")

def Dgk():
	qLoadAnims("Dgk","first_appears","Dgk_first_appears","DalGurak")
	qLoadAnims("Dgk","demoniogurak","Dgk_demoniogurak","DalGurak")
	qLoadAnims("Dgk","appears3","Dgk_appears3","DalGurak")
