

def Init():
    import Bladex
    #
    # Some genreic watchanimations . 
    # I didn't knonw were to put them , so here they are ...
    #
    Bladex.AddWatchAnim("agony01")
    Bladex.AddWatchAnim("agony02")
    Bladex.AddWatchAnim("rlx")
    Bladex.AddWatchAnim("rlx_1h")
    Bladex.AddWatchAnim("rlx_2h")
    Bladex.AddWatchAnim("rlx_no")
    Bladex.AddWatchAnim("rlx_b")
    Bladex.AddWatchAnim("rlx_s")
    Bladex.AddWatchAnim("rlx_01")
    Bladex.AddWatchAnim("rlx_02")
    Bladex.AddWatchAnim("dth_sleep")
    Bladex.AddWatchAnim("sleep")
    Bladex.AddWatchAnim("sleep2")
    Bladex.AddWatchAnim("sleep_hit")
    Bladex.AddWatchAnim("sleep_d")
    Bladex.AddWatchAnim("sleep_wall")



#    #
#    # Make the specific overwritings
#    #
#    # 	When the first animation should be launch , 
#    #     it will replaced with the second one
#    #       NOT upper-lower case sensitive
#    #	For example :
#    #		kgt.ChangeAnimation("Kgt_SNK_1H","Kgt_wlk_1h")
#
#
#
#
#
#
#    #
#    # Share animations
#    #
#
#    """
#    VERSIONES VIEJAS 
#    Bladex.ShareAllAnimations("Barbarian_living_dead","Knight_N")		# No existe !!! Quitar ?
#    Bladex.ShareAllAnimations("Copperson","Knight_N")					# No existe !!! Quitar ?
#    Bladex.ShareAllAnimations("Buggy","Knight_N")						# No existe !!! Quitar ?
#    Bladex.ShareAllAnimations("ShirGurak","Knight_N")					# No existe !!! Quitar ?
#    #Bladex.ShareAllAnimations("Skeleton_burning","Knight_N")			# No existe !!! Quitar ?
#    #Bladex.ShareAllAnimations("Snake_monk","Knight_N")					# No existe !!! Quitar ?
#    Bladex.ShareAllAnimations("Dasakar","Knight_N")						# No existe !!! Quitar ?
#    #Bladex.ShareAllAnimations("Knight_living_dead","Knight_N")			# No existe !!! Quitar ?
#    Bladex.ShareAllAnimations("Knight_2A0","Knight_N")					# No existe !!! Quitar ?
#    #Bladex.ShareAllAnimations("ChaosKnight","Knight_N")				#Me dijeron que no era asi
#
#    Bladex.ShareAllAnimations("Golem_clay","Troll_Dark")				# No existe !!! Quitar ?
#    Bladex.ShareAllAnimations("Minotaur_chief","Troll_Dark")			# No existe !!! Quitar ?
#    """
#
#
#
#    # Non Playing Races
#    pr1=Bladex.GetCharType("Prisoner_1","Prs_1")
#    pr3=Bladex.GetCharType("Prisoner_3","Prs_3")
#    pr5=Bladex.GetCharType("Prisoner_5","Prs_5")
#    pr6=Bladex.GetCharType("Prisoner_6","Prs_6")
#
#
#
#    Min=Bladex.GetCharType("Minotaur","Min")
#    Min.SetAnmDefaultPrefix("Min")
#    Min.ChangeAnimation("Min_hurt_f_lite",  "Min_hurt_lite") 
#    Min.ChangeAnimation("Min_hurt_f_big",   "Min_hurt_big") 
#    Min.ChangeAnimation("Min_hurt_f_head",  "Min_hurt_big") 
#    Min.ChangeAnimation("Min_hurt_f_breast","Min_hurt_lite") 
#    Min.ChangeAnimation("Min_hurt_f_back",  "Min_hurt_lite") 
#    Min.ChangeAnimation("Min_hurt_f_r_arm", "Min_hurt_lite") 
#    Min.ChangeAnimation("Min_hurt_f_l_arm", "Min_hurt_lite") 
#    Min.ChangeAnimation("Min_hurt_f_r_leg", "Min_hurt_lite") 
#    Min.ChangeAnimation("Min_hurt_f_l_leg", "Min_hurt_lite") 
#    Min.ChangeAnimation("Min_hurt_jog",     "Min_hurt_lite") 
#    Min.ChangeAnimation("Min_hurt_head",    "Min_hurt_lite") 
#    Min.ChangeAnimation("Min_hurt_breast",  "Min_hurt_lite") 
#    Min.ChangeAnimation("Min_hurt_back",    "Min_hurt_lite") 
#    Min.ChangeAnimation("Min_hurt_r_arm",   "Min_hurt_lite") 
#    Min.ChangeAnimation("Min_hurt_l_arm",   "Min_hurt_lite") 
#    Min.ChangeAnimation("Min_hurt_r_leg",   "Min_hurt_lite") 
#    Min.ChangeAnimation("Min_hurt_l_leg",   "Min_hurt_lite") 
#
#
#
#    #PruebaKK
#    Min.ChangeAnimation("Min_df_s_broken",   "Min_hurt_big") 
#    Min.ChangeAnimation("Min_df_01",   "Min_hurt_big") 
#    Min.ChangeAnimation("Min_df_02",   "Min_hurt_big") 
#    Min.ChangeAnimation("Min_shield",   "Min_hurt_big") 
#
#    Slm=Bladex.GetCharType("Salamander","Slm")
#    Slm.SetAnmDefaultPrefix("Slm")
#    Slm.ChangeAnimation("Slm_hurt_lite",    "Slm_hurt_f_lite") 
#    Slm.ChangeAnimation("Slm_hurt_big",     "Slm_hurt_f_big") 
#    Slm.ChangeAnimation("Slm_hurt_f_head",  "Slm_hurt_f_big") 
#    Slm.ChangeAnimation("Slm_hurt_f_breast","Slm_hurt_f_lite") 
#    Slm.ChangeAnimation("Slm_hurt_f_back",  "Slm_hurt_f_lite") 
#    Slm.ChangeAnimation("Slm_hurt_f_r_arm", "Slm_hurt_f_lite") 
#    Slm.ChangeAnimation("Slm_hurt_f_l_arm", "Slm_hurt_f_lite") 
#    Slm.ChangeAnimation("Slm_hurt_f_r_leg", "Slm_hurt_f_lite") 
#    Slm.ChangeAnimation("Slm_hurt_f_l_leg", "Slm_hurt_f_lite") 
#    Slm.ChangeAnimation("Slm_hurt_jog",     "Slm_hurt_f_lite") 
#    Slm.ChangeAnimation("Slm_hurt_head",    "Slm_hurt_f_lite") 
#    Slm.ChangeAnimation("Slm_hurt_breast",  "Slm_hurt_f_lite") 
#    Slm.ChangeAnimation("Slm_hurt_back",    "Slm_hurt_f_lite") 
#    Slm.ChangeAnimation("Slm_hurt_r_arm",   "Slm_hurt_f_lite") 
#    Slm.ChangeAnimation("Slm_hurt_l_arm",   "Slm_hurt_f_lite") 
#    Slm.ChangeAnimation("Slm_hurt_r_leg",   "Slm_hurt_f_lite") 
#    Slm.ChangeAnimation("Slm_hurt_l_leg",   "Slm_hurt_f_lite") 
#
#    Vmp=Bladex.GetCharType("Vamp","Vmp")
#    Vmp.SetAnmDefaultPrefix("Vmp")
#    Vmp.ChangeAnimation("Vmp_hurt_f_lite",  "Vmp_hurt_f_lite") 
#    Vmp.ChangeAnimation("Vmp_hurt_f_big",   "Vmp_hurt_f_big") 
#    Vmp.ChangeAnimation("Vmp_hurt_f_head",  "Vmp_hurt_f_big") 
#    Vmp.ChangeAnimation("Vmp_hurt_f_breast","Vmp_hurt_f_lite") 
#    Vmp.ChangeAnimation("Vmp_hurt_f_back",  "Vmp_hurt_f_lite") 
#    Vmp.ChangeAnimation("Vmp_hurt_f_r_arm", "Vmp_hurt_f_lite") 
#    Vmp.ChangeAnimation("Vmp_hurt_f_l_arm", "Vmp_hurt_f_lite") 
#    Vmp.ChangeAnimation("Vmp_hurt_f_r_leg", "Vmp_hurt_f_lite") 
#    Vmp.ChangeAnimation("Vmp_hurt_f_l_leg", "Vmp_hurt_f_lite") 
#    Vmp.ChangeAnimation("Vmp_hurt_jog",     "Vmp_hurt_lite") 
#    Vmp.ChangeAnimation("Vmp_hurt_head",    "Vmp_hurt_big") 
#    Vmp.ChangeAnimation("Vmp_hurt_breast",  "Vmp_hurt_lite") 
#    Vmp.ChangeAnimation("Vmp_hurt_back",    "Vmp_hurt_lite") 
#    Vmp.ChangeAnimation("Vmp_hurt_r_arm",   "Vmp_hurt_lite") 
#    Vmp.ChangeAnimation("Vmp_hurt_l_arm",   "Vmp_hurt_lite") 
#    Vmp.ChangeAnimation("Vmp_hurt_r_leg",   "Vmp_hurt_lite") 
#    Vmp.ChangeAnimation("Vmp_hurt_l_leg",   "Vmp_hurt_lite") 
#    Vmp.ChangeAnimation("Vmp_df_s_broken",   "Kgt_df_s_broken") 
#    Vmp.ChangeAnimation("Vmp_sword_broken",   "Kgt_sword_broken") 
#
#
#
#
#
#    tkn=Bladex.GetCharType("Knight_Traitor","Tkn")
#    tkn.SetAnmDefaultPrefix("Tkn")
#
#    tkn.ChangeAnimation("Tkn_dth_fll","Kgt_dth_fll")
#    tkn.ChangeAnimation("Tkn_dth_fll2","Kgt_dth_fll2")
#    tkn.ChangeAnimation("Tkn_dth_c1","Kgt_dth_c1")
#    tkn.ChangeAnimation("Tkn_dth_c2","Kgt_dth_c2")
#    tkn.ChangeAnimation("Tkn_dth_c3","Kgt_dth_c3")
#    tkn.ChangeAnimation("Tkn_dth_c4","Kgt_dth_c4")
#    tkn.ChangeAnimation("Tkn_dth_c5","Kgt_dth_c5")
#    tkn.ChangeAnimation("Tkn_dth_c6","Kgt_dth_c6")
#    tkn.ChangeAnimation("Tkn_dth_c7","Ork_dth_c1")
#    tkn.ChangeAnimation("Tkn_dth_burn","Kgt_dth_burn")
#    tkn.ChangeAnimation("Tkn_dth_n01","Kgt_dth_n01")
#    tkn.ChangeAnimation("Tkn_dth_n02","Kgt_dth_n02")
#    tkn.ChangeAnimation("Tkn_dth_n03","Kgt_dth_n03")
#    tkn.ChangeAnimation("Tkn_dth_n04","Kgt_dth_n04")
#    tkn.ChangeAnimation("Tkn_dth_n05","Kgt_dth_n05")
#    tkn.ChangeAnimation("Tkn_dth_n06","Kgt_dth_n06")
#    tkn.ChangeAnimation("Tkn_dth_rock","Kgt_dth_rock")
#    tkn.ChangeAnimation("Tkn_dth_rockfront","Kgt_dth_rockfront")
#    tkn.ChangeAnimation("Tkn_dth0","Kgt_dth0")
#
#    tkn.ChangeAnimation("Tkn_attack_chg_r_l","Kgt_attack_chg_r_l")
#    tkn.ChangeAnimation("Tkn_attack_chg_r","Kgt_attack_chg_r")
#    tkn.ChangeAnimation("Tkn_attack_chg_l","Kgt_attack_chg_l")
#    tkn.ChangeAnimation("Tkn_chg_r_l","Kgt_attack_chg_r_l")
#    tkn.ChangeAnimation("Tkn_chg_r","Kgt_attack_chg_r")
#    tkn.ChangeAnimation("Tkn_chg_l","Kgt_attack_chg_l")
#
#    tkn.ChangeAnimation("Tkn_attack_drink","Kgt_attack_drink")
#
#    tkn.ChangeAnimation("Tkn_hurt_f_lite","Kgt_hurt_f_lite")
#    tkn.ChangeAnimation("Tkn_hurt_f_big","Kgt_hurt_f_big")
#    tkn.ChangeAnimation("Tkn_hurt_f_head","Kgt_hurt_f_head") 
#    tkn.ChangeAnimation("Tkn_hurt_f_breast","Kgt_hurt_f_breast")
#    tkn.ChangeAnimation("Tkn_hurt_f_back","Kgt_hurt_f_back") 
#    tkn.ChangeAnimation("Tkn_hurt_f_r_arm","Kgt_hurt_f_r_arm") 
#    tkn.ChangeAnimation("Tkn_hurt_f_l_arm","Kgt_hurt_f_l_arm")
#    tkn.ChangeAnimation("Tkn_hurt_f_r_leg","Kgt_hurt_f_r_leg")
#    tkn.ChangeAnimation("Tkn_hurt_f_l_leg","Kgt_hurt_f_l_leg")
#    tkn.ChangeAnimation("Tkn_hurt_jog","Kgt_hurt_jog")  
#    tkn.ChangeAnimation("Tkn_hurt_head","Kgt_hurt_head") 
#    tkn.ChangeAnimation("Tkn_hurt_breast","Kgt_hurt_breast") 
#    tkn.ChangeAnimation("Tkn_hurt_back","Kgt_hurt_back") 
#    tkn.ChangeAnimation("Tkn_hurt_r_arm","Kgt_hurt_r_arm") 
#    tkn.ChangeAnimation("Tkn_hurt_l_arm","Kgt_hurt_l_arm") 
#    tkn.ChangeAnimation("Tkn_hurt_r_leg","Kgt_hurt_r_leg") 
#    tkn.ChangeAnimation("Tkn_hurt_l_leg","Kgt_hurt_l_leg")  
#    tkn.ChangeAnimation("Tkn_df_s_broken",   "Kgt_df_s_broken") 
#    tkn.ChangeAnimation("Tkn_sword_broken",   "Kgt_sword_broken") 
#
#
#    tkn.ChangeAnimation("Tkn_look_around",  "Tkn_patrol1")
#    tkn.ChangeAnimation("Tkn_insult",       "Rgn_insult")
#                     
#
#
#
#
#
#
#
#
    dkn=Bladex.GetCharType("Dark_Knight","Dkn")
    dkn.SetAnmDefaultPrefix("Tkn")
#    dkn.ChangeAnimation("Tkn_dth_fll","Kgt_dth_fll")
#    dkn.ChangeAnimation("Tkn_dth_fll2","Kgt_dth_fll2")
#    dkn.ChangeAnimation("Tkn_dth_c1","Kgt_dth_c1")
#    dkn.ChangeAnimation("Tkn_dth_c2","Kgt_dth_c2")
#    dkn.ChangeAnimation("Tkn_dth_c3","Kgt_dth_c3")
#    dkn.ChangeAnimation("Tkn_dth_c4","Kgt_dth_c4")
#    dkn.ChangeAnimation("Tkn_dth_c5","Kgt_dth_c5")
#    dkn.ChangeAnimation("Tkn_dth_c6","Kgt_dth_c6")
#    dkn.ChangeAnimation("Tkn_dth_c7","Ork_dth_c1")
#    dkn.ChangeAnimation("Tkn_dth_burn","Kgt_dth_burn")
#    dkn.ChangeAnimation("Tkn_dth_n01","Kgt_dth_n01")
#    dkn.ChangeAnimation("Tkn_dth_n02","Kgt_dth_n02")
#    dkn.ChangeAnimation("Tkn_dth_n03","Kgt_dth_n03")
#    dkn.ChangeAnimation("Tkn_dth_n04","Kgt_dth_n04")
#    dkn.ChangeAnimation("Tkn_dth_n05","Kgt_dth_n05")
#    dkn.ChangeAnimation("Tkn_dth_n06","Kgt_dth_n06")
#    dkn.ChangeAnimation("Tkn_dth_rock","Kgt_dth_rock")
#    dkn.ChangeAnimation("Tkn_dth_rockfront","Kgt_dth_rockfront")
#    dkn.ChangeAnimation("Tkn_dth0","Kgt_dth0")
#                         
#    dkn.ChangeAnimation("Tkn_attack_chg_r_l","Kgt_attack_chg_r_l")
#    dkn.ChangeAnimation("Tkn_attack_chg_r","Kgt_attack_chg_r")
#    dkn.ChangeAnimation("Tkn_attack_chg_l","Kgt_attack_chg_l")
#    dkn.ChangeAnimation("Tkn_chg_r_l","Kgt_attack_chg_r_l")
#    dkn.ChangeAnimation("Tkn_chg_r","Kgt_attack_chg_r")
#    dkn.ChangeAnimation("Tkn_chg_l","Kgt_attack_chg_l")
#                         
#    dkn.ChangeAnimation("Tkn_attack_drink","Kgt_attack_drink")
#                         
#    dkn.ChangeAnimation("Tkn_hurt_f_lite","Kgt_hurt_f_lite")
#    dkn.ChangeAnimation("Tkn_hurt_f_big","Kgt_hurt_f_big")
#    dkn.ChangeAnimation("Tkn_hurt_f_head","Kgt_hurt_f_head") 
#    dkn.ChangeAnimation("Tkn_hurt_f_breast","Kgt_hurt_f_breast")
#    dkn.ChangeAnimation("Tkn_hurt_f_back","Kgt_hurt_f_back") 
#    dkn.ChangeAnimation("Tkn_hurt_f_r_arm","Kgt_hurt_f_r_arm") 
#    dkn.ChangeAnimation("Tkn_hurt_f_l_arm","Kgt_hurt_f_l_arm")
#    dkn.ChangeAnimation("Tkn_hurt_f_r_leg","Kgt_hurt_f_r_leg")
#    dkn.ChangeAnimation("Tkn_hurt_f_l_leg","Kgt_hurt_f_l_leg")
#    dkn.ChangeAnimation("Tkn_hurt_jog","Kgt_hurt_jog")  
#    dkn.ChangeAnimation("Tkn_hurt_head","Kgt_hurt_head") 
#    dkn.ChangeAnimation("Tkn_hurt_breast","Kgt_hurt_breast") 
#    dkn.ChangeAnimation("Tkn_hurt_back","Kgt_hurt_back") 
#    dkn.ChangeAnimation("Tkn_hurt_r_arm","Kgt_hurt_r_arm") 
#    dkn.ChangeAnimation("Tkn_hurt_l_arm","Kgt_hurt_l_arm") 
#    dkn.ChangeAnimation("Tkn_hurt_r_leg","Kgt_hurt_r_leg") 
#    dkn.ChangeAnimation("Tkn_hurt_l_leg","Kgt_hurt_l_leg")  
#    dkn.ChangeAnimation("Tkn_df_s_broken",   "Kgt_df_s_broken") 
#    dkn.ChangeAnimation("Tkn_sword_broken",   "Kgt_sword_broken") 
#                         
#                         
#    dkn.ChangeAnimation("Tkn_look_around",  "Tkn_patrol1")
#    dkn.ChangeAnimation("Tkn_insult",       "Rgn_insult")
#
#
#
#
#
#
#
#    Ldm=Bladex.GetCharType("Little_Demon","Ldm")
#    Ldm.ChangeAnimation("Ldm_attack_f_s","Ldm_rlx_s")
#    Ldm.ChangeAnimation("Ldm_attack_b_s","Ldm_rlx_s")
#
#    Ldm.ChangeAnimation("Ldm_hurt_f_head",  "Ldm_hurt_f_big") 
#    Ldm.ChangeAnimation("Ldm_hurt_f_breast","Ldm_hurt_f_lite") 
#    Ldm.ChangeAnimation("Ldm_hurt_f_back",  "Ldm_hurt_f_lite") 
#    Ldm.ChangeAnimation("Ldm_hurt_f_r_arm", "Ldm_hurt_f_lite") 
#    Ldm.ChangeAnimation("Ldm_hurt_f_l_arm", "Ldm_hurt_f_lite") 
#    Ldm.ChangeAnimation("Ldm_hurt_f_r_leg", "Ldm_hurt_f_lite") 
#    Ldm.ChangeAnimation("Ldm_hurt_f_l_leg", "Ldm_hurt_f_lite") 
#    Ldm.ChangeAnimation("Ldm_hurt_jog",     "Ldm_hurt_lite") 
#    Ldm.ChangeAnimation("Ldm_hurt_head",    "Ldm_hurt_big") 
#    Ldm.ChangeAnimation("Ldm_hurt_breast",  "Ldm_hurt_lite") 
#    Ldm.ChangeAnimation("Ldm_hurt_back",    "Ldm_hurt_lite") 
#    Ldm.ChangeAnimation("Ldm_hurt_r_arm",   "Ldm_hurt_lite") 
#    Ldm.ChangeAnimation("Ldm_hurt_l_arm",   "Ldm_hurt_lite") 
#    Ldm.ChangeAnimation("Ldm_hurt_r_leg",   "Ldm_hurt_lite") 
#    Ldm.ChangeAnimation("Ldm_hurt_l_leg",   "Ldm_hurt_lite") 
#
#    Gdm=Bladex.GetCharType("Great_Demon","Gdm")
#    Gdm.ChangeAnimation("Gdm_df_01",        "Gdm_hurt_big") 
#    Gdm.ChangeAnimation("Gdm_df_02",        "Gdm_hurt_big") 
#    Gdm.ChangeAnimation("Gdm_hurt_f_big",   "Gdm_hurt_big") 
#    Gdm.ChangeAnimation("Gdm_hurt_f_lite",  "Gdm_hurt_big") 
#    Gdm.ChangeAnimation("Gdm_hurt_lite",    "Gdm_hurt_big") 
#    Gdm.ChangeAnimation("Gdm_hurt_f_head",  "Gdm_hurt_big") 
#    Gdm.ChangeAnimation("Gdm_hurt_f_breast","Gdm_hurt_big") 
#    Gdm.ChangeAnimation("Gdm_hurt_f_back",  "Gdm_hurt_big") 
#    Gdm.ChangeAnimation("Gdm_hurt_f_r_arm", "Gdm_hurt_big") 
#    Gdm.ChangeAnimation("Gdm_hurt_f_l_arm", "Gdm_hurt_big") 
#    Gdm.ChangeAnimation("Gdm_hurt_f_r_leg", "Gdm_hurt_big") 
#    Gdm.ChangeAnimation("Gdm_hurt_f_l_leg", "Gdm_hurt_big") 
#    Gdm.ChangeAnimation("Gdm_hurt_jog",     "Gdm_hurt_big") 
#    Gdm.ChangeAnimation("Gdm_hurt_head",    "Gdm_hurt_big") 
#    Gdm.ChangeAnimation("Gdm_hurt_breast",  "Gdm_hurt_big") 
#    Gdm.ChangeAnimation("Gdm_hurt_back",    "Gdm_hurt_big") 
#    Gdm.ChangeAnimation("Gdm_hurt_r_arm",   "Gdm_hurt_big") 
#    Gdm.ChangeAnimation("Gdm_hurt_l_arm",   "Gdm_hurt_big") 
#    Gdm.ChangeAnimation("Gdm_hurt_r_leg",   "Gdm_hurt_big") 
#    Gdm.ChangeAnimation("Gdm_hurt_l_leg",   "Gdm_hurt_big") 
#
#    ork=Bladex.GetCharType("Ork","Ork")
#    ork.SetAnmDefaultPrefix("Ork")
#    # hurts
#    ork.ChangeAnimation("Ork_alarm01",      "Tkn_alarm01")
#    ork.ChangeAnimation("Ork_hurt_f_breast","Ork_hurt_f_back")
#    ork.ChangeAnimation("Ork_hurt_lite",    "Ork_hurt_f_lite")
#    ork.ChangeAnimation("Ork_hurt_big",     "Ork_hurt_f_big")
#    ork.ChangeAnimation("Ork_hurt_head",    "Ork_hurt_f_head")
#    ork.ChangeAnimation("Ork_hurt_breast",  "Ork_hurt_f_back")
#    ork.ChangeAnimation("Ork_hurt_back",    "Ork_hurt_f_back")
#    ork.ChangeAnimation("Ork_hurt_r_arm",   "Ork_hurt_f_r_arm")
#    ork.ChangeAnimation("Ork_hurt_l_arm",   "Ork_hurt_f_l_arm")
#    ork.ChangeAnimation("Ork_hurt_r_leg",   "Ork_hurt_f_r_leg")
#    ork.ChangeAnimation("Ork_hurt_l_leg",   "Ork_hurt_f_l_leg")
#    ork.ChangeAnimation("Ork_hurt_jog",     "Ork_hurt_f_back")
#    ork.ChangeAnimation("Ork_dth_rock",     "Kgt_dth_rock")
#    ork.ChangeAnimation("Ork_dth_rockfront","Kgt_dth_rockfront")
#    ork.ChangeAnimation("Ork_dth_n00","Kgt_dth_n00")
#    ork.ChangeAnimation("Ork_dth_n01","Kgt_dth_n01")
#    ork.ChangeAnimation("Ork_dth_n02","Kgt_dth_n02")
#    ork.ChangeAnimation("Ork_dth_n03","Kgt_dth_n03")
#    ork.ChangeAnimation("Ork_dth_n04","Kgt_dth_n04")
#    ork.ChangeAnimation("Ork_dth_n05","Kgt_dth_n05")
#    ork.ChangeAnimation("Ork_dth_n06","Kgt_dth_n06")
#    ork.ChangeAnimation("Ork_dth_c7","Kgt_dth_c1")
#    ork.ChangeAnimation("Ork_dth_c2","Kgt_dth_c2")
#    ork.ChangeAnimation("Ork_dth_c3","Kgt_dth_c3")
#    ork.ChangeAnimation("Ork_dth_c4","Kgt_dth_c4")
#    ork.ChangeAnimation("Ork_dth_c5","Kgt_dth_c5")
#    ork.ChangeAnimation("Ork_dth_c6","Kgt_dth_c6")
#    ork.ChangeAnimation("Ork_dth_burn","Kgt_dth_burn")
#
#    ork.ChangeAnimation("Ork_clmb_medium_1h","Kgt_clmb_medium_1h")
#    ork.ChangeAnimation("Ork_clmb_medlow_1h","Kgt_clmb_medlow_1h")
#    ork.ChangeAnimation("Ork_clmb_high_1h","Kgt_clmb_high_1h")
#    ork.ChangeAnimation("Ork_clmb_low_1h","Kgt_clmb_low_1h")
#
#    ork.ChangeAnimation("Ork_chg_r_l",	"Kgt_attack_chg_r_l")
#    ork.ChangeAnimation("Ork_attack_chg_r_l",	"Kgt_attack_chg_r_l")
#
#
    gok=Bladex.GetCharType("Great_Ork","Gok")
    gok.SetAnmDefaultPrefix("Ork")
#    # hurts
#    gok.ChangeAnimation("Ork_hurt_f_breast","Ork_hurt_f_back")
#    gok.ChangeAnimation("Ork_hurt_lite",    "Ork_hurt_f_lite")
#    gok.ChangeAnimation("Ork_hurt_big",     "Ork_hurt_f_big")
#    gok.ChangeAnimation("Ork_hurt_head",    "Ork_hurt_f_head")
#    gok.ChangeAnimation("Ork_hurt_breast",  "Ork_hurt_f_back")
#    gok.ChangeAnimation("Ork_hurt_back",    "Ork_hurt_f_back")
#    gok.ChangeAnimation("Ork_hurt_r_arm",   "Ork_hurt_f_r_arm")
#    gok.ChangeAnimation("Ork_hurt_l_arm",   "Ork_hurt_f_l_arm")
#    gok.ChangeAnimation("Ork_hurt_r_leg",   "Ork_hurt_f_r_leg")
#    gok.ChangeAnimation("Ork_hurt_l_leg",   "Ork_hurt_f_l_leg")
#    gok.ChangeAnimation("Ork_hurt_jog",     "Ork_hurt_f_back")
#    gok.ChangeAnimation("Ork_dth_rock",     "Kgt_dth_rock")
#    gok.ChangeAnimation("Ork_dth_rockfront","Kgt_dth_rockfront")
#    gok.ChangeAnimation("Ork_dth_n00","Kgt_dth_n00")
#    gok.ChangeAnimation("Ork_dth_n01","Kgt_dth_n01")
#    gok.ChangeAnimation("Ork_dth_n02","Kgt_dth_n02")
#    gok.ChangeAnimation("Ork_dth_n03","Kgt_dth_n03")
#    gok.ChangeAnimation("Ork_dth_n04","Kgt_dth_n04")
#    gok.ChangeAnimation("Ork_dth_n05","Kgt_dth_n05")
#    gok.ChangeAnimation("Ork_dth_n06","Kgt_dth_n06")
#    gok.ChangeAnimation("Ork_dth_c7","Kgt_dth_c1")
#    gok.ChangeAnimation("Ork_dth_c2","Kgt_dth_c2")
#    gok.ChangeAnimation("Ork_dth_c3","Kgt_dth_c3")
#    gok.ChangeAnimation("Ork_dth_c4","Kgt_dth_c4")
#    gok.ChangeAnimation("Ork_dth_c5","Kgt_dth_c5")
#    gok.ChangeAnimation("Ork_dth_c6","Kgt_dth_c6")
#    gok.ChangeAnimation("Ork_dth_burn","Kgt_dth_burn")
#    gok.ChangeAnimation("Ork_chg_r_l",	"Kgt_attack_chg_r_l")
#    gok.ChangeAnimation("Ork_attack_chg_r_l","Kgt_attack_chg_r_l")
#    # misc
#    gok.ChangeAnimation("Ork_alarm01",      "Tkn_alarm01")
#
    dok=Bladex.GetCharType("Dark_Ork","Dok")
    dok.SetAnmDefaultPrefix("Ork")
#    # hurts
#    dok.ChangeAnimation("Ork_hurt_f_breast","Ork_hurt_f_back")
#    dok.ChangeAnimation("Ork_hurt_lite",    "Ork_hurt_f_lite")
#    dok.ChangeAnimation("Ork_hurt_big",     "Ork_hurt_f_big")
#    dok.ChangeAnimation("Ork_hurt_head",    "Ork_hurt_f_head")
#    dok.ChangeAnimation("Ork_hurt_breast",  "Ork_hurt_f_back")
#    dok.ChangeAnimation("Ork_hurt_back",    "Ork_hurt_f_back")
#    dok.ChangeAnimation("Ork_hurt_r_arm",   "Ork_hurt_f_r_arm")
#    dok.ChangeAnimation("Ork_hurt_l_arm",   "Ork_hurt_f_l_arm")
#    dok.ChangeAnimation("Ork_hurt_r_leg",   "Ork_hurt_f_r_leg")
#    dok.ChangeAnimation("Ork_hurt_l_leg",   "Ork_hurt_f_l_leg")
#    dok.ChangeAnimation("Ork_hurt_jog",     "Ork_hurt_f_back")
#    dok.ChangeAnimation("Ork_dth_rock",     "Kgt_dth_rock")
#    dok.ChangeAnimation("Ork_dth_rockfront","Kgt_dth_rockfront")
#    dok.ChangeAnimation("Ork_dth_n00","Kgt_dth_n00")
#    dok.ChangeAnimation("Ork_dth_n01","Kgt_dth_n01")
#    dok.ChangeAnimation("Ork_dth_n02","Kgt_dth_n02")
#    dok.ChangeAnimation("Ork_dth_n03","Kgt_dth_n03")
#    dok.ChangeAnimation("Ork_dth_n04","Kgt_dth_n04")
#    dok.ChangeAnimation("Ork_dth_n05","Kgt_dth_n05")
#    dok.ChangeAnimation("Ork_dth_n06","Kgt_dth_n06")
#    dok.ChangeAnimation("Ork_dth_c7","Kgt_dth_c1")
#    dok.ChangeAnimation("Ork_dth_c2","Kgt_dth_c2")
#    dok.ChangeAnimation("Ork_dth_c3","Kgt_dth_c3")
#    dok.ChangeAnimation("Ork_dth_c4","Kgt_dth_c4")
#    dok.ChangeAnimation("Ork_dth_c5","Kgt_dth_c5")
#    dok.ChangeAnimation("Ork_dth_c6","Kgt_dth_c6")
#    dok.ChangeAnimation("Ork_chg_r_l",	"Kgt_attack_chg_r_l")
#    dok.ChangeAnimation("Ork_attack_chg_r_l","Kgt_attack_chg_r_l")
#    # misc
#    dok.ChangeAnimation("Ork_alarm01",      "Tkn_alarm01")
#
#
    org=Bladex.GetCharType("Gold_Ork","Org")
    org.SetAnmDefaultPrefix("Ork")
#    # hurts
#    org.ChangeAnimation("Ork_hurt_f_breast","Ork_hurt_f_back")
#    org.ChangeAnimation("Ork_hurt_lite",    "Ork_hurt_f_lite")
#    org.ChangeAnimation("Ork_hurt_big",     "Ork_hurt_f_big")
#    org.ChangeAnimation("Ork_hurt_head",    "Ork_hurt_f_head")
#    org.ChangeAnimation("Ork_hurt_breast",  "Ork_hurt_f_back")
#    org.ChangeAnimation("Ork_hurt_back",    "Ork_hurt_f_back")
#    org.ChangeAnimation("Ork_hurt_r_arm",   "Ork_hurt_f_r_arm")
#    org.ChangeAnimation("Ork_hurt_l_arm",   "Ork_hurt_f_l_arm")
#    org.ChangeAnimation("Ork_hurt_r_leg",   "Ork_hurt_f_r_leg")
#    org.ChangeAnimation("Ork_hurt_l_leg",   "Ork_hurt_f_l_leg")
#    org.ChangeAnimation("Ork_hurt_jog",     "Ork_hurt_f_back")
#    org.ChangeAnimation("Ork_dth_rock",     "Kgt_dth_rock")
#    org.ChangeAnimation("Ork_dth_rockfront","Kgt_dth_rockfront")
#    org.ChangeAnimation("Ork_dth_n00","Kgt_dth_n00")
#    org.ChangeAnimation("Ork_dth_n01","Kgt_dth_n01")
#    org.ChangeAnimation("Ork_dth_n02","Kgt_dth_n02")
#    org.ChangeAnimation("Ork_dth_n03","Kgt_dth_n03")
#    org.ChangeAnimation("Ork_dth_n04","Kgt_dth_n04")
#    org.ChangeAnimation("Ork_dth_n05","Kgt_dth_n05")
#    org.ChangeAnimation("Ork_dth_n06","Kgt_dth_n06")
#    org.ChangeAnimation("Ork_dth_c7","Kgt_dth_c1")
#    org.ChangeAnimation("Ork_dth_c2","Kgt_dth_c2")
#    org.ChangeAnimation("Ork_dth_c3","Kgt_dth_c3")
#    org.ChangeAnimation("Ork_dth_c4","Kgt_dth_c4")
#    org.ChangeAnimation("Ork_dth_c5","Kgt_dth_c5")
#    org.ChangeAnimation("Ork_dth_c6","Kgt_dth_c6")
#    org.ChangeAnimation("Ork_chg_r_l",	"Kgt_attack_chg_r_l")
#    org.ChangeAnimation("Ork_attack_chg_r_l","Kgt_attack_chg_r_l")
#    # misc
#    org.ChangeAnimation("Ork_alarm01",      "Tkn_alarm01")
#
#
#    #ork.ChangeAnimation("Kgt_dth_sleep","Tkn_dth_sleep")
#    #ork.ChangeAnimation("Kgt_sleep_wall","Tkn_sleep_wall")
#    #ork.ChangeAnimation("Kgt_sleep_wall_d","Tkn_sleep_wall_d")
#    #ork.ChangeAnimation("Kgt_dth_sleep_wall","Tkn_dth_sleep_wall")
#    #ork.ChangeAnimation("Kgt_speak01","Tkn_speak01")
#    #ork.ChangeAnimation("Kgt_speak02","Tkn_speak02")
#    #ork.ChangeAnimation("Kgt_alarm01","Tkn_alarm01")
#    #ork.ChangeAnimation("Kgt_alarm02","Tkn_alarm02")
#    #ork.ChangeAnimation("Kgt_walk_t","Tkn_walk_t")
#
#
#
#    skl=Bladex.GetCharType("Skeleton","Skl") 
#    skl.SetAnmDefaultPrefix("Skl")
#     
#    skl.ChangeAnimation("skl_attack_chg_r_l",	"Kgt_attack_chg_r_l")
#    skl.ChangeAnimation("skl_chg_r_l",	"Kgt_attack_chg_r_l") 
#    # misc
#    skl.ChangeAnimation("Skl_look_around",  "Skl_patrol1")
#    skl.ChangeAnimation("Skl_alarm01",      "Tkn_alarm01")
#    skl.ChangeAnimation("Skl_alarm02",      "Tkn_alarm02")
#    skl.ChangeAnimation("Skl_dth_c7","Ork_dth_c1")
#    skl.ChangeAnimation("Skl_dth_fll","Kgt_dth_fll")
#    skl.ChangeAnimation("Skl_dth_fll2","Kgt_dth_fll2")
#    skl.ChangeAnimation("Skl_dth_c1","Kgt_dth_c1")
#    skl.ChangeAnimation("Skl_dth_c2","Kgt_dth_c2")
#    skl.ChangeAnimation("Skl_dth_c3","Kgt_dth_c3")
#    skl.ChangeAnimation("Skl_dth_c4","Kgt_dth_c4")
#    skl.ChangeAnimation("Skl_dth_c5","Kgt_dth_c5")
#    skl.ChangeAnimation("Skl_dth_c6","Kgt_dth_c6")
#    skl.ChangeAnimation("Skl_dth_c7","Ork_dth_c1")
#    skl.ChangeAnimation("Skl_dth_burn","Kgt_dth_burn")
#    #skl.ChangeAnimation("Skl_dth_n01","Kgt_dth_n01")
#    skl.ChangeAnimation("Skl_dth_n02","Kgt_dth_n02")
#    skl.ChangeAnimation("Skl_dth_n03","Kgt_dth_n03")
#    skl.ChangeAnimation("Skl_dth_n04","Kgt_dth_n04")
#    skl.ChangeAnimation("Skl_dth_n05","Kgt_dth_n05")
#    skl.ChangeAnimation("Skl_dth_n06","Kgt_dth_n06")
#    skl.ChangeAnimation("Skl_dth_rock","Kgt_dth_rock")
#    skl.ChangeAnimation("Skl_dth_rockfront","Kgt_dth_rockfront")
#    skl.ChangeAnimation("Skl_dth0","Kgt_dth0") 
#    skl.ChangeAnimation("Skl_df_s_broken","Kgt_df_s_broken") 
#    # hurts
#    #skl.ChangeAnimation("Kgt_df_01",        "Skl_df_01") 
#    #skl.ChangeAnimation("Kgt_df_02",        "Skl_df_02") 
#    #skl.ChangeAnimation("Kgt_hurt_f_lite",  "Skl_hurt_f_lite") 
#    #skl.ChangeAnimation("Kgt_hurt_f_big",   "Skl_hurt_f_big") 
#    #skl.ChangeAnimation("Kgt_hurt_f_head",  "Skl_hurt_f_head") 
#    #skl.ChangeAnimation("Kgt_hurt_f_breast","Skl_hurt_f_breast") 
#    #skl.ChangeAnimation("Kgt_hurt_f_back",  "Skl_hurt_f_back") 
#    #skl.ChangeAnimation("Kgt_hurt_f_r_arm", "Skl_hurt_f_r_arm") 
#    #skl.ChangeAnimation("Kgt_hurt_f_l_arm", "Skl_hurt_f_l_arm") 
#    #skl.ChangeAnimation("Kgt_hurt_f_r_leg", "Skl_hurt_f_r_leg") 
#    #skl.ChangeAnimation("Kgt_hurt_f_l_leg", "Skl_hurt_f_l_leg") 
#    skl.ChangeAnimation("Skl_hurt_jog",     "Skl_hurt_back") 
#    skl.ChangeAnimation("Skl_hurt_head",    "Skl_hurt_f_head") 
#    skl.ChangeAnimation("Skl_hurt_breast",  "Skl_hurt_f_breast") 
#    skl.ChangeAnimation("Skl_hurt_f_back",    "Skl_hurt_back") 
#    skl.ChangeAnimation("Skl_hurt_r_arm",   "Skl_hurt_f_r_arm") 
#    skl.ChangeAnimation("Skl_hurt_l_arm",   "Skl_hurt_f_l_arm") 
#    skl.ChangeAnimation("Skl_hurt_r_leg",   "Skl_hurt_f_r_leg") 
#    skl.ChangeAnimation("Skl_hurt_l_leg",   "Skl_hurt_f_l_leg")
#    #skl.ChangeAnimation("Kgt_chg_r_l",	"Kgt_attack_chg_r_l")
#
#
#
#
#
#
#    Chk=Bladex.GetCharType("ChaosKnight","Chk")
#    Chk.SetAnmDefaultPrefix("Chk")
#
#
#    Chk.ChangeAnimation("Chk_df_01",        "Chk_hurt_hip")
#    Chk.ChangeAnimation("Chk_df_02",        "Chk_hurt01")
#    Chk.ChangeAnimation("Chk_hurt_f_lite",  "Chk_hurt_hip")
#    Chk.ChangeAnimation("Chk_hurt_f_breast","Chk_hurt_hip")
#    Chk.ChangeAnimation("Chk_hurt_f_back",  "Chk_hurt_hip")
#    Chk.ChangeAnimation("Chk_hurt_f_r_arm", "Chk_hurt_hip")
#    Chk.ChangeAnimation("Chk_hurt_f_l_arm", "Chk_hurt_hip")
#    Chk.ChangeAnimation("Chk_hurt_f_r_leg", "Chk_hurt_hip")
#    Chk.ChangeAnimation("Chk_hurt_f_l_leg", "Chk_hurt_hip")
#    Chk.ChangeAnimation("Chk_hurt_jog",     "Chk_hurt_hip")
#    Chk.ChangeAnimation("Chk_hurt_head",    "Chk_hurt_hip")  
#    Chk.ChangeAnimation("Chk_hurt_breast",  "Chk_hurt_hip")  
#    Chk.ChangeAnimation("Chk_hurt_back",    "Chk_hurt_hip")  
#    Chk.ChangeAnimation("Chk_hurt_r_arm",   "Chk_hurt_hip") 
#    Chk.ChangeAnimation("Chk_hurt_l_arm",   "Chk_hurt_hip") 
#    Chk.ChangeAnimation("Chk_hurt_r_leg",   "Chk_hurt_hip") 
#    Chk.ChangeAnimation("Chk_hurt_l_leg",   "Chk_hurt_hip") 
#    Chk.ChangeAnimation("Chk_hurt_lite",   	"Chk_hurt_hip") 
#    Chk.ChangeAnimation("Chk_hurt_big",   	"Chk_hurt01") 
#    Chk.ChangeAnimation("Chk_hurt_f_lite",  "Chk_hurt_hip")
#    Chk.ChangeAnimation("Chk_hurt_f_big",   "Chk_hurt01") 
#    Chk.ChangeAnimation("Chk_dth0",   "Chk_dth_0")
#     
#
#
    rgn=Bladex.GetCharType("Ragnar","Rgn")
    rgn.SetAnmDefaultPrefix("Kgt")
#
#    rgn.ChangeAnimation("Kgt_end_ragnar",   "Rgn_end_ragnar")
#    rgn.ChangeAnimation("Kgt_g_escape",     "Rgn_g_escape")
#    rgn.ChangeAnimation("Kgt_g_d_l",        "Rgn_g_d_l")
#    rgn.ChangeAnimation("Kgt_g_d_r",        "Rgn_g_d_r")
#    rgn.ChangeAnimation("Kgt_laugh",        "Rgn_laugh")
#    rgn.ChangeAnimation("Kgt_insult",       "Rgn_insult")
#    rgn.ChangeAnimation("Kgt_attack_drink", "Rgn_attack_drink")
#    rgn.ChangeAnimation("Kgt_scape",        "Rgn_scape")
#    rgn.ChangeAnimation("Kgt_escape2",      "Rgn_escape2")
#    rgn.ChangeAnimation("Kgt_dth",          "Rgn_death")
#
#    #rgn=Bladex.GetCharType("Ragnar","Rgn")
#    #rgn.SetAnmDefaultPrefix("Rgn")
#    #
#    #
#    #rgn.ChangeAnimation("Rgn_dth_fll","Kgt_dth_fll")
#    #rgn.ChangeAnimation("Rgn_dth_fll2","Kgt_dth_fll2")
#    #rgn.ChangeAnimation("Rgn_dth_c1","Kgt_dth_c1")
#    #rgn.ChangeAnimation("Rgn_dth_c2","Kgt_dth_c2")
#    #rgn.ChangeAnimation("Rgn_dth_c3","Kgt_dth_c3")
#    #rgn.ChangeAnimation("Rgn_dth_c4","Kgt_dth_c4")
#    #rgn.ChangeAnimation("Rgn_dth_c5","Kgt_dth_c5")
#    #rgn.ChangeAnimation("Rgn_dth_c6","Kgt_dth_c6")
#    #rgn.ChangeAnimation("Rgn_dth_c7","Ork_dth_c1")
#    #rgn.ChangeAnimation("Rgn_dth_burn","Kgt_dth_burn")
#    #rgn.ChangeAnimation("Rgn_dth_n01","Kgt_dth_n01")
#    #rgn.ChangeAnimation("Rgn_dth_n02","Kgt_dth_n02")
#    #rgn.ChangeAnimation("Rgn_dth_n03","Kgt_dth_n03")
#    #rgn.ChangeAnimation("Rgn_dth_n04","Kgt_dth_n04")
#    #rgn.ChangeAnimation("Rgn_dth_n05","Kgt_dth_n05")
#    #rgn.ChangeAnimation("Rgn_dth_n06","Kgt_dth_n06")
#    #rgn.ChangeAnimation("Rgn_dth_rock","Kgt_dth_rock")
#    #rgn.ChangeAnimation("Rgn_dth_rockfront","Kgt_dth_rockfront")
#    #rgn.ChangeAnimation("Rgn_dth0","Kgt_dth0")
#    #
#    #rgn.ChangeAnimation("Rgn_attack_chg_r_l","Kgt_attack_chg_r_l")
#    #rgn.ChangeAnimation("Rgn_attack_chg_r","Kgt_attack_chg_r")
#    #rgn.ChangeAnimation("Rgn_attack_chg_l","Kgt_attack_chg_l")
#    #rgn.ChangeAnimation("Rgn_chg_r_l","Kgt_attack_chg_r_l")
#    #rgn.ChangeAnimation("Rgn_chg_r","Kgt_attack_chg_r")
#    #rgn.ChangeAnimation("Rgn_chg_l","Kgt_attack_chg_l")
#    #
#    #rgn.ChangeAnimation("Rgn_attack_drink","Kgt_attack_drink")
#    #
#    #rgn.ChangeAnimation("Rgn_hurt_f_lite","Kgt_hurt_f_lite")
#    #rgn.ChangeAnimation("Rgn_hurt_f_big","Kgt_hurt_f_big")
#    #rgn.ChangeAnimation("Rgn_hurt_f_head","Kgt_hurt_f_head") 
#    #rgn.ChangeAnimation("Rgn_hurt_f_breast","Kgt_hurt_f_breast")
#    #rgn.ChangeAnimation("Rgn_hurt_f_back","Kgt_hurt_f_back") 
#    #rgn.ChangeAnimation("Rgn_hurt_f_r_arm","Kgt_hurt_f_r_arm") 
#    #rgn.ChangeAnimation("Rgn_hurt_f_l_arm","Kgt_hurt_f_l_arm")
#    #rgn.ChangeAnimation("Rgn_hurt_f_r_leg","Kgt_hurt_f_r_leg")
#    #rgn.ChangeAnimation("Rgn_hurt_f_l_leg","Kgt_hurt_f_l_leg")
#    #rgn.ChangeAnimation("Rgn_hurt_jog","Kgt_hurt_jog")  
#    #rgn.ChangeAnimation("Rgn_hurt_head","Kgt_hurt_head") 
#    #rgn.ChangeAnimation("Rgn_hurt_breast","Kgt_hurt_breast") 
#    #rgn.ChangeAnimation("Rgn_hurt_back","Kgt_hurt_back") 
#    #rgn.ChangeAnimation("Rgn_hurt_r_arm","Kgt_hurt_r_arm") 
#    #rgn.ChangeAnimation("Rgn_hurt_l_arm","Kgt_hurt_l_arm") 
#    #rgn.ChangeAnimation("Rgn_hurt_r_leg","Kgt_hurt_r_leg") 
#    #rgn.ChangeAnimation("Rgn_hurt_l_leg","Kgt_hurt_l_leg")  
#    #rgn.ChangeAnimation("Rgn_df_s_broken",   "Kgt_df_s_broken") 
#    #rgn.ChangeAnimation("Rgn_sword_broken",   "Kgt_sword_broken") 
#    #                     
#    #rgn.ChangeAnimation("Rgn_look_around",  "Tkn_patrol1")
#
#
#
#    Bar=Bladex.GetCharType("Barbarian_N","Bar")
#    Bar.SetAnmDefaultPrefix("Bar")
#
#
#    Bar.ChangeAnimation("Bar_dth_c1","Kgt_dth_c1")
#    Bar.ChangeAnimation("Bar_dth_c2","Kgt_dth_c2")
#    Bar.ChangeAnimation("Bar_dth_c3","Kgt_dth_c3")
#    Bar.ChangeAnimation("Bar_dth_c4","Kgt_dth_c4")
#    Bar.ChangeAnimation("Bar_dth_c5","Kgt_dth_c5")
#    Bar.ChangeAnimation("Bar_dth_c6","Kgt_dth_c6")
#    Bar.ChangeAnimation("Bar_dth_c7","Ork_dth_c1")
#    Bar.ChangeAnimation("Bar_dth_n00","Kgt_dth_n00")
#    Bar.ChangeAnimation("Bar_dth_n01","Kgt_dth_n01")
#    Bar.ChangeAnimation("Bar_dth_n02","Kgt_dth_n02")
#    Bar.ChangeAnimation("Bar_dth_n03","Kgt_dth_n03")
#    Bar.ChangeAnimation("Bar_dth_n04","Kgt_dth_n04")
#    Bar.ChangeAnimation("Bar_dth_n05","Kgt_dth_n05")
#    Bar.ChangeAnimation("Bar_dth_n06","Kgt_dth_n06")
#    Bar.ChangeAnimation("Bar_dth_rock","Kgt_dth_rock")
#    Bar.ChangeAnimation("Bar_dth_rockfront","Kgt_dth_rockfront")
#    Bar.ChangeAnimation("Bar_dth_dth0","Kgt_dth_dth0")
#    Bar.ChangeAnimation("Bar_dth_burn","Kgt_dth_burn")
#    Bar.ChangeAnimation("Bar_tke_r_key04","Bar_tke_r_key05")
#    #Bar.ChangeAnimation("Bar_1tw_l_f","Kgt_1tw_l_f")
#    #Bar.ChangeAnimation("Bar_1tw_l","Kgt_1tw_l")
#    #Bar.ChangeAnimation("Bar_1tw_h_f","Kgt_1tw_h_f")
#    #Bar.ChangeAnimation("Bar_1tw_h","Bar_1tw_h_f")
#    Bar.ChangeAnimation("Bar_eat00","Kgt_eat00")
#    Bar.ChangeAnimation("Bar_attack_drink","Kgt_attack_drink")
#    Bar.ChangeAnimation("Bar_pulsador","Kgt_pulsador")
#    Bar.ChangeAnimation("Bar_chg_r","Bar_attack_chg_r")
#    Bar.ChangeAnimation("Bar_chg_l","Bar_attack_chg_l")
#    Bar.ChangeAnimation("Bar_chg_r_l","Bar_attack_chg_r_l")
#
#
#
#    amz=Bladex.GetCharType("Amazon_N","Amz_N")
#    amz.SetAnmDefaultPrefix("Amz")
#
#    amz.ChangeAnimation("Amz_drp_l","Kgt_drp_l")
#
#     
#    #amz.ChangeAnimation("Amz_hurt_head","Kgt_hurt_f_head") 
#    #amz.ChangeAnimation("Amz_hurt_breast","Kgt_hurt_f_breast") 
#    #amz.ChangeAnimation("Amz_hurt_back","Kgt_hurt_f_back") 
#    #amz.ChangeAnimation("Amz_hurt_r_arm","Kgt_hurt_f_r_arm") 
#    #amz.ChangeAnimation("Amz_hurt_l_arm","Kgt_hurt_f_l_arm") 
#    #amz.ChangeAnimation("Amz_hurt_r_leg","Kgt_hurt_f_r_leg") 
#    #amz.ChangeAnimation("Amz_hurt_l_leg","Kgt_hurt_f_l_leg") 
#    #amz.ChangeAnimation("Amz_hurt_lite","Kgt_hurt_f_lite") 
#    #amz.ChangeAnimation("Amz_hurt_big","Kgt_hurt_f_big") 
#
#
#    amz.ChangeAnimation("Amz_attack_drink", "Kgt_attack_drink")
#    #amz.ChangeAnimation("Amz_drink", "Kgt_drink")
#    amz.ChangeAnimation("Amz_dth_fll","Kgt_dth_fll")
#    amz.ChangeAnimation("Amz_dth_fll2","Kgt_dth_fll2")
#    amz.ChangeAnimation("Amz_dth_c1","Kgt_dth_c1")
#    amz.ChangeAnimation("Amz_dth_c2","Kgt_dth_c2")
#    amz.ChangeAnimation("Amz_dth_c3","Kgt_dth_c3")
#    amz.ChangeAnimation("Amz_dth_c4","Kgt_dth_c4")
#    amz.ChangeAnimation("Amz_dth_c5","Kgt_dth_c5")
#    amz.ChangeAnimation("Amz_dth_c6","Kgt_dth_c6")
#    amz.ChangeAnimation("Amz_dth_c7","Ork_dth_c1")
#    amz.ChangeAnimation("Amz_dth_burn","Kgt_dth_burn")
#    amz.ChangeAnimation("Amz_dth_n01","Kgt_dth_n00")
#    amz.ChangeAnimation("Amz_dth_n01","Kgt_dth_n01")
#    amz.ChangeAnimation("Amz_dth_n02","Kgt_dth_n02")
#    amz.ChangeAnimation("Amz_dth_n03","Kgt_dth_n03")
#    amz.ChangeAnimation("Amz_dth_n04","Kgt_dth_n04")
#    amz.ChangeAnimation("Amz_dth_n05","Kgt_dth_n05")
#    amz.ChangeAnimation("Amz_dth_n06","Kgt_dth_n06")
#    amz.ChangeAnimation("Amz_dth_rock","Kgt_dth_rock")
#    amz.ChangeAnimation("Amz_dth_rockfront","Kgt_dth_rockfront")
#    amz.ChangeAnimation("Amz_dth0","Kgt_dth0")
#
#    amz.ChangeAnimation("Amz_tke_r_01","Kgt_tke_r_01")
#    amz.ChangeAnimation("Amz_tke_r_02","Kgt_tke_r_02")
#    amz.ChangeAnimation("Amz_tke_r_03","Kgt_tke_r_03")
#    amz.ChangeAnimation("Amz_tke_r_04","Kgt_tke_r_04")
#    amz.ChangeAnimation("Amz_tke_r_05","Kgt_tke_r_05")
#
#    amz.ChangeAnimation("Amz_tke_r_key04","Kgt_tke_r_key04")
#    amz.ChangeAnimation("Amz_tke_r_key01","Kgt_tke_r_key01")
#    amz.ChangeAnimation("Amz_tke_r_key02","Kgt_tke_r_key02")
#    amz.ChangeAnimation("Amz_tke_r_key03","Kgt_tke_r_key03")
#    amz.ChangeAnimation("Amz_tke_r_key05","Kgt_tke_r_key05")
#    amz.ChangeAnimation("Amz_tke_r_key00","Kgt_tke_r_key00")
#
#    amz.ChangeAnimation("Amz_attack_chg_r_l","Kgt_attack_chg_r_l")
#    amz.ChangeAnimation("Amz_attack_chg_r","Kgt_attack_chg_r")
#    amz.ChangeAnimation("Amz_chg_r_l","Kgt_attack_chg_r_l")
#    amz.ChangeAnimation("Amz_chg_r","Kgt_attack_chg_r")
#    amz.ChangeAnimation("Amz_chg_l","Amz_attack_chg_l")
#
#    amz.ChangeAnimation("Amz_drink","Kgt_drink")
#    amz.ChangeAnimation("Amz_attack_drink","Kgt_attack_drink")
#    amz.ChangeAnimation("Amz_eat00","Kgt_eat00")
#    amz.ChangeAnimation("Amz_gulp00", "Kgt_gulp") 
#    amz.ChangeAnimation("Amz_key","Kgt_key")
#    amz.ChangeAnimation("Amz_lvr_u", "Kgt_lvr_u")
#    amz.ChangeAnimation("Amz_lvr_d", "Kgt_lvr_d")
#    amz.ChangeAnimation("Amz_pulsador", "Kgt_pulsador")
#
#    amz.ChangeAnimation("Amz_fire0","Kgt_fire0")
#    amz.ChangeAnimation("Amz_fire1","Kgt_fire1")
#    amz.ChangeAnimation("Amz_fire2","Kgt_fire2")
#    amz.ChangeAnimation("Amz_fire3","Kgt_fire3")
#    amz.ChangeAnimation("Amz_fire_g","Kgt_fire_g")
#
#    amz.ChangeAnimation("Amz_df_s_broken","Kgt_df_s_broken")
#    amz.ChangeAnimation("Amz_sword_broken","Kgt_sword_broken") 
#
#
#    #amz.ChangeAnimation("Amz_1tw_h","Amz_1tw_h_f")
#    #amz.ChangeAnimation("Amz_1tw_l","Kgt_1tw_l_f")
#    #amz.ChangeAnimation("Amz_1tw_l_f","Kgt_1tw_l_f")
#
#
#
#
#
#
#
#    Dwf=Bladex.GetCharType("Dwarf_N","Dwf")
#    Dwf.SetAnmDefaultPrefix("Dwf")
#
#    Dwf.ChangeAnimation("Dwf_act01","Bar_act01")
#    Dwf.ChangeAnimation("Dwf_r_f","Bar_r_f")
#    Dwf.ChangeAnimation("Dwf_dth_c2","Kgt_dth_c2")
#    Dwf.ChangeAnimation("Dwf_dth_c3","Kgt_dth_c3")
#    Dwf.ChangeAnimation("Dwf_dth_c4","Kgt_dth_c4")
#    Dwf.ChangeAnimation("Dwf_dth_c5","Kgt_dth_c5")
#    Dwf.ChangeAnimation("Dwf_dth_c6","Kgt_dth_c6")
#    Dwf.ChangeAnimation("Dwf_dth_c7","Ork_dth_c1")
#    Dwf.ChangeAnimation("Dwf_dth_n04","Kgt_dth_n04")
#    Dwf.ChangeAnimation("Dwf_dth_n05","Kgt_dth_n05")
#    Dwf.ChangeAnimation("Dwf_dth_n06","Kgt_dth_n06")
#    Dwf.ChangeAnimation("Dwf_dth_burn","Kgt_dth_burn")
#    Dwf.ChangeAnimation("Dwf_dth_rock","Kgt_dth_rock")
#    Dwf.ChangeAnimation("Dwf_dth_rockfront","Kgt_dth_rockfront")
#    Dwf.ChangeAnimation("Dwf_dth0","Kgt_dth0")
#    #Dwf.ChangeAnimation("Dwf_1tw_h_f","Kgt_1tw_h_f")
#    Dwf.ChangeAnimation("Dwf_attack_drink","Kgt_attack_drink")
#
#
#
#    Cos=Bladex.GetCharType("Cos","Cos")
#    Cos.ChangeAnimation("Cos_clmb_low_1h","Cos_clmb_low_no")
#    Cos.ChangeAnimation("Cos_clmb_medlow_1h","Cos_clmb_medlow_no")
#    Cos.ChangeAnimation("Cos_clmb_medium_1h","Cos_clmb_medium_no")
#    Cos.ChangeAnimation("Cos_clmb_high_1h","Cos_clmb_high_no")
#    Cos.ChangeAnimation("Cos_alarm01","Cos_alarm")
#
#    Spd=Bladex.GetCharType("Spidersmall","Spd")
#    Spd.ChangeAnimation("Spd_clmb_low_1h","Spd_clmb_low_no")
#    Spd.ChangeAnimation("Spd_clmb_medlow_1h","Spd_clmb_medlow_no")
#    Spd.ChangeAnimation("Spd_clmb_medium_1h","Spd_clmb_medium_no")
#    Spd.ChangeAnimation("Spd_clmb_high_1h","Spd_clmb_high_no")
#    Spd.ChangeAnimation("Spd_jmp0_no","Spd_jmp0_1h")
#    Spd.ChangeAnimation("Spd_jmp1_no","Spd_jmp1_1h")
#    Spd.ChangeAnimation("Spd_jmp2_no","Spd_jmp2_1h")
#    Spd.ChangeAnimation("Spd_jmp3_no","Spd_jmp3_1h")
#    Spd.ChangeAnimation("Spd_jmp4_no","Spd_jmp4_1h")
#    Spd.ChangeAnimation("Spd_rlx_1h","Spd_rlx_no")
#    Spd.ChangeAnimation("Spd_jog_1h","Spd_jog_no")
#    Spd.ChangeAnimation("Spd_wbk_1h","Spd_wbk_no")
#
#
#
#
#
#
#
#
    Zkn=Bladex.GetCharType("Knight_Zombie","Zkn")
    Zkn.SetAnmDefaultPrefix("Lch")
#
#    # hurts
#    Zkn.ChangeAnimation("Lch_df_01",        "Lch_hurt_f_lite") 
#    Zkn.ChangeAnimation("Lch_df_02",        "Lch_hurt_big2") 
#    Zkn.ChangeAnimation("Lch_hurt_f_lite",  "Lch_hurt_f_lite") 
#    Zkn.ChangeAnimation("Lch_hurt_f_big",   "Lch_hurt_f_big") 
#    Zkn.ChangeAnimation("Lch_hurt_f_head",  "Lch_hurt_f_big") 
#    Zkn.ChangeAnimation("Lch_hurt_f_breast","Lch_hurt_f_lite") 
#    Zkn.ChangeAnimation("Lch_hurt_f_back",  "Lch_hurt_f_lite") 
#    Zkn.ChangeAnimation("Lch_hurt_f_r_arm", "Lch_hurt_f_lite") 
#    Zkn.ChangeAnimation("Lch_hurt_f_l_arm", "Lch_hurt_f_lite") 
#    Zkn.ChangeAnimation("Lch_hurt_f_r_leg", "Lch_hurt_f_lite") 
#    Zkn.ChangeAnimation("Lch_hurt_f_l_leg", "Lch_hurt_f_lite") 
#    Zkn.ChangeAnimation("Lch_hurt_jog",     "Lch_hurt_big2") 
#    Zkn.ChangeAnimation("Lch_hurt_head",    "Lch_hurt_big") 
#    Zkn.ChangeAnimation("Lch_hurt_breast",  "Lch_hurt_big") 
#    Zkn.ChangeAnimation("Lch_hurt_back",    "Lch_hurt_big") 
#    Zkn.ChangeAnimation("Lch_hurt_r_arm",   "Lch_hurt_lite") 
#    Zkn.ChangeAnimation("Lch_hurt_l_arm",   "Lch_hurt_lite") 
#    Zkn.ChangeAnimation("Lch_hurt_r_leg",   "Lch_hurt_lite") 
#    Zkn.ChangeAnimation("Lch_hurt_l_leg",   "Lch_hurt_lite") 
#
#    # deaths 
#
#    Zkn.ChangeAnimation("Lch_dth_fll","Kgt_dth_fll")
#    Zkn.ChangeAnimation("Lch_dth_fll2","Kgt_dth_fll2")
#    Zkn.ChangeAnimation("Lch_dth_c1","Kgt_dth_c1")
#    Zkn.ChangeAnimation("Lch_dth_c2","Kgt_dth_c2")
#    Zkn.ChangeAnimation("Lch_dth_c3","Kgt_dth_c3")
#    Zkn.ChangeAnimation("Lch_dth_c4","Kgt_dth_c4")
#    Zkn.ChangeAnimation("Lch_dth_c5","Kgt_dth_c5")
#    Zkn.ChangeAnimation("Lch_dth_c6","Kgt_dth_c6")
#    Zkn.ChangeAnimation("Lch_dth_c7","Ork_dth_c1")
#    Zkn.ChangeAnimation("Lch_dth_burn","Kgt_dth_burn")
#    Zkn.ChangeAnimation("Lch_dth_n01","Kgt_dth_n01")
#    Zkn.ChangeAnimation("Lch_dth_n02","Kgt_dth_n02")
#    Zkn.ChangeAnimation("Lch_dth_n03","Kgt_dth_n03")
#    Zkn.ChangeAnimation("Lch_dth_n04","Kgt_dth_n04")
#    Zkn.ChangeAnimation("Lch_dth_n05","Kgt_dth_n05")
#    Zkn.ChangeAnimation("Lch_dth_n06","Kgt_dth_n06")
#    Zkn.ChangeAnimation("Lch_dth_rock","Kgt_dth_rock")
#    Zkn.ChangeAnimation("Lch_dth_rockfront","Kgt_dth_rockfront")
#    Zkn.ChangeAnimation("Lch_dth0","Kgt_dth0")
#
#
#
#    Lch=Bladex.GetCharType("Lich","Lch")
#    Lch.SetAnmDefaultPrefix("Lch")
#
#    # hurts
#    Lch.ChangeAnimation("Lch_df_01",        "Lch_hurt_lite") 
#    Lch.ChangeAnimation("Lch_df_02",        "Lch_hurt_big2") 
#    Lch.ChangeAnimation("Lch_hurt_f_lite",  "Lch_hurt_lite") 
#    Lch.ChangeAnimation("Lch_hurt_f_breast","Lch_hurt_big") 
#    Lch.ChangeAnimation("Lch_hurt_f_back",  "Lch_hurt_lite") 
#    Lch.ChangeAnimation("Lch_hurt_f_r_arm", "Lch_hurt_lite") 
#    Lch.ChangeAnimation("Lch_hurt_f_l_arm", "Lch_hurt_lite") 
#    Lch.ChangeAnimation("Lch_hurt_f_r_leg", "Lch_hurt_lite") 
#    Lch.ChangeAnimation("Lch_hurt_f_l_leg", "Lch_hurt_lite") 
#    Lch.ChangeAnimation("Lch_hurt_jog",     "Lch_hurt_big2") 
#    Lch.ChangeAnimation("Lch_hurt_head",    "Lch_hurt_big") 
#    Lch.ChangeAnimation("Lch_hurt_breast",  "Lch_hurt_big") 
#    Lch.ChangeAnimation("Lch_hurt_back",    "Lch_hurt_big") 
#    Lch.ChangeAnimation("Lch_hurt_r_arm",   "Lch_hurt_lite") 
#    Lch.ChangeAnimation("Lch_hurt_l_arm",   "Lch_hurt_lite") 
#    Lch.ChangeAnimation("Lch_hurt_r_leg",   "Lch_hurt_lite") 
#    Lch.ChangeAnimation("Lch_hurt_l_leg",   "Lch_hurt_lite") 
#
#
#    Lch.ChangeAnimation("Lch_dth_c1","Lch_dth_c1")
#    Lch.ChangeAnimation("Lch_dth_c2","Lch_dth_c2")
#    Lch.ChangeAnimation("Lch_dth_c3","Lch_dth_c3")
#    Lch.ChangeAnimation("Lch_dth_c4","Lch_dth_c4")
#    Lch.ChangeAnimation("Lch_dth_c5","Lch_dth_c5")
#    Lch.ChangeAnimation("Lch_dth_c6","Lch_dth_c6")
#    Lch.ChangeAnimation("Lch_dth_c7","Lch_dth_c1")
#    Lch.ChangeAnimation("Lch_dth_n01","Lch_dth_n01")
#    Lch.ChangeAnimation("Lch_dth_n02","Lch_dth_n02")
#    Lch.ChangeAnimation("Lch_dth_n03","Lch_dth_n03")
#    Lch.ChangeAnimation("Lch_dth_n04","Lch_dth_n04")
#    Lch.ChangeAnimation("Lch_dth_n05","Lch_dth_n05")
#    Lch.ChangeAnimation("Lch_dth_n06","Lch_dth_n06")
#    Lch.ChangeAnimation("Lch_dth0","Lch_dth0")
#
#
#
#
#
#
#
#
#
#
#    ########TROLL##################
#
#
#
#
#    Trl=Bladex.GetCharType("Troll_Dark","Trl_dk")
#    Trl.SetAnmDefaultPrefix("Trl")
#
#    Trl.ChangeAnimation("Trl_hurt_f_lite",  "Trl_hurt_l_arm")  
#    Trl.ChangeAnimation("Trl_hurt_f_big",   "Trl_hurt_big")   
#    Trl.ChangeAnimation("Trl_hurt_f_head",  "Trl_hurt_breast")  
#    Trl.ChangeAnimation("Trl_hurt_f_breast","Trl_hurt_breast")
#    Trl.ChangeAnimation("Trl_hurt_f_back",  "Trl_hurt_back")  
#    Trl.ChangeAnimation("Trl_hurt_f_r_arm", "Trl_hurt_r_arm") 
#    Trl.ChangeAnimation("Trl_hurt_f_l_arm", "Trl_hurt_l_arm") 
#    Trl.ChangeAnimation("Trl_hurt_f_r_leg", "Trl_hurt_r_leg") 
#    Trl.ChangeAnimation("Trl_hurt_f_l_leg", "Trl_hurt_l_leg")  
#    Trl.ChangeAnimation("Trl_hurt_head",    "Trl_hurt_breast")
#
#
#
#
#
#
#
#
#
#    # hurts
#
#
#
#
#
#    #####XAPUSA DE LOS ENANOS##########
#
#
#    Dwf=Bladex.GetCharType("Enano1","Dwf")
#    Dwf.SetAnmDefaultPrefix("Dwf")
#
#    Dwf.ChangeAnimation("Dwf_act01","Bar_act01")
#    Dwf.ChangeAnimation("Dwf_lvr_u","Bar_lvr_u")
#    Dwf.ChangeAnimation("Dwf_r_f","Bar_r_f")
#    Dwf.ChangeAnimation("Dwf_fire0","Bar_fire0")
#    Dwf.ChangeAnimation("Dwf_fire1","Bar_fire1")
#    Dwf.ChangeAnimation("Dwf_fire2","Bar_fire2")
#    Dwf.ChangeAnimation("Dwf_fire3","Bar_fire3")
#    Dwf.ChangeAnimation("Dwf_fire_g","Bar_fire_g")
#    Dwf.ChangeAnimation("Dwf_dth_c2","Kgt_dth_c2")
#    Dwf.ChangeAnimation("Dwf_dth_c3","Kgt_dth_c3")
#    Dwf.ChangeAnimation("Dwf_dth_c4","Kgt_dth_c4")
#    Dwf.ChangeAnimation("Dwf_dth_c5","Kgt_dth_c5")
#    Dwf.ChangeAnimation("Dwf_dth_c6","Kgt_dth_c6")
#    Dwf.ChangeAnimation("Dwf_dth_c7","Ork_dth_c1")
#    Dwf.ChangeAnimation("Dwf_dth_n04","Kgt_dth_n04")
#    Dwf.ChangeAnimation("Dwf_dth_n05","Kgt_dth_n05")
#    Dwf.ChangeAnimation("Dwf_dth_n06","Kgt_dth_n06")
#    Dwf.ChangeAnimation("Dwf_dth_burn","Kgt_dth_burn")
#    Dwf.ChangeAnimation("Dwf_dth_rock","Kgt_dth_rock")
#    Dwf.ChangeAnimation("Dwf_dth_rockfront","Kgt_dth_rockfront")
#    Dwf.ChangeAnimation("Dwf_dth0","Kgt_dth0")
#    Dwf.ChangeAnimation("Dwf_dth_burn","Kgt_dth_burn")
#    #Dwf.ChangeAnimation("Dwf_1tw_h_f","Kgt_1tw_h_f")
#    Dwf.ChangeAnimation("Dwf_attack_drink","Kgt_attack_drink")
#    Dwf.ChangeAnimation("Dwf_pulsador","Kgt_pulsador")
#    Dwf.ChangeAnimation("Dwf_fire1","Kgt_fire1")
#    Dwf.ChangeAnimation("Dwf_fire2","Kgt_fire2")
#    Dwf.ChangeAnimation("Dwf_fire3","Kgt_fire3")
#
#
#
#    Dwf=Bladex.GetCharType("Enano2","Dwf")
#    Dwf.SetAnmDefaultPrefix("Dwf")
#
#    Dwf.ChangeAnimation("Dwf_act01","Bar_act01")
#    Dwf.ChangeAnimation("Dwf_lvr_u","Bar_lvr_u")
#    Dwf.ChangeAnimation("Dwf_r_f","Bar_r_f")
#    Dwf.ChangeAnimation("Dwf_fire0","Bar_fire0")
#    Dwf.ChangeAnimation("Dwf_fire1","Bar_fire1")
#    Dwf.ChangeAnimation("Dwf_fire2","Bar_fire2")
#    Dwf.ChangeAnimation("Dwf_fire3","Bar_fire3")
#    Dwf.ChangeAnimation("Dwf_fire_g","Bar_fire_g")
#    Dwf.ChangeAnimation("Dwf_dth_c2","Kgt_dth_c2")
#    Dwf.ChangeAnimation("Dwf_dth_c3","Kgt_dth_c3")
#    Dwf.ChangeAnimation("Dwf_dth_c4","Kgt_dth_c4")
#    Dwf.ChangeAnimation("Dwf_dth_c5","Kgt_dth_c5")
#    Dwf.ChangeAnimation("Dwf_dth_c6","Kgt_dth_c6")
#    Dwf.ChangeAnimation("Dwf_dth_c7","Ork_dth_c1")
#    Dwf.ChangeAnimation("Dwf_dth_n04","Kgt_dth_n04")
#    Dwf.ChangeAnimation("Dwf_dth_n05","Kgt_dth_n05")
#    Dwf.ChangeAnimation("Dwf_dth_n06","Kgt_dth_n06")
#    Dwf.ChangeAnimation("Dwf_dth_burn","Kgt_dth_burn")
#    Dwf.ChangeAnimation("Dwf_dth_rock","Kgt_dth_rock")
#    Dwf.ChangeAnimation("Dwf_dth_rockfront","Kgt_dth_rockfront")
#    Dwf.ChangeAnimation("Dwf_dth0","Kgt_dth0")
#    Dwf.ChangeAnimation("Dwf_dth_burn","Kgt_dth_burn")
#    #Dwf.ChangeAnimation("Dwf_1tw_h_f","Kgt_1tw_h_f")
#    Dwf.ChangeAnimation("Dwf_attack_drink","Kgt_attack_drink")
#    Dwf.ChangeAnimation("Dwf_pulsador","Kgt_pulsador")
#    Dwf.ChangeAnimation("Dwf_fire1","Kgt_fire1")
#    Dwf.ChangeAnimation("Dwf_fire2","Kgt_fire2")
#    Dwf.ChangeAnimation("Dwf_fire3","Kgt_fire3")
#
#
#    Glm=Bladex.GetCharType("Golem_stone","Glm")
#    Glm.SetAnmDefaultPrefix("Glm")
#    Glm.ChangeAnimation("Glm_hurt_f_big",   "Glm_hurt_big") 
#
#    Glm=Bladex.GetCharType("Golem_clay","Glm")
#    Glm.SetAnmDefaultPrefix("Glm")
#    Glm.ChangeAnimation("Glm_hurt_f_big",   "Glm_hurt_big") 
#
#    Glm=Bladex.GetCharType("Golem_lava","Glm")
#    Glm.SetAnmDefaultPrefix("Glm")
#    Glm.ChangeAnimation("Glm_hurt_f_big",   "Glm_hurt_big") 
#     
#    Glm=Bladex.GetCharType("Golem_metal","Glm")
#    Glm.SetAnmDefaultPrefix("Glm")
#    Glm.ChangeAnimation("Glm_hurt_f_big",   "Glm_hurt_big")
#
#
#
#
#    Kgt=Bladex.GetCharType("Knight_N","Kgt")
#    Kgt.SetAnmDefaultPrefix("Kgt")
#    Kgt.ChangeAnimation("Kgt_chg_r_l",   "Kgt_attack_chg_r_l")
#    Kgt.ChangeAnimation("Kgt_chg_r",   "Kgt_attack_chg_r")
#    Kgt.ChangeAnimation("Kgt_chg_l",   "Kgt_attack_chg_l")
#    Kgt.ChangeAnimation("Kgt_dth_c7","Ork_dth_c1")
#    Kgt.ChangeAnimation("Kgt_gulp00","Kgt_gulp")
#
#
#    """
#    # Death animations
#    "Glm_dth0"
#    "Glm_dth_c1"
#    "Glm_dth0"
#    "Glm_dth0"
#    "Glm_dth0"
#    "Glm_dth0"
#
#    # Blocking/Hurt animations
#    "df_01_2w"
#    "df_01_axe"
#    "df_01_spear"
#    "df_01"
#    "df_02_2w"
#    "df_02_axe"
#    "df_02_spear"
#    "df_02"
#    "hurt_f_lite"
#    "hurt_f_big"
#    "hurt_f_head"
#    "hurt_f_breast"
#    "hurt_f_back"
#    "hurt_f_r_arm"
#    "hurt_f_l_arm"
#    "hurt_f_r_leg"
#    "hurt_f_l_leg"
#    "hurt_jog"
#    "hurt_head"
#    "hurt_breast"
#    "hurt_back"
#    "hurt_r_arm"
#    "hurt_l_arm"
#    "hurt_r_leg"
#    "hurt_l_leg"
#    """