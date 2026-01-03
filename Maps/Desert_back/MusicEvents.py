import Bladex
import DMusic
import string
import AuxFuncs


language = Language.CheckFallback()

Bladex.AddMusicEventMP3("tablilla","../../Sounds/"+language+"/desierto-tablilla.mp3", 0.1, 1.0, 1.0, 1000, 0, 0 )



###SORPRESAS

Bladex.AddMusicEventWAV("sorpresa6","../../Sounds/SORPRESA6.wav",        1.0, 1.0, 1.0, 500, 0, 0 )

Bladex.AddMusicEventMP3("atm12","../../Sounds/ATMOSFERA12.mp3",          0.1, 0.1, 1.0, 1, 0, 0 )

Bladex.AddMusicEventWAV("incomb4","../../Sounds/INICIOCOMBATE4.wav",     0.1, 0.1, 1.0, 200, 0, 0 )

Bladex.AddMusicEventWAV("comb2","../../Sounds/COMBATE2.wav",        1.0, 1.0, 1.0, 500, 0, -1 )



###VACIO
Bladex.AddMusicEventMP3( "empty",  "", 2.0, 3.0, 1.0, 600, 1, 1 )
Bladex.AddMusicEventMP3( "emptyloquesea",  "", 2.0, 3.0, 1.0, 600, 1, 1 )



###MUSICAS
Bladex.AddMusicEventWAV("acomblh","../../Sounds/combate-ligth.wav", 0.1, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventWAV("combate6","../../Sounds/COMBATE6.wav",     1.0, 1.0, 1.0, 1  , 1, -1 )

Bladex.AddMusicEventWAV( "atm1","../../Sounds/ATMOSFERA1.wav"   , 1.0, 1.0, 1.0, 1  , 1, -1 )


Bladex.AddMusicEventWAV( "atm7","../../Sounds/ATMOSFERA7.wav"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventWAV( "atm19","../../Sounds/ATMOSFERA19.wav"   , 1.0, 0.3, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventWAV( "atm18","../../Sounds/ATMOSFERA18.wav"   , 1.0, 0.3, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventWAV( "atm24","../../Sounds/ATMOSFERA24.wav"   , 1.0, 1.0, 1.0, 1  , 1, -1 )


#Bladex.ExeMusicEvent( Bladex.GetMusicEvent("atm1") )