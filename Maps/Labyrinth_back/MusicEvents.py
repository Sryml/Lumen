import Bladex
from Language import Current

language = Language.CheckFallback()

locspath="../../Sounds/"+language+"/"
musicspath="../../Sounds/"



### Locuciones

Bladex.AddMusicEventMP3  ( "musica_tablilla",  locspath+"laberintotablilla.mp3", 0.1, 1.0, 1.0, 10000, 0, 0 )


### Ambientes y musicas sin voz para escenas

Bladex.AddMusicEventADPCM( "alcantytabvue",    musicspath+"ATMOSFERA7.wav",      1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventADPCM( "musicatablida",    musicspath+"ATMOSFERA3.wav",      1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventADPCM( "musicatrampatabl", musicspath+"COMBATE2.wav",        1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventADPCM( "musica1anillo",    musicspath+"ATMOSFERA18.wav",     1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventADPCM( "musica2anillo",    musicspath+"ATMOSFERA4.wav",      1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventADPCM( "entradatrampa",    musicspath+"INICIOCOMBATE5.wav",  0.1, 1.0, 1.0, 100,   0, 0 )
Bladex.AddMusicEventADPCM( "entradaalcant",    musicspath+"INICIOCOMBATE33.wav", 0.1, 1.0, 1.0, 100,   0, 0 )
Bladex.AddMusicEventADPCM( "musicaapchaos",    musicspath+"ATMOSFERA11.wav",     0.1, 1.0, 1.0, 0,     1, 0 )
