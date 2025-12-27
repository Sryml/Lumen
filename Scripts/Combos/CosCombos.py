######################################################
#
# Create sets of attacks
#
#        - Cos -
#
######################################################


import Bladex

ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2

# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Cos","g_01","ATTACKING")

# Predeclare & link all my dodges into DODGING action event tables
Bladex.SetActionEventTable("Cos","D_r", "DODGING")
Bladex.SetActionEventTable("Cos","D_l", "DODGING")

cos=Bladex.GetCharType("Cos","Cos")

###############################
# GRUPOS DE GOLPES ALEATORIOS #
###############################
#GA group

cos.AddAttack("GA","Cos_g_01")
cos.AttackWindow("Cos_g_01",5,15,"GA_Window")

cos.AttackTypeFlag("GA",ATK_RANDOM)

cos.AllowAttack("GA","A","","","")


