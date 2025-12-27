import Bladex


# ***********************************
# *      Asignacion de sonidos      *
# ***********************************

AsignarSonidosCaballeroKaosCalled=0
def AsignarSonidosCaballeroKaos(Personaje):

	from AniSoundChkX import *
	
	per=Bladex.GetEntity(Personaje)


	# Sonidos de eventos

	per.AddEventSound('shield_block', GolpeArmaEscudoChk)
	per.AddEventSound('weapon_block', GolpeArmaArmaChk)
	per.AddEventSound('impale', TajoEmpalanteMetalChk)
	per.AddEventSound('slash', TajoCortanteMetalChk)
	per.AddEventSound('mutilate', TajoMutilacionMetalChk)
	per.AddEventSound('crush', GolpeContundenteChk)
	
	
	
	global AsignarSonidosCaballeroKaosCalled
	if AsignarSonidosCaballeroKaosCalled:
		return
	AsignarSonidosCaballeroKaosCalled=1



	# Sonidos de animaciones

	
	per.AddAnimSound('Chk_g_12', SesgadoLargoGrave2, 0.4000)
	per.AddAnimSound('Chk_g_12', EsfuerzoGolpeFrontalChk, 0.2410)
	per.AddAnimSound('Chk_g_18', SesgadoLargoGrave2, 0.4224)
	per.AddAnimSound('Chk_g_18', EsfuerzoGolpeArribaChk, 0.4224)
	per.AddAnimSound('Chk_g_01', SesgadoLargoGrave, 0.3117)
	per.AddAnimSound('Chk_g_01', EsfuerzoCorto6Chk, 0.3117)
	per.AddAnimSound('Chk_g_02', SesgadoLargoGrave, 0.3026)
	per.AddAnimSound('Chk_g_02', EsfuerzoCorto5Chk, 0.2200)
	per.AddAnimSound('Chk_g_07', SesgadoLargoGrave, 0.2500)
	per.AddAnimSound('Chk_g_07', EsfuerzoCorto4Chk, 0.3291)
	per.AddAnimSound('Chk_g_08', SesgadoLargoGrave, 0.3000)
	per.AddAnimSound('Chk_g_08', EsfuerzoCorto2Chk, 0.4030)
	per.AddAnimSound('Chk_g_31', SesgadoLargoGrave2, 0.2950)
	per.AddAnimSound('Chk_g_31', EsfuerzoGolpeAtrasChk, 0.2950)
	per.AddAnimSound('Chk_g_31', SesgadoLargoGrave2, 0.2950)	
	
	
	per.AddAnimSound('Chk_dth0', MuerteChk, 0.2950)	
	per.AddAnimSound('Chk_dth0', electrico, 0.1500)	