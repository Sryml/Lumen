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
Bladex.SetActionEventTable("Skl","g_01","ATTACKING")
Bladex.SetActionEventTable("Skl","g_02","ATTACKING")
Bladex.SetActionEventTable("Skl","g_07","ATTACKING")
Bladex.SetActionEventTable("Skl","g_09","ATTACKING")
Bladex.SetActionEventTable("Skl","g_16","ATTACKING")
Bladex.SetActionEventTable("Skl","g_18","ATTACKING")
Bladex.SetActionEventTable("Skl","g_22","ATTACKING")

skl=Bladex.GetCharType("Skeleton","Skl")

###############################
# GRUPOS DE GOLPES ALEATORIOS #
###############################
#GA group

skl.AddAttack("GA","Skl_g_01")
skl.AddAttack("GA","Skl_g_02")
skl.AddAttack("GA","Skl_g_07")
skl.AddAttack("GA","Skl_g_09")

skl.AttackTypeFlag("GA",ATK_RANDOM)

###############################
# GRUPOS DE GOLPES SELECTIVOS #
###############################

#GM1 group
skl.AddAttack("GM1","Skl_g_16")

skl.AttackTypeFlag("GM1",ATK_SEQUENTIAL)

#GM2 group
skl.AddAttack("GM2","Skl_g_16")
skl.AddAttack("GM2","Skl_g_18")

skl.AttackTypeFlag("GM2",ATK_SEQUENTIAL)

#G22 group
skl.AddAttack("G22","Skl_g_22")

skl.AttackTypeFlag("G22",ATK_UNIQUE)


###############################
# GRUPO PARA ESCALERAS        #
###############################
skl.AddAttack("STAIRS","Ork_g_16")
skl.AddAttack("STAIRS","Ork_g_18")

skl.AttackTypeFlag("STAIRS",ATK_RANDOM)



