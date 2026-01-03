import Bladex

#qLoadAnims("Dwf",,"Dwarf_N")
#qLoadAnims("Kgt",,"Knight_N")
#qLoadAnims("Amz",,"Amazon_N")
#qLoadAnims("Bar",,"Barbarian_N")

def qLoadAnims(Kind,Animation,AnimationFile,person):
	Bladex.LoadSampledAnimation("../../Anm/"+AnimationFile+".BMV",AnimationFile,0,person)
	Bladex.AddBipedAction(Kind,Animation,AnimationFile,0.0,1.0,0)

def Dwf():
	qLoadAnims("Dwf","start_isla","Dwf_start_isla","Dwarf_N")
	qLoadAnims("Dwf","sombra_vampiro","Dwf_sombra_vampiro","Dwarf_N")
	qLoadAnims("Dwf","sala_tablillas","Dwf_sala_tablillas","Dwarf_N")
	qLoadAnims("Dwf","aparicion_vampiro","Kgt_aparicion_vampiro","Dwarf_N")
	qLoadAnims("Dwf","isla_mira_mural","Kgt_isla_mira_mural","Dwarf_N")

def Amz():
	qLoadAnims("Amz","sala_tablillas","Kgt_sala_tablillas","Amazon_N")
	qLoadAnims("Amz","start_isla","Kgt_start_isla","Amazon_N")
	qLoadAnims("Amz","aparicion_vampiro","Kgt_aparicion_vampiro","Amazon_N")
	qLoadAnims("Amz","sombra_vampiro","Kgt_sombra_vampiro","Amazon_N")
	qLoadAnims("Amz","isla_mira_mural","Kgt_isla_mira_mural","Amazon_N")

def Bar():
	qLoadAnims("Bar","sala_tablillas","Kgt_sala_tablillas","Barbarian_N")
	qLoadAnims("Bar","start_isla","Kgt_start_isla","Barbarian_N")
	qLoadAnims("Bar","aparicion_vampiro","Kgt_aparicion_vampiro","Barbarian_N")
	qLoadAnims("Bar","sombra_vampiro","Kgt_sombra_vampiro","Barbarian_N")
	qLoadAnims("Bar","isla_mira_mural","Kgt_isla_mira_mural","Barbarian_N")


def Knight():
	qLoadAnims("Kgt","sala_tablillas","Kgt_sala_tablillas","Knight_N")
	qLoadAnims("Kgt","start_isla","Kgt_start_isla","Knight_N")
	qLoadAnims("Kgt","aparicion_vampiro","Kgt_aparicion_vampiro","Knight_N")
	qLoadAnims("Kgt","sombra_vampiro","Kgt_sombra_vampiro","Knight_N")
	qLoadAnims("Kgt","isla_mira_mural","Kgt_isla_mira_mural","Knight_N")


def Vmp():
	qLoadAnims("Vmp","aparicion_vampiro","Vmp_aparicion_vampiro","")
	qLoadAnims("Vmp","escena01","Vmp_escena01","")
	qLoadAnims("Vmp","cansado","Vmp_cansado","")
	qLoadAnims("Vmp","sombra","Vmp_sombra","")

def Ldm():
	qLoadAnims("Ldm","appears","Ldm_appears","Little_Demon")

def Skl():
	qLoadAnims("Skl","appears1","Skl_appears1","Skeleton")