import Bladex


# ***********************************
# *      Asignacion de sonidos      *
# ***********************************
AsignarSonidosVampiroCalled=0
def AsignarSonidosVampiro(Personaje):
	
	from AniSoundVmpX import *
	per=Bladex.GetEntity(Personaje)

	# Sonidos de eventos

	per.AddEventSound('shield_block', GolpeArmaEscudoVmp)
	per.AddEventSound('weapon_block', GolpeArmaArmaVmp)
	per.AddEventSound('impale', TajoEmpalanteVmp)
	per.AddEventSound('slash', TajoCortanteVmp)
	per.AddEventSound('mutilate', TajoMutilacionVmp)
	per.AddEventSound('crush', GolpeContundenteVmp)
	
	global AsignarSonidosVampiroCalled
	if AsignarSonidosVampiroCalled:
		return
	AsignarSonidosVampiroCalled=1
		






	# Sonidos de animaciones

	
	per.AddAnimSound('Vmp_chg_r', Enfundar, 0.3000)
	per.AddAnimSound('Vmp_chg_r_l', Enfundar, 3500)
	per.AddAnimSound('Vmp_attack_chg_r_l', Enfundar,0.3000)
	per.AddAnimSound('Vmp_attack_chg_r', Enfundar, 0.3000)
	per.AddAnimSound('Vmp_chg_r', Enfundar,0.3599)
	per.AddAnimSound('Vmp_chg_r_l', Enfundar, 3000)
	per.AddAnimSound('Vmp_attack_chg_r_l', Enfundar, 0.3000)
	per.AddAnimSound('Vmp_attack_chg_r', Enfundar, 0.3000)

	per.AddAnimSound('Vmp_g_01', EsfuerzoCortoVmp, 0.2500)
	per.AddAnimSound('Vmp_g_01', RespiracionVmp1, 0.6000)
	per.AddAnimSound('Vmp_g_01', RoceVmp2, 0.2000)
	per.AddAnimSound('Vmp_g_01', RoceVmp1, 0.4000)
	per.AddAnimSound('Vmp_g_01', RoceVmp2, 0.6000)
	per.AddAnimSound('Vmp_g_01', RoceVmp1, 0.8000)
	per.AddAnimSound('Vmp_g_06', EsfuerzoCorto3Vmp, 0.3500)
	per.AddAnimSound('Vmp_g_06', AguadoVmp2, 0.6000)
	per.AddAnimSound('Vmp_g_06', RoceVmp1, 0.2000)
	per.AddAnimSound('Vmp_g_06', RoceVmp2, 0.4000)
	per.AddAnimSound('Vmp_g_06', RoceVmp1, 0.7000)
	per.AddAnimSound('Vmp_g_06', RoceVmp2, 0.9000)
	per.AddAnimSound('Vmp_g_07', EsfuerzoCorto2Vmp, 0.2500)
	per.AddAnimSound('Vmp_g_07', RespiracionVmp3, 0.5000)
	per.AddAnimSound('Vmp_g_07', RoceVmp1, 0.2000)
	per.AddAnimSound('Vmp_g_07', RoceVmp2, 0.4000)
	per.AddAnimSound('Vmp_g_07', RoceVmp1, 0.6000)
	per.AddAnimSound('Vmp_g_07', RoceVmp2, 0.8000)
	per.AddAnimSound('Vmp_g_01', SesgadoCorto, 0.3117)
	per.AddAnimSound('Vmp_g_06', SesgadoCorto, 0.4342)
	per.AddAnimSound('Vmp_g_07', SesgadoCortoAgudo, 0.3291)
	per.AddAnimSound('Vmp_g_26', EsfuerzoCorto1Vmp, 0.1720)
	per.AddAnimSound('Vmp_g_26', SesgadoLargoAgudo, 0.2700)
	per.AddAnimSound('Vmp_g_26', AguadoVmp1, 0.6000)
	per.AddAnimSound('Vmp_g_26', RoceVmp1, 0.3000)
	per.AddAnimSound('Vmp_g_26', RoceVmp2, 0.5000)
	per.AddAnimSound('Vmp_g_26', RoceVmp1, 0.7000)
	per.AddAnimSound('Vmp_g_26', RoceVmp1, 0.9000)
	
	per.AddAnimSound('Vmp_disappear', DesapareceVmp, 0.1780)
	per.AddAnimSound('Vmp_disappear', EsfuerzoCorto2Vmp, 0.4650)
	per.AddAnimSound('Vmp_disappear', SesgadoLargoAgudo, 0.4750)
	per.AddAnimSound('Vmp_disappear', RoceVmp1, 0.5000)
	per.AddAnimSound('Vmp_disappear', RoceVmp2, 0.7000)
	per.AddAnimSound('Vmp_disappear', RoceVmp1, 0.9000)
	per.AddAnimSound('Vmp_disappear', RespiracionVmp2, 0.6000)
	
	

	per.AddAnimSound("Vmp_dth0", MuerteVmp1, 0.2000)
	per.AddAnimSound("Vmp_dth0", RoceVmp1, 0.1450)
	per.AddAnimSound("Vmp_dth0", RoceVmp2, 0.2350)
	per.AddAnimSound("Vmp_dth0", RoceVmp1, 0.3150)
	per.AddAnimSound("Vmp_dth0", RoceVmp2, 0.4670)
	per.AddAnimSound("Vmp_dth0", RoceVmp1, 0.8000)
	per.AddAnimSound("Vmp_dth0", RespiracionVmp3, 0.5000)
	per.AddAnimSound("Vmp_dth0", AguadoVmp3, 0.7000)
	per.AddAnimSound("Vmp_dth0", CaidaVmp1, 0.5750)
	per.AddAnimSound("Vmp_dth0", CaidaVmp2, 0.6190)
	
	per.AddAnimSound("Vmp_hurt_f_lite", HeridaVmp2, 0.3000)
	per.AddAnimSound("Vmp_hurt_f_lite", RoceVmp1, 0.1200)
	per.AddAnimSound("Vmp_hurt_f_lite", RoceVmp2, 0.3000)
	per.AddAnimSound("Vmp_hurt_f_lite", RoceVmp1, 0.5000)
	per.AddAnimSound("Vmp_hurt_f_lite", RoceVmp2, 0.7000)
	per.AddAnimSound("Vmp_hurt_f_lite", RoceVmp1, 0.9000)
	per.AddAnimSound("Vmp_hurt_f_lite", RespiracionVmp3, 0.5000)
	
	per.AddAnimSound("Vmp_hurt_f_big", HeridaVmp2, 0.3000)
	per.AddAnimSound("Vmp_hurt_f_big", RoceVmp1, 0.1200)
	per.AddAnimSound("Vmp_hurt_f_big", RoceVmp2, 0.3000)
	per.AddAnimSound("Vmp_hurt_f_big", RoceVmp1, 0.5000)
	per.AddAnimSound("Vmp_hurt_f_big", RoceVmp2, 0.7000)
	per.AddAnimSound("Vmp_hurt_f_big", RoceVmp1, 0.9000)
	per.AddAnimSound("Vmp_hurt_f_big", RespiracionVmp1, 0.5000)

	per.AddAnimSound("Vmp_attack_f", RespiracionVmp1, 0.1100)
	per.AddAnimSound("Vmp_attack_f", RespiracionVmp2, 0.6000)

	per.AddAnimSound("Vmp_attack_f", RoceVmp1, 0.1100)
	per.AddAnimSound("Vmp_attack_f", RoceVmp2, 0.3100)
	per.AddAnimSound("Vmp_attack_f", RoceVmp1, 0.5100)
	per.AddAnimSound("Vmp_attack_f", RoceVmp2, 0.7100)
	per.AddAnimSound("Vmp_attack_f", RoceVmp1, 0.9000)
	
	per.AddAnimSound("Vmp_attack_f_s", RespiracionVmp4, 0.1100)
	per.AddAnimSound("Vmp_attack_f_s", RespiracionVmp3, 0.6000)
	
	per.AddAnimSound("Vmp_attack_f_s", RoceVmp1, 0.1100)
	per.AddAnimSound("Vmp_attack_f_s", RoceVmp2, 0.3100)
	per.AddAnimSound("Vmp_attack_f_s", RoceVmp1, 0.5100)
	per.AddAnimSound("Vmp_attack_f_s", RoceVmp2, 0.7100)
	per.AddAnimSound("Vmp_attack_f_s", RoceVmp1, 0.9000)
	
	per.AddAnimSound("Vmp_attack_b", RespiracionVmp1, 0.1100)
	per.AddAnimSound("Vmp_attack_b", RespiracionVmp2, 0.6000)
	
	per.AddAnimSound("Vmp_attack_b", RoceVmp1, 0.1100)
	per.AddAnimSound("Vmp_attack_b", RoceVmp2, 0.3100)
	per.AddAnimSound("Vmp_attack_b", RoceVmp1, 0.5100)
	per.AddAnimSound("Vmp_attack_b", RoceVmp2, 0.7100)
	per.AddAnimSound("Vmp_attack_b", RoceVmp1, 0.9000)
	
	per.AddAnimSound("Vmp_attack_b_s", RespiracionVmp4, 0.1100)
	per.AddAnimSound("Vmp_attack_b_s", RespiracionVmp3, 0.6000)
	
	per.AddAnimSound("Vmp_attack_b_s", RoceVmp1, 0.1100)
	per.AddAnimSound("Vmp_attack_b_s", RoceVmp2, 0.3100)
	per.AddAnimSound("Vmp_attack_b_s", RoceVmp1, 0.5100)
	per.AddAnimSound("Vmp_attack_b_s", RoceVmp2, 0.7100)
	per.AddAnimSound("Vmp_attack_b_s", RoceVmp1, 0.9000)
	
	per.AddAnimSound("Vmp_attack_r", RespiracionVmp1, 0.1100)
	per.AddAnimSound("Vmp_attack_r", RespiracionVmp2, 0.6000)

	per.AddAnimSound("Vmp_attack_r", RoceVmp1, 0.1100)
	per.AddAnimSound("Vmp_attack_r", RoceVmp2, 0.3000)
	per.AddAnimSound("Vmp_attack_r", RoceVmp1, 0.5000)
	per.AddAnimSound("Vmp_attack_r", RoceVmp2, 0.7000)
	per.AddAnimSound("Vmp_attack_r", RoceVmp1, 0.9000)
	
	per.AddAnimSound("Vmp_attack_r_s", RespiracionVmp4, 0.1100)
	per.AddAnimSound("Vmp_attack_r_s", RespiracionVmp3, 0.6000)
	
	per.AddAnimSound("Vmp_attack_r_s", RoceVmp1, 0.1100)
	per.AddAnimSound("Vmp_attack_r_s", RoceVmp2, 0.3000)
	per.AddAnimSound("Vmp_attack_r_s", RoceVmp1, 0.5000)
	per.AddAnimSound("Vmp_attack_r_s", RoceVmp2, 0.7000)
	per.AddAnimSound("Vmp_attack_r_s", RoceVmp1, 0.9000)
	
	per.AddAnimSound("Vmp_attack_l", RespiracionVmp1, 0.1100)
	per.AddAnimSound("Vmp_attack_l", RespiracionVmp2, 0.6000)
	
	per.AddAnimSound("Vmp_attack_l", RoceVmp1, 0.1100)
	per.AddAnimSound("Vmp_attack_l", RoceVmp2, 0.3000)
	per.AddAnimSound("Vmp_attack_l", RoceVmp1, 0.5000)
	per.AddAnimSound("Vmp_attack_l", RoceVmp2, 0.7000)
	per.AddAnimSound("Vmp_attack_l", RoceVmp1, 0.9000)
	
	
	per.AddAnimSound("Vmp_attack_l_s", RespiracionVmp4, 0.1100)
	per.AddAnimSound("Vmp_attack_l_s", RespiracionVmp3, 0.6000)
	
	
	per.AddAnimSound("Vmp_attack_l_s", RoceVmp1, 0.1100)
	per.AddAnimSound("Vmp_attack_l_s", RoceVmp2, 0.3000)
	per.AddAnimSound("Vmp_attack_l_s", RoceVmp1, 0.5000)
	per.AddAnimSound("Vmp_attack_l_s", RoceVmp2, 0.7000)
	per.AddAnimSound("Vmp_attack_l_s", RoceVmp1, 0.9000)
	
	per.AddAnimSound("Vmp_rlx_f", RespiracionVmp1, 0.1100)
	per.AddAnimSound("Vmp_rlx_f", RespiracionVmp2, 0.6000)
	
	per.AddAnimSound("Vmp_insult", InsultoVmp, 0.1100)
	
	

	
