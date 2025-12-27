import Bladex

#import AnimationSets


#AnimationSets.LoadGokAnimationSet("Gok")

####################################################################################
#
# Escalar + saltos
#
####################################################################################

Bladex.AddBipedAction("Gok","clmb_low_1h","Gok_clmb_low_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Gok","clmb_medlow_1h","Gok_clmb_low_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Gok","clmb_medium_1h","Gok_clmb_medium_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Gok","clmb_high_1h","Gok_clmb_medium_1h",0.0,1.0,0)	

#Bladex.AddBipedAction("Gok","LongJump1H","Gok_jmp_1h",0.0,1.0,0)	
#Bladex.AddBipedAction("Gok","LongJumpNo","Gok_jmp_1h",0.0,1.0,0)	
#Bladex.AddBipedAction("Gok","ShortJump","Gok_jmp_1h",0.0,1.0,0)	



####################################################################################
#
# Others
#
####################################################################################

Bladex.AddBipedAction("Gok","slip","Gok_slip",0.0,1.0,0)	
Bladex.AddBipedAction("Gok","slip_b","Gok_slip_b",0.0,1.0,0)	
Bladex.AddBipedAction("Gok","derrape","Gok_derrape",0.0,1.0,0)	


Bladex.AddBipedAction("Gok","b1","Gok_b1",0.0,1.0,0)
Bladex.AddBipedAction("Gok","b2","Gok_b2",0.0,1.0,0)
Bladex.AddBipedAction("Gok","b3","Gok_b3",0.0,1.0,0)




####################################################################################
#
# Relax.
#
####################################################################################

Bladex.AddBipedAction("Gok","Rlx_no","Rlx_no_Gok",0.0,1.0,0)
Bladex.AddBipedAction("Gok","Rlx_1h","Rlx_1h_Gok",0.0,1.0,0)
Bladex.AddBipedAction("Gok","Rlx_b","Rlx_b_Gok",0.0,1.0,0)
Bladex.AddBipedAction("Gok","Rlx_2h","Rlx_1h_Gok",0.0,1.0,0)
Bladex.AddBipedAction("Gok","Rlx_s","Rlx_1h_Gok",0.0,1.0,0)

####################################################################################
#
# Pasos.- Andares
#
####################################################################################

Bladex.AddBipedAction("Gok","Attack_f_s_nc","Gok_attack_f_s",0.0,1.0,0)
Bladex.AddBipedAction("Gok","Attack_b_s_nc","Gok_attack_b_s",0.0,1.0,0)

# Andar hacia atrás
Bladex.AddBipedAction("Gok","WBK_b","Wbk_b_Gok",0.0,1.0,0)
Bladex.AddBipedAction("Gok","WBK_no","Gok_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Gok","WBK_1h","Gok_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Gok","WBK_2h","Gok_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Gok","WBK_s","Gok_attack_b",0.0,1.0,0)

#Andar hacia alante
Bladex.AddBipedAction("Gok","WLK_b","Wlk_b_Gok",0.0,1.0,0)
Bladex.AddBipedAction("Gok","WLK_no","Wlk_1h_Gok",0.0,1.0,0)
Bladex.AddBipedAction("Gok","WLK_1h","Wlk_1h_Gok",0.0,1.0,0)
Bladex.AddBipedAction("Gok","WLK_2h","Wlk_1h_Gok",0.0,1.0,0)
Bladex.AddBipedAction("Gok","WLK_s","Wlk_1h_Gok",0.0,1.0,0)

#Correr hacia atrás
Bladex.AddBipedAction("Gok","WBK_JOG_b","Wbk_b_Gok",0.0,1.0,0)
Bladex.AddBipedAction("Gok","WBK_JOG_no","Gok_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Gok","WBK_JOG_s","Gok_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Gok","WBK_JOG_1h","Gok_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Gok","WBK_JOG_2h","Gok_attack_b",0.0,1.0,0)

#Correr hacia delante
Bladex.AddBipedAction("Gok","JOG_b","Jog_b_Gok",0.0,1.0,0)
Bladex.AddBipedAction("Gok","JOG_no","Jog_1h_Gok",0.0,1.0,0)
Bladex.AddBipedAction("Gok","JOG_s","Jog_1h_Gok",0.0,1.0,0)
Bladex.AddBipedAction("Gok","JOG_1h","Jog_1h_Gok",0.0,1.0,0)
Bladex.AddBipedAction("Gok","JOG_2h","Jog_1h_Gok",0.0,1.0,0)


#Modo sneak
Bladex.AddBipedAction("Gok","SNK_b","Wlk_b_Gok",0.0,1.0,0)
Bladex.AddBipedAction("Gok","SNK_no","Wlk_1h_Gok",0.0,1.0,0)
Bladex.AddBipedAction("Gok","SNK_s","Wlk_1h_Gok",0.0,1.0,0)
Bladex.AddBipedAction("Gok","SNK_1h","Wlk_1h_Gok",0.0,1.0,0)
Bladex.AddBipedAction("Gok","SNK_2h","Wlk_1h_Gok",0.0,1.0,0)




####################################################################################
#
# Caidas.
#
####################################################################################

Bladex.AddBipedAction("Gok","FllLow","FallMed_Gok",0.37,0.8,0)
Bladex.AddBipedAction("Gok","FllMed","FallMed_Gok",0.37,0.8,0)
Bladex.AddBipedAction("Gok","FllHigh","FallHigh_Gok",0.1,0.8,0)
Bladex.AddBipedAction("Gok","Dth_Fll","Dth_Fll_Gok",0.0,1.0,0)
Bladex.AddBipedAction("Gok","Dth_Fll2","Dth_Fll2_Gok",0.0,1.0,0)



####################################################################################
#
# Animaciones en combate
#
####################################################################################

#MOvement without shield
Bladex.AddBipedAction("Gok","Attack_f_1h","Gok_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Gok","Attack_b_1h","Gok_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Gok","Attack_r_1h","Gok_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Gok","Attack_l_1h","Gok_attack_l",0.0,1.0,0)

Bladex.AddBipedAction("Gok","Attack_f_2h","Gok_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Gok","Attack_b_2h","Gok_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Gok","Attack_r_2h","Gok_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Gok","Attack_l_2h","Gok_attack_l",0.0,1.0,0)

#Movement with shield
Bladex.AddBipedAction("Gok","Shattack_f_2h","Gok_attack_f_s",0.0,1.0,0)
Bladex.AddBipedAction("Gok","Shattack_b_2h","Gok_attack_b_s",0.0,1.0,0)
Bladex.AddBipedAction("Gok","Shattack_r_2h","Gok_attack_r_s",0.0,1.0,0)
Bladex.AddBipedAction("Gok","Shattack_l_2h","Gok_attack_l_s",0.0,1.0,0)

#Relax
Bladex.AddBipedAction("Gok","Rlx_f_1h","Gok_attack_rlx",0.0,1.0,0)
Bladex.AddBipedAction("Gok","Rlx_f_2h","Gok_attack_rlx",0.0,1.0,0)
Bladex.AddBipedAction("Gok","Shattack_rlx_2h","Gok_attack_rlx_s",0.0,1.0,0)

##Quick turns
#Bladex.AddBipedAction("Gok","Attack_t_r","Gok_attack_t_r",0.0,1.0,0)
#Bladex.AddBipedAction("Gok","Attack_t_r_s","Gok_attack_t_r_s",0.0,1.0,0)
#Bladex.AddBipedAction("Gok","Attack_t_l","Gok_attack_t_l",0.0,1.0,0)
#Bladex.AddBipedAction("Gok","Attack_t_l_s","Gok_attack_t_l_s",0.0,1.0,0)


#Dodges
Bladex.AddBipedAction("Gok","D_b","Gok_d_b",0.0,1.0,0)
Bladex.AddBipedAction("Gok","D_l","Gok_d_l",0.0,1.0,0)
Bladex.AddBipedAction("Gok","D_r","Gok_d_r",0.0,1.0,0)




####################################################################################
#
# Cambio de armas
#
####################################################################################


Bladex.AddBipedAction("Gok","Attack_Chg_r_l","Gok_attack_chg_r_l",0.0,1.0,0)
Bladex.AddBipedAction("Gok","Chg_r_l","Gok_attack_chg_r_l",0.0,1.0,0)

Bladex.AddBipedAction("Gok","attack_drink","Gok_attack_drink",0.0,1.0,0)






####################################################################################
#
# Animaciones de vigia
#
####################################################################################


Bladex.AddBipedAction("Gok","Wai_01","Gok_wai_01",0.0,1.0,0)
Bladex.AddBipedAction("Gok","Wai_02","Gok_wai_02",0.0,1.0,0)

Bladex.AddBipedAction("Gok","alarm01","Gok_alarm01",0.0,1.0,0)

Bladex.AddBipedAction("Gok","patrol1","Gok_patrol1",0.0,1.0,0)
Bladex.AddBipedAction("Gok","patrol2","Gok_patrol2",0.0,1.0,0)
Bladex.AddBipedAction("Gok","fury","Gok_fury",0.0,1.0,0)

Bladex.AddBipedAction("Gok","attack_look","Gok_attack_look",0.0,1.0,0)

Bladex.AddBipedAction("Gok","order","Gok_order",0.0,1.0,0)

Bladex.AddBipedAction("Gok","insult","Gok_insult",0.0,1.0,0)





####################################################################################
#
# Ataques
#
####################################################################################
	
Bladex.AddBipedAction("Gok","g_01","Gok_g_01",0.0,0.63,0)	
Bladex.AddBipedAction("Gok","g_02","Gok_g_02",0.0,0.75,0)	
Bladex.AddBipedAction("Gok","g_06","Gok_g_06",0.0,0.74,0)	
Bladex.AddBipedAction("Gok","g_15","Gok_g_15",0.0,0.76,0)
Bladex.AddBipedAction("Gok","g_16","Gok_g_16",0.0,0.78,0)	
Bladex.AddBipedAction("Gok","g_18","Gok_g_18",0.0,0.94,0)


####################################################################################
#
# Reacciones
#
####################################################################################


Bladex.AddBipedAction("Gok","df_01","Gok_df_01",0.10,0.50,0)	
Bladex.AddBipedAction("Gok","df_02","Gok_df_02",0.10,0.54,0)

Bladex.AddBipedAction("Gok","sw_react","Gok_df_s_broken",0.35,1.0,0)

Bladex.AddBipedAction("Gok","df_s_broken","Gok_df_s_broken",0.0,1.0,0)



	
Bladex.AddBipedAction("Gok","hurt_f_lite","Gok_hurt_f_lite",0.14,0.65,0)
Bladex.AddBipedAction("Gok","hurt_f_big","Gok_hurt_f_big",0.10,0.59,0)

Bladex.AddBipedAction("Gok","hurt_f_head","Gok_hurt_f_head",0.11,0.60,0)
Bladex.AddBipedAction("Gok","hurt_f_breast","Gok_hurt_f_back",0.10,0.58,0)
Bladex.AddBipedAction("Gok","hurt_f_back","Gok_hurt_f_back",0.10,0.58,0)
Bladex.AddBipedAction("Gok","hurt_f_r_arm","Gok_hurt_f_r_arm",0.10,0.55,0)
Bladex.AddBipedAction("Gok","hurt_f_l_arm","Gok_hurt_f_l_arm",0.10,0.58,0)
Bladex.AddBipedAction("Gok","hurt_f_r_leg","Gok_hurt_f_r_leg",0.10,0.54,0)
Bladex.AddBipedAction("Gok","hurt_f_l_leg","Gok_hurt_f_l_leg",0.10,0.56,0)

Bladex.AddBipedAction("Gok","hurt_jog","Gok_hurt_f_back",0.10,0.58,0)

Bladex.AddBipedAction("Gok","hurt_head","Gok_hurt_f_head",0.11,0.60,0)
Bladex.AddBipedAction("Gok","hurt_breast","Gok_hurt_f_back",0.10,0.58,0)
Bladex.AddBipedAction("Gok","hurt_back","Gok_hurt_f_back",0.10,0.58,0)
Bladex.AddBipedAction("Gok","hurt_r_arm","Gok_hurt_f_r_arm",0.10,0.55,0)
Bladex.AddBipedAction("Gok","hurt_l_arm","Gok_hurt_f_l_arm",0.10,0.58,0)
Bladex.AddBipedAction("Gok","hurt_r_leg","Gok_hurt_f_r_leg",0.10,0.54,0)
Bladex.AddBipedAction("Gok","hurt_l_leg","Gok_hurt_f_l_leg",0.10,0.56,0)	




####################################################################################
#
# MUERTES
#
####################################################################################

Bladex.AddBipedAction("Gok","dth_c1", "Gok_dth_c1",0.0,1.0,0)
Bladex.AddBipedAction("Gok","dth_c2", "Gok_dth_c2",0.0,1.0,0)
Bladex.AddBipedAction("Gok","dth_c3", "Gok_dth_c3",0.0,1.0,0)
Bladex.AddBipedAction("Gok","dth_c4", "Gok_dth_c4",0.0,1.0,0)
Bladex.AddBipedAction("Gok","dth_c5", "Gok_dth_c5",0.0,1.0,0)
Bladex.AddBipedAction("Gok","dth_c6", "Gok_dth_c6",0.0,1.0,0)
Bladex.AddBipedAction("Gok","dth_c7", "Gok_dth_c7",0.0,1.0,0)
Bladex.AddBipedAction("Gok","dth0",   "Gok_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Gok","dth_n00","Gok_dth_n00",0.0,1.0,0)
Bladex.AddBipedAction("Gok","dth_n01","Gok_dth_n01",0.0,1.0,0)
Bladex.AddBipedAction("Gok","dth_n02","Gok_dth_n02",0.0,1.0,0)
Bladex.AddBipedAction("Gok","dth_n03","Gok_dth_n03",0.0,1.0,0)
Bladex.AddBipedAction("Gok","dth_n04","Gok_dth_n04",0.0,1.0,0)
Bladex.AddBipedAction("Gok","dth_n05","Gok_dth_n05",0.0,1.0,0)
Bladex.AddBipedAction("Gok","dth_n06","Gok_dth_n06",0.0,1.0,0)

Bladex.AddBipedAction("Gok","dth_rock","Gok_dth_rock",0.0,1.0,0)
Bladex.AddBipedAction("Gok","dth_rockfront","Gok_dth_rockfront",0.0,1.0,0)
Bladex.AddBipedAction("Gok","dth_burn","Gok_dth_burn",0.0,1.0,0)	



	


