######################################################
#
# Create sets of attacks
#
#        - TRL -
#
######################################################


import Bladex

ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2



##############
# Dark Troll #
##############

# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Trl","g_01","ATTACKING")
Bladex.SetActionEventTable("Trl","g_02","ATTACKING")
Bladex.SetActionEventTable("Trl","g_04","ATTACKING")
Bladex.SetActionEventTable("Trl","g_06","ATTACKING")
Bladex.SetActionEventTable("Trl","g_12","ATTACKING")
Bladex.SetActionEventTable("Trl","g_18","ATTACKING")
Bladex.SetActionEventTable("Trl","g_19","ATTACKING")
Bladex.SetActionEventTable("Trl","g_31","ATTACKING")

trl=Bladex.GetCharType("Troll_Dark","Trl_dk")

###############################
# GRUPOS DE GOLPES ALEATORIOS #
###############################
#GA group

#G01 group
trl.AddAttack("G01","Trl_g_01")
trl.AttackTypeFlag("G01",ATK_UNIQUE)

trl.AddAttack("G02","Trl_g_02")
trl.AttackTypeFlag("G02",ATK_UNIQUE)

trl.AddAttack("G04","Trl_g_04")
trl.AttackTypeFlag("G04",ATK_UNIQUE)

trl.AddAttack("G06","Trl_g_06")
trl.AttackTypeFlag("G06",ATK_UNIQUE)

trl.AddAttack("G12","Trl_g_12")
trl.AttackTypeFlag("G12",ATK_UNIQUE)

trl.AddAttack("G18","Trl_g_18")
trl.AttackTypeFlag("G18",ATK_UNIQUE)

trl.AddAttack("G19","Trl_g_19")
trl.AttackTypeFlag("G19",ATK_UNIQUE)

trl.AddAttack("G31","Trl_g_31")
trl.AttackTypeFlag("G31",ATK_UNIQUE)


# Move the snow troll combos into a file of their own and add SetActionEventTable calls
##############
# Snow Troll #
##############

trl=Bladex.GetCharType("Troll_snow","Trl_sn")

###############################
# GRUPOS DE GOLPES ALEATORIOS #
###############################
#GA group

#G01 group
trl.AddAttack("G01","Trl_g_01")
trl.AttackTypeFlag("G01",ATK_UNIQUE)

trl.AddAttack("G02","Trl_g_02")
trl.AttackTypeFlag("G02",ATK_UNIQUE)

trl.AddAttack("G04","Trl_g_04")
trl.AttackTypeFlag("G04",ATK_UNIQUE)

trl.AddAttack("G06","Trl_g_06")
trl.AttackTypeFlag("G06",ATK_UNIQUE)

trl.AddAttack("G12","Trl_g_12")
trl.AttackTypeFlag("G12",ATK_UNIQUE)

trl.AddAttack("G18","Trl_g_18")
trl.AttackTypeFlag("G18",ATK_UNIQUE)

trl.AddAttack("G19","Trl_g_19")
trl.AttackTypeFlag("G19",ATK_UNIQUE)

trl.AddAttack("G31","Trl_g_31")
trl.AttackTypeFlag("G31",ATK_UNIQUE)
