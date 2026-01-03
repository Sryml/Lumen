import Bladex

def qLoadAnims(Kind,Animation,AnimationFile,person,interp = 0):
	Bladex.LoadSampledAnimation("../../Anm/"+AnimationFile+".BMV",Kind+"_"+Animation,0,person,interp)
	Bladex.AddBipedAction(Kind,Animation,Kind+"_"+Animation,0.0,1.0,0)


def Knight():
	qLoadAnims("Kgt","dth_rockfront","Kgt_dth_rockfront","Knight_N")
	qLoadAnims("Kgt","drop_magic_key","Kgt_drop_magic_key","Knight_N")
	qLoadAnims("Kgt","diosa_start","Kgt_diosa_start","Knight_N")
	qLoadAnims("Kgt","coger_blade","Kgt_coger_blade","Knight_N")
	qLoadAnims("Kgt","blade_tablillas_no","Kgt_blade_tablillas_no","Knight_N")
	qLoadAnims("Kgt","blade_solotablas","Kgt_blade_solotablas","Knight_N")
	qLoadAnims("Kgt","blade_faltantablillas","Kgt_blade_faltantablillas","Knight_N")
	qLoadAnims("Kgt","powerblade","Kgt_powerblade","Knight_N")


def Amz():
	qLoadAnims("Amz","dth_rockfront","Kgt_dth_rockfront","Amazon_N")
	qLoadAnims("Amz","drop_magic_key","Kgt_drop_magic_key","Amazon_N")
	qLoadAnims("Amz","diosa_start","Kgt_diosa_start","Amazon_N")
	qLoadAnims("Amz","coger_blade","Amz_coger_blade","Amazon_N")
	qLoadAnims("Amz","blade_tablillas_no","Amz_blade_tablillas_no","Amazon_N")
	qLoadAnims("Amz","blade_solotablas","Amz_blade_solotablas","Amazon_N")
	qLoadAnims("Amz","blade_faltantablillas","Amz_blade_faltantablillas","Amazon_N")
	qLoadAnims("Amz","powerblade","Amz_powerblade","Amazon_N")

def Dwf():
	qLoadAnims("Dwf","dth_rockfront","Kgt_dth_rockfront","Dwarf_N")
	qLoadAnims("Dwf","drop_magic_key","Kgt_drop_magic_key","Dwarf_N")
	qLoadAnims("Dwf","diosa_start","Kgt_diosa_start","Dwarf_N")
	qLoadAnims("Dwf","coger_blade","Dwf_coger_blade","Dwarf_N")
	qLoadAnims("Dwf","blade_tablillas_no","Dwf_blade_tablillas_no","Dwarf_N")
	qLoadAnims("Dwf","blade_solotablas","Dwf_blade_solotablas","Dwarf_N")
	qLoadAnims("Dwf","blade_faltantablillas","Dwf_blade_faltantablillas","Dwarf_N")
	qLoadAnims("Dwf","powerblade","Dwf_powerblade","Dwarf_N")

def Bar():
	qLoadAnims("Bar","dth_rockfront","Kgt_dth_rockfront","Barbarian_N")
	qLoadAnims("Bar","drop_magic_key","Kgt_drop_magic_key","Barbarian_N")
	qLoadAnims("Bar","diosa_start","Kgt_diosa_start","Barbarian_N")
	qLoadAnims("Bar","coger_blade","Bar_coger_blade","Barbarian_N")
	qLoadAnims("Bar","blade_tablillas_no","Bar_blade_tablillas_no","Barbarian_N")
	qLoadAnims("Bar","blade_solotablas","Kgt_blade_solotablas","Barbarian_N")
	qLoadAnims("Bar","blade_faltantablillas","Bar_blade_faltantablillas","Barbarian_N")
	qLoadAnims("Bar","powerblade","Bar_powerblade","Barbarian_N")


def Ork():
	qLoadAnims("Ork","ejer1","Ork_ejer1","Ork")
	qLoadAnims("Ork","ejer2","Ork_ejer2","Ork")
	qLoadAnims("Ork","ejer_bow","Ork_ejer_bow","Ork")
	qLoadAnims("Ork","ejer5","Ork_ejer5","Ork")
	qLoadAnims("Ork","ejer4","Ork_ejer4","Ork")
	qLoadAnims("Ork","ejercito8","Ork_ejercito8","Ork")
	qLoadAnims("Ork","ejercito7","Ork_ejercito7","Ork")
	qLoadAnims("Ork","ejercito4","Ork_ejercito4","Ork")
	qLoadAnims("Ork","ejercito5","Ork_ejercito5","Ork")

def Gok():
	qLoadAnims("Gor","ejer3","Gor_ejer3","Great_Ork")
	qLoadAnims("Gor","ejercito6","Gor_ejercito6","Great_Ork")
