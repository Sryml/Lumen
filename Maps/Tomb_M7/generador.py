import Bladex
import EnmGenRnd
import B3DLib
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


generadorT1x = EnmGenRnd.CreateEnemiesGenerator(7, 3)
generadorT1x.VirGenPos = 71058.5, 6700, 20517.2
generadorT1x.CallBak = acAreafuncT1x
generadorT1x.AddPoint((71058.5, 6700, 20517.2),("tombaGen11Skl", "Skeleton", "Espadaelfica", 0, "Escudo2", 1), "Skl_appears1",6)
generadorT1x.AddPoint((57449.1, 6700, 25138.7),("tombaGen12Skl", "Skeleton", "Espadaelfica", 0, "Escudo2", 1), "Skl_appears1",7)
generadorT1x.AddPoint((65742.2, 6700, 30462.8),("tombaGen13Skl", "Skeleton", "Hacha4", 0, "Escudo1", 1), "Skl_appears1",8)
generadorT1x.AddPoint((67000.2, 6700, 20750.0),("tombaGen14Skl", "Skeleton", "Hacha4", 0, "Escudo1", 1), "Skl_appears1",8)
generadorT1x.AddPoint((62500.2, 6700, 23500.8),("tombaGen15Skl", "Skeleton", "Hacha4", 0, "Escudo1", 1), "Skl_appears1",8)
generadorT1x.AddPoint((72000.2, 6700, 23000.8),("tombaGen16Skl", "Skeleton", "Hacha4", 0, "Escudo1", 1), "Skl_appears1",8)
generadorT1x.AddPoint((57500.2, 6700, 26000.8),("tombaGen17Skl", "Skeleton", "Hacha4", 0, "Escudo1", 1), "Skl_appears1",8)

generadorT1x.InitGenFunc=SaltaTierraGen
generadorT1x.Activate()

############# GENERADOR 2 ######################





generadorT2 = EnmGenRnd.CreateEnemiesGenerator(6, 3)
generadorT2.VirGenPos = 30214.4, 1800, 20525.6
generadorT2.CallBak = acAreafuncT2
generadorT2.AddPoint((30214.4, 1800, 20525.6),("tombaGen21Skl", "Skeleton", "Espadaelfica", 0, "Escudo1", 1), "Skl_appears1",8)
generadorT2.AddPoint((39487.8, 1800, 24300.5),("tombaGen22Skl", "Skeleton", "Hacha4", 0, "Escudo1", 1), "Skl_appears1",9)
generadorT2.AddPoint((48000.8, 1800, 23000.5),("tombaGen23Skl", "Skeleton", "Hacha4", 0, "Escudo1", 1), "Skl_appears1",9)
generadorT2.AddPoint((40000.8, 1800, 21500.5),("tombaGen24Skl", "Skeleton", "Hacha4", 0, "Escudo1", 1), "Skl_appears1",9)
generadorT2.AddPoint((29000.8, 1800, 19250.5),("tombaGen25Skl", "Skeleton", "Hacha4", 0, "Escudo1", 1), "Skl_appears1",9)
generadorT2.AddPoint((22500.8, 1800, 25250.5),("tombaGen26Skl", "Skeleton", "Hacha4", 0, "Escudo1", 1), "Skl_appears1",9)

generadorT2.InitGenFunc=SaltaTierraGen
generadorT2.Activate()



SecGen1o = Bladex.GetSector(65000, 0, 22000)



############# GENERADOR 3 ######################en los zombies

generadorT3 = EnmGenRnd.CreateEnemiesGenerator(3, 3)

generadorT3.AddPoint((99000, 9500, 21000),("tombaGen31Skl", "Knight_Zombie", "Espadaelfica", 0, "Escudo1", 1), "Lch_appears1",8)
generadorT3.AddPoint((94500, 9500, 27000),("tombaGen32Skl", "Knight_Zombie", "Hacha4", 0, "Escudo1", 1), "Lch_appears1",9)
generadorT3.AddPoint((99000, 9500, 28000),("tombaGen33Skl", "Knight_Zombie", "Hacha4", 0, "Escudo1", 1), "Lch_appears1",9)


generadorT3.InitGenFunc=SaltaTierraGen
generadorT3.Activate()


darfuncs.EnterSecEvent(96000, 8000, 19000,generadorT3.GenerateEnemy)




############# GENERADOR 4 ######################en los zombies
#def acAreafuncT4(pers):
	#pers.ActionAreaMin=pow(2,2)
	#pers.ActionAreaMax=pow(2,3)


generadorT4 = EnmGenRnd.CreateEnemiesGenerator(4, 2)
#generadorT4.VirGenPos = 77500, 8200, 37500
#generadorT4.CallBak = acAreafuncT4
generadorT4.AddPoint((77500, 8200, 37500),("tombaGen41Skl", "Knight_Zombie", "Espadaelfica", 0, "Escudo1", 1), "Lch_appears1",8)
generadorT4.AddPoint((81500, 8200, 42000),("tombaGen42Skl", "Knight_Zombie", "Hacha4", 0, "Escudo1", 1), "Lch_appears1",9)
generadorT4.AddPoint((77500, 8200, 43500),("tombaGen43Skl", "Knight_Zombie", "Hacha4", 0, "Escudo1", 1), "Lch_appears1",9)
generadorT4.AddPoint((81000, 8200, 50750),("tombaGen44Skl", "Knight_Zombie", "Hacha4", 0, "Escudo1", 1), "Lch_appears1",9)


generadorT4.InitGenFunc=SaltaTierraGen
generadorT4.Activate()



darfuncs.EnterSecEvent(80000, 5000, 38000,generadorT4.GenerateEnemy)



############# GENERADOR 5 ######################en los zombies

generadorT5 = EnmGenRnd.CreateEnemiesGenerator(5, 2)

generadorT5.AddPoint((70000, 8400, 52000),("tombaGen51Skl", "Knight_Zombie", "Espadaelfica", 0, "Escudo1", 1), "Lch_appears1",8)
generadorT5.AddPoint((64500, 8400, 52250),("tombaGen52Skl", "Knight_Zombie", "Hacha4", 0, "Escudo1", 1), "Lch_appears1",9)
generadorT5.AddPoint((59000, 8400, 55000),("tombaGen53Skl", "Knight_Zombie", "Hacha4", 0, "Escudo1", 1), "Lch_appears1",9)
generadorT5.AddPoint((70000, 8400, 58000),("tombaGen54Skl", "Knight_Zombie", "Hacha4", 0, "Escudo1", 1), "Lch_appears1",9)
generadorT5.AddPoint((58000, 8400, 55000),("tombaGen55Skl", "Knight_Zombie", "Hacha4", 0, "Escudo1", 1), "Lch_appears1",9)


generadorT5.InitGenFunc=SaltaTierraGen
generadorT5.Activate()

darfuncs.EnterSecEvent(71000, 5000, 55000,generadorT5.GenerateEnemy)

#darfuncs.EnterSecEvent(71000, 5000, 55000,KreaKeletos)

###################################
###enemigos en el templo en la parte de arriba
fetichonKK = 0
