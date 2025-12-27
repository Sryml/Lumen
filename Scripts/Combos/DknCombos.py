######################################################
#
# Create sets of attacks
#
#        - dkn -
#
######################################################



import Bladex

ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2


# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Dkn","g_01","ATTACKING")
Bladex.SetActionEventTable("Dkn","g_02","ATTACKING")
Bladex.SetActionEventTable("Dkn","g_05","ATTACKING")
Bladex.SetActionEventTable("Dkn","g_07","ATTACKING")
Bladex.SetActionEventTable("Dkn","g_08","ATTACKING")
Bladex.SetActionEventTable("Dkn","g_11","ATTACKING")
Bladex.SetActionEventTable("Dkn","g_13","ATTACKING")
Bladex.SetActionEventTable("Dkn","g_14","ATTACKING")
Bladex.SetActionEventTable("Dkn","g_16","ATTACKING")
Bladex.SetActionEventTable("Dkn","g_18","ATTACKING")

# Predeclare & link all my dodges into DODGING action event tables
Bladex.SetActionEventTable("Dkn","D_r", "DODGING")
Bladex.SetActionEventTable("Dkn","D_l", "DODGING")
Bladex.SetActionEventTable("Dkn","D_b", "DODGING")


dkn=Bladex.GetCharType("Dark_Knight","Dkn")

###############################
# GRUPOS DE GOLPES ALEATORIOS #
###############################
#GA group

dkn.AddAttack("GA","Tkn_g_01")
dkn.AttackWindow("Tkn_g_01",5,15,"GA_Window")

dkn.AddAttack("GA","Tkn_g_02")
dkn.AttackWindow("Tkn_g_02",5,15,"GA_Window")

dkn.AddAttack("GA","Tkn_g_07")
dkn.AttackWindow("Tkn_g_07",5,15,"GA_Window")

dkn.AddAttack("GA","Tkn_g_08")
dkn.AttackWindow("Tkn_g_08",5,15,"GA_Window")

dkn.AttackTypeFlag("GA",ATK_RANDOM)

###############################
# GRUPOS DE GOLPES SELECTIVOS #
###############################

#GM1 group
dkn.AddAttack("GM1","Tkn_g_13")
dkn.AddAttack("GM1","Tkn_g_16")

dkn.AttackTypeFlag("GM1",ATK_SEQUENTIAL)

#GM2 group
dkn.AddAttack("GM2","Tkn_g_13")
dkn.AddAttack("GM2","Tkn_g_16")
dkn.AddAttack("GM2","Tkn_g_18")

dkn.AttackTypeFlag("GM2",ATK_SEQUENTIAL)



###############################
# GRUPO PARA ESCALERAS        #
###############################
dkn.AddAttack("STAIRS","Tkn_g_08")
dkn.AddAttack("STAIRS","Tkn_g_01")
#dkn.AddAttack("STAIRS","Tkn_g_05")
#dkn.AddAttack("STAIRS","Tkn_g_07")
dkn.AddAttack("STAIRS","Tkn_g_18")
dkn.AddAttack("STAIRS","Tkn_g_14")
#dkn.AddAttack("STAIRS","Tkn_g_11")

dkn.AttackTypeFlag("STAIRS",ATK_RANDOM)







