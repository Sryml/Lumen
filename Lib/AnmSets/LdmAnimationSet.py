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



def LoadLdmAnimationSet(ct_name):

	print "Loading the Demon animation sets..."

	Bladex.LoadSampledAnimation("../../Anm/Ldm_appears.BMV","Ldm_appears",0)
	Bladex.AddAnmRStep("Ldm_appears",0)
	Bladex.AddAnmLStep("Ldm_appears",0)

	### ANDARES ####

	anm_name="Ldm_wlk_no"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.369)
	Bladex.AddAnmRStep(anm_name,0.545)
	Bladex.AddAnmLRelease(anm_name,0.816)
	Bladex.AddAnmLStep(anm_name,1.0)
	Bladex.AddStopTests(anm_name)

	anm_name="Ldm_wbk_no"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.310)
	Bladex.AddAnmLStep(anm_name,0.548)
	Bladex.AddAnmRRelease(anm_name,0.735)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddStopTests(anm_name)


	### GOLPES ENCARADO ####

	anm_name="Ldm_g_03"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.175)
	Bladex.AddAnmRStep(anm_name,0.281)
	Bladex.AddAnmLRelease(anm_name,0.348)
	Bladex.AddAnmLStep(anm_name,0.417)
	Bladex.AddAnmRRelease(anm_name,0.702)
	Bladex.AddAnmRStep(anm_name,0.878)




	anm_name="Ldm_g_06"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.109)
	Bladex.AddAnmLStep(anm_name,0.232)
	Bladex.AddAnmRRelease(anm_name,0.277)
	Bladex.AddAnmRStep(anm_name,0.421)
	Bladex.AddAnmRRelease(anm_name,0.678)
	Bladex.AddAnmRStep(anm_name,0.854)




	anm_name="Ldm_g_07"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.103)
	Bladex.AddAnmLStep(anm_name,0.248)
	Bladex.AddAnmRRelease(anm_name,0.347)
	Bladex.AddAnmLRelease(anm_name,0.445)
	Bladex.AddAnmLStep(anm_name,0.500)
	Bladex.AddAnmRStep(anm_name,0.540)
	Bladex.AddAnmLRelease(anm_name,0.600)
	Bladex.AddAnmLStep(anm_name,0.691)
	Bladex.AddAnmRRelease(anm_name,0.697)
	Bladex.AddAnmRStep(anm_name,0.848)



	anm_name="Ldm_g_22"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.080)
	Bladex.AddAnmRRelease(anm_name,0.103)
	Bladex.AddAnmLStep(anm_name,0.151)
	Bladex.AddAnmRStep(anm_name,0.153)
	Bladex.AddAnmRRelease(anm_name,0.274)
	Bladex.AddAnmLRelease(anm_name,0.300)
	Bladex.AddAnmRStep(anm_name,0.356)
	Bladex.AddAnmLStep(anm_name,0.418)
	Bladex.AddAnmLRelease(anm_name,0.500)
	Bladex.AddAnmRRelease(anm_name,0.528)
	Bladex.AddAnmLStep(anm_name,0.564)
	Bladex.AddAnmRStep(anm_name,0.600)
	Bladex.AddAnmLRelease(anm_name,0.756)
	Bladex.AddAnmLStep(anm_name,0.840)



	anm_name="Ldm_g_27"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.138)
	Bladex.AddAnmLRelease(anm_name,0.189)
	Bladex.AddAnmRStep(anm_name,0.197)
	Bladex.AddAnmLStep(anm_name,0.251)
	Bladex.AddAnmLRelease(anm_name,0.413)
	Bladex.AddAnmRRelease(anm_name,0.424)
	Bladex.AddAnmRStep(anm_name,0.454)
	Bladex.AddAnmLStep(anm_name,0.494)
	Bladex.AddAnmRRelease(anm_name,0.636)
	Bladex.AddAnmRStep(anm_name,0.710)
	Bladex.AddAnmRRelease(anm_name,0.835)
	Bladex.AddAnmRStep(anm_name,0.903)



	anm_name="Ldm_g_spit"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.007)
	Bladex.AddAnmRStep(anm_name,0.201)
	Bladex.AddAnmRRelease(anm_name,0.740)
	Bladex.AddAnmRStep(anm_name,0.928)


	anm_name="Ldm_g_jumpl"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.410)
	Bladex.AddAnmRRelease(anm_name,0.490)
	#Bladex.AddAnmRStep(anm_name,0.558) # dummy step, to check floor when reappearing
	#Bladex.AddAnmLStep(anm_name,0.558) # dummy step, to check floor when reappearing
	Bladex.AddAnmRStep(anm_name,0.794)
	Bladex.AddAnmLStep(anm_name,0.794)


	anm_name="Ldm_g_jumpr"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.267)
	Bladex.AddAnmLRelease(anm_name,0.367)
	#Bladex.AddAnmRStep(anm_name,0.497) # dummy step, to check floor when reappearing
	#Bladex.AddAnmLStep(anm_name,0.497) # dummy step, to check floor when reappearing
	Bladex.AddAnmRStep(anm_name,0.671)
	Bladex.AddAnmLStep(anm_name,0.964)


	anm_name="Ldm_fll_high"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)


	anm_name="Ldm_fll_low"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)



	anm_name="Ldm_jog_no"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.366)
	Bladex.AddAnmLStep(anm_name,0.468)
	Bladex.AddAnmLRelease(anm_name,0.835)
	Bladex.AddAnmRStep(anm_name,1.0)
	Bladex.AddStopTests(anm_name)



	anm_name="Ldm_attack_f"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.369)
	Bladex.AddAnmRStep(anm_name,0.545)
	Bladex.AddAnmLRelease(anm_name,0.816)
	Bladex.AddAnmLStep(anm_name,1.0)
	Bladex.AddStopTests(anm_name)


	anm_name="Ldm_attack_b"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.290)
	Bladex.AddAnmRStep(anm_name,0.480)
	Bladex.AddAnmLRelease(anm_name,0.762)
	Bladex.AddAnmLStep(anm_name,1.0)
	Bladex.AddStopTests(anm_name)


	anm_name="Ldm_attack_r"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.277)
	Bladex.AddAnmRStep(anm_name,0.385)
	Bladex.AddAnmLRelease(anm_name,0.832)
	Bladex.AddAnmLStep(anm_name,1.0)
	Bladex.AddStopTests(anm_name)


	anm_name="Ldm_attack_l"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.418)
	Bladex.AddAnmRStep(anm_name,0.541)
	Bladex.AddAnmLRelease(anm_name,0.836)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)


	#anm_name="Ldm_df1"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmLStep(anm_name,0)



	anm_name="Ldm_rlx_f"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

#	anm_name="Ldm_t_r_no"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0)
#	Bladex.AddAnmRRelease(anm_name,0.127)
#	Bladex.AddAnmRStep(anm_name,0.467)
#	Bladex.AddAnmLRelease(anm_name,0.839)
#	Bladex.AddAnmLStep(anm_name,1.0)
#	Bladex.AddStopTests(anm_name)
#
#
#	anm_name="Ldm_t_l_no"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0)
#	Bladex.AddAnmLRelease(anm_name,0.353)
#	Bladex.AddAnmLStep(anm_name,0.420)
#	Bladex.AddAnmRRelease(anm_name,0.893)
#	Bladex.AddAnmRStep(anm_name,1.0)
#	Bladex.AddStopTests(anm_name)


	anm_name="Ldm_hurt_big"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.147)
	Bladex.AddAnmLRelease(anm_name,0.216)
	Bladex.AddAnmRStep(anm_name,0.249)
	Bladex.AddAnmLRelease(anm_name,0.268)
	Bladex.AddAnmRRelease(anm_name,0.440)
	Bladex.AddAnmLStep(anm_name,0.496)
	Bladex.AddAnmRStep(anm_name,0.694)


	anm_name="Ldm_hurt_f_big"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.248)
	Bladex.AddAnmRStep(anm_name,0.329)
	Bladex.AddAnmLRelease(anm_name,0.334)
	Bladex.AddAnmRRelease(anm_name,0.433)
	Bladex.AddAnmRStep(anm_name,0.560)
	Bladex.AddAnmLRelease(anm_name,0.642)
	Bladex.AddAnmLStep(anm_name,0.718)


	anm_name="Ldm_hurt_f_lite"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.312)
	Bladex.AddAnmRRelease(anm_name,0.334)
	Bladex.AddAnmLStep(anm_name,0.388)
	Bladex.AddAnmRStep(anm_name,0.540)
	Bladex.AddAnmLRelease(anm_name,0.613)
	Bladex.AddAnmLStep(anm_name,0.843)


	anm_name="Ldm_hurt_lite"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.181)
	Bladex.AddAnmLRelease(anm_name,0.357)
	Bladex.AddAnmRStep(anm_name,0.389)
	Bladex.AddAnmLRelease(anm_name,0.372)
	Bladex.AddAnmLStep(anm_name,0.494)

	anm_name="Ldm_patrol1"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)


	anm_name="Ldm_rlx_no"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)


	anm_name="Ldm_rlx_f_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)


	#anm_name="Ldm_hurt_lite"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmLStep(anm_name,0)
	#Bladex.AddAnmRRelease(anm_name,0.470)
	#Bladex.AddAnmLRelease(anm_name,0.532)
	#Bladex.AddAnmRStep(anm_name,0.687)
	#Bladex.AddAnmLStep(anm_name,0.699)


	#anm_name="Ldm_jmp_no"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmLStep(anm_name,0)
	#Bladex.AddAnmRRelease(anm_name,0.468)
	#Bladex.AddAnmLRelease(anm_name,0.468)
	#Bladex.AddAnmRStep(anm_name,0.694)
	#Bladex.AddAnmLStep(anm_name,0.705)

#Caida enorme
	Bladex.LoadSampledAnimation("../../Anm/Ldm_dth_fll.BMV","Dth_Fll_Ldm",1)
	#Bladex.AddAnmRStep("Dth_Fll_Ldm",0.0)
	#Bladex.AddAnmLStep("Dth_Fll_Ldm",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Ldm_dth_fll2.BMV","Dth_Fll2_Ldm",0)
	Bladex.AddAnmRStep("Dth_Fll2_Ldm",0.0)
	Bladex.AddAnmLStep("Dth_Fll2_Ldm",0.0)


#### Muerte


	anm_name="Ldm_dth0"
	Bladex.LoadSampledAnimation("../../Anm/Ldm_dth_disap.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.028)
	Bladex.AddAnmLRelease(anm_name,0.028)