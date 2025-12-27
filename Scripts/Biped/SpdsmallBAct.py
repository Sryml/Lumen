import Bladex



####################################################################################
#
# Escalar + saltos
#
####################################################################################

#Bladex.AddBipedAction("Spd","clmb_low_1h","Spd_clmb_low",0.0,1.0,0)	
#Bladex.AddBipedAction("Spd","clmb_medlow_1h","Spd_clmb_low",0.0,1.0,0)	
#Bladex.AddBipedAction("Spd","clmb_medium_1h","Spd_clmb_low",0.0,1.0,0)	
#Bladex.AddBipedAction("Spd","clmb_high_1h","Spd_clmb_low",0.0,1.0,0)	

Bladex.AddBipedAction("Spd","LongJump1H","Spd_jmp_no",0.0,0.93,0)	
Bladex.AddBipedAction("Spd","LongJumpNo","Spd_jmp_no",0.0,0.93,0)	
Bladex.AddBipedAction("Spd","ShortJump","Spd_jmph_no",0.41,1.0,0)	


####################################################################################
#
# Others
#
####################################################################################

Bladex.AddBipedAction("Spd","slip","Spd_wlk_no",0.0,1.0,0)	
Bladex.AddBipedAction("Spd","slip_b","Spd_wlk_no",0.0,1.0,0)	
Bladex.AddBipedAction("Spd","derrape","Spd_wlk_no",0.14,1.0,0)	



Bladex.AddBipedAction("Spd","b1","Spd_rlx_no",0.0,0.1,0)	
Bladex.AddBipedAction("Spd","b2","Spd_rlx_no",0.0,0.1,0)	
Bladex.AddBipedAction("Spd","b3","Spd_rlx_no",0.0,0.1,0)	



####################################################################################
#
# Relax.
#
####################################################################################

Bladex.AddBipedAction("Spd","Rlx_no","Spd_rlx_no",0.0,1.0,0)
Bladex.AddBipedAction("Spd","Rlx_1h","Spd_rlx_no",0.0,1.0,0)
Bladex.AddBipedAction("Spd","Rlx_b","Spd_rlx_no",0.0,1.0,0)
Bladex.AddBipedAction("Spd","Rlx_2h","Spd_rlx_no",0.0,1.0,0)
Bladex.AddBipedAction("Spd","Rlx_s","Spd_rlx_no",0.0,1.0,0)







####################################################################################
#
# Pasos.- Andares
#
####################################################################################

#Movement with shield -> !NPC only!!!!
Bladex.AddBipedAction("Spd","Attack_f_s_nc","Spd_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Spd","Attack_b_s_nc","Spd_wlk_no",0.0,1.0,0)

#Bladex.AddBipedAction("Spd","ShortStep","Spd_wlk_no", 0.0,1.0,0)

#Bladex.AddBipedAction("Spd","LStepUp","Wlk_1h_Spd","Spd_wlk_no",0.0,0.5,0)
#Bladex.AddBipedAction("Spd","RStepUp","Wlk_1h_Spd","Spd_wlk_no",0.5,1.0,0)

#Bladex.AddBipedAction("Spd","LStairsUp","StairsUp_Spd","Spd_wlk_no",0.0,0.5,0)
#Bladex.AddBipedAction("Spd","RStairsUp","StairsUp_Spd","Spd_wlk_no",0.5,1.0,0)

#Bladex.AddBipedAction("Spd","LStepDown","Wlk_1h_Spd","Spd_wlk_no",0.0,0.5,0)
#Bladex.AddBipedAction("Spd","RStepDown","Wlk_1h_Spd","Spd_wlk_no",0.5,1.0,0)

#Bladex.AddBipedAction("Spd","LStairsDown","Spd_wlk_no",0.0,0.5,0)
#Bladex.AddBipedAction("Spd","RStairsDown","Spd_wlk_no",0.5,1.0,0)

# Andar hacia atrás
Bladex.AddBipedAction("Spd","WBK_b","Spd_attack_b",0.0,1.0,0)	
Bladex.AddBipedAction("Spd","WBK_no","Spd_attack_b",0.0,1.0,0)	
Bladex.AddBipedAction("Spd","WBK_1h","Spd_attack_b",0.0,1.0,0)		
Bladex.AddBipedAction("Spd","WBK_2h","Spd_attack_b",0.0,1.0,0)		
Bladex.AddBipedAction("Spd","WBK_s","Spd_attack_b",0.0,1.0,0)	

#Andar hacia delante
Bladex.AddBipedAction("Spd","WLK_b","Spd_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Spd","WLK_no","Spd_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Spd","WLK_1h","Spd_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Spd","WLK_2h","Spd_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Spd","WLK_s","Spd_wlk_no",0.0,1.0,0)

#Correr hacia delante
Bladex.AddBipedAction("Spd","JOG_b","Spd_jog_no",0.0,1.0,0)
Bladex.AddBipedAction("Spd","JOG_no","Spd_jog_no",0.0,1.0,0)
Bladex.AddBipedAction("Spd","JOG_s","Spd_jog_no",0.0,1.0,0)
Bladex.AddBipedAction("Spd","JOG_1h","Spd_jog_no",0.0,1.0,0)
Bladex.AddBipedAction("Spd","JOG_2h","Spd_jog_no",0.0,1.0,0)

#Correr hacia atrás
Bladex.AddBipedAction("Spd","WBK_JOG_b","Spd_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Spd","WBK_JOG_no","Spd_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Spd","WBK_JOG_1h","Spd_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Spd","WBK_JOG_2h","Spd_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Spd","WBK_JOG_s","Spd_attack_b",0.0,1.0,0)

#Modo sneak
Bladex.AddBipedAction("Spd","SNK_b","Spd_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Spd","SNK_no","Spd_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Spd","SNK_s", "Spd_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Spd","SNK_1h","Spd_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Spd","SNK_2h","Spd_wlk_no",0.0,1.0,0)





####################################################################################
#
# Caidas.
#
####################################################################################

Bladex.AddBipedAction("Spd","FllLow","Spd_fll_low_no",0.0,0.1,0)
Bladex.AddBipedAction("Spd","FllMed","Spd_fll_low_no",0.0,0.1,0)
Bladex.AddBipedAction("Spd","FllHigh","Spd_fll_low_no",0.0,0.2,0)
Bladex.AddBipedAction("Spd","Dth_Fll","Dth_Fll_Spd",0.0,1.0,0)
Bladex.AddBipedAction("Spd","Dth_Fll2","Dth_Fll2_Spd",0.0,1.0,0)





####################################################################################
#
# Animaciones en combate
#
####################################################################################

#MOvement without shield
#Bladex.AddBipedAction("Spd","Attack_f_1h","Spd_wlk_no",0.0,1.0,0)
#Bladex.AddBipedAction("Spd","Attack_b_1h","Spd_attack_b",0.0,1.0,0)
#Bladex.AddBipedAction("Spd","Attack_r_1h","Spd_wlk_no",0.0,1.0,0)
#Bladex.AddBipedAction("Spd","Attack_l_1h","Spd_wlk_no",0.0,1.0,0)

Bladex.AddBipedAction("Spd","Attack_f_no","Spd_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Spd","Attack_b_no","Spd_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Spd","Attack_r_no","Spd_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Spd","Attack_l_no","Spd_wlk_no",0.0,1.0,0)

#MOvement without shield
#Bladex.AddBipedAction("Spd","Attack_f_2h","Spd_wlk_no",0.0,1.0,0)
#Bladex.AddBipedAction("Spd","Attack_b_2h","Spd_attack_b",0.0,1.0,0)
#Bladex.AddBipedAction("Spd","Attack_r_2h","Spd_wlk_no",0.0,1.0,0)
#Bladex.AddBipedAction("Spd","Attack_l_2h","Spd_wlk_no",0.0,1.0,0)

#Movement with shield
#Bladex.AddBipedAction("Spd","Attack_f_s","Spd_wlk_no",0.0,1.0,0)
#Bladex.AddBipedAction("Spd","Attack_b_s","Spd_attack_b",0.0,1.0,0)
#Bladex.AddBipedAction("Spd","Attack_r_s","Spd_wlk_no",0.0,1.0,0)
#Bladex.AddBipedAction("Spd","Attack_l_s","Spd_wlk_no",0.0,1.0,0)

#Relax
#Bladex.AddBipedAction("Spd","Rlx_f_1h","Spd_rlx_no",0.0,1.0,0)
Bladex.AddBipedAction("Spd","Rlx_f_no","Spd_rlx_no",0.0,1.0,0)
#Bladex.AddBipedAction("Spd","Attack_rlx_s","Spd_rlx_no",0.0,1.0,0)

#Quick turns
#Bladex.AddBipedAction("Spd","Attack_t_r","Spd_t_r_no",0.0,1.0,0)
#Bladex.AddBipedAction("Spd","Attack_t_r_s","Spd_t_r_no",0.0,1.0,0)
#Bladex.AddBipedAction("Spd","Attack_t_l","Spd_t_l_no",0.0,1.0,0)
#Bladex.AddBipedAction("Spd","Attack_t_l_s","Spd_t_l_no",0.0,1.0,0)


#Dodges
Bladex.AddBipedAction("Spd","D_b","Spd_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Spd","D_l","Spd_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Spd","D_r","Spd_attack_b",0.0,1.0,0)




####################################################################################
#
# Ataques
#
####################################################################################

Bladex.AddBipedAction("Spd","g_01","Spd_g_01",0.0,1.0,0)	
Bladex.AddBipedAction("Spd","Spd_g_spit","Spd_g_spit",0.0,1.0,0)



####################################################################################
#
# Muertes y Heridas
#
####################################################################################

Bladex.AddBipedAction("Spd","dth0","Spd_dth0",0.0,1.0,0)	
Bladex.AddBipedAction("Spd","dth_n00","Spd_dth2",0.0,1.0,0)
Bladex.AddBipedAction("Spd","dth_c1","Spd_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Spd","dth_c2","Spd_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Spd","dth_c3","Spd_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Spd","dth_c4","Spd_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Spd","dth_c5","Spd_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Spd","dth_c6","Spd_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Spd","dth_c7","Spd_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Spd","dth0",  "Spd_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Spd","dth_n01","Spd_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Spd","dth_n02","Spd_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Spd","dth_n03","Spd_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Spd","dth_n04","Spd_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Spd","dth_n05","Spd_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Spd","dth_n06","Spd_dth0",0.0,1.0,0)
                       
Bladex.AddBipedAction("Spd","dth_rock","Spd_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Spd","dth_rockfront","Spd_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Spd","dth_burn","Spd_dth0",0.0,1.0,0)	



Bladex.AddBipedAction("Spd","hurt_f_lite","Spd_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Spd","hurt_f_big","Spd_hurt_big",0.0,1.0,0)
Bladex.AddBipedAction("Spd","hurt_f_head","Spd_hurt_big",0.0,1.0,0)
Bladex.AddBipedAction("Spd","hurt_f_breast","Spd_hurt_big",0.0,1.0,0)
Bladex.AddBipedAction("Spd","hurt_f_back","Spd_hurt_big",0.0,1.0,0)
Bladex.AddBipedAction("Spd","hurt_f_r_arm","Spd_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Spd","hurt_f_l_arm","Spd_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Spd","hurt_f_r_leg","Spd_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Spd","hurt_f_l_leg","Spd_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Spd","hurt_jog","Spd_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Spd","hurt_head","Spd_hurt_big",0.0,1.0,0)
Bladex.AddBipedAction("Spd","hurt_breast","Spd_hurt_big",0.0,1.0,0)
Bladex.AddBipedAction("Spd","hurt_back","Spd_hurt_big",0.0,1.0,0)
Bladex.AddBipedAction("Spd","hurt_r_arm","Spd_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Spd","hurt_l_arm","Spd_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Spd","hurt_r_leg","Spd_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Spd","hurt_l_leg","Spd_hurt_lite",0.0,1.0,0)	




