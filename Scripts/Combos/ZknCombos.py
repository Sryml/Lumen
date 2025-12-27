######################################################
#
# Create sets of attacks
#
#        - Zkn -
#
######################################################


import Bladex

ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2



# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Zkn","g_spit","ATTACKING")
Bladex.SetActionEventTable("Zkn","spit_drag","ATTACKING")
Bladex.SetActionEventTable("Zkn","g_12","ATTACKING")
Bladex.SetActionEventTable("Zkn","g_13","ATTACKING")
Bladex.SetActionEventTable("Zkn","g_16","ATTACKING")
Bladex.SetActionEventTable("Zkn","g_18","ATTACKING")
Bladex.SetActionEventTable("Zkn","g_claw1","ATTACKING")
Bladex.SetActionEventTable("Zkn","g_claw2","ATTACKING")
Bladex.SetActionEventTable("Zkn","g_claw3","ATTACKING")

zkn=Bladex.GetCharType("Knight_Zombie","Zkn")


###############################
# GRUPOS DE GOLPES SELECTIVOS #
###############################

#SP1 group
zkn.AddAttack("SP1","Lch_g_spit")
zkn.AttackTypeFlag("SP1",ATK_UNIQUE)
zkn.AddLevels("Lch_g_spit",0,0)

#SP2 group
zkn.AddAttack("SP2","Lch_spit_drag")
zkn.AttackTypeFlag("SP2",ATK_UNIQUE)
zkn.AddLevels("Lch_spit_drag",0,0)

#G12 group
zkn.AddAttack("G12","Lch_g_12")
zkn.AttackTypeFlag("G12",ATK_UNIQUE)
zkn.AddLevels("Lch_g_12",0,0)

#G13 group
zkn.AddAttack("G13","Lch_g_13")
zkn.AttackTypeFlag("G13",ATK_UNIQUE)
zkn.AddLevels("Lch_g_13",0,0)

#G16 group
zkn.AddAttack("G16","Lch_g_16")
zkn.AttackTypeFlag("G16",ATK_UNIQUE)
zkn.AddLevels("Lch_g_16",0,0)

#G18 group
zkn.AddAttack("G18","Lch_g_18")
zkn.AttackTypeFlag("G18",ATK_UNIQUE)
zkn.AddLevels("Lch_g_18",0,0)

#C1 group
zkn.AddAttack("C1","Lch_g_claw1")
zkn.AttackTypeFlag("C1",ATK_UNIQUE)
zkn.AddLevels("Lch_claw1",0,0)

#C2 group
zkn.AddAttack("C2","Lch_g_claw2")
zkn.AttackTypeFlag("C2",ATK_UNIQUE)
zkn.AddLevels("Lch_claw2",0,0)

#C3 group
zkn.AddAttack("C3","Lch_g_claw3")
zkn.AttackTypeFlag("C3",ATK_UNIQUE)
zkn.AddLevels("Lch_claw3",0,0)
