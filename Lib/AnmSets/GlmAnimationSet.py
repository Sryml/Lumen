import Bladex
import Enm_Def



def LoadGlmAnimationSet(ct_name):

	print "Loading the "+ct_name+"s animation set..."

	#### MOVIMIENTOS NORMALES ####

	anm_name="Glm_jog_no"

	Bladex.LoadSampledAnimation("../../Anm/Glm_jog_no.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.533)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.477)
	Bladex.AddAnmLRelease(anm_name,0.956)

	Bladex.AddStopTests(anm_name)


	anm_name="Glm_wbk_no"

	Bladex.LoadSampledAnimation("../../Anm/Glm_wbk_no.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.604)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.053)
	Bladex.AddAnmLStep(anm_name,0.422)

	Bladex.AddStopTests(anm_name)



	anm_name="Glm_wlk_no"

	Bladex.LoadSampledAnimation("../../Anm/Glm_wlk_no.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.750)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.233)
	Bladex.AddAnmLStep(anm_name,0.500)

	Bladex.AddStopTests(anm_name)


	anm_name="Glm_rlx_no"

	Bladex.LoadSampledAnimation("../../Anm/Glm_rlx_no.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)









	######### GOLPES ###########


	anm_name="Glm_g_01"

	Bladex.LoadSampledAnimation("../../Anm/Glm_g_01.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.143)
	Bladex.AddAnmRStep(anm_name,0.286)
	Bladex.AddAnmRRelease(anm_name,0.743)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.000)




	anm_name="Glm_g_114"

	Bladex.LoadSampledAnimation("../../Anm/Glm_g_114.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.338)
	Bladex.AddAnmRStep(anm_name,0.463)
	Bladex.AddAnmRRelease(anm_name,0.725)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.000)




	anm_name="Glm_g_12"

	Bladex.LoadSampledAnimation("../../Anm/Glm_g_12.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.222)
	Bladex.AddAnmRStep(anm_name,0.389)
	Bladex.AddAnmRRelease(anm_name,0.736)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.000)




	anm_name="Glm_g_21_27"

	Bladex.LoadSampledAnimation("../../Anm/Glm_g_21_27.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.140)
	Bladex.AddAnmRStep(anm_name,0.335)
	Bladex.AddAnmRRelease(anm_name,0.632)
	Bladex.AddAnmRStep(anm_name,0.807)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.373)
	Bladex.AddAnmLStep(anm_name,0.610)




	anm_name="Glm_g_21"

	Bladex.LoadSampledAnimation("../../Anm/Glm_g_21.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.162)
	Bladex.AddAnmRStep(anm_name,0.416)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.430)
	Bladex.AddAnmLStep(anm_name,0.710)




	anm_name="Glm_g_31"

	Bladex.LoadSampledAnimation("../../Anm/Glm_g_31.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.080)
	Bladex.AddAnmRStep(anm_name,0.320)
	Bladex.AddAnmRRelease(anm_name,0.610)
	Bladex.AddAnmRStep(anm_name,0.740)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.062)



	anm_name="Glm_g_spit"

	Bladex.LoadSampledAnimation("../../Anm/Glm_spit.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)


#	anm_name="Glm_g_1tw"
#
#	Bladex.LoadSampledAnimation("../../Anm/Glm_1tw.BMV",anm_name,1)
#	Bladex.AddAnmRStep(anm_name,0.000)
#	Bladex.AddAnmRRelease(anm_name,0.400)
#	Bladex.AddAnmRStep(anm_name,0.489)
#	Bladex.AddAnmRRelease(anm_name,0.767)
#	Bladex.AddAnmRStep(anm_name,0.900)
#	Bladex.AddAnmLStep(anm_name,0.000)










	#### VARIOS ####



	anm_name="Glm_hurt_big"

	Bladex.LoadSampledAnimation("../../Anm/Glm_hurt_big.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.150)
	Bladex.AddAnmRStep(anm_name,0.325)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.310)
	Bladex.AddAnmLStep(anm_name,0.520)




	anm_name="Glm_g_1tw"

	Bladex.LoadSampledAnimation("../../Anm/Glm_1tw.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.400)
	Bladex.AddAnmRStep(anm_name,0.489)
	Bladex.AddAnmRRelease(anm_name,0.767)
	Bladex.AddAnmRStep(anm_name,0.900)
	Bladex.AddAnmLStep(anm_name,0.000)






	anm_name="Glm_fll_low"

	Bladex.LoadSampledAnimation("../../Anm/Glm_fll_low.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.194)
	Bladex.AddAnmLStep(anm_name,0.194)



	anm_name="Glm_clmb_low"

	Bladex.LoadSampledAnimation("../../Anm/Glm_clmb_low.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.091)
	Bladex.AddAnmRStep(anm_name,0.394)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.652)
	Bladex.AddAnmLStep(anm_name,0.909)


	#Caida enorme
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_fll.BMV","Dth_Fll_Glm",0,"Golem_stone")
	#Bladex.AddAnmRStep("Dth_Fll_Glm",0.0)
	#Bladex.AddAnmLStep("Dth_Fll_Glm",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_fll2.BMV","Dth_Fll2_Glm",0,"Golem_stone")
	Bladex.AddAnmRStep("Dth_Fll2_Glm",0.0)
	Bladex.AddAnmLStep("Dth_Fll2_Glm",0.0)


	anm_name="Glm_slip"
	Bladex.LoadSampledAnimation("../../Anm/Glm_slip.BMV",anm_name,1,)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Glm_slip_b"
	Bladex.LoadSampledAnimation("../../Anm/Glm_slip_b.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Glm_derrape"
	Bladex.LoadSampledAnimation("../../Anm/Glm_derrape.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.099)
	Bladex.AddAnmRStep(anm_name,0.32)
	Bladex.AddAnmLStep(anm_name,0.105)
	Bladex.AddAnmLRelease(anm_name,0.36)
	Bladex.AddAnmLStep(anm_name,0.98)




###################
#                 #
# A�adidos Luismi #
#                 #
###################





####	Muerte

	anm_name="Glm_dth0"

	Bladex.LoadSampledAnimation("../../Anm/Glm_dth0.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.117)
	Bladex.AddAnmRStep(anm_name,0.239)
	Bladex.AddAnmRRelease(anm_name,0.769)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.253)
	Bladex.AddAnmLStep(anm_name,0.378)
	Bladex.AddAnmLRelease(anm_name,0.758)
