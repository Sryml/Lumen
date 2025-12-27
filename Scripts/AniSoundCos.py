import Bladex
#import NetSounds
#import netgame


# ***********************************
# *      Asignacion de sonidos      *
# ***********************************
AsignarSonidosCositaCalled=0
def AsignarSonidosCosita(Personaje):

	from AniSoundCosX import *
	
	per=Bladex.GetEntity(Personaje)

	# Sonidos de eventos

#	
	per.AddEventSound('shield_block', GolpeArmaEscudoCos)
	per.AddEventSound('weapon_block', GolpeArmaArmaCos)
	per.AddEventSound('impale', TajoEmpalanteCos)
	per.AddEventSound('slash', TajoCortanteCos)
	per.AddEventSound('mutilate', TajoMutilacionCos)
	per.AddEventSound('crush', GolpeContundenteCos)
	
	
	global AsignarSonidosCositaCalled
	if AsignarSonidosCositaCalled:
		return
	AsignarSonidosCositaCalled=1
	

	# Sonidos de animaciones

#	Animation Alarm (We want a selection of sounds, so better link a function)
	#per.AddAnimSound('Cos_alarm01', KnightKeepStill, 0)

	per.AddAnimSound('Cos_g_01', Mordisco1Cos, 0.0227)
	per.AddAnimSound('Cos_g_02', Mordisco2Cos, 0.4118)
	per.AddAnimSound('Cos_attack_b', EsfuerzoLargoCos, 0.5)
	per.AddAnimSound('Cos_attack_f', EsfuerzoCortoCos, 0.5)
	per.AddAnimSound('Cos_attack_l', EsfuerzoMedioCos, 0.5)
	per.AddAnimSound('Cos_attack_r', EsfuerzoLargoCos, 0.5)

	per.AddAnimSound('Cos_alarm', SustoCos, 0.1430)
	per.AddAnimSound('Cos_alarm', EsfuerzoCortoCos, 0.3880)
	per.AddAnimSound('Cos_alarm', SustoCos, 0.6630)

	per.AddAnimSound('Cos_jmp0_1h', EsfuerzoCortoCos, 0.1)
	per.AddAnimSound('Cos_jmp1_1h', EsfuerzoCortoCos, 0.1)
	per.AddAnimSound('Cos_jmp2_1h', EsfuerzoMedioCos, 0.1)
	per.AddAnimSound('Cos_jmp3_1h', EsfuerzoMedioCos, 0.1)

	per.AddAnimSound('Cos_dth0', MuerteCos, 0.1800)
	per.AddAnimSound('Cos_dth_fly', MuerteCos, 0.5172)

	per.AddAnimSound('Cos_fury', Risa1Cos, 0.4)

	per.AddAnimSound('Cos_hurt_lite', Herida1Cos, 0.0294)

	per.AddAnimSound('Cos_rlx_f', Risa2Cos, 0.2000)
	per.AddAnimSound('Cos_rlx_no', Risa3Cos, 0.2000)