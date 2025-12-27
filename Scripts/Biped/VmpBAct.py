import Bladex

#import AnimationSets


#AnimationSets.LoadVmpAnimationSet("Vmp")

############################################
#
#Relax
#
############################################

Bladex.AddBipedAction("Vmp","Rlx_1h","Vmp_rlx_f",0.0,1.0,0)	
Bladex.AddBipedAction("Vmp","Rlx_f_1h","Vmp_rlx_f",0.0,1.0,0)	
Bladex.AddBipedAction("Vmp","Rlx_f_2h","Vmp_rlx_f",0.0,1.0,0)	


Bladex.AddBipedAction("Vmp","Rlx_no","Vmp_rlx_f",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","Rlx_b","Vmp_rlx_f",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","Rlx_2h","Vmp_rlx_f",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","Rlx_s","Vmp_rlx_f_s",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","Rlx_block","Vmp_rlx_f_s",0.0,1.0,0)


############################################
#
#Animaciones en combate
#
############################################


Bladex.AddBipedAction("Vmp","Attack_f_1h","Vmp_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","Attack_b_1h","Vmp_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","Attack_r_1h","Vmp_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","Attack_l_1h","Vmp_attack_l",0.0,1.0,0)

Bladex.AddBipedAction("Vmp","Attack_f_2h","Vmp_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","Attack_b_2h","Vmp_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","Attack_r_2h","Vmp_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","Attack_l_2h","Vmp_attack_l",0.0,1.0,0)

Bladex.AddBipedAction("Vmp","Shattack_f_2h","Vmp_attack_f_s",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","Shattack_b_2h","Vmp_attack_b_s",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","Shattack_r_2h","Vmp_attack_r_s",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","Shattack_l_2h","Vmp_attack_l_s",0.0,1.0,0)


#Relax
Bladex.AddBipedAction("Vmp","Shattack_rlx_2h","Vmp_rlx_f_s",0.0,1.0,0)

#Quick turns
#Bladex.AddBipedAction("Vmp","Attack_t_r","Vmp_attack_r",0.0,1.0,0)
#Bladex.AddBipedAction("Vmp","Attack_t_r_s","Vmp_attack_r",0.0,1.0,0)
#Bladex.AddBipedAction("Vmp","Attack_t_l","Vmp_attack_l",0.0,1.0,0)
#Bladex.AddBipedAction("Vmp","Attack_t_l_s","Vmp_attack_l",0.0,1.0,0)


#Dodges
Bladex.AddBipedAction("Vmp","D_b","Vmp_attack_l",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","D_l","Vmp_attack_l",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","D_r","Vmp_attack_r",0.0,1.0,0)

#Correr con escudo en modo no combate                                       
Bladex.AddBipedAction("Vmp","Attack_f_s_nc","Vmp_attack_f_s",0.0,1.0,0)     
Bladex.AddBipedAction("Vmp","Attack_b_s_nc","Vmp_attack_b_s",0.0,1.0,0)     




############################################
#
#Ataques
#
############################################

Bladex.AddBipedAction("Vmp","disappear","Vmp_disappear",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","g_01","Vmp_g_01",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","g_06","Vmp_g_06",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","g_07","Vmp_g_07",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","g_26","Vmp_g_26",0.0,1.0,0)


####################################################################################
#
# Pasos.- Andares
#
####################################################################################


# Andar hacia atrás
Bladex.AddBipedAction("Vmp","WBK_b","Vmp_wbk_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Vmp","WBK_no","Vmp_wbk_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Vmp","WBK_1h","Vmp_wbk_1h",0.0,1.0,0)		
Bladex.AddBipedAction("Vmp","WBK_2h","Vmp_wbk_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Vmp","WBK_s","Vmp_wbk_1h",0.0,1.0,0)

#Andar hacia alante
Bladex.AddBipedAction("Vmp","WLK_b","Vmp_wlk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","WLK_no","Vmp_wlk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","WLK_1h","Vmp_wlk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","WLK_2h","Vmp_wlk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","WLK_s","Vmp_wlk_1h",0.0,1.0,0)

#Correr hacia atrás
Bladex.AddBipedAction("Vmp","JOG_b_b","Vmp_wbk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","JOG_b_no","Vmp_wbk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","JOG_b_s","Vmp_wbk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","JOG_b_1h","Vmp_wbk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","JOG_b_2h","Vmp_wbk_1h",0.0,1.0,0)

#Correr hacia delante
Bladex.AddBipedAction("Vmp","JOG_b","Vmp_wlk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","JOG_no","Vmp_wlk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","JOG_s","Vmp_wlk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","JOG_1h","Vmp_wlk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","JOG_2h","Vmp_wlk_1h",0.0,1.0,0)

#Modo sneak
Bladex.AddBipedAction("Vmp","SNK_b","Vmp_wlk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","SNK_no","Vmp_wlk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","SNK_s","Vmp_wlk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","SNK_1h","Vmp_wlk_1h",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","SNK_2h","Vmp_wlk_1h",0.0,1.0,0)




####################################################################################
#
# Caidas.
#
####################################################################################

Bladex.AddBipedAction("Vmp","FllLow","Vmp_rlx_f",0.37,0.8,0)
Bladex.AddBipedAction("Vmp","FllMed","Vmp_rlx_f",0.37,0.8,0)
Bladex.AddBipedAction("Vmp","FllHigh","Vmp_rlx_f",0.1,0.8,0)
Bladex.AddBipedAction("Vmp","Dth_Fll","Dth_Fll_Vmp",0.0,1.0,0)
Bladex.AddBipedAction("Vmp","Dth_Fll2","Dth_Fll2_Vmp",0.0,1.0,0)




####################################################################################
#
#Heridas
#
####################################################################################




Bladex.AddBipedAction("Vmp","df_01","Vmp_df_01",0.108,0.481,0)	
Bladex.AddBipedAction("Vmp","df_02","Vmp_df_02",0.0,0.630,0)	
Bladex.AddBipedAction("Vmp","df_s_broken","Vmp_df_s_broken",0.0,1.0,0)

Bladex.AddBipedAction("Vmp","sw_react","Vmp_sword_broken",0.143,0.7,0)
	
Bladex.AddBipedAction("Vmp","hurt_f_lite","Vmp_hurt_f_lite",0.0,1.0,0)	
Bladex.AddBipedAction("Vmp","hurt_f_big","Vmp_hurt_f_big",0.0,1.0,0)	

Bladex.AddBipedAction("Vmp","hurt_f_head","Vmp_hurt_f_big",0.0,1.0,0)	
Bladex.AddBipedAction("Vmp","hurt_f_breast","Vmp_hurt_f_big",0.0,1.0,0)	
Bladex.AddBipedAction("Vmp","hurt_f_back","Vmp_hurt_f_lite",0.0,1.0,0)	
Bladex.AddBipedAction("Vmp","hurt_f_r_arm","Vmp_hurt_f_lite",0.0,1.0,0)	
Bladex.AddBipedAction("Vmp","hurt_f_l_arm","Vmp_hurt_f_lite",0.0,1.0,0)	
Bladex.AddBipedAction("Vmp","hurt_f_r_leg","Vmp_hurt_f_lite",0.0,1.0,0)	
Bladex.AddBipedAction("Vmp","hurt_f_l_leg","Vmp_hurt_f_lite",0.0,1.0,0)	

Bladex.AddBipedAction("Vmp","hurt_jog","Vmp_hurt_f_lite",0.0,1.0,0)	

Bladex.AddBipedAction("Vmp","hurt_head","Vmp_hurt_f_big",0.0,1.0,0)	
Bladex.AddBipedAction("Vmp","hurt_breast","Vmp_hurt_f_big",0.0,1.0,0)	
Bladex.AddBipedAction("Vmp","hurt_back","Vmp_hurt_f_lite",0.0,1.0,0)	
Bladex.AddBipedAction("Vmp","hurt_r_arm","Vmp_hurt_f_lite",0.0,1.0,0)	
Bladex.AddBipedAction("Vmp","hurt_l_arm","Vmp_hurt_f_lite",0.0,1.0,0)	
Bladex.AddBipedAction("Vmp","hurt_r_leg","Vmp_hurt_f_lite",0.0,1.0,0)	
Bladex.AddBipedAction("Vmp","hurt_l_leg","Vmp_hurt_f_lite",0.0,1.0,0)	






####################################################################################
#
# Others
#
####################################################################################

Bladex.AddBipedAction("Vmp","slip","Vmp_wlk_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Vmp","slip_b","Vmp_wlk_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Vmp","derrape","Vmp_wlk_1h",0.0,1.0,0)

	
Bladex.AddBipedAction("Vmp","order","Vmp_order",0.0,1.0,0)	
Bladex.AddBipedAction("Vmp","insult","Vmp_insult",0.0,1.0,0)	
Bladex.AddBipedAction("Vmp","patrol","Vmp_patrol",0.0,1.0,0)




	


