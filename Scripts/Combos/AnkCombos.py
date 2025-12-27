######################################################
#
# Create sets of attacks
#
#        - Ank -
#
######################################################

import Bladex

ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2





# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Ank","g_01","ATTACKING")
Bladex.SetActionEventTable("Ank","g_02","ATTACKING")
Bladex.SetActionEventTable("Ank","g_07","ATTACKING")



#Aim3Missiles
Bladex.SetActionEventTable("Ank","g_mgc01","ATTACKING")
#AimEnergyBall
Bladex.SetActionEventTable("Ank","g_mgc02","ATTACKING")
#AimLaser
Bladex.SetActionEventTable("Ank","g_mgc03","ATTACKING")



print "HOLA MUNDO - AnkCombos.py !!!"


Ank=Bladex.GetCharType("DarkLord","Ank")

###############################
# GRUPOS DE GOLPES SELECTIVOS #
###############################


Ank.AddAttack("g_01","Ank_g_01")
Ank.AttackTypeFlag("g_01",ATK_UNIQUE)

Ank.AddAttack("g_02","Ank_g_02")
Ank.AttackTypeFlag("g_02",ATK_UNIQUE)

Ank.AddAttack("g_07","Ank_g_07")
Ank.AttackTypeFlag("g_07",ATK_UNIQUE)

#Aim3Missiles
Ank.AddAttack("g_mgc01","Ank_g_mgc01")
Ank.AttackTypeFlag("g_mgc01",ATK_UNIQUE)

#AimEnergyBall
Ank.AddAttack("g_mgc02","Ank_g_mgc02")
Ank.AttackTypeFlag("g_mgc02",ATK_UNIQUE)

#AimLaser
Ank.AddAttack("g_mgc03","Ank_g_mgc03")
Ank.AttackTypeFlag("g_mgc03",ATK_UNIQUE)
