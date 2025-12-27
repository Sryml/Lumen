
######################################################
#
# Create sets of attacks
#
#        - SLM -
#
######################################################


import Bladex

ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2



##############
# Salamander #
##############

# Link my combos into Attacking Action Tables
Bladex.SetActionEventTable("Slm","g_bite","ATTACKING")
Bladex.SetActionEventTable("Slm","g_r","ATTACKING")
Bladex.SetActionEventTable("Slm","spit","ATTACKING")

Slm=Bladex.GetCharType("Salamander","Slm")

#g_bite group
Slm.AddAttack("g_bite","Slm_g_bite")
Slm.AttackTypeFlag("g_bite",ATK_UNIQUE)

#g_r group
Slm.AddAttack("g_r","Slm_g_r")
Slm.AttackTypeFlag("g_r",ATK_UNIQUE)

#spit group
Slm.AddAttack("spit","Slm_spit")
Slm.AttackTypeFlag("spit",ATK_UNIQUE)


