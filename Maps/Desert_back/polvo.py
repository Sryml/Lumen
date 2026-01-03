#------------------------------------------------------------------#
#                        Pa' que aprenda!                          #
#------------------------------------------------------------------#
import dust
import Sounds

dust.intensidad = 140                          	 	# pps
dust.SetPolvinColor(223,202,130)                	# snow winds

WindSound = Sounds.CreateEntitySound("../../Sounds/M-rafaga-viento.wav", "CasualWind")

Efepolvo = dust.WindFX(-29800, 0, -139000)      	# sector as params
Efepolvo.SetSound(WindSound)                    	# coolsound
Efepolvo.SetGenerationPoint(-25500, 8800, -136500)
Efepolvo.SetWindVector(-4000,-5000)               	# This way is the win
Efepolvo.Variance = 0                           	# 3 of 1 time

#delante de la gruta
Efepolvo2 = dust.WindFX(-3000, 0, -118000)
Efepolvo2.SetSound(WindSound)
Efepolvo2.SetGenerationPoint(-8000, 6000, -113500)
Efepolvo2.SetWindVector(5000,-2000)
Efepolvo2.Variance = 0