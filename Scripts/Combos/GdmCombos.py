######################################################
#
# Create sets of attacks
#
#        - Gdm -
#
######################################################



import Bladex

ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2


# Predeclare & link all my combos into ATTACKING action event tables


Bladex.SetActionEventTable("Gdm","g_01","ATTACKING")
Bladex.SetActionEventTable("Gdm","g_12","ATTACKING")
Bladex.SetActionEventTable("Gdm","g_back","ATTACKING")
Bladex.SetActionEventTable("Gdm","g_claw","ATTACKING")
Bladex.SetActionEventTable("Gdm","g_quake","ATTACKING")
Bladex.SetActionEventTable("Gdm","g_magic","ATTACKING")
Bladex.SetActionEventTable("Gdm","g_spit_f","ATTACKING")
Bladex.SetActionEventTable("Gdm","g_spitball","ATTACKING")
Bladex.SetActionEventTable("Gdm","g_spit_around","ATTACKING")


Gdm=Bladex.GetCharType("Great_Demon","Gdm")


###############################
# GRUPOS DE GOLPES SELECTIVOS #
###############################

Gdm.AddAttack("g_01","Gdm_g_01")
Gdm.AttackTypeFlag("g_01",ATK_UNIQUE)

Gdm.AddAttack("g_12","Gdm_g_12")
Gdm.AttackTypeFlag("g_12",ATK_UNIQUE)

Gdm.AddAttack("g_back","Gdm_g_back")
Gdm.AttackTypeFlag("g_back",ATK_UNIQUE)

Gdm.AddAttack("g_claw","Gdm_g_claw")
Gdm.AttackTypeFlag("g_claw",ATK_UNIQUE)

Gdm.AddAttack("g_quake","Gdm_g_quake")
Gdm.AttackTypeFlag("g_quake",ATK_UNIQUE)

Gdm.AddAttack("g_magic","Gdm_g_magic")
Gdm.AttackTypeFlag("g_magic",ATK_UNIQUE)

Gdm.AddAttack("g_spit_f","Gdm_g_spit_f")
Gdm.AttackTypeFlag("g_spit_f",ATK_UNIQUE)

Gdm.AddAttack("g_spitball","Gdm_g_spitball")
Gdm.AttackTypeFlag("g_spitball",ATK_UNIQUE)

Gdm.AddAttack("g_spit_around","Gdm_g_spit_around")
Gdm.AttackTypeFlag("g_spit_around",ATK_UNIQUE)






