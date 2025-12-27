######################################################
#
# Create sets of attacks
#
#        - Dgk -
#
######################################################


import Bladex


# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Dgk","g_m01","ATTACKING")
Bladex.SetActionEventTable("Dgk","g_m02","ATTACKING")
Bladex.SetActionEventTable("Dgk","g_tw5","ATTACKING")
Bladex.SetActionEventTable("Dgk","g_magic","ATTACKING")
Bladex.SetActionEventTable("Dgk","g_magic2","ATTACKING")

# Simples
Bladex.SetActionEventTable("Dgk","g_07_new","ATTACKING")
Bladex.SetActionEventTable("Dgk","g_08_new","ATTACKING")
Bladex.SetActionEventTable("Dgk","g_02_new","ATTACKING")
Bladex.SetActionEventTable("Dgk","g_01_7_new","ATTACKING")
Bladex.SetActionEventTable("Dgk","g_22lowkata_new","ATTACKING")

# Specials
Bladex.SetActionEventTable("Dgk","g_21_6_s8new","ATTACKING")
Bladex.SetActionEventTable("Dgk","g_19_bs1_new","ATTACKING")
Bladex.SetActionEventTable("Dgk","g_b32kata_new","ATTACKING")
Bladex.SetActionEventTable("Dgk","g_29_3new","ATTACKING")

# Dodge attacks
Bladex.SetActionEventTable("Dgk","g_d_l","ATTACKING")
Bladex.SetActionEventTable("Dgk","g_d_r","ATTACKING")

# Backstroke
Bladex.SetActionEventTable("Dgk","g_back","ATTACKING")


Dgk=Bladex.GetCharType("DalGurak","Dgk")

###############################
# MAGICAL ATTACKS             #
###############################
Dgk.AddAttack("GM01","Dgk_g_m01")	# DISC	
Dgk.AddAttack("GM02","Dgk_g_m02")	# ENERGY BALL
Dgk.AddAttack("GTH5","Dgk_g_tw5")	# Launched Weapon


#####################################
# LAUNCH TRAILS ATTACKS WITH WEAPON #
#####################################
Dgk.AddAttack("GMG1","Dgk_g_magic")
Dgk.AddAttack("GMG2","Dgk_g_magic2")


###############################
# MELEE ATTACKS (SIMPLES)     #
###############################
Dgk.AddAttack("g_07_new","Dgk_g_07_new")
Dgk.AddAttack("g_08_new","Dgk_g_08_new")
Dgk.AddAttack("g_02_new","Dgk_g_02_new")
Dgk.AddAttack("g_01_7_new","Dgk_g_01_7_new")
Dgk.AddAttack("g_22lowkata_new","Dgk_g_22lowkata_new")

###############################
# MELEE ATTACKS (SPECIALS)    #
###############################
Dgk.AddAttack("g_21_6_s8new","Dgk_g_21_6_s8new")
Dgk.AddAttack("g_19_bs1_new","Dgk_g_19_bs1_new")
Dgk.AddAttack("g_b32kata_new","Dgk_g_b32kata_new")
Dgk.AddAttack("g_29_3new","Dgk_g_29_3new")

###############################
# DODGE ATTACKS               #
###############################
Dgk.AddAttack("g_d_l","Dgk_g_d_l")
Dgk.AddAttack("g_d_r","Dgk_g_d_r")

###############################
# BACKSTROKE ATTACKS          #
###############################
Dgk.AddAttack("g_back","Dgk_g_back")

