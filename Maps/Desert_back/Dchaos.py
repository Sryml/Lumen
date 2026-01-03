import BackMisc
import darfuncs



res=ReadGSFile.ReadGhostSectorFile("Dchaos.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])


Bladex.GetEntity("Player1").SendTriggerSectorMsgs=1

#
# CHAOS KNIGHT
#

BackMisc.CHAOS_KNIGHT_LEVEL       = 4
BackMisc.CHAOS_KNIGHT_POSITION    = -44500, -6000, 126500
BackMisc.CHAOS_KNIGHT_ANGLE       = 0


BackMisc.AddChaosDisappearsSector(-35500,-5000,106000)
BackMisc.AddChaosDisappearsSector(-15980.2336942, -4911.04583472, 102529.3)
BackMisc.AddChaosDisappearsSector(-11350.2881911, -4411.72266718, 106476.6)
BackMisc.AddChaosDisappearsSector(-27074.1176288, -5090.57103493, 94868.6)
BackMisc.AddChaosDisappearsSector(-53797.1, 2558.7, 139988.6)		


BackMisc.EXEC_IN_PLAYER_APPEARING       = EnciendeMusicaInicio
BackMisc.EXEC_IN_CHAOS_KNIGHT_APPEARING = EnciendeMusicaApChaos

BackMisc.HideEnemiesSector   ((-40000, -5000, 116000))


BackMisc.AddChaosAppearsSector(-40000, -5000, 116000)
BackMisc.AddChaosAppearsSector(-44500, -8000, 136500)

BackMisc.PrepareChaosAppears()



## DEMONIOS Y VAMPIROS 17 MONSTRUOS EN TOTAL

BackMisc.AddVampires(8,(-24686.0252265, -1430.77399154, 10420.0),3)
BackMisc.AddDemons  (9,(-24686.0252265, -1430.77399154, 10420.0),6)

## DEMONS IN THE PATIO CENTRAL Y TWO ALTARES

#EN EL CENTRO
BackMisc.HideEnemiesSector   (("secF1"))
BackMisc.AddDemonAppears     (("secF1"),(-24686.0, -1430.7, 10420.0),0.1)
idx = BackMisc.AddSectorCount(("secF1"),3,0)
BackMisc.AddSectorDelete(idx, ("secF1"))


#ALTAR AGUA
BackMisc.HideEnemiesSector ((9283.0, -3812.1, 27657.8))
BackMisc.AddDemonAppears   ((9283.0, -3812.1, 27657.8),(4603.9, -3760.9, 38179.7),0.1)
idx = BackMisc.AddSectorCount((9283.0, -3812.1, 27657.8),3,0)
BackMisc.AddSectorDelete(idx, (9283.0, -3812.1, 27657.8))

#ALTAR FUEGO
BackMisc.HideEnemiesSector ((-52464.6, -3508.0, 33463.7))
BackMisc.AddDemonAppears   ((-52464.6, -3508.0, 33463.7),(-50804.4, -3462.7, 34832.7),0.1)
idx = BackMisc.AddSectorCount((-52464.6, -3508.0, 33463.7),3,0)
BackMisc.AddSectorDelete(idx, (-52464.6, -3508.0, 33463.7))


#ALTAR FUEGO
BackMisc.HideEnemiesSector ((-53184.2, -3766.7, 51851.7))
BackMisc.AddDemonAppears   ((-53184.2, -3766.7, 51851.7),(-53160.6, -4063.8, 55856.1),0.1)
idx = BackMisc.AddSectorCount((-53184.2, -3766.7, 51851.7),2,0)
BackMisc.AddSectorDelete(idx, (-53184.2, -3766.7, 51851.7))

#detras pilono ALTAR FUEGO
BackMisc.HideEnemiesSector ((-40315.5, -5250.6, 74537.7))
BackMisc.AddDemonAppears   ((-40315.5, -5250.6, 74537.7),(-40315.5, -5250.6, 74537.7),0.1)
idx = BackMisc.AddSectorCount((-40315.5, -5250.6, 74537.7),2,0)
BackMisc.AddSectorDelete(idx, (-40315.5, -5250.6, 74537.7))


## DEMONIO AL LADO CORTO DE LA MASTABA

BackMisc.HideEnemiesSector ((-37629.9, -5265.2, 89984.0))
BackMisc.AddDemonAppears   ((-37629.9, -5265.2, 89984.0),(-37629.9, -5265.2, 89984.0),0.1)
idx = BackMisc.AddSectorCount((-37629.9, -5265.2, 89984.0),2,0)
BackMisc.AddSectorDelete(idx, (-37629.9, -5265.2, 89984.0))

## DEMONS IN THE PATIO DESPUES DEL ALTAR DE AGUA

BackMisc.HideEnemiesSector ((-3315.6, -4375.3, 56668.6))
BackMisc.AddDemonAppears   ((-3315.6, -4375.3, 56668.6),(-10817.1, -4661.5, 61627.9),0.1)
#idx = BackMisc.AddSectorCount((325375, 9, -173845),3,0)
#BackMisc.AddSectorDelete(idx, (325375, 9, -173845))
#BackMisc.AddSectorDelete(idx, (325334, -69, -181620))

#al lado de la escalera subida
BackMisc.HideEnemiesSector   ((-7965.2, -5595.0, 81292.9))
BackMisc.AddVampireAppears   ((-7965.2, -5595.0, 81292.9),(-7965.2, -5595.0, 81292.9),0.1)
#idx = BackMisc.AddSectorCount((325375, 9, -173845),3,0)
#BackMisc.AddSectorDelete(idx, (325375, 9, -173845))
#BackMisc.AddSectorDelete(idx, (325334, -69, -181620))



#	VAMPIRO EN EL PASO DE MADERA


BackMisc.HideEnemiesSector   ((-10280.9, -11899.6, 88217.9))
BackMisc.AddVampireAppears   ((-10280.9, -11899.6, 88217.9),(-17593.8, -12685.0, 88334.3),0.1)
#idx = BackMisc.AddSectorCount((325375, 9, -173845),3,0)
#BackMisc.AddSectorDelete(idx, (325375, 9, -173845))
#BackMisc.AddSectorDelete(idx, (325334, -69, -181620))




##  TWO DEMONS IN THE MASTABA 

BackMisc.HideEnemiesSector  ((-29673.6, -5590.5, 88806.2))
BackMisc.AddDemonAppears    ((-29673.6, -5590.5, 88806.2),(-29673.6, -5590.5, 88806.2),0.3)


##  VAMPIROS EN LA SALA HIPOSTILA 

BackMisc.HideEnemiesSector   ((-25813.5, -4072.6, 116511.1))
BackMisc.AddVampireAppears   ((-25813.5, -4072.6, 116511.1),(-20791.0, -4090.3, 116610.0),0.9)
BackMisc.AddVampireAppears   ((-25813.5, -4072.6, 116511.1),(-26965.5, -4082.7, 121892.6),0.5)

BackMisc.ActivateSectorProcs()