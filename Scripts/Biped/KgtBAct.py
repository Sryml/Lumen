import Bladex



####################################################################################
#
# Escalar + saltos
#
####################################################################################

Bladex.AddBipedAction("Knight","clmb_low_1h","Kgt_clmb_low_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Knight","clmb_medlow_1h","Kgt_clmb_medlow_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Knight","clmb_medium_1h","Kgt_clmb_medium_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Knight","clmb_high_1h","Kgt_clmb_high_1h",0.0,0.934,0)	

Bladex.AddBipedAction("Knight","LongJump1H","Kgt_jmp_1h",0.06,0.93,0)	
Bladex.AddBipedAction("Knight","LongJumpNo","Kgt_jmp_no",0.06,0.93,0)	
Bladex.AddBipedAction("Knight","ShortJump","Kgt_jmph0_no",0.41,1.0,0)	


####################################################################################
#
# Others
#
####################################################################################

Bladex.AddBipedAction("Knight","slip","Kgt_slip",0.0,1.0,0)	
#Bladex.AddBipedAction("Knight","slip_b","Kgt_slip_b",0.0,1.0,0)	
Bladex.AddBipedAction("Knight","derrape","Kgt_derrape",0.14,1.0,0)	



Bladex.AddBipedAction("Knight","b1","Kgt_b1",0.0,1.0,0)	
Bladex.AddBipedAction("Knight","b2","Kgt_b2",0.0,1.0,0)	
Bladex.AddBipedAction("Knight","b3","Kgt_b3",0.0,1.0,0)
	
Bladex.AddBipedAction("Knight","1tw_h_f","Kgt_1tw_h_f",0.0,1.0,0)	
Bladex.AddBipedAction("Knight","1tw_l_f","Kgt_1tw_l_f",0.0,0.75,0)	


Bladex.AddBipedAction("Knight","jog_turn","Kgt_jog_turn",0.0,1.0,0)	
Bladex.AddBipedAction("Knight","wlk_turn","Kgt_wlk_turn",0.0,1.0,0)	
Bladex.AddBipedAction("Knight","snk_turn","Kgt_snk_turn",0.0,1.0,0)	
Bladex.AddBipedAction("Knight","rlx_turn","Kgt_rlx_turn",0.0,1.0,0)	


####################################################################################
#
# Relax.
#
####################################################################################

Bladex.AddBipedAction("Knight","Rlx_no","Rlx_no_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Rlx_1h","Rlx_1h_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Rlx_b","Rlx_b_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Rlx_2h","Rlx_2h_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Rlx_s","Rlx_s_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Rlx_2w","Rlx_2w_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Rlx_axe","Rlx_spear_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Rlx_sp","Rlx_spear_Kgt",0.0,1.0,0)

Bladex.AddBipedAction("Knight","Rlx_block","Kgt_attack_rlx_s",0.0,1.0,0)

Bladex.AddBipedAction("Knight","Rlx_vt","Kgt_rlx_vt",0.0,1.0,0)






####################################################################################
#
# Pasos.- Andares
#
####################################################################################

#Movement with shield -> !NPC only!!!!
Bladex.AddBipedAction("Knight","Attack_f_s_nc","Kgt_attack_f_s",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_b_s_nc","Kgt_attack_b_s",0.0,1.0,0)


#pasito
#Bladex.AddBipedAction("Knight","ShortStep_no","WlkShort_Kgt", 0.0,1.0,0)
#Bladex.AddBipedAction("Knight","ShortStep_s","WlkShort_Kgt", 0.0,1.0,0)
#Bladex.AddBipedAction("Knight","ShortStep_1h","WlkShort_Kgt", 0.0,1.0,0)
#Bladex.AddBipedAction("Knight","ShortStep_2h","WlkShort_Kgt", 0.0,1.0,0)
#Bladex.AddBipedAction("Knight","ShortStep_b","WlkShort_Kgt", 0.0,1.0,0)
#Bladex.AddBipedAction("Knight","ShortStep_2w","WlkShort_2w_Kgt", 0.0,1.0,0)
#Bladex.AddBipedAction("Knight","ShortStep_sp","WlkShort_spear_Kgt", 0.0,1.0,0)
#Bladex.AddBipedAction("Knight","ShortStep_axe","WlkShort_spear_Kgt", 0.0,1.0,0)





#Bladex.AddBipedAction("Knight","LStepUp","Wlk_1h_Kgt","WlkUp_Kgt",0.0,0.5,0)
#Bladex.AddBipedAction("Knight","RStepUp","Wlk_1h_Kgt","WlkUp_Kgt",0.5,1.0,0)

#Bladex.AddBipedAction("Knight","LStairsUp","StairsUp_Kgt","StairsUpP_Kgt",0.0,0.5,0)
#Bladex.AddBipedAction("Knight","RStairsUp","StairsUp_Kgt","StairsUpP_Kgt",0.5,1.0,0)

#Bladex.AddBipedAction("Knight","LStepDown","Wlk_1h_Kgt","WlkDown_Kgt",0.0,0.5,0)
#Bladex.AddBipedAction("Knight","RStepDown","Wlk_1h_Kgt","WlkDown_Kgt",0.5,1.0,0)

#Bladex.AddBipedAction("Knight","LStairsDown","StairsDown_Kgt",0.0,0.5,0)
#Bladex.AddBipedAction("Knight","RStairsDown","StairsDown_Kgt",0.5,1.0,0)

# Andar hacia atrás
Bladex.AddBipedAction("Knight","WBK_b","Wbk_b_Kgt",0.0,1.0,0)	
Bladex.AddBipedAction("Knight","WBK_no","Wbk_no_Kgt",0.0,1.0,0)	
Bladex.AddBipedAction("Knight","WBK_1h","Wbk_1h_Kgt",0.0,1.0,0)		
Bladex.AddBipedAction("Knight","WBK_2h","Wbk_2h_Kgt",0.0,1.0,0)		
Bladex.AddBipedAction("Knight","WBK_s","Wbk_no_Kgt",0.0,1.0,0)	
Bladex.AddBipedAction("Knight","WBK_sp","Wbk_spear_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","WBK_axe","Wbk_spear_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","WBK_2w","Wbk_2w_Kgt",0.0,1.0,0)



#Andar hacia delante
Bladex.AddBipedAction("Knight","WLK_b","Wlk_b_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","WLK_no","Wlk_no_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","WLK_1h","Wlk_1h_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","WLK_2h","Wlk_2h_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","WLK_s","Wlk_s_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","WLK_2w","Wlk_2w_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","WLK_axe","Wlk_spear_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","WLK_sp","Wlk_spear_Kgt",0.0,1.0,0)



#Correr hacia delante
Bladex.AddBipedAction("Knight","JOG_b","Jog_b_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","JOG_no","Jog_no_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","JOG_s","Jog_no_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","JOG_1h","Jog_1h_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","JOG_2h","Jog_1h_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","JOG_2w","Jog_2w_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","JOG_axe","Jog_spear_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","JOG_sp","Jog_spear_Kgt",0.0,1.0,0)




#Correr hacia atrás
Bladex.AddBipedAction("Knight","WBK_JOG_b","Kgt_jogb_no",0.0,1.0,0)
Bladex.AddBipedAction("Knight","WBK_JOG_no","Kgt_jogb_no",0.0,1.0,0)
Bladex.AddBipedAction("Knight","WBK_JOG_1h","Kgt_jogb_1h",0.0,1.0,0)
Bladex.AddBipedAction("Knight","WBK_JOG_2h","Kgt_jogb_2h",0.0,1.0,0)
Bladex.AddBipedAction("Knight","WBK_JOG_s","Kgt_jogb_s",0.0,1.0,0)
Bladex.AddBipedAction("Knight","WBK_JOG_2w","Kgt_jogb_sword",0.0,1.0,0)
Bladex.AddBipedAction("Knight","WBK_JOG_axe","Kgt_jogb_spear",0.0,1.0,0)
Bladex.AddBipedAction("Knight","WBK_JOG_sp","Kgt_jogb_spear",0.0,1.0,0)




#Modo sneak
Bladex.AddBipedAction("Knight","SNK_b","Snk_b_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","SNK_no","Snk_no_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","SNK_s", "Snk_no_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","SNK_1h","Snk_1h_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","SNK_2h","Snk_1h_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","SNK_sp", "Snk_spear_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","SNK_2w","Snk_2w_Kgt",0.0,1.0,0)
Bladex.AddBipedAction("Knight","SNK_axe","Snk_spear_Kgt",0.0,1.0,0)




####################################################################################
#
# Caidas.
#
####################################################################################

Bladex.AddBipedAction("Knight","FllLow","FallLow_Kgt",0.0,0.8,0)
Bladex.AddBipedAction("Knight","FllMed","FallMed_Kgt",0.0,0.8,0)
Bladex.AddBipedAction("Knight","FllHigh","FallHigh_Kgt",0.15,0.9,0)
Bladex.AddBipedAction("Knight","Dth_Fll","Dth_Fll_Kgt",0.0,0.33,0)
Bladex.AddBipedAction("Knight","Dth_Fll2","Dth_Fll2_Kgt",0.0,1.0,0)




####################################################################################
#
# Animaciones en combate
#
####################################################################################

#MOvement without shield
Bladex.AddBipedAction("Knight","Attack_f_1h","Kgt_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_b_1h","Kgt_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_r_1h","Kgt_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_l_1h","Kgt_attack_l",0.0,1.0,0)

#MOvement without shield
Bladex.AddBipedAction("Knight","Attack_f_2h","Kgt_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_b_2h","Kgt_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_r_2h","Kgt_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_l_2h","Kgt_attack_l",0.0,1.0,0)

#MOvement without weapons
Bladex.AddBipedAction("Knight","Attack_f_no","Kgt_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_b_no","Kgt_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_r_no","Kgt_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_l_no","Kgt_attack_l",0.0,1.0,0)

#MOvement without weapon but shield none raised
Bladex.AddBipedAction("Knight","Attack_f_s","Kgt_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_b_s","Kgt_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_r_s","Kgt_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_l_s","Kgt_attack_l",0.0,1.0,0)

#MOvement without weapon with shield BEING raised
Bladex.AddBipedAction("Knight","Shattack_f_s","Kgt_attack_f_s",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Shattack_b_s","Kgt_attack_b_s",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Shattack_r_s","Kgt_attack_r_s",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Shattack_l_s","Kgt_attack_l_s",0.0,1.0,0)

#Movement with shield
Bladex.AddBipedAction("Knight","Shattack_f_2h","Kgt_attack_f_s",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Shattack_b_2h","Kgt_attack_b_s",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Shattack_r_2h","Kgt_attack_r_s",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Shattack_l_2h","Kgt_attack_l_s",0.0,1.0,0)

#Movement with 2hand sword
Bladex.AddBipedAction("Knight","Attack_f_2w","Kgt_attack_f_sword",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_b_2w","Kgt_jogb_sword",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_r_2w","Kgt_attack_r_sword",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_l_2w","Kgt_attack_l_sword",0.0,1.0,0)

#Movement with axe
Bladex.AddBipedAction("Knight","Attack_f_axe","Kgt_attack_f_spear",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_b_axe","Kgt_jogb_spear",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_r_axe","Kgt_attack_r_spear",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_l_axe","Kgt_attack_l_spear",0.0,1.0,0)


#MOvement with spear
Bladex.AddBipedAction("Knight","Attack_f_sp","Kgt_attack_f_spear",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_b_sp","Kgt_jogb_spear",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_r_sp","Kgt_attack_r_spear",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_l_sp","Kgt_attack_l_spear",0.0,1.0,0)



#Relax
Bladex.AddBipedAction("Knight","Rlx_f_1h","Kgt_rlx_f",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Rlx_f_2h","Kgt_rlx_f",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Shattack_rlx_2h","Kgt_attack_rlx_s",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Shattack_rlx_s","Kgt_attack_rlx_s",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Rlx_f_axe","Kgt_rlx_f_spear",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Rlx_f_sp","Kgt_rlx_f_spear",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Rlx_f_2w","Kgt_rlx_f_sword",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Rlx_f_no","Kgt_rlx_f",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Rlx_f_s","Kgt_rlx_f",0.0,1.0,0)



#Quick turns
#Bladex.AddBipedAction("Knight","Attack_t_r","Kgt_attack_t_r",0.0,1.0,0)
#Bladex.AddBipedAction("Knight","Attack_t_r_s","Kgt_attack_t_r_s",0.0,1.0,0)
#Bladex.AddBipedAction("Knight","Attack_t_l","Kgt_attack_t_l",0.0,1.0,0)
#Bladex.AddBipedAction("Knight","Attack_t_l_s","Kgt_attack_t_l_s",0.0,1.0,0)

#Dodge-attacks
Bladex.AddBipedAction("Knight","g_d_l","Kgt_g_d_l",0.36,1.0,0)
Bladex.AddBipedAction("Knight","g_d_r","Kgt_g_d_r",0.37,1.0,0)


#Dodges
Bladex.AddBipedAction("Knight","D_b","Kgt_d_b",0.0,0.75,0)
Bladex.AddBipedAction("Knight","D_l","Kgt_g_d_l",0.0,0.32,0)
Bladex.AddBipedAction("Knight","D_r","Kgt_g_d_r",0.0,0.3,0)


#Parry - 2 handed things exclusively!
Bladex.AddBipedAction("Knight","Parry_axe","Kgt_parryspear",0.0,0.65,0)
Bladex.AddBipedAction("Knight","Parry_2w","Kgt_parry2w",0.0,0.50,0)
Bladex.AddBipedAction("Knight","Parry_sp","Kgt_parryspear",0.0,0.65,0)


####################################################################################
#
# REACCIONES A LOS GOLPES:  Heridas / detenciones
#
####################################################################################

Bladex.AddBipedAction("Knight","df_01","Kgt_df_01",0.0,0.420,0)
Bladex.AddBipedAction("Knight","df_02","Kgt_df_02",0.0,0.680,0)

Bladex.AddBipedAction("Knight","df_01_spear","Kgt_df_01_spear",0.0,1.0,0)
Bladex.AddBipedAction("Knight","df_02_spear","Kgt_df_02_spear",0.0,1.0,0)

Bladex.AddBipedAction("Knight","df_01_axe","Kgt_df_01_spear",0.0,1.0,0)
Bladex.AddBipedAction("Knight","df_02_axe","Kgt_df_02_spear",0.0,1.0,0)

Bladex.AddBipedAction("Knight","df_01_2w","Kgt_df_01_2w",0.0,0.45,0)
Bladex.AddBipedAction("Knight","df_02_2w","Kgt_df_02_2w",0.0,1.0,0)

Bladex.AddBipedAction("Knight","df_s_broken","Kgt_df_s_broken",0.0,1.0,0)

Bladex.AddBipedAction("Knight","sw_react","Kgt_sword_reaction",0.10,0.60,0)

Bladex.AddBipedAction("Knight","sword_broken","Kgt_sword_broken",0.10,0.60,0)



	
Bladex.AddBipedAction("Knight","hurt_f_lite","Kgt_hurt_f_lite",0.14,0.65,0)	
Bladex.AddBipedAction("Knight","hurt_f_big","Kgt_hurt_f_big",0.10,0.59,0)	

Bladex.AddBipedAction("Knight","hurt_f_head","Kgt_hurt_f_head",0.11,0.60,0)	
Bladex.AddBipedAction("Knight","hurt_f_breast","Kgt_hurt_f_breast",0.11,0.58,0)	
Bladex.AddBipedAction("Knight","hurt_f_back","Kgt_hurt_f_back",0.10,0.58,0)	
Bladex.AddBipedAction("Knight","hurt_f_r_arm","Kgt_hurt_f_r_arm",0.10,0.55,0)	
Bladex.AddBipedAction("Knight","hurt_f_l_arm","Kgt_hurt_f_l_arm",0.10,0.58,0)	
Bladex.AddBipedAction("Knight","hurt_f_r_leg","Kgt_hurt_f_r_leg",0.10,0.54,0)	
Bladex.AddBipedAction("Knight","hurt_f_l_leg","Kgt_hurt_f_l_leg",0.10,0.56,0)	

Bladex.AddBipedAction("Knight","hurt_jog","Kgt_hurt_jog",0.05,0.37,0)	

Bladex.AddBipedAction("Knight","hurt_head","Kgt_hurt_head",0.10,0.50,0)	
Bladex.AddBipedAction("Knight","hurt_breast","Kgt_hurt_breast",0.10,0.50,0)	
Bladex.AddBipedAction("Knight","hurt_back","Kgt_hurt_back",0.10,0.53,0)	
Bladex.AddBipedAction("Knight","hurt_r_arm","Kgt_hurt_r_arm",0.10,0.50,0)	
Bladex.AddBipedAction("Knight","hurt_l_arm","Kgt_hurt_l_arm",0.10,0.50,0)	
Bladex.AddBipedAction("Knight","hurt_r_leg","Kgt_hurt_r_leg",0.10,0.50,0)	
Bladex.AddBipedAction("Knight","hurt_l_leg","Kgt_hurt_l_leg",0.10,0.54,0)




####################################################################################
#
# Cambiar Armas
#
####################################################################################	

Bladex.AddBipedAction("Knight","Attack_Chg_r_l","Kgt_attack_chg_r_l",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_Chg_r",  "Kgt_attack_chg_r",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Attack_Chg_l",  "Kgt_attack_chg_l",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Chg_r_l",       "Kgt_attack_chg_r_l",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Chg_r",         "Kgt_attack_chg_r",0.0,1.0,0)
Bladex.AddBipedAction("Knight","Chg_l",         "Kgt_attack_chg_l",0.0,1.0,0)
Bladex.AddBipedAction("Knight","drp_r",         "Kgt_drp_r",0.0,1.0,0)
Bladex.AddBipedAction("Knight","drp_l",         "Kgt_drp_l",0.0,1.0,0)




####################################################################################
#
# eat/drink/use/activate
#
####################################################################################	

Bladex.AddBipedAction("Knight","gulp00","Kgt_gulp00",0.0,1.0,0)
Bladex.AddBipedAction("Knight","eat00", "Kgt_eat00",0.0,1.0,0)
Bladex.AddBipedAction("Knight","drink", "Kgt_drink",0.0,1.0,0)
Bladex.AddBipedAction("Knight","attack_drink", "Kgt_attack_drink",0.0,1.0,0)

Bladex.AddBipedAction("Knight","key","Kgt_key",0.0,1.0,0)
Bladex.AddBipedAction("Knight","pulsador","Kgt_pulsador",0.0,1.0,0)
Bladex.AddBipedAction("Knight","lvr_d","Kgt_lvr_d",0.0,1.0,0)
Bladex.AddBipedAction("Knight","lvr_u","Kgt_lvr_u",0.0,1.0,0)

Bladex.AddBipedAction("Knight","fire0","Kgt_fire0",0.0,1.0,0)
Bladex.AddBipedAction("Knight","fire1","Kgt_fire1",0.0,1.0,0)
Bladex.AddBipedAction("Knight","fire2","Kgt_fire2",0.0,1.0,0)
Bladex.AddBipedAction("Knight","fire3","Kgt_fire3",0.0,1.0,0)
Bladex.AddBipedAction("Knight","fire_g","Kgt_fire_g",0.0,1.0,0)




####################################################################################
#
# tke
#
####################################################################################

Bladex.AddBipedAction("Knight","tke_r_01",    "Kgt_tke_r_01",0.0,1.0,0)
Bladex.AddBipedAction("Knight","tke_r_02",    "Kgt_tke_r_02",0.0,1.0,0)
Bladex.AddBipedAction("Knight","tke_r_03",    "Kgt_tke_r_03",0.0,1.0,0)
Bladex.AddBipedAction("Knight","tke_r_04",    "Kgt_tke_r_04",0.0,1.0,0)
Bladex.AddBipedAction("Knight","tke_r_05",    "Kgt_tke_r_05",0.0,1.0,0)
Bladex.AddBipedAction("Knight","tke_r_key00","Kgt_tke_r_key00",0.0,1.0,0)
Bladex.AddBipedAction("Knight","tke_r_key01","Kgt_tke_r_key01",0.0,1.0,0)
Bladex.AddBipedAction("Knight","tke_r_key02","Kgt_tke_r_key02",0.0,1.0,0)
Bladex.AddBipedAction("Knight","tke_r_key03","Kgt_tke_r_key03",0.0,1.0,0)
Bladex.AddBipedAction("Knight","tke_r_key04","Kgt_tke_r_key05",0.0,1.0,0)




####################################################################################
#
# MUERTES
#
####################################################################################

Bladex.AddBipedAction("Knight","dth_c1","Kgt_dth_c1",0.0,1.0,0)
Bladex.AddBipedAction("Knight","dth_c2","Kgt_dth_c2",0.0,1.0,0)
Bladex.AddBipedAction("Knight","dth_c3","Kgt_dth_c3",0.0,1.0,0)
Bladex.AddBipedAction("Knight","dth_c4","Kgt_dth_c4",0.0,1.0,0)
Bladex.AddBipedAction("Knight","dth_c5","Kgt_dth_c5",0.0,1.0,0)
Bladex.AddBipedAction("Knight","dth_c6","Kgt_dth_c6",0.0,1.0,0)
Bladex.AddBipedAction("Knight","dth_c7","Kgt_dth_c7",0.0,1.0,0)
Bladex.AddBipedAction("Knight","dth0",  "Kgt_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Knight","dth_n00","Kgt_dth_n00",0.0,1.0,0)
Bladex.AddBipedAction("Knight","dth_n01","Kgt_dth_n01",0.0,1.0,0)
Bladex.AddBipedAction("Knight","dth_n02","Kgt_dth_n02",0.0,1.0,0)
Bladex.AddBipedAction("Knight","dth_n03","Kgt_dth_n03",0.0,1.0,0)
Bladex.AddBipedAction("Knight","dth_n04","Kgt_dth_n04",0.0,1.0,0)
Bladex.AddBipedAction("Knight","dth_n05","Kgt_dth_n05",0.0,1.0,0)
Bladex.AddBipedAction("Knight","dth_n06","Kgt_dth_n06",0.0,1.0,0)

Bladex.AddBipedAction("Knight","dth_rock","Kgt_dth_rock",0.0,1.0,0)
Bladex.AddBipedAction("Knight","dth_rockfront","Kgt_dth_rockfront",0.0,1.0,0)
Bladex.AddBipedAction("Knight","dth_burn","Kgt_dth_burn",0.0,1.0,0)



####################################################################################
#
# Ataques
#
####################################################################################

Bladex.AddBipedAction("Knight","g_08","Kgt_g_08",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_01","Kgt_g_01",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_02","Kgt_g_02",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_05","Kgt_g_05",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_06","Kgt_g_06",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_07","Kgt_g_07",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_09","Kgt_g_09",0.0,1.0,0)

Bladex.AddBipedAction("Knight","g_13","Kgt_g_13",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_18","Kgt_g_18",0.0,1.0,0)

Bladex.AddBipedAction("Knight","g_14","Kgt_g_14",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_11","Kgt_g_11",0.0,1.0,0)

Bladex.AddBipedAction("Knight","g_16","Kgt_g_16",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_12","Kgt_g_12",0.0,1.0,0)

Bladex.AddBipedAction("Knight","g_17","Kgt_g_17",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_15","Kgt_g_15",0.0,1.0,0)

Bladex.AddBipedAction("Knight","g_21","Kgt_g_21",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_22","Kgt_g_22",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_23","Kgt_g_23",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_26","Kgt_g_26",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_27","Kgt_g_27",0.0,1.0,0)

Bladex.AddBipedAction("Knight","g_31","Kgt_g_31",0.0,1.0,0)	

Bladex.AddBipedAction("Knight","g_08_new","Kgt_g_08_new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_01_7_new","Kgt_g_01_7_new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_18_11_22_new","Kgt_g_18_11_22_new",0.0,1.0,0)	
Bladex.AddBipedAction("Knight","g_07_new","Kgt_g_07_new",0.0,1.0,0)	
Bladex.AddBipedAction("Knight","g_s3_new","Kgt_g_s3_new",0.0,1.0,0)	
Bladex.AddBipedAction("Knight","g_12_new","Kgt_g_12_new",0.0,1.0,0)	
Bladex.AddBipedAction("Knight","g_12_7_s1new","Kgt_g_12_7_s1new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_02_new","Kgt_g_02_new",0.0,1.0,0)	
Bladex.AddBipedAction("Knight","g_sb25_new","Kgt_g_sb25_new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_b06_new","Kgt_g_b06_new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_19_bs1_new","Kgt_g_19_bs1_new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_01low_new","Kgt_g_01low_new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_22lowkata_new","Kgt_g_22lowkata_new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_s28kata_new","Kgt_g_s28kata_new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_3s9_6new","Kgt_g_3s9_6new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_06lowkata_new","Kgt_g_06lowkata_new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_28new","Kgt_g_28new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_b32kata_new","Kgt_g_b32kata_new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_s19_new","Kgt_g_s19_new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_29_3new","Kgt_g_29_3new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_21_6_s8new","Kgt_g_21_6_s8new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_s22low_new","Kgt_g_s22low_new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_s18_new","Kgt_g_s18_new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_27kata_new","Kgt_g_27kata_new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_26low_new","Kgt_g_26low_new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_22kata_23_new","Kgt_g_22kata_23_new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_09_07_s6low_new","Kgt_g_09_07_s6low_new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_01_new","Kgt_g_01_new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_07_01_19_26low_new","Kgt_g_07_01_19_26low_new",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_32_5_3new","Kgt_g_32_5_3new",0.0,1.0,0)

Bladex.AddBipedAction("Knight","g_bad_axe","Kgt_g_bad_axe",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_bad_sword","Kgt_g_bad_sword",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_bad_sword2","Kgt_g_bad_sword2",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_bad_sword3","Kgt_g_bad_sword3",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_bad_spear","Kgt_g_bad_spear",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_bad_spear2","Kgt_g_bad_spear2",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_bad_1h","Kgt_g_bad_1h",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_bad_no","Kgt_g_bad_no",0.0,1.0,0)


Bladex.AddBipedAction("Knight","g_back","Kgt_g_back",0.0,1.0,0)


Bladex.AddBipedAction("Knight","g_magic","Kgt_g_magic",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_magic2","Kgt_g_magic2",0.0,1.0,0)

Bladex.AddBipedAction("Knight","g_punch1","Kgt_g_punch1",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_punch2","Kgt_g_punch2",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_punch4","Kgt_g_punch4",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_kick","Kgt_g_kick",0.0,1.0,0)


Bladex.AddBipedAction("Knight","g_draw_rlx","Kgt_g_draw_rlx",0.0,1.0,0)
Bladex.AddBipedAction("Knight","g_draw_run","Kgt_g_draw_run",0.0,1.0,0)
