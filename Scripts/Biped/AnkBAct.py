import Bladex



####################################################################################
#
# Escalar + saltos
#
####################################################################################

Bladex.AddBipedAction("Ank","clmb_low_1h","Wlk_no_Ank",0.0,1.0,0)	
Bladex.AddBipedAction("Ank","clmb_medlow_1h","Wlk_no_Ank",0.0,1.0,0)	
Bladex.AddBipedAction("Ank","clmb_medium_1h","Wlk_no_Ank",0.0,1.0,0)	
Bladex.AddBipedAction("Ank","clmb_high_1h","Wlk_no_Ank",0.0,1.0,0)	

Bladex.AddBipedAction("Ank","LongJump1H","Wlk_no_Ank",0.0,0.93,0)	
Bladex.AddBipedAction("Ank","LongJumpNo","Wlk_no_Ank",0.0,0.93,0)	
Bladex.AddBipedAction("Ank","ShortJump","Wlk_no_Ank",0.41,1.0,0)	


####################################################################################
#
# Others
#
####################################################################################

Bladex.AddBipedAction("Ank","slip","Wlk_no_Ank",0.0,1.0,0)	
Bladex.AddBipedAction("Ank","slip_b","Wlk_no_Ank",0.0,1.0,0)	
Bladex.AddBipedAction("Ank","derrape","Wlk_no_Ank",0.14,1.0,0)



####################################################################################
#
# Relax.
#
####################################################################################

Bladex.AddBipedAction("Ank","Rlx_no","Rlx_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","Rlx_1h","Rlx_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","Rlx_b","Rlx_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","Rlx_2h","Rlx_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","Rlx_s","Rlx_no_Ank",0.0,1.0,0)







####################################################################################
#
# Pasos.- Andares
#
####################################################################################

#Movement with shield -> !NPC only!!!!
Bladex.AddBipedAction("Ank","Attack_f_s_nc","Wlk_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","Attack_b_s_nc","Wbk_no_Ank",0.0,1.0,0)

#Bladex.AddBipedAction("Ank","ShortStep","Wlk_no_Ank", 0.0,1.0,0)

#Bladex.AddBipedAction("Ank","LStepUp","Wlk_no_Ank","WlkUp_Ank",0.0,0.5,0)
#Bladex.AddBipedAction("Ank","RStepUp","Wlk_no_Ank","WlkUp_Ank",0.5,1.0,0)

#Bladex.AddBipedAction("Ank","LStairsUp","Wlk_no_Ank","Wlk_no_Ank",0.0,0.5,0)
#Bladex.AddBipedAction("Ank","RStairsUp","Wlk_no_Ank","Wlk_no_Ank",0.5,1.0,0)

#Bladex.AddBipedAction("Ank","LStepDown","Wlk_no_Ank","Wlk_no_Ank",0.0,0.5,0)
#Bladex.AddBipedAction("Ank","RStepDown","Wlk_no_Ank","Wlk_no_Ank",0.5,1.0,0)

#Bladex.AddBipedAction("Ank","LStairsDown","Wlk_no_Ank",0.0,0.5,0)
#Bladex.AddBipedAction("Ank","RStairsDown","Wlk_no_Ank",0.5,1.0,0)

# Andar hacia atrás
Bladex.AddBipedAction("Ank","WBK_b","Wbk_no_Ank",0.0,1.0,0)	
Bladex.AddBipedAction("Ank","WBK_no","Wbk_no_Ank",0.0,1.0,0)	
Bladex.AddBipedAction("Ank","WBK_1h","Wbk_no_Ank",0.0,1.0,0)		
Bladex.AddBipedAction("Ank","WBK_2h","Wbk_no_Ank",0.0,1.0,0)		
Bladex.AddBipedAction("Ank","WBK_s","Wbk_no_Ank",0.0,1.0,0)	

#Andar hacia delante
Bladex.AddBipedAction("Ank","WLK_b","Wlk_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","WLK_no","Wlk_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","WLK_1h","Wlk_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","WLK_2h","Wlk_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","WLK_s","Wlk_no_Ank",0.0,1.0,0)

#Correr hacia delante
Bladex.AddBipedAction("Ank","JOG_b","Wlk_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","JOG_no","Wlk_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","JOG_s","Wlk_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","JOG_1h","Wlk_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","JOG_2h","Wlk_no_Ank",0.0,1.0,0)

#Correr hacia atrás
Bladex.AddBipedAction("Ank","WBK_JOG_b","Wbk_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","WBK_JOG_no","Wbk_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","WBK_JOG_1h","Wbk_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","WBK_JOG_2h","Wbk_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","WBK_JOG_s","Wbk_no_Ank",0.0,1.0,0)

#Modo sneak
Bladex.AddBipedAction("Ank","SNK_b","Wlk_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","SNK_no","Wlk_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","SNK_s", "Wlk_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","SNK_1h","Wlk_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","SNK_2h","Wlk_no_Ank",0.0,1.0,0)





####################################################################################
#
# Caidas.
#
####################################################################################

Bladex.AddBipedAction("Ank","FllLow","Ank_fll",0.5,0.8,0)
Bladex.AddBipedAction("Ank","FllMed","Ank_fll",0.37,0.8,0)
Bladex.AddBipedAction("Ank","FllHigh","Ank_fll",0.1,0.8,0)
Bladex.AddBipedAction("Ank","Dth_Fll","Ank_fll",0.0,0.33,0)
Bladex.AddBipedAction("Ank","Dth_Fll2","Ank_fll",0.11,0.9,0)




####################################################################################
#
# Animaciones en combate
#
####################################################################################

#MOvement without shield
Bladex.AddBipedAction("Ank","Attack_f_no","Wlk_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","Attack_b_no","Wbk_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","Attack_r_no","Wlk_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","Attack_l_no","Wlk_no_Ank",0.0,1.0,0)

#Relax
Bladex.AddBipedAction("Ank","Rlx_f_no","Rlx_no_Ank",0.0,1.0,0)

##Quick turns
#Bladex.AddBipedAction("Ank","Attack_t_r","Rlx_no_Ank",0.0,1.0,0)
#Bladex.AddBipedAction("Ank","Attack_t_r_s","Rlx_no_Ank",0.0,1.0,0)
#Bladex.AddBipedAction("Ank","Attack_t_l","Rlx_no_Ank",0.0,1.0,0)
#Bladex.AddBipedAction("Ank","Attack_t_l_s","Rlx_no_Ank",0.0,1.0,0)


#Dodges
Bladex.AddBipedAction("Ank","D_b","Rlx_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","D_l","Rlx_no_Ank",0.0,1.0,0)
Bladex.AddBipedAction("Ank","D_r","Rlx_no_Ank",0.0,1.0,0)




####################################################################################
#
# Ataques
#
####################################################################################

Bladex.AddBipedAction("Ank","g_mgc03","Ank_g_mgc03",0.0,1.0,0)	
Bladex.AddBipedAction("Ank","g_01","Ank_g_01",0.0,1.0,0)	
Bladex.AddBipedAction("Ank","g_02","Ank_g_02",0.0,1.0,0)	
Bladex.AddBipedAction("Ank","g_mgc02","Ank_g_mgc02",0.0,1.0,0)	
Bladex.AddBipedAction("Ank","g_mgc01","Ank_g_mgc01",0.0,1.0,0)	
Bladex.AddBipedAction("Ank","g_07","Ank_g_07",0.0,1.0,0)








	
#Bladex.AddBipedAction("Ank","g_09","Ank_g_09",0.0,1.0,0)	
#
#Bladex.AddBipedAction("Ank","g_13","Ank_g_13",0.0,1.0,0)	
#Bladex.AddBipedAction("Ank","g_18","Ank_g_18",0.0,1.0,0)	
#
#Bladex.AddBipedAction("Ank","g_14","Ank_g_14",0.0,1.0,0)	
#Bladex.AddBipedAction("Ank","g_11","Ank_g_11",0.0,1.0,0)	
#
#Bladex.AddBipedAction("Ank","g_16","Ank_g_16",0.0,1.0,0)	
#Bladex.AddBipedAction("Ank","g_12","Ank_g_12",0.0,1.0,0)	
#
#Bladex.AddBipedAction("Ank","g_17","Ank_g_17",0.0,1.0,0)	
#Bladex.AddBipedAction("Ank","g_15","Ank_g_15",0.0,1.0,0)	
#
#Bladex.AddBipedAction("Ank","g_21","Ank_g_21",0.0,1.0,0)	
#Bladex.AddBipedAction("Ank","g_22","Ank_g_22",0.0,1.0,0)	
#Bladex.AddBipedAction("Ank","g_23","Ank_g_23",0.0,1.0,0)	
#Bladex.AddBipedAction("Ank","g_26","Ank_g_26",0.0,1.0,0)	
#Bladex.AddBipedAction("Ank","g_27","Ank_g_27",0.0,1.0,0)	
#
#Bladex.AddBipedAction("Ank","g_31","Ank_g_31",0.0,1.0,0)	




