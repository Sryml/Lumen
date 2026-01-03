import Bladex




### Animaciones ###


def Amz():
	Bladex.LoadSampledAnimation("../../Anm/Amz_darkbook.bmv","Amz_darkbook",0,"Amazon_L")
	Bladex.AddBipedAction("Amz","darkbook","Amz_darkbook",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Amz_ruinas_final.bmv","Amz_ruinas_final",0,"Amazon_L")
	Bladex.AddBipedAction("Amz","ruinas_final","Amz_ruinas_final",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Amz_start.bmv","Amz_start",0,"Amazon_L")
	Bladex.AddBipedAction("Amz","start","Amz_start",0.0,1.0,0)
	Bladex.LoadSampledAnimation("../../Anm/Amz_push_sarcofa.bmv","Amz_push_sarcofa",0,"Amazon_L")
	Bladex.AddBipedAction("Amz","push_sarcofa","Amz_push_sarcofa",0.0,1.0,0)
