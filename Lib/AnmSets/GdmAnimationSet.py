import Bladex
import Enm_Def



def LoadGdmAnimationSet(ct_name):

	print "Loading GreatDemon Animations..."




	anm_name="Gdm_wlk_no"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.51)
	Bladex.AddAnmRStep(anm_name,1.0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.12)
	Bladex.AddAnmLStep(anm_name,0.61)
	Bladex.AddStopTests(anm_name)

	anm_name="Gdm_wbk_no"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.075)
	Bladex.AddAnmRStep(anm_name,0.550)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.475)
	Bladex.AddAnmLStep(anm_name,1.000)
	Bladex.AddStopTests(anm_name)

	anm_name="Gdm_rlx_no"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.0)

	#anm_name="Gdm_mgc_hurt"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	#Bladex.AddAnmLStep(anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmLRelease(anm_name,0.21)
	#Bladex.AddAnmLStep(anm_name,0.42)
	#Bladex.AddAnmRRelease(anm_name,0.48)
	#Bladex.AddAnmRStep(anm_name,0.83)

	#anm_name="Gdm_appears"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0.0)
	#Bladex.AddAnmLStep(anm_name,0.0)

	anm_name="Gdm_g_01"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.0)

	anm_name="Gdm_g_12"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.251)
	Bladex.AddAnmLRelease(anm_name,0.625)
	Bladex.AddAnmRRelease(anm_name,0.327)
	Bladex.AddAnmRStep(anm_name,0.616)
	Bladex.AddAnmLStep(anm_name,0.873)
	Bladex.AddAnmLRelease(anm_name,1.0)

	anm_name="Gdm_g_claw"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.286)
	Bladex.AddAnmLStep(anm_name,0.481)
	Bladex.AddAnmLRelease(anm_name,0.789)
	Bladex.AddAnmLStep(anm_name,0.922)


	anm_name="Gdm_g_quake"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.189)
	Bladex.AddAnmLRelease(anm_name,0.503)
	Bladex.AddAnmLStep(anm_name,0.602)
	Bladex.AddAnmLRelease(anm_name,0.743)
	Bladex.AddAnmLStep(anm_name,0.868)
	Bladex.AddAnmLRelease(anm_name,1.0)


	anm_name="Gdm_g_magic"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.523)
	Bladex.AddAnmRStep(anm_name,0.641)
	Bladex.AddAnmRRelease(anm_name,0.8)
	Bladex.AddAnmRStep(anm_name,1.0)


	anm_name="Gdm_g_back"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.1)
	Bladex.AddAnmLStep(anm_name,0.2)
	Bladex.AddAnmLRelease(anm_name,0.63)
	Bladex.AddAnmLStep(anm_name,0.8)
	Bladex.AddAnmRRelease(anm_name,0.2)
	Bladex.AddAnmRStep(anm_name,0.31)
	Bladex.AddAnmRRelease(anm_name,0.85)
	Bladex.AddAnmRStep(anm_name,0.93)
#	Bladex.AddStopTests(anm_name)



	anm_name="Gdm_g_spit_around"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)

	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)


	anm_name="Gdm_g_spit_f"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)

	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)


	anm_name="Gdm_g_spitball"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)

	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.298)
	Bladex.AddAnmRStep(anm_name,0.405)
	Bladex.AddAnmRRelease(anm_name,0.84)
	Bladex.AddAnmRStep(anm_name,0.94)



	anm_name="Gdm_mgc_df"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)

	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.15)
	Bladex.AddAnmRStep(anm_name,0.39)
	Bladex.AddAnmRRelease(anm_name,0.76)
	Bladex.AddAnmRStep(anm_name,0.94)


	anm_name="Gdm_dth0"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.392)
	Bladex.AddAnmLRelease(anm_name,0.357)
	Bladex.AddAnmRStep(anm_name,0.67)
	Bladex.AddAnmLStep(anm_name,0.433)
	Bladex.AddAnmLRelease(anm_name,0.551)
	Bladex.AddAnmLStep(anm_name,0.641)



	anm_name="Gdm_hurt_big"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.404)
	Bladex.AddAnmLRelease(anm_name,0.202)
	Bladex.AddAnmRStep(anm_name,0.834)
	Bladex.AddAnmLStep(anm_name,0.414)
