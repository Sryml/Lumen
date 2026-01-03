import GameText
import Raster
import Scorer
import AuxFuncs

AuxFuncs.SingleFrameFade()
Scorer.SetVisible(0)

initial_time = 0
alpha = 1.0

FADE = 3.2
BLACK = 2.0

#char.Position =   325973.1,  -6124.8,        83.29
Bladex.AddScheduledFunc(Bladex.GetTime(),GurakInicio,())

