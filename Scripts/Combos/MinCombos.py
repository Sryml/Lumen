######################################################
#
# Create sets of attacks
#
#        - MIN -
#
######################################################


import Bladex

ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2



##############
# Minotaur #
##############

# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Min","g_01","ATTACKING")
Bladex.SetActionEventTable("Min","g_07","ATTACKING")
Bladex.SetActionEventTable("Min","g_08","ATTACKING")
Bladex.SetActionEventTable("Min","g_12","ATTACKING")
Bladex.SetActionEventTable("Min","g_31","ATTACKING")

# Predeclare & link all my dodges into DODGING action event tables
Bladex.SetActionEventTable("Min","D_r", "DODGING")
Bladex.SetActionEventTable("Min","D_l", "DODGING")
Bladex.SetActionEventTable("Min","D_b", "DODGING")

Min=Bladex.GetCharType("Minotaur","Min")

###############################
# GRUPOS DE GOLPES ALEATORIOS #
###############################
#GA group

#G01 group
Min.AddAttack("G01","Min_g_01")
Min.AttackTypeFlag("G01",ATK_UNIQUE)

Min.AddAttack("G07","Min_g_07")
Min.AttackTypeFlag("G07",ATK_UNIQUE)

Min.AddAttack("G08","Min_g_08")
Min.AttackTypeFlag("G08",ATK_UNIQUE)

Min.AddAttack("G12","Min_g_12")
Min.AttackTypeFlag("G12",ATK_UNIQUE)

Min.AddAttack("G31","Min_g_31")
Min.AttackTypeFlag("G31",ATK_UNIQUE)

