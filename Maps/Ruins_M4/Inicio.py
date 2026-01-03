import Bladex
import AuxFuncs
import GameText
import Scorer
import GotoMapVars



######## Funcion: ReiniciaCamaraInicio(ent_name)

######## Funcion: UltimoTravelling()

######## Funcion: LanzaAnimacionInicio()

######## Funcion: MusicayTexto()

######## Funcion: Comienza()

AuxFuncs.SingleFrameFade()
Scorer.SetVisible(0)

Bladex.AddScheduledFunc(Bladex.GetTime(), Comienza, ())
