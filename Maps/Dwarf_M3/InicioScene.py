import AuxFuncs
import Sounds
import GameText
import Scorer
import AbreCam

AuxFuncs.SingleFrameFade()
Scorer.SetVisible(0)

#enano-muerte-2.wav
#enano-herida1.wav


CAIDASPIEDRAS2=Sounds.CreateEntitySound('../../Sounds/CAIDAS-PIEDRAS-2.wav', 'Soundtevantarse')
CAIDASPIEDRAS2.Volume=1.0
CAIDASPIEDRAS2.MinDistance=10000
CAIDASPIEDRAS2.MaxDistance=20000

soundlevantarse=Sounds.CreateEntitySound('../../Sounds/esfuerzo-barb-largo.wav', 'SoundLevantarse')
soundlevantarse.Volume=1.0
soundlevantarse.MinDistance=10000
soundlevantarse.MaxDistance=20000

soundburr=Sounds.CreateEntitySound('../../Sounds/enano-herida1.wav', 'SoundBurr')
soundburr.Volume=1.0
soundburr.MinDistance=10000
soundburr.MaxDistance=20000

soundclean=Sounds.CreateEntitySound('../../Sounds/Movsuti2man.wav', 'SoundClean')
soundclean.Volume=1.0
soundclean.MinDistance=10000
soundclean.MaxDistance=20000

#soundhitplayer=Sounds.CreateEntitySound('../../Sounds/golpe-roca-1.wav', 'SoundHitPlayer')
soundhitplayer=Sounds.CreateEntitySound('../../Sounds/caida-mano.wav', 'SoundHitPlayer')
soundhitplayer.Volume=0.7
soundhitplayer.MinDistance=10000
soundhitplayer.MaxDistance=20000

soundhit2player=Sounds.CreateEntitySound('../../Sounds/enano-golpe2.wav', 'SoundHitPlayer')
soundhit2player.Volume=0.7
soundhit2player.MinDistance=10000
soundhit2player.MaxDistance=20000

soundhit3player=Sounds.CreateEntitySound('../../Sounds/enano-golpe2.wav', 'SoundHitPlayer')
soundhit3player.Volume=0.7
soundhit3player.MinDistance=10000
soundhit3player.MaxDistance=20000

soundavalanche=Sounds.CreateEntitySound('../../Sounds/impact-watersplash.wav', 'Avalancha')
soundavalanche.Volume=1
soundavalanche.MinDistance=10000
soundavalanche.MaxDistance=20000

weaponini = Bladex.GetEntity(char.InvRight)
shieldini = Bladex.GetEntity(char.InvLeft)
"""
weaponini2 = Bladex.CreateEntity("ArmaInicio",weaponini.Kind,0,0,0)
weaponini2.Static = 0
shieldini2 = Bladex.CreateEntity("EscudoInicio",shieldini.Kind,0,0,0)
shieldini2.Static = 0
"""
o=Bladex.CreateEntity("Stone0","Piedra_09",57963.847115,-4915.957098,-106575.387082)
o=Bladex.CreateEntity("Stone1","Piedra_09",60032.455646,-732.030206,-109345.212112)
o=Bladex.CreateEntity("Stone2","Piedra_01",56765.193238,-72.321999,-108475.494438)
o=Bladex.CreateEntity("Stone3","Piedra_09",53506.165855,-8770.481444,-102107.821394)
o=Bladex.CreateEntity("Stone4","Piedra_01",57908.679014,-1825.742886,-105875.452629)
o=Bladex.CreateEntity("Stone5","Piedra_01",57686.910795,-1224.010416,-106959.183863)
o=Bladex.CreateEntity("Stone6","Piedra_01",54280.582824,-4287.980518,-104983.516886)
o=Bladex.CreateEntity("Stone7","Piedra_01",56194.568641,-3264.709008,-106113.414490)
o=Bladex.CreateEntity("Stone8","Piedra_01",54729.107530,-10.200729,-109043.743072)
o=Bladex.CreateEntity("Stone9","Piedra_01",53617.592992,-919.598205,-110386.819424)


Launched = 0



"""
AbreCam.PTS =   [((146414.018398, 1459.1389425, -100339.301085), (146200.36749, 1763.78871955, -100861.004957), 0.1),
		 ((132925.18676, 7605.57806919, -121679.081488), (128619.720564, 8718.50247968, -121000.810616),  2),
		 ((107111.95343, 7360.49688027, -120512.869295), (105344.16801, 8475.82588629, -124507.140761),   2),
		 ((98569.450521, 7381.97205053, -138017.114617), (94311.6493059, 8495.18722464, -138954.20962),   2),
		 ((73978.5976694, 5967.93164242, -130267.028172), (72702.1403773, 7080.81752729, -126099.723034), 2),
		 ((68964.4865008, 7301.44577413, -120177.942821), (64643.4255363, 6444.77825199, -119287.385204), 2),
		 ((54593.7667752, 7519.95190412, -117965.846502), (54232.1126615, 5892.05341749, -116801.850326), 2)]

AbreCam.PTS =   [((73978.5976694, 5967.93164242, -130267.028172), (72702.1403773, 7080.81752729, -126099.723034), 0.01),
		 ((68964.4865008, 7301.44577413, -120177.942821), (64643.4255363, 6444.77825199, -119287.385204), 3),
		 ((54593.7667752, 7519.95190412, -117965.846502), (54232.1126615, 5892.05341749, -116801.850326), 3)]
"""






AbreCam.PTS =   [((146414.018398, 1459.1389425, -100339.301085), (146200.36749, 1763.78871955, -100861.004957), 0.1),
		 ((132925.18676, 7605.57806919, -121679.081488), (128619.720564, 8718.50247968, -121000.810616),  2),
		 ((107111.95343, 7360.49688027, -120512.869295), (105344.16801, 8475.82588629, -124507.140761),   2),
		 ((98569.450521, 7381.97205053, -138017.114617), (94311.6493059, 8495.18722464, -138954.20962),   2),
		 ((73978.5976694, 5967.93164242, -130267.028172), (72702.1403773, 7080.81752729, -126099.723034), 2),
		 ((68964.4865008, 7301.44577413, -120177.942821), (64643.4255363, 6444.77825199, -119287.385204), 2),
		 ((54593.7667752, 7519.95190412, -117965.846502), (54232.1126615, 5892.05341749, -116801.850326), 2)]


AbreCam.LastTime = 0.01
Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, RunAbreCam,())

ReverStep = [0,0,0]

ReverStep[0]=Sounds.CreateEntitySound('../../Sounds/paso-piedra-reverb-1.wav', 'ReverStep0')
ReverStep[0].Volume=1.0
ReverStep[0].MinDistance=10000
ReverStep[0].MaxDistance=20000

ReverStep[1]=Sounds.CreateEntitySound('../../Sounds/paso-piedra-reverb-2.wav', 'ReverStep1')
ReverStep[1].Volume=1.0
ReverStep[1].MinDistance=10000
ReverStep[1].MaxDistance=20000

ReverStep[2]=Sounds.CreateEntitySound('../../Sounds/paso-piedra-reverb-3.wav', 'ReverStep2')
ReverStep[2].Volume=1.0
ReverStep[2].MinDistance=10000
ReverStep[2].MaxDistance=20000