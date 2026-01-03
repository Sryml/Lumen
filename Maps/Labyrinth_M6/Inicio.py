import Bladex
import AuxFuncs
import GameText



######## Funcion: StopCameraInicio(Camera,Frame)

######## Funcion: ChangeCameraInicio(Camera,Frame)

######## Funcion: MusicaytextoInicio()

######## Funcion: Aterrizaje()

######## Funcion: ContStartInicio()

######## Funcion: StartInicio()

AuxFuncs.SingleFrameFade()
Scorer.SetVisible(0)

Bladex.AddScheduledFunc(Bladex.GetTime(), StartInicio,())
