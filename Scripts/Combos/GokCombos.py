######################################################
#
# Create sets of attacks
#
#        - Gok -
#
######################################################


import Bladex

ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2


# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Gok","g_01","ATTACKING")
Bladex.SetActionEventTable("Gok","g_02","ATTACKING")
Bladex.SetActionEventTable("Gok","g_06","ATTACKING")
Bladex.SetActionEventTable("Gok","g_15","ATTACKING")
Bladex.SetActionEventTable("Gok","g_16","ATTACKING")
Bladex.SetActionEventTable("Gok","g_18","ATTACKING")

# Predeclare & link all my dodges into DODGES action event tables
Bladex.SetActionEventTable("Gok","D_r", "DODGING")
Bladex.SetActionEventTable("Gok","D_l", "DODGING")
Bladex.SetActionEventTable("Gok","D_b", "DODGING")

gok=Bladex.GetCharType("Great_Ork","Gok")

#####################
# GRUPOS DE GOLPES #
####################
gok.AddAttack("g_01","Ork_g_01")
gok.AttackTypeFlag("g_01",ATK_UNIQUE)

gok.AddAttack("g_02","Ork_g_02")
gok.AttackTypeFlag("g_02",ATK_UNIQUE)

gok.AddAttack("g_06","Ork_g_06")
gok.AttackTypeFlag("g_06",ATK_UNIQUE)

gok.AddAttack("g_15","Ork_g_15")
gok.AssignTrail("g_15","","EstelaAmarilla1")
gok.AttackTypeFlag("g_15",ATK_UNIQUE)

gok.AddAttack("g_16","Ork_g_16")
gok.AssignTrail("g_16","","EstelaAmarilla1")
gok.AttackTypeFlag("g_16",ATK_UNIQUE)

gok.AddAttack("g_18","Ork_g_18")
gok.AssignTrail("g_18","","EstelaRoja1")
gok.AttackTypeFlag("g_18",ATK_UNIQUE)

gok.AttackTypeFlag("COMBO1",ATK_SEQUENTIAL)
gok.AddAttack("COMBO1","Ork_g_06")
gok.AddAttack("COMBO1","Ork_g_02")
gok.AddAttack("COMBO1","Ork_g_18")

gok.AttackTypeFlag("COMBO2",ATK_SEQUENTIAL)
gok.AddAttack("COMBO2","Ork_g_16")
gok.AddAttack("COMBO2","Ork_g_01")

gok.AttackTypeFlag("COMBO3",ATK_SEQUENTIAL)
gok.AddAttack("COMBO3","Ork_g_02")
gok.AddAttack("COMBO3","Ork_g_06")
gok.AddAttack("COMBO3","Ork_g_01")

###############################
# GRUPO PARA ESCALERAS        #
###############################
gok.AddAttack("STAIRS","Ork_g_16")
gok.AssignTrail("STAIRS","","EstelaAmarilla1")
gok.AddAttack("STAIRS","Ork_g_18")
gok.AssignTrail("STAIRS","","EstelaRoja1")
gok.AttackTypeFlag("STAIRS",ATK_RANDOM)






