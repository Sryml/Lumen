import Bladex
import Enm_Def



def LoadDgkAnimationSet(ct_name):

	print "Loading Dal's animation sets..."

	#### Relax ####

	anm_name="Dgk_df_01"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.12)
	Bladex.AddAnmRStep(anm_name,0.42)

	anm_name="Dgk_df_02"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.15)
	Bladex.AddAnmLStep(anm_name,0.46)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.43)
	Bladex.AddAnmRStep(anm_name,0.62)


	anm_name="Dgk_g_m01"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmEvent("Dgk_g_m01","Diskcreate",0.222) #0.167)
	Bladex.AddAnmEvent("Dgk_g_m01","Diskthrow",0.555) #0.569)

	anm_name="Dgk_g_m02"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmEvent("Dgk_g_m02","StartBall",0.1)
	Bladex.AddAnmEvent("Dgk_g_m02","FireBall",0.65)


	anm_name="Dgk_g_tw5"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.32)
	Bladex.AddAnmRStep(anm_name,0.44)
	Bladex.AddAnmRRelease(anm_name,0.57)
	Bladex.AddAnmRStep(anm_name,0.73)
	Bladex.AddAnmEvent("Dgk_g_tw5","ThrowHeavyEvent",0.354)


	anm_name="Dgk_g_07_new"
	Bladex.LoadSampledAnimation("../../Anm/Dgk_g_07_new.BMV",anm_name,0,"DalGurak")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.091)
	Bladex.AddAnmRStep(anm_name,0.344)
	Bladex.AddAnmRRelease(anm_name,0.553)
	Bladex.AddAnmRStep(anm_name,0.823)
	Bladex.AddAnmLStep(anm_name,0.000)


	anm_name="Dgk_g_08_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_08_new.BMV",anm_name,0,"DalGurak")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.069)
	Bladex.AddAnmRStep(anm_name,0.367)
	Bladex.AddAnmRRelease(anm_name,0.577)
	Bladex.AddAnmRStep(anm_name,0.954)
	Bladex.AddAnmLStep(anm_name,0.000)


	anm_name="Dgk_g_02_new"
	Bladex.LoadSampledAnimation("../../Anm/Dgk_g_02_new.BMV",anm_name,0,"DalGurak")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.101)
	Bladex.AddAnmRStep(anm_name,0.336)
	Bladex.AddAnmRRelease(anm_name,0.610)
	Bladex.AddAnmRStep(anm_name,0.865)
	Bladex.AddAnmLStep(anm_name,0.000)


	anm_name="Dgk_g_01_7_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_01_7_new.BMV",anm_name,0,"DalGurak")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.081)
	Bladex.AddAnmRStep(anm_name,0.215)
	Bladex.AddAnmRRelease(anm_name,0.341)
	Bladex.AddAnmRStep(anm_name,0.526)
	Bladex.AddAnmRRelease(anm_name,0.704)
	Bladex.AddAnmRStep(anm_name,0.867)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.274)
	Bladex.AddAnmLStep(anm_name,0.481)


	anm_name="Dgk_g_22lowkata_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_22lowkata_new.BMV",anm_name,0,"DalGurak")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.162)
	Bladex.AddAnmRStep(anm_name,0.418)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.264)
	Bladex.AddAnmLStep(anm_name,0.972)


	anm_name="Dgk_g_21_6_s8new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_21_6_s8new.BMV",anm_name,0,"DalGurak")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.108)
	Bladex.AddAnmRStep(anm_name,0.186)
	Bladex.AddAnmRRelease(anm_name,0.369)
	Bladex.AddAnmRStep(anm_name,0.410)
	Bladex.AddAnmRRelease(anm_name,0.453)
	Bladex.AddAnmRStep(anm_name,0.557)
	Bladex.AddAnmRRelease(anm_name,0.731)
	Bladex.AddAnmRStep(anm_name,0.853)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.432)
	Bladex.AddAnmLStep(anm_name,0.532)


	anm_name="Dgk_g_19_bs1_new"
	Bladex.LoadSampledAnimation("../../Anm/Dgk_g_19_bs1_new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.081)
	Bladex.AddAnmRStep(anm_name,0.215)
	Bladex.AddAnmRRelease(anm_name,0.341)
	Bladex.AddAnmRStep(anm_name,0.526)
	Bladex.AddAnmRRelease(anm_name,0.704)
	Bladex.AddAnmRStep(anm_name,0.867)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.274)
	Bladex.AddAnmLStep(anm_name,0.481)

	anm_name="Dgk_g_b32kata_new"
	Bladex.LoadSampledAnimation("../../Anm/Dgk_g_b32kata_new.BMV",anm_name,0,"DalGurak")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.274)
	Bladex.AddAnmRStep(anm_name,0.502)
	Bladex.AddAnmRRelease(anm_name,0.597)
	Bladex.AddAnmRStep(anm_name,0.843)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.134)
	Bladex.AddAnmLStep(anm_name,0.200)
	Bladex.AddAnmLRelease(anm_name,0.368)
	Bladex.AddAnmLStep(anm_name,0.558)
	Bladex.AddAnmLRelease(anm_name,0.814)
	Bladex.AddAnmLStep(anm_name,0.962)


	anm_name="Dgk_g_29_3new"
	Bladex.LoadSampledAnimation("../../Anm/Dgk_g_29_3new.BMV",anm_name,0,"DalGurak")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.233)
	Bladex.AddAnmRStep(anm_name,0.305)
	Bladex.AddAnmRRelease(anm_name,0.363)
	Bladex.AddAnmRStep(anm_name,0.473)
	Bladex.AddAnmRRelease(anm_name,0.741)
	Bladex.AddAnmRStep(anm_name,0.899)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.116)
	Bladex.AddAnmLStep(anm_name,0.217)
	Bladex.AddAnmLRelease(anm_name,0.295)
	Bladex.AddAnmLStep(anm_name,0.350)



	anm_name="Dgk_g_d_l"
	Bladex.LoadSampledAnimation("../../Anm/Dgk_g_d_l.BMV",anm_name,0,"DalGurak")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.144)
	Bladex.AddAnmRStep(anm_name,0.540)
	Bladex.AddAnmRRelease(anm_name,0.736)
	Bladex.AddAnmRStep(anm_name,0.830)
	Bladex.AddAnmLStep(anm_name,0.132)
	Bladex.AddAnmLRelease(anm_name,0.433)
	Bladex.AddAnmLStep(anm_name,0.778)



	anm_name="Dgk_g_d_r"
	Bladex.LoadSampledAnimation("../../Anm/Dgk_g_d_r.BMV",anm_name,0,"DalGurak")
	Bladex.AddAnmRStep(anm_name,0.175)
	Bladex.AddAnmRRelease(anm_name,0.459)
	Bladex.AddAnmRStep(anm_name,0.879)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.233)
	Bladex.AddAnmLStep(anm_name,0.438)

	anm_name="Dgk_g_back"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_back.BMV",anm_name,0,"DalGurak")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.477)
	Bladex.AddAnmRStep(anm_name,0.767)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.131)
	Bladex.AddAnmLStep(anm_name,0.305)
	Bladex.AddAnmLRelease(anm_name,0.829)
	Bladex.AddAnmLStep(anm_name,1.000)




	anm_name="Dgk_g_magic"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_magic.BMV",anm_name,0,"DalGurak")
	Bladex.AddAnmRStep(anm_name,0.105)
	Bladex.AddAnmRRelease(anm_name,0.558)
	Bladex.AddAnmRStep(anm_name,0.762)
	Bladex.AddAnmRRelease(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.465)
	Bladex.AddAnmLStep(anm_name,0.545)
	Bladex.AddAnmEvent("Dgk_g_magic","LaunchTrail",0.595)


	anm_name="Dgk_g_magic2"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_magic2.BMV",anm_name,0,"DalGurak")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.161)
	Bladex.AddAnmRStep(anm_name,0.361)
	Bladex.AddAnmRRelease(anm_name,0.742)
	Bladex.AddAnmRStep(anm_name,0.913)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.188)
	Bladex.AddAnmLStep(anm_name,0.357)
	Bladex.AddAnmLRelease(anm_name,0.735)
	Bladex.AddAnmLStep(anm_name,0.921)
	Bladex.AddAnmEvent("Dgk_g_magic2","LaunchTrail",0.377)


	anm_name="Dgk_attack_b"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.118)
	Bladex.AddAnmRStep(anm_name,0.280)
	Bladex.AddAnmLRelease(anm_name,0.340)
	Bladex.AddAnmLStep(anm_name,0.521)
	Bladex.AddAnmRRelease(anm_name,0.611)
	Bladex.AddAnmRStep(anm_name,0.766)
	Bladex.AddAnmLRelease(anm_name,0.865)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)


	anm_name="Dgk_attack_b_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.118)
	Bladex.AddAnmRStep(anm_name,0.280)
	Bladex.AddAnmLRelease(anm_name,0.340)
	Bladex.AddAnmLStep(anm_name,0.521)
	Bladex.AddAnmRRelease(anm_name,0.611)
	Bladex.AddAnmRStep(anm_name,0.766)
	Bladex.AddAnmLRelease(anm_name,0.865)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)


	anm_name="Dgk_attack_f"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.240)
	Bladex.AddAnmRRelease(anm_name,0.308)
	Bladex.AddAnmRStep(anm_name,0.515)
	Bladex.AddAnmLRelease(anm_name,0.582)
	Bladex.AddAnmLStep(anm_name,0.716)
	Bladex.AddAnmRRelease(anm_name,0.810)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddAnmLRelease(anm_name,1)
	Bladex.AddStopTests(anm_name)


	anm_name="Dgk_attack_f_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.240)
	Bladex.AddAnmRRelease(anm_name,0.308)
	Bladex.AddAnmRStep(anm_name,0.515)
	Bladex.AddAnmLRelease(anm_name,0.582)
	Bladex.AddAnmLStep(anm_name,0.716)
	Bladex.AddAnmRRelease(anm_name,0.810)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddAnmLRelease(anm_name,1)
	Bladex.AddStopTests(anm_name)

	anm_name="Dgk_attack_l"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRStep(anm_name,0.208)
	Bladex.AddAnmLRelease(anm_name,0.286)
	Bladex.AddAnmLStep(anm_name,0.460)
	Bladex.AddAnmRRelease(anm_name,0.541)
	Bladex.AddAnmRStep(anm_name,0.708)
	Bladex.AddAnmLRelease(anm_name,0.795)
	Bladex.AddAnmLStep(anm_name,1.0)
	Bladex.AddAnmRRelease(anm_name,1)
	Bladex.AddStopTests(anm_name)


	anm_name="Dgk_attack_r"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.276)
	Bladex.AddAnmRRelease(anm_name,0.349)
	Bladex.AddAnmRStep(anm_name,0.520)
	Bladex.AddAnmLRelease(anm_name,0.613)
	Bladex.AddAnmLStep(anm_name,0.770)
	Bladex.AddAnmRRelease(anm_name,0.838)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddAnmLRelease(anm_name,1)
	Bladex.AddStopTests(anm_name)


	anm_name="Dgk_attack_l_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRStep(anm_name,0.208)
	Bladex.AddAnmLRelease(anm_name,0.286)
	Bladex.AddAnmLStep(anm_name,0.460)
	Bladex.AddAnmRRelease(anm_name,0.541)
	Bladex.AddAnmRStep(anm_name,0.708)
	Bladex.AddAnmLRelease(anm_name,0.795)
	Bladex.AddAnmLStep(anm_name,1.0)
	Bladex.AddAnmRRelease(anm_name,1)
	Bladex.AddStopTests(anm_name)


	anm_name="Dgk_attack_r_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.276)
	Bladex.AddAnmRRelease(anm_name,0.349)
	Bladex.AddAnmRStep(anm_name,0.520)
	Bladex.AddAnmLRelease(anm_name,0.613)
	Bladex.AddAnmLStep(anm_name,0.770)
	Bladex.AddAnmRRelease(anm_name,0.838)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddAnmLRelease(anm_name,1)
	Bladex.AddStopTests(anm_name)


	anm_name="Dgk_catch"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmEvent("Dgk_catch","PickupEvent",0.239)

	anm_name="Dgk_rlx_1h"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRStep(anm_name,0.0)

	anm_name="Dgk_rlx_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRStep(anm_name,0.0)

	anm_name="Dgk_rlx_1"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRStep(anm_name,0.0)



	anm_name="Dgk_dth0"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.036)
	Bladex.AddAnmLStep(anm_name,0.070)
	Bladex.AddAnmRRelease(anm_name,0.071)
	Bladex.AddAnmRStep(anm_name,0.102)
	Bladex.AddAnmLRelease(anm_name,0.103)
	Bladex.AddAnmLStep(anm_name,0.138)
	Bladex.AddAnmLRelease(anm_name,0.178)
	Bladex.AddAnmLStep(anm_name,0.208)
	Bladex.AddAnmLRelease(anm_name,0.436)
	Bladex.AddAnmLStep(anm_name,0.497)
	Bladex.AddAnmLRelease(anm_name,1)
	Bladex.AddAnmRRelease(anm_name,1)


	anm_name="Dgk_lifeup1"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.07)
	Bladex.AddAnmRStep(anm_name,0.255)
	Bladex.AddAnmRRelease(anm_name,0.715)
	Bladex.AddAnmRStep(anm_name,0.915)
	Bladex.AddAnmEvent(anm_name,"StartLifeUp",0.2)

	# by Sryml: start
	Bladex.LoadSampledAnimation("../../Anm/Dgk_hurt_back.BMV","Dgk_hurt_back",0)
	Bladex.LoadSampledAnimation("../../Anm/Dgk_hurt_big.BMV","Dgk_hurt_big",0)
	Bladex.LoadSampledAnimation("../../Anm/Dgk_hurt_chest.BMV","Dgk_hurt_chest",0)
	Bladex.LoadSampledAnimation("../../Anm/Dgk_hurt_l_arm.BMV","Dgk_hurt_l_arm",0)
	Bladex.LoadSampledAnimation("../../Anm/Dgk_hurt_l_leg.BMV","Dgk_hurt_l_leg",0)
	Bladex.LoadSampledAnimation("../../Anm/Dgk_hurt_lite.BMV","Dgk_hurt_lite",0)
	Bladex.LoadSampledAnimation("../../Anm/Dgk_hurt_r_arm.BMV","Dgk_hurt_r_arm",0)
	Bladex.LoadSampledAnimation("../../Anm/Dgk_hurt_r_leg.BMV","Dgk_hurt_r_leg",0)
	Bladex.LoadSampledAnimation("../../Anm/Dgk_powup.BMV","Dgk_powup",0)
	# by Sryml: end
