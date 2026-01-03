import Bladex
import EnmGenRnd
import AuxFuncs
import ReadGSFile
import Doors
import Button
import Sounds
import Breakings
import Actions
import EnemyTypes

######################
#     Particulas     #
######################



CreateArenilla()


Bladex.AddParticleGType("Tierra3","GenericParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	aux=(60-i)/60
	r=40
	g=30
	b=0
	a=255*(1.0-aux/2.0)
	size=60.0*(1.0-aux)
	Bladex.SetParticleGVal("Tierra3",i,r,g,b,a,size)

###################################################
#     Funciones complementarias del generador     #
###################################################



#######################
#     Generadores     #
#######################


# Magic Rod Enemy Generator################################
# Rod 18/1/2000, God save the luck! (I hope this works)

#activate Enemy Gemerator in Magic Rod Zone
		

generadorT1 = EnmGenRnd.CreateEnemiesGenerator(8, 2)

	
generadorT1.CallBak = CreaSkeletoDichoso

generadorT1.AddPoint((-46463, 200, 10252), ("M13Gen11Skl_1", "Skeleton", "Gladius"	, 0, "Escudo5", 1), "Skl_appears1")
generadorT1.AddPoint((-37493, 200,  2765), ("M13Gen11Skl_2", "Skeleton", "Gladius"	, 0, "Escudo5", 1), "Skl_appears1")
generadorT1.AddPoint((-28499, 200,  3456), ("M13Gen11Skl_3", "Skeleton", "Hacha5"	, 0, "Escudo5", 1), "Skl_appears1")
generadorT1.AddPoint((-20289, 200,  9696), ("M13Gen11Skl_4", "Skeleton", "Hacha5"	, 0, "Escudo5", 1), "Skl_appears1")
generadorT1.AddPoint((-14145, 200,  1131), ("M13Gen11Skl_5", "Skeleton", "Gladius"	, 0, "Escudo5", 1), "Skl_appears1")
generadorT1.AddPoint((- 7908, 200,  5029), ("M13Gen11Skl_6", "Skeleton", "Hacha5"	, 0, "Escudo5", 1), "Skl_appears1")
generadorT1.AddPoint((-27160, 200, 11200), ("M13Gen11Skl_7", "Skeleton", "Hacha5"	, 0, "Escudo5", 1), "Skl_appears1")
generadorT1.AddPoint((-24667, 200,  1918), ("M13Gen11Skl_8", "Skeleton", "Gladius"	, 0, "Escudo5", 1), "Skl_appears1")

generadorT1.InitGenFunc = SaltaTierraGen
#generadorT1.FinishGenFunc = Abrepta3
generadorT1.DifTime = 1.6
generadorT1.Activate()
generadorT1.OnEnd = ApareceElTipoDeLaLlave

RodEnemyGen1 = Bladex.GetSector(- 2000, -5000, 18000)
RodEnemyGen2 = Bladex.GetSector(-22000, -5000,  8000)


TempleEnemyGenerator = EnmGenRnd.CreateEnemiesGenerator(6, 2)

TempleEnemyGenerator.AddPoint((-13003, -1800, 43714), ("M13Gen11Lch_1", "Lich", "Martillo"	, 0, "Escudo5", 1), "Skl_appears1")
TempleEnemyGenerator.AddPoint((-38009, -1800, 44429), ("M13Gen11Lch_5", "Lich", "Martillo"	, 0, "Escudo5", 1), "Skl_appears1")
TempleEnemyGenerator.AddPoint((-37384, -1800, 40195), ("M13Gen11Lch_6", "Lich", "Martillo"	, 0, "Escudo5", 1), "Skl_appears1")
TempleEnemyGenerator.AddPoint((-17391,  -800, 27822), ("M13Gen11Lch_2", "Lich", "Martillo"	, 0, "Escudo5", 1), "Skl_appears1")
TempleEnemyGenerator.AddPoint((-26847,  -800, 29114), ("M13Gen11Lch_3", "Lich", "Hacha3"	, 0, "Escudo2", 1), "Skl_appears1")
TempleEnemyGenerator.AddPoint((-30842,  -800, 27946), ("M13Gen11Lch_4", "Lich", "Hacha3"	, 0, "Escudo2", 1), "Skl_appears1")

TempleEnemyGenerator.InitGenFunc = SaltaTierraGen
TempleEnemyGenerator.DifTime = 1.6
TempleEnemyGenerator.Activate()


TempleEnemyGenerator.OnEnd = ApareceElEskeletoDeLaOstia

InsideTempleZone = Bladex.GetSector(-25931.546808, -3224.7176561, 41237.498878)
InsideTempleZone.OnEnter = ActivateTempleEnemyGenerator

