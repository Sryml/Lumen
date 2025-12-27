import Bladex
import Enm_Def



def LoadVmpAnimationSet(ct_name):

	print "Loading the Vmp animation sets..."



	#### Relax ####


	#Bladex.LoadSampledAnimation("../../Anm/Vmp_rlx_1h.BMV","Vmp_rlx_1h",1)
	#Bladex.AddAnmRStep("Vmp_rlx_1h",0.0)
	#Bladex.AddAnmLStep("Vmp_rlx_1h",0.0)


	Bladex.LoadSampledAnimation("../../Anm/Vmp_rlx_f.BMV","Vmp_rlx_f",1)
	Bladex.AddAnmRStep("Vmp_rlx_f",0.0)
	Bladex.AddAnmLStep("Vmp_rlx_f",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Vmp_rlx_f_s.BMV","Vmp_rlx_f_s",1)
	Bladex.AddAnmRStep("Vmp_rlx_f_s",0.0)
	Bladex.AddAnmLStep("Vmp_rlx_f_s",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Vmp_insult.BMV","Vmp_insult",0)
	Bladex.AddAnmRStep("Vmp_insult",0.0)
	Bladex.AddAnmLStep("Vmp_insult",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Vmp_order.BMV","Vmp_order",0)
	Bladex.AddAnmRStep("Vmp_order",0.0)
	Bladex.AddAnmLStep("Vmp_order",0.0)


	Bladex.LoadSampledAnimation("../../Anm/Vmp_patrol.BMV","Vmp_patrol",0)
	Bladex.AddAnmRStep("Vmp_patrol",0.0)
	Bladex.AddAnmLStep("Vmp_patrol",0.0)

	#### Animaciones de combate ####


	Bladex.LoadSampledAnimation("../../Anm/Vmp_attack_b.BMV","Vmp_attack_b",1)
	Bladex.AddAnmRStep("Vmp_attack_b",0.35)
	Bladex.AddAnmRRelease("Vmp_attack_b",1.0)
	Bladex.AddAnmLStep("Vmp_attack_b",0.0)
	Bladex.AddAnmLRelease("Vmp_attack_b",0.5)
	Bladex.AddAnmLStep("Vmp_attack_b",1)
	Bladex.AddStopTests("Vmp_attack_b")

	Bladex.LoadSampledAnimation("../../Anm/Vmp_attack_b_s.BMV","Vmp_attack_b_s",1)
	Bladex.AddAnmRStep("Vmp_attack_b_s",0.35)
	Bladex.AddAnmRRelease("Vmp_attack_b_s",1.0)
	Bladex.AddAnmLStep("Vmp_attack_b_s",0.0)
	Bladex.AddAnmLRelease("Vmp_attack_b_s",0.5)
	Bladex.AddAnmLStep("Vmp_attack_b_s",1)
	Bladex.AddStopTests("Vmp_attack_b_s")


	Bladex.LoadSampledAnimation("../../Anm/Vmp_attack_f.BMV","Vmp_attack_f",1)
	Bladex.AddAnmRStep("Vmp_attack_f",0)
	Bladex.AddAnmRRelease("Vmp_attack_f",0.424)
	Bladex.AddAnmRStep("Vmp_attack_f",0.546)
	Bladex.AddAnmRRelease("Vmp_attack_f",0.887)
	Bladex.AddAnmRStep("Vmp_attack_f",1)
	Bladex.AddAnmLStep("Vmp_attack_f",0.0)
	Bladex.AddAnmLRelease("Vmp_attack_f",0.179)
	Bladex.AddAnmLStep("Vmp_attack_f",0.265)
	Bladex.AddAnmLRelease("Vmp_attack_f",0.650)
	Bladex.AddAnmLStep("Vmp_attack_f",0.765)
	Bladex.AddStopTests("Vmp_attack_f")


	Bladex.LoadSampledAnimation("../../Anm/Vmp_attack_f_s.BMV","Vmp_attack_f_s",1)
	Bladex.AddAnmRStep("Vmp_attack_f_s",0)
	Bladex.AddAnmRRelease("Vmp_attack_f_s",0.424)
	Bladex.AddAnmRStep("Vmp_attack_f_s",0.546)
	Bladex.AddAnmRRelease("Vmp_attack_f_s",0.887)
	Bladex.AddAnmRStep("Vmp_attack_f_s",1)
	Bladex.AddAnmLStep("Vmp_attack_f_s",0.0)
	Bladex.AddAnmLRelease("Vmp_attack_f_s",0.179)
	Bladex.AddAnmLStep("Vmp_attack_f_s",0.265)
	Bladex.AddAnmLRelease("Vmp_attack_f_s",0.650)
	Bladex.AddAnmLStep("Vmp_attack_f_s",0.765)
	Bladex.AddStopTests("Vmp_attack_f_s")


	Bladex.LoadSampledAnimation("../../Anm/Vmp_attack_l.BMV","Vmp_attack_l",1)
	Bladex.AddAnmRStep("Vmp_attack_l",0.0)
	Bladex.AddAnmRRelease("Vmp_attack_l",0.23)
	Bladex.AddAnmRStep("Vmp_attack_l",0.47)
	Bladex.AddAnmRRelease("Vmp_attack_l",0.74)
	Bladex.AddAnmRStep("Vmp_attack_l",1.0)
	Bladex.AddAnmLStep("Vmp_attack_l",0.27)
	Bladex.AddAnmLRelease("Vmp_attack_l",0.46)
	Bladex.AddAnmLStep("Vmp_attack_l",0.77)
	Bladex.AddAnmLRelease("Vmp_attack_l",0.96)
	Bladex.AddStopTests("Vmp_attack_l")


	Bladex.LoadSampledAnimation("../../Anm/Vmp_attack_l_s.BMV","Vmp_attack_l_s",1)
	Bladex.AddAnmRStep("Vmp_attack_l_s",0.0)
	Bladex.AddAnmRRelease("Vmp_attack_l_s",0.23)
	Bladex.AddAnmRStep("Vmp_attack_l_s",0.47)
	Bladex.AddAnmRRelease("Vmp_attack_l_s",0.74)
	Bladex.AddAnmRStep("Vmp_attack_l_s",1.0)
	Bladex.AddAnmLStep("Vmp_attack_l_s",0.27)
	Bladex.AddAnmLRelease("Vmp_attack_l_s",0.46)
	Bladex.AddAnmLStep("Vmp_attack_l_s",0.77)
	Bladex.AddAnmLRelease("Vmp_attack_l_s",0.96)
	Bladex.AddStopTests("Vmp_attack_l_s")


	Bladex.LoadSampledAnimation("../../Anm/Vmp_attack_r.BMV","Vmp_attack_r",1)
	Bladex.AddAnmRStep("Vmp_attack_r",0.0)
	Bladex.AddAnmRRelease("Vmp_attack_r",0.74)
	Bladex.AddAnmRStep("Vmp_attack_r",1.0)
	Bladex.AddAnmLStep("Vmp_attack_r",0.0)
	Bladex.AddAnmLRelease("Vmp_attack_r",0.18)
	Bladex.AddAnmLStep("Vmp_attack_r",0.7)
	Bladex.AddStopTests("Vmp_attack_r")


	Bladex.LoadSampledAnimation("../../Anm/Vmp_attack_r_s.BMV","Vmp_attack_r_s",1)
	Bladex.AddAnmRStep("Vmp_attack_r_s",0.0)
	Bladex.AddAnmRRelease("Vmp_attack_r_s",0.74)
	Bladex.AddAnmRStep("Vmp_attack_r_s",1.0)
	Bladex.AddAnmLStep("Vmp_attack_r_s",0.0)
	Bladex.AddAnmLRelease("Vmp_attack_r_s",0.18)
	Bladex.AddAnmLStep("Vmp_attack_r_s",0.7)
	Bladex.AddStopTests("Vmp_attack_r_s")





	####Ataques####


	Bladex.LoadSampledAnimation("../../Anm/Vmp_g_01.BMV","Vmp_g_01",0)
	Bladex.AddAnmRStep("Vmp_g_01",0.0)
	Bladex.AddAnmRRelease("Vmp_g_01",0.076)
	Bladex.AddAnmRStep("Vmp_g_01",0.33)
	Bladex.AddAnmRRelease("Vmp_g_01",0.64)
	Bladex.AddAnmRStep("Vmp_g_01",1.0)
	Bladex.AddAnmLStep("Vmp_g_01",0.0)





	Bladex.LoadSampledAnimation("../../Anm/Vmp_g_06.BMV","Vmp_g_06",0)

	Bladex.AddAnmRStep("Vmp_g_06",0.0)
	Bladex.AddAnmRRelease("Vmp_g_06",0.06)
	Bladex.AddAnmRStep("Vmp_g_06",0.24)
	Bladex.AddAnmRRelease("Vmp_g_06",0.66)
	Bladex.AddAnmRStep("Vmp_g_06",0.95)
	Bladex.AddAnmLStep("Vmp_g_06",0.0)



	Bladex.LoadSampledAnimation("../../Anm/Vmp_g_07.BMV","Vmp_g_07",0)

	Bladex.AddAnmRStep("Vmp_g_07",0.0)
	Bladex.AddAnmRRelease("Vmp_g_07",0.04)
	Bladex.AddAnmRStep("Vmp_g_07",0.27)
	Bladex.AddAnmRRelease("Vmp_g_07",0.59)
	Bladex.AddAnmRStep("Vmp_g_07",0.83)
	Bladex.AddAnmLStep("Vmp_g_07",0.0)



	Bladex.LoadSampledAnimation("../../Anm/Vmp_g_26.BMV","Vmp_g_26",0)

	Bladex.AddAnmRStep("Vmp_g_26",0.0)
	Bladex.AddAnmRRelease("Vmp_g_26",0.08)
	Bladex.AddAnmRStep("Vmp_g_26",0.42)
	Bladex.AddAnmRRelease("Vmp_g_26",0.6)
	Bladex.AddAnmRStep("Vmp_g_26",0.85)
	Bladex.AddAnmLStep("Vmp_g_26",0.0)
	Bladex.AddAnmLRelease("Vmp_g_26",0.15)
	Bladex.AddAnmLStep("Vmp_g_26",0.27)


	Bladex.LoadSampledAnimation("../../Anm/Vmp_disappear.BMV","Vmp_disappear",0)
	Bladex.AddAnmRStep("Vmp_disappear",0.0)
	Bladex.AddAnmLStep("Vmp_disappear",0.0)
	Bladex.AddAnmLRelease("Vmp_disappear",0.238)
	Bladex.AddAnmLStep("Vmp_disappear",0.431)


	#Bladex.LoadSampledAnimation("../../Anm/Vmp_appear.BMV","Vmp_appear",0)
	#Bladex.AddAnmRStep("Vmp_appear",0.0)
	#Bladex.AddAnmLStep("Vmp_appear",0.0)
	#Bladex.AddAnmLRelease("Vmp_appear",0.577)
	#Bladex.AddAnmLStep("Vmp_appear",0.792)





	####Andares y pasos####


	Bladex.LoadSampledAnimation("../../Anm/Vmp_wbk_1h.BMV","Vmp_wbk_1h",1)

	Bladex.AddAnmRStep("Vmp_wbk_1h",0.0)
	Bladex.AddAnmRRelease("Vmp_wbk_1h",0.52)
	Bladex.AddAnmRStep("Vmp_wbk_1h",1.0)
	Bladex.AddAnmLStep("Vmp_wbk_1h",0.54)
	Bladex.AddAnmLRelease("Vmp_wbk_1h",1.0)
	Bladex.AddStopTests("Vmp_wbk_1h")


	Bladex.LoadSampledAnimation("../../Anm/Vmp_wlk_1h.BMV","Vmp_wlk_1h",1)

	Bladex.AddAnmRStep("Vmp_wlk_1h",0.5)
	Bladex.AddAnmRRelease("Vmp_wlk_1h",1.0)
	Bladex.AddAnmLStep("Vmp_wlk_1h",0.0)
	Bladex.AddAnmLRelease("Vmp_wlk_1h",0.5)
	Bladex.AddAnmLStep("Vmp_wlk_1h",1.0)
	Bladex.AddStopTests("Vmp_wlk_1h")



	###CA�DAS#####

	#Caida enorme
	Bladex.LoadSampledAnimation("../../Anm/Vmp_dth_fll.BMV","Dth_Fll_Vmp",0)
	Bladex.LoadSampledAnimation("../../Anm/Vmp_dth_fll2.BMV","Dth_Fll2_Vmp",0)
	Bladex.AddAnmRStep("Dth_Fll2_Vmp",0.0)
	Bladex.AddAnmLStep("Dth_Fll2_Vmp",0.0)



	anm_name="Vmp_df_01"
	Bladex.LoadSampledAnimation("../../Anm/Vmp_df_01.BMV","Vmp_df_01",0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.187)
	Bladex.AddAnmRStep(anm_name,0.386)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.230)
	Bladex.AddAnmLStep(anm_name,0.560)

	anm_name="Vmp_df_02"
	Bladex.LoadSampledAnimation("../../Anm/Vmp_df_02.BMV","Vmp_df_02",0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.029)
	Bladex.AddAnmRStep(anm_name,0.198)
	Bladex.AddAnmRRelease(anm_name,0.311)
	Bladex.AddAnmRStep(anm_name,0.468)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.127)
	Bladex.AddAnmLStep(anm_name,0.335)


	anm_name="Vmp_df_s_broken"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_df_s_broken.BMV",anm_name,0,"Vamp")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.131)
	Bladex.AddAnmLStep(anm_name,0.414)
	Bladex.AddAnmRRelease(anm_name,0.439)
	Bladex.AddAnmRStep(anm_name,595)
	Bladex.AddAnmLRelease(anm_name,0.708)
	Bladex.AddAnmLStep(anm_name,0.867)

	anm_name="Vmp_sword_broken"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_sword_broken.BMV",anm_name,0,"Vamp")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.238)
	Bladex.AddAnmRStep(anm_name,0.332)
	Bladex.AddAnmRRelease(anm_name,0.529)
	Bladex.AddAnmRStep(anm_name,0.667)
	Bladex.AddAnmLRelease(anm_name,0.333)
	Bladex.AddAnmLStep(anm_name,0.497)
	Bladex.AddAnmLRelease(anm_name,0.537)
	Bladex.AddAnmLStep(anm_name,0.697)

	anm_name="Vmp_hurt_f_big"
	Bladex.LoadSampledAnimation("../../Anm/Vmp_hurt_f_big.BMV","Vmp_hurt_f_big",0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.029)
	Bladex.AddAnmRStep(anm_name,0.198)
	Bladex.AddAnmRRelease(anm_name,0.311)
	Bladex.AddAnmRStep(anm_name,0.468)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.127)
	Bladex.AddAnmLStep(anm_name,0.335)

	anm_name="Vmp_hurt_f_lite"
	Bladex.LoadSampledAnimation("../../Anm/Vmp_hurt_f_lite.BMV","Vmp_hurt_f_lite",0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.187)
	Bladex.AddAnmRStep(anm_name,0.386)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.230)
	Bladex.AddAnmLStep(anm_name,0.560)
