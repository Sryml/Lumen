######################################################
#
# Create sets of attacks
#
#        - Lch -
#
######################################################


import Bladex

ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2


# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Lch","g_spit","ATTACKING")
Bladex.SetActionEventTable("Lch","spit_drag","ATTACKING")
Bladex.SetActionEventTable("Lch","g_12","ATTACKING")
Bladex.SetActionEventTable("Lch","g_13","ATTACKING")
Bladex.SetActionEventTable("Lch","g_16","ATTACKING")
Bladex.SetActionEventTable("Lch","g_18","ATTACKING")
Bladex.SetActionEventTable("Lch","g_claw1","ATTACKING")
Bladex.SetActionEventTable("Lch","g_claw2","ATTACKING")
Bladex.SetActionEventTable("Lch","g_claw3","ATTACKING")

lch=Bladex.GetCharType("Lich","Lch")

ATK_UNIQUE=0

###############################
# GRUPOS DE GOLPES SELECTIVOS #
###############################

#SP1 group
lch.AddAttack("SP1","Lch_g_spit")
lch.AttackTypeFlag("SP1",ATK_UNIQUE)
lch.AddLevels("Lch_g_spit",0,0)

#SP2 group
lch.AddAttack("SP2","Lch_spit_drag")
lch.AttackTypeFlag("SP2",ATK_UNIQUE)
lch.AddLevels("Lch_spit_drag",0,0)

#G12 group
lch.AddAttack("G12","Lch_g_12")
lch.AttackTypeFlag("G12",ATK_UNIQUE)
lch.AddLevels("Lch_g_12",0,0)

#G13 group
lch.AddAttack("G13","Lch_g_13")
lch.AttackTypeFlag("G13",ATK_UNIQUE)
lch.AddLevels("Lch_g_13",0,0)

#G16 group
lch.AddAttack("G16","Lch_g_16")
lch.AttackTypeFlag("G16",ATK_UNIQUE)
lch.AddLevels("Lch_g_16",0,0)

#G18 group
lch.AddAttack("G18","Lch_g_18")
lch.AttackTypeFlag("G18",ATK_UNIQUE)
lch.AddLevels("Lch_g_18",0,0)

#C1 group
lch.AddAttack("C1","Lch_g_claw1")
lch.AttackTypeFlag("C1",ATK_UNIQUE)
lch.AddLevels("Lch_claw1",0,0)

#C2 group
lch.AddAttack("C2","Lch_g_claw2")
lch.AttackTypeFlag("C2",ATK_UNIQUE)
lch.AddLevels("Lch_claw2",0,0)

#C3 group
lch.AddAttack("C3","Lch_g_claw3")
lch.AttackTypeFlag("C3",ATK_UNIQUE)
lch.AddLevels("Lch_claw3",0,0)
