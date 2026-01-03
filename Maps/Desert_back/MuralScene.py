import Bladex
import Raster
import Reference
import AuxFuncs
import Sounds
import GameText
import Scorer
import Torchs

soundhitplayer=Sounds.CreateEntitySound('../../Sounds/Golpe-Piedra-Mediana.wav', 'SoundHitPlayer')
soundhitplayer.Volume=0.5
soundhitplayer.MinDistance=100000
soundhitplayer.MaxDistance=200000

soundhit2player=Sounds.CreateEntitySound('../../Sounds/Esfuerzo-Barb-Corto-2.wav', 'SoundHit2Player')
soundhit2player.Volume=0.5
soundhit2player.MinDistance=100000
soundhit2player.MaxDistance=200000

soundesfuerzoplayer=Sounds.CreateEntitySound('../../Sounds/Esfuerzo-Barb-Corto-1.wav', 'SoundEsfuerzoPlayer')
soundesfuerzoplayer.Volume=0.5
soundesfuerzoplayer.MinDistance=100000
soundesfuerzoplayer.MaxDistance=200000

soundhittorch=Sounds.CreateEntitySound('../../Sounds/Golpe-Madera-Mediana.wav', 'SoundHitTorch')
soundhittorch.Volume=0.5
soundhittorch.MinDistance=100000
soundhittorch.MaxDistance=200000


antini = Bladex.CreateEntity("AntorchaInicio","Antorcha",-41560.0605302, 7031.3666973, -118575.876983)
antini.Orientation = 0.805480003357, 0.201679393649, 0.312958061695, 0.4610689878
antini.Static=0
#Torchs.SetUsable("AntorchaInicio",3,3,15)
antini.FiresIntensity=[ 0 ]
#antini.Lights=[ (0.000000,0.031250,(255,196,128)) ]

#antini.Static = 0
#antini.FiresIntensity=[0]
#antini.Lights=[ (3.920125,0.031250,(86,169,167)) ]
antini.Lights=[ (1.000000,0.051250,(255,196,128)) ]










#def StopMuralScene(camera,frame):




Bladex.AddScheduledFunc(Bladex.GetTime(),ParchePrecarga,())
#Bladex.AddScheduledFunc(Bladex.GetTime()+1.0,LookMuralScene,())
