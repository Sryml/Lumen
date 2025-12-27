import Bladex

#import AnimationSets


#AnimationSets.LoadSlmAnimationSet("Slm")

####################################################################################
#
# Escalar + saltos
#
####################################################################################

Bladex.AddBipedAction("Slm","clmb_low_1h","Slm_clmb_low",0.0,1.0,0)	
Bladex.AddBipedAction("Slm","clmb_medlow_1h","Slm_clmb_low",0.0,1.0,0)	
Bladex.AddBipedAction("Slm","clmb_medium_1h","Slm_clmb_low",0.0,1.0,0)	
Bladex.AddBipedAction("Slm","clmb_high_1h","Slm_clmb_low",0.0,1.0,0)	

Bladex.AddBipedAction("Slm","LongJump1H","Wlk_no_Slm",0.0,1.0,0)	
Bladex.AddBipedAction("Slm","LongJumpNo","Wlk_no_Slm",0.0,1.0,0)	
Bladex.AddBipedAction("Slm","ShortJump","Wlk_no_Slm",0.0,1.0,0)	



####################################################################################
#
# Others
#
####################################################################################

Bladex.AddBipedAction("Slm","slip","Wlk_no_Slm",0.0,1.0,0)	
Bladex.AddBipedAction("Slm","slip_b","Wlk_no_Slm",0.0,1.0,0)	
Bladex.AddBipedAction("Slm","derrape","Wlk_no_Slm",0.0,1.0,0)	



####################################################################################
#
# Relax.
#
####################################################################################

Bladex.AddBipedAction("Slm","Rlx_no","Rlx_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","Rlx_1h","Rlx_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","Rlx_b","Rlx_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","Rlx_2h","Rlx_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","Rlx_s","Rlx_no_Slm",0.0,1.0,0)

####################################################################################
#
# Pasos.- Andares
#
####################################################################################


#Bladex.AddBipedAction("Slm","LStepShort","Wlk_no_Slm",0.0,0.5,0)
#Bladex.AddBipedAction("Slm","RStepShort","Wlk_no_Slm",0.5,1.0,0)

#Bladex.AddBipedAction("Slm","LStepUp","Wlk_Slm","Wlk_no_Slm",0.0,0.5,0)
#Bladex.AddBipedAction("Slm","RStepUp","Wlk_Slm","Wlk_no_Slm",0.5,1.0,0)

#Bladex.AddBipedAction("Slm","LStairsUp","StairsUp_Slm","Wlk_no_Slm",0.0,0.5,0)
#Bladex.AddBipedAction("Slm","RStairsUp","StairsUp_Slm","Wlk_no_Slm",0.5,1.0,0)

#Bladex.AddBipedAction("Slm","LStepDown","Wlk_Slm","Wlk_no_Slm",0.0,0.5,0)
#Bladex.AddBipedAction("Slm","RStepDown","Wlk_Slm","Wlk_no_Slm",0.5,1.0,0)

#Bladex.AddBipedAction("Slm","LStairsDown","Wlk_no_Slm",0.0,0.5,0)
#Bladex.AddBipedAction("Slm","RStairsDown","Wlk_no_Slm",0.5,1.0,0)

# Andar hacia atrás
Bladex.AddBipedAction("Slm","WBK_b","Wbk_no_Slm",0.0,1.0,0)	
Bladex.AddBipedAction("Slm","WBK_no","Wbk_no_Slm",0.0,1.0,0)	
Bladex.AddBipedAction("Slm","WBK_1h","Wbk_no_Slm",0.0,1.0,0)		
Bladex.AddBipedAction("Slm","WBK_2h","Wbk_no_Slm",0.0,1.0,0)	
Bladex.AddBipedAction("Slm","WBK_s","Wbk_no_Slm",0.0,1.0,0)

#Andar hacia alante
Bladex.AddBipedAction("Slm","WLK_b","Jog_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","WLK_no","Jog_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","WLK_1h","Jog_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","WLK_2h","Jog_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","WLK_s","Jog_no_Slm",0.0,1.0,0)

#Correr hacia atrás
Bladex.AddBipedAction("Slm","WBK_JOG_b","Wbk_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","WBK_JOG_no","Wbk_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","WBK_JOG_s","Wbk_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","WBK_JOG_1h","Wbk_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","WBK_JOG_2h","Wbk_no_Slm",0.0,1.0,0)

#Correr hacia delante
Bladex.AddBipedAction("Slm","JOG_b","Jog_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","JOG_no","Jog_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","JOG_s","Jog_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","JOG_1h","Jog_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","JOG_2h","Jog_no_Slm",0.0,1.0,0)


#Modo sneak
Bladex.AddBipedAction("Slm","SNK_b","Wlk_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","SNK_no","Wlk_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","SNK_s","Wlk_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","SNK_1h","Wlk_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","SNK_2h","Wlk_no_Slm",0.0,1.0,0)




####################################################################################
#
# Caidas.
#
####################################################################################

Bladex.AddBipedAction("Slm","FllLow","FallLow_Slm",0.37,0.8,0)
Bladex.AddBipedAction("Slm","FllMed","FallHigh_Slm",0.37,0.8,0)
Bladex.AddBipedAction("Slm","FllHigh","FallHigh_Slm",0.1,0.8,0)
Bladex.AddBipedAction("Slm","Dth_Fll","Dth_Fll_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","Dth_Fll2","Dth_Fll2_Slm",0.0,1.0,0)


####################################################################################
#
# Muertes
#
####################################################################################

Bladex.AddBipedAction("Slm","dth0","Slm_hurt_f_big",0.0,0.294,0)
Bladex.AddBipedAction("Slm","dth_c1","Slm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Slm","dth_c2","Slm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Slm","dth_c3","Slm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Slm","dth_c4","Slm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Slm","dth_c5","Slm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Slm","dth_c6","Slm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Slm","dth_c7","Slm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Slm","dth0",  "Slm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Slm","dth_n00","Slm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Slm","dth_n01","Slm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Slm","dth_n02","Slm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Slm","dth_n03","Slm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Slm","dth_n04","Slm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Slm","dth_n05","Slm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Slm","dth_n06","Slm_dth0",0.0,1.0,0)
                       
Bladex.AddBipedAction("Slm","dth_rock","Slm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Slm","dth_rockfront","Slm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Slm","dth_burn","Slm_dth0",0.0,1.0,0)	


####################################################################################
#
# Heridas
#
####################################################################################

Bladex.AddBipedAction("Slm","hurt_f_lite","Slm_hurt_f_lite",0.0,1.0,0)
Bladex.AddBipedAction("Slm","hurt_f_big","Slm_hurt_f_big",0.0,1.0,0)
Bladex.AddBipedAction("Slm","hurt_f_head","Slm_hurt_f_big",0.0,1.0,0)
Bladex.AddBipedAction("Slm","hurt_f_breast","Slm_hurt_f_lite",0.0,1.0,0)
Bladex.AddBipedAction("Slm","hurt_f_back","Slm_hurt_f_lite",0.0,1.0,0)
Bladex.AddBipedAction("Slm","hurt_f_r_arm","Slm_hurt_f_lite",0.0,1.0,0)
Bladex.AddBipedAction("Slm","hurt_f_l_arm","Slm_hurt_f_lite",0.0,1.0,0)
Bladex.AddBipedAction("Slm","hurt_f_r_leg","Slm_hurt_f_lite",0.0,1.0,0)
Bladex.AddBipedAction("Slm","hurt_f_l_leg","Slm_hurt_f_lite",0.0,1.0,0)
Bladex.AddBipedAction("Slm","hurt_jog","Slm_hurt_f_big",0.0,1.0,0)
Bladex.AddBipedAction("Slm","hurt_head","Slm_hurt_f_big",0.0,1.0,0)
Bladex.AddBipedAction("Slm","hurt_breast","Slm_hurt_f_lite",0.0,1.0,0)
Bladex.AddBipedAction("Slm","hurt_back","Slm_hurt_f_lite",0.0,1.0,0)
Bladex.AddBipedAction("Slm","hurt_r_arm","Slm_hurt_f_lite",0.0,1.0,0)
Bladex.AddBipedAction("Slm","hurt_l_arm","Slm_hurt_f_lite",0.0,1.0,0)
Bladex.AddBipedAction("Slm","hurt_r_leg","Slm_hurt_f_lite",0.0,1.0,0)
Bladex.AddBipedAction("Slm","hurt_l_leg","Slm_hurt_f_lite",0.0,1.0,0)



####################################################################################
#
# Animaciones en combate
#
####################################################################################

#MOvement without shield
#Bladex.AddBipedAction("Slm","Attack_f_1h","Wlk_no_Slm",0.0,1.0,0)
#Bladex.AddBipedAction("Slm","Attack_b_1h","Wbk_no_Slm",0.0,1.0,0)
#Bladex.AddBipedAction("Slm","Attack_r_1h","Wlk_no_Slm",0.0,1.0,0)
#Bladex.AddBipedAction("Slm","Attack_l_1h","Wlk_no_Slm",0.0,1.0,0)


Bladex.AddBipedAction("Slm","Attack_f_no","Jog_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","Attack_b_no","Wbk_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","Attack_r_no","Jog_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","Attack_l_no","Jog_no_Slm",0.0,1.0,0)

#Bladex.AddBipedAction("Slm","Attack_f_2h","Wlk_no_Slm",0.0,1.0,0)
#Bladex.AddBipedAction("Slm","Attack_b_2h","Wbk_no_Slm",0.0,1.0,0)
#Bladex.AddBipedAction("Slm","Attack_r_2h","Wlk_no_Slm",0.0,1.0,0)
#Bladex.AddBipedAction("Slm","Attack_l_2h","Wlk_no_Slm",0.0,1.0,0)

#Movement with shield
#Bladex.AddBipedAction("Slm","Shattack_f_2h","Wlk_no_Slm",0.0,1.0,0)
#Bladex.AddBipedAction("Slm","Shattack_b_2h","Wbk_no_Slm",0.0,1.0,0)
#Bladex.AddBipedAction("Slm","Shattack_r_2h","Wlk_no_Slm",0.0,1.0,0)
#Bladex.AddBipedAction("Slm","Shattack_l_2h","Wlk_no_Slm",0.0,1.0,0)

#Relax
#Bladex.AddBipedAction("Slm","Rlx_f_1h","Rlx_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","Rlx_f_no","Rlx_no_Slm",0.0,1.0,0)
#Bladex.AddBipedAction("Slm","Shattack_rlx_2h","Rlx_no_Slm",0.0,1.0,0)

#Quick turns
#Bladex.AddBipedAction("Slm","Attack_t_r","Rlx_no_Slm",0.0,1.0,0)
#Bladex.AddBipedAction("Slm","Attack_t_r_s","Rlx_no_Slm",0.0,1.0,0)
#Bladex.AddBipedAction("Slm","Attack_t_l","Rlx_no_Slm",0.0,1.0,0)
#Bladex.AddBipedAction("Slm","Attack_t_l_s","Rlx_no_Slm",0.0,1.0,0)


#Dodges
Bladex.AddBipedAction("Slm","D_b","Wbk_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","D_l","Wbk_no_Slm",0.0,1.0,0)
Bladex.AddBipedAction("Slm","D_r","Wbk_no_Slm",0.0,1.0,0)



####################################################################################
#
# Ataques
#
####################################################################################


Bladex.AddBipedAction("Slm","g_r","Slm_g_r",0.0,1.0,0)	
	
Bladex.AddBipedAction("Slm","g_bite","Slm_g_bite",0.0,1.0,0)	

Bladex.AddBipedAction("Slm","g_spit","Slm_g_spit",0.0,1.0,0)



####################################################################################
#
# Patrullas 
#
####################################################################################


Bladex.AddBipedAction("Slm","patrol","Slm_patrol",0.0,1.0,0)