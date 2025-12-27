import Bladex
import Enm_Def



def LoadSlmAnimationSet(ct_name):

	print "Loading the Salamander's animation sets..."

	#### Relax ####


	Bladex.LoadSampledAnimation("../../Anm/Slm_rlx_no.BMV","Rlx_no_Slm",1)
	Bladex.AddAnmRStep("Rlx_no_Slm",0.0)
	Bladex.AddAnmLStep("Rlx_no_Slm",0.0)



	### CORRER   ####


	Bladex.LoadSampledAnimation("../../Anm/Slm_jog_no.BMV","Jog_no_Slm",1)
	Bladex.AddAnmLStep("Jog_no_Slm",0.0)
	Bladex.AddAnmRStep("Jog_no_Slm",0.467)
	Bladex.AddAnmLRelease("Jog_no_Slm",0.437)
	Bladex.AddAnmLStep("Jog_no_Slm",1)
	Bladex.AddAnmRRelease("Jog_no_Slm",0.947)
	Bladex.AddStopTests("Jog_no_Slm")




	#### SNEAK   ####



	####  WBK ####

	Bladex.LoadSampledAnimation("../../Anm/Slm_wbk_no.BMV","Wbk_no_Slm",1)
	Bladex.AddAnmRStep("Wbk_no_Slm",0.0)
	Bladex.AddAnmRRelease("Wbk_no_Slm",0.576)
	Bladex.AddAnmRStep("Wbk_no_Slm",1)
	Bladex.AddAnmLStep("Wbk_no_Slm",0.0)
	Bladex.AddAnmLRelease("Wbk_no_Slm",0.1)
	Bladex.AddAnmLStep("Wbk_no_Slm",0.5)
	Bladex.AddStopTests("Wbk_no_Slm")


	#
	#### Caminar ####
	#


	Bladex.LoadSampledAnimation("../../Anm/Slm_Wlk_no.BMV","Wlk_no_Slm",1)
	Bladex.AddAnmRStep("Wlk_no_Slm",0)
	Bladex.AddAnmLStep("Wlk_no_Slm",0)
	Bladex.AddAnmLRelease("Wlk_no_Slm",0.207)
	Bladex.AddAnmLStep("Wlk_no_Slm",0.512)
	Bladex.AddAnmRRelease("Wlk_no_Slm",0.682)
	Bladex.AddAnmRStep("Wlk_no_Slm",1)
	Bladex.AddStopTests("Wlk_no_Slm")



	#### Caidas ####


	#Bladex.LoadSampledAnimation("../../Anm/Slm_fll_med_1h.BMV","FallMed_Slm",0)
	#Bladex.AddAnmRStep("FallMed_Slm",0.0)
	#Bladex.AddAnmLStep("FallMed_Slm",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Slm_fll_low_no.BMV","FallLow_Slm",0)
	Bladex.AddAnmRStep("FallLow_Slm",0.0)
	Bladex.AddAnmLStep("FallLow_Slm",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Slm_fll_high.BMV","FallHigh_Slm",0)
	Bladex.AddAnmRStep("FallHigh_Slm",0.0)
	Bladex.AddAnmLStep("FallHigh_Slm",0.0)

	#Caida enorme
	Bladex.LoadSampledAnimation("../../Anm/Slm_dth_fll.BMV","Dth_Fll_Slm",0)
	Bladex.LoadSampledAnimation("../../Anm/Slm_dth_fll2.BMV","Dth_Fll2_Slm",0)
	Bladex.AddAnmRStep("Dth_Fll2_Slm",0.0)
	Bladex.AddAnmLStep("Dth_Fll2_Slm",0.0)



	anm_name="Slm_dth0"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.001)
	Bladex.AddAnmRRelease(anm_name,0.001)

	#
	# Ataques
	#


	Bladex.LoadSampledAnimation("../../Anm/Slm_g_bite.BMV","Slm_g_bite",0)
	Bladex.AddAnmRStep("Slm_g_bite",0)
	Bladex.AddAnmRRelease("Slm_g_bite",0.18)
	Bladex.AddAnmRStep("Slm_g_bite",0.648)
	Bladex.AddAnmRRelease("Slm_g_bite",0.704)
	Bladex.AddAnmRStep("Slm_g_bite",0.820)
	Bladex.AddAnmLStep("Slm_g_bite",0)
	Bladex.AddAnmLRelease("Slm_g_bite",0.112)
	Bladex.AddAnmLStep("Slm_g_bite",0.179)
	Bladex.AddAnmLRelease("Slm_g_bite",0.218)
	Bladex.AddAnmLStep("Slm_g_bite",0.336)
	Bladex.AddAnmLRelease("Slm_g_bite",0.656)
	Bladex.AddAnmLStep("Slm_g_bite",0.805)
	Bladex.AddAnmLRelease("Slm_g_bite",0.883)
	Bladex.AddAnmLStep("Slm_g_bite",1)


	anm_name="Slm_g_spit"
	Bladex.LoadSampledAnimation("../../Anm/Slm_spit.BMV","Slm_g_spit",0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.19)
	Bladex.AddAnmRStep(anm_name,0.43)
	Bladex.AddAnmRRelease(anm_name,0.51)
	Bladex.AddAnmRStep(anm_name,0.59)
	Bladex.AddAnmRRelease(anm_name,0.71)
	Bladex.AddAnmRStep(anm_name,0.82)
	Bladex.AddAnmLRelease(anm_name,0.10)
	Bladex.AddAnmLStep(anm_name,0.18)
	Bladex.AddAnmLRelease(anm_name,0.21)
	Bladex.AddAnmLStep(anm_name,0.31)
	Bladex.AddAnmLRelease(anm_name,0.66)
	Bladex.AddAnmLStep(anm_name,0.77)


	anm_name="Slm_g_r"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.189)
	Bladex.AddAnmRStep(anm_name,0.382)
	Bladex.AddAnmRRelease(anm_name,0.751)
	Bladex.AddAnmRStep(anm_name,0.983)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.150)



	#
	# Movimientos en combate
	#

	anm_name="Slm_clmb_low"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.23)
	Bladex.AddAnmRStep(anm_name,0.64)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.25)
	Bladex.AddAnmLStep(anm_name,0.64)


	anm_name="Slm_hurt_f_big"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.0001)
	Bladex.AddAnmRRelease(anm_name,0.0001)
	Bladex.AddAnmLStep(anm_name,0.747)
	Bladex.AddAnmRStep(anm_name,0.980)
	Bladex.AddAnmRRelease(anm_name,1)
	Bladex.AddAnmLRelease(anm_name,1)


	anm_name="Slm_hurt_f_lite"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRStep(anm_name,0.0)

	anm_name="Slm_patrol"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRStep(anm_name,0.0)