######################################################
#
# Create sets of attacks
#
#        - Rgn -
#
######################################################


import Bladex

ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2



# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Rgn","g_01","ATTACKING")
Bladex.SetActionEventTable("Rgn","g_02","ATTACKING")
Bladex.SetActionEventTable("Rgn","g_03","ATTACKING")
Bladex.SetActionEventTable("Rgn","g_07","ATTACKING")
Bladex.SetActionEventTable("Rgn","g_d_r","ATTACKING")
Bladex.SetActionEventTable("Rgn","g_d_l","ATTACKING")
Bladex.SetActionEventTable("Rgn","g_escape","ATTACKING")
Bladex.SetActionEventTable("Rgn","g_17","ATTACKING")
Bladex.SetActionEventTable("Rgn","g_21","ATTACKING")

# Predeclare & link all my dodges into DODGING action event tables
Bladex.SetActionEventTable("Rgn","D_r", "DODGING")
Bladex.SetActionEventTable("Rgn","D_l", "DODGING")
Bladex.SetActionEventTable("Rgn","D_b", "DODGING")



rgn=Bladex.GetCharType("Ragnar","Rgn")


###############################
# GRUPOS DE GOLPES SELECTIVOS #
###############################


rgn.AddAttack("G01","Rgn_g_01")
rgn.AttackTypeFlag("G01",ATK_UNIQUE)


rgn.AddAttack("G02","Rgn_g_02")
rgn.AttackTypeFlag("G02",ATK_UNIQUE)

rgn.AddAttack("G03","Rgn_g_03")
rgn.AttackTypeFlag("G03",ATK_UNIQUE)

rgn.AddAttack("G07","Rgn_g_07")
rgn.AttackTypeFlag("G07",ATK_UNIQUE)

rgn.AddAttack("GDR","Rgn_g_d_r")
rgn.AttackTypeFlag("GDR",ATK_UNIQUE)

rgn.AddAttack("GDL","Rgn_g_d_l")
rgn.AttackTypeFlag("GDL",ATK_UNIQUE)

rgn.AddAttack("GDB","Rgn_g_escape")
rgn.AttackTypeFlag("GDB",ATK_UNIQUE)

rgn.AddAttack("G17","Rgn_g_17")
rgn.AttackTypeFlag("G17",ATK_UNIQUE)

rgn.AddAttack("G21","Rgn_g_21")
rgn.AttackTypeFlag("G21",ATK_UNIQUE)
