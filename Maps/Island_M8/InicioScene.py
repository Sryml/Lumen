import AuxFuncs
import GameText
import Scorer

crowinicio2=Bladex.CreateEntity("CrowInicio2","Crw",-58654,-20381,-2515)
crowinicio2.RotateRel(0,0,0,1,0,0,1.57)
crowinicio2.Static = 1

AuxFuncs.SingleFrameFade()
Scorer.SetVisible(0)


Bladex.AddScheduledFunc(Bladex.GetTime(), ParchePrecarga,())
#Bladex.AddScheduledFunc(Bladex.GetTime(), StartInicio,())

