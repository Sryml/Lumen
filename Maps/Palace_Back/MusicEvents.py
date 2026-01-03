import Bladex
import Language

language = Language.CheckFallback()

locspath="../../Sounds/"+language+"/"
musicspath="../../Sounds/"



Bladex.AddMusicEventMP3("espadacontodastablillas",     locspath+"espadacontt.mp3",        0.1, 1.0, 1.0, 10000.0, 0, 0 )
Bladex.AddMusicEventMP3("espadasinalgunatablilla",     locspath+"espadasinat.mp3",        0.1, 1.0, 1.0, 10000.0, 0, 0 )
Bladex.AddMusicEventMP3("espadasinningunatablilla",    locspath+"espadasinnt.mp3",        0.1, 1.0, 1.0, 10000.0, 0, 0 )
Bladex.AddMusicEventMP3("solopoderconrestotablillas",  locspath+"solopoderrt.mp3",        0.1, 1.0, 1.0, 10000.0, 0, 0 )
Bladex.AddMusicEventMP3("solotablillas",               musicspath+"solotablillas.mp3",    0.1, 1.0, 1.0, 10000.0, 0, 0 )


Bladex.AddMusicEventMP3( "miserere",                   musicspath+"CORO3.mp3",            1.0, 1.0, 1.0, 0,       1, -1)
