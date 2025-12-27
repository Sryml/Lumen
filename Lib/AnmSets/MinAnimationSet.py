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



def LoadMinAnimationSet(ct_name):

	print "Loading the Min animation sets..."



	Bladex.LoadSampledAnimation("../../Anm/Min_rlx_1h.BMV","Rlx_1h_Min",1)
	Bladex.AddAnmRStep("Rlx_1h_Min",0.0)
	Bladex.AddAnmLStep("Rlx_1h_Min",0.0)



	anm_name="Jog_1h_Min"
	Bladex.LoadSampledAnimation("../../Anm/Min_jog_1h.BMV","Jog_1h_Min",1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.646)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.108)
	Bladex.AddAnmLStep(anm_name,0.512)
	Bladex.AddStopTests("Jog_1h_Min")




	anm_name="Wlk_1h_Min"
	Bladex.LoadSampledAnimation("../../Anm/Min_wlk_1h.BMV","Wlk_1h_Min",1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.350)
	Bladex.AddAnmRStep(anm_name,0.538)
	Bladex.AddAnmRRelease(anm_name,0.800)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.283)
	Bladex.AddAnmLRelease(anm_name,0.582)
	Bladex.AddAnmLStep(anm_name,0.778)
	Bladex.AddAnmLRelease(anm_name,1.000)
	Bladex.AddStopTests("Wlk_1h_Min")







	####  WBK ####

	anm_name="Wbk_1h_Min"
	Bladex.LoadSampledAnimation("../../Anm/Min_wbk_1h.BMV","Wbk_1h_Min",1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.327)
	Bladex.AddAnmRStep(anm_name,0.530)
	Bladex.AddAnmRRelease(anm_name,0.831)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.057)
	Bladex.AddAnmLStep(anm_name,0.270)
	Bladex.AddAnmLRelease(anm_name,0.580)
	Bladex.AddAnmLStep(anm_name,0.777)
	Bladex.AddStopTests("Wbk_1h_Min")


	Bladex.AddAnmEvent("Wbk_1h_Min","StopTest",0.2)
	Bladex.AddAnmEvent("Wbk_1h_Min","StopTest",0.7)





	#
	#### Caminar ####
	#

#	Bladex.LoadSampledAnimation("../../Anm/Min_wlk_1h.BMV","Wlk_1h_Min",1)
#
#	Bladex.AddAnmRStep("Wlk_1h_Min",0.290)
#	Bladex.AddAnmRRelease("Wlk_1h_Min",0.543)
#	Bladex.AddAnmRStep("Wlk_1h_Min",0.763)
#	Bladex.AddAnmRRelease("Wlk_1h_Min",1)
#	Bladex.AddAnmLStep("Wlk_1h_Min",0)
#	Bladex.AddAnmLRelease("Wlk_1h_Min",0.294)
#	Bladex.AddAnmLStep("Wlk_1h_Min",0.537)
#	Bladex.AddAnmLRelease("Wlk_1h_Min",0.789)
#	Bladex.AddAnmLStep("Wlk_1h_Min",1)
#	Bladex.AddStopTests("Wlk_1h_Min")





	Bladex.LoadSampledAnimation("../../Anm/Min_fll_low.BMV","FallLow_Min",0)
	Bladex.AddAnmRStep("FallLow_Min",0.0)
	Bladex.AddAnmLStep("FallLow_Min",0.0)

	#Caida enorme
	Bladex.LoadSampledAnimation("../../Anm/Min_dth_fll.BMV","Dth_Fll_Min",1)
	anm_name="Min_dth_fll2"
	Bladex.LoadSampledAnimation("../../Anm/Min_dth_fll2.BMV","Min_dth_fll2",0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)


	#
	# Ataques
	#


	anm_name="Min_g_01"
	Bladex.LoadSampledAnimation("../../Anm/Min_g_01.BMV","Min_g_01",0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.193)
	Bladex.AddAnmRStep(anm_name,0.279)
	Bladex.AddAnmRRelease(anm_name,0.608)
	Bladex.AddAnmRStep(anm_name,0.759)
	Bladex.AddAnmLStep(anm_name,0.000)



	anm_name="Min_g_07"
	Bladex.LoadSampledAnimation("../../Anm/Min_g_07.BMV","Min_g_07",0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.188)
	Bladex.AddAnmRStep(anm_name,0.353)
	Bladex.AddAnmRRelease(anm_name,0.591)
	Bladex.AddAnmRStep(anm_name,0.696)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.345)
	Bladex.AddAnmLStep(anm_name,0.617)



	anm_name="Min_g_08"
	Bladex.LoadSampledAnimation("../../Anm/Min_g_08.BMV","Min_g_08",0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.203)
	Bladex.AddAnmRStep(anm_name,0.269)
	Bladex.AddAnmRRelease(anm_name,0.519)
	Bladex.AddAnmRStep(anm_name,0.637)
	Bladex.AddAnmLStep(anm_name,0.000)



	anm_name="Min_g_12"
	Bladex.LoadSampledAnimation("../../Anm/Min_g_12.BMV","Min_g_12",0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.244)
	Bladex.AddAnmRStep(anm_name,0.334)
	Bladex.AddAnmRRelease(anm_name,0.663)
	Bladex.AddAnmRStep(anm_name,0.797)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.395)
	Bladex.AddAnmLStep(anm_name,0.579)




	anm_name="Min_g_31"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.147)
	Bladex.AddAnmRStep(anm_name,0.207)
	Bladex.AddAnmRRelease(anm_name,0.506)
	Bladex.AddAnmRStep(anm_name,0.626)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.236)
	Bladex.AddAnmLStep(anm_name,0.285)
	Bladex.AddAnmLRelease(anm_name,0.364)
	Bladex.AddAnmLStep(anm_name,0.459)
	Bladex.AddAnmLRelease(anm_name,0.727)
	Bladex.AddAnmLStep(anm_name,0.802)






	anm_name="Min_hurt_big"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.044)
	Bladex.AddAnmRStep(anm_name,0.211)
	Bladex.AddAnmRRelease(anm_name,0.889)
	Bladex.AddAnmRStep(anm_name,0.933)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.056)
	Bladex.AddAnmLStep(anm_name,0.122)
	Bladex.AddAnmLRelease(anm_name,0.211)
	Bladex.AddAnmLStep(anm_name,0.322)
	Bladex.AddAnmLRelease(anm_name,0.889)
	Bladex.AddAnmLStep(anm_name,0.967)



	anm_name="Min_hurt_lite"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.183)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.183)



########Muertes



	anm_name="Min_dth0"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)



	anm_name="Min_dth_n00"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.098)
	Bladex.AddAnmRStep(anm_name,0.191)
	Bladex.AddAnmRRelease(anm_name,0.362)
	Bladex.AddAnmRStep(anm_name,0.411)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.200)
	Bladex.AddAnmLStep(anm_name,0.258)



	anm_name="Min_dth_c1"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.048)
	Bladex.AddAnmRStep(anm_name,0.129)
	Bladex.AddAnmRRelease(anm_name,0.282)
	Bladex.AddAnmRStep(anm_name,0.366)
	Bladex.AddAnmRRelease(anm_name,0.569)
	Bladex.AddAnmRStep(anm_name,0.726)
	Bladex.AddAnmRRelease(anm_name,0.825)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.157)
	Bladex.AddAnmLStep(anm_name,0.226)
	Bladex.AddAnmLRelease(anm_name,0.462)
	Bladex.AddAnmLStep(anm_name,0.541)
	Bladex.AddAnmLRelease(anm_name,0.827)



	#
	# Slip
	#
	anm_name="Min_slip"
	Bladex.LoadSampledAnimation("../../Anm/Min_slip.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Min_slip_b"
	Bladex.LoadSampledAnimation("../../Anm/Min_slip_b.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Min_derrape"
	Bladex.LoadSampledAnimation("../../Anm/Min_derrape.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.04)
	Bladex.AddAnmRStep(anm_name,0.13)
	Bladex.AddAnmRRelease(anm_name,0.27)
	Bladex.AddAnmRStep(anm_name,0.44)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmLRelease(anm_name,0.09)
	Bladex.AddAnmLStep(anm_name,0.30)













####### OTROS

	anm_name="Min_eat"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)
