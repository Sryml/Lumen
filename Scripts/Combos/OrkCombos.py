######################################################
#
# Create sets of attacks
#
#        - ORK -
#
######################################################


import Bladex


ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2

# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Ork","g_01","ATTACKING")
Bladex.SetActionEventTable("Ork","g_02","ATTACKING")
Bladex.SetActionEventTable("Ork","g_06","ATTACKING")
Bladex.SetActionEventTable("Ork","g_15","ATTACKING")
Bladex.SetActionEventTable("Ork","g_16","ATTACKING")
Bladex.SetActionEventTable("Ork","g_18","ATTACKING")

# Predeclare & link all my dodges into DODGING action event tables
Bladex.SetActionEventTable("Ork","D_r", "DODGING")
Bladex.SetActionEventTable("Ork","D_l", "DODGING")
Bladex.SetActionEventTable("Ork","D_b", "DODGING")

ork=Bladex.GetCharType("Ork","Ork")






####################
# GRUPOS DE GOLPES #
####################
ork.AddAttack("g_01","Ork_g_01")
ork.AttackTypeFlag("g_01",ATK_UNIQUE)

ork.AddAttack("g_02","Ork_g_02")
ork.AttackTypeFlag("g_02",ATK_UNIQUE)

ork.AddAttack("g_06","Ork_g_06")
ork.AttackTypeFlag("g_06",ATK_UNIQUE)

ork.AddAttack("g_15","Ork_g_15")
ork.AssignTrail("g_15","","EstelaAmarilla1")
ork.AttackTypeFlag("g_15",ATK_UNIQUE)

ork.AddAttack("g_16","Ork_g_16")
ork.AssignTrail("g_16","","EstelaAmarilla1")
ork.AttackTypeFlag("g_16",ATK_UNIQUE)

ork.AddAttack("g_18","Ork_g_18")
ork.AssignTrail("g_18","","EstelaRoja1")
ork.AttackTypeFlag("g_18",ATK_UNIQUE)

ork.AttackTypeFlag("COMBO1",ATK_SEQUENTIAL)
ork.AddAttack("COMBO1","Ork_g_06")
ork.AddAttack("COMBO1","Ork_g_02")
ork.AddAttack("COMBO1","Ork_g_18")

ork.AttackTypeFlag("COMBO2",ATK_SEQUENTIAL)
ork.AddAttack("COMBO2","Ork_g_16")
ork.AddAttack("COMBO2","Ork_g_01")

ork.AttackTypeFlag("COMBO3",ATK_SEQUENTIAL)
ork.AddAttack("COMBO3","Ork_g_02")
ork.AddAttack("COMBO3","Ork_g_06")
ork.AddAttack("COMBO3","Ork_g_01")

###############################
# GRUPO PARA ESCALERAS        #
###############################
ork.AddAttack("STAIRS","Ork_g_16")
ork.AssignTrail("STAIRS","","EstelaAmarilla1")
ork.AddAttack("STAIRS","Ork_g_18")
ork.AssignTrail("STAIRS","","EstelaRoja1")
ork.AttackTypeFlag("STAIRS",ATK_RANDOM)




