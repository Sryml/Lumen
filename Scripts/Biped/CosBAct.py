import Bladex

#import AnimationSets


#AnimationSets.LoadCosAnimationSet("Cos")

####################################################################################
#
# Escalar + saltos
#
####################################################################################

Bladex.AddBipedAction("Cos","clmb_low_1h","Cos_clmb_medium_no",0.0,1.0,0)	
Bladex.AddBipedAction("Cos","clmb_medlow_1h","Cos_clmb_medium_no",0.0,1.0,0)	
Bladex.AddBipedAction("Cos","clmb_medium_1h","Cos_clmb_medium_no",0.0,1.0,0)	
Bladex.AddBipedAction("Cos","clmb_high_1h","Cos_clmb_medium_no",0.0,1.0,0)	

Bladex.AddBipedAction("Cos","LongJump1H","Cos_jmp_no",0.0,1.0,0)	
Bladex.AddBipedAction("Cos","LongJumpNo","Cos_jmp_no",0.0,1.0,0)	
Bladex.AddBipedAction("Cos","ShortJump","Cos_jmp_no",0.0,1.0,0)	



####################################################################################
#
# Others
#
####################################################################################

Bladex.AddBipedAction("Cos","slip","Cos_slip",0.0,1.0,0)	
Bladex.AddBipedAction("Cos","slip_b","Cos_slip",0.0,1.0,0)	
Bladex.AddBipedAction("Cos","derrape","Cos_slip",0.0,1.0,0)	
Bladex.AddBipedAction("Cos","jmp_back1","Cos_jmp_back1",0.0,1.0,0)


####################################################################################
#
# Relax.
#
####################################################################################

Bladex.AddBipedAction("Cos","Rlx_no","Rlx_no_Cos",0.0,1.0,0)
Bladex.AddBipedAction("Cos","Rlx_1h","Rlx_no_Cos",0.0,1.0,0)
Bladex.AddBipedAction("Cos","Rlx_b","Rlx_no_Cos",0.0,1.0,0)
Bladex.AddBipedAction("Cos","Rlx_2h","Rlx_no_Cos",0.0,1.0,0)
Bladex.AddBipedAction("Cos","Rlx_s","Rlx_no_Cos",0.0,1.0,0)

####################################################################################
#
# Pasos.- Andares
#
####################################################################################

#Bladex.AddBipedAction("Cos","LStepUp","Wlk_Cos","Wlk_no_Cos",0.0,0.5,0)
#Bladex.AddBipedAction("Cos","RStepUp","Wlk_Cos","Wlk_no_Cos",0.5,1.0,0)

#Bladex.AddBipedAction("Cos","LStairsUp","StairsUp_Cos","Wlk_no_Cos",0.0,0.5,0)
#Bladex.AddBipedAction("Cos","RStairsUp","StairsUp_Cos","Wlk_no_Cos",0.5,1.0,0)

#Bladex.AddBipedAction("Cos","LStepDown","Wlk_Cos","Wlk_no_Cos",0.0,0.5,0)
#Bladex.AddBipedAction("Cos","RStepDown","Wlk_Cos","Wlk_no_Cos",0.5,1.0,0)

#Bladex.AddBipedAction("Cos","LStairsDown","Wlk_no_Cos",0.0,0.5,0)
#Bladex.AddBipedAction("Cos","RStairsDown","Wlk_no_Cos",0.5,1.0,0)

# Andar hacia atrás
Bladex.AddBipedAction("Cos","WBK_b","Wbk_no_Cos",0.0,1.0,0)	
Bladex.AddBipedAction("Cos","WBK_no","Wbk_no_Cos",0.0,1.0,0)	
Bladex.AddBipedAction("Cos","WBK_1h","Wbk_no_Cos",0.0,1.0,0)		
Bladex.AddBipedAction("Cos","WBK_2h","Wbk_no_Cos",0.0,1.0,0)	
Bladex.AddBipedAction("Cos","WBK_s","Wbk_no_Cos",0.0,1.0,0)

#Andar hacia alante
Bladex.AddBipedAction("Cos","WLK_b","Wlk_no_Cos",0.0,1.0,0)
Bladex.AddBipedAction("Cos","WLK_no","Wlk_no_Cos",0.0,1.0,0)
Bladex.AddBipedAction("Cos","WLK_1h","Wlk_no_Cos",0.0,1.0,0)
Bladex.AddBipedAction("Cos","WLK_2h","Wlk_no_Cos",0.0,1.0,0)
Bladex.AddBipedAction("Cos","WLK_s","Wlk_no_Cos",0.0,1.0,0)

#Correr hacia atrás
Bladex.AddBipedAction("Cos","JOG_b_b","Wbk_no_Cos",0.0,1.0,0)
Bladex.AddBipedAction("Cos","JOG_b_no","Wbk_no_Cos",0.0,1.0,0)
Bladex.AddBipedAction("Cos","JOG_b_s","Wbk_no_Cos",0.0,1.0,0)
Bladex.AddBipedAction("Cos","JOG_b_1h","Wbk_no_Cos",0.0,1.0,0)
Bladex.AddBipedAction("Cos","JOG_b_2h","Wbk_no_Cos",0.0,1.0,0)

#Correr hacia delante
Bladex.AddBipedAction("Cos","JOG_b","Jog_no_Cos",0.0,1.0,0)
Bladex.AddBipedAction("Cos","JOG_no","Jog_no_Cos",0.0,1.0,0)
Bladex.AddBipedAction("Cos","JOG_s","Jog_no_Cos",0.0,1.0,0)
Bladex.AddBipedAction("Cos","JOG_1h","Jog_no_Cos",0.0,1.0,0)
Bladex.AddBipedAction("Cos","JOG_2h","Jog_no_Cos",0.0,1.0,0)


#Modo sneak
Bladex.AddBipedAction("Cos","SNK_b","Wlk_no_Cos",0.0,1.0,0)
Bladex.AddBipedAction("Cos","SNK_no","Wlk_no_Cos",0.0,1.0,0)
Bladex.AddBipedAction("Cos","SNK_s","Wlk_no_Cos",0.0,1.0,0)
Bladex.AddBipedAction("Cos","SNK_1h","Wlk_no_Cos",0.0,1.0,0)
Bladex.AddBipedAction("Cos","SNK_2h","Wlk_no_Cos",0.0,1.0,0)




####################################################################################
#
# Caidas.
#
####################################################################################

Bladex.AddBipedAction("Cos","FllLow","FallMed_Cos",0.37,0.8,0)
Bladex.AddBipedAction("Cos","FllMed","FallMed_Cos",0.37,0.8,0)
Bladex.AddBipedAction("Cos","FllHigh","FallMed_Cos",0.1,0.8,0)
Bladex.AddBipedAction("Cos","Dth_Fll","Dth_Fll_Cos",0.0,1.0,0)
Bladex.AddBipedAction("Cos","Dth_Fll2","Dth_Fll2_Cos",0.0,1.0,0)




####################################################################################
#
# Animaciones en combate
#
####################################################################################

Bladex.AddBipedAction("Cos","Attack_f_no","Cos_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Cos","Attack_b_no","Cos_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Cos","Attack_r_no","Cos_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Cos","Attack_l_no","Cos_attack_l",0.0,1.0,0)

#Relax
#Bladex.AddBipedAction("Cos","Rlx_f_1h","Cos_rlx_f",0.0,1.0,0)
Bladex.AddBipedAction("Cos","Rlx_f_no","Rlx_no_Cos",0.0,1.0,0)
#Bladex.AddBipedAction("Cos","Attack_rlx_s","Cos_rlx_f",0.0,1.0,0)



#Dodges
Bladex.AddBipedAction("Cos","D_b","Wbk_no_Cos",0.0,1.0,0)
Bladex.AddBipedAction("Cos","D_l","Cos_d_l",0.0,1.0,0)
Bladex.AddBipedAction("Cos","D_r","Cos_d_r",0.0,1.0,0)

##MOvement without shield
#Bladex.AddBipedAction("Cos","Attack_f_1h","Cos_attack_f",0.0,1.0,0)
#Bladex.AddBipedAction("Cos","Attack_b_1h","Cos_attack_b",0.0,1.0,0)
#Bladex.AddBipedAction("Cos","Attack_r_1h","Cos_attack_r",0.0,1.0,0)
#Bladex.AddBipedAction("Cos","Attack_l_1h","Cos_attack_l",0.0,1.0,0)
#
##MOvement with shield
#Bladex.AddBipedAction("Cos","Attack_f_2h","Cos_attack_f",0.0,1.0,0)
#Bladex.AddBipedAction("Cos","Attack_b_2h","Cos_attack_b",0.0,1.0,0)
#Bladex.AddBipedAction("Cos","Attack_r_2h","Cos_attack_r",0.0,1.0,0)
#Bladex.AddBipedAction("Cos","Attack_l_2h","Cos_attack_l",0.0,1.0,0)

##Quick turns
#Bladex.AddBipedAction("Cos","Attack_t_r","Cos_attack_r",0.0,1.0,0)
#Bladex.AddBipedAction("Cos","Attack_t_r_s","Cos_attack_r",0.0,1.0,0)
#Bladex.AddBipedAction("Cos","Attack_t_l","Cos_attack_l",0.0,1.0,0)
#Bladex.AddBipedAction("Cos","Attack_t_l_s","Cos_attack_l",0.0,1.0,0)
#
##Movement with shield
#Bladex.AddBipedAction("Cos","Attack_f_s","Cos_attack_f",0.0,1.0,0)
#Bladex.AddBipedAction("Cos","Attack_b_s","Cos_attack_b",0.0,1.0,0)
#Bladex.AddBipedAction("Cos","Attack_r_s","Cos_attack_r",0.0,1.0,0)
#Bladex.AddBipedAction("Cos","Attack_l_s","Cos_attack_l",0.0,1.0,0)



####################################################################################
#
# Ataques
#
####################################################################################
	
Bladex.AddBipedAction("Cos","g_01","Cos_g_01",0.0,1.0,0)	
Bladex.AddBipedAction("Cos","g_02","Cos_g_02",0.0,1.0,0)




####################################################################################
#
# Ambient
#
####################################################################################
	
Bladex.AddBipedAction("Cos","alarm01","Cos_alarm",0.0,1.0,0)
Bladex.AddBipedAction("Cos","fury","Cos_fury",0.0,1.0,0)



####################################################################################
#
# Muerte y heridas
#
####################################################################################
	
Bladex.AddBipedAction("Cos","dth_fly","Cos_dth_fly",0.0,1.0,0)
Bladex.AddBipedAction("Cos","dth0","Cos_dth0",0.0,1.0,0)

Bladex.AddBipedAction("Cos","dth_c1","Cos_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Cos","dth_c2","Cos_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Cos","dth_c3","Cos_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Cos","dth_c4","Cos_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Cos","dth_c5","Cos_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Cos","dth_c6","Cos_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Cos","dth_c7","Cos_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Cos","dth0",  "Cos_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Cos","dth_n00","Cos_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Cos","dth_n01","Cos_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Cos","dth_n02","Cos_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Cos","dth_n03","Cos_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Cos","dth_n04","Cos_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Cos","dth_n05","Cos_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Cos","dth_n06","Cos_dth0",0.0,1.0,0)
                       
Bladex.AddBipedAction("Cos","dth_rock","Cos_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Cos","dth_rockfront","Cos_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Cos","dth_burn","Cos_dth0",0.0,1.0,0)	




Bladex.AddBipedAction("Cos","hurt_f_lite","Cos_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Cos","hurt_f_big","Cos_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Cos","hurt_f_head","Cos_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Cos","hurt_f_breast","Cos_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Cos","hurt_f_back","Cos_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Cos","hurt_f_r_arm","Cos_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Cos","hurt_f_l_arm","Cos_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Cos","hurt_f_r_leg","Cos_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Cos","hurt_f_l_leg","Cos_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Cos","hurt_jog","Cos_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Cos","hurt_head","Cos_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Cos","hurt_breast","Cos_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Cos","hurt_back","Cos_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Cos","hurt_r_arm","Cos_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Cos","hurt_l_arm","Cos_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Cos","hurt_r_leg","Cos_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Cos","hurt_l_leg","Cos_hurt_lite",0.0,1.0,0)
