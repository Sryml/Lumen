import GameText
import dust
import Scorer
import AuxFuncs


AuxFuncs.SingleFrameFade()
Scorer.SetVisible(0)
Bladex.AddScheduledFunc(Bladex.GetTime(),PreStartInicio,(),"PreStartInicio")
