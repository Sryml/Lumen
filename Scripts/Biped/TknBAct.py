import Bladex

#import AnimationSets


#AnimationSets.LoadKnightAnimationSet("Tkn")

####################################################################################
#
# Escalar
#
####################################################################################

Bladex.AddBipedAction("Knight_Traitor","clmb_low_1h","Tkn_clmb_low_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Knight_Traitor","clmb_medlow_1h","Tkn_clmb_medlow_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Knight_Traitor","clmb_medium_1h","Tkn_clmb_medium_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Knight_Traitor","clmb_high_1h","Tkn_clmb_high_1h",0.0,1.0,0)	


####################################################################################
#
# Others
#
####################################################################################

Bladex.AddBipedAction("Knight_Traitor","slip","Tkn_slip",0.0,1.0,0)	
Bladex.AddBipedAction("Knight_Traitor","slip_b","Tkn_slip_b",0.0,1.0,0)	
Bladex.AddBipedAction("Knight_Traitor","derrape","Tkn_derrape",0.14,1.0,0)	

Bladex.AddBipedAction("Knight_Traitor","attack_drink", "Tkn_attack_drink",0.0,1.0,0)

Bladex.AddBipedAction("Knight_Traitor","b1","Tkn_b1",0.0,1.0,0)	
Bladex.AddBipedAction("Knight_Traitor","b2","Tkn_b2",0.0,1.0,0)	
Bladex.AddBipedAction("Knight_Traitor","b3","Tkn_b3",0.0,1.0,0)	




####################################################################################
#
# Relax.
#
####################################################################################

Bladex.AddBipedAction("Knight_Traitor","Rlx_no","Rlx_no_Tkn",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","Rlx_s","Rlx_1h_Tkn",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","Rlx_1h","Rlx_1h_Tkn",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","Rlx_2h","Rlx_1h_Tkn",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","Rlx_b","Rlx_b_Tkn",0.0,1.0,0)
#Bladex.AddBipedAction("Knight_Traitor","Rlx_block","Tkn_rlx_f_s",0.0,1.0,0)


####################################################################################
#
# Pasos.- Andares
#
####################################################################################

#ladex.AddBipedAction("Knight_Traitor","LStepUp","Wlk_Tkn","WlkUp_Tkn",0.0,0.5,0)
#ladex.AddBipedAction("Knight_Traitor","RStepUp","Wlk_Tkn","WlkUp_Tkn",0.5,1.0,0)

#Bladex.AddBipedAction("Knight_Traitor","LStairsUp","StairsUp_Tkn","StairsUpP_Tkn",0.0,0.5,0)
#Bladex.AddBipedAction("Knight_Traitor","RStairsUp","StairsUp_Tkn","StairsUpP_Tkn",0.5,1.0,0)

#Bladex.AddBipedAction("Knight_Traitor","LStepDown","Wlk_Tkn","WlkDown_Tkn",0.0,0.5,0)
#Bladex.AddBipedAction("Knight_Traitor","RStepDown","Wlk_Tkn","WlkDown_Tkn",0.5,1.0,0)

#Bladex.AddBipedAction("Knight_Traitor","LStairsDown","StairsDown_Tkn",0.0,0.5,0)
#Bladex.AddBipedAction("Knight_Traitor","RStairsDown","StairsDown_Tkn",0.5,1.0,0)

# Andar hacia detras
Bladex.AddBipedAction("Knight_Traitor","WBK_b","Wbk_b_Tkn",0.0,1.0,0)	
Bladex.AddBipedAction("Knight_Traitor","WBK_no","Wbk_no_Tkn",0.0,1.0,0)	
Bladex.AddBipedAction("Knight_Traitor","WBK_1h","Wbk_1h_Tkn",0.0,1.0,0)	
Bladex.AddBipedAction("Knight_Traitor","WBK_2h","Wbk_1h_Tkn",0.0,1.0,0)	
Bladex.AddBipedAction("Knight_Traitor","WBK_s","Wbk_1h_Tkn",0.0,1.0,0)	

#Andar hacia delante
Bladex.AddBipedAction("Knight_Traitor","WLK_b","Wlk_b_Tkn",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","WLK_no","Wlk_no_Tkn",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","WLK_1h","Wlk_1h_Tkn",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","WLK_2h","Wlk_2h_Tkn",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","WLK_s","Wlk_1h_Tkn",0.0,1.0,0)

#Correr hacia delante
Bladex.AddBipedAction("Knight_Traitor","JOG_b","Jog_b_Tkn",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","JOG_no","Jog_1h_Tkn",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","JOG_1h","Jog_1h_Tkn",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","JOG_2h","Jog_2h_Tkn",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","JOG_s","Jog_1h_Tkn",0.0,1.0,0)

#Correr hacia atrás
Bladex.AddBipedAction("Knight_Traitor","WBK_JOG_b","Wbk_b_Tkn",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","WBK_JOG_no","Wbk_no_Tkn",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","WBK_JOG_s","Wbk_1h_Tkn",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","WBK_JOG_1h","Wbk_1h_Tkn",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","WBK_JOG_2h","Wbk_1h_Tkn",0.0,1.0,0)


#Modo sneak
Bladex.AddBipedAction("Knight_Traitor","SNK_b","Snk_b_Tkn",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","SNK_no","Snk_no_Tkn",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","SNK_1h","Snk_1h_Tkn",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","SNK_2h","Snk_1h_Tkn",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","SNK_s","Snk_1h_Tkn",0.0,1.0,0)

#Correr con escudo en modo no combate
Bladex.AddBipedAction("Knight_Traitor","Attack_f_s_nc","Tkn_attack_f_s",0.0,1.0,0)     
Bladex.AddBipedAction("Knight_Traitor","Attack_b_s_nc","Tkn_attack_b_s",0.0,1.0,0)     


####################################################################################
#
# Cambiar Armas
#
####################################################################################	

Bladex.AddBipedAction("Knight_Traitor","Attack_Chg_r_l","Tkn_attack_chg_r_l",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","Chg_r_l",       "Tkn_attack_chg_r_l",0.0,1.0,0)


####################################################################################
#
# Caidas.
#
####################################################################################

Bladex.AddBipedAction("Knight_Traitor","FllLow","FallLow_Tkn",0.0,0.8,0)

Bladex.AddBipedAction("Knight_Traitor","FllMed","FallMed_Tkn",0.0,0.8,0)

Bladex.AddBipedAction("Knight_Traitor","FllHigh","FallHigh_Tkn",0.15,0.8,0)
Bladex.AddBipedAction("Knight_Traitor","Dth_Fll","Dth_Fll_Tkn",0.0,0.33,0)
Bladex.AddBipedAction("Knight_Traitor","Dth_Fll2","Dth_Fll2_Tkn",0.0,1.0,0)



####################################################################################
#
# Animaciones en combate
#
####################################################################################


Bladex.AddBipedAction("Knight_Traitor","Attack_f_1h","Tkn_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","Attack_b_1h","Tkn_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","Attack_r_1h","Tkn_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","Attack_l_1h","Tkn_attack_l",0.0,1.0,0)

Bladex.AddBipedAction("Knight_Traitor","Attack_f_2h","Tkn_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","Attack_b_2h","Tkn_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","Attack_r_2h","Tkn_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","Attack_l_2h","Tkn_attack_l",0.0,1.0,0)

Bladex.AddBipedAction("Knight_Traitor","Shattack_f_2h","Tkn_attack_f_s",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","Shattack_b_2h","Tkn_attack_b_s",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","Shattack_r_2h","Tkn_attack_r_s",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","Shattack_l_2h","Tkn_attack_l_s",0.0,1.0,0)

Bladex.AddBipedAction("Knight_Traitor","Rlx_f_1h","Tkn_rlx_f",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","Rlx_f_2h","Tkn_rlx_f",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","Shattack_rlx_2h","Tkn_rlx_f_s",0.0,1.0,0)


Bladex.AddBipedAction("Knight_Traitor","D_b","Tkn_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","D_l","Tkn_d_l",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","D_r","Tkn_d_r",0.0,1.0,0)


####################################################################################
#
# Heridas
#
####################################################################################

Bladex.AddBipedAction("Knight_Traitor","hurt_f_lite","Tkn_hurt_f_lite",0.14,0.65,0)	
Bladex.AddBipedAction("Knight_Traitor","hurt_f_big","Tkn_hurt_f_big",0.10,0.59,0)	
Bladex.AddBipedAction("Knight_Traitor","hurt_f_head","Tkn_hurt_f_head",0.11,0.60,0)	
Bladex.AddBipedAction("Knight_Traitor","hurt_f_breast","Tkn_hurt_f_breast",0.11,0.58,0)	
Bladex.AddBipedAction("Knight_Traitor","hurt_f_back","Tkn_hurt_f_back",0.10,0.58,0)	
Bladex.AddBipedAction("Knight_Traitor","hurt_f_r_arm","Tkn_hurt_f_r_arm",0.10,0.55,0)	
Bladex.AddBipedAction("Knight_Traitor","hurt_f_l_arm","Tkn_hurt_f_l_arm",0.10,0.58,0)	
Bladex.AddBipedAction("Knight_Traitor","hurt_f_r_leg","Tkn_hurt_f_r_leg",0.10,0.54,0)	
Bladex.AddBipedAction("Knight_Traitor","hurt_f_l_leg","Tkn_hurt_f_l_leg",0.10,0.56,0)	
Bladex.AddBipedAction("Knight_Traitor","hurt_jog","Tkn_hurt_jog",0.05,0.37,0)	
Bladex.AddBipedAction("Knight_Traitor","hurt_head","Tkn_hurt_head",0.10,0.50,0)	
Bladex.AddBipedAction("Knight_Traitor","hurt_breast","Tkn_hurt_breast",0.10,0.50,0)	
Bladex.AddBipedAction("Knight_Traitor","hurt_back","Tkn_hurt_back",0.10,0.53,0)	
Bladex.AddBipedAction("Knight_Traitor","hurt_r_arm","Tkn_hurt_r_arm",0.10,0.50,0)	
Bladex.AddBipedAction("Knight_Traitor","hurt_l_arm","Tkn_hurt_l_arm",0.10,0.50,0)	
Bladex.AddBipedAction("Knight_Traitor","hurt_r_leg","Tkn_hurt_r_leg",0.10,0.50,0)	
Bladex.AddBipedAction("Knight_Traitor","hurt_l_leg","Tkn_hurt_l_leg",0.10,0.54,0)

Bladex.AddBipedAction("Knight_Traitor","df_01","Tkn_df_01",0.10,0.494,0)
Bladex.AddBipedAction("Knight_Traitor","df_02","Tkn_df_02",0.10,0.680,0)

Bladex.AddBipedAction("Knight_Traitor","df_s_broken","Tkn_df_s_broken",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","sw_react","Tkn_sword_reaction",0.10,0.60,0)	
#Bladex.AddBipedAction("Knight_Traitor","sword_broken","Tkn_sword_broken",0.0,1.0,0)


####################################################################################
#
# MUERTES
#
####################################################################################

Bladex.AddBipedAction("Knight_Traitor","dth_c1","Tkn_dth_c1",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","dth_c2","Tkn_dth_c2",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","dth_c3","Tkn_dth_c3",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","dth_c4","Tkn_dth_c4",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","dth_c5","Tkn_dth_c5",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","dth_c6","Tkn_dth_c6",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","dth_c7","Tkn_dth_c7",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","dth0",  "Tkn_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","dth_n00","Tkn_dth_n00",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","dth_n01","Tkn_dth_n01",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","dth_n02","Tkn_dth_n02",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","dth_n03","Tkn_dth_n03",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","dth_n04","Tkn_dth_n04",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","dth_n05","Tkn_dth_n05",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","dth_n06","Tkn_dth_n06",0.0,1.0,0)

Bladex.AddBipedAction("Knight_Traitor","dth_rock","Tkn_dth_rock",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","dth_rockfront","Tkn_dth_rockfront",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","dth_burn","Tkn_dth_burn",0.0,1.0,0)




####################################################################################
#
# Ataques
#
####################################################################################

Bladex.AddBipedAction("Knight_Traitor","g_08","Tkn_g_08",0.0,0.72,0)	
Bladex.AddBipedAction("Knight_Traitor","g_01","Tkn_g_01",0.0,0.69,0)	
Bladex.AddBipedAction("Knight_Traitor","g_02","Tkn_g_02",0.0,0.57,0)	
Bladex.AddBipedAction("Knight_Traitor","g_05","Tkn_g_05",0.0,1.0,0)	
Bladex.AddBipedAction("Knight_Traitor","g_06","Tkn_g_06",0.0,1.0,0)	
Bladex.AddBipedAction("Knight_Traitor","g_07","Tkn_g_07",0.0,0.55,0)	
Bladex.AddBipedAction("Knight_Traitor","g_09","Tkn_g_09",0.0,1.0,0)	

Bladex.AddBipedAction("Knight_Traitor","g_13","Tkn_g_13",0.0,0.69,0)	
Bladex.AddBipedAction("Knight_Traitor","g_18","Tkn_g_18",0.0,0.75,0)	

Bladex.AddBipedAction("Knight_Traitor","g_14","Tkn_g_14",0.0,1.0,0)	
Bladex.AddBipedAction("Knight_Traitor","g_11","Tkn_g_11",0.0,1.0,0)	

Bladex.AddBipedAction("Knight_Traitor","g_16","Tkn_g_16",0.0,0.77,0)	
Bladex.AddBipedAction("Knight_Traitor","g_12","Tkn_g_12",0.0,1.0,0)	

Bladex.AddBipedAction("Knight_Traitor","g_17","Tkn_g_17",0.0,1.0,0)	
Bladex.AddBipedAction("Knight_Traitor","g_15","Tkn_g_15",0.0,1.0,0)	

Bladex.AddBipedAction("Knight_Traitor","g_21","Tkn_g_21",0.0,1.0,0)	
Bladex.AddBipedAction("Knight_Traitor","g_22","Tkn_g_22",0.0,1.0,0)	
Bladex.AddBipedAction("Knight_Traitor","g_23","Tkn_g_23",0.0,1.0,0)	
Bladex.AddBipedAction("Knight_Traitor","g_26","Tkn_g_26",0.0,1.0,0)	
Bladex.AddBipedAction("Knight_Traitor","g_27","Tkn_g_27",0.0,1.0,0)	

Bladex.AddBipedAction("Knight_Traitor","g_31","Tkn_g_31",0.0,1.0,0)



####################################################################################
#
# Burlas
#
####################################################################################

Bladex.AddBipedAction("Knight_Traitor","fury","Tkn_fury",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","laugh","Tkn_laugh",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","alarm01","Tkn_alarm01",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","alarm02","Tkn_alarm02",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","insult","Tkn_insult",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","look_around","Tkn_look_around",0.0,1.0,0)
Bladex.AddBipedAction("Knight_Traitor","attack_look","Tkn_attack_look",0.0,1.0,0)