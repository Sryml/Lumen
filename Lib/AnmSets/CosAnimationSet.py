import Bladex
import Enm_Def

#	JOG_ANM
def LoadCosAnimationSet(ct_name):

	print "Loading the Cos animation sets..."

	#### Relax ####
	#Bladex.AddAnimFlags("Cos_rlx",0,0,0,1,Enm_Def.BM_XYZ,Enm_Def.HEADF_ENG)

	Bladex.LoadSampledAnimation("../../Anm/Cos_rlx_no.BMV","Rlx_no_Cos",1)
	Bladex.AddAnmRStep("Rlx_no_Cos",0.0)
	Bladex.AddAnmLStep("Rlx_no_Cos",0.0)


	# other
	Bladex.LoadSampledAnimation("../../Anm/Cos_jmp_back1.BMV","Cos_jmp_back1",0)
#	Bladex.AddAnmRStep("Cos_jmp_back1",0.0)
#	Bladex.AddAnmLStep("Cos_jmp_back1",0.0)


	###############
	#
	#    AMBIENT
	#
	###############


	Bladex.LoadSampledAnimation("../../Anm/Cos_alarm.BMV","Cos_alarm",1)
	Bladex.AddAnmRStep("Cos_alarm",0.0)
	Bladex.AddAnmRRelease("Cos_alarm",0.2)
	Bladex.AddAnmRStep("Cos_alarm",0.39)
	Bladex.AddAnmLStep("Cos_alarm",0.0)
	Bladex.AddAnmLRelease("Cos_alarm",0.2)
	Bladex.AddAnmLStep("Cos_alarm",0.39)

	Bladex.LoadSampledAnimation("../../Anm/Cos_fury.BMV","Cos_fury",1)
	Bladex.AddAnmRStep("Cos_fury",0.0)
	Bladex.AddAnmLStep("Cos_fury",0.0)


	### CORRER   ####




	Bladex.LoadSampledAnimation("../../Anm/Cos_jog_no.BMV","Jog_no_Cos",1)
	Bladex.AddAnmLStep("Jog_no_Cos",0.44)
	Bladex.AddAnmLRelease("Jog_no_Cos",0.605)
	Bladex.AddAnmRStep("Jog_no_Cos",0.0)
	Bladex.AddAnmRRelease("Jog_no_Cos",0.254)
	Bladex.AddAnmRStep("Jog_no_Cos",1)
	Bladex.AddStopTests("Jog_no_Cos")

	Bladex.LoadSampledAnimation("../../Anm/Cos_jog_no.BMV","Wlk_no_Cos",1)
	Bladex.AddAnmLStep("Wlk_no_Cos",0.44)
	Bladex.AddAnmLRelease("Wlk_no_Cos",0.605)
	Bladex.AddAnmRStep("Wlk_no_Cos",0.0)
	Bladex.AddAnmRRelease("Wlk_no_Cos",0.254)
	Bladex.AddAnmRStep("Wlk_no_Cos",1)
	Bladex.AddStopTests("Wlk_no_Cos")




	####  WBK ####
	Bladex.LoadSampledAnimation("../../Anm/Cos_wbk_no.BMV","Wbk_no_Cos",1)
	Bladex.AddAnmRStep("Wbk_no_Cos",0.333)
	Bladex.AddAnmRRelease("Wbk_no_Cos",0.638)
	Bladex.AddAnmLStep("Wbk_no_Cos",0)
	Bladex.AddAnmLRelease("Wbk_no_Cos",0.478)
	Bladex.AddAnmLStep("Wbk_no_Cos",1)
	Bladex.AddStopTests("Wbk_no_Cos")


	Bladex.AddAnmEvent("Wbk_no_Cos","StopTest",0.2)
	Bladex.AddAnmEvent("Wbk_no_Cos","StopTest",0.7)


	#
	#### Caminar ####
	#

	"""
	Bladex.LoadSampledAnimation("../../Anm/Cos_wlk_no.BMV","Wlk_no_Cos",1)
	Bladex.AddAnmRStep("Wlk_no_Cos",0.424)
	Bladex.AddAnmRRelease("Wlk_no_Cos",0.920)
	Bladex.AddAnmLStep("Wlk_no_Cos",0.0)
	Bladex.AddAnmLRelease("Wlk_no_Cos",0.197)
	Bladex.AddAnmLStep("Wlk_no_Cos",1.0)
	Bladex.AddStopTests("Wlk_no_Cos")
	"""


	#### Caidas ####


	Bladex.LoadSampledAnimation("../../Anm/Cos_fll_medium_1h.BMV","FallMed_Cos",0)
	Bladex.AddAnmRStep("FallMed_Cos",0.0)
	Bladex.AddAnmLStep("FallMed_Cos",0.0)



	#Caida enorme
	Bladex.LoadSampledAnimation("../../Anm/Cos_dth_fll.BMV","Dth_Fll_Cos",0)
	Bladex.LoadSampledAnimation("../../Anm/Cos_dth_fll2.BMV","Dth_Fll2_Cos",0)
	Bladex.AddAnmRStep("Dth_Fll2_Cos",0.0)
	Bladex.AddAnmLStep("Dth_Fll2_Cos",0.0)


	Bladex.LoadSampledAnimation("../../Anm/Cos_dth_fly.BMV","Cos_dth_fly",0)

	Bladex.LoadSampledAnimation("../../Anm/Cos_dth0.BMV","Cos_dth0",0)
	Bladex.AddAnmRStep("Cos_dth0",0.0)
	Bladex.AddAnmLStep("Cos_dth0",0.0)
	Bladex.AddAnmRRelease("Cos_dth0",0.001)
	Bladex.AddAnmLRelease("Cos_dth0",0.001)



	Bladex.LoadSampledAnimation("../../Anm/Cos_hurt_lite.BMV","Cos_hurt_lite",1)
	Bladex.AddAnmRStep("Cos_hurt_lite",0.0)
	Bladex.AddAnmLStep("Cos_hurt_lite",0.0)




	#### Golpes ####




	Bladex.LoadSampledAnimation("../../Anm/Cos_g_01.BMV","Cos_g_01",0)
	Bladex.AddAnmRStep("Cos_g_01",0)
	Bladex.AddAnmLStep("Cos_g_01",0)
	Bladex.AddAnmRRelease("Cos_g_01",0.175)
	Bladex.AddAnmRStep("Cos_g_01",0.499)
	Bladex.AddAnmRRelease("Cos_g_01",0.586)
	Bladex.AddAnmRStep("Cos_g_01",0.752)
	Bladex.AddAnmLRelease("Cos_g_01",0.175)
	Bladex.AddAnmLStep("Cos_g_01",0.499)
	Bladex.AddAnmLRelease("Cos_g_01",0.586)
	Bladex.AddAnmLStep("Cos_g_01",0.752)


	Bladex.LoadSampledAnimation("../../Anm/Cos_g_02.BMV","Cos_g_02",0)
	Bladex.AddAnmRStep("Cos_g_02",0)
	Bladex.AddAnmLStep("Cos_g_02",0)
	Bladex.AddAnmRRelease("Cos_g_02",0.377)
	Bladex.AddAnmRStep("Cos_g_02",0.923)
	Bladex.AddAnmLRelease("Cos_g_02",0.377)
	Bladex.AddAnmLStep("Cos_g_02",0.923)





	#
	# Movimientos en combate
	#
	anm_name="Cos_attack_l"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.12)
	Bladex.AddAnmLStep(anm_name,0.92)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.121)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddStopTests(anm_name)

	anm_name="Cos_attack_r"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.121)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.12)
	Bladex.AddAnmRStep(anm_name,0.92)
	Bladex.AddStopTests(anm_name)

	anm_name="Cos_attack_f"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.126)
	Bladex.AddAnmRStep(anm_name,0.198)
	Bladex.AddAnmRRelease(anm_name,0.255)
	Bladex.AddAnmRStep(anm_name,0.504)
	Bladex.AddAnmRRelease(anm_name,0.624)
	Bladex.AddAnmRStep(anm_name,0.666)
	Bladex.AddAnmRRelease(anm_name,0.766)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.1261)
	Bladex.AddAnmLStep(anm_name,0.1981)
	Bladex.AddAnmLRelease(anm_name,0.2551)
	Bladex.AddAnmLStep(anm_name,0.5041)
	Bladex.AddAnmLRelease(anm_name,0.6241)
	Bladex.AddAnmLStep(anm_name,0.6661)
	Bladex.AddAnmLRelease(anm_name,0.7661)
	Bladex.AddAnmLStep(anm_name,0.9751)
	Bladex.AddStopTests(anm_name)

	anm_name="Cos_attack_b"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.140)
	Bladex.AddAnmRStep(anm_name,0.369)
	Bladex.AddAnmRRelease(anm_name,0.437)
	Bladex.AddAnmRStep(anm_name,0.590)
	Bladex.AddAnmRRelease(anm_name,0.646)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.1401)
	Bladex.AddAnmLStep(anm_name,0.3691)
	Bladex.AddAnmLRelease(anm_name,0.4371)
	Bladex.AddAnmLStep(anm_name,0.5901)
	Bladex.AddAnmLRelease(anm_name,0.6461)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)


	anm_name="Cos_d_r"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.341)
	Bladex.AddAnmRStep(anm_name,0.693)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.366)
	Bladex.AddAnmLStep(anm_name,0.754)

	anm_name="Cos_d_l"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.379)
	Bladex.AddAnmRStep(anm_name,0.678)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.150)
	Bladex.AddAnmRStep(anm_name,0.370)
	Bladex.AddAnmLRelease(anm_name,0.396)
	Bladex.AddAnmLStep(anm_name,0.829)



#	anm_name="Cos_rlx_f"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0)



	anm_name="Cos_jmp_no"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV","Cos_jmp_no",0)
	Bladex.AddAnmRStep("Cos_jmp_no",0.0)
	Bladex.AddAnmRRelease("Cos_jmp_no",0.223)
	Bladex.AddAnmRStep("Cos_jmp_no",0.795)
	Bladex.AddAnmLStep("Cos_jmp_no",0.0)
	Bladex.AddAnmLRelease("Cos_jmp_no",0.297)
	Bladex.AddAnmLStep("Cos_jmp_no",0.745)


	#
	# Slip
	#
	anm_name="Cos_slip"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)





	#
	# Climb
	#
#	anm_name="Cos_clmb_high_no"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0)
#	Bladex.AddAnmRRelease(anm_name,0.30)
#	Bladex.AddAnmLRelease(anm_name,0.30)
#	Bladex.AddAnmRStep(anm_name,0.77)
#	Bladex.AddAnmLStep(anm_name,0.78)
#
	anm_name="Cos_clmb_medium_no"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.30)
	Bladex.AddAnmLRelease(anm_name,0.30)
	Bladex.AddAnmRStep(anm_name,0.77)
	Bladex.AddAnmLStep(anm_name,0.78)

#	anm_name="Cos_clmb_medlow_no"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0)
#	Bladex.AddAnmRRelease(anm_name,0.30)
#	Bladex.AddAnmLRelease(anm_name,0.30)
#	Bladex.AddAnmRStep(anm_name,0.77)
#	Bladex.AddAnmLStep(anm_name,0.78)
#
#	anm_name="Cos_clmb_low_no"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0)
#	Bladex.AddAnmRRelease(anm_name,0.30)
#	Bladex.AddAnmLRelease(anm_name,0.30)
#	Bladex.AddAnmRStep(anm_name,0.77)
#	Bladex.AddAnmLStep(anm_name,0.78)
