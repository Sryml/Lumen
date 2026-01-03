


import math
import EnmGenRnd

#char.Position = -26315.4249668, -1223.90439316, -37016.8



Bladex.ReadAlphaBitMap("../../Data/Bubble.bmp","BubbleParticle")


CreateParticle(50,60,30,50)


Esp = 0


generadorT1Agua = EnmGenRnd.CreateEnemiesGenerator(2, 2,'../../Sounds/generador-agua.wav')

generadorT1Agua.AddPoint((-9500,8000,-17000),("TombGen1LichX", "Skeleton", "Hacha3", 1, "Escudo5", 1), "Skl_appears1")
generadorT1Agua.AddPoint((-9500,8000,2500),("TombGen2LichX", "Skeleton", "Hacha3", 1, "Escudo5", 1), "Skl_appears1")
generadorT1Agua.InitGenFunc=SaltaAguaGenActivate
generadorT1Agua.VirGenPos = -9500,8000,-17000

generadorT1Agua.Activate()

Gen1SecAgua = Bladex.GetSector(-9500,5000,-3500)
Gen1SecAgua.OnEnter = ActivateGen1Agua

####################

generadorT2Agua = EnmGenRnd.CreateEnemiesGenerator(2, 2,'../../Sounds/generador-agua.wav')

generadorT2Agua.AddPoint((7250,8000,-25000),("TombGen1LichXXL", "Skeleton", "Hacha3", 1, "Escudo5", 1), "Skl_appears1")
generadorT2Agua.AddPoint((-10000,8000,-24500),("TombGen2LichXXL", "Skeleton", "Hacha3", 1, "Escudo5", 1), "Skl_appears1")
generadorT2Agua.InitGenFunc=SaltaAguaGenActivate
generadorT2Agua.VirGenPos = 7250,8000,-25000

generadorT2Agua.Activate()

Gen2SecAgua = Bladex.GetSector(-6500,5000,-25000)
Gen2SecAgua.OnEnter = ActivateGen2Agua