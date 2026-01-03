import Bladex
import DMusic
import Language

language = Language.CheckFallback()
#### ESCENAS

Bladex.AddMusicEventMP3("abismo-carga","../../Sounds/"+language+"/abismo-carga.mp3",       0.1, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventMP3("despelote","../../Sounds/esqueletos-despelote.mp3",  0.1, 0.1, 0.3, 500, 0, 0 )
Bladex.AddMusicEventMP3("moulinex","../../Sounds/viejete.mp3",                0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventMP3("viejeteblabla","../../Sounds/"+language+"/quevieneelviejete.mp3", 2.0, 0.1, 1.0, 499, 0, 0 )


## GOLPES DE EFECTO

Bladex.AddMusicEventWAV("sorpresa-1","../../Sounds/SORPRESA1.wav",    0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-1a","../../Sounds/SORPRESA1a.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-1b","../../Sounds/SORPRESA1b.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-3","../../Sounds/SORPRESA3.wav",    0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-4","../../Sounds/SORPRESA4.wav",    0.1, 0.1, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-5","../../Sounds/SORPRESA5.wav",    0.1, 0.1, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-6","../../Sounds/SORPRESA6.wav",    0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-7","../../Sounds/SORPRESA7.wav",    0.1, 0.1, 1.0, 190, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-8","../../Sounds/SORPRESA8.wav",    0.1, 1.0, 1.0, 190, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-12","../../Sounds/SORPRESA12.wav",  0.1, 1.0, 1.0, 190, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-13","../../Sounds/SOPRESA13.wav",   0.0, 0.0, 1.0, 190, 0, 0 )
Bladex.AddMusicEventMP3("Coro1","../../Sounds/CORO1.mp3",             0.5, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventMP3("Coro3","../../Sounds/final-miserere.mp3",    0.0, 0.1, 1.0, 200, 0, 0 )
Bladex.AddMusicEventMP3("Coro5","../../Sounds/CORO5.mp3",             0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventMP3("Coro6","../../Sounds/CORO6.mp3",             0.1, 0.1, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicio1","../../Sounds/INICIOCOMBATE1.wav",  0.1, 0.1, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicio2","../../Sounds/INICIOCOMBATE2.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicio3","../../Sounds/INICIOCOMBATE3.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicio4","../../Sounds/INICIOCOMBATE4.wav",  0.1, 0.1, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicio5","../../Sounds/INICIOCOMBATE5.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicio6","../../Sounds/INICIOCOMBATE6.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicio7","../../Sounds/INICIOCOMBATE7.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicio23","../../Sounds/INICIO23.wav",       0.1, 0.1, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicioatm20","../../Sounds/INICIO-ATMOSFERA20.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("coro2-2","../../Sounds/CORO2.2.mp3",         5.0, 0.1, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("1Combate1","../../Sounds/COMBATE1.wav",      0.1, 0.1, 1.0, 200, 0, 2 )
Bladex.AddMusicEventMP3("inicioatm11","../../Sounds/ATMOSFERA11.mp3", 0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventMP3("atm12mp3","../../Sounds/ATMOSFERA12.mp3",    0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventMP3("atm9mp3","../../Sounds/ATMOSFERA9.mp3",      0.1, 1.0, 1.0, 200, 0, 0 )

## ATMOSFERAS

Bladex.AddMusicEventWAV("Atmosfera1","../../Sounds/ATMOSFERA1.wav",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm1MP3","../../Sounds/ATMOSFERA1.mp3",      0.0, 0.0, 0.5, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Atmosfera2","../../Sounds/ATMOSFERA2.wav",   3.0, 0.1, 0.7, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm2MP3","../../Sounds/ATMOSFERA2.mp3",      2.0, 3.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Atmosfera3","../../Sounds/ATMOSFERA3.wav",   0.1, 0.5, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Atmosfera4","../../Sounds/ATMOSFERA4.wav",   0.1, 0.5, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Atm4temp","../../Sounds/ATMOSFERA4.wav",     0.1, 1.0, 1.0, 0.0, 1, 0 )
Bladex.AddMusicEventWAV("Atmosfera5","../../Sounds/ATMOSFERA5.wav",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm5mp3","../../Sounds/ATMOSFERA5.mp3",      0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Atmosfera6","../../Sounds/ATMOSFERA6.wav",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm6mp3","../../Sounds/ATMOSFERA6.mp3",      0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Atmosfera7","../../Sounds/ATMOSFERA7.wav",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm7mp3","../../Sounds/ATMOSFERA7.mp3",      0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Atmosfera8","../../Sounds/ATMOSFERA8.wav",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Atmosfera8b","../../Sounds/ATMOSFERA8.wav",  0.1, 0.1, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm8mp3","../../Sounds/ATMOSFERA8.mp3",      0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Atmosfera10","../../Sounds/ATMOSFERA10.wav", 0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera11","../../Sounds/ATMOSFERA11.mp3", 2.0, 1.0, 0.5, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm11prelude","../../Sounds/ATMOSFERA11.mp3",3.0, 1.0, 0.5, 0.0, 1,  0 )
Bladex.AddMusicEventWAV("Atmosfera18","../../Sounds/ATMOSFERA18.wav", 0.5, 0.5, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm18MP3","../../Sounds/ATMOSFERA18.mp3",    2.0, 1.0, 0.5, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Atmosfera19","../../Sounds/ATMOSFERA19.wav", 0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm19MP3","../../Sounds/ATMOSFERA19.mp3",    2.0, 1.0, 0.5, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Atmosfera20","../../Sounds/ATMOSFERA20.wav", 0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Atmosfera21","../../Sounds/ATMOSFERA21.wav", 0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Atmosfera22","../../Sounds/ATMOSFERA22.wav", 0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Atmosfera23","../../Sounds/ATMOSFERA23.wav", 0.1, 0.5, 0.7, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Atmosfera24","../../Sounds/ATMOSFERA24.wav", 0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm20MP3","../../Sounds/ATMOSFERA20.mp3",    2.0, 1.0, 0.5, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("inicio2atm20","../../Sounds/INICIO-ATMOSFERA20.wav",2.0, 1.0, 0.5, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("inicio2atm20b","../../Sounds/INICIO-ATMOSFERA20.wav",2.0, 1.0, 0.5, 0.0, 1, 0 )
Bladex.AddMusicEventWAV("Atmosfera20a","../../Sounds/ATMOSFERA20A.wav",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combate1","../../Sounds/COMBATE1.wav",           0.0, 3.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combate2","../../Sounds/COMBATE2.wav",           0.1, 2.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combate3","../../Sounds/COMBATE3.wav",           0.1, 5.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combate3b","../../Sounds/COMBATE3.wav",          0.1, 0.1, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combate4","../../Sounds/COMBATE4.wav",           0.1, 0.1, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combate6","../../Sounds/COMBATE6.wav",           0.1, 0.1, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combatelight","../../Sounds/combate-ligth.wav",  1.0, 6.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combatehard","../../Sounds/combate-hard.wav",    1.0, 2.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("atmsorpresa8","../../Sounds/SORPRESA8.wav",      0.1, 0.1, 1.0, 0.0, 1, 0 )
Bladex.AddMusicEventWAV("Kaos","../../Sounds/COMBATE-KAOS.wav",           3.0, 1.0, 1.0, 0.0, 1, -1 )


Bladex.AddMusicEventMP3("atmemptyloquesea", "",                          2.0, 0.5, 1.0, 0.0, 1, -1 )



## VACIO

Bladex.AddMusicEventMP3("emptyloquesea", "", 2.0, 3.0, 1.0, 300, 0, 0)
