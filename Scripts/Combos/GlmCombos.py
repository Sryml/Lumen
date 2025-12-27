######################################################
#
# Create sets of attacks
#
#        - GLM -
#
######################################################
import Bladex

ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2

def AddGolemAttacks(ctype, biped_name):

	# Predeclare & link all my combos into ATTACKING action event tables
	Bladex.SetActionEventTable(biped_name,"g_01","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_114","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_12","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_21","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_21_27","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_31","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_spit","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_1tw","ATTACKING")


	###############################
	# GRUPOS DE GOLPES ALEATORIOS #
	###############################
	#GA group
	
	#G01 group
	ctype.AddAttack("g_01","Glm_g_01")
	ctype.AttackTypeFlag("g_01",ATK_UNIQUE)
	
	ctype.AddAttack("g_114","Glm_g_114")
	ctype.AttackTypeFlag("G114",ATK_UNIQUE)
	
	ctype.AddAttack("g_12","Glm_g_12")
	ctype.AttackTypeFlag("g_12",ATK_UNIQUE)
	
	ctype.AddAttack("g_21","Glm_g_21")
	ctype.AttackTypeFlag("g_21",ATK_UNIQUE)
	
	ctype.AddAttack("g_21_27","Glm_g_21_27")
	ctype.AttackTypeFlag("g_21_27",ATK_UNIQUE)

	ctype.AddAttack("g_31","Glm_g_31")
	ctype.AttackTypeFlag("g_31",ATK_UNIQUE)

	ctype.AddAttack("g_spit","Glm_g_spit")
	ctype.AttackTypeFlag("g_spit",ATK_UNIQUE)

	ctype.AddAttack("g_1tw","Glm_g_1tw")
	ctype.AttackTypeFlag("g_1tw",ATK_UNIQUE)