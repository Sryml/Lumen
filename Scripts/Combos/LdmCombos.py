######################################################
#
# Create sets of attacks
#
#        - Ldm -
#
######################################################


import Bladex

ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2


# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Ldm","g_spit","ATTACKING")
Bladex.SetActionEventTable("Ldm","g_03","ATTACKING")
Bladex.SetActionEventTable("Ldm","g_06","ATTACKING")
Bladex.SetActionEventTable("Ldm","g_07","ATTACKING")
Bladex.SetActionEventTable("Ldm","g_22","ATTACKING")
Bladex.SetActionEventTable("Ldm","g_27","ATTACKING")
Bladex.SetActionEventTable("Ldm","g_jumpl","ATTACKING")
Bladex.SetActionEventTable("Ldm","g_jumpr","ATTACKING")


ldm=Bladex.GetCharType("Little_Demon","Ldm")


###############################
# GRUPOS DE GOLPES SELECTIVOS #
###############################

#SP group
ldm.AddAttack("SP1","Ldm_g_spit")
ldm.AttackTypeFlag("SP1",ATK_UNIQUE)

#G03 group
ldm.AddAttack("G03","Ldm_g_03")
ldm.AttackTypeFlag("G03",ATK_UNIQUE)

#G06 group
ldm.AddAttack("G06","Ldm_g_06")
ldm.AttackTypeFlag("G06",ATK_UNIQUE)

#G07 group
ldm.AddAttack("G07","Ldm_g_07")
ldm.AttackTypeFlag("G07",ATK_UNIQUE)

#G22 group
ldm.AddAttack("G22","Ldm_g_22")
ldm.AttackTypeFlag("G22",ATK_UNIQUE)

#G27 group
ldm.AddAttack("G27","Ldm_g_27")
ldm.AttackTypeFlag("G27",ATK_UNIQUE)

#ZIG group
ldm.AddAttack("ZIG","Ldm_g_jumpl")
ldm.AttackTypeFlag("ZIG",ATK_UNIQUE)

#ZAG group
ldm.AddAttack("ZAG","Ldm_g_jumpr")
ldm.AttackTypeFlag("ZAG",ATK_UNIQUE)






