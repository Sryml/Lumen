import Bladex
import Enm_Def





def LoadAnkAnimationSet(ct_name):

	print "Loading the An-Ahkard animation sets...(Se�or obscuro)"

	#### Relax ####

	Bladex.LoadSampledAnimation("../../Anm/Ank_rlx.BMV","Rlx_no_Ank",1)
	Bladex.AddAnmRStep("Rlx_no_Ank",0.0)
	Bladex.AddAnmLStep("Rlx_no_Ank",0.0)




	Bladex.LoadSampledAnimation("../../Anm/Ank_wbk.BMV","Wbk_no_Ank",1)
	Bladex.AddAnmRStep("Wbk_no_Ank",0.000)
	Bladex.AddAnmRRelease("Wbk_no_Ank",0.025)
	Bladex.AddAnmRStep("Wbk_no_Ank",0.450)
	Bladex.AddAnmLStep("Wbk_no_Ank",0.000)
	Bladex.AddAnmLRelease("Wbk_no_Ank",0.400)
	Bladex.AddAnmLStep("Wbk_no_Ank",1.000)

	Bladex.AddStopTests("Wbk_no_Ank")






	Bladex.LoadSampledAnimation("../../Anm/Ank_wlk.BMV","Wlk_no_Ank",1)
	Bladex.AddAnmRStep("Wlk_no_Ank",0.000)
	Bladex.AddAnmRRelease("Wlk_no_Ank",0.575)
	Bladex.AddAnmRStep("Wlk_no_Ank",1.000)
	Bladex.AddAnmLStep("Wlk_no_Ank",0.000)
	Bladex.AddAnmLRelease("Wlk_no_Ank",0.064)
	Bladex.AddAnmLStep("Wlk_no_Ank",0.574)


	Bladex.AddStopTests("Wlk_no_Ank")



	anm_name="Ank_g_mgc03"
	Bladex.LoadSampledAnimation("../../Anm/Ank_g_mgc03.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmEvent("Ank_g_mgc03","Aim",0.0500)
	Bladex.AddAnmEvent("Ank_g_mgc03","Fire",0.3700) #0.3833)



	anm_name="Ank_g_mgc02"
	Bladex.LoadSampledAnimation("../../Anm/Ank_g_mgc02.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.425)
	Bladex.AddAnmLStep(anm_name,0.575)
	Bladex.AddAnmLRelease(anm_name,0.808)
	Bladex.AddAnmLStep(anm_name,0.900)
	Bladex.AddAnmEvent("Ank_g_mgc02","Aim",0.08)
	Bladex.AddAnmEvent("Ank_g_mgc02","Fire",0.56)




	anm_name="Ank_g_mgc01"
	Bladex.LoadSampledAnimation("../../Anm/Ank_g_mgc01.BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.430)
	Bladex.AddAnmLStep(anm_name,0.530)
	Bladex.AddAnmLRelease(anm_name,0.740)
	Bladex.AddAnmLStep(anm_name,0.840)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmEvent("Ank_g_mgc01","Aim",0.09)
	Bladex.AddAnmEvent("Ank_g_mgc01","Fire",0.54)


	anm_name="Ank_g_07"
	Bladex.LoadSampledAnimation("../../Anm/Ank_g_07.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.303)
	Bladex.AddAnmLStep(anm_name,0.409)
	Bladex.AddAnmLRelease(anm_name,0.621)
	Bladex.AddAnmLStep(anm_name,0.727)


	anm_name="Ank_g_02"
	Bladex.LoadSampledAnimation("../../Anm/Ank_g_02.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.028)
	Bladex.AddAnmLStep(anm_name,0.306)
	Bladex.AddAnmLRelease(anm_name,0.750)
	Bladex.AddAnmLStep(anm_name,0.931)



	anm_name="Ank_g_01"
	Bladex.LoadSampledAnimation("../../Anm/Ank_g_01.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Ank_fll"
	Bladex.LoadSampledAnimation("../../Anm/Ank_fll.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.250)
	Bladex.AddAnmLStep(anm_name,0.250)
