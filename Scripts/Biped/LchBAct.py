import Bladex

#import AnimationSets


#AnimationSets.LoadLchAnimationSet("Lch")

####################################################################################
#
# Escalar + saltos
#
####################################################################################

#Bladex.AddBipedAction("Lch","clmb_low_1h","Lch_clmb_low_1h",0.0,1.0,0)	
#Bladex.AddBipedAction("Lch","clmb_medlow_1h","Lch_clmb_medlow_1h",0.0,1.0,0)	
#Bladex.AddBipedAction("Lch","clmb_medium_1h","Lch_clmb_medium_1h",0.0,1.0,0)	
#Bladex.AddBipedAction("Lch","clmb_high_1h","Lch_clmb_high_1h",0.0,1.0,0)	

Bladex.AddBipedAction("Lch","LongJump1H","Wlk_1h_Lch", 0.0, 1.0, 0)	
Bladex.AddBipedAction("Lch","LongJumpNo","Wlk_1h_Lch",0.0,1.0,0)	
Bladex.AddBipedAction("Lch","ShortJump","Wlk_1h_Lch",0.0,1.0,0)	



####################################################################################
#
# Others
#
####################################################################################

Bladex.AddBipedAction("Lch","slip","Lch_slip",0.0,1.0,0)
Bladex.AddBipedAction("Lch","slip_b","Lch_slip_b",0.0,1.0,0)
Bladex.AddBipedAction("Lch","derrape","Lch_derrape",0.0,1.0,0)

Bladex.AddBipedAction("Lch","appears1","Lch_appears1",0.0,1.0,0)

####################################################################################
#
# Relax.
#
####################################################################################

Bladex.AddBipedAction("Lch","Rlx_no","Rlx_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Rlx_1h","Rlx_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Rlx_b","Rlx_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Rlx_2h","Rlx_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Rlx_s","Rlx_1h_Lch",0.0,1.0,0)

####################################################################################
#
# Pasos.- Andares
#
####################################################################################

#Bladex.AddBipedAction("Lch","LStepUp","Wlk_Lch","Wlk_1h_Lch",0.0,0.5,0)
#Bladex.AddBipedAction("Lch","RStepUp","Wlk_Lch","Wlk_1h_Lch",0.5,1.0,0)

#Bladex.AddBipedAction("Lch","LStairsUp","StairsUp_Lch","StairsUpP_Lch",0.0,0.5,0)
#Bladex.AddBipedAction("Lch","RStairsUp","StairsUp_Lch","StairsUpP_Lch",0.5,1.0,0)

#Bladex.AddBipedAction("Lch","LStepDown","Wlk_Lch","WlkDown_Lch",0.0,0.5,0)
#Bladex.AddBipedAction("Lch","RStepDown","Wlk_Lch","WlkDown_Lch",0.5,1.0,0)

#Bladex.AddBipedAction("Lch","LStairsDown","StairsDown_Lch",0.0,0.5,0)
#Bladex.AddBipedAction("Lch","RStairsDown","StairsDown_Lch",0.5,1.0,0)

# Andar hacia atrás
Bladex.AddBipedAction("Lch","WBK_b","Lch_wbk_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Lch","WBK_no","Lch_wbk_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Lch","WBK_1h","Lch_wbk_1h",0.0,1.0,0)		
Bladex.AddBipedAction("Lch","WBK_2h","Lch_wbk_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Lch","WBK_s","Lch_wbk_1h",0.0,1.0,0)

#Andar hacia alante
Bladex.AddBipedAction("Lch","WLK_b","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","WLK_no","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","WLK_1h","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","WLK_2h","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","WLK_s","Wlk_1h_Lch",0.0,1.0,0)

#Correr hacia atrás
Bladex.AddBipedAction("Lch","WBK_JOG_b","Lch_wbk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Lch","WBK_JOG_no","Lch_wbk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Lch","WBK_JOG_s","Lch_wbk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Lch","WBK_JOG_1h","Lch_wbk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Lch","WBK_JOG_2h","Lch_wbk_1h",0.0,1.0,0)

#Correr hacia delante
Bladex.AddBipedAction("Lch","JOG_b","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","JOG_no","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","JOG_s","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","JOG_1h","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","JOG_2h","Wlk_1h_Lch",0.0,1.0,0)


#Modo sneak
Bladex.AddBipedAction("Lch","SNK_b","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","SNK_no","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","SNK_s","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","SNK_1h","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","SNK_2h","Wlk_1h_Lch",0.0,1.0,0)




####################################################################################
#
# Caidas.
#
####################################################################################

Bladex.AddBipedAction("Lch","FllLow","Wlk_1h_Lch",0.5,0.8,0)
Bladex.AddBipedAction("Lch","FllMed","Wlk_1h_Lch",0.37,0.8,0)
Bladex.AddBipedAction("Lch","FllHigh","Wlk_1h_Lch",0.1,0.8,0)
Bladex.AddBipedAction("Lch","Dth_Fll","Dth_Fll_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Dth_Fll2","Dth_Fll2_Lch",0.0,1.0,0)




####################################################################################
#
# MUERTES
#
####################################################################################

Bladex.AddBipedAction("Lch","dth_c1", "Lch_dth_c1",0.0,1.0,0)
Bladex.AddBipedAction("Lch","dth_c2", "Lch_dth_c2",0.0,1.0,0)
Bladex.AddBipedAction("Lch","dth_c3", "Lch_dth_c3",0.0,1.0,0)
Bladex.AddBipedAction("Lch","dth_c4", "Lch_dth_c4",0.0,1.0,0)
Bladex.AddBipedAction("Lch","dth_c5", "Lch_dth_c5",0.0,1.0,0)
Bladex.AddBipedAction("Lch","dth_c6", "Lch_dth_c6",0.0,1.0,0)
Bladex.AddBipedAction("Lch","dth_c7", "Lch_dth_c7",0.0,1.0,0)
Bladex.AddBipedAction("Lch","dth0",   "Lch_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Lch","dth_n00","Lch_dth_n00",0.0,1.0,0)
Bladex.AddBipedAction("Lch","dth_n01","Lch_dth_n01",0.0,1.0,0)
Bladex.AddBipedAction("Lch","dth_n02","Lch_dth_n02",0.0,1.0,0)
Bladex.AddBipedAction("Lch","dth_n03","Lch_dth_n03",0.0,1.0,0)
Bladex.AddBipedAction("Lch","dth_n04","Lch_dth_n04",0.0,1.0,0)
Bladex.AddBipedAction("Lch","dth_n05","Lch_dth_n05",0.0,1.0,0)
Bladex.AddBipedAction("Lch","dth_n06","Lch_dth_n06",0.0,1.0,0)

Bladex.AddBipedAction("Lch","dth_rock","Lch_dth_n02",0.0,1.0,0)
Bladex.AddBipedAction("Lch","dth_rockfront","Lch_dth_n02",0.0,1.0,0)
Bladex.AddBipedAction("Lch","dth_burn","Lch_dth_c7",0.0,1.0,0)


####################################################################################
#
# HERIDAS
#
####################################################################################


	
Bladex.AddBipedAction("Lch","hurt_f_lite","Lch_hurt_lite",0.0,1.0,0)	
Bladex.AddBipedAction("Lch","hurt_f_big","Lch_hurt_big",0.0,1.0,0)	

Bladex.AddBipedAction("Lch","hurt_f_head","Lch_hurt_big2",0.0,1.0,0)	
Bladex.AddBipedAction("Lch","hurt_f_breast","Lch_hurt_big",0.0,1.0,0)	
Bladex.AddBipedAction("Lch","hurt_f_back","Lch_hurt_lite",0.0,1.0,0)	
Bladex.AddBipedAction("Lch","hurt_f_r_arm","Lch_hurt_lite",0.0,1.0,0)	
Bladex.AddBipedAction("Lch","hurt_f_l_arm","Lch_hurt_lite",0.0,1.0,0)	
Bladex.AddBipedAction("Lch","hurt_f_r_leg","Lch_hurt_lite",0.0,1.0,0)	
Bladex.AddBipedAction("Lch","hurt_f_l_leg","Lch_hurt_lite",0.0,1.0,0)	

Bladex.AddBipedAction("Lch","hurt_jog","Lch_hurt_big",0.0,1.0,0)	

Bladex.AddBipedAction("Lch","hurt_head","Lch_hurt_big",0.0,1.0,0)	
Bladex.AddBipedAction("Lch","hurt_breast","Lch_hurt_big",0.0,1.0,0)	
Bladex.AddBipedAction("Lch","hurt_back","Lch_hurt_big2",0.0,1.0,0)	
Bladex.AddBipedAction("Lch","hurt_r_arm","Lch_hurt_lite",0.0,1.0,0)	
Bladex.AddBipedAction("Lch","hurt_l_arm","Lch_hurt_lite",0.0,1.0,0)	
Bladex.AddBipedAction("Lch","hurt_r_leg","Lch_hurt_lite",0.0,1.0,0)	
Bladex.AddBipedAction("Lch","hurt_l_leg","Lch_hurt_lite",0.0,1.0,0)



####################################################################################
#
# Animaciones en combate
#
####################################################################################

#MOvement without shield
Bladex.AddBipedAction("Lch","Attack_f_1h","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Attack_b_1h","Lch_wbk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Attack_r_1h","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Attack_l_1h","Wlk_1h_Lch",0.0,1.0,0)

Bladex.AddBipedAction("Lch","Attack_f_no","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Attack_b_no","Lch_wbk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Attack_r_no","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Attack_l_no","Wlk_1h_Lch",0.0,1.0,0)

Bladex.AddBipedAction("Lch","Attack_f_2h","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Attack_b_2h","Lch_wbk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Attack_r_2h","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Attack_l_2h","Wlk_1h_Lch",0.0,1.0,0)


#Movement with shield
Bladex.AddBipedAction("Lch","Shattack_f_2h","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Shattack_b_2h","Lch_wbk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Shattack_r_2h","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Shattack_l_2h","Wlk_1h_Lch",0.0,1.0,0)

#MOvement without weapon but with shield
Bladex.AddBipedAction("Lch","Attack_f_s","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Attack_b_s","Lch_wbk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Attack_r_s","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Attack_l_s","Wlk_1h_Lch",0.0,1.0,0)

#MOvement without weapon with shield BEING raised
Bladex.AddBipedAction("Lch","Shattack_f_s","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Shattack_b_s","Lch_wbk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Shattack_r_s","Wlk_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Shattack_l_s","Wlk_1h_Lch",0.0,1.0,0)

#Relax
Bladex.AddBipedAction("Lch","Rlx_f_1h","Rlx_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Rlx_f_no","Rlx_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Rlx_f_2h","Rlx_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Shattack_rlx_2h","Rlx_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","attack_rlx_s","Rlx_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Shattack_rlx_s","Rlx_1h_Lch",0.0,1.0,0)
Bladex.AddBipedAction("Lch","Rlx_f_s","Rlx_1h_Lch",0.0,1.0,0)

#Quick turns
#Bladex.AddBipedAction("Lch","Attack_t_r","Wlk_1h_Lch",0.0,1.0,0)
#Bladex.AddBipedAction("Lch","Attack_t_r_s","Wlk_1h_Lch",0.0,1.0,0)
#Bladex.AddBipedAction("Lch","Attack_t_l","Wlk_1h_Lch",0.0,1.0,0)
#Bladex.AddBipedAction("Lch","Attack_t_l_s","Wlk_1h_Lch",0.0,1.0,0)


#Dodges
#Bladex.AddBipedAction("Lch","D_b","Rlx_1h_Lch",0.0,1.0,0)
#Bladex.AddBipedAction("Lch","D_l","Rlx_1h_Lch",0.0,1.0,0)
#Bladex.AddBipedAction("Lch","D_r","Rlx_1h_Lch",0.0,1.0,0)

#Bladex.AddBipedAction("Lch","alarm01","Rlx_1h_Lch",0.0,1.0,0)
#Bladex.AddBipedAction("Lch","fury","Rlx_1h_Lch",0.0,1.0,0)
#Bladex.AddBipedAction("Lch","look_around","Rlx_1h_Lch",0.0,1.0,0)


####################################################################################
#
# Ataques
#
####################################################################################

Bladex.AddBipedAction("Lch","g_spit","Lch_g_spit",0.0,1.0,0)
Bladex.AddBipedAction("Lch","g_13","Lch_g_13",0.0,1.0,0)	
Bladex.AddBipedAction("Lch","g_18","Lch_g_18",0.0,1.0,0)
Bladex.AddBipedAction("Lch","g_16","Lch_g_16",0.0,1.0,0)	
Bladex.AddBipedAction("Lch","g_12","Lch_g_12",0.0,1.0,0)
Bladex.AddBipedAction("Lch","g_claw1","Lch_g_claw1",0.0,1.0,0)	
Bladex.AddBipedAction("Lch","g_claw2","Lch_g_claw2",0.0,1.0,0)	
Bladex.AddBipedAction("Lch","g_claw3","Lch_g_claw3",0.0,1.0,0)


####################################################################################
#
# Animaciones de giro
#
####################################################################################

#Giro no encarando
#Bladex.AddBipedAction("Lch","Turn_l","Lch_t_l_1h",0.0,1.0,0)
#Bladex.AddBipedAction("Lch","Turn_r","Lch_t_r_1h",0.0,1.0,0)




