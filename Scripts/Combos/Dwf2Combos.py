######################################################
#
# Create sets of attacks
#
#        - DWF -
#
######################################################




import Bladex

ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2



# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Enb","g_08","ATTACKING")
Bladex.SetActionEventTable("Enb","g_01","ATTACKING")
Bladex.SetActionEventTable("Enb","g_02","ATTACKING")
Bladex.SetActionEventTable("Enb","g_05","ATTACKING")
Bladex.SetActionEventTable("Enb","g_06","ATTACKING")
Bladex.SetActionEventTable("Enb","g_07","ATTACKING")
Bladex.SetActionEventTable("Enb","g_09","ATTACKING")
Bladex.SetActionEventTable("Enb","g_18","ATTACKING")
Bladex.SetActionEventTable("Enb","g_15","ATTACKING")
Bladex.SetActionEventTable("Enb","g_14","ATTACKING")
Bladex.SetActionEventTable("Enb","g_13","ATTACKING")
Bladex.SetActionEventTable("Enb","g_16","ATTACKING")
Bladex.SetActionEventTable("Enb","g_11","ATTACKING")
Bladex.SetActionEventTable("Enb","g_12","ATTACKING")
Bladex.SetActionEventTable("Enb","g_17","ATTACKING")
Bladex.SetActionEventTable("Enb","g_21","ATTACKING")
Bladex.SetActionEventTable("Enb","g_22","ATTACKING")
Bladex.SetActionEventTable("Enb","g_23","ATTACKING")
Bladex.SetActionEventTable("Enb","g_26","ATTACKING")
Bladex.SetActionEventTable("Enb","g_27","ATTACKING")
Bladex.SetActionEventTable("Enb","g_31","ATTACKING")

# Predeclare & link all my dodges into DODGES action event tables
Bladex.SetActionEventTable("Enb","D_r", "DODGING")
Bladex.SetActionEventTable("Enb","D_l", "DODGING")
Bladex.SetActionEventTable("Enb","D_b", "DODGING")

dwf=Bladex.GetCharType("Enano2","Enano2")

#GI "group"
dwf.AddAttack("GI","Dwf_g_08")
dwf.AttackWindow("Dwf_g_08",2,20,"GI_Window")
#dwf.AttackTypeFlag("GI",ATK_UNIQUE) #If only one attack given , UNIQUE flag is applied


###############################
# GRUPOS DE GOLPES ALEATORIOS #
###############################
#GA group

dwf.AddAttack("GA","Dwf_g_01")
dwf.AttackWindow("Dwf_g_01",5,15,"GA_Window")

dwf.AddAttack("GA","Dwf_g_02")
dwf.AttackWindow("Dwf_g_02",5,15,"GA_Window")

dwf.AddAttack("GA","Dwf_g_05")
dwf.AttackWindow("Dwf_g_05",5,15,"GA_Window")

dwf.AddAttack("GA","Dwf_g_06")
dwf.AttackWindow("Dwf_g_06",5,15,"GA_Window")

dwf.AddAttack("GA","Dwf_g_07")
dwf.AttackWindow("Dwf_g_07",5,15,"GA_Window")

dwf.AddAttack("GA","Dwf_g_08")
dwf.AttackWindow("Dwf_g_08",5,15,"GA_Window")

dwf.AddAttack("GA","Dwf_g_09")
dwf.AttackWindow("Dwf_g_09",5,15,"GA_Window")


dwf.AttackTypeFlag("GA",ATK_RANDOM)

###############################
# GRUPOS DE GOLPES SELECTIVOS #
###############################

#GM1 group
dwf.AddAttack("GM1","Dwf_g_18")
dwf.AddAttack("GM1","Dwf_g_15")

dwf.AttackTypeFlag("GM1",ATK_SEQUENTIAL)

#GM2 group
dwf.AddAttack("GM2","Dwf_g_14")
dwf.AddAttack("GM2","Dwf_g_13")

dwf.AttackTypeFlag("GM2",ATK_SEQUENTIAL)

#GM3 group
dwf.AddAttack("GM3","Dwf_g_16")
dwf.AddAttack("GM3","Dwf_g_11")

dwf.AttackTypeFlag("GM3",ATK_SEQUENTIAL)

#GM4 group
dwf.AddAttack("GM4","Dwf_g_12")
dwf.AddAttack("GM4","Dwf_g_17")

dwf.AttackTypeFlag("GM4",ATK_SEQUENTIAL)


#GAI meta-group
dwf.MetaAttack("GIAM","GI")
dwf.MetaAttack("GIAM","GA")
dwf.MetaAttack("GIAM","GM1")
dwf.MetaAttack("GIAM","GM2")
dwf.MetaAttack("GIAM","GM3")
dwf.MetaAttack("GIAM","GM4")


#GM meta-group
dwf.MetaAttack("GM","GM1")
dwf.MetaAttack("GM","GM2")
dwf.MetaAttack("GM","GM3")
dwf.MetaAttack("GM","GM4")

############################
# GRUPOS DE GOLPES FINALES #
############################

#GGF1
dwf.AddAttack("GGF1","Dwf_g_21")

#GGF2
dwf.AddAttack("GGF2","Dwf_g_22")

#GGF3
dwf.AddAttack("GGF3","Dwf_g_23")

#GGF4
dwf.AddAttack("GGF4","Dwf_g_26")

#GGF5
dwf.AddAttack("GGF5","Dwf_g_27")

#GGF meta-group
dwf.MetaAttack("GGF","GGF1")
dwf.MetaAttack("GGF","GGF2")
dwf.MetaAttack("GGF","GGF3")
dwf.MetaAttack("GGF","GGF4")
dwf.MetaAttack("GGF","GGF5")

###############################
# GRUPOS DE GOLPES ESPECIALES #
###############################

#GE
dwf.AddAttack("GE","Dwf_g_31")



######################################################
#
#        - Attacks themselves -
#
######################################################

# *Name of NEW attack (anm name itself , group name or metagroup)
# *Keys
#       R , L , F , B -> Control keys
#       A -> Attack 
#       D -> Defense(block)
#     
# -->Keys Modifiers
#       a+b . Simultaneous press
#       !c . Should not be pressed
#       &d . Should be already pressed
# *Previous Historial
#       "GA,GA,GM,GGF"
# *Previous NEGATIVE historial
#       +/- idem b4
#
#

#####################
# GOLPES INICIALES  #
#####################

#GI
dwf.AllowAttack("GI","A","","GIAM","")

#####################
# GOLPES ALEATORIOS #
#####################

#GAs

dwf.AllowAttack("GA","A","","","")

#####################
# GOLPES SELECTIVOS #
#####################

#GM1
dwf.AllowAttack("GM1","A+F","","","")
dwf.AllowAttack("GM1","&A+F","","","")
dwf.AllowAttack("GM1","&A+F","GIAM","","")


#GM2
dwf.AllowAttack("GM2","A+B","","","")
dwf.AllowAttack("GM2","&A+B","","","")					
dwf.AllowAttack("GM2","&A+B","GIAM","","")	

#GM3
dwf.AllowAttack("GM3","A+R","","","")
dwf.AllowAttack("GM3","&A+R","","","")					
dwf.AllowAttack("GM3","&A+R","GIAM","","")	

#GM4
dwf.AllowAttack("GM4","A+L","","","")
dwf.AllowAttack("GM4","&A+L","","","")				
dwf.AllowAttack("GM4","&A+L","GIAM","","")	

##############################
# CADENA DE GOLPES CON FINAL #
##############################


#GGF4
dwf.AllowAttack("GGF4","L+R","GM2,GM1","","")
dwf.AllowAttack("GGF4","&A+L+R","GM2,GM1","","")

#GGF2
dwf.AllowAttack("GGF2","B+R","GM4,GM1","","")
dwf.AllowAttack("GGF2","&A+B+R","GM4,GM1","","")

#GGF3
dwf.AllowAttack("GGF3","B+L","GM3,GM1","","")
dwf.AllowAttack("GGF3","&A+B+L","GM3,GM1","","")

#GGF1
dwf.AllowAttack("GGF1","F+B","GM3,GM4","","")
dwf.AllowAttack("GGF1","&A+F+B","GM3,GM4","","")

#GGF5
dwf.AllowAttack("GGF5","L+R","GM1,GM2","","")
dwf.AllowAttack("GGF5","&A+L+R","GM1,GM2","","")

###############################
# CADENA DE GOLPES ESPECIALES #
###############################

#GE1
dwf.AllowAttack("GE","&A","GGF4","","")

#GE2
dwf.AllowAttack("GE","&A","GGF2","","")

#GE3
dwf.AllowAttack("GGF2","F+B","GGF4","","")

#GE4
dwf.AllowAttack("GGF4","F+L","GGF2","","")









