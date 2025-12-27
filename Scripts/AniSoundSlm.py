import Bladex

# ***********************************
# *      Asignacion de sonidos      *
# ***********************************

AsignarSonidosSalamanderCalled=0
def AsignarSonidosSalamander(Personaje):
	from AniSoundSlmX import *

	per=Bladex.GetEntity(Personaje)

	# Sonidos de eventos

	per.AddEventSound('shield_block', GolpeArmaEscudoSlm)
	per.AddEventSound('weapon_block', GolpeArmaArmaSlm)
	per.AddEventSound('impale', TajoEmpalanteSlm)
	per.AddEventSound('slash', TajoCortanteSlm)
	per.AddEventSound('mutilate', TajoMutilacionSlm)
	per.AddEventSound('crush', GolpeContundenteSlm)
	
	
	
	global AsignarSonidosSalamanderCalled
	if AsignarSonidosSalamanderCalled:
		return
	AsignarSonidosSalamanderCalled=1


	# Sonidos de animaciones

	# Animation Sleep
	
	per.AddAnimSound('Slm_spit', EsfuerzoCorto1Slm, 0.3620)
	per.AddAnimSound('Slm_spit', FuegoSlm,0.3700)
	per.AddAnimSound('Slm_spit', RespiraSlm2,0.6500)
	per.AddAnimSound('Slm_spit', RespiraSlm1,0.8500)
	per.AddAnimSound('Slm_spit', MovSlm1, 0.1100)
	per.AddAnimSound('Slm_spit', MovSlm2, 0.3000)
	per.AddAnimSound('Slm_spit', MovSlm2, 0.5000)
	per.AddAnimSound('Slm_spit', MovSlm1, 0.9000)
	per.AddAnimSound('Slm_g_bite', EsfuerzoCorto2Slm, 0.1500)
	per.AddAnimSound('Slm_g_bite', MovSlm1, 0.2500)
	per.AddAnimSound('Slm_g_bite', MovSlm2, 0.5000)
	per.AddAnimSound('Slm_g_bite', MovSlm1, 0.5000)
	per.AddAnimSound('Slm_g_bite', EsfuerzoCorto3Slm, 0.6930)
	per.AddAnimSound('Slm_g_r', EsfuerzoCorto4Slm, 0.2750)
	per.AddAnimSound('Slm_g_r', MovSlm1, 0.2500)
	per.AddAnimSound('Slm_g_r', MovSlm2, 0.5000)
	per.AddAnimSound('Slm_g_r', MovSlm1, 0.5000)
	
	
	

	per.AddAnimSound('Slm_clmb_low', EsfuerzoCorto1Slm, 0.2550)
	per.AddAnimSound("Slm_dth0", MuerteSlm2, 0.1100)
	per.AddAnimSound("Slm_dth0", MovSlm1, 0.1800)
	per.AddAnimSound("Slm_dth0", MovSlm2, 0.3500)
	per.AddAnimSound("Slm_dth0", MovSlm1, 0.5200)
	per.AddAnimSound("Slm_dth0", MovSlm2, 0.7500)
	per.AddAnimSound("Slm_dth0", MovSlm1, 0.9000)
	per.AddAnimSound("Slm_dth0", EsfuerzoCorto4Slm, 0.3000)
	per.AddAnimSound("Slm_dth0", RespiraSlm1, 0.3000)
	per.AddAnimSound("Slm_dth0", MuerteSlm1, 0.4000)
	per.AddAnimSound("Slm_dth0", RespiraSlm1, 0.7500)
	per.AddAnimSound("Slm_dth0", RespiraSlm2, 0.9000)
	per.AddAnimSound("Slm_dth0", CaidaSlm, 0.1550)
	per.AddAnimSound("Slm_hurt_f_lite", HeridaSlm2, 0.2100)
	per.AddAnimSound("Slm_hurt_f_lite", RespiraSlm2, 0.3500)
	per.AddAnimSound("Slm_hurt_f_lite", RespiraSlm1, 0.5500)
	per.AddAnimSound("Slm_hurt_f_lite", RespiraSlm2, 0.7500)
	per.AddAnimSound("Slm_hurt_f_lite", RespiraSlm1, 0.3500)
	per.AddAnimSound("Slm_hurt_f_lite", MovSlm1, 0.1300)
	per.AddAnimSound("Slm_hurt_f_lite", MovSlm2, 0.3000)
	per.AddAnimSound("Slm_hurt_f_lite", MovSlm1, 0.7000)
	per.AddAnimSound("Slm_hurt_f_lite", MovSlm2, 0.5000)
	per.AddAnimSound("Slm_hurt_f_big", HeridaSlm1, 0.1100)
	per.AddAnimSound("Slm_hurt_f_big", CaidaSlm, 0.1900)
	per.AddAnimSound("Slm_hurt_f_big", RespiraSlm1, 0.5000)
	per.AddAnimSound("Slm_hurt_f_big", RespiraSlm2, 0.7000)
	per.AddAnimSound("Slm_hurt_f_big", HeridaSlm2, 0.3000)
	per.AddAnimSound("Slm_hurt_f_big", EsfuerzoCorto4Slm, 0.9000)
	per.AddAnimSound("Slm_hurt_f_big", MovSlm1, 0.2000)
	per.AddAnimSound("Slm_hurt_f_big", MovSlm2, 0.4000)
	per.AddAnimSound("Slm_hurt_f_big", MovSlm1, 0.6000)
	per.AddAnimSound("Slm_hurt_f_big", MovSlm2, 0.8000)
	per.AddAnimSound("Wlk_no_Slm", RespiraSlm2, 0.2000)
	per.AddAnimSound("Wlk_no_Slm", MovSlm1, 0.1100)
	per.AddAnimSound("Wlk_no_Slm", RespiraSlm2, 0.4000)
	per.AddAnimSound("Wlk_no_Slm", MovSlm2, 0.5000)
	per.AddAnimSound("Wlk_no_Slm", RespiraSlm1, 0.6000)
	per.AddAnimSound("Wlk_no_Slm", MovSlm1, 0.7000)
	per.AddAnimSound("Wlk_no_Slm", RespiraSlm2, 0.8000)
	per.AddAnimSound("Wlk_no_Slm", MovSlm2, 0.9000)
	per.AddAnimSound("Wbk_no_Slm", RespiraSlm2, 0.2000)
	per.AddAnimSound("Wbk_no_Slm", MovSlm1, 0.1100)
	per.AddAnimSound("Wbk_no_Slm", RespiraSlm2, 0.4000)
	per.AddAnimSound("Wbk_no_Slm", MovSlm2, 0.5000)
	per.AddAnimSound("Wbk_no_Slm", RespiraSlm1, 0.6000)
	per.AddAnimSound("Wbk_no_Slm", MovSlm1, 0.7000)
	per.AddAnimSound("Wbk_no_Slm", RespiraSlm2, 0.8000)
	per.AddAnimSound("Wbk_no_Slm", MovSlm2, 0.9000)
	per.AddAnimSound("Rlx_no_Slm", RespiraSlm2, 0.2000)
	per.AddAnimSound("Rlx_no_Slm", MovSlm1, 0.1100)
	per.AddAnimSound("Rlx_no_Slm", RespiraSlm2, 0.4000)
	per.AddAnimSound("Rlx_no_Slm", MovSlm1, 0.5000)
	per.AddAnimSound("Rlx_no_Slm", RespiraSlm1, 0.6000)
	per.AddAnimSound("Rlx_no_Slm", MovSlm1, 0.8000)
	per.AddAnimSound("Rlx_no_Slm", RespiraSlm2, 0.8000)
	per.AddAnimSound("Rlx_no_jog", RespiraSlm2, 0.2000)
	per.AddAnimSound("Rlx_no_jog", MovSlm1, 0.1100)
	per.AddAnimSound("Rlx_no_jog", RespiraSlm2, 0.4000)
	per.AddAnimSound("Rlx_no_jog", MovSlm1, 0.5000)
	per.AddAnimSound("Rlx_no_jog", RespiraSlm1, 0.6000)
	per.AddAnimSound("Rlx_no_jog", MovSlm1, 0.8000)
	per.AddAnimSound("Rlx_no_jog", RespiraSlm2, 0.8000)




