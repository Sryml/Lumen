import Bladex

# ***********************************
# *      Asignacion de sonidos      *
# ***********************************
AsignarSonidosGolem_mtCalled=0
def AsignarSonidosGolem_mt(Personaje):

	from AniSoundGlm_mtX import *
	
	per=Bladex.GetEntity(Personaje)

	# Sonidos de eventos
	
	#per.AddEventSound('shield_block', GolpeArmaEscudoGlmmt)
	#per.AddEventSound('weapon_block', GolpeArmaArmaGlmmt)
	per.AddEventSound('impale', TajoEmpalanteGlmmt)
	per.AddEventSound('slash', TajoCortanteGlmmt)
	per.AddEventSound('mutilate', TajoMutilacionGlmmt)
	per.AddEventSound('crush', GolpeContundenteGlmmt)


	global AsignarSonidosGolem_mtCalled
	if AsignarSonidosGolem_mtCalled:
		return
	AsignarSonidosGolem_mtCalled=1
		
	# Sonidos de animaciones
	
	per.AddAnimSound('Glm_g_01', EsfuerzoGlmmt1, 0.3790)
	per.AddAnimSound('Glm_g_01', SesgadoGlmmt1, 0.4000)
	per.AddAnimSound('Glm_g_12', SesgadoGlmmt2, 0.3880)
	per.AddAnimSound('Glm_g_12', EsfuerzoGlmmt2, 0.3050)
	per.AddAnimSound('Glm_g_21', SesgadoGlmmt3, 0.3440)
	per.AddAnimSound('Glm_g_21', EsfuerzoGlmmt3, 0.3000)
	per.AddAnimSound('Glm_g_31', SesgadoGlmmt4, 0.3000)
	per.AddAnimSound('Glm_g_31', EsfuerzoGlmmt4, 0.2840)
	per.AddAnimSound('Glm_g_31', caidagolemmt2, 0.3240)
	per.AddAnimSound('Glm_g_114', SesgadoGlmmt5, 0.4350)
	per.AddAnimSound('Glm_g_114', EsfuerzoGlmmt5, 0.2390)
	per.AddAnimSound('Glm_g_21_27', SesgadoGlmmt6, 0.2750)
	per.AddAnimSound('Glm_g_21_27', EsfuerzoGlmmt6, 0.2750)
	per.AddAnimSound('Glm_g_21_27', SesgadoGlmmt7, 0.5430)
	per.AddAnimSound('Glm_g_21_27', EsfuerzoGlmmt7, 0.5430)
	per.AddAnimSound('Glm_g_tw1', CreaPiedraGlmmt, 0.5430)
	
	per.AddAnimSound('Glm_dth0', caidagolemmt, 0.7720)
	per.AddAnimSound('Glm_dth0', MuerteGlmmt1, 0.1590)
	per.AddAnimSound('Glm_dth2', caidagolemmt, 0.7720)
	per.AddAnimSound('Glm_dth2', MuerteGlmmt1, 0.1590)
	per.AddAnimSound('Glm_dth_c1', caidagolemmt, 0.9150)
	per.AddAnimSound('Glm_dth_c1', caidagolemmt2, 0.6270)
	per.AddAnimSound('Glm_dth_c1', MuerteGlmmt1, 0.1590)
	per.AddAnimSound('Glm_dth_i1', caidagolemmt2, 0.5830)
	per.AddAnimSound('Glm_dth_i1', caidagolemmt3, 0.7020)
	per.AddAnimSound('Glm_dth_i1', MuerteGlmmt1, 0.1590)
	per.AddAnimSound('Glm_dth_i1', caidagolemmt2, 0.3630)
	per.AddAnimSound('Glm_dth_i1', caidagolemmt3, 0.6200)
	per.AddAnimSound('Glm_dth_i1', MuerteGlmmt1, 0.1590)


	per.AddAnimSound('Glm_hurt_big', HeridaGlmmt1, 0.1670)
	per.AddAnimSound('Glm_hurt_lite', HeridaGlmmt2, 0.1720)
	
	
	
	
	