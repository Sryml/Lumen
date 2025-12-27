import Bladex



####################################################################################
#
# Escalar + saltos
#
####################################################################################

Bladex.AddBipedAction("Rgn","clmb_low_1h","Rgn_clmb_low_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Rgn","clmb_medlow_1h","Rgn_clmb_medlow_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Rgn","clmb_medium_1h","Rgn_clmb_medium_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Rgn","clmb_high_1h","Rgn_clmb_high_1h",0.0,1.0,0)	

#Bladex.AddBipedAction("Rgn","LongJump1H","Kgt_jmp_1h",0.0,0.93,0)	
#Bladex.AddBipedAction("Rgn","LongJumpNo","Kgt_jmp_no",0.0,0.93,0)	
#Bladex.AddBipedAction("Rgn","ShortJump","Kgt_jmph0_no",0.41,1.0,0)	


####################################################################################
#
# Others
#
####################################################################################

Bladex.AddBipedAction("Rgn","slip","Rgn_slip",0.0,1.0,0)	
Bladex.AddBipedAction("Rgn","slip_b","Rgn_slip_b",0.0,1.0,0)	
Bladex.AddBipedAction("Rgn","derrape","Rgn_derrape",0.14,1.0,0)	

Bladex.AddBipedAction("Rgn","attack_drink", "Rgn_attack_drink",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","escape", "Rgn_escape",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","escape2", "Rgn_escape2",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","end_ragnar_ragnar", "Rgn_end_ragnar_ragnar",0.0,1.0,0)


#Bladex.AddBipedAction("Rgn","b1","Kgt_b1",0.0,1.0,0)	
#Bladex.AddBipedAction("Rgn","b2","Kgt_b2",0.0,1.0,0)	
#Bladex.AddBipedAction("Rgn","b3","Kgt_b3",0.0,1.0,0)	



####################################################################################
#
# Relax.
#
####################################################################################

Bladex.AddBipedAction("Rgn","Rlx_no","Rlx_1h_Rgn",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","Rlx_1h","Rlx_1h_Rgn",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","Rlx_b","Rlx_1h_Rgn",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","Rlx_2h","Rlx_1h_Rgn",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","Rlx_s","Rlx_1h_Rgn",0.0,1.0,0)



####################################################################################
#
# Pasos.- Andares
#
####################################################################################

#Movement with shield -> !NPC only!!!!
Bladex.AddBipedAction("Rgn","Attack_f_s_nc","Rgn_attack_f_s",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","Attack_b_s_nc","Rgn_attack_b_s",0.0,1.0,0)

#Bladex.AddBipedAction("Rgn","ShortStep","WlkShort_Rgn", 0.0,1.0,0)

#Bladex.AddBipedAction("Rgn","LStepUp","Wlk_1h_Rgn","WlkUp_Rgn",0.0,0.5,0)
#Bladex.AddBipedAction("Rgn","RStepUp","Wlk_1h_Rgn","WlkUp_Rgn",0.5,1.0,0)

#Bladex.AddBipedAction("Rgn","LStairsUp","StairsUp_Rgn","StairsUpP_Rgn",0.0,0.5,0)
#Bladex.AddBipedAction("Rgn","RStairsUp","StairsUp_Rgn","StairsUpP_Rgn",0.5,1.0,0)

#Bladex.AddBipedAction("Rgn","LStepDown","Wlk_1h_Rgn","WlkDown_Rgn",0.0,0.5,0)
#Bladex.AddBipedAction("Rgn","RStepDown","Wlk_1h_Rgn","WlkDown_Rgn",0.5,1.0,0)

#Bladex.AddBipedAction("Rgn","LStairsDown","StairsDown_Rgn",0.0,0.5,0)
#Bladex.AddBipedAction("Rgn","RStairsDown","StairsDown_Rgn",0.5,1.0,0)

# Andar hacia atrás
Bladex.AddBipedAction("Rgn","WBK_b","Wbk_1h_Rgn",0.0,1.0,0)	
Bladex.AddBipedAction("Rgn","WBK_no","Wbk_1h_Rgn",0.0,1.0,0)	
Bladex.AddBipedAction("Rgn","WBK_1h","Wbk_1h_Rgn",0.0,1.0,0)		
Bladex.AddBipedAction("Rgn","WBK_2h","Wbk_1h_Rgn",0.0,1.0,0)		
Bladex.AddBipedAction("Rgn","WBK_s","Wbk_1h_Rgn",0.0,1.0,0)	

#Andar hacia delante
Bladex.AddBipedAction("Rgn","WLK_b","Wlk_1h_Rgn",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","WLK_no","Wlk_1h_Rgn",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","WLK_1h","Wlk_1h_Rgn",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","WLK_2h","Wlk_1h_Rgn",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","WLK_s","Wlk_1h_Rgn",0.0,1.0,0)

#Correr hacia delante
Bladex.AddBipedAction("Rgn","JOG_b","Jog_1h_Rgn",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","JOG_no","Jog_1h_Rgn",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","JOG_s","Jog_1h_Rgn",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","JOG_1h","Jog_1h_Rgn",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","JOG_2h","Jog_1h_Rgn",0.0,1.0,0)

#Correr hacia atrás
Bladex.AddBipedAction("Rgn","WBK_JOG_b","Wbk_1h_Rgn",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","WBK_JOG_no","Wbk_1h_Rgn",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","WBK_JOG_1h","Wbk_1h_Rgn",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","WBK_JOG_2h","Wbk_1h_Rgn",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","WBK_JOG_s","Wbk_1h_Rgn",0.0,1.0,0)

#Modo sneak
Bladex.AddBipedAction("Rgn","SNK_b","Wlk_1h_Rgn",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","SNK_no","Wlk_1h_Rgn",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","SNK_s", "Wlk_1h_Rgn",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","SNK_1h","Wlk_1h_Rgn",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","SNK_2h","Wlk_1h_Rgn",0.0,1.0,0)


####################################################################################
#
# Cambiar Armas
#
####################################################################################	

Bladex.AddBipedAction("Rgn","Attack_Chg_r_l","Rgn_attack_chg_r_l",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","Chg_r_l",       "Rgn_attack_chg_r_l",0.0,1.0,0)


####################################################################################
#
# Caidas.
#
####################################################################################

Bladex.AddBipedAction("Rgn","FllLow","FallLow_Rgn",0.5,0.8,0)
Bladex.AddBipedAction("Rgn","FllMed","FallMed_Rgn",0.37,0.8,0)
Bladex.AddBipedAction("Rgn","FllHigh","FallHigh_Rgn",0.1,0.8,0)


####################################################################################
#
# Animaciones en combate
#
####################################################################################

#MOvement without shield
Bladex.AddBipedAction("Rgn","Attack_f_1h","Rgn_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","Attack_b_1h","Rgn_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","Attack_r_1h","Rgn_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","Attack_l_1h","Rgn_attack_l",0.0,1.0,0)

Bladex.AddBipedAction("Rgn","Attack_f_2h","Rgn_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","Attack_b_2h","Rgn_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","Attack_r_2h","Rgn_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","Attack_l_2h","Rgn_attack_l",0.0,1.0,0)

#Movement with shield
Bladex.AddBipedAction("Rgn","Shattack_f_2h","Rgn_attack_f_s",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","Shattack_b_2h","Rgn_attack_b_s",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","Shattack_r_2h","Rgn_attack_r_s",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","Shattack_l_2h","Rgn_attack_l_s",0.0,1.0,0)

#Relax
Bladex.AddBipedAction("Rgn","Rlx_f_1h","Rgn_rlx_f_s",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","Rlx_f_2h","Rgn_rlx_f_s",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","Shattack_rlx_2h","Rgn_rlx_f_s",0.0,1.0,0)

#Quick turns
#Bladex.AddBipedAction("Rgn","Attack_t_r","Rgn_attack_t_r",0.0,1.0,0)
#Bladex.AddBipedAction("Rgn","Attack_t_r_s","Rgn_attack_t_r_s",0.0,1.0,0)
#Bladex.AddBipedAction("Rgn","Attack_t_l","Rgn_attack_t_l",0.0,1.0,0)
#Bladex.AddBipedAction("Rgn","Attack_t_l_s","Rgn_attack_t_l_s",0.0,1.0,0)


#Dodges
Bladex.AddBipedAction("Rgn","D_b","Rgn_d_b",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","D_l","Rgn_d_l",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","D_r","Rgn_d_r",0.0,1.0,0)


####################################################################################
#
# Heridas
#
####################################################################################

Bladex.AddBipedAction("Rgn","hurt_f_lite","Rgn_hurt_f_lite",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","hurt_f_big","Rgn_hurt_f_big",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","hurt_f_head","Rgn_hurt_f_head",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","hurt_f_breast","Rgn_hurt_f_breast",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","hurt_f_back","Rgn_hurt_f_back",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","hurt_f_r_arm","Rgn_hurt_f_r_arm",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","hurt_f_l_arm","Rgn_hurt_f_l_arm",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","hurt_f_r_leg","Rgn_hurt_f_r_leg",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","hurt_f_l_leg","Rgn_hurt_f_l_leg",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","hurt_jog","Rgn_hurt_jog",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","hurt_head","Rgn_hurt_head",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","hurt_breast","Rgn_hurt_breast",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","hurt_back","Rgn_hurt_back",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","hurt_r_arm","Rgn_hurt_r_arm",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","hurt_l_arm","Rgn_hurt_l_arm",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","hurt_r_leg","Rgn_hurt_r_leg",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","hurt_l_leg","Rgn_hurt_l_leg",0.0,1.0,0)


Bladex.AddBipedAction("Rgn","df_01","Rgn_df_01",0.0,0.494,0)
Bladex.AddBipedAction("Rgn","df_02","Rgn_df_02",0.0,0.680,0)

Bladex.AddBipedAction("Rgn","df_s_broken","Rgn_df_s_broken",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","sw_react","Rgn_sword_reaction",0.143,0.5,0)	

#Bladex.AddBipedAction("Knight_Traitor","sword_broken","Tkn_sword_broken",0.0,1.0,0)


####################################################################################
#
# MUERTES
#
####################################################################################

Bladex.AddBipedAction("Rgn","dth_c1","Rgn_dth_c1",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","dth_c2","Rgn_dth_c2",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","dth_c3","Rgn_dth_c3",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","dth_c4","Rgn_dth_c4",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","dth_c5","Rgn_dth_c5",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","dth_c6","Rgn_dth_c6",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","dth_c7","Rgn_dth_c7",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","dth0",  "Rgn_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","dth_n00","Rgn_dth_n00",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","dth_n01","Rgn_dth_n01",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","dth_n02","Rgn_dth_n02",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","dth_n03","Rgn_dth_n03",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","dth_n04","Rgn_dth_n04",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","dth_n05","Rgn_dth_n05",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","dth_n06","Rgn_dth_n06",0.0,1.0,0)


Bladex.AddBipedAction("Rgn","dth_burn","Rgn_dth_burn",0.0,1.0,0)
#Bladex.AddBipedAction("Rgn","Dth_Fll","Dth_Fll_Rgn",0.0,0.33,0)
#Bladex.AddBipedAction("Rgn","Dth_Fll2","Dth_Fll2_Rgn",0.0,1.0,0)


####################################################################################
#
# Ataques
#
####################################################################################
	
Bladex.AddBipedAction("Rgn","g_01","Rgn_g_01",0.0,1.0,0)	
Bladex.AddBipedAction("Rgn","g_02","Rgn_g_02",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","g_03","Rgn_g_03",0.0,1.0,0)	
Bladex.AddBipedAction("Rgn","g_07","Rgn_g_07",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","g_17","Rgn_g_17",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","g_21","Rgn_g_21",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","g_d_l","Rgn_g_d_l",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","g_d_r","Rgn_g_d_r",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","g_escape","Rgn_g_escape",0.0,1.0,0)



####################################################################################
#
# Burlas
#
####################################################################################

Bladex.AddBipedAction("Rgn","insult","Rgn_insult",0.0,1.0,0)
Bladex.AddBipedAction("Rgn","laugh","Rgn_laugh",0.0,1.0,0)



