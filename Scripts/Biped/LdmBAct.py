import Bladex

#import AnimationSets


#AnimationSets.LoadLdmAnimationSet("Ldm")

####################################################################################
#
# Escalar + saltos
#
####################################################################################

#Bladex.AddBipedAction("Ldm","clmb_low_1h","Ldm_clmb_low_1h",0.0,1.0,0)	
#Bladex.AddBipedAction("Ldm","clmb_medlow_1h","Ldm_clmb_medlow_1h",0.0,1.0,0)	
#Bladex.AddBipedAction("Ldm","clmb_medium_1h","Ldm_clmb_medium_1h",0.0,1.0,0)	
#Bladex.AddBipedAction("Ldm","clmb_high_1h","Ldm_clmb_high_1h",0.0,1.0,0)	

#Bladex.AddBipedAction("Ldm","LongJump1H","Ldm_jmp_no",0.0,1.0,0)	
#Bladex.AddBipedAction("Ldm","LongJumpNo","Ldm_jmp_no",0.0,1.0,0)	
#Bladex.AddBipedAction("Ldm","ShortJump","Ldm_jmp_no",0.0,1.0,0)	


####################################################################################
#
# Others
#
####################################################################################

Bladex.AddBipedAction("Ldm","slip","Ldm_rlx_no",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","slip_b","Ldm_rlx_no",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","derrape","Ldm_rlx_no",0.0,1.0,0)

Bladex.AddBipedAction("Ldm","appears","Ldm_appears",0.0,1.0,0)

####################################################################################
#
# Relax.
#
####################################################################################

Bladex.AddBipedAction("Ldm","Rlx_no","Ldm_rlx_no",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","Rlx_1h","Ldm_rlx_no",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","Rlx_b","Ldm_rlx_no",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","Rlx_2h","Ldm_rlx_no",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","Rlx_s","Ldm_rlx_f_s",0.0,1.0,0)


####################################################################################
#
# Pasos.- Andares
#
####################################################################################

#Bladex.AddBipedAction("Ldm","LStepUp","Wlk_Ldm","Ldm_rlx_no",0.0,0.5,0)
#Bladex.AddBipedAction("Ldm","RStepUp","Wlk_Ldm","Ldm_rlx_no",0.5,1.0,0)

#Bladex.AddBipedAction("Ldm","LStairsUp","StairsUp_Ldm","Ldm_rlx_no",0.0,0.5,0)
#Bladex.AddBipedAction("Ldm","RStairsUp","StairsUp_Ldm","Ldm_rlx_no",0.5,1.0,0)

#Bladex.AddBipedAction("Ldm","LStepDown","Wlk_Ldm","Ldm_rlx_no",0.0,0.5,0)
#Bladex.AddBipedAction("Ldm","RStepDown","Wlk_Ldm","Ldm_rlx_no",0.5,1.0,0)

#Bladex.AddBipedAction("Ldm","LStairsDown","Ldm_rlx_no",0.0,0.5,0)
#Bladex.AddBipedAction("Ldm","RStairsDown","Ldm_rlx_no",0.5,1.0,0)

# Andar hacia atrás
Bladex.AddBipedAction("Ldm","WBK_b","Ldm_wbk_no",0.0,1.0,0)	 
Bladex.AddBipedAction("Ldm","WBK_no","Ldm_wbk_no",0.0,1.0,0)	
Bladex.AddBipedAction("Ldm","WBK_1h","Ldm_wbk_no",0.0,1.0,0)		
Bladex.AddBipedAction("Ldm","WBK_2h","Ldm_wbk_no",0.0,1.0,0)	
Bladex.AddBipedAction("Ldm","WBK_s","Ldm_wbk_no",0.0,1.0,0)

#Andar hacia alante
Bladex.AddBipedAction("Ldm","WLK_b","Ldm_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","WLK_no","Ldm_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","WLK_1h","Ldm_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","WLK_2h","Ldm_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","WLK_s","Ldm_wlk_no",0.0,1.0,0)

#Correr hacia atrás
Bladex.AddBipedAction("Ldm","WBK_JOG_b","Ldm_wbk_no",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","WBK_JOG_no","Ldm_wbk_no",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","WBK_JOG_1h","Ldm_wbk_no",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","WBK_JOG_s","Ldm_wbk_no",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","WBK_JOG_2h","Ldm_wbk_no",0.0,1.0,0)


#Correr hacia adelante
Bladex.AddBipedAction("Ldm","JOG_b","Ldm_jog_no",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","JOG_no","Ldm_jog_no",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","JOG_1h","Ldm_jog_no",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","JOG_s","Ldm_jog_no",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","JOG_2h","Ldm_jog_no",0.0,1.0,0)


#Modo sneak
Bladex.AddBipedAction("Ldm","SNK_b","Ldm_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","SNK_no","Ldm_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","SNK_1h","Ldm_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","SNK_s","Ldm_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","SNK_2h","Ldm_attack_f",0.0,1.0,0)

#Correr con escudo en modo no combate                                       
Bladex.AddBipedAction("Ldm","Attack_f_s_nc","Ldm_rlx_f_s",0.0,1.0,0)     
Bladex.AddBipedAction("Ldm","Attack_b_s_nc","Ldm_rlx_f_s",0.0,1.0,0)     



####################################################################################
#
# Caidas.
#
####################################################################################

Bladex.AddBipedAction("Ldm","FllLow","Ldm_fll_low",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","FllMed","Ldm_fll_low",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","FllHigh","Ldm_fll_high",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","Dth_Fll","Dth_Fll_Ldm",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","Dth_Fll2","Dth_Fll2_Ldm",0.0,1.0,0)



####################################################################################
#
# Animaciones en combate
#
####################################################################################

#MOvement without shield
#Bladex.AddBipedAction("Ldm","Attack_f_1h","Ldm_attack_f",0.0,1.0,0)
#Bladex.AddBipedAction("Ldm","Attack_b_1h","Ldm_attack_b",0.0,1.0,0)
#Bladex.AddBipedAction("Ldm","Attack_r_1h","Ldm_attack_r",0.0,1.0,0)
#Bladex.AddBipedAction("Ldm","Attack_l_1h","Ldm_attack_l",0.0,1.0,0)

Bladex.AddBipedAction("Ldm","Attack_f_no","Ldm_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","Attack_b_no","Ldm_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","Attack_r_no","Ldm_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","Attack_l_no","Ldm_attack_l",0.0,1.0,0)

#Bladex.AddBipedAction("Ldm","Attack_f_2h","Ldm_attack_f",0.0,1.0,0)
#Bladex.AddBipedAction("Ldm","Attack_b_2h","Ldm_attack_b",0.0,1.0,0)
#Bladex.AddBipedAction("Ldm","Attack_r_2h","Ldm_attack_r",0.0,1.0,0)
#Bladex.AddBipedAction("Ldm","Attack_l_2h","Ldm_attack_l",0.0,1.0,0)

#Movement with shield
#Bladex.AddBipedAction("Ldm","Shattack_f_2h","Ldm_attack_f",0.0,1.0,0)
#Bladex.AddBipedAction("Ldm","Shattack_b_2h","Ldm_attack_b",0.0,1.0,0)
#Bladex.AddBipedAction("Ldm","Shattack_r_2h","Ldm_attack_r",0.0,1.0,0)
#Bladex.AddBipedAction("Ldm","Shattack_l_2h","Ldm_attack_l",0.0,1.0,0)

#Relax
#Bladex.AddBipedAction("Ldm","Rlx_f_1h","Ldm_rlx_f",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","Rlx_f_no","Ldm_rlx_f",0.0,1.0,0)
#Bladex.AddBipedAction("Ldm","Shattack_rlx_2h","Ldm_rlx_f_s",0.0,1.0,0)

#Quick turns
#Bladex.AddBipedAction("Ldm","Attack_t_r","Ldm_t_r_no",0.0,1.0,0)
#Bladex.AddBipedAction("Ldm","Attack_t_r_s","Ldm_t_r_no",0.0,1.0,0)
#Bladex.AddBipedAction("Ldm","Attack_t_l","Ldm_t_l_no",0.0,1.0,0)
#Bladex.AddBipedAction("Ldm","Attack_t_l_s","Ldm_t_l_no",0.0,1.0,0)


#Dodges
Bladex.AddBipedAction("Ldm","D_b","Ldm_g_07",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","D_l","Ldm_g_07",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","D_r","Ldm_g_07",0.0,1.0,0)


####################################################################################
#
# Heridas
#
####################################################################################

Bladex.AddBipedAction("Ldm","hurt_f_lite","Ldm_hurt_f_lite",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","hurt_f_big","Ldm_hurt_f_big",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","hurt_f_head","Ldm_hurt_f_big",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","hurt_f_breast","Ldm_hurt_f_lite",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","hurt_f_back","Ldm_hurt_f_lite",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","hurt_f_r_arm","Ldm_hurt_f_lite",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","hurt_f_l_arm","Ldm_hurt_f_lite",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","hurt_f_r_leg","Ldm_hurt_f_lite",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","hurt_f_l_leg","Ldm_hurt_f_lite",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","hurt_jog","Ldm_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","hurt_head","Ldm_hurt_big",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","hurt_breast","Ldm_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","hurt_back","Ldm_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","hurt_r_arm","Ldm_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","hurt_l_arm","Ldm_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","hurt_r_leg","Ldm_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","hurt_l_leg","Ldm_hurt_lite",0.0,1.0,0)


####################################################################################
#
# Muertes
#
####################################################################################

Bladex.AddBipedAction("Ldm","dth0",  "Ldm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","dth_c1","Ldm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","dth_c2","Ldm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","dth_c3","Ldm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","dth_c4","Ldm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","dth_c5","Ldm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","dth_c6","Ldm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","dth_c7","Ldm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","dth0",  "Ldm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","dth_n00","Ldm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","dth_n01","Ldm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","dth_n02","Ldm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","dth_n03","Ldm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","dth_n04","Ldm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","dth_n05","Ldm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","dth_n06","Ldm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","dth_rock","Ldm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","dth_rockfront","Ldm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","dth_burn","Ldm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","dth_disap","Ldm_dth_disap",0.0,1.0,0)


####################################################################################
#
# Ataques
#
####################################################################################

Bladex.AddBipedAction("Ldm","g_03","Ldm_g_03",0.0,1.0,0)	
Bladex.AddBipedAction("Ldm","g_06","Ldm_g_06",0.0,1.0,0)	
Bladex.AddBipedAction("Ldm","g_07","Ldm_g_07",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","g_27","Ldm_g_27",0.0,1.0,0)	
Bladex.AddBipedAction("Ldm","g_22","Ldm_g_22",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","g_spit","Ldm_g_spit",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","g_jumpl","Ldm_g_jumpl",0.0,1.0,0)
Bladex.AddBipedAction("Ldm","g_jumpr","Ldm_g_jumpr",0.0,1.0,0)
####################################################################################
#
# Animaciones Varias
#
####################################################################################

Bladex.AddBipedAction("Ldm","patrol1","Ldm_patrol1",0.0,1.0,0)	
