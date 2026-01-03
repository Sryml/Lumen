import Bladex
import DMusic
import Language

language = Language.CheckFallback()

locspath="../../Sounds/"+language+"/"
musicspath="../../Sounds/"



### Locuciones

#Bladex.AddMusicEventMP3(nombre, fichero, tiempo_fadein, tiempo_fadeout, volumen, prioridad, ambiente, iNext)
Bladex.AddMusicEventMP3  ("musica_inicio",           locspath+"files07.MP3",          0.1, 1.0, 1.0, 10000, 0, 0)
Bladex.AddMusicEventMP3  ("musica_invocacion",       locspath+"loc-libromaldito.mp3", 0.1, 1.0, 1.0, 10000, 0, 0)
Bladex.AddMusicEventMP3  ("espiritu_libre",          locspath+"ruins-libre.mp3",      0.1, 1.0, 1.0, 10000, 0, 0)
Bladex.AddMusicEventMP3  ("puerta_laberinto_y_pozo", musicspath+"CORO5.mp3",          0.1, 1.0, 1.0, 10000, 0, 0)


### Ambientes

Bladex.AddMusicEventADPCM("mausoleo",                musicspath+"ATMOSFERA3.wav",     1.0, 1.0, 1.0, 0, 1, -1)
Bladex.AddMusicEventADPCM("exterior_despues",        musicspath+"ATMOSFERA4.wav",     1.0, 1.0, 1.0, 0, 1, -1)
Bladex.AddMusicEventADPCM("exterior_antes",          musicspath+"ATMOSFERA5.wav",     1.0, 1.0, 1.0, 0, 1, -1)
Bladex.AddMusicEventADPCM("laberinto_e_interiores",  musicspath+"ATMOSFERA6.wav",     1.0, 1.0, 1.0, 0, 1, -1)
Bladex.AddMusicEventADPCM("catacumbas",              musicspath+"ATMOSFERA7.wav",     1.0, 1.0, 1.0, 0, 1, -1)
Bladex.AddMusicEventADPCM("templo_final",            musicspath+"ATMOSFERA8.wav",     1.0, 1.0, 1.0, 0, 1, -1)
Bladex.AddMusicEventMP3  ("emptyloquesea",           "",                              0.1, 0.1, 1.0, 0, 1, 0 )


### Combates

DMusic.AddCombatMusic    ("Beej11",        musicspath+"COMBATE2.wav", 126, 0)
DMusic.AddCombatMusic    ("Beej12",        musicspath+"COMBATE2.wav", 126, 0)
DMusic.AddCombatMusic    ("OrkF3",         musicspath+"COMBATE2.wav", 126, 0)
Bladex.AddMusicEventWAV  ("combate_final", musicspath+"COMBATE3.wav", 1.0, 1.0, 1.0, 0, 1, -1)  # Esta en particular me interesa manejarla a pelo como musica ambiente
