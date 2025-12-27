import Bladex

# ***********************************
# *      Asignacion de sonidos      *
# ***********************************
AsignarSonidosGolem_clCalled=0
def AsignarSonidosGolem_cl(Personaje):
	
	from AniSoundGlm_clX import *
	
	per=Bladex.GetEntity(Personaje)

	# Sonidos de eventos
	
	#per.AddEventSound('shield_block', GolpeArmaEscudoGlmcl)
	#per.AddEventSound('weapon_block', GolpeArmaArmaGlmcl)
	per.AddEventSound('impale', TajoEmpalanteGlmcl)
	per.AddEventSound('slash', TajoCortanteGlmcl)
	per.AddEventSound('mutilate', TajoMutilacionGlmcl)
	per.AddEventSound('crush', GolpeContundenteGlmcl)
	
	global AsignarSonidosGolem_clCalled
	if AsignarSonidosGolem_clCalled:
		return
	AsignarSonidosGolem_clCalled=1


	# Sonidos de animaciones
	
	
	per.AddAnimSound('Glm_g_01', EsfuerzoGlmcl1, 0.3790)
	per.AddAnimSound('Glm_g_01', SesgadoGlmcl1, 0.4000)
	per.AddAnimSound('Glm_g_12', SesgadoGlmcl2, 0.3880)
	per.AddAnimSound('Glm_g_12', EsfuerzoGlmcl2, 0.3050)
	per.AddAnimSound('Glm_g_21', SesgadoGlmcl3, 0.3440)
	per.AddAnimSound('Glm_g_21', EsfuerzoGlmcl3, 0.3000)
	per.AddAnimSound('Glm_g_31', SesgadoGlmcl4, 0.3000)
	per.AddAnimSound('Glm_g_31', EsfuerzoGlmcl4, 0.2840)
	per.AddAnimSound('Glm_g_31', caidagolemcl2, 0.3240)
	per.AddAnimSound('Glm_g_114', SesgadoGlmcl5, 0.4350)
	per.AddAnimSound('Glm_g_114', EsfuerzoGlmcl5, 0.2390)
	per.AddAnimSound('Glm_g_21_27', SesgadoGlmcl6, 0.2750)
	per.AddAnimSound('Glm_g_21_27', EsfuerzoGlmcl6, 0.2750)
	per.AddAnimSound('Glm_g_21_27', SesgadoGlmcl7, 0.5430)
	per.AddAnimSound('Glm_g_21_27', EsfuerzoGlmcl7, 0.5430)
	per.AddAnimSound('Glm_g_1tw', CreaPiedraGlmcl, 0.5430)
	
	per.AddAnimSound('Glm_dth0', caidagolemcl, 0.5000)
	per.AddAnimSound('Glm_dth0', MuerteGlmcl1, 0.1590)
	per.AddAnimSound('Glm_dth2', caidagolemcl, 0.7720)
	per.AddAnimSound('Glm_dth2', MuerteGlmcl1, 0.1590)
	per.AddAnimSound('Glm_dth_c1', caidagolemcl, 0.9150)
	per.AddAnimSound('Glm_dth_c1', caidagolemcl2, 0.6270)
	per.AddAnimSound('Glm_dth_c1', MuerteGlmcl1, 0.1590)
	per.AddAnimSound('Glm_dth_i1', caidagolemcl2, 0.5830)
	per.AddAnimSound('Glm_dth_i1', caidagolemcl3, 0.7020)
	per.AddAnimSound('Glm_dth_i1', MuerteGlmcl1, 0.1590)
	per.AddAnimSound('Glm_dth_i1', caidagolemcl2, 0.3630)
	per.AddAnimSound('Glm_dth_i1', caidagolemcl3, 0.6200)
	per.AddAnimSound('Glm_dth_i1', MuerteGlmcl1, 0.1590)


	per.AddAnimSound('Glm_hurt_big', HeridaGlmcl1, 0.2000)
	per.AddAnimSound('Glm_hurt_lite', HeridaGlmcl2, 0.2000)
	
	
	
	