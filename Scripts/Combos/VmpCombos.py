######################################################
#
# Create sets of attacks
#
#        - Vmp -
#
######################################################


import Bladex

ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2


# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Vmp","disappear","ATTACKING")
Bladex.SetActionEventTable("Vmp","g_01","ATTACKING")
Bladex.SetActionEventTable("Vmp","g_06","ATTACKING")
Bladex.SetActionEventTable("Vmp","g_07","ATTACKING")
Bladex.SetActionEventTable("Vmp","g_26","ATTACKING")


vmp=Bladex.GetCharType("Vamp","Vmp")


###############################
# GRUPOS DE GOLPES SELECTIVOS #
###############################

#SP1 group
vmp.AddAttack("disappear","Vmp_disappear")
vmp.AttackTypeFlag("disappear",ATK_UNIQUE)
vmp.AddLevels("Vmp_disappears",0,0)

vmp.AddAttack("g_01","Vmp_g_01")
vmp.AttackTypeFlag("g_01",ATK_UNIQUE)
vmp.AddLevels("Vmp_g_01",0,0)

vmp.AddAttack("g_06","Vmp_g_06")
vmp.AttackTypeFlag("g_06",ATK_UNIQUE)
vmp.AddLevels("Vmp_g_06",0,0)

vmp.AddAttack("g_07","Vmp_g_07")
vmp.AttackTypeFlag("g_07",ATK_UNIQUE)
vmp.AddLevels("Vmp_g_07",0,0)

vmp.AddAttack("g_26","Vmp_g_26")
vmp.AttackTypeFlag("g_26",ATK_UNIQUE)
vmp.AddLevels("Vmp_g_26",0,0)


vmp.AttackTypeFlag("COMBO1",ATK_SEQUENTIAL)
vmp.AddAttack("COMBO1","Vmp_g_07")
vmp.AddAttack("COMBO1","Vmp_g_01")

vmp.AttackTypeFlag("COMBO2",ATK_SEQUENTIAL)
vmp.AddAttack("COMBO2","Vmp_g_01")
vmp.AddAttack("COMBO2","Vmp_g_26")




