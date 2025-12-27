######################################################
#
# Create sets of attacks
#
#        - CHK -
#
######################################################



import Bladex

ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2


# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Chk","g_magic","ATTACKING")
Bladex.SetActionEventTable("Chk","g_01","ATTACKING")
Bladex.SetActionEventTable("Chk","g_02","ATTACKING")
Bladex.SetActionEventTable("Chk","g_07","ATTACKING")
Bladex.SetActionEventTable("Chk","g_08","ATTACKING")
Bladex.SetActionEventTable("Chk","g_12","ATTACKING")
Bladex.SetActionEventTable("Chk","g_18","ATTACKING")
Bladex.SetActionEventTable("Chk","g_31","ATTACKING")


chk=Bladex.GetCharType("ChaosKnight","Chk")


###############################
# GRUPOS DE GOLPES SELECTIVOS #
###############################
#SP1 group (magic)
chk.AddAttack("SP1","Chk_g_magic")
chk.AttackTypeFlag("SP1",ATK_UNIQUE)

#GM1 group
chk.AddAttack("G01","Chk_g_01")
chk.AttackTypeFlag("GM1",ATK_UNIQUE)
chk.AddLevels("Chk_g_01",0,0)

#GM2 group
chk.AddAttack("G02","Chk_g_02")
chk.AttackTypeFlag("GM2",ATK_UNIQUE)
chk.AddLevels("Chk_g_02",0,0)

#GM3 group
chk.AddAttack("G07","Chk_g_07")
chk.AttackTypeFlag("GM3",ATK_UNIQUE)
chk.AddLevels("Chk_g_07",0,0)

#GM4 group
chk.AddAttack("G08","Chk_g_08")
chk.AttackTypeFlag("GM4",ATK_UNIQUE)
chk.AddLevels("Chk_g_08",0,0)

#GM5 group
chk.AddAttack("G12","Chk_g_12")
chk.AttackTypeFlag("GM5",ATK_UNIQUE)
chk.AddLevels("Chk_g_12",0,0)
chk.AssignTrail("G12","","EstelaAmarilla1")

#GM6 group
chk.AddAttack("G18","Chk_g_18")
chk.AttackTypeFlag("GM6",ATK_UNIQUE)
chk.AddLevels("Chk_g_18",0,0)
chk.AssignTrail("G18","","EstelaRoja1")

#GM7 group
chk.AddAttack("G31","Chk_g_31")
chk.AttackTypeFlag("GM7",ATK_UNIQUE)
chk.AddLevels("Chk_g_31",0,0)
chk.AssignTrail("G31","","EstelaRoja1")








