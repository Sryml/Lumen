import Bladex

# ***********************************
# *      Asignacion de sonidos      *
# ***********************************

AsignarSonidosDalGurakCalled=0
def AsignarSonidosDalGurak(Personaje):

	from AniSoundDgkX import *
	
	per=Bladex.GetEntity(Personaje)

	# Sonidos de eventos

	per.AddEventSound('shield_block', GolpeArmaEscudoDgk)
	per.AddEventSound('weapon_block', GolpeArmaArmaDgk)
	per.AddEventSound('impale', TajoEmpalanteDgk)
	per.AddEventSound('slash', TajoCortanteDgk)
	per.AddEventSound('mutilate', TajoMutilacionDgk)
	per.AddEventSound('crush', GolpeContundenteDgk)
	
	
	global AsignarSonidosDalGurakCalled
	if AsignarSonidosDalGurakCalled:
		return
	AsignarSonidosDalGurakCalled=1



	# Sonidos de animaciones	
	
	per.AddAnimSound('Dgk_df_02',EsfuerzoCorto1Dgk,0.1150)
	
	per.AddAnimSound('Dgk_g_07_new',RespiracionDgk1,0.1200)
	per.AddAnimSound('Dgk_g_07_new',RespiracionDgk2,0.4000)
	per.AddAnimSound('Dgk_g_07_new',RespiracionDgk1,0.6000)
	per.AddAnimSound('Dgk_g_07_new',RespiracionDgk2,0.8000)
	per.AddAnimSound('Dgk_g_07_new',EsfuerzoCorto1Dgk,0.2500)
	per.AddAnimSound('Dgk_g_07_new',SesgadoCortoAgudo,0.2700)
	per.AddAnimSound('Dgk_g_08_new',EsfuerzoCorto2Dgk,0.1550)
	per.AddAnimSound('Dgk_g_08_new',SesgadoCortoGrave,0.1550)
	per.AddAnimSound('Dgk_g_08_new',RespiracionDgk1,0.2500)
	per.AddAnimSound('Dgk_g_08_new',RespiracionDgk2,0.4000)
	per.AddAnimSound('Dgk_g_08_new',RespiracionDgk1,0.6000)
	per.AddAnimSound('Dgk_g_08_new',RespiracionDgk2,0.8000)
	per.AddAnimSound('Dgk_g_02_new',EsfuerzoCorto3Dgk,0.2500)
	per.AddAnimSound('Dgk_g_02_new',SesgadoCorto,0.2950)
	per.AddAnimSound('Dgk_g_02_new',RespiracionDgk1,0.4000)
	per.AddAnimSound('Dgk_g_02_new',RespiracionDgk2,0.6000)
	per.AddAnimSound('Dgk_g_02_new',RespiracionDgk1,0.8000)
	per.AddAnimSound('Dgk_g_01_new',EsfuerzoCorto1Dgk,0.2950)
	per.AddAnimSound('Dgk_g_01_new',SesgadoLargo,0.2950)
	per.AddAnimSound('Dgk_g_01_new',RespiracionDgk1,0.1500)
	per.AddAnimSound('Dgk_g_01_new',RespiracionDgk2,0.4000)
	per.AddAnimSound('Dgk_g_01_new',RespiracionDgk1,0.6000)
	per.AddAnimSound('Dgk_g_01_new',RespiracionDgk2,0.8000)
	per.AddAnimSound('Dgk_g_22lowkata_new',SesgadoLargoAgudo,0.1320)
	per.AddAnimSound('Dgk_g_22lowkata_new',SesgadoLargo,0.3570)
	per.AddAnimSound('Dgk_g_22lowkata_new',EsfuerzoGolpeLateralDgk,0.1200)
	per.AddAnimSound('Dgk_g_22lowkata_new',RespiracionDgk1,0.4000)
	per.AddAnimSound('Dgk_g_22lowkata_new',RespiracionDgk2,0.6000)
	per.AddAnimSound('Dgk_g_22lowkata_new',RespiracionDgk1,0.8000)
	per.AddAnimSound('Dgk_g_19_bs1_new',SesgadoLargoGrave,0.2650)
	per.AddAnimSound('Dgk_g_19_bs1_new',SesgadoCorto,0.4810)
	per.AddAnimSound('Dgk_g_19_bs1_new',EsfuerzoCorto4Dgk,0.4810)
	per.AddAnimSound('Dgk_g_19_bs1_new',EsfuerzoGolpeArribaDgk,0.1423)
	per.AddAnimSound('Dgk_g_19_bs1_new',RespiracionDgk1,0.6000)
	per.AddAnimSound('Dgk_g_19_bs1_new',RespiracionDgk2,0.8000)
	per.AddAnimSound('Dgk_g_21_6_s8new',SesgadoCorto,0.1000)
	per.AddAnimSound('Dgk_g_21_6_s8new',SesgadoCortoAgudo,0.1780)
	per.AddAnimSound('Dgk_g_21_6_s8new',SesgadoCorto,0.3250)
	per.AddAnimSound('Dgk_g_21_6_s8new',SesgadoCortoAgudo,0.5900)
	per.AddAnimSound('Dgk_g_21_6_s8new',EsfuerzoCorto2Dgk,0.1500)
	per.AddAnimSound('Dgk_g_21_6_s8new',EsfuerzoGolpeArribaDgk,0.3200)
	per.AddAnimSound('Dgk_g_21_6_s8new',EsfuerzoGolpeLateralDgk,0.4810)
	per.AddAnimSound('Dgk_g_21_6_s8new',RespiracionDgk1,0.6000)
	per.AddAnimSound('Dgk_g_21_6_s8new',RespiracionDgk1,0.8000)
	per.AddAnimSound('Dgk_g_29_3new',EsfuerzoCorto4Dgk,0.2800)
	per.AddAnimSound('Dgk_g_29_3new',EsfuerzoGolpeArribaDgk,0.4200)
	per.AddAnimSound('Dgk_g_29_3new',SesgadoLargoGrave,0.2900)
	per.AddAnimSound('Dgk_g_29_3new',SesgadoLargoAgudo,0.4710)
	per.AddAnimSound('Dgk_g_29_3new',RespiracionDgk1,0.6000)
	per.AddAnimSound('Dgk_g_29_3new',RespiracionDgk2,0.8000)
	
	
	per.AddAnimSound('Dgk_g_01_7_new',EsfuerzoCorto4Dgk,0.1800)
	per.AddAnimSound('Dgk_g_01_7_new',EsfuerzoGolpeArribaDgk,0.4160)
	per.AddAnimSound('Dgk_g_01_7_new',SesgadoLargoGrave,0.1850)
	per.AddAnimSound('Dgk_g_01_7_new',SesgadoLargoAgudo,0.4160)
	per.AddAnimSound('Dgk_g_01_7_new',RespiracionDgk1,0.7000)
	per.AddAnimSound('Dgk_g_01_7_new',RespiracionDgk2,0.9000)
	per.AddAnimSound('Dgk_g_back',SesgadoCorto,0.1700)
	per.AddAnimSound('Dgk_g_back',SesgadoLargoAgudo,0.4110)
	per.AddAnimSound('Dgk_g_back',EsfuerzoGolpeLateralDgk,0.4110)
	per.AddAnimSound('Dgk_g_back',RespiracionDgk1,0.1200)
	per.AddAnimSound('Dgk_g_back',RespiracionDgk2,0.3000)
	per.AddAnimSound('Dgk_g_back',RespiracionDgk2,0.6000)
	per.AddAnimSound('Dgk_g_back',RespiracionDgk2,0.8000)
	per.AddAnimSound('Dgk_g_m01',RespiracionDgk1,0.1200)
	per.AddAnimSound('Dgk_g_m01',RespiracionDgk2,0.4000)
	per.AddAnimSound('Dgk_g_m01',RespiracionDgk2,0.6000)
	per.AddAnimSound('Dgk_g_m01',RespiracionDgk2,0.8000)
	per.AddAnimSound('Dgk_g_m01',EsfuerzoCorto3Dgk,0.2350)
	per.AddAnimSound('Dgk_g_m01',SesgadoLargoGrave,0.5500)
	per.AddAnimSound('Dgk_g_m01',EsfuerzoGolpeArribaDgk,0.4780)
	per.AddAnimSound('Dgk_g_m02',EsfuerzoCorto1Dgk,0.2500)
	per.AddAnimSound('Dgk_g_m02',SesgadoLargoAgudo,0.3000)
	per.AddAnimSound('Dgk_g_m02',RespiracionDgk1,0.1500)
	per.AddAnimSound('Dgk_g_m02',RespiracionDgk2,0.4000)
	per.AddAnimSound('Dgk_g_m02',RespiracionDgk1,0.6000)
	per.AddAnimSound('Dgk_g_m02',RespiracionDgk1,0.8000)
	
	
	
	per.AddAnimSound('Dgk_g_b32kata_new',SesgadoCorto,0.1000)
	per.AddAnimSound('Dgk_g_b32kata_new',SesgadoLargoAgudo,0.3000)
	per.AddAnimSound('Dgk_g_b32kata_new',SesgadoLargo,0.5860)
	per.AddAnimSound('Dgk_g_b32kata_new',EsfuerzoCorto1Dgk,0.2800)
	per.AddAnimSound('Dgk_g_b32kata_new',EsfuerzoCorto2Dgk,0.5500)
	per.AddAnimSound('Dgk_g_b32kata_new',EsfuerzoGolpeLateralDgk,0.1500)
	per.AddAnimSound('Dgk_g_b32kata_new',RespiracionDgk1,0.4000)
	per.AddAnimSound('Dgk_g_b32kata_new',RespiracionDgk2,0.6000)
	per.AddAnimSound('Dgk_g_b32kata_new',RespiracionDgk1,0.8000)
	
	
	per.AddAnimSound('Dgk_attack_b',RespiracionDgk1,0.2000)
	per.AddAnimSound('Dgk_attack_b',RespiracionDgk2,0.4000)
	per.AddAnimSound('Dgk_attack_b',RespiracionDgk1,0.6000)
	per.AddAnimSound('Dgk_attack_b',RespiracionDgk2,0.8000)
	per.AddAnimSound('Dgk_attack_b_s',RespiracionDgk1,0.2000)
	per.AddAnimSound('Dgk_attack_b_s',RespiracionDgk2,0.4000)
	per.AddAnimSound('Dgk_attack_b_s',RespiracionDgk1,0.6000)
	per.AddAnimSound('Dgk_attack_b_s',RespiracionDgk2,0.8000)
	per.AddAnimSound('Dgk_attack_f',RespiracionDgk1,0.2000)
	per.AddAnimSound('Dgk_attack_f',RespiracionDgk2,0.4000)
	per.AddAnimSound('Dgk_attack_f',RespiracionDgk1,0.6000)
	per.AddAnimSound('Dgk_attack_f',RespiracionDgk2,0.8000)
	per.AddAnimSound('Dgk_attack_f_s',RespiracionDgk1,0.2000)
	per.AddAnimSound('Dgk_attack_f_s',RespiracionDgk2,0.4000)
	per.AddAnimSound('Dgk_attack_f_s',RespiracionDgk1,0.6000)
	per.AddAnimSound('Dgk_attack_f_s',RespiracionDgk2,0.8000)
	per.AddAnimSound('Dgk_attack_l',RespiracionDgk1,0.2000)
	per.AddAnimSound('Dgk_attack_l',RespiracionDgk2,0.4000)
	per.AddAnimSound('Dgk_attack_l',RespiracionDgk1,0.6000)
	per.AddAnimSound('Dgk_attack_l',RespiracionDgk2,0.8000)
	per.AddAnimSound('Dgk_attack_l_s',RespiracionDgk1,0.2000)
	per.AddAnimSound('Dgk_attack_l_s',RespiracionDgk2,0.4000)
	per.AddAnimSound('Dgk_attack_l_s',RespiracionDgk1,0.6000)
	per.AddAnimSound('Dgk_attack_l_s',RespiracionDgk2,0.8000)
	per.AddAnimSound('Dgk_attack_r',RespiracionDgk1,0.2000)
	per.AddAnimSound('Dgk_attack_r',RespiracionDgk2,0.4000)
	per.AddAnimSound('Dgk_attack_r',RespiracionDgk1,0.6000)
	per.AddAnimSound('Dgk_attack_r',RespiracionDgk2,0.8000)
	per.AddAnimSound('Dgk_attack_r_s',RespiracionDgk1,0.2000)
	per.AddAnimSound('Dgk_attack_r_s',RespiracionDgk2,0.4000)
	per.AddAnimSound('Dgk_attack_r_s',RespiracionDgk1,0.6000)
	per.AddAnimSound('Dgk_attack_r_s',RespiracionDgk2,0.8000)
	
	per.AddAnimSound('Dgk_catch',EsfuerzoCorto4Dgk,0.3300)
	
	per.AddAnimSound('Dgk_rlx_1h',RespiracionDgk1,0.2000)
	per.AddAnimSound('Dgk_rlx_1h',RespiracionDgk2,0.4000)
	per.AddAnimSound('Dgk_rlx_1h',RespiracionDgk1,0.6000)
	per.AddAnimSound('Dgk_rlx_1h',RespiracionDgk2,0.8000)
	per.AddAnimSound('Dgk_rlx_1',RespiracionDgk1,0.2000)
	per.AddAnimSound('Dgk_rlx_1',RespiracionDgk2,0.4000)
	per.AddAnimSound('Dgk_rlx_1',RespiracionDgk1,0.6000)
	per.AddAnimSound('Dgk_rlx_1',RespiracionDgk2,0.8000)
	per.AddAnimSound('Dgk_rlx_s',RespiracionDgk1,0.2000)
	per.AddAnimSound('Dgk_rlx_s',RespiracionDgk2,0.4000)
	per.AddAnimSound('Dgk_rlx_s',RespiracionDgk1,0.6000)
	per.AddAnimSound('Dgk_rlx_s',RespiracionDgk2,0.8000)
	
	per.AddAnimSound('Dgk_dth0',MuerteDgk,0.1000)
	
	per.AddAnimSound('Dgk_lifeup1',VidaDgk,0.3300)
	
	per.AddAnimSound('Dgk_hurt_back',Herida1Dgk,0.1100)
	per.AddAnimSound('Dgk_hurt_big',Herida2Dgk,0.1100)
	per.AddAnimSound('Dgk_hurt_chest',Herida3Dgk,0.1100)
	per.AddAnimSound('Dgk_hurt_lite',Herida1Dgk,0.1100)
	per.AddAnimSound('Dgk_hurt_back',Herida2Dgk,0.1100)
	per.AddAnimSound('Dgk_hurt_l_arm',Herida3Dgk,0.1100)
	per.AddAnimSound('Dgk_hurt_l_leg',Herida1Dgk,0.1100)
	per.AddAnimSound('Dgk_hurt_r_arm',Herida2Dgk,0.1100)
	per.AddAnimSound('Dgk_hurt_r_leg',Herida3Dgk,0.1100)
	
	
	per.AddAnimSound('Dgk_g_d_r',Herida2Dgk, 0.2100)
	per.AddAnimSound('Dgk_g_d_r',EsfuerzoCorto2Dgk, 0.6000)
	per.AddAnimSound('Dgk_g_d_l',Herida2Dgk, 0.2100)
	per.AddAnimSound('Dgk_g_d_l',EsfuerzoCorto2Dgk, 0.6000)
	
	
	
	
	
	








