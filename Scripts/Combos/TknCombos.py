######################################################
#
# Create sets of attacks
#
#        - TKN -
#
######################################################


import Bladex

ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2



# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Knight_Traitor","g_01","ATTACKING")
Bladex.SetActionEventTable("Knight_Traitor","g_02","ATTACKING")
Bladex.SetActionEventTable("Knight_Traitor","g_05","ATTACKING")
Bladex.SetActionEventTable("Knight_Traitor","g_07","ATTACKING")
Bladex.SetActionEventTable("Knight_Traitor","g_08","ATTACKING")
Bladex.SetActionEventTable("Knight_Traitor","g_11","ATTACKING")
Bladex.SetActionEventTable("Knight_Traitor","g_13","ATTACKING")
Bladex.SetActionEventTable("Knight_Traitor","g_14","ATTACKING")
Bladex.SetActionEventTable("Knight_Traitor","g_16","ATTACKING")
Bladex.SetActionEventTable("Knight_Traitor","g_18","ATTACKING")

# Predeclare & link all my dodges into DODGING action event tables
Bladex.SetActionEventTable("Knight_Traitor","D_r", "DODGING")
Bladex.SetActionEventTable("Knight_Traitor","D_l", "DODGING")
Bladex.SetActionEventTable("Knight_Traitor","D_b", "DODGING")



tkn=Bladex.GetCharType("Knight_Traitor","Tkn")

###############################
# GRUPOS DE GOLPES ALEATORIOS #
###############################
#GA group

tkn.AddAttack("GA","Tkn_g_01")
tkn.AttackWindow("Tkn_g_01",5,15,"GA_Window")

tkn.AddAttack("GA","Tkn_g_02")
tkn.AttackWindow("Tkn_g_02",5,15,"GA_Window")

tkn.AddAttack("GA","Tkn_g_07")
tkn.AttackWindow("Tkn_g_07",5,15,"GA_Window")

tkn.AddAttack("GA","Tkn_g_08")
tkn.AttackWindow("Tkn_g_08",5,15,"GA_Window")

tkn.AttackTypeFlag("GA",ATK_RANDOM)

###############################
# GRUPOS DE GOLPES SELECTIVOS #
###############################

#GM1 group
tkn.AddAttack("GM1","Tkn_g_13")
tkn.AddAttack("GM1","Tkn_g_16")

tkn.AttackTypeFlag("GM1",ATK_SEQUENTIAL)

#GM2 group
tkn.AddAttack("GM2","Tkn_g_13")
tkn.AddAttack("GM2","Tkn_g_16")
tkn.AddAttack("GM2","Tkn_g_18")

tkn.AttackTypeFlag("GM2",ATK_SEQUENTIAL)


###############################
# GRUPO PARA ESCALERAS        #
###############################
tkn.AddAttack("STAIRS","Tkn_g_08")
tkn.AddAttack("STAIRS","Tkn_g_01")
#tkn.AddAttack("STAIRS","Tkn_g_05")
#tkn.AddAttack("STAIRS","Tkn_g_07")
tkn.AddAttack("STAIRS","Tkn_g_18")
tkn.AddAttack("STAIRS","Tkn_g_14")
#tkn.AddAttack("STAIRS","Tkn_g_11")

tkn.AttackTypeFlag("STAIRS",ATK_RANDOM)





