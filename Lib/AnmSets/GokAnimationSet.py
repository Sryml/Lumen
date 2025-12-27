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



def LoadGokAnimationSet(ct_name):

	print "Loading the Gok animation sets..."

	#### Relax ####
	#Bladex.AddAnimFlags("Gok_rlx",0,0,0,1,Enm_Def.BM_XYZ,Enm_Def.HEADF_ENG)

	Bladex.LoadSampledAnimation("../../Anm/Ork_rlx_no.BMV","Rlx_no_Gok",1,"Great_Ork")
	Bladex.AddAnmRStep("Rlx_no_Gok",0.0)
	Bladex.AddAnmLStep("Rlx_no_Gok",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Ork_rlx_1h.BMV","Rlx_1h_Gok",1,"Great_Ork")
	Bladex.AddAnmRStep("Rlx_1h_Gok",0.0)
	Bladex.AddAnmLStep("Rlx_1h_Gok",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Ork_rlx_b.BMV","Rlx_b_Gok",1,"Great_Ork")
	Bladex.AddAnmRStep("Rlx_b_Gok",0.0)
	Bladex.AddAnmLStep("Rlx_b_Gok",0.0)

	### CORRER   ####


	Bladex.LoadSampledAnimation("../../Anm/Gok_jog_1h.BMV","Jog_1h_Gok",1,"Great_Ork")
	Bladex.AddAnmLStep("Jog_1h_Gok",0)
	Bladex.AddAnmLRelease("Jog_1h_Gok",0.257)
	Bladex.AddAnmLStep("Jog_1h_Gok",0.535)
	Bladex.AddAnmLRelease("Jog_1h_Gok",0.750)
	Bladex.AddAnmLStep("Jog_1h_Gok",1)
	Bladex.AddAnmRStep("Jog_1h_Gok",0.331)
	Bladex.AddAnmRRelease("Jog_1h_Gok",0.548)
	Bladex.AddAnmRStep("Jog_1h_Gok",0.811)
	Bladex.AddAnmRRelease("Jog_1h_Gok",1)
	Bladex.AddStopTests("Jog_1h_Gok")

	Bladex.LoadSampledAnimation("../../Anm/Ork_jog_b.BMV","Jog_b_Gok",1,"Great_Ork")
	Bladex.AddAnmLStep("Jog_b_Gok",0)
	Bladex.AddAnmLRelease("Jog_b_Gok",0.201)
	Bladex.AddAnmLStep("Jog_b_Gok",0.535)
	Bladex.AddAnmLRelease("Jog_b_Gok",0.734)
	Bladex.AddAnmLStep("Jog_b_Gok",1)
	Bladex.AddAnmRStep("Jog_b_Gok",0.0)
	Bladex.AddAnmRRelease("Jog_b_Gok",0.033)
	Bladex.AddAnmRStep("Jog_b_Gok",0.346)
	Bladex.AddAnmRRelease("Jog_b_Gok",0.51)
	Bladex.AddAnmRStep("Jog_b_Gok",0.83)
	Bladex.AddStopTests("Jog_b_Gok")


#############################
########## Caminar atras ####
#############################



	Bladex.LoadSampledAnimation("../../Anm/Ork_wbk_b.BMV","Wbk_b_Gok",1,"Great_Ork")
	Bladex.AddAnmRStep("Wbk_b_Gok",0.0)
	Bladex.AddAnmRRelease("Wbk_b_Gok",0.172)
	Bladex.AddAnmRStep("Wbk_b_Gok",0.434)
	Bladex.AddAnmRRelease("Wbk_b_Gok",0.688)
	Bladex.AddAnmRStep("Wbk_b_Gok",1)
	Bladex.AddAnmLStep("Wbk_b_Gok",0.0)
	Bladex.AddAnmLRelease("Wbk_b_Gok",0.024)
	Bladex.AddAnmLStep("Wbk_b_Gok",0.260)
	Bladex.AddAnmLRelease("Wbk_b_Gok",0.51)
	Bladex.AddAnmLStep("Wbk_b_Gok",0.767)
	Bladex.AddStopTests("Wbk_b_Gok")


#############################
################ Caminar ####
#############################


	Bladex.LoadSampledAnimation("../../Anm/Ork_wlk_b.BMV","Wlk_b_Gok",1,"Great_Ork")

	Bladex.AddAnmRStep("Wlk_b_Gok",0.0)
	Bladex.AddAnmLStep("Wlk_b_Gok",0.0)
	Bladex.AddAnmRRelease("Wlk_b_Gok",0.097)
	Bladex.AddAnmLRelease("Wlk_b_Gok",0.264)
	Bladex.AddAnmRStep("Wlk_b_Gok",0.309)
	Bladex.AddAnmLStep("Wlk_b_Gok",0.487)
	Bladex.AddAnmRRelease("Wlk_b_Gok",0.588)
	Bladex.AddAnmLRelease("Wlk_b_Gok",0.757)
	Bladex.AddAnmRStep("Wlk_b_Gok",0.804)
	Bladex.AddAnmLStep("Wlk_b_Gok",1)
	Bladex.AddStopTests("Wlk_b_Gok")




	Bladex.LoadSampledAnimation("../../Anm/Gok_wlk_1h.BMV","Wlk_1h_Gok",1)

	Bladex.AddAnmRStep("Wlk_1h_Gok",0.0)
	Bladex.AddAnmRRelease("Wlk_1h_Gok",0.3)
	Bladex.AddAnmRStep("Wlk_1h_Gok",0.511)
	Bladex.AddAnmRRelease("Wlk_1h_Gok",0.804)
	Bladex.AddAnmRStep("Wlk_1h_Gok",1.0)
	Bladex.AddAnmLStep("Wlk_1h_Gok",0.249)
	Bladex.AddAnmLRelease("Wlk_1h_Gok",0.538)
	Bladex.AddAnmLStep("Wlk_1h_Gok",0.760)
	Bladex.AddAnmLRelease("Wlk_1h_Gok",1)
	Bladex.AddStopTests("Wlk_1h_Gok")




	#
	# End caminar
	#

	#### Caidas ####


	Bladex.LoadSampledAnimation("../../Anm/Gok_fll_med_1h.BMV","FallMed_Gok",0)
	Bladex.AddAnmRStep("FallMed_Gok",0.0)
	Bladex.AddAnmLStep("FallMed_Gok",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Gok_fll_high_1h.BMV","FallHigh_Gok",0)
	Bladex.AddAnmRStep("FallHigh_Gok",0.0)
	Bladex.AddAnmLStep("FallHigh_Gok",0.0)


########### ARCO ###########

	#
	# Bowing
	#
	anm_name="Gok_b1"
	Bladex.LoadSampledAnimation("../../Anm/Ork_b1.BMV",anm_name,0,"Great_Ork")

	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Gok_b2"
	Bladex.LoadSampledAnimation("../../Anm/Ork_b2.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Gok_b3"
	Bladex.LoadSampledAnimation("../../Anm/Ork_b3.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)



	#
	# Ataques
	#



	Bladex.LoadSampledAnimation("../../Anm/Gok_g_01.BMV","Gok_g_01",0)
	Bladex.AddAnmRStep("Gok_g_01",0)
	Bladex.AddAnmLStep("Gok_g_01",0)
	Bladex.AddAnmRRelease("Gok_g_01",0.105)
	Bladex.AddAnmRStep("Gok_g_01",0.245)
	Bladex.AddAnmRRelease("Gok_g_01",0.440)
	Bladex.AddAnmRStep("Gok_g_01",0.632)


	Bladex.LoadSampledAnimation("../../Anm/Gok_g_02.BMV","Gok_g_02",0)
	Bladex.AddAnmRStep("Gok_g_02",0)
	Bladex.AddAnmLStep("Gok_g_02",0)
	Bladex.AddAnmRRelease("Gok_g_02",0.105)
	Bladex.AddAnmRStep("Gok_g_02",0.280)
	Bladex.AddAnmRRelease("Gok_g_02",0.514)
	Bladex.AddAnmRStep("Gok_g_02",0.790)


#	Bladex.LoadSampledAnimation("../../Anm/Ork_g_05.BMV","Gok_g_05",0)
#	Bladex.AddAnmRStep("Gok_g_05",0)
#	Bladex.AddAnmLStep("Gok_g_05",0)
#	Bladex.AddAnmRRelease("Gok_g_05",0.28)
#	Bladex.AddAnmRStep("Gok_g_05",0.5)
#	Bladex.AddAnmRRelease("Gok_g_05",0.72)
#	Bladex.AddAnmRStep("Gok_g_05",0.9)


	Bladex.LoadSampledAnimation("../../Anm/Gok_g_06.BMV","Gok_g_06",0)
	Bladex.AddAnmRStep("Gok_g_06",0)
	Bladex.AddAnmLStep("Gok_g_06",0)
	Bladex.AddAnmRRelease("Gok_g_06",0.153)
	Bladex.AddAnmRStep("Gok_g_06",0.372)
	Bladex.AddAnmRRelease("Gok_g_06",0.554)
	Bladex.AddAnmRStep("Gok_g_06",0.788)


#	Bladex.LoadSampledAnimation("../../Anm/Ork_g_07.BMV","Gok_g_07",0)
#	Bladex.AddAnmRStep("Gok_g_07",0)
#	Bladex.AddAnmLStep("Gok_g_07",0)
#	Bladex.AddAnmRRelease("Gok_g_07",0.153)
#	Bladex.AddAnmRStep("Gok_g_07",0.35)
#	Bladex.AddAnmRRelease("Gok_g_07",0.51)
#	Bladex.AddAnmRStep("Gok_g_07",0.72)
#
#
#	Bladex.LoadSampledAnimation("../../Anm/Ork_g_09.BMV","Gok_g_09",0)
#	Bladex.AddAnmRStep("Gok_g_09",0)
#	Bladex.AddAnmLStep("Gok_g_09",0)
#	Bladex.AddAnmRRelease("Gok_g_09",0.23)
#	Bladex.AddAnmRStep("Gok_g_09",0.36)
#	Bladex.AddAnmRRelease("Gok_g_09",0.55)
#	Bladex.AddAnmRStep("Gok_g_09",0.71)
#
#
#	Bladex.LoadSampledAnimation("../../Anm/Ork_g_13.BMV","Gok_g_13",0)
#	Bladex.AddAnmRStep("Gok_g_13",0)
#	Bladex.AddAnmLStep("Gok_g_13",0)
#	Bladex.AddAnmRRelease("Gok_g_13",0.41)
#	Bladex.AddAnmRStep("Gok_g_13",0.57)
#	Bladex.AddAnmLRelease("Gok_g_13",0.76)
#	Bladex.AddAnmLStep("Gok_g_13",0.89)
#

	Bladex.LoadSampledAnimation("../../Anm/Gok_g_18.BMV","Gok_g_18",0)
	Bladex.AddAnmRStep("Gok_g_18",0)
	Bladex.AddAnmRRelease("Gok_g_18",0.211)
	Bladex.AddAnmRStep("Gok_g_18",0.503)
	Bladex.AddAnmRRelease("Gok_g_18",0.730)
	Bladex.AddAnmRStep("Gok_g_18",0.894)
	Bladex.AddAnmLStep("Gok_g_18",0)
	Bladex.AddAnmLRelease("Gok_g_18",0.091)
	Bladex.AddAnmLStep("Gok_g_18",0.207)
	Bladex.AddAnmLRelease("Gok_g_18",0.308)
	Bladex.AddAnmLStep("Gok_g_18",0.48)
	Bladex.AddAnmLRelease("Gok_g_18",0.793)
	Bladex.AddAnmLStep("Gok_g_18",0.841)


#	Bladex.LoadSampledAnimation("../../Anm/Ork_g_14.BMV","Gok_g_14",0)
#	Bladex.AddAnmRStep("Gok_g_14",0)
#	Bladex.AddAnmLStep("Gok_g_14",0)
#	Bladex.AddAnmLRelease("Gok_g_14",0.15)
#	Bladex.AddAnmLStep("Gok_g_14",0.37)
#	Bladex.AddAnmRRelease("Gok_g_14",0.43)
#	Bladex.AddAnmRStep("Gok_g_14",0.56)
#	Bladex.AddAnmLRelease("Gok_g_14",0.73)
#	Bladex.AddAnmLStep("Gok_g_14",0.85)
#
#
#	Bladex.LoadSampledAnimation("../../Anm/Ork_g_11.BMV","Gok_g_11",0)
#	Bladex.AddAnmRStep("Gok_g_11",0)
#	Bladex.AddAnmLStep("Gok_g_11",0)
#	Bladex.AddAnmRRelease("Gok_g_11",0.4)
#	Bladex.AddAnmRStep("Gok_g_11",0.55)
#	Bladex.AddAnmLRelease("Gok_g_11",0.78)
#	Bladex.AddAnmLStep("Gok_g_11",0.93)


	Bladex.LoadSampledAnimation("../../Anm/Gok_g_16.BMV","Gok_g_16",0)
	Bladex.AddAnmRStep("Gok_g_16",0)
	Bladex.AddAnmLStep("Gok_g_16",0)
	Bladex.AddAnmRRelease("Gok_g_16",0.525)
	Bladex.AddAnmRStep("Gok_g_16",0.681)
	Bladex.AddAnmLRelease("Gok_g_16",0.525)
	Bladex.AddAnmLStep("Gok_g_16",0.732)


#	Bladex.LoadSampledAnimation("../../Anm/Ork_g_12.BMV","Gok_g_12",0)
#	Bladex.AddAnmRStep("Gok_g_12",0)
#	Bladex.AddAnmLStep("Gok_g_12",0)
#	Bladex.AddAnmRRelease("Gok_g_12",0.4)
#	Bladex.AddAnmRStep("Gok_g_12",0.52)
#	Bladex.AddAnmLRelease("Gok_g_12",0.71)
#	Bladex.AddAnmLStep("Gok_g_12",0.85)


#Bladex.LoadSampledAnimation("../../Anm/Ork_g_17.BMV","Gok_g_17",0)
#Bladex.AddAnmRStep("Gok_g_17",0)
#Bladex.AddAnmLStep("Gok_g_17",0)
#Bladex.AddAnmRRelease("Gok_g_17",0.16)
#Bladex.AddAnmRStep("Gok_g_17",0.27)
#Bladex.AddAnmLRelease("Gok_g_17",0.53)
#Bladex.AddAnmLStep("Gok_g_17",0.65)



	Bladex.LoadSampledAnimation("../../Anm/Gok_g_15.BMV","Gok_g_15",0)
	Bladex.AddAnmRStep("Gok_g_15",0)
	Bladex.AddAnmLStep("Gok_g_15",0)
	Bladex.AddAnmRRelease("Gok_g_15",0.105)
	Bladex.AddAnmRStep("Gok_g_15",0.281)
	Bladex.AddAnmLRelease("Gok_g_15",0.350)
	Bladex.AddAnmRRelease("Gok_g_15",0.413)
	Bladex.AddAnmRStep("Gok_g_15",0.541)
	Bladex.AddAnmLStep("Gok_g_15",0.578)



#Bladex.LoadSampledAnimation("../../Anm/Gok_g_21.BMV","Gok_g_21",0)
#Bladex.AddAnmRStep("Gok_g_21",0)
#Bladex.AddAnmLStep("Gok_g_21",0)
#Bladex.AddAnmRRelease("Gok_g_21",0.51)
#Bladex.AddAnmRStep("Gok_g_21",0.669)
#Bladex.AddAnmLRelease("Gok_g_21",0.696)
#Bladex.AddAnmLStep("Gok_g_21",0.834)
#
#
#Bladex.LoadSampledAnimation("../../Anm/Gok_g_22.BMV","Gok_g_22",0)
#Bladex.AddAnmRStep("Gok_g_22",0)
#Bladex.AddAnmLStep("Gok_g_22",0)
#Bladex.AddAnmRRelease("Gok_g_22",0.474)
#Bladex.AddAnmRStep("Gok_g_22",0.544)
#Bladex.AddAnmRRelease("Gok_g_22",0.605)
#Bladex.AddAnmRStep("Gok_g_22",0.67)
#Bladex.AddAnmRRelease("Gok_g_22",0.781)
#Bladex.AddAnmRStep("Gok_g_22",0.847)
#Bladex.AddAnmLRelease("Gok_g_22",0.2)
#Bladex.AddAnmLStep("Gok_g_22",0.433)
#Bladex.AddAnmLRelease("Gok_g_22",0.549)
#Bladex.AddAnmLStep("Gok_g_22",0.6)
#
#
#Bladex.LoadSampledAnimation("../../Anm/Gok_g_23.BMV","Gok_g_23",0)
#Bladex.AddAnmRStep("Gok_g_23",0)
#Bladex.AddAnmLStep("Gok_g_23",0)
#Bladex.AddAnmRRelease("Gok_g_23",0.529)
#Bladex.AddAnmRStep("Gok_g_23",0.743)
#Bladex.AddAnmLRelease("Gok_g_23",0.75)
#Bladex.AddAnmLStep("Gok_g_23",0.85)
#
#
#Bladex.LoadSampledAnimation("../../Anm/Gok_g_26.BMV","Gok_g_26",0)
#Bladex.AddAnmRStep("Gok_g_26",0)
#Bladex.AddAnmLStep("Gok_g_26",0)
#Bladex.AddAnmRRelease("Gok_g_26",0.135)
#Bladex.AddAnmRStep("Gok_g_26",0.236)
#Bladex.AddAnmLRelease("Gok_g_26",0.48)
#Bladex.AddAnmLStep("Gok_g_26",0.682)
#Bladex.AddAnmLRelease("Gok_g_26",0.79)
#Bladex.AddAnmLStep("Gok_g_26",0.885)
#
#
#Bladex.LoadSampledAnimation("../../Anm/Gok_g_27.BMV","Gok_g_27",0)
#Bladex.AddAnmRStep("Gok_g_27",0)
#Bladex.AddAnmLStep("Gok_g_27",0)
#Bladex.AddAnmRRelease("Gok_g_27",0.28)
#Bladex.AddAnmRStep("Gok_g_27",0.5)
#Bladex.AddAnmLRelease("Gok_g_27",0.72)
#Bladex.AddAnmLStep("Gok_g_27",0.74)
#
#
#anm_name="Gok_g_31"
#Bladex.LoadSampledAnimation("../../Anm/Gok_g_31.BMV",anm_name,0)
#Bladex.AddAnmRStep(anm_name,0)
#Bladex.AddAnmLStep(anm_name,0)
#Bladex.AddAnmRRelease(anm_name,0.283)
#Bladex.AddAnmRStep(anm_name,0.383)
#Bladex.AddAnmRRelease(anm_name,0.544)
#Bladex.AddAnmRStep(anm_name,0.597)
#Bladex.AddAnmLRelease(anm_name,0.010)
#Bladex.AddAnmLStep(anm_name,0.257)
#Bladex.AddAnmLRelease(anm_name,0.51)
#Bladex.AddAnmLStep(anm_name,0.597)


	#
	# Movimientos en combate
	#
	anm_name="Gok_attack_l"
	Bladex.LoadSampledAnimation("../../Anm/Gok_attack_l.BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.213)
	Bladex.AddAnmLStep(anm_name,0.528)
	Bladex.AddAnmLRelease(anm_name,0.703)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.307)
	Bladex.AddAnmRRelease(anm_name,0.537)
	Bladex.AddAnmRStep(anm_name,0.821)
	Bladex.AddAnmRRelease(anm_name,1)
	Bladex.AddStopTests(anm_name)

	anm_name="Gok_attack_r"
	Bladex.LoadSampledAnimation("../../Anm/Gok_attack_r.BMV",anm_name,1,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmRRelease(anm_name,0.230)
	Bladex.AddAnmRStep(anm_name,0.496)
	Bladex.AddAnmRRelease(anm_name,0.695)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.1)
	Bladex.AddAnmLStep(anm_name,0.361)
	Bladex.AddAnmLRelease(anm_name,0.604)
	Bladex.AddAnmLStep(anm_name,0.822)
	Bladex.AddStopTests(anm_name)

	anm_name="Gok_attack_f"
	Bladex.LoadSampledAnimation("../../Anm/Gok_attack_f.BMV",anm_name,1,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.07)
	Bladex.AddAnmRStep(anm_name,0.376)
	Bladex.AddAnmRRelease(anm_name,0.515)
	Bladex.AddAnmRStep(anm_name,0.859)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmLRelease(anm_name,0.204)
	Bladex.AddAnmLStep(anm_name,0.513)
	Bladex.AddAnmLRelease(anm_name,0.656)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)

	anm_name="Gok_attack_b"
	Bladex.LoadSampledAnimation("../../Anm/Gok_attack_b.BMV",anm_name,1,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.166)
	Bladex.AddAnmRStep(anm_name,0.621)
	Bladex.AddAnmRRelease(anm_name,0.7)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.046)
	Bladex.AddAnmLStep(anm_name,0.345)
	Bladex.AddAnmLRelease(anm_name,0.541)
	Bladex.AddAnmLStep(anm_name,0.849)
	Bladex.AddStopTests(anm_name)

	anm_name="Gok_d_b"
	Bladex.LoadSampledAnimation("../../Anm/Ork_d_b.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.296)
	Bladex.AddAnmRStep(anm_name,0.562)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.416)
	Bladex.AddAnmLStep(anm_name,0.709)

	anm_name="Gok_d_r"
	Bladex.LoadSampledAnimation("../../Anm/Ork_d_r.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.166)
	Bladex.AddAnmRStep(anm_name,0.318)
	Bladex.AddAnmRRelease(anm_name,0.481)
	Bladex.AddAnmRStep(anm_name,0.807)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.272)
	Bladex.AddAnmLStep(anm_name,0.648)

	anm_name="Gok_d_l"
	Bladex.LoadSampledAnimation("../../Anm/Ork_d_l.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.067)
	Bladex.AddAnmRStep(anm_name,0.150)
	Bladex.AddAnmRRelease(anm_name,0.325)
	Bladex.AddAnmRStep(anm_name,0.678)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.150)
	Bladex.AddAnmRStep(anm_name,0.370)
	Bladex.AddAnmLRelease(anm_name,0.566)
	Bladex.AddAnmLStep(anm_name,0.829)

	anm_name="Gok_attack_l_s"
	Bladex.LoadSampledAnimation("../../Anm/Gok_attack_l_s.BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.213)
	Bladex.AddAnmLStep(anm_name,0.528)
	Bladex.AddAnmLRelease(anm_name,0.703)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.307)
	Bladex.AddAnmRRelease(anm_name,0.537)
	Bladex.AddAnmRStep(anm_name,0.821)
	Bladex.AddAnmRRelease(anm_name,1)
	Bladex.AddStopTests(anm_name)

	anm_name="Gok_attack_r_s"
	Bladex.LoadSampledAnimation("../../Anm/Gok_attack_r_s.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmRRelease(anm_name,0.230)
	Bladex.AddAnmRStep(anm_name,0.496)
	Bladex.AddAnmRRelease(anm_name,0.695)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.1)
	Bladex.AddAnmLStep(anm_name,0.361)
	Bladex.AddAnmLRelease(anm_name,0.604)
	Bladex.AddAnmLStep(anm_name,0.822)
	Bladex.AddStopTests(anm_name)

	anm_name="Gok_attack_f_s"
	Bladex.LoadSampledAnimation("../../Anm/Gok_attack_f_s.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.07)
	Bladex.AddAnmRStep(anm_name,0.376)
	Bladex.AddAnmRRelease(anm_name,0.515)
	Bladex.AddAnmRStep(anm_name,0.859)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmLRelease(anm_name,0.204)
	Bladex.AddAnmLStep(anm_name,0.513)
	Bladex.AddAnmLRelease(anm_name,0.656)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)

	anm_name="Gok_attack_b_s"
	Bladex.LoadSampledAnimation("../../Anm/Gok_attack_b_s.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.166)
	Bladex.AddAnmRStep(anm_name,0.621)
	Bladex.AddAnmRRelease(anm_name,0.7)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.046)
	Bladex.AddAnmLStep(anm_name,0.345)
	Bladex.AddAnmLRelease(anm_name,0.541)
	Bladex.AddAnmLStep(anm_name,0.849)
	Bladex.AddStopTests(anm_name)

	anm_name="Gok_attack_rlx"
	Bladex.LoadSampledAnimation("../../Anm/Gok_attack_rlx.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Gok_attack_rlx_s"
	Bladex.LoadSampledAnimation("../../Anm/Gok_attack_rlx_s.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)




##############################
#############Cambio de armas##
##############################

	anm_name="Gok_attack_chg_r_l"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_attack_chg_r_l.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)

	anm_name="Gok_attack_drink"
	Bladex.LoadSampledAnimation("../../Anm/Ork_attack_drink.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)




######################################
#
#	Ambiente Mapas
#
######################################





	anm_name="Gok_alarm01"
	Bladex.LoadSampledAnimation("../../Anm/Tkn_alarm01.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)


	anm_name="Gok_fury"
	Bladex.LoadSampledAnimation("../../Anm/Tkn_fury.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)



	anm_name="Gok_wai_01"
	Bladex.LoadSampledAnimation("../../Anm/Tkn_wai_01.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)



	anm_name="Gok_wai_02"
	Bladex.LoadSampledAnimation("../../Anm/Tkn_wai_02.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)


	anm_name="Gok_patrol1"
	Bladex.LoadSampledAnimation("../../Anm/Ork_patrol1.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)



	anm_name="Gok_patrol2"
	Bladex.LoadSampledAnimation("../../Anm/Ork_patrol2.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)



	anm_name="Gok_attack_look"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_attack_look.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)



	anm_name="Gok_order"
	Bladex.LoadSampledAnimation("../../Anm/Ork_order.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)


	anm_name="Gok_insult"
	Bladex.LoadSampledAnimation("../../Anm/Ork_insult.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmLRelease(anm_name,0.21)
	Bladex.AddAnmLStep(anm_name,0.23)
	Bladex.AddAnmLRelease(anm_name,0.75)
	Bladex.AddAnmLStep(anm_name,0.79)





	#
	# Slip
	#
	anm_name="Gok_slip"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_slip.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Gok_slip_b"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_slip_b.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Gok_derrape"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_derrape.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)




##################################
#####################   TREPAR   #
##################################


	anm_name="Gok_clmb_low_1h"
	Bladex.LoadSampledAnimation("../../Anm/Ork_clmb_low_1h.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.1)
	Bladex.AddAnmRStep(anm_name,0.14)
	Bladex.AddAnmRRelease(anm_name,0.24)
	Bladex.AddAnmRStep(anm_name,0.34)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.24)
	Bladex.AddAnmLStep(anm_name,0.34)
	Bladex.AddAnmLRelease(anm_name,0.40)
	Bladex.AddAnmLStep(anm_name,0.46)


	anm_name="Gok_clmb_medium_1h"
	Bladex.LoadSampledAnimation("../../Anm/Ork_clmb_med_1h.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.13)
	Bladex.AddAnmRStep(anm_name,0.33)
	Bladex.AddAnmRRelease(anm_name,0.38)
	Bladex.AddAnmRStep(anm_name,0.84)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.25)
	Bladex.AddAnmLStep(anm_name,0.35)
	Bladex.AddAnmLRelease(anm_name,0.40)
	Bladex.AddAnmLStep(anm_name,0.61)





##############################
##Caida enorme
##############################


	Bladex.LoadSampledAnimation("../../Anm/Gok_dth_fll.BMV","Dth_Fll_Gok",0)
	#Bladex.AddAnmRStep("Dth_Fll_Gok",0.0)
	#Bladex.AddAnmLStep("Dth_Fll_Gok",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Gok_dth_fll2.BMV","Dth_Fll2_Gok",0)
	Bladex.AddAnmRStep("Dth_Fll2_Gok",0.0)
	Bladex.AddAnmLStep("Dth_Fll2_Gok",0.0)



	anm_name="Gok_df_s_broken"
	Bladex.LoadSampledAnimation("../../Anm/Ork_df_s_broken.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.12)
	Bladex.AddAnmRStep(anm_name,0.19)
	Bladex.AddAnmRRelease(anm_name,0.41)
	Bladex.AddAnmRStep(anm_name,0.58)
	Bladex.AddAnmLRelease(anm_name,0.18)
	Bladex.AddAnmLStep(anm_name,0.44)




	anm_name="Gok_hurt_f_big"
	Bladex.LoadSampledAnimation("../../Anm/Ork_hurt_f_big.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.087)
	Bladex.AddAnmLRelease(anm_name,0.119)
	Bladex.AddAnmRStep(anm_name,0.169)
	Bladex.AddAnmLStep(anm_name,0.322)
	Bladex.AddAnmRRelease(anm_name,0.325)
	Bladex.AddAnmRStep(anm_name,0.483)
	Bladex.AddAnmLRelease(anm_name,0.509)
	Bladex.AddAnmLStep(anm_name,0.670)
	Bladex.AddAnmRRelease(anm_name,0.751)
	Bladex.AddAnmRStep(anm_name,0.924)

	anm_name="Gok_hurt_f_lite"
	Bladex.LoadSampledAnimation("../../Anm/Ork_hurt_f_lite.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.128)
	Bladex.AddAnmRStep(anm_name,0.322)
	Bladex.AddAnmLRelease(anm_name,0.383)
	Bladex.AddAnmLStep(anm_name,0.705)
	Bladex.AddAnmRRelease(anm_name,0.821)
	Bladex.AddAnmRStep(anm_name,1)
#
#	anm_name="Gok_hurt_big_b"
#	Bladex.LoadSampledAnimation("../../Anm/Ork_hurt_big_b.BMV",anm_name,0,"Great_Ork")
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0)
#	Bladex.AddAnmLRelease(anm_name,0.183)
#	Bladex.AddAnmLStep(anm_name,0.427)
#	Bladex.AddAnmRRelease(anm_name,0.481)
#	Bladex.AddAnmRStep(anm_name,0.659)
#	Bladex.AddAnmLRelease(anm_name,0.764)
#	Bladex.AddAnmLStep(anm_name,0.877)


	anm_name="Gok_hurt_f_r_arm"
	Bladex.LoadSampledAnimation("../../Anm/Ork_hurt_f_r_arm.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)


	anm_name="Gok_hurt_f_l_arm"
	Bladex.LoadSampledAnimation("../../Anm/Ork_hurt_f_l_arm.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)


	anm_name="Gok_hurt_f_l_leg"
	Bladex.LoadSampledAnimation("../../Anm/Ork_hurt_f_l_leg.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.183)
	Bladex.AddAnmLStep(anm_name,0.62)
	Bladex.AddAnmRRelease(anm_name,0.19)
	Bladex.AddAnmRStep(anm_name,0.49)



	anm_name="Gok_hurt_f_r_leg"
	Bladex.LoadSampledAnimation("../../Anm/Ork_hurt_f_r_leg.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.1)
	Bladex.AddAnmRStep(anm_name,0.8)


	anm_name="Gok_hurt_f_head"
	Bladex.LoadSampledAnimation("../../Anm/Ork_hurt_f_head.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)


	anm_name="Gok_hurt_f_back"
	Bladex.LoadSampledAnimation("../../Anm/Ork_hurt_f_back.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.115)
	Bladex.AddAnmLStep(anm_name,0.245)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.113)
	Bladex.AddAnmRStep(anm_name,0.23)


	anm_name="Gok_df_02"
	Bladex.LoadSampledAnimation("../../Anm/Gok_df_02.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.053)
	Bladex.AddAnmRStep(anm_name,0.170)
	Bladex.AddAnmRRelease(anm_name,0.268)
	Bladex.AddAnmRStep(anm_name,0.529)
	Bladex.AddAnmRRelease(anm_name,0.648)
	Bladex.AddAnmRStep(anm_name,0.831)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.201)
	Bladex.AddAnmLStep(anm_name,0.398)
	Bladex.AddAnmLRelease(anm_name,0.509)
	Bladex.AddAnmLStep(anm_name,0.674)


	anm_name="Gok_df_01"
	Bladex.LoadSampledAnimation("../../Anm/Gok_df_01.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.574)
	Bladex.AddAnmRStep(anm_name,0.817)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.252)
	Bladex.AddAnmLStep(anm_name,0.581)




###################################################
#
#	Muertes
#
###################################################



	anm_name="Gok_dth0"
	Bladex.LoadSampledAnimation("../../Anm/Ork_dth0.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.026)
	Bladex.AddAnmRStep(anm_name,0.145)
	Bladex.AddAnmRRelease(anm_name,0.200)
	Bladex.AddAnmRStep(anm_name,0.245)
	Bladex.AddAnmRRelease(anm_name,0.689)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.022)
	Bladex.AddAnmLStep(anm_name,0.157)
	Bladex.AddAnmLRelease(anm_name,0.244)
	Bladex.AddAnmLStep(anm_name,0.299)

	anm_name="Gok_dth_c1"
	Bladex.LoadSampledAnimation("../../Anm/Ork_dth_c1.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.282)
	Bladex.AddAnmRStep(anm_name,0.384)
	Bladex.AddAnmRRelease(anm_name,0.659)
	Bladex.AddAnmRStep(anm_name,0.887)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.579)
	Bladex.AddAnmLStep(anm_name,0.890)

	anm_name="Gok_dth_c2"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c2.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.037)
	Bladex.AddAnmRStep(anm_name,0.083)
	Bladex.AddAnmRRelease(anm_name,0.166)
	Bladex.AddAnmRStep(anm_name,0.306)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.083)
	Bladex.AddAnmLStep(anm_name,0.126)

	anm_name="Gok_dth_c3"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c3.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.583)
	Bladex.AddAnmRStep(anm_name,0.758)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.597)
	Bladex.AddAnmLStep(anm_name,0.886)


	anm_name="Gok_dth_c4"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c4.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.277)
	Bladex.AddAnmRStep(anm_name,0.407)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.079)
	Bladex.AddAnmLStep(anm_name,0.242)
	Bladex.AddAnmLRelease(anm_name,0.418)
	Bladex.AddAnmLStep(anm_name,0.524)
	Bladex.AddAnmLRelease(anm_name,0.645)
	Bladex.AddAnmLStep(anm_name,0.796)


	anm_name="Gok_dth_c5"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c5.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.507)
	Bladex.AddAnmRStep(anm_name,0.591)
	Bladex.AddAnmRRelease(anm_name,0.667)
	Bladex.AddAnmRStep(anm_name,0.898)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.521)
	Bladex.AddAnmLStep(anm_name,0.593)
	Bladex.AddAnmLRelease(anm_name,0.659)
	Bladex.AddAnmLStep(anm_name,0.917)


	anm_name="Gok_dth_c6"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c6.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.086)
	Bladex.AddAnmRStep(anm_name,0.134)
	Bladex.AddAnmRRelease(anm_name,0.249)
	Bladex.AddAnmRStep(anm_name,0.343)
	Bladex.AddAnmRRelease(anm_name,0.484)
	Bladex.AddAnmRStep(anm_name,0.536)
	Bladex.AddAnmRRelease(anm_name,0.729)
	Bladex.AddAnmRStep(anm_name,0.838)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.151)
	Bladex.AddAnmLStep(anm_name,0.234)
	Bladex.AddAnmLRelease(anm_name,0.357)
	Bladex.AddAnmLStep(anm_name,0.441)
	Bladex.AddAnmLRelease(anm_name,0.558)
	Bladex.AddAnmLStep(anm_name,0.607)
	Bladex.AddAnmLRelease(anm_name,0.746)
	Bladex.AddAnmLStep(anm_name,0.845)


	anm_name="Gok_dth_c7"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c1.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmLRelease(anm_name,0.040)
	Bladex.AddAnmLStep(anm_name,0.081)



	anm_name="Gok_dth_n00"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n00.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.641)
	Bladex.AddAnmRStep(anm_name,0.878)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.192)
	Bladex.AddAnmLStep(anm_name,0.411)
	Bladex.AddAnmLRelease(anm_name,0.626)
	Bladex.AddAnmLStep(anm_name,0.873)

	anm_name="Gok_dth_n01"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n01.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.500)
	Bladex.AddAnmRStep(anm_name,0.761)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.081)
	Bladex.AddAnmLStep(anm_name,0.356)
	Bladex.AddAnmLRelease(anm_name,0.428)
	Bladex.AddAnmLStep(anm_name,0.515)
	Bladex.AddAnmLRelease(anm_name,0.617)
	Bladex.AddAnmLStep(anm_name,0.772)


	anm_name="Gok_dth_n02"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n02.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.681)
	Bladex.AddAnmRStep(anm_name,0.859)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.315)
	Bladex.AddAnmLStep(anm_name,0.611)
	Bladex.AddAnmLRelease(anm_name,0.703)
	Bladex.AddAnmLStep(anm_name,0.921)

	anm_name="Gok_dth_n03"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n03.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.101)
	Bladex.AddAnmRStep(anm_name,0.271)
	Bladex.AddAnmRRelease(anm_name,0.478)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.530)
	Bladex.AddAnmLStep(anm_name,0.692)

	anm_name="Gok_dth_n04"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n04.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.154)
	Bladex.AddAnmRStep(anm_name,0.198)
	Bladex.AddAnmRRelease(anm_name,0.290)
	Bladex.AddAnmRStep(anm_name,0.347)
	Bladex.AddAnmRRelease(anm_name,0.557)
	Bladex.AddAnmRStep(anm_name,0.595)
	Bladex.AddAnmRRelease(anm_name,0.743)
	Bladex.AddAnmRStep(anm_name,0.838)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.046)
	Bladex.AddAnmLStep(anm_name,0.069)
	Bladex.AddAnmLRelease(anm_name,0.223)
	Bladex.AddAnmLStep(anm_name,0.295)
	Bladex.AddAnmLRelease(anm_name,0.417)
	Bladex.AddAnmLStep(anm_name,0.479)
	Bladex.AddAnmLRelease(anm_name,0.592)
	Bladex.AddAnmLStep(anm_name,0.728)
	Bladex.AddAnmLRelease(anm_name,0.747)
	Bladex.AddAnmLStep(anm_name,0.886)

	anm_name="Gok_dth_n05"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n05.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.825)
	Bladex.AddAnmRStep(anm_name,0.979)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.050)
	Bladex.AddAnmLStep(anm_name,0.138)
	Bladex.AddAnmLRelease(anm_name,0.816)
	Bladex.AddAnmLStep(anm_name,0.950)

	anm_name="Gok_dth_n06"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n06.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.303)
	Bladex.AddAnmRStep(anm_name,0.469)
	Bladex.AddAnmRRelease(anm_name,0.497)
	Bladex.AddAnmRStep(anm_name,0.627)
	Bladex.AddAnmRRelease(anm_name,0.709)
	Bladex.AddAnmRStep(anm_name,0.832)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.100)
	Bladex.AddAnmLStep(anm_name,0.305)
	Bladex.AddAnmLRelease(anm_name,0.347)
	Bladex.AddAnmLStep(anm_name,0.417)
	Bladex.AddAnmLRelease(anm_name,0.474)
	Bladex.AddAnmLStep(anm_name,0.690)

	anm_name="Gok_dth_burn"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_burn.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.089)
	Bladex.AddAnmRStep(anm_name,0.119)
	Bladex.AddAnmRRelease(anm_name,0.203)
	Bladex.AddAnmRStep(anm_name,0.242)
	Bladex.AddAnmRRelease(anm_name,0.284)
	Bladex.AddAnmRStep(anm_name,0.330)
	Bladex.AddAnmRRelease(anm_name,0.378)
	Bladex.AddAnmRStep(anm_name,0.414)
	Bladex.AddAnmRRelease(anm_name,0.467)
	Bladex.AddAnmRStep(anm_name,0.486)
	Bladex.AddAnmRRelease(anm_name,0.539)
	Bladex.AddAnmRStep(anm_name,0.570)
	Bladex.AddAnmRRelease(anm_name,0.671)
	Bladex.AddAnmRStep(anm_name,0.715)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.046)
	Bladex.AddAnmLStep(anm_name,0.075)
	Bladex.AddAnmLRelease(anm_name,0.145)
	Bladex.AddAnmLStep(anm_name,0.185)
	Bladex.AddAnmLRelease(anm_name,0.256)
	Bladex.AddAnmLStep(anm_name,0.278)
	Bladex.AddAnmLRelease(anm_name,0.411)
	Bladex.AddAnmLStep(anm_name,0.463)
	Bladex.AddAnmLRelease(anm_name,0.563)
	Bladex.AddAnmLStep(anm_name,0.599)
	Bladex.AddAnmLRelease(anm_name,0.627)
	Bladex.AddAnmLStep(anm_name,0.667)
	Bladex.AddAnmLRelease(anm_name,0.678)
	Bladex.AddAnmLStep(anm_name,0.713)


	anm_name="Gok_dth_rock"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_rock.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Gok_dth_rockfront"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_rockfront.BMV",anm_name,0,"Great_Ork")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.348)
	Bladex.AddAnmRStep(anm_name,0.796)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.335)
	Bladex.AddAnmLStep(anm_name,0.792)
