import GameText
import Bladex
import Scorer
import Sounds
import AuxFuncs

AuxFuncs.SingleFrameFade()
Scorer.SetVisible(0)

soundesfuerzo = 0

SelectSoundEsfuerzo(char.Kind)

soundhitplayer=Sounds.CreateEntitySound('../../Sounds/M-caida-nieve1.wav', 'SoundHitPlayer')
soundhitplayer.Volume=0.5
soundhitplayer.MinDistance=10000
soundhitplayer.MaxDistance=20000

char = Bladex.GetEntity("Player1")


Bladex.AddScheduledFunc(Bladex.GetTime(), Musicaytexto, ())
