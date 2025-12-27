import Bladex


# ***********************************
# *      Asignacion de sonidos      *
# ***********************************
AsignarSonidosLittleDemonCalled=0
def AsignarSonidosLittleDemon(Personaje):
	from AniSoundLdmX import *

	per=Bladex.GetEntity(Personaje)

	# Sonidos de eventos

	per.AddEventSound('impale', TajoEmpalanteLdm)
	per.AddEventSound('slash', TajoCortanteLdm)
	per.AddEventSound('mutilate', TajoMutilacionLdm)
	per.AddEventSound('crush', GolpeContundenteLdm)
	
	
	global AsignarSonidosLittleDemonCalled
	if AsignarSonidosLittleDemonCalled:
		return
	AsignarSonidosLittleDemonCalled=1



	# Sonidos de animaciones
	
	
	per.AddAnimSound('Ldm_g_03', RespiracionDemonRapida1, 0.1100)
	per.AddAnimSound('Ldm_g_03', EsfuerzoCorto1Ldm, 0.2170)
	per.AddAnimSound('Ldm_g_03', SesgadoLargoGrave, 0.3530)
	per.AddAnimSound('Ldm_g_03', RespiracionDemonRapida1, 0.5000)
	per.AddAnimSound('Ldm_g_03', RespiracionDemonRapida2, 0.7000)
	per.AddAnimSound('Ldm_g_03', RespiracionDemonRapida1, 0.9000)
	per.AddAnimSound('Ldm_g_06', SesgadoLargo, 0.4620)
	per.AddAnimSound('Ldm_g_06', EsfuerzoCorto2Ldm, 0.4300)
	per.AddAnimSound('Ldm_g_06', RespiracionDemonRapida1, 0.1100)
	per.AddAnimSound('Ldm_g_06', RespiracionDemonRapida2, 0.3000)
	per.AddAnimSound('Ldm_g_06', RespiracionDemonRapida1, 0.6000)
	per.AddAnimSound('Ldm_g_06', RespiracionDemonRapida2, 0.8500)
	per.AddAnimSound('Ldm_g_07', SesgadoCorto, 0.3220)
	per.AddAnimSound('Ldm_g_07', SesgadoCortoGrave, 0.4710)
	per.AddAnimSound('Ldm_g_07', EsfuerzoGolpeArribaLdm, 0.4000)
	per.AddAnimSound('Ldm_g_07', RespiracionDemonRapida1, 0.1200)
	per.AddAnimSound('Ldm_g_07', RespiracionDemonRapida2, 0.2200)
	per.AddAnimSound('Ldm_g_07', RespiracionDemonRapida1, 0.5500)
	per.AddAnimSound('Ldm_g_07', RespiracionDemonRapida2, 0.7000)
	per.AddAnimSound('Ldm_g_07', RespiracionDemonRapida1, 0.8500)
	per.AddAnimSound('Ldm_g_12', EsfuerzoGolpeArribaLdm, 0.1720)
	per.AddAnimSound('Ldm_g_12', EsfuerzoCorto3Ldm, 0.3800)
	per.AddAnimSound('Ldm_g_12', EsfuerzoCorto1Ldm, 0.5440)
	per.AddAnimSound('Ldm_g_12', SesgadoLargoGrave, 0.5440)
	per.AddAnimSound('Ldm_g_12', EsfuerzoGolpeCabezaLdm, 0.6860)
	per.AddAnimSound('Ldm_g_12', RespiracionDemonRapida1, 0.2500)
	per.AddAnimSound('Ldm_g_12', RespiracionDemonRapida2, 0.4000)
	per.AddAnimSound('Ldm_g_12', RespiracionDemonRapida1, 0.6860)
	per.AddAnimSound('Ldm_g_12', RespiracionDemonRapida2, 0.6860)
	per.AddAnimSound('Ldm_g_17', EsfuerzoCorto1Ldm, 0.1600)
	per.AddAnimSound('Ldm_g_17', EsfuerzoCortoLdm, 0.3890)
	per.AddAnimSound('Ldm_g_17', EsfuerzoGolpeFrontalLdm, 0.6000)
	per.AddAnimSound('Ldm_g_17', SesgadoLargoGrave, 0.6270)
	per.AddAnimSound('Ldm_g_22', EsfuerzoGolpeLateralLdm, 0.1000)
	per.AddAnimSound('Ldm_g_22', SesgadoLargo, 0.1700)
	per.AddAnimSound('Ldm_g_22', SesgadoCortoGrave, 0.4250)
	per.AddAnimSound('Ldm_g_27', EsfuerzoGolpeFrontalLdm, 0.1150)
	per.AddAnimSound('Ldm_g_27', SesgadoCorto, 0.2300)
	
	per.AddAnimSound('Ldm_g_spit', LanzarFuego, 0.4300)
	per.AddAnimSound('Ldm_dth_disap', MuerteLdm, 0.1200)
	
	per.AddAnimSound('Ldm_hurt_big', HeridaLdm1, 0.1100)
	per.AddAnimSound('Ldm_hurt_f_big', HeridaLdm2, 0.1600)
	per.AddAnimSound('Ldm_hurt_f_lite', HeridaLdm3, 0.2840)
	
	per.AddAnimSound('Ldm_g_jumpr', SaltoLdm1, 0.3000)
	per.AddAnimSound('Ldm_g_jumpl', SaltoLdm2, 0.3800)
	
	per.AddAnimSound('Ldm_jump_no', CaidaLdm1, 0.9000)
	per.AddAnimSound('Ldm_jump_no', EsfuerzoCorto1Ldm, 0.4770)
	
	per.AddAnimSound('Ldm_fll_high', CaidaLdm1, 0.1100)
	per.AddAnimSound('Ldm_fll_high', EsfuerzoCorto1Ldm, 0.4770)
	per.AddAnimSound('Ldm_fll_high', EsfuerzoGolpeCabezaLdm, 0.8430)
	
	
	per.AddAnimSound('Ldm_jog_no', RespiracionDemonRapida1, 0.1000)
	per.AddAnimSound('Ldm_jog_no', RespiracionDemonRapida2, 0.3000)
	per.AddAnimSound('Ldm_jog_no', RespiracionDemonRapida1, 0.6000)
	per.AddAnimSound('Ldm_jog_no', RespiracionDemonRapida2, 0.9000)
	per.AddAnimSound('Ldm_attack_f', RespiracionDemonRapida1, 0.1000)
	per.AddAnimSound('Ldm_attack_f', RespiracionDemonRapida2, 0.3000)
	per.AddAnimSound('Ldm_attack_f', RespiracionDemonRapida1, 0.6000)
	per.AddAnimSound('Ldm_attack_f', RespiracionDemonRapida2, 0.9000)
	per.AddAnimSound('Ldm_attack_b', RespiracionDemonRapida1, 0.1000)
	per.AddAnimSound('Ldm_attack_b', RespiracionDemonRapida2, 0.3000)
	per.AddAnimSound('Ldm_attack_b', RespiracionDemonRapida1, 0.6000)
	per.AddAnimSound('Ldm_attack_b', RespiracionDemonRapida2, 0.9000)
	per.AddAnimSound('Ldm_wbk_no', RespiracionDemon1, 0.1000)
	per.AddAnimSound('Ldm_wbk_no', RespiracionDemon2, 0.3000)
	per.AddAnimSound('Ldm_wbk_no', RespiracionDemon1, 0.6000)
	per.AddAnimSound('Ldm_wbk_no', RespiracionDemon2, 0.9000)
	per.AddAnimSound('Ldm_wlk_no', RespiracionDemon1, 0.1000)
	per.AddAnimSound('Ldm_wlk_no', RespiracionDemon2, 0.3000)
	per.AddAnimSound('Ldm_wlk_no', RespiracionDemon1, 0.6000)
	per.AddAnimSound('Ldm_wlk_no', RespiracionDemon2, 0.9000)
	per.AddAnimSound('Ldm_rlx_no', RespiracionDemon1, 0.1000)
	per.AddAnimSound('Ldm_rlx_no', RespiracionDemon2, 0.3000)
	per.AddAnimSound('Ldm_rlx_no', RespiracionDemon1, 0.6000)
	per.AddAnimSound('Ldm_rlx_no', RespiracionDemon2, 0.9000)
	per.AddAnimSound('Ldm_appears', RugidoAparicionDemon, 0.5694)
