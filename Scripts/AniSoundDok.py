import Bladex

# ***********************************
# *      Asignacion de sonidos      *
# ***********************************


def AsignarSonidosOrcoOscuro(Personaje):
	from AniSoundDokX import *
	
	per=Bladex.GetEntity(Personaje)

	# Sonidos de eventos

	per.AddEventSound('shield_block', GolpeArmaEscudoDok)
	per.AddEventSound('weapon_block', GolpeArmaArmaDok)
	per.AddEventSound('impale', TajoEmpalanteDok)
	per.AddEventSound('slash', TajoCortanteDok)
	per.AddEventSound('mutilate', TajoMutilacionDok)
	per.AddEventSound('crush', GolpeContundenteDok)


	# Sonidos de animaciones

	# Animation Alarm (We want a selection of sounds, so better link a function)
	per.AddAnimSound('Tkn_alarm01', KnightKeepStill, 0)
	
	# Animation Speak01
	per.AddAnimSound('Ork_chg_r', Enfundar, 7)
	per.AddAnimSound('Ork_chg_r_l', Enfundar, 7)
	per.AddAnimSound('Ork_attack_chg_r_l', Enfundar, 8)
	per.AddAnimSound('Ork_attack_chg_r', Enfundar, 7)
	per.AddAnimSound('Ork_chg_r', Enfundar, 7)
	per.AddAnimSound('Ork_chg_r_l', Enfundar, 7)
	per.AddAnimSound('Ork_attack_chg_r_l', Enfundar, 8)
	per.AddAnimSound('Ork_attack_chg_r', Enfundar, 7)

	per.AddAnimSound('Ork_g_01', EsfuerzoCortoDok, 32)
	per.AddAnimSound('Ork_g_02', EsfuerzoCorto1Dok, 32)
	per.AddAnimSound('Ork_g_06', EsfuerzoCorto3Dok, 42)
	per.AddAnimSound('Ork_g_01', SesgadoCorto, 30)
	per.AddAnimSound('Ork_g_02', SesgadoCortoAgudo, 34)
	per.AddAnimSound('Ork_g_06', SesgadoCorto, 40)
	per.AddAnimSound('Ork_g_15', EsfuerzoGolpeLateralDok, 54)
	per.AddAnimSound('Ork_g_16', EsfuerzoGolpeLateralDok, 62)
	per.AddAnimSound('Ork_g_18', EsfuerzoGolpeArribaDok, 47)
	per.AddAnimSound('Ork_g_15', SesgadoLargo, 50)
	per.AddAnimSound('Ork_g_16', SesgadoLargoAgudo, 69)
	per.AddAnimSound('Ork_g_18', SesgadoLargoGrave, 48)

	per.AddAnimSound('Ork_clmb_medlow_1h', EsfuerzoCorto2Dok, 8)
	per.AddAnimSound('Ork_clmb_medium_1h', EsfuerzoCorto2Dok, 8)
	per.AddAnimSound('Ork_clmb_high_1h', EsfuerzoCorto1Dok, 8)
	per.AddAnimSound('Ork_clmb_medlow_no', EsfuerzoCorto2Dok, 8)
	per.AddAnimSound('Ork_clmb_medium_no', EsfuerzoCorto2Dok, 8)
	per.AddAnimSound('Ork_clmb_high_no', EsfuerzoCorto1Dok, 8)
	per.AddAnimSound('Ork_clmb_medium_1h', EsfuerzoCortoDok, 28)
	per.AddAnimSound('Ork_clmb_high_1h', EsfuerzoCorto3Dok, 35)
	per.AddAnimSound('Ork_clmb_high_1h', EsfuerzoCortoDok, 62)
	per.AddAnimSound('Ork_clmb_medium_no', EsfuerzoCortoDok, 28)
	per.AddAnimSound('Ork_clmb_high_no', EsfuerzoCorto3Dok, 35)
	per.AddAnimSound('Ork_clmb_high_no', EsfuerzoCortoDok, 62)

	per.AddAnimSound("Ork_dth0", MuerteDok1, 1)
	per.AddAnimSound("Ork_dth_n00", MuerteDok1, 1)
	per.AddAnimSound("Ork_dth_n01", MuerteDok2, 3)
	per.AddAnimSound("Ork_dth_n02", MuerteDok3, 3)
	per.AddAnimSound("Ork_dth_n03", MuerteDok4, 3)
	per.AddAnimSound("Ork_dth_i1", MuerteDok1, 6)
	per.AddAnimSound("Ork_dth_i2", MuerteDok4, 4)
	per.AddAnimSound("Ork_dth_bl1", MuerteDok2, 4)
	per.AddAnimSound("Ork_dth_bl2", MuerteDok1, 3)
	per.AddAnimSound("Ork_dth_rock", MuerteDok3, 9)

	per.AddAnimSound("Ork_hurt_jog", HeridaDok1, 3)
	per.AddAnimSound("Ork_hurt_neck", HeridaDok2, 3)
	per.AddAnimSound("Ork_hurt_breast", HeridaDok2, 3)
	per.AddAnimSound("Ork_hurt_back", HeridaDok2, 5)
	per.AddAnimSound("Ork_hurt_r_arm", HeridaDok2, 3)
	per.AddAnimSound("Ork_hurt_l_arm", HeridaDok3, 3)
	per.AddAnimSound("Ork_hurt_r_leg", HeridaDok1, 3)
	per.AddAnimSound("Ork_hurt_l_leg", HeridaDok2, 3)
	per.AddAnimSound("Ork_hurt_f_head", HeridaDok3, 3)
	per.AddAnimSound("Ork_hurt_f_neck", HeridaDok2, 2)
	per.AddAnimSound("Ork_hurt_f_breast", HeridaDok2, 3)
	per.AddAnimSound("Ork_hurt_f_back", HeridaDok2, 2)
	per.AddAnimSound("Ork_hurt_f_r_arm", HeridaDok1, 3)
	per.AddAnimSound("Ork_hurt_f_l_arm", HeridaDok3, 3)
	per.AddAnimSound("Ork_hurt_f_r_leg", HeridaDok2, 3)
	per.AddAnimSound("Ork_hurt_f_l_leg", HeridaDok2, 3)
	per.AddAnimSound("Ork_hurt_f_lite", HeridaDok1, 2)
	per.AddAnimSound("Ork_hurt_f_big", HeridaDok3, 3)
	per.AddAnimSound("Ork_hurt_head", HeridaDok2, 3)
