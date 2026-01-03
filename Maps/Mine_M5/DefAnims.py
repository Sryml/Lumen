### Animaciones ###
import Bladex

def Bar():
	Bladex.LoadSampledAnimation("../../Anm/Bar_start_mina.bmv","Bar_start_mina",0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_ambush_mine.bmv","Bar_ambush_mine",0,"Barbarian_N")
	Bladex.LoadSampledAnimation("../../Anm/Kgt_escena01_mina.bmv","Bar_escena01_mina",0,"Barbarian_N")
	Bladex.LoadSampledAnimation("../../Anm/Bar_escena_mina_acido.bmv","Bar_escena_mina_acido",0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_final_mina.bmv","Bar_final_mina",0,"Barbarian_N")

	Bladex.AddBipedAction("Bar","start_mina","Bar_start_mina",0.0,1.0,0)
	Bladex.AddBipedAction("Bar","ambush_mine","Bar_ambush_mine",0.0,1.0,0)
	Bladex.AddBipedAction("Bar","escena01_mina","Bar_escena01_mina",0.0,1.0,0)
	Bladex.AddBipedAction("Bar","escena_mina_acido","Bar_escena_mina_acido",0.0,1.0,0)
	Bladex.AddBipedAction("Bar","final_mina","Bar_final_mina",0.0,1.0,0)

def Knight():
	Bladex.LoadSampledAnimation("../../Anm/Kgt_start_mina.bmv","Kgt_start_mina",0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_ambush_mine.bmv","Kgt_ambush_mine",0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_escena01_mina.bmv","Kgt_escena01_mina",0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_escena_mina_acido.bmv","Kgt_escena_mina_acido",0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_final_mina.bmv","Kgt_final_mina",0)

	Bladex.AddBipedAction("Knight","start_mina","Kgt_start_mina",0.0,1.0,0)
	Bladex.AddBipedAction("Knight","ambush_mine","Kgt_ambush_mine",0.0,1.0,0)
	Bladex.AddBipedAction("Knight","escena01_mina","Kgt_escena01_mina",0.0,1.0,0)
	Bladex.AddBipedAction("Knight","escena_mina_acido","Kgt_escena_mina_acido",0.0,1.0,0)
	Bladex.AddBipedAction("Knight","final_mina","Kgt_final_mina",0.0,1.0,0)

def Amz():
	Bladex.LoadSampledAnimation("../../Anm/Amz_start_mina.bmv","Amz_start_mina",0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_ambush_mine.bmv","Amz_ambush_mine",0,"Amazon_L")
	Bladex.LoadSampledAnimation("../../Anm/Kgt_escena01_mina.bmv","Amz_escena01_mina",0,"Amazon_L")
	Bladex.LoadSampledAnimation("../../Anm/Amz_escena_mina_acido.bmv","Amz_escena_mina_acido",0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_final_mina.bmv","Amz_final_mina",0,"Amazon_L")

	Bladex.AddBipedAction("Amz","start_mina","Amz_start_mina",0.0,1.0,0)
	Bladex.AddBipedAction("Amz","ambush_mine","Amz_ambush_mine",0.0,1.0,0)
	Bladex.AddBipedAction("Amz","escena01_mina","Amz_escena01_mina",0.0,1.0,0)
	Bladex.AddBipedAction("Amz","escena_mina_acido","Amz_escena_mina_acido",0.0,1.0,0)
	Bladex.AddBipedAction("Amz","final_mina","Amz_final_mina",0.0,1.0,0)

def Dwf():
	Bladex.LoadSampledAnimation("../../Anm/Dwf_start_mina.bmv","Dwf_start_mina",0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_ambush_mine.bmv","Dwf_ambush_mine",0,"Dwarf_N")
	Bladex.LoadSampledAnimation("../../Anm/Dwf_escena01_mina.bmv","Dwf_escena01_mina",0)
	Bladex.LoadSampledAnimation("../../Anm/Dwf_escena_mina_acido.bmv","Dwf_escena_mina_acido",0)
	Bladex.LoadSampledAnimation("../../Anm/Kgt_final_mina.bmv","Dwf_final_mina",0,"Dwarf_N")

	Bladex.AddBipedAction("Dwf","start_mina","Dwf_start_mina",0.0,1.0,0)
	Bladex.AddBipedAction("Dwf","ambush_mine","Dwf_ambush_mine",0.0,1.0,0)
	Bladex.AddBipedAction("Dwf","escena01_mina","Dwf_escena01_mina",0.0,1.0,0)
	Bladex.AddBipedAction("Dwf","escena_mina_acido","Dwf_escena_mina_acido",0.0,1.0,0)
	Bladex.AddBipedAction("Dwf","final_mina","Dwf_final_mina",0.0,1.0,0)

def Ork():
	Bladex.LoadSampledAnimation("../../Anm/Ork_1_ambush_mine.bmv","Ork_1_ambush_mine",0)
	Bladex.LoadSampledAnimation("../../Anm/Ork_2_ambush_mine.bmv","Ork_2_ambush_mine",0)
	Bladex.LoadSampledAnimation("../../Anm/Ork_3_ambush_mine.bmv","Ork_3_ambush_mine",0)
	Bladex.LoadSampledAnimation("../../Anm/Ork_jmp_elevator.bmv","Ork_jmp_elevator",0)

	Bladex.AddBipedAction("Ork","1_ambush_mine","Ork_1_ambush_mine",0.0,1.0,0)
	Bladex.AddBipedAction("Ork","2_ambush_mine","Ork_2_ambush_mine",0.0,1.0,0)
	Bladex.AddBipedAction("Ork","3_ambush_mine","Ork_3_ambush_mine",0.0,1.0,0)
	Bladex.AddBipedAction("Ork","jmp_elevator","Ork_jmp_elevator",0.0,1.0,0)

def Spd():
	Bladex.LoadSampledAnimation("../../Anm/Spd_1_mina_01.bmv","Spd_1_mina_01",0,"Spidersmall",20)
	Bladex.LoadSampledAnimation("../../Anm/Spd_2_mina_01.bmv","Spd_2_mina_01",0,"Spidersmall",20)
	Bladex.LoadSampledAnimation("../../Anm/Spd_3_mina_01.bmv","Spd_3_mina_01",0,"Spidersmall",20)

	Bladex.AddBipedAction("Spd","1_mina_01","Spd_1_mina_01",0.0,1.0,0)
	Bladex.AddBipedAction("Spd","2_mina_01","Spd_2_mina_01",0.0,1.0,0)
	Bladex.AddBipedAction("Spd","3_mina_01","Spd_3_mina_01",0.0,1.0,0)
