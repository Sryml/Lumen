import Bladex

#import AnimationSets


#AnimationSets.LoadSklAnimationSet("Skl")

####################################################################################
#
# Escalar + saltos
#
####################################################################################

Bladex.AddBipedAction("Skl","clmb_low_1h","Skl_clmb_low",0.25,0.8,0)	
Bladex.AddBipedAction("Skl","clmb_medlow_1h","Skl_clmb_low",0.25,0.8,0)	
Bladex.AddBipedAction("Skl","clmb_medium_1h","Skl_clmb_low",0.25,0.8,0)	
Bladex.AddBipedAction("Skl","clmb_high_1h","Skl_clmb_low",0.25,0.8,0)	

Bladex.AddBipedAction("Skl","LongJump1H","Skl_jmp_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Skl","LongJumpNo","Skl_jmp_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Skl","ShortJump","Skl_jmp_1h",0.0,1.0,0)	



####################################################################################
#
# Others
#
####################################################################################

Bladex.AddBipedAction("Skl","slip","Skl_slip",0.0,1.0,0)	
Bladex.AddBipedAction("Skl","slip_b","Skl_slip_b",0.0,1.0,0)	
Bladex.AddBipedAction("Skl","derrape","Skl_derrape",0.0,1.0,0)	


#Bladex.AddBipedAction("Skl","LookArround","Skl_patrol1",0.0,1.0,0)	

Bladex.AddBipedAction("Skl","b1","Skl_b1",0.0,1.0,0)	
Bladex.AddBipedAction("Skl","b2","Skl_b2",0.0,1.0,0)	
Bladex.AddBipedAction("Skl","b3","Skl_b3",0.0,1.0,0)	

Bladex.AddBipedAction("Skl","appears1","Skl_appears1",0.0,1.0,0)

####################################################################################
#
# Relax.
#
####################################################################################

Bladex.AddBipedAction("Skl","Rlx_no","Rlx_1h_Skl",0.0,1.0,0)
Bladex.AddBipedAction("Skl","Rlx_1h","Rlx_1h_Skl",0.0,1.0,0)
Bladex.AddBipedAction("Skl","Rlx_b","Rlx_1h_Skl",0.0,1.0,0)
Bladex.AddBipedAction("Skl","Rlx_2h","Rlx_1h_Skl",0.0,1.0,0)
Bladex.AddBipedAction("Skl","Rlx_s","Rlx_1h_Skl",0.0,1.0,0)

####################################################################################
#
# Pasos.- Andares
#
####################################################################################

#Bladex.AddBipedAction("Skl","LStepUp","Wlk_Skl","WlkUp_Skl",0.0,0.5,0)
#Bladex.AddBipedAction("Skl","RStepUp","Wlk_Skl","WlkUp_Skl",0.5,1.0,0)

#Bladex.AddBipedAction("Skl","LStairsUp","StairsUp_Skl","StairsUpP_Skl",0.0,0.5,0)
#Bladex.AddBipedAction("Skl","RStairsUp","StairsUp_Skl","StairsUpP_Skl",0.5,1.0,0)


#Bladex.AddBipedAction("Skl","ShortStep","Wlk_1h_Skl", 0.0,1.0,0)

#Bladex.AddBipedAction("Skl","LStepDown","Wlk_Skl","WlkDown_Skl",0.0,0.5,0)
#Bladex.AddBipedAction("Skl","RStepDown","Wlk_Skl","WlkDown_Skl",0.5,1.0,0)

#Bladex.AddBipedAction("Skl","LStairsDown","StairsDown_Skl",0.0,0.5,0)
#Bladex.AddBipedAction("Skl","RStairsDown","StairsDown_Skl",0.5,1.0,0)

# Andar hacia atrás
Bladex.AddBipedAction("Skl","WBK_b","Skl_attack_b",0.0,1.0,0)	
Bladex.AddBipedAction("Skl","WBK_no","Skl_attack_b",0.0,1.0,0)	
Bladex.AddBipedAction("Skl","WBK_1h","Skl_attack_b",0.0,1.0,0)		
Bladex.AddBipedAction("Skl","WBK_2h","Skl_attack_b",0.0,1.0,0)	
Bladex.AddBipedAction("Skl","WBK_s","Skl_attack_b",0.0,1.0,0)

#Andar hacia alante
Bladex.AddBipedAction("Skl","WLK_b","Wlk_b_Skl",0.0,1.0,0)
Bladex.AddBipedAction("Skl","WLK_no","Wlk_1h_Skl",0.0,1.0,0)
Bladex.AddBipedAction("Skl","WLK_1h","Wlk_1h_Skl",0.0,1.0,0)
Bladex.AddBipedAction("Skl","WLK_2h","Wlk_1h_Skl",0.0,1.0,0)
Bladex.AddBipedAction("Skl","WLK_s","Wlk_1h_Skl",0.0,1.0,0)

#Correr hacia atrás
Bladex.AddBipedAction("Skl","WBK_JOG_b","Skl_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Skl","WBK_JOG_no","Skl_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Skl","WBK_JOG_s","Skl_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Skl","WBK_JOG_1h","Skl_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Skl","WBK_JOG_2h","Skl_attack_b",0.0,1.0,0)

#Correr hacia delante
Bladex.AddBipedAction("Skl","JOG_b","Jog_1h_Skl",0.0,1.0,0)
Bladex.AddBipedAction("Skl","JOG_no","Jog_1h_Skl",0.0,1.0,0)
Bladex.AddBipedAction("Skl","JOG_s","Jog_1h_Skl",0.0,1.0,0)
Bladex.AddBipedAction("Skl","JOG_1h","Jog_1h_Skl",0.0,1.0,0)
Bladex.AddBipedAction("Skl","JOG_2h","Jog_1h_Skl",0.0,1.0,0)


#Modo sneak
Bladex.AddBipedAction("Skl","SNK_b","Snk_b_Skl",0.0,1.0,0)
Bladex.AddBipedAction("Skl","SNK_no","Snk_no_Skl",0.0,1.0,0)
Bladex.AddBipedAction("Skl","SNK_s","Snk_no_Skl",0.0,1.0,0)
Bladex.AddBipedAction("Skl","SNK_1h","Snk_1h_Skl",0.0,1.0,0)
Bladex.AddBipedAction("Skl","SNK_2h","Snk_1h_Skl",0.0,1.0,0)




####################################################################################
#
# Caidas.
#
####################################################################################

Bladex.AddBipedAction("Skl","FllLow","FallMed_Skl",0.23,0.9,0)
Bladex.AddBipedAction("Skl","FllMed","FallMed_Skl",0.23,0.9,0)
Bladex.AddBipedAction("Skl","FllHigh","FallMed_Skl",0.23,0.9,0)
Bladex.AddBipedAction("Skl","Dth_Fll","Dth_Fll_Skl",0.0,1.0,0)
Bladex.AddBipedAction("Skl","Dth_Fll2","Dth_Fll2_Skl",0.0,1.0,0)





####################################################################################
#
# Animaciones en combate
#
####################################################################################

#MOvement without shield
Bladex.AddBipedAction("Skl","Attack_f_1h","Skl_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Skl","Attack_b_1h","Skl_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Skl","Attack_r_1h","Skl_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Skl","Attack_l_1h","Skl_attack_l",0.0,1.0,0)

Bladex.AddBipedAction("Skl","Attack_f_2h","Skl_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Skl","Attack_b_2h","Skl_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Skl","Attack_r_2h","Skl_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Skl","Attack_l_2h","Skl_attack_l",0.0,1.0,0)

#Movement with shield
Bladex.AddBipedAction("Skl","Shattack_f_2h","Skl_attack_f_s",0.0,1.0,0)
Bladex.AddBipedAction("Skl","Shattack_b_2h","Skl_attack_b_s",0.0,1.0,0)
Bladex.AddBipedAction("Skl","Shattack_r_2h","Skl_attack_r_s",0.0,1.0,0)
Bladex.AddBipedAction("Skl","Shattack_l_2h","Skl_attack_l_s",0.0,1.0,0)

Bladex.AddBipedAction("Skl","Attack_b_s_nc","Skl_attack_b_s",0.0,1.0,0)
Bladex.AddBipedAction("Skl","Attack_f_s_nc","Skl_attack_f_s",0.0,1.0,0)

#Relax
Bladex.AddBipedAction("Skl","Rlx_f_1h","Rlx_1h_Skl",0.0,1.0,0)
Bladex.AddBipedAction("Skl","Rlx_f_2h","Rlx_1h_Skl",0.0,1.0,0)
Bladex.AddBipedAction("Skl","Shattack_rlx_2h","Rlx_1h_Skl",0.0,1.0,0)

#Quick turns
#Bladex.AddBipedAction("Skl","Attack_t_r","Skl_attack_t_r",0.0,1.0,0)
#Bladex.AddBipedAction("Skl","Attack_t_r_s","Skl_attack_t_r_s",0.0,1.0,0)
#Bladex.AddBipedAction("Skl","Attack_t_l","Skl_attack_t_l",0.0,1.0,0)
#Bladex.AddBipedAction("Skl","Attack_t_l_s","Skl_attack_t_l_s",0.0,1.0,0)


#Dodges
Bladex.AddBipedAction("Skl","D_b","Skl_attack_b_s",0.0,1.0,0)
Bladex.AddBipedAction("Skl","D_l","Skl_attack_l_s",0.0,1.0,0)
Bladex.AddBipedAction("Skl","D_r","Skl_attack_r_s",0.0,1.0,0)



####################################################################################
#
# Ataques
#
####################################################################################

	
Bladex.AddBipedAction("Skl","g_01","Skl_g_01",0.0,1.0,0)	
Bladex.AddBipedAction("Skl","g_02","Skl_g_02",0.0,1.0,0)	
Bladex.AddBipedAction("Skl","g_07","Skl_g_07",0.0,1.0,0)	
Bladex.AddBipedAction("Skl","g_09","Skl_g_09",0.0,1.0,0)
Bladex.AddBipedAction("Skl","g_16","Skl_g_16",0.0,1.0,0)
Bladex.AddBipedAction("Skl","g_18","Skl_g_18",0.0,1.0,0)	
Bladex.AddBipedAction("Skl","g_22","Skl_g_22",0.0,1.0,0)



####################################################################################
#
# Animaciones de giro
#
####################################################################################

#Giro no encarando
#Bladex.AddBipedAction("Skl","Turn_l","Skl_t_l_1h",0.0,1.0,0)
#Bladex.AddBipedAction("Skl","Turn_r","Skl_t_r_1h",0.0,1.0,0)


####################################################################################
#
# Reacciones
#
####################################################################################




Bladex.AddBipedAction("Skl","sw_react","Skl_sword_reaction",0.143,0.8,0)	




###########################
#                         #
#     Añadidos Luismi     #
#                         #
###########################


Bladex.AddBipedAction("Skl","Chg_r_l","Skl_attack_chg_r_l",0.0,1.0,0)
Bladex.AddBipedAction("Skl","Attack_Chg_r_l","Skl_attack_chg_r_l",0.0,1.0,0)

Bladex.AddBipedAction("Skl","look_around","Skl_patrol1",0.0,1.0,0)

Bladex.AddBipedAction("Skl","alarm01","Skl_alarm01",0.0,1.0,0)
#Bladex.AddBipedAction("Skl","alarm02","Skl_alarm02",0.0,1.0,0)
#Bladex.AddBipedAction("Skl","fury","Skl_fury",0.0,1.0,0)


Bladex.AddBipedAction("Skl","df_s_broken","Skl_df_s_broken",0.0,1.0,0)


#### Muertes

Bladex.AddBipedAction("Skl","dth_c1","Skl_dth_c1",0.0,1.0,0)
Bladex.AddBipedAction("Skl","dth_c2","Skl_dth_c2",0.0,1.0,0)
Bladex.AddBipedAction("Skl","dth_c3","Skl_dth_c3",0.0,1.0,0)
Bladex.AddBipedAction("Skl","dth_c4","Skl_dth_c4",0.0,1.0,0)
Bladex.AddBipedAction("Skl","dth_c5","Skl_dth_c5",0.0,1.0,0)
Bladex.AddBipedAction("Skl","dth_c6","Skl_dth_c6",0.0,1.0,0)
Bladex.AddBipedAction("Skl","dth_c7","Skl_dth_c7",0.0,1.0,0)
Bladex.AddBipedAction("Skl","dth0",  "Skl_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Skl","dth_n00","Skl_dth_n00",0.0,1.0,0)
Bladex.AddBipedAction("Skl","dth_n01","Skl_dth_n01",0.0,1.0,0)
Bladex.AddBipedAction("Skl","dth_n02","Skl_dth_n02",0.0,1.0,0)
Bladex.AddBipedAction("Skl","dth_n03","Skl_dth_n03",0.0,1.0,0)
Bladex.AddBipedAction("Skl","dth_n04","Skl_dth_n04",0.0,1.0,0)
Bladex.AddBipedAction("Skl","dth_n05","Skl_dth_n05",0.0,1.0,0)
Bladex.AddBipedAction("Skl","dth_n06","Skl_dth_n06",0.0,1.0,0)

Bladex.AddBipedAction("Skl","dth_rock","Skl_dth_rock",0.0,1.0,0)
Bladex.AddBipedAction("Skl","dth_rockfront","Skl_dth_rockfront",0.0,1.0,0)
Bladex.AddBipedAction("Skl","dth_burn","Skl_dth_burn",0.0,1.0,0)


##### Heridas


Bladex.AddBipedAction("Skl","hurt_f_lite","Skl_hurt_f_lite",0.14,0.65,0)	
Bladex.AddBipedAction("Skl","hurt_f_big","Skl_hurt_f_big",0.10,0.59,0)	
Bladex.AddBipedAction("Skl","hurt_f_head","Skl_hurt_f_head",0.11,0.60,0)	
Bladex.AddBipedAction("Skl","hurt_f_breast","Skl_hurt_f_breast",0.11,0.58,0)	
Bladex.AddBipedAction("Skl","hurt_f_back","Skl_hurt_back",0.10,0.53,0)	
Bladex.AddBipedAction("Skl","hurt_f_r_arm","Skl_hurt_f_r_arm",0.10,0.55,0)	
Bladex.AddBipedAction("Skl","hurt_f_l_arm","Skl_hurt_f_l_arm",0.10,0.58,0)	
Bladex.AddBipedAction("Skl","hurt_f_r_leg","Skl_hurt_f_r_leg",0.10,0.54,0)	
Bladex.AddBipedAction("Skl","hurt_f_l_leg","Skl_hurt_f_l_leg",0.10,0.56,0)	
Bladex.AddBipedAction("Skl","hurt_jog","Skl_hurt_back",0.10,0.53,0)	
Bladex.AddBipedAction("Skl","hurt_head","Skl_hurt_f_head",0.11,0.60,0)	
Bladex.AddBipedAction("Skl","hurt_breast","Skl_hurt_f_breast",0.11,0.58,0)	
Bladex.AddBipedAction("Skl","hurt_back","Skl_hurt_back",0.10,0.53,0)	
Bladex.AddBipedAction("Skl","hurt_r_arm","Skl_hurt_f_r_arm",0.10,0.55,0)	
Bladex.AddBipedAction("Skl","hurt_l_arm","Skl_hurt_f_l_arm",0.10,0.58,0)
Bladex.AddBipedAction("Skl","hurt_r_leg","Skl_hurt_f_r_leg",0.10,0.54,0)	
Bladex.AddBipedAction("Skl","hurt_l_leg","Skl_hurt_f_l_leg",0.10,0.56,0)

Bladex.AddBipedAction("Skl","df_01","Skl_df_01",0.10,0.48,0)
Bladex.AddBipedAction("Skl","df_02","Skl_df_02",0.10,0.60,0)