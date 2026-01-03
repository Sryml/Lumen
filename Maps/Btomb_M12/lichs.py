import math
import EnmGenRnd

	
Bladex.ReadAlphaBitMap("../../Data/Bubble.bmp","BubbleParticle")


CreateParticle(30,30,30)


Esp = 0
	

generadorT1 = EnmGenRnd.CreateEnemiesGenerator(6, 2)

generadorT1.AddPoint((345814.923666, 17500, -215537.911917),("BtombGen1Lich_1", "Lich", "Hacha3", 1, "Escudo5", 1), "Skl_appears1")
generadorT1.AddPoint((354341.721605, 17500, -214814.78778),("BtombGen1Lich_2", "Lich", "Hacha3", 1, "Escudo5", 1), "Skl_appears2")
generadorT1.AddPoint((356560.971299, 17500, -219859.539876),("BtombGen1Lich_3", "Lich", "Hacha3", 1, "Escudo5", 1), "Skl_appears1")
generadorT1.InitGenFunc=SaltaAguaGenActivate
generadorT1.VirGenPos = 0,0,0

generadorT1.CallBak = AsingaPropiedadesLich

generadorT1.Activate()

Gen1Sec = Bladex.GetSector(345833.476277, 15999.4985642, -222126.248763)
Gen1Sec.OnEnter = ActivateGen1