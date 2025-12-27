import Bladex

# ***********************************
# *      Asignacion de sonidos      *
# ***********************************

AsignarSonidosTrollCalled=0
def AsignarSonidosTroll(Personaje):
	from AniSoundTrlX import *

	per=Bladex.GetEntity(Personaje)

	# Sonidos de eventos

	per.AddEventSound('shield_block', GolpeArmaEscudoTrl)
	per.AddEventSound('weapon_block', GolpeArmaArmaTrl)
	per.AddEventSound('impale', TajoEmpalanteTrl)
	per.AddEventSound('slash', TajoCortanteTrl)
	per.AddEventSound('mutilate', TajoMutilacionTrl)
	per.AddEventSound('crush', GolpeContundenteTrl)
	
	
	
	
	global AsignarSonidosTrollCalled
	if AsignarSonidosTrollCalled:
		return
	AsignarSonidosTrollCalled=1


	# Sonidos de animaciones
	
	
	
	per.AddAnimSound('Trl_g_01', EsfuerzoCorto1Trl, 0.4550)
	per.AddAnimSound('Trl_g_01', SesgadoCortoTrl, 0.4550)
	#per.AddAnimSound('Trl_g_01', RespiracionTrl5, 0.7000)
	per.AddAnimSound('Trl_g_01', MovimientoTrl1, 0.8500)
	per.AddAnimSound('Trl_g_02', EsfuerzoCortoTrl, 0.3500)
	per.AddAnimSound('Trl_g_02', SesgadoLargoGraveTrl, 0.3500)
	per.AddAnimSound('Trl_g_02', EsfuerzoCorto1Trl, 0.1000)
	per.AddAnimSound('Trl_g_02', MovimientoTrl2, 0.7500)
	#per.AddAnimSound('Trl_g_02', RespiracionTrl6, 0.8000)
	per.AddAnimSound('Trl_g_04', EsfuerzoGolpeArribaTrl, 0.3900)
	per.AddAnimSound('Trl_g_04', SesgadoCortoGraveTrl, 0.3900)
	#per.AddAnimSound('Trl_g_04', RespiracionTrl7, 0.3510)
	per.AddAnimSound('Trl_g_04', MovimientoTrl2, 0.7000)
	per.AddAnimSound('Trl_g_04', EsfuerzoGolpeLateralTrl, 0.1000)
	per.AddAnimSound('Trl_g_06', EsfuerzoCorto2Trl, 0.4350)
	per.AddAnimSound('Trl_g_06', SesgadoCortoTrl, 0.4350)
	#per.AddAnimSound('Trl_g_06', RespiracionTrl8, 0.7000)
	per.AddAnimSound('Trl_g_06', MovimientoTrl1, 0.8500)
	per.AddAnimSound('Trl_g_06', EsfuerzoCorto3Trl, 0.1100)
	per.AddAnimSound('Trl_g_12', EsfuerzoGolpeLateralTrl, 0.3300)
	per.AddAnimSound('Trl_g_12', SesgadoLargoGraveTrl, 0.3300)
	#per.AddAnimSound('Trl_g_12', RespiracionTrl5, 0.6000)
	per.AddAnimSound('Trl_g_12', MovimientoTrl2, 0.1000)
	per.AddAnimSound('Trl_g_12', EsfuerzoGolpeLateralTrl, 0.1100)
	per.AddAnimSound('Trl_g_18', EsfuerzoCorto3Trl, 0.2540)
	per.AddAnimSound('Trl_g_18', SesgadoLargoTrl, 0.2560)
	#per.AddAnimSound('Trl_g_18', RespiracionTrl6, 0.5000)
	per.AddAnimSound('Trl_g_18', MovimientoTrl1, 0.7000)
	per.AddAnimSound('Trl_g_19', EsfuerzoCorto1Trl, 0.4600)
	per.AddAnimSound('Trl_g_19', SesgadoCortoGraveTrl, 0.4600)
	#per.AddAnimSound('Trl_g_19', RespiracionTrl7, 0.6500)
	per.AddAnimSound('Trl_g_19', MovimientoTrl2, 0.8000)
	per.AddAnimSound('Trl_g_19', EsfuerzoCorto3Trl, 0.1000)
	per.AddAnimSound('Trl_g_31', EsfuerzoGolpeArribaTrl,0.2896)
	per.AddAnimSound('Trl_g_31', SesgadoLargoTrl, 0.3166)
	per.AddAnimSound('Trl_g_31', EsfuerzoGolpeArribaTrl,0.5300)
	per.AddAnimSound('Trl_g_31', SesgadoCortoGraveTrl, 0.5300)
	#per.AddAnimSound('Trl_g_31', RespiracionTrl8, 0.1370)
	per.AddAnimSound('Trl_g_31', MovimientoTrl2, 0.6000)
	
	#per.AddAnimSound('Trl_clmb_medlow_1h', EsfuerzoCorto1Trl, 0.1232)
	#per.AddAnimSound('Trl_clmb_medium_1h', EsfuerzoCorto2Trl, 0.1235)
	#per.AddAnimSound('Trl_clmb_high_1h', EsfuerzoCorto3Trl, 0.1235)
	#per.AddAnimSound('Trl_clmb_medlow_no', EsfuerzoCortoTrl, 0.1235)
	#per.AddAnimSound('Trl_clmb_medium_no', EsfuerzoCorto3Trl, 0.1235)
	#per.AddAnimSound('Trl_clmb_high_no', EsfuerzoCorto1Trl, 01.1235)
	#per.AddAnimSound('Trl_clmb_medium_1h', EsfuerzoCorto2Trl, 0.5621)
	#per.AddAnimSound('Trl_clmb_high_1h', EsfuerzoCorto1Trl, 0.2546)
	#per.AddAnimSound('Trl_clmb_high_1h', EsfuerzoCortoTrl, 0.5214)
	#per.AddAnimSound('Trl_clmb_medium_no', EsfuerzoCorto2Trl, 0.2365)
	#per.AddAnimSound('Trl_clmb_high_no', EsfuerzoCorto3Trl, 0.2354)
	#per.AddAnimSound('Trl_clmb_high_no', EsfuerzoCortoTrl, 0.6541)

	per.AddAnimSound("Trl_dth0", MuerteTrl2, 0.1200)
	per.AddAnimSound("Trl_dth0", MovimientoTrl1, 0.2000)
	per.AddAnimSound("Trl_dth0", MovimientoTrl2, 0.4000)
	per.AddAnimSound("Trl_dth0", MovimientoTrl1, 0.6000)
	per.AddAnimSound("Trl_dth0", MovimientoTrl2, 0.7500)
	per.AddAnimSound("Trl_dth0", CaidaTrl, 0.7700)
	per.AddAnimSound("Trl_dth_n00", MuerteTrl1, 1100)
	per.AddAnimSound("Trl_dth_n00", MovimientoTrl1, 0.2000)
	per.AddAnimSound("Trl_dth_n00", MovimientoTrl2, 0.4000)
	per.AddAnimSound("Trl_dth_n00", MovimientoTrl1, 0.6000)
	per.AddAnimSound("Trl_dth_n00", MovimientoTrl2, 0.7500)
	per.AddAnimSound("Trl_dth_n00", CaidaTrl, 0.3700)
	per.AddAnimSound("Trl_dth_n00", CaidaTrl, 0.6110)
	per.AddAnimSound("Trl_dth_n00", CaidaTrl, 0.6700)
	per.AddAnimSound("Trl_dth_n01", MuerteTrl2, 1100)
	per.AddAnimSound("Trl_dth_n01", MovimientoTrl1, 0.2000)
	per.AddAnimSound("Trl_dth_n01", MovimientoTrl2, 0.4000)
	per.AddAnimSound("Trl_dth_n01", MovimientoTrl1, 0.6000)
	per.AddAnimSound("Trl_dth_n01", MovimientoTrl2, 0.7500)
	per.AddAnimSound("Trl_dth_n01", CaidaTrl, 0.5200)
	per.AddAnimSound("Trl_dth_n01", CaidaTrl, 0.6200)
	per.AddAnimSound("Trl_dth_i1", MuerteTrl1, 0.1234)
	per.AddAnimSound("Trl_dth_bl1", MuerteTrl1, 0.2145)
	per.AddAnimSound("Trl_dth_c1", MovimientoTrl1, 0.2000)
	per.AddAnimSound("Trl_dth_c1", MovimientoTrl2, 0.4000)
	per.AddAnimSound("Trl_dth_c1", MovimientoTrl1, 0.6000)
	per.AddAnimSound("Trl_dth_c1", MovimientoTrl2, 0.7500)
	per.AddAnimSound("Trl_dth_c1", CaidaTrl, 0.5100)
	per.AddAnimSound("Trl_dth_c1", CaidaTrl, 0.7530)	
	per.AddAnimSound("Trl_dth_c2", MovimientoTrl1, 0.2000)
	per.AddAnimSound("Trl_dth_c2", MovimientoTrl2, 0.4000)
	per.AddAnimSound("Trl_dth_c2", MovimientoTrl1, 0.6000)
	per.AddAnimSound("Trl_dth_c2", MovimientoTrl2, 0.7500)
	per.AddAnimSound("Trl_dth_c2", CaidaTrl, 0.6430)
	per.AddAnimSound("Trl_dth_c2", CaidaTrl, 0.8800)
	per.AddAnimSound("Trl_dth_fll", GritoCaidaTrl, 0.1000)
	per.AddAnimSound("Trl_dth_fll2", GritoCaidaTrl, 0.1000)
	per.AddAnimSound("Trl_dth_burned", MuerteQuemandoTrl, 0.1100)

	per.AddAnimSound("Trl_hurt_jog", HeridaTrl1, 0.5714)
	per.AddAnimSound("Trl_hurt_neck", HeridaTrl2, 0.3158)
	per.AddAnimSound("Trl_hurt_breast", HeridaTrl3, 0.3889)
	per.AddAnimSound("Trl_hurt_back", HeridaTrl4, 0.4211)
	per.AddAnimSound("Trl_hurt_r_arm", HeridaTrl2, 0.4706)
	per.AddAnimSound("Trl_hurt_l_arm", HeridaTrl1, 0.5333)
	per.AddAnimSound("Trl_hurt_r_leg", HeridaTrl3, 0.4706)
	per.AddAnimSound("Trl_hurt_l_leg", HeridaTrl4, 0.4375)
	per.AddAnimSound("Trl_hurt_f_head", HeridaTrl2, 0.3333)
	per.AddAnimSound("Trl_hurt_f_neck", HeridaTrl2, 0.3158)
	per.AddAnimSound("Trl_hurt_f_breast", HeridaTrl2, 0.0980)
	per.AddAnimSound("Trl_hurt_f_back", HeridaTrl3, 0.1282)
	per.AddAnimSound("Trl_hurt_f_r_arm", HeridaTrl1, 0.2000)
	per.AddAnimSound("Trl_hurt_f_l_arm", HeridaTrl2, 0.1786)
	per.AddAnimSound("Trl_hurt_f_r_leg", HeridaTrl4, 0.1351)
	per.AddAnimSound("Trl_hurt_f_l_leg", HeridaTrl2, 0.2857)
	per.AddAnimSound("Trl_hurt_f_lite", HeridaTrl2, 0.3000)
	per.AddAnimSound("Trl_hurt_f_big", HeridaTrl1, 0.3000)
	per.AddAnimSound("Trl_hurt_head", HeridaTrl2, 0.6000)
	
	per.AddAnimSound("Trl_rlx_1h", RespiracionTrl1, 0.3000)
	per.AddAnimSound("Trl_rlx_1h", RespiracionTrl2, 0.6000)
	#per.AddAnimSound("Trl_rlx_1h", RespiracionTrl7, 0.7250)
	#per.AddAnimSound("Trl_rlx_1h", RespiracionTrl8, 0.9000)
	
	per.AddAnimSound("Trl_rlx_1h", MovimientoTrl1, 0.1500)
	per.AddAnimSound("Trl_rlx_1h", MovimientoTrl2, 0.4000)
	per.AddAnimSound("Trl_rlx_1h", MovimientoTrl1, 0.6000)
	per.AddAnimSound("Trl_rlx_1h", MovimientoTrl2, 0.8000)
	
	per.AddAnimSound("Trl_wlk_no", EsfuerzoCorto3Trl, 0.2500)
	#per.AddAnimSound("Trl_wlk_no", RespiracionTrl6, 0.5000)
	#per.AddAnimSound("Trl_wlk_no", RespiracionTrl7, 0.7250)
	#per.AddAnimSound("Trl_wlk_no", RespiracionTrl8, 0.9000)
	
	per.AddAnimSound("Trl_wlk_no", MovimientoTrl1, 0.1500)
	per.AddAnimSound("Trl_wlk_no", MovimientoTrl2, 0.4000)
	per.AddAnimSound("Trl_wlk_no", MovimientoTrl1, 0.6000)
	per.AddAnimSound("Trl_wlk_no", MovimientoTrl2, 0.8000)
	
	per.AddAnimSound("Trl_wbk_no", EsfuerzoCorto2Trl, 0.2500)
	#per.AddAnimSound("Trl_wbk_no", RespiracionTrl6, 0.5000)
	#per.AddAnimSound("Trl_wbk_no", RespiracionTrl7, 0.7250)
	#per.AddAnimSound("Trl_wbk_no", RespiracionTrl8, 0.9000)
	
	per.AddAnimSound("Trl_wbk_no", MovimientoTrl1, 0.1500)
	per.AddAnimSound("Trl_wbk_no", MovimientoTrl2, 0.4000)
	per.AddAnimSound("Trl_wbk_no", MovimientoTrl1, 0.6000)
	per.AddAnimSound("Trl_wbk_no", MovimientoTrl2, 0.8000)
	
	per.AddAnimSound("Trl_rlx_no", RespiracionTrl1, 0.3000)
	per.AddAnimSound("Trl_rlx_no", RespiracionTrl2, 0.6000)
	#per.AddAnimSound("Trl_rlx_no", RespiracionTrl7, 0.7250)
	#per.AddAnimSound("Trl_rlx_no", RespiracionTrl8, 0.9000)
	
	per.AddAnimSound("Trl_rlx_no", MovimientoTrl1, 0.1500)
	per.AddAnimSound("Trl_rlx_no", MovimientoTrl2, 0.4000)
	per.AddAnimSound("Trl_rlx_no", MovimientoTrl1, 0.6000)
	per.AddAnimSound("Trl_rlx_no", MovimientoTrl2, 0.8000)
	
	per.AddAnimSound("Trl_attack_f", EsfuerzoGolpeArribaTrl, 0.2500)
	#per.AddAnimSound("Trl_attack_f", RespiracionTrl2, 0.5000)
	#per.AddAnimSound("Trl_attack_f", RespiracionTrl3, 0.7500)
	#per.AddAnimSound("Trl_attack_f", RespiracionTrl4, 0.9000)
	per.AddAnimSound("Trl_attack_b", EsfuerzoCorto3Trl, 0.2500)
	#per.AddAnimSound("Trl_attack_b", RespiracionTrl2, 0.5000)
	#per.AddAnimSound("Trl_attack_b", RespiracionTrl3, 0.7250)
	#per.AddAnimSound("Trl_attack_b", RespiracionTrl4, 0.9000)
	
	per.AddAnimSound("Trl_attack_f", MovimientoTrl1, 0.1500)
	per.AddAnimSound("Trl_attack_f", MovimientoTrl2, 0.4000)
	per.AddAnimSound("Trl_attack_f", MovimientoTrl1, 0.6000)
	per.AddAnimSound("Trl_attack_f", MovimientoTrl2, 0.8000)
	per.AddAnimSound("Trl_attack_b", MovimientoTrl1, 0.1500)
	per.AddAnimSound("Trl_attack_b", MovimientoTrl2, 0.4000)
	per.AddAnimSound("Trl_attack_b", MovimientoTrl1, 0.6000)
	per.AddAnimSound("Trl_attack_b", MovimientoTrl2, 0.8000)
	
	
	per.AddAnimSound("Trl_jog_no", EsfuerzoGolpeArribaTrl, 0.2500)
	#per.AddAnimSound("Trl_jog_no", RespiracionTrl2, 0.5000)
	#per.AddAnimSound("Trl_jog_no", RespiracionTrl3, 0.7500)
	#per.AddAnimSound("Trl_jog_no", RespiracionTrl4, 0.9000)
	per.AddAnimSound("Trl_jog_1h", EsfuerzoGolpeLateralTrl, 0.2500)
	#per.AddAnimSound("Trl_jog_1h", RespiracionTrl2, 0.4900)
	#per.AddAnimSound("Trl_jog_1h", RespiracionTrl3, 0.7250)
	#per.AddAnimSound("Trl_jog_1h", RespiracionTrl4, 0.9000)
	per.AddAnimSound("Trl_jog_2o", EsfuerzoCorto3Trl, 0.2500)
	#per.AddAnimSound("Trl_jog_2o", RespiracionTrl2, 0.5000)
	#per.AddAnimSound("Trl_jog_2o", RespiracionTrl3, 0.7250)
	#per.AddAnimSound("Trl_jog_2o", RespiracionTrl4, 0.9000)
	
	
	per.AddAnimSound("Trl_jog_no", MovimientoTrl1, 0.1500)
	per.AddAnimSound("Trl_jog_no", MovimientoTrl2, 0.4000)
	per.AddAnimSound("Trl_jog_no", MovimientoTrl1, 0.6000)
	per.AddAnimSound("Trl_jog_no", MovimientoTrl2, 0.8000)
	per.AddAnimSound("Trl_jog_1h", MovimientoTrl1, 0.1500)
	per.AddAnimSound("Trl_jog_1h", MovimientoTrl2, 0.4000)
	per.AddAnimSound("Trl_jog_1h", MovimientoTrl1, 0.6000)
	per.AddAnimSound("Trl_jog_1h", MovimientoTrl2, 0.8000)
	per.AddAnimSound("Trl_jog_2o", MovimientoTrl1, 0.1500)
	per.AddAnimSound("Trl_jog_2o", MovimientoTrl2, 0.4000)
	per.AddAnimSound("Trl_jog_2o", MovimientoTrl1, 0.6000)
	per.AddAnimSound("Trl_jog_2o", MovimientoTrl2, 0.8000)





