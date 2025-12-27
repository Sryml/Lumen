import Bladex

#import AnimationSets


#AnimationSets.LoadOrkAnimationSet("Ork")

####################################################################################
#
# Escalar + saltos
#
####################################################################################

Bladex.AddBipedAction("Ork","clmb_low_1h","Ork_clmb_low_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Ork","clmb_medlow_1h","Ork_clmb_low_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Ork","clmb_medium_1h","Ork_clmb_medium_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Ork","clmb_high_1h","Ork_clmb_medium_1h",0.0,1.0,0)	

Bladex.AddBipedAction("Ork","LongJump1H","Ork_jmp_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Ork","LongJumpNo","Ork_jmp_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Ork","ShortJump","Ork_jmp_1h",0.0,1.0,0)	



####################################################################################
#
# Others
#
####################################################################################

Bladex.AddBipedAction("Ork","slip","Ork_slip",0.0,1.0,0)	
Bladex.AddBipedAction("Ork","slip_b","Ork_slip_b",0.0,1.0,0)	
Bladex.AddBipedAction("Ork","derrape","Ork_derrape",0.0,1.0,0)	


Bladex.AddBipedAction("Ork","b1","Ork_b1",0.0,1.0,0)	
Bladex.AddBipedAction("Ork","b2","Ork_b2",0.0,1.0,0)	
Bladex.AddBipedAction("Ork","b3","Ork_b3",0.0,1.0,0)	




####################################################################################
#
# Relax.
#
####################################################################################

Bladex.AddBipedAction("Ork","Rlx_no","Rlx_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Ork","Rlx_1h","Rlx_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Ork","Rlx_b","Rlx_b_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Ork","Rlx_2h","Rlx_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Ork","Rlx_s","Rlx_1h_Ork",0.0,1.0,0)

####################################################################################
#
# Pasos.- Andares
#
####################################################################################

#Bladex.AddBipedAction("Ork","LStepUp","Wlk_Ork","WlkUp_Ork",0.0,0.5,0)
#Bladex.AddBipedAction("Ork","RStepUp","Wlk_Ork","WlkUp_Ork",0.5,1.0,0)

#Bladex.AddBipedAction("Ork","LStairsUp","StairsUp_Ork","StairsUpP_Ork",0.0,0.5,0)
#Bladex.AddBipedAction("Ork","RStairsUp","StairsUp_Ork","StairsUpP_Ork",0.5,1.0,0)

#Bladex.AddBipedAction("Ork","LStepDown","Wlk_Ork","WlkDown_Ork",0.0,0.5,0)
#Bladex.AddBipedAction("Ork","RStepDown","Wlk_Ork","WlkDown_Ork",0.5,1.0,0)

#Bladex.AddBipedAction("Ork","LStairsDown","StairsDown_Ork",0.0,0.5,0)
#Bladex.AddBipedAction("Ork","RStairsDown","StairsDown_Ork",0.5,1.0,0)

# Andar hacia atrás
Bladex.AddBipedAction("Ork","WBK_b","Wbk_b_Ork",0.0,1.0,0)	
Bladex.AddBipedAction("Ork","WBK_no","Ork_attack_b",0.0,1.0,0)	
Bladex.AddBipedAction("Ork","WBK_1h","Ork_attack_b",0.0,1.0,0)		
Bladex.AddBipedAction("Ork","WBK_2h","Ork_attack_b",0.0,1.0,0)	
Bladex.AddBipedAction("Ork","WBK_s","Ork_attack_b",0.0,1.0,0)

#Andar hacia alante
Bladex.AddBipedAction("Ork","WLK_b","Wlk_b_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Ork","WLK_no","Wlk_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Ork","WLK_1h","Wlk_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Ork","WLK_2h","Wlk_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Ork","WLK_s","Wlk_1h_Ork",0.0,1.0,0)

#Correr hacia atrás
Bladex.AddBipedAction("Ork","WBK_JOG_b","Wbk_b_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Ork","WBK_JOG_no","Ork_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Ork","WBK_JOG_s","Ork_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Ork","WBK_JOG_1h","Ork_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Ork","WBK_JOG_2h","Ork_attack_b",0.0,1.0,0)

#Correr hacia delante
Bladex.AddBipedAction("Ork","JOG_b","Jog_b_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Ork","JOG_no","Jog_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Ork","JOG_s","Jog_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Ork","JOG_1h","Jog_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Ork","JOG_2h","Jog_1h_Ork",0.0,1.0,0)


#Modo sneak
Bladex.AddBipedAction("Ork","SNK_b","Wlk_b_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Ork","SNK_no","Wlk_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Ork","SNK_s","Wlk_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Ork","SNK_1h","Wlk_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Ork","SNK_2h","Wlk_1h_Ork",0.0,1.0,0)

#Correr con escudo en modo no combate                                       
Bladex.AddBipedAction("Ork","Attack_f_s_nc","Ork_attack_f_s",0.0,1.0,0)     
Bladex.AddBipedAction("Ork","Attack_b_s_nc","Ork_attack_b_s",0.0,1.0,0)     
                                                                          
####################################################################################
#
# Caidas.
#
####################################################################################

Bladex.AddBipedAction("Ork","FllLow","FallMed_Ork",0.37,0.8,0)
Bladex.AddBipedAction("Ork","FllMed","FallMed_Ork",0.37,0.8,0)
Bladex.AddBipedAction("Ork","FllHigh","FallHigh_Ork",0.1,0.8,0)
Bladex.AddBipedAction("Ork","Dth_Fll","Dth_Fll_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Ork","Dth_Fll2","Dth_Fll2_Ork",0.0,1.0,0)



####################################################################################
#
# Animaciones en combate
#
####################################################################################

#MOvement without shield
Bladex.AddBipedAction("Ork","Attack_f_1h","Ork_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Ork","Attack_b_1h","Ork_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Ork","Attack_r_1h","Ork_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Ork","Attack_l_1h","Ork_attack_l",0.0,1.0,0)

Bladex.AddBipedAction("Ork","Attack_f_2h","Ork_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Ork","Attack_b_2h","Ork_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Ork","Attack_r_2h","Ork_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Ork","Attack_l_2h","Ork_attack_l",0.0,1.0,0)

#Movement with shield
Bladex.AddBipedAction("Ork","Shattack_f_2h","Ork_attack_f_s",0.0,1.0,0)
Bladex.AddBipedAction("Ork","Shattack_b_2h","Ork_attack_b_s",0.0,1.0,0)
Bladex.AddBipedAction("Ork","Shattack_r_2h","Ork_attack_r_s",0.0,1.0,0)
Bladex.AddBipedAction("Ork","Shattack_l_2h","Ork_attack_l_s",0.0,1.0,0)

#Relax
Bladex.AddBipedAction("Ork","Rlx_f_1h","Ork_attack_rlx",0.0,1.0,0)
Bladex.AddBipedAction("Ork","Rlx_f_2h","Ork_attack_rlx",0.0,1.0,0)
Bladex.AddBipedAction("Ork","Shattack_rlx_2h","Ork_attack_rlx_s",0.0,1.0,0)

#Quick turns
#Bladex.AddBipedAction("Ork","Attack_t_r","Ork_attack_t_r",0.0,1.0,0)
#Bladex.AddBipedAction("Ork","Attack_t_r_s","Ork_attack_t_r_s",0.0,1.0,0)
#Bladex.AddBipedAction("Ork","Attack_t_l","Ork_attack_t_l",0.0,1.0,0)
#Bladex.AddBipedAction("Ork","Attack_t_l_s","Ork_attack_t_l_s",0.0,1.0,0)


#Dodges
Bladex.AddBipedAction("Ork","D_b","Ork_d_b",0.0,1.0,0)
Bladex.AddBipedAction("Ork","D_l","Ork_d_l",0.0,1.0,0)
Bladex.AddBipedAction("Ork","D_r","Ork_d_r",0.0,1.0,0)



####################################################################################
#
# Ataques
#
####################################################################################
	
Bladex.AddBipedAction("Ork","g_01","Ork_g_01",0.0,1.0,0)	
Bladex.AddBipedAction("Ork","g_02","Ork_g_02",0.0,1.0,0)	
Bladex.AddBipedAction("Ork","g_06","Ork_g_06",0.0,1.0,0)	
Bladex.AddBipedAction("Ork","g_15","Ork_g_15",0.0,1.0,0)
Bladex.AddBipedAction("Ork","g_16","Ork_g_16",0.0,1.0,0)	
Bladex.AddBipedAction("Ork","g_18","Ork_g_18",0.0,1.0,0)






####################################################################################
#
# Animaciones de vigia
#
####################################################################################


Bladex.AddBipedAction("Ork","Wai_01","Ork_wai_01",0.0,1.0,0)
Bladex.AddBipedAction("Ork","Wai_02","Ork_wai_02",0.0,1.0,0)

Bladex.AddBipedAction("Ork","alarm01","Ork_alarm01",0.0,1.0,0)

Bladex.AddBipedAction("Ork","patrol1","Ork_patrol1",0.0,1.0,0)
Bladex.AddBipedAction("Ork","patrol2","Ork_patrol2",0.0,1.0,0)
Bladex.AddBipedAction("Ork","fury","Ork_fury",0.0,1.0,0)

Bladex.AddBipedAction("Ork","attack_look","Ork_attack_look",0.0,1.0,0)

Bladex.AddBipedAction("Ork","order","Ork_order",0.0,1.0,0)

Bladex.AddBipedAction("Ork","insult","Ork_insult",0.0,1.0,0)




####################################################################################
#
# Cambio de armas
#
####################################################################################


Bladex.AddBipedAction("Ork","Attack_Chg_r_l","Ork_attack_chg_r_l",0.0,1.0,0)
Bladex.AddBipedAction("Ork","Chg_r_l","Ork_attack_chg_r_l",0.0,1.0,0)

Bladex.AddBipedAction("Ork","attack_drink","Ork_attack_drink",0.0,1.0,0)


####################################################################################
#
# Reacciones
#
####################################################################################


Bladex.AddBipedAction("Ork","df_01","Ork_df_01",0.10,0.48,0)	
Bladex.AddBipedAction("Ork","df_02","Ork_df_02",0.10,0.67,0)

Bladex.AddBipedAction("Ork","sw_react","Ork_df_s_broken",0.35,1.0,0)

Bladex.AddBipedAction("Ork","df_s_broken","Ork_df_s_broken",0.0,1.0,0)



	
Bladex.AddBipedAction("Ork","hurt_f_lite","Ork_hurt_f_lite",0.14,0.65,0)	
Bladex.AddBipedAction("Ork","hurt_f_big","Ork_hurt_f_big",0.10,0.59,0)	
Bladex.AddBipedAction("Ork","hurt_f_head","Ork_hurt_f_head",0.11,0.60,0)	
Bladex.AddBipedAction("Ork","hurt_f_breast","Ork_hurt_f_back",0.10,0.58,0)	
Bladex.AddBipedAction("Ork","hurt_f_back","Ork_hurt_f_back",0.10,0.58,0)	
Bladex.AddBipedAction("Ork","hurt_f_r_arm","Ork_hurt_f_r_arm",0.10,0.55,0)	
Bladex.AddBipedAction("Ork","hurt_f_l_arm","Ork_hurt_f_l_arm",0.10,0.58,0)	
Bladex.AddBipedAction("Ork","hurt_f_r_leg","Ork_hurt_f_r_leg",0.10,0.54,0)	
Bladex.AddBipedAction("Ork","hurt_f_l_leg","Ork_hurt_f_l_leg",0.10,0.56,0)	
Bladex.AddBipedAction("Ork","hurt_jog","Ork_hurt_f_back",0.10,0.58,0)	
Bladex.AddBipedAction("Ork","hurt_head","Ork_hurt_f_head",0.11,0.60,0)	
Bladex.AddBipedAction("Ork","hurt_breast","Ork_hurt_f_back",0.10,0.58,0)	
Bladex.AddBipedAction("Ork","hurt_back","Ork_hurt_f_back",0.10,0.58,0)	
Bladex.AddBipedAction("Ork","hurt_r_arm","Ork_hurt_f_r_arm",0.10,0.55,0)	
Bladex.AddBipedAction("Ork","hurt_l_arm","Ork_hurt_f_l_arm",0.10,0.58,0)
Bladex.AddBipedAction("Ork","hurt_r_leg","Ork_hurt_f_r_leg",0.10,0.54,0)	
Bladex.AddBipedAction("Ork","hurt_l_leg","Ork_hurt_f_l_leg",0.10,0.56,0)



####################################################################################
#
# MUERTES
#
####################################################################################

Bladex.AddBipedAction("Ork","dth_c1", "Ork_dth_c1",0.0,1.0,0)
Bladex.AddBipedAction("Ork","dth_c2", "Ork_dth_c2",0.0,1.0,0)
Bladex.AddBipedAction("Ork","dth_c3", "Ork_dth_c3",0.0,1.0,0)
Bladex.AddBipedAction("Ork","dth_c4", "Ork_dth_c4",0.0,1.0,0)
Bladex.AddBipedAction("Ork","dth_c5", "Ork_dth_c5",0.0,1.0,0)
Bladex.AddBipedAction("Ork","dth_c6", "Ork_dth_c6",0.0,1.0,0)
Bladex.AddBipedAction("Ork","dth_c7", "Ork_dth_c7",0.0,1.0,0)
Bladex.AddBipedAction("Ork","dth0",   "Ork_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Ork","dth_n00","Ork_dth_n00",0.0,1.0,0)
Bladex.AddBipedAction("Ork","dth_n01","Ork_dth_n01",0.0,1.0,0)
Bladex.AddBipedAction("Ork","dth_n02","Ork_dth_n02",0.0,1.0,0)
Bladex.AddBipedAction("Ork","dth_n03","Ork_dth_n03",0.0,1.0,0)
Bladex.AddBipedAction("Ork","dth_n04","Ork_dth_n04",0.0,1.0,0)
Bladex.AddBipedAction("Ork","dth_n05","Ork_dth_n05",0.0,1.0,0)
Bladex.AddBipedAction("Ork","dth_n06","Ork_dth_n06",0.0,1.0,0)

Bladex.AddBipedAction("Ork","dth_rock","Ork_dth_rock",0.0,1.0,0)
Bladex.AddBipedAction("Ork","dth_rockfront","Ork_dth_rockfront",0.0,1.0,0)
Bladex.AddBipedAction("Ork","dth_burn","Ork_dth_burn",0.0,1.0,0)	



