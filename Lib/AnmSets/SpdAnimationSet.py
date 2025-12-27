import Bladex
import Enm_Def

#	JOG_ANM
#	#                     Name      WUEA,MOD_Y,SOLF,COPY_ROT,BNG_MOV,HEADF
#	Bladex.AddAnimFlags("Cos_attack_f",0,0,0,1,Enm_Def.BM_XYZ,Enm_Def.HEADF_ENG)
#
#
#
#
#



def LoadSpdAnimationSet(ct_name):

	print "Loading the Spider animation sets..."

	#### Movimientos normales ####


	Bladex.LoadSampledAnimation("../../Anm/Spd_wlk_no.BMV","Spd_wlk_no",1)
	Bladex.AddAnmRStep("Spd_wlk_no",0)
	Bladex.AddAnmRRelease("Spd_wlk_no",0.061)
	Bladex.AddAnmRStep("Spd_wlk_no",0.197)
	Bladex.AddAnmRRelease("Spd_wlk_no",0.262)
	Bladex.AddAnmRStep("Spd_wlk_no",0.391)
	Bladex.AddAnmRRelease("Spd_wlk_no",0.443)
	Bladex.AddAnmRStep("Spd_wlk_no",0.591)
	Bladex.AddAnmRRelease("Spd_wlk_no",0.651)
	Bladex.AddAnmRStep("Spd_wlk_no",0.789)
	Bladex.AddAnmRRelease("Spd_wlk_no",0.839)
	Bladex.AddAnmRStep("Spd_wlk_no",1)

	Bladex.AddAnmLStep("Spd_wlk_no",0.0)
	Bladex.AddAnmLRelease("Spd_wlk_no",0.198)
	Bladex.AddAnmLStep("Spd_wlk_no",0.345)
	Bladex.AddAnmLRelease("Spd_wlk_no",0.394)
	Bladex.AddAnmLStep("Spd_wlk_no",0.547)
	Bladex.AddAnmLRelease("Spd_wlk_no",0.592)
	Bladex.AddAnmLStep("Spd_wlk_no",0.751)
	Bladex.AddAnmLRelease("Spd_wlk_no",0.788)
	Bladex.AddAnmLStep("Spd_wlk_no",0.956)


	Bladex.AddStopTests("Spd_wlk_no")



#	Bladex.LoadSampledAnimation("../../Anm/Spd_clmb_low.BMV","Spd_clmb_low",0)
#	Bladex.AddAnmRStep("Spd_clmb_low",0)
#	Bladex.AddAnmLStep("Spd_clmb_low",0)
#	Bladex.AddAnmLRelease("Spd_clmb_low",0.369)
#	Bladex.AddAnmRRelease("Spd_clmb_low",0.369)
#	Bladex.AddAnmRStep("Spd_clmb_low",0.525)
#	Bladex.AddAnmLStep("Spd_clmb_low",0.525)
#	Bladex.AddStopTests("Spd_wlk_no")



	Bladex.LoadSampledAnimation("../../Anm/Spd_jmp_no.BMV","Spd_jmp_no",0)
	Bladex.AddAnmRStep("Spd_jmp_no",0)
	Bladex.AddAnmLStep("Spd_jmp_no",0)
	Bladex.AddAnmLRelease("Spd_jmp_no",0.369)
	Bladex.AddAnmRRelease("Spd_jmp_no",0.369)
	Bladex.AddAnmRStep("Spd_jmp_no",0.525)
	Bladex.AddAnmLStep("Spd_jmp_no",0.525)
	#Bladex.AddStopTests("Spd_jmp_no")


	Bladex.LoadSampledAnimation("../../Anm/Spd_jmph_no.BMV","Spd_jmph_no",0)
	Bladex.AddAnmRStep("Spd_jmph_no",0)
	Bladex.AddAnmLStep("Spd_jmph_no",0)
	Bladex.AddAnmLRelease("Spd_jmph_no",0.369)
	Bladex.AddAnmRRelease("Spd_jmph_no",0.369)
	Bladex.AddAnmRStep("Spd_jmph_no",0.525)
	Bladex.AddAnmLStep("Spd_jmph_no",0.525)
	#Bladex.AddStopTests("Spd_jmph_no")


	Bladex.LoadSampledAnimation("../../Anm/Spd_jog_no.BMV","Spd_jog_no",1)
	Bladex.AddAnmRStep("Spd_jog_no",0)
	Bladex.AddAnmRRelease("Spd_jog_no",0.475)
	Bladex.AddAnmLStep("Spd_jog_no",0.648)
	Bladex.AddAnmRStep("Spd_jog_no",1)
	Bladex.AddAnmLRelease("Spd_jog_no",1)
	Bladex.AddStopTests("Spd_jog_no")


	Bladex.LoadSampledAnimation("../../Anm/Spd_rlx_no.BMV","Spd_rlx_no",1)
	Bladex.AddAnmRStep("Spd_rlx_no",0)
	Bladex.AddAnmLStep("Spd_rlx_no",0)


#	Bladex.LoadSampledAnimation("../../Anm/Spd_t_l_no.BMV","Spd_t_l_no",1)
#	Bladex.AddAnmRStep("Spd_t_l_no",0)
#	Bladex.AddAnmRRelease("Spd_t_l_no",0.205)
#	Bladex.AddAnmRStep("Spd_t_l_no",0.515)
#	Bladex.AddAnmLStep("Spd_t_l_no",0.691)
#	Bladex.AddAnmLRelease("Spd_t_l_no",1)
#	Bladex.AddStopTests("Spd_t_l_no")


#	Bladex.LoadSampledAnimation("../../Anm/Spd_t_r_no.BMV","Spd_t_r_no",1)
#	Bladex.AddAnmRStep("Spd_t_r_no",0)
#	Bladex.AddAnmLStep("Spd_t_r_no",0)
#	Bladex.AddAnmRRelease("Spd_t_r_no",0.310)
#	Bladex.AddAnmLRelease("Spd_t_r_no",0.731)
#	Bladex.AddAnmRStep("Spd_t_r_no",0.818)
#	Bladex.AddAnmLStep("Spd_t_r_no",1)
#	Bladex.AddStopTests("Spd_t_r_no")


	#### Encarado ####



	Bladex.LoadSampledAnimation("../../Anm/Spd_attack_b.BMV","Spd_attack_b",1)

	Bladex.AddAnmRStep("Spd_attack_b",0)
	Bladex.AddAnmLStep("Spd_attack_b",0)
	Bladex.AddAnmRRelease("Spd_attack_b",0.423)
	Bladex.AddAnmLRelease("Spd_attack_b",0.423)
	Bladex.AddAnmRStep("Spd_attack_b",1)
	Bladex.AddAnmLStep("Spd_attack_b",1)
	Bladex.AddStopTests("Spd_attack_b")



############  Muertes

	Bladex.LoadSampledAnimation("../../Anm/Spd_dth0.BMV","Spd_dth0",0)
	Bladex.AddAnmRStep("Spd_dth0",0)
	Bladex.AddAnmLStep("Spd_dth0",0)
	Bladex.AddAnmRRelease("Spd_dth0",0.181)
	Bladex.AddAnmLRelease("Spd_dth0",0.183)

	Bladex.LoadSampledAnimation("../../Anm/Spd_dth2.BMV","Spd_dth2",0)
	Bladex.AddAnmRStep("Spd_dth2",0)
	Bladex.AddAnmLStep("Spd_dth2",0)
	Bladex.AddAnmRRelease("Spd_dth2",0.072)
	Bladex.AddAnmLRelease("Spd_dth2",0.072)


###########  Caidas

	Bladex.LoadSampledAnimation("../../Anm/Spd_fll_low_no.BMV","Spd_fll_low_no",0)
	Bladex.AddAnmRStep("Spd_fll_low_no",0.341)
	Bladex.AddAnmLStep("Spd_fll_low_no",0.341)

	#Caida enorme
	Bladex.LoadSampledAnimation("../../Anm/Spd_dth_fll.BMV","Dth_Fll_Spd",0)
	Bladex.LoadSampledAnimation("../../Anm/Spd_dth_fll2.BMV","Dth_Fll2_Spd",0)
	Bladex.AddAnmRStep("Dth_Fll2_Spd",0.0)
	Bladex.AddAnmLStep("Dth_Fll2_Spd",0.0)


#########  Ataques

	Bladex.LoadSampledAnimation("../../Anm/Spd_g_01.BMV","Spd_g_01",0)
	Bladex.AddAnmRStep("Spd_g_01",0)
	Bladex.AddAnmLStep("Spd_g_01",0)

#	Bladex.LoadSampledAnimation("../../Anm/Spd_g_02.BMV","Spd_g_02",0)
#	Bladex.AddAnmRStep("Spd_g_02",0)
#	Bladex.AddAnmLStep("Spd_g_02",0)

	Bladex.LoadSampledAnimation("../../Anm/Spd_g_spit.BMV","Spd_g_spit",0)
	Bladex.AddAnmRStep("Spd_g_spit",0)
	Bladex.AddAnmLStep("Spd_g_spit",0)






########   Heridas

	Bladex.LoadSampledAnimation("../../Anm/Spd_hurt_big.BMV","Spd_hurt_big",0)
	Bladex.AddAnmRStep("Spd_hurt_big",0)
	Bladex.AddAnmLStep("Spd_hurt_big",0)
	Bladex.AddAnmRRelease("Spd_hurt_big",0.205)
	Bladex.AddAnmLRelease("Spd_hurt_big",0.205)
	Bladex.AddAnmRStep("Spd_hurt_big",0.402)
	Bladex.AddAnmLStep("Spd_hurt_big",0.402)


	Bladex.LoadSampledAnimation("../../Anm/Spd_hurt_lite.BMV","Spd_hurt_lite",0)
	Bladex.AddAnmRStep("Spd_hurt_lite",0)
	Bladex.AddAnmLStep("Spd_hurt_lite",0)
	Bladex.AddAnmRRelease("Spd_hurt_big",0.373)
	Bladex.AddAnmLRelease("Spd_hurt_big",0.373)
	Bladex.AddAnmRStep("Spd_hurt_lite",0.835)
	Bladex.AddAnmLStep("Spd_hurt_lite",0.835)
