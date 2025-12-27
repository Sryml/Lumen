import Bladex

#import AnimationSets


#AnimationSets.LoadMinAnimationSet("Min")

####################################################################################
#
# Escalar + saltos
#
####################################################################################

#Bladex.AddBipedAction("Min","clmb_low_1h","Min_clmb_low_1h",0.0,1.0,0)	
#Bladex.AddBipedAction("Min","clmb_medlow_1h","Min_clmb_low_1h",0.0,1.0,0)	
#Bladex.AddBipedAction("Min","clmb_medium_1h","Min_clmb_low_1h",0.0,1.0,0)	
#Bladex.AddBipedAction("Min","clmb_high_1h","Min_clmb_low_1h",0.0,1.0,0)	

Bladex.AddBipedAction("Min","LongJump1H","Jog_1h_Min",0.0,1.0,0)	
Bladex.AddBipedAction("Min","LongJumpNo","Jog_1h_Min",0.0,1.0,0)	
Bladex.AddBipedAction("Min","ShortJump","Jog_1h_Min",0.0,1.0,0)	



####################################################################################
#
# Others
#
####################################################################################

Bladex.AddBipedAction("Min","slip","Min_slip",0.0,1.0,0)	
Bladex.AddBipedAction("Min","slip_b","Min_slip_b",0.0,1.0,0)	
Bladex.AddBipedAction("Min","derrape","Min_derrape",0.0,1.0,0)
	
Bladex.AddBipedAction("Min","eat","Min_eat",0.0,1.0,0)


####################################################################################
#
# Relax.
#
####################################################################################

Bladex.AddBipedAction("Min","Rlx_no","Rlx_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","Rlx_1h","Rlx_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","Rlx_b","Rlx_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","Rlx_2h","Rlx_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","Rlx_s","Rlx_1h_Min",0.0,1.0,0)

####################################################################################
#
# Pasos.- Andares
#
####################################################################################

Bladex.AddBipedAction("Min","ShortStep","Wlk_1h_Min", 0.0,1.0,0)


# Andar hacia atrás
Bladex.AddBipedAction("Min","WBK_b","Wbk_1h_Min",0.0,1.0,0)	
Bladex.AddBipedAction("Min","WBK_no","Wbk_1h_Min",0.0,1.0,0)	
Bladex.AddBipedAction("Min","WBK_1h","Wbk_1h_Min",0.0,1.0,0)		
Bladex.AddBipedAction("Min","WBK_2h","Wbk_1h_Min",0.0,1.0,0)	
Bladex.AddBipedAction("Min","WBK_s","Wbk_1h_Min",0.0,1.0,0)

#Andar hacia alante
Bladex.AddBipedAction("Min","WLK_b","Wlk_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","WLK_no","Wlk_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","WLK_1h","Wlk_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","WLK_2h","Wlk_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","WLK_s","Wlk_1h_Min",0.0,1.0,0)

#Correr hacia atrás
Bladex.AddBipedAction("Min","WBK_JOG_b","Wbk_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","WBK_JOG_no","Wbk_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","WBK_JOG_s","Wbk_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","WBK_JOG_1h","Wbk_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","WBK_JOG_2h","Wbk_1h_Min",0.0,1.0,0)

#Correr hacia delante
Bladex.AddBipedAction("Min","JOG_b","Jog_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","JOG_no","Jog_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","JOG_s","Jog_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","JOG_1h","Jog_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","JOG_2h","Jog_1h_Min",0.0,1.0,0)


#Modo sneak
Bladex.AddBipedAction("Min","SNK_b","Wlk_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","SNK_no","Wlk_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","SNK_s","Wlk_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","SNK_1h","Wlk_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","SNK_2h","Wlk_1h_Min",0.0,1.0,0)




####################################################################################
#
# Caidas.
#
####################################################################################

Bladex.AddBipedAction("Min","FllLow","FallLow_Min",0.0,0.8,0)
Bladex.AddBipedAction("Min","FllMed","FallLow_Min",0.0,0.8,0)
Bladex.AddBipedAction("Min","FllHigh","FallLow_Min",0.0,0.8,0)
Bladex.AddBipedAction("Min","Dth_Fll","Dth_Fll_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","Dth_Fll2","Min_dth_fll2",0.0,1.0,0)





####################################################################################
#
# Animaciones en combate
#
####################################################################################

#MOvement without shield
Bladex.AddBipedAction("Min","Attack_f_1h","Wlk_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","Attack_b_1h","Wbk_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","Attack_r_1h","Wlk_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","Attack_l_1h","Wlk_1h_Min",0.0,1.0,0)

Bladex.AddBipedAction("Min","Attack_f_2h","Wlk_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","Attack_b_2h","Wbk_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","Attack_r_2h","Wlk_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","Attack_l_2h","Wlk_1h_Min",0.0,1.0,0)

#Movement with shield
Bladex.AddBipedAction("Min","Shattack_f_2h","Wlk_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","Shattack_b_2h","Wbk_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","Shattack_r_2h","Wlk_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","Shattack_l_2h","Wlk_1h_Min",0.0,1.0,0)

#Relax
Bladex.AddBipedAction("Min","Rlx_f_1h","Rlx_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","Rlx_f_2h","Rlx_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","Shattack_rlx_2h","Rlx_1h_Min",0.0,1.0,0)

#Quick turns
#Bladex.AddBipedAction("Min","Attack_t_r","Rlx_1h_Min",0.0,1.0,0)
#Bladex.AddBipedAction("Min","Attack_t_r_s","Rlx_1h_Min",0.0,1.0,0)
#Bladex.AddBipedAction("Min","Attack_t_l","Rlx_1h_Min",0.0,1.0,0)
#Bladex.AddBipedAction("Min","Attack_t_l_s","Rlx_1h_Min",0.0,1.0,0)


#Dodges
Bladex.AddBipedAction("Min","D_b","Rlx_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","D_l","Rlx_1h_Min",0.0,1.0,0)
Bladex.AddBipedAction("Min","D_r","Rlx_1h_Min",0.0,1.0,0)



####################################################################################
#
# Ataques
#
####################################################################################

Bladex.AddBipedAction("Min","g_08","Min_g_08",0.0,1.0,0)	
Bladex.AddBipedAction("Min","g_01","Min_g_01",0.0,1.0,0)	
Bladex.AddBipedAction("Min","g_07","Min_g_07",0.0,1.0,0)	
Bladex.AddBipedAction("Min","g_12","Min_g_12",0.0,1.0,0)
Bladex.AddBipedAction("Min","g_31","Min_g_31",0.0,1.0,0)



#######################
#                     #
#   Añadidos Luismi   #
#                     #
#######################


#### "Rotura escudo"

Bladex.AddBipedAction("Min","df_s_broken","Min_hurt_big",0.0,1.0,0)


####  Muertes

Bladex.AddBipedAction("Min","dth0","Min_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Min","dth_n00","Min_dth_n00",0.0,1.0,0)
Bladex.AddBipedAction("Min","dth_c1","Min_dth_c1",0.0,1.0,0)
Bladex.AddBipedAction("Min","dth_c2","Min_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Min","dth_c3","Min_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Min","dth_c4","Min_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Min","dth_c5","Min_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Min","dth_c6","Min_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Min","dth_c7","Min_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Min","dth0",  "Min_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Min","dth_n01","Min_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Min","dth_n02","Min_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Min","dth_n03","Min_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Min","dth_n04","Min_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Min","dth_n05","Min_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Min","dth_n06","Min_dth0",0.0,1.0,0)
                       
Bladex.AddBipedAction("Min","dth_rock","Min_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Min","dth_rockfront","Min_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Min","dth_burn","Min_dth0",0.0,1.0,0)	


####  Heridas

Bladex.AddBipedAction("Min","df_01","Min_hurt_big",0.0,1.0,0)
Bladex.AddBipedAction("Min","df_02","Min_hurt_big",0.0,1.0,0)

Bladex.AddBipedAction("Min","hurt_f_lite","Min_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Min","hurt_f_big","Min_hurt_big",0.0,1.0,0)
Bladex.AddBipedAction("Min","hurt_f_head","Min_hurt_big",0.0,1.0,0)
Bladex.AddBipedAction("Min","hurt_f_breast","Min_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Min","hurt_f_back","Min_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Min","hurt_f_r_arm","Min_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Min","hurt_f_l_arm","Min_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Min","hurt_f_r_leg","Min_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Min","hurt_f_l_leg","Min_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Min","hurt_jog","Min_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Min","hurt_head","Min_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Min","hurt_breast","Min_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Min","hurt_back","Min_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Min","hurt_r_arm","Min_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Min","hurt_l_arm","Min_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Min","hurt_r_leg","Min_hurt_lite",0.0,1.0,0)
Bladex.AddBipedAction("Min","hurt_l_leg","Min_hurt_lite",0.0,1.0,0)





