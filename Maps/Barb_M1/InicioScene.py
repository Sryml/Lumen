import Bladex
import GameText
import Scorer
import AuxFuncs

AuxFuncs.SingleFrameFade()
Scorer.SetVisible(0)

cuervo1_sound=Bladex.CreateSound('../../Sounds/cuervo-graznido.wav', 'SonidoCuervo1')
cuervo1_sound.Volume=1.0
cuervo1_sound.MinDistance=3000
cuervo1_sound.MaxDistance=40000

crowinicio=Bladex.CreateEntity("CrowInicio1","Crw",-158880,110,-92840)
crowinicio.RotateRel(0,0,0,1,0,0,1.57)
crowinicio.Static = 1

crowinicio2=Bladex.CreateEntity("CrowInicio2","Crw",-95859,3777,-111372)
crowinicio2.RotateRel(0,0,0,1,0,0,1.57)
crowinicio2.Static = 1



#Bladex.LoadSampledAnimation("../../Anm/Crw_start_pic.BMV","Crw_start_pic",1,"Crw")
#Bladex.LoadSampledAnimation("../../Anm/Crw_start_fly.BMV","Crw_start_fly",1,"Crw")
#Bladex.LoadSampledAnimation("../../Anm/crw_pic.BMV","Crw_pic",1,"Crw")

import Actions
Actions.ToggleProfiling()
Actions.ToggleProfiling()
AuxFuncs.SingleFrameFade()
Scorer.SetVisible(0)
Bladex.AddScheduledFunc(Bladex.GetTime(),ParchePrecarga,(),"ParchePrecarga")
#Bladex.AddScheduledFunc(Bladex.GetTime(),BarbInicio,())