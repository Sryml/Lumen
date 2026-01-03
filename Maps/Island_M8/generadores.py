import math
import EnmGenRnd

#char.Position = -26315.4249668, -1223.90439316, -37016.8



Esp = 0


generadorT1 = EnmGenRnd.CreateEnemiesGenerator(6, 3,'../../Sounds/generador-agua.wav')
generadorT1.VirGenPos = -34500,  8500, -35000

generadorT1.AddPoint((-34500,  9500, -35000),("Gen1Lich_1", "Lich", "Maza2", 1, "", 0), "Lch_appears1",4)
generadorT1.AddPoint((-35000,  9500, -47000),("Gen1Lich_2", "Lich", "Hacha4", 1, "", 0), "Lch_appears1",5)
generadorT1.AddPoint((-42000,  9500, -41100),("Gen1Lich_3", "Lich", "Hacha4", 1, "Escudo2", 1), "Lch_appears1",5)
generadorT1.AddPoint((-42000,  9500, -35000),("Gen1Lich_4", "Lich", "Martillo", 1, "Escudo2", 1), "Lch_appears1",6)
generadorT1.AddPoint((-31000,  9500, -45000),("Gen1Lich_5", "Lich", "Hacha3", 1, "Escudo5", 1), "Lch_appears1",8)
generadorT1.AddPoint((-44000,  9500, -37100),("Gen1Lich_6", "Lich", "Martillo", 1, "Escudo1", 1), "Lch_appears1",9)
generadorT1.InitGenFunc=SaltaAguaGenActivate

generadorT1.NumDeaths = 4

generadorT1.NumDeaths = 5

generadorT1.Activate()
generadorT1.SonidoGen.Volume = 1.0
generadorT1.FinishGenFunc    = terminaGeneradorT1
Gen1Sec = Bladex.GetSector(-35000, 7000, -41000)
Gen1Sec.OnEnter = ActivateGen1
