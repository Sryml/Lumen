import Bladex

def Knight():
	Bladex.LoadSampledAnimation("../../Anm/Kgt_escena01_mina.BMV","Kgt_escena01_mina",0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_final_mina.bmv","Kgt_final_mina",0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_ambush_mine.bmv","Kgt_ambush_mine",0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_tablilla_tumba.BMV","Kgt_tablilla_tumba",0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_tumba_rey.BMV","Kgt_tumba_rey",0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_reina_start.BMV","Kgt_reina_start",0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_abrirsarcofago.BMV","Kgt_abrirsarcofago",0)

	Bladex.AddBipedAction("Kgt","escena01_mina","Kgt_escena01_mina",0.0,1.0,0)
	Bladex.AddBipedAction("Kgt","final_mina","Kgt_final_mina",0.0,1.0,0)
	Bladex.AddBipedAction("Kgt","ambush_mine","Kgt_ambush_mine",0.0,1.0,0)
	Bladex.AddBipedAction("Kgt","tablilla_tumba","Kgt_tablilla_tumba",0.0,1.0,0)
	Bladex.AddBipedAction("Kgt","tumba_rey","Kgt_tumba_rey",0.0,1.0,0)
	Bladex.AddBipedAction("Kgt","reina_start","Kgt_reina_start",0.0,1.0,0)
	Bladex.AddBipedAction("Kgt","abrirsarcofago","Kgt_abrirsarcofago",0.0,1.0,0)

def Amz():
	Bladex.LoadSampledAnimation("../../Anm/Kgt_escena01_mina.BMV","Amz_escena01_mina",0,"Amazon_N")
	Bladex.LoadSampledAnimation("../../Anm/Kgt_final_mina.bmv","Amz_final_mina",0,"Amazon_N")
	Bladex.LoadSampledAnimation("../../Anm/Kgt_ambush_mine.bmv","Amz_ambush_mine",0,"Amazon_N")
	Bladex.LoadSampledAnimation("../../Anm/Amz_tablilla_tumba.BMV","Amz_tablilla_tumba",0)
	Bladex.LoadSampledAnimation("../../Anm/Amz_tumba_rey.BMV","Amz_tumba_rey",0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_reina_start.BMV","Amz_reina_start",0,"Amazon_N")
	Bladex.LoadSampledAnimation("../../Anm/Amz_abrirsarcofago.BMV","Amz_abrirsarcofago",0,"Knight_N")

	Bladex.AddBipedAction("Amz","escena01_mina","Amz_escena01_mina",0.0,1.0,0)
	Bladex.AddBipedAction("Amz","final_mina","Amz_final_mina",0.0,1.0,0)
	Bladex.AddBipedAction("Amz","ambush_mine","Amz_ambush_mine",0.0,1.0,0)
	Bladex.AddBipedAction("Amz","tablilla_tumba","Amz_tablilla_tumba",0.0,1.0,0)
	Bladex.AddBipedAction("Amz","tumba_rey","Amz_tumba_rey",0.0,1.0,0)
	Bladex.AddBipedAction("Amz","reina_start","Amz_reina_start",0.0,1.0,0)
	Bladex.AddBipedAction("Amz","abrirsarcofago","Amz_abrirsarcofago",0.0,1.0,0)

def Bar():
	Bladex.LoadSampledAnimation("../../Anm/Kgt_escena01_mina.BMV","Bar_escena01_mina",0,"Barbarian_N")
	Bladex.LoadSampledAnimation("../../Anm/Kgt_final_mina.bmv","Bar_final_mina",0,"Barbarian_N")
	Bladex.LoadSampledAnimation("../../Anm/Kgt_ambush_mine.bmv","Bar_ambush_mine",0,"Barbarian_N")
	Bladex.LoadSampledAnimation("../../Anm/Bar_tablilla_tumba.BMV","Bar_tablilla_tumba",0)
	Bladex.LoadSampledAnimation("../../Anm/Bar_tumba_rey.BMV","Bar_tumba_rey",0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_reina_start.BMV","Kgt_reina_start",0,"Knight_N")
	Bladex.LoadSampledAnimation("../../Anm/Kgt_abrirsarcofago.BMV","Bar_abrirsarcofago",0,"Barbarian_N")

	Bladex.AddBipedAction("Bar","escena01_mina","Bar_escena01_mina",0.0,1.0,0)
	Bladex.AddBipedAction("Bar","final_mina","Bar_final_mina",0.0,1.0,0)
	Bladex.AddBipedAction("Bar","ambush_mine","Bar_ambush_mine",0.0,1.0,0)
	Bladex.AddBipedAction("Bar","tablilla_tumba","Bar_tablilla_tumba",0.0,1.0,0)
	Bladex.AddBipedAction("Bar","tumba_rey","Bar_tumba_rey",0.0,1.0,0)
	Bladex.AddBipedAction("Bar","reina_start","Kgt_reina_start",0.0,1.0,0)
	Bladex.AddBipedAction("Bar","abrirsarcofago","Bar_abrirsarcofago",0.0,1.0,0)


def Dwf():
	Bladex.LoadSampledAnimation("../../Anm/Dwf_escena01_mina.BMV","Dwf_escena01_mina",0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_final_mina.bmv","Dwf_final_mina",0,"Dwarf_N")
	Bladex.LoadSampledAnimation("../../Anm/Kgt_ambush_mine.bmv","Dwf_ambush_mine",0,"Dwarf_N")
	Bladex.LoadSampledAnimation("../../Anm/Dwf_tablilla_tumba.BMV","Dwf_tablilla_tumba",0)
	Bladex.LoadSampledAnimation("../../Anm/Dwf_tumba_rey.BMV","Dwf_tumba_rey",0)
	Bladex.LoadSampledAnimation("../../Anm/Dwf_reina_start.BMV","Dwf_reina_start",0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_abrirsarcofago.BMV","Dwf_abrirsarcofago",0,"Dwarf_N")

	Bladex.AddBipedAction("Dwf","escena01_mina","Dwf_escena01_mina",0.0,1.0,0)
	Bladex.AddBipedAction("Dwf","final_mina","Dwf_final_mina",0.0,1.0,0)
	Bladex.AddBipedAction("Dwf","ambush_mine","Dwf_ambush_mine",0.0,1.0,0)
	Bladex.AddBipedAction("Dwf","tablilla_tumba","Dwf_tablilla_tumba",0.0,1.0,0)
	Bladex.AddBipedAction("Dwf","tumba_rey","Dwf_tumba_rey",0.0,1.0,0)
	Bladex.AddBipedAction("Dwf","reina_start","Dwf_reina_start",0.0,1.0,0)
	Bladex.AddBipedAction("Dwf","abrirsarcofago","Dwf_abrirsarcofago",0.0,1.0,0)

def Spd():
	Bladex.LoadSampledAnimation("../../Anm/Spd_1_mina_01.bmv","Spd_1_mina_01",0,"Spidersmall",20)
	Bladex.LoadSampledAnimation("../../Anm/Spd_2_mina_01.bmv","Spd_2_mina_01",0,"Spidersmall",20)
	Bladex.LoadSampledAnimation("../../Anm/Spd_3_mina_01.bmv","Spd_3_mina_01",0,"Spidersmall",20)

	Bladex.AddBipedAction("Spd","1_mina_01","Spd_1_mina_01",0.0,1.0,0)
	Bladex.AddBipedAction("Spd","2_mina_01","Spd_2_mina_01",0.0,1.0,0)
	Bladex.AddBipedAction("Spd","3_mina_01","Spd_3_mina_01",0.0,1.0,0)

def Skl():
	Bladex.LoadSampledAnimation("../../Anm/Skl_tumba_rey.bmv","Skl_tumba_rey_aguila",0)

	Bladex.AddBipedAction("Skl","tumba_rey_aguila","Skl_tumba_rey_aguila",0.0,1.0,0)

def Ork():
	Bladex.LoadSampledAnimation("../../Anm/Ork_jmp_elevator.BMV","Ork_jmp_elevator",0)

	Bladex.AddBipedAction("Ork","jmp_elevator","Ork_jmp_elevator",0.0,1.0,0)

def Glm_st():
	Bladex.LoadSampledAnimation("../../Anm/Glm_break_wall.BMV","Glm_break_wall",0)

	Bladex.AddBipedAction("Glm_st","break_wall","Glm_break_wall",0.0,1.0,0)

# Estas creo que estan en el conjunto de animaciones del personaje

#("Chg_r")
#("Chg_r_l")
#("Fire1")
