import Bladex
import Enm_Def





def LoadPrsAnimationSet(ct_name):

	print "Loading the Prisioner animation sets..."


	Bladex.LoadSampledAnimation("../../Anm/Prs_rlx_01.BMV","Prs_rlx_01",1)
	Bladex.AddAnmRStep("Prs_rlx_01",0.0)
	Bladex.AddAnmLStep("Prs_rlx_01",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Prs_rlx_02.BMV","Prs_rlx",1)
	Bladex.AddAnmRStep("Prs_rlx",0.0)
	Bladex.AddAnmLStep("Prs_rlx",0.0)


	Bladex.LoadSampledAnimation("../../Anm/Prs_agony01.BMV","Prs_agony01",1)
	Bladex.AddAnmRStep("Prs_agony01",0.0)
	Bladex.AddAnmLStep("Prs_agony01",0.0)


	Bladex.LoadSampledAnimation("../../Anm/Prs_agony02.BMV","Prs_agony02",1)
	Bladex.AddAnmRStep("Prs_agony02",0.0)
	Bladex.AddAnmLStep("Prs_agony02",0.0)


	Bladex.LoadSampledAnimation("../../Anm/Prs_dth.BMV","Prs_dth0",1)
	Bladex.AddAnmRStep("Prs_dth0",0.0)
	Bladex.AddAnmLStep("Prs_dth0",0.0)
