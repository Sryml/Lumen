import Bladex



####################################################################################
#
# Escalar + saltos
#
####################################################################################

Bladex.AddBipedAction("Gdm","clmb_low_1h","Gdm_rlx_no",0.0,1.0,0)	
Bladex.AddBipedAction("Gdm","clmb_medlow_1h","Gdm_rlx_no",0.0,1.0,0)	
Bladex.AddBipedAction("Gdm","clmb_medium_1h","Gdm_rlx_no",0.0,1.0,0)	
Bladex.AddBipedAction("Gdm","clmb_high_1h","Gdm_rlx_no",0.0,1.0,0)	

Bladex.AddBipedAction("Gdm","LongJump1H","Gdm_rlx_no",0.0,0.93,0)	
Bladex.AddBipedAction("Gdm","LongJumpNo","Gdm_rlx_no",0.0,0.93,0)	
Bladex.AddBipedAction("Gdm","ShortJump","Gdm_rlx_no",0.41,1.0,0)	


####################################################################################
#
# Others
#
####################################################################################

Bladex.AddBipedAction("Gdm","slip","Gdm_rlx_no",0.0,1.0,0)	
Bladex.AddBipedAction("Gdm","slip_b","Gdm_rlx_no",0.0,1.0,0)	
Bladex.AddBipedAction("Gdm","derrape","Gdm_rlx_no",0.14,1.0,0)	



Bladex.AddBipedAction("Gdm","b1","Gdm_rlx_no",0.0,1.0,0)	
Bladex.AddBipedAction("Gdm","b2","Gdm_rlx_no",0.0,1.0,0)	
Bladex.AddBipedAction("Gdm","b3","Gdm_rlx_no",0.0,1.0,0)	

Bladex.AddBipedAction("Gdm","mgc_df","Gdm_mgc_df",0.0,1.0,0)


####################################################################################
#
# Relax.
#
####################################################################################

Bladex.AddBipedAction("Gdm","Rlx_no","Gdm_rlx_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","Rlx_1h","Gdm_rlx_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","Rlx_b","Gdm_rlx_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","Rlx_2h","Gdm_rlx_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","Rlx_s","Gdm_rlx_no",0.0,1.0,0)







####################################################################################
#
# Pasos.- Andares
#
####################################################################################

#Movement with shield -> !NPC only!!!!
Bladex.AddBipedAction("Gdm","Attack_f_s_nc","Gdm_rlx_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","Attack_b_s_nc","Gdm_rlx_no",0.0,1.0,0)

Bladex.AddBipedAction("Gdm","ShortStep","Gdm_rlx_no", 0.0,1.0,0)

#Bladex.AddBipedAction("Gdm","LStepUp","Gdm_wlk_no","WlkUp_Kgt",0.0,0.5,0)
#Bladex.AddBipedAction("Gdm","RStepUp","Gdm_wlk_no","WlkUp_Kgt",0.5,1.0,0)

#Bladex.AddBipedAction("Gdm","LStairsUp","StairsUp_Kgt","StairsUpP_Kgt",0.0,0.5,0)
#Bladex.AddBipedAction("Gdm","RStairsUp","StairsUp_Kgt","StairsUpP_Kgt",0.5,1.0,0)

#Bladex.AddBipedAction("Gdm","LStepDown","Gdm_wlk_no","WlkDown_Kgt",0.0,0.5,0)
#Bladex.AddBipedAction("Gdm","RStepDown","Gdm_wlk_no","WlkDown_Kgt",0.5,1.0,0)

#Bladex.AddBipedAction("Gdm","LStairsDown","StairsDown_Kgt",0.0,0.5,0)
#Bladex.AddBipedAction("Gdm","RStairsDown","StairsDown_Kgt",0.5,1.0,0)

# Andar hacia atrás
Bladex.AddBipedAction("Gdm","WBK_b","Gdm_wbk_no",0.0,1.0,0)	
Bladex.AddBipedAction("Gdm","WBK_no","Gdm_wbk_no",0.0,1.0,0)	
Bladex.AddBipedAction("Gdm","WBK_1h","Gdm_wbk_no",0.0,1.0,0)		
Bladex.AddBipedAction("Gdm","WBK_2h","Gdm_wbk_no",0.0,1.0,0)		
Bladex.AddBipedAction("Gdm","WBK_s","Gdm_wbk_no",0.0,1.0,0)	

#Andar hacia delante
Bladex.AddBipedAction("Gdm","WLK_b","Gdm_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","WLK_no","Gdm_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","WLK_1h","Gdm_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","WLK_2h","Gdm_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","WLK_s","Gdm_wlk_no",0.0,1.0,0)

#Correr hacia delante
Bladex.AddBipedAction("Gdm","JOG_b","Gdm_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","JOG_no","Gdm_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","JOG_s","Gdm_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","JOG_1h","Gdm_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","JOG_2h","Gdm_wlk_no",0.0,1.0,0)

#Correr hacia atrás
Bladex.AddBipedAction("Gdm","WBK_JOG_b","Gdm_wbk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","WBK_JOG_no","Gdm_wbk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","WBK_JOG_1h","Gdm_wbk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","WBK_JOG_2h","Gdm_wbk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","WBK_JOG_s","Gdm_wbk_no",0.0,1.0,0)

#Modo sneak
Bladex.AddBipedAction("Gdm","SNK_b","Gdm_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","SNK_no","Gdm_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","SNK_s", "Gdm_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","SNK_1h","Gdm_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","SNK_2h","Gdm_wlk_no",0.0,1.0,0)





####################################################################################
#
# Caidas.
#
####################################################################################

Bladex.AddBipedAction("Gdm","FllLow","Gdm_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","FllMed","Gdm_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","FllHigh","Gdm_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","Dth_Fll","Gdm_rlx_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","Dth_Fll2","Gdm_dth0",0.534,1.0,0)


####################################################################################
#
# Muertes 
#
####################################################################################

Bladex.AddBipedAction("Gdm","dth0","Gdm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","dth_c1","Gdm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","dth_c2","Gdm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","dth_c3","Gdm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","dth_c4","Gdm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","dth_c5","Gdm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","dth_c6","Gdm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","dth_c7","Gdm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","dth0",  "Gdm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","dth_n00","Gdm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","dth_n01","Gdm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","dth_n02","Gdm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","dth_n03","Gdm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","dth_n04","Gdm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","dth_n05","Gdm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","dth_n06","Gdm_dth0",0.0,1.0,0)
                       
Bladex.AddBipedAction("Gdm","dth_rock","Gdm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","dth_rockfront","Gdm_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","dth_burn","Gdm_dth0",0.0,1.0,0)	


####################################################################################
#
# Heridas 
#
####################################################################################

Bladex.AddBipedAction("Gdm","hurt_f_lite","Gdm_rlx_no",0.8,1.0,0)
Bladex.AddBipedAction("Gdm","hurt_f_big","Gdm_hurt_big",0.0,0.34,0)
Bladex.AddBipedAction("Gdm","hurt_f_head","Gdm_hurt_big",0.0,0.34,0)
Bladex.AddBipedAction("Gdm","hurt_f_breast","Gdm_rlx_no",0.8,1.0,0)
Bladex.AddBipedAction("Gdm","hurt_f_back","Gdm_rlx_no",0.8,1.0,0)
Bladex.AddBipedAction("Gdm","hurt_f_r_arm","Gdm_rlx_no",0.8,1.0,0)
Bladex.AddBipedAction("Gdm","hurt_f_l_arm","Gdm_rlx_no",0.8,1.0,0)
Bladex.AddBipedAction("Gdm","hurt_f_r_leg","Gdm_rlx_no",0.8,1.0,0)
Bladex.AddBipedAction("Gdm","hurt_f_l_leg","Gdm_rlx_no",0.8,1.0,0)
Bladex.AddBipedAction("Gdm","hurt_jog","Gdm_hurt_big",0.0,0.34,0)
Bladex.AddBipedAction("Gdm","hurt_head","Gdm_hurt_big",0.0,0.34,0)
Bladex.AddBipedAction("Gdm","hurt_breast","Gdm_rlx_no",0.8,1.0,0)
Bladex.AddBipedAction("Gdm","hurt_back","Gdm_rlx_no",0.8,1.0,0)
Bladex.AddBipedAction("Gdm","hurt_r_arm","Gdm_rlx_no",0.8,1.0,0)
Bladex.AddBipedAction("Gdm","hurt_l_arm","Gdm_rlx_no",0.8,1.0,0)
Bladex.AddBipedAction("Gdm","hurt_r_leg","Gdm_rlx_no",0.8,1.0,0)
Bladex.AddBipedAction("Gdm","hurt_l_leg","Gdm_rlx_no",0.8,1.0,0)



####################################################################################
#
# Animaciones en combate
#
####################################################################################

Bladex.AddBipedAction("Gdm","Attack_f_no","Gdm_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","Attack_b_no","Gdm_wbk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","Attack_r_no","Gdm_rlx_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","Attack_l_no","Gdm_rlx_no",0.0,1.0,0)


#Relax
#Bladex.AddBipedAction("Gdm","Rlx_f_1h","Gdm_rlx_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","Rlx_f_no","Gdm_rlx_no",0.0,1.0,0)
#Bladex.AddBipedAction("Gdm","Attack_rlx_s","Gdm_rlx_no",0.0,1.0,0)


#Dodges
Bladex.AddBipedAction("Gdm","D_b","Gdm_wbk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","D_l","Gdm_wbk_no",0.0,1.0,0)
Bladex.AddBipedAction("Gdm","D_r","Gdm_wbk_no",0.0,1.0,0)

##MOvement without shield                 
#Bladex.AddBipedAction("Gdm","Attack_f_1h","Gdm_wlk_no",0.0,1.0,0)
#Bladex.AddBipedAction("Gdm","Attack_b_1h","Gdm_wbk_no",0.0,1.0,0)
#Bladex.AddBipedAction("Gdm","Attack_r_1h","Gdm_rlx_no",0.0,1.0,0)
#Bladex.AddBipedAction("Gdm","Attack_l_1h","Gdm_rlx_no",0.0,1.0,0)
#
##Quick turns
#Bladex.AddBipedAction("Gdm","Attack_t_r","Gdm_rlx_no",0.0,1.0,0)
#Bladex.AddBipedAction("Gdm","Attack_t_r_s","Gdm_rlx_no",0.0,1.0,0)
#Bladex.AddBipedAction("Gdm","Attack_t_l","Gdm_rlx_no",0.0,1.0,0)
#Bladex.AddBipedAction("Gdm","Attack_t_l_s","Gdm_rlx_no",0.0,1.0,0)
#
#Bladex.AddBipedAction("Gdm","Attack_f_2h","Gdm_wlk_no",0.0,1.0,0)
#Bladex.AddBipedAction("Gdm","Attack_b_2h","Gdm_wbk_no",0.0,1.0,0)
#Bladex.AddBipedAction("Gdm","Attack_r_2h","Gdm_rlx_no",0.0,1.0,0)
#Bladex.AddBipedAction("Gdm","Attack_l_2h","Gdm_rlx_no",0.0,1.0,0)
#
##Movement with shield
#Bladex.AddBipedAction("Gdm","Attack_f_s","Gdm_wlk_no",0.0,1.0,0)
#Bladex.AddBipedAction("Gdm","Attack_b_s","Gdm_wbk_no",0.0,1.0,0)
#Bladex.AddBipedAction("Gdm","Attack_r_s","Gdm_rlx_no",0.0,1.0,0)
#Bladex.AddBipedAction("Gdm","Attack_l_s","Gdm_rlx_no",0.0,1.0,0)




####################################################################################
#
# Ataques
#
####################################################################################


Bladex.AddBipedAction("Gdm","g_01","Gdm_g_01",0.0,1.0,0)	
Bladex.AddBipedAction("Gdm","g_12","Gdm_g_12",0.0,1.0,0)	
Bladex.AddBipedAction("Gdm","g_back","Gdm_g_back",0.0,1.0,0)	
Bladex.AddBipedAction("Gdm","g_quake","Gdm_g_quake",0.0,1.0,0)	
Bladex.AddBipedAction("Gdm","g_magic","Gdm_g_magic",0.0,1.0,0)	
Bladex.AddBipedAction("Gdm","g_claw","Gdm_g_claw",0.0,1.0,0)	
Bladex.AddBipedAction("Gdm","g_spit_around","Gdm_g_spit_around",0.0,0.80,0)	
Bladex.AddBipedAction("Gdm","g_spit_f","Gdm_g_spit_f",0.0,0.76,0)
Bladex.AddBipedAction("Gdm","g_spitball","Gdm_g_spitball",0.0,0.80,0)



