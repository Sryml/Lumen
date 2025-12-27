import Bladex



####################################################################################
#
# Escalar + saltos
#
####################################################################################

Bladex.AddBipedAction("Dgk","clmb_low_1h","Dgk_rlx_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Dgk","clmb_medlow_1h","Dgk_rlx_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Dgk","clmb_medium_1h","Dgk_rlx_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Dgk","clmb_high_1h","Dgk_rlx_1h",0.0,1.0,0)	

Bladex.AddBipedAction("Dgk","LongJump1H","Dgk_rlx_1h",0.0,0.93,0)	
Bladex.AddBipedAction("Dgk","LongJumpNo","Dgk_rlx_1",0.0,0.93,0)	
Bladex.AddBipedAction("Dgk","ShortJump","Dgk_rlx_1h",0.41,1.0,0)	


####################################################################################
#
# Others
#
####################################################################################

Bladex.AddBipedAction("Dgk","slip","Dgk_rlx_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Dgk","slip_b","Dgk_rlx_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Dgk","derrape","Dgk_rlx_1h",0.14,1.0,0)	



Bladex.AddBipedAction("Dgk","b1","Dgk_rlx_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Dgk","b2","Dgk_rlx_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Dgk","b3","Dgk_rlx_1h",0.0,1.0,0)	



####################################################################################
#
# Relax.
#
####################################################################################

Bladex.AddBipedAction("Dgk","Rlx_no","Dgk_rlx_1",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Rlx_1h","Dgk_rlx_1h",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Rlx_b","Dgk_rlx_1h",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Rlx_2h","Dgk_rlx_1h",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Rlx_s","Dgk_rlx_1h",0.0,1.0,0)




Bladex.AddBipedAction("Dgk","powup","Dgk_powup",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","lifeup1","Dgk_lifeup1",0.0,1.0,0)







####################################################################################
#
# Pasos.- Andares
#
####################################################################################

#Movement with shield -> !NPC only!!!!
Bladex.AddBipedAction("Dgk","Attack_f_s_nc","Dgk_rlx_s",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Attack_b_s_nc","Dgk_rlx_s",0.0,1.0,0)

Bladex.AddBipedAction("Dgk","ShortStep","Dgk_rlx_1h", 0.0,1.0,0)
# Andar hacia atrás
Bladex.AddBipedAction("Dgk","WBK_b","Dgk_attack_b",0.0,1.0,0)	
Bladex.AddBipedAction("Dgk","WBK_no","Dgk_rlx_1",0.0,1.0,0)	
Bladex.AddBipedAction("Dgk","WBK_1h","Dgk_attack_b",0.0,1.0,0)		
Bladex.AddBipedAction("Dgk","WBK_2h","Dgk_attack_b",0.0,1.0,0)		
Bladex.AddBipedAction("Dgk","WBK_s","Dgk_attack_b",0.0,1.0,0)	

#Andar hacia delante
Bladex.AddBipedAction("Dgk","WLK_b","Dgk_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","WLK_no","Dgk_rlx_1",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","WLK_1h","Dgk_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","WLK_2h","Dgk_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","WLK_s","Dgk_attack_f",0.0,1.0,0)

#Correr hacia delante
Bladex.AddBipedAction("Dgk","JOG_b","Dgk_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","JOG_no","Dgk_rlx_1",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","JOG_s","Dgk_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","JOG_1h","Dgk_rlx_1",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","JOG_2h","Dgk_attack_f",0.0,1.0,0)

#Correr hacia atrás
Bladex.AddBipedAction("Dgk","WBK_JOG_b","Dgk_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","WBK_JOG_no","Dgk_rlx_1",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","WBK_JOG_1h","Dgk_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","WBK_JOG_2h","Dgk_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","WBK_JOG_s","Dgk_attack_b",0.0,1.0,0)

#Modo sneak
Bladex.AddBipedAction("Dgk","SNK_b","Dgk_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","SNK_no","Dgk_rlx_1",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","SNK_s", "Dgk_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","SNK_1h","Dgk_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","SNK_2h","Dgk_attack_f",0.0,1.0,0)





####################################################################################
#
# Caidas.
#
####################################################################################

Bladex.AddBipedAction("Dgk","FllLow","Dgk_attack_f",0.5,0.8,0)
Bladex.AddBipedAction("Dgk","FllMed","Dgk_attack_f",0.37,0.8,0)
Bladex.AddBipedAction("Dgk","FllHigh","Dgk_attack_f",0.1,0.8,0)




####################################################################################
#
# Animaciones en combate
#
####################################################################################

#MOvement without weapons
Bladex.AddBipedAction("Dgk","Attack_f_no","Dgk_rlx_1",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Attack_b_no","Dgk_rlx_1",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Attack_r_no","Dgk_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Attack_l_no","Dgk_attack_l",0.0,1.0,0)

#MOvement with both weapons
Bladex.AddBipedAction("Dgk","Attack_f_2h","Dgk_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Attack_b_2h","Dgk_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Attack_r_2h","Dgk_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Attack_l_2h","Dgk_attack_l",0.0,1.0,0)


#Movement with shield
Bladex.AddBipedAction("Dgk","Attack_f_s","Dgk_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Attack_b_s","Dgk_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Attack_r_s","Dgk_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Attack_l_s","Dgk_attack_l",0.0,1.0,0)

#Movement without weapon with shield BEING raised
Bladex.AddBipedAction("Dgk","Shattack_f_s","Dgk_attack_f_s",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Shattack_b_s","Dgk_attack_b_s",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Shattack_r_s","Dgk_attack_r_s",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Shattack_l_s","Dgk_attack_l_s",0.0,1.0,0)

#Movement with shield BEING raised
Bladex.AddBipedAction("Dgk","Shattack_f_2h","Dgk_attack_f_s",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Shattack_b_2h","Dgk_attack_b_s",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Shattack_r_2h","Dgk_attack_r_s",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Shattack_l_2h","Dgk_attack_l_s",0.0,1.0,0)

#Relax
Bladex.AddBipedAction("Dgk","Rlx_f_no","Dgk_rlx_1",0.0,1.0,0)
#Bladex.AddBipedAction("Dgk","Rlx_f_1h","Dgk_rlx_1",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Rlx_f_2h","Dgk_rlx_1h",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Rlx_f_s","Dgk_rlx_1",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","Shattack_rlx_2h","Dgk_rlx_s",0.0,1.0,0)

Bladex.AddBipedAction("Dgk","Rlx_block","Dgk_rlx_s",0.0,1.0,0)


#Dodges
Bladex.AddBipedAction("Dgk","D_b","Dgk_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","D_l","Dgk_attack_l",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","D_r","Dgk_attack_r",0.0,1.0,0)

Bladex.AddBipedAction("Dgk","catch","Dgk_catch",0.0,1.0,0)


#Dodge-attacks
Bladex.AddBipedAction("Dgk","g_d_l","Dgk_g_d_l",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","g_d_r","Dgk_g_d_r",0.0,1.0,0)


##MOvement without shield
#Bladex.AddBipedAction("Dgk","Attack_f_1h","Dgk_rlx_1",0.0,1.0,0)
#Bladex.AddBipedAction("Dgk","Attack_b_1h","Dgk_rlx_1",0.0,1.0,0)
#Bladex.AddBipedAction("Dgk","Attack_r_1h","Dgk_attack_r",0.0,1.0,0)
#Bladex.AddBipedAction("Dgk","Attack_l_1h","Dgk_attack_l",0.0,1.0,0)
#
##Quick turns
#Bladex.AddBipedAction("Dgk","Attack_t_r","Dgk_attack_r",0.0,1.0,0)
#Bladex.AddBipedAction("Dgk","Attack_t_r_s","Dgk_rlx_s",0.0,1.0,0)
#Bladex.AddBipedAction("Dgk","Attack_t_l","Dgk_attack_l",0.0,1.0,0)
#Bladex.AddBipedAction("Dgk","Attack_t_l_s","Dgk_rlx_s",0.0,1.0,0)






####################################################################################
#
# Heridas
#
####################################################################################

Bladex.AddBipedAction("Dgk","df_01","Dgk_df_01",0.13,0.55,0)	
Bladex.AddBipedAction("Dgk","df_02","Dgk_df_02",0.08,0.57,0)

Bladex.AddBipedAction("Dgk","sw_react","Dgk_hurt_big",0.06,0.47,0)
	
Bladex.AddBipedAction("Dgk","hurt_f_lite","Dgk_hurt_lite",0.10,0.57,0)	
Bladex.AddBipedAction("Dgk","hurt_f_big","Dgk_hurt_big",0.06,0.47,0)	

Bladex.AddBipedAction("Dgk","hurt_f_head","Dgk_hurt_big",0.06,0.47,0)	
Bladex.AddBipedAction("Dgk","hurt_f_breast","Dgk_hurt_chest",0.29,0.40,0)	
Bladex.AddBipedAction("Dgk","hurt_f_back","Dgk_hurt_back",0.10,0.43,0)	
Bladex.AddBipedAction("Dgk","hurt_f_r_arm","Dgk_hurt_r_arm",0.16,0.36,0)	
Bladex.AddBipedAction("Dgk","hurt_f_l_arm","Dgk_hurt_l_arm",0.16,0.36,0)	
Bladex.AddBipedAction("Dgk","hurt_f_r_leg","Dgk_hurt_r_leg",0.10,0.30,0)	
Bladex.AddBipedAction("Dgk","hurt_f_l_leg","Dgk_hurt_l_leg",0.10,0.30,0)	

Bladex.AddBipedAction("Dgk","hurt_jog","Dgk_hurt_back",0.10,0.43,0)	

Bladex.AddBipedAction("Dgk","hurt_head","Dgk_hurt_big",0.06,0.47,0)	
Bladex.AddBipedAction("Dgk","hurt_breast","Dgk_hurt_chest",0.29,0.40,0)	
Bladex.AddBipedAction("Dgk","hurt_back","Dgk_hurt_back",0.10,0.43,0)	
Bladex.AddBipedAction("Dgk","hurt_r_arm","Dgk_hurt_r_arm",0.16,0.36,0)	
Bladex.AddBipedAction("Dgk","hurt_l_arm","Dgk_hurt_l_arm",0.16,0.36,0)	
Bladex.AddBipedAction("Dgk","hurt_r_leg","Dgk_hurt_r_leg",0.10,0.30,0)	
Bladex.AddBipedAction("Dgk","hurt_l_leg","Dgk_hurt_l_leg",0.10,0.30,0)	

	
Bladex.AddBipedAction("Dgk","dth0","Dgk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","dth_c1","Dgk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","dth_c2","Dgk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","dth_c3","Dgk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","dth_c4","Dgk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","dth_c5","Dgk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","dth_c6","Dgk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","dth_c7","Dgk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","dth0",  "Dgk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","dth_n00","Dgk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","dth_n01","Dgk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","dth_n02","Dgk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","dth_n03","Dgk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","dth_n04","Dgk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","dth_n05","Dgk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","dth_n06","Dgk_dth0",0.0,1.0,0)
                       
Bladex.AddBipedAction("Dgk","dth_rock","Dgk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","dth_rockfront","Dgk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","dth_burn","Dgk_dth0",0.0,1.0,0)	




####################################################################################
#
# Ataques
#
####################################################################################

Bladex.AddBipedAction("Dgk","g_m01","Dgk_g_m01",0.0,1.0,0) #DISC	
Bladex.AddBipedAction("Dgk","g_m02","Dgk_g_m02",0.0,1.0,0) #ENERGY BALL	
Bladex.AddBipedAction("Dgk","g_tw5","Dgk_g_tw5",0.0,1.0,0) #Launched Weapon
Bladex.AddBipedAction("Dgk","g_magic","Dgk_g_magic",0.0,1.0,0) #Launched Weapon
Bladex.AddBipedAction("Dgk","g_magic2","Dgk_g_magic2",0.0,1.0,0) #Launched Weapon
Bladex.AddBipedAction("Dgk","g_07_new","Dgk_g_07_new",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","g_08_new","Dgk_g_08_new",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","g_02_new","Dgk_g_02_new",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","g_01_7_new","Dgk_g_01_7_new",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","g_22lowkata_new","Dgk_g_22lowkata_new",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","g_21_6_s8new","Dgk_g_21_6_s8new",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","g_19_bs1_new","Dgk_g_19_bs1_new",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","g_b32kata_new","Dgk_g_b32kata_new",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","g_29_3new","Dgk_g_29_3new",0.0,1.0,0)
Bladex.AddBipedAction("Dgk","g_back","Dgk_g_back",0.0,1.0,0)