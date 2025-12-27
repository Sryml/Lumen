######################################################
#
# Create sets of attacks
#
#        - Bar -
#
######################################################



import Bladex
import netgame

ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2


# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Bar","g_01","ATTACKING")
Bladex.SetActionEventTable("Bar","g_02","ATTACKING")
Bladex.SetActionEventTable("Bar","g_05","ATTACKING")
Bladex.SetActionEventTable("Bar","g_06","ATTACKING")
Bladex.SetActionEventTable("Bar","g_07","ATTACKING")
Bladex.SetActionEventTable("Bar","g_08","ATTACKING")
Bladex.SetActionEventTable("Bar","g_09","ATTACKING")
Bladex.SetActionEventTable("Bar","g_18","ATTACKING")
Bladex.SetActionEventTable("Bar","g_15","ATTACKING")
Bladex.SetActionEventTable("Bar","g_14","ATTACKING")
Bladex.SetActionEventTable("Bar","g_13","ATTACKING")
Bladex.SetActionEventTable("Bar","g_16","ATTACKING")
Bladex.SetActionEventTable("Bar","g_11","ATTACKING")
Bladex.SetActionEventTable("Bar","g_12","ATTACKING")
Bladex.SetActionEventTable("Bar","g_17","ATTACKING")
Bladex.SetActionEventTable("Bar","g_21","ATTACKING")
Bladex.SetActionEventTable("Bar","g_22","ATTACKING")
Bladex.SetActionEventTable("Bar","g_23","ATTACKING")
Bladex.SetActionEventTable("Bar","g_26","ATTACKING")
Bladex.SetActionEventTable("Bar","g_27","ATTACKING")
Bladex.SetActionEventTable("Bar","g_31","ATTACKING")

#Idem 2 handed weapons attacks
Bladex.SetActionEventTable("Bar","g2h_21_7","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_21_2","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_02kata","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_21_6kata","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_b7","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_08","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_28","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_s8kata","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_b6kata","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_s8","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_12","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_02","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_b6","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_11","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_01","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_13","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_12low","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_02low","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_b6low","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_01","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_b29","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_17","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_b7","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_s7","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_19","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_26_b6","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_26","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_earthpow","ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_back","ATTACKING")
Bladex.SetActionEventTable("Bar","g_axe08","ATTACKING")
Bladex.SetActionEventTable("Bar","g_axe18","ATTACKING")
Bladex.SetActionEventTable("Bar","g_axe28","ATTACKING")
Bladex.SetActionEventTable("Bar","g_axe01","ATTACKING")
Bladex.SetActionEventTable("Bar","g_axe02","ATTACKING")
Bladex.SetActionEventTable("Bar","g_axe12","ATTACKING")
Bladex.SetActionEventTable("Bar","g_axe13","ATTACKING")
Bladex.SetActionEventTable("Bar","g_axe08strong","ATTACKING")
Bladex.SetActionEventTable("Bar","g_axe32","ATTACKING")
Bladex.SetActionEventTable("Bar","g_axe21","ATTACKING")
Bladex.SetActionEventTable("Bar","g_axe34","ATTACKING")
Bladex.SetActionEventTable("Bar","g_axe111","ATTACKING")
Bladex.SetActionEventTable("Bar","g_axe211","ATTACKING")
Bladex.SetActionEventTable("Bar","g_axe_2katab6low","ATTACKING")
Bladex.SetActionEventTable("Bar","g_axe31","ATTACKING")
Bladex.SetActionEventTable("Bar","g_axe_26kata","ATTACKING")
Bladex.SetActionEventTable("Bar","g_axe_3s2","ATTACKING")
Bladex.SetActionEventTable("Bar","g_axe_b2kata","ATTACKING")
Bladex.SetActionEventTable("Bar","g_axe_32kata_b2","ATTACKING")
Bladex.SetActionEventTable("Bar","g_axe30","ATTACKING")
Bladex.SetActionEventTable("Bar","g_axe33","ATTACKING")
Bladex.SetActionEventTable("Bar","g_punch1","ATTACKING")
Bladex.SetActionEventTable("Bar","g_punch2","ATTACKING")
Bladex.SetActionEventTable("Bar","g_punch3","ATTACKING")
Bladex.SetActionEventTable("Bar","g_punch4","ATTACKING")
Bladex.SetActionEventTable("Bar","g_06lowkata_new","ATTACKING")
Bladex.SetActionEventTable("Bar","g_kick","ATTACKING")
Bladex.SetActionEventTable("Bar","g_magic","ATTACKING")
Bladex.SetActionEventTable("Bar","g_magic2","ATTACKING")

# clumsy attacks
Bladex.SetActionEventTable("Bar","g_bad_axe", "ATTACKING_NOMOVE")
Bladex.SetActionEventTable("Bar","g_bad_spear", "ATTACKING_NOMOVE")
Bladex.SetActionEventTable("Bar","g_bad_sword", "ATTACKING_NOMOVE")
Bladex.SetActionEventTable("Bar","g_bad_no", "ATTACKING_NOMOVE")
Bladex.SetActionEventTable("Bar","g_bad_1h", "ATTACKING_NOMOVE")

# Draw attacks
Bladex.SetActionEventTable("Bar","g_draw_rlx", "ATTACKING")
Bladex.SetActionEventTable("Bar","g_draw_run", "ATTACKING")


#Dodge->attacks
Bladex.SetActionEventTable("Bar","g2h_d_r", "ATTACKING")
Bladex.SetActionEventTable("Bar","g2h_d_l", "ATTACKING")
Bladex.SetActionEventTable("Bar","g_d_r_axe", "ATTACKING")
Bladex.SetActionEventTable("Bar","g_d_l_axe", "ATTACKING")

# Predeclare & link all my dodges into DODGES action event tables
Bladex.SetActionEventTable("Bar","D_r", "DODGING")
Bladex.SetActionEventTable("Bar","D_l", "DODGING")
Bladex.SetActionEventTable("Bar","D_b", "DODGING")


bar=Bladex.GetCharType("Barbarian_N","Bar")

#
#Dodge groups
#

#Dodges themselves
bar.AddAttack("DR","D_r")
bar.AttackTypeFlag("DR",ATK_UNIQUE) 

bar.AddAttack("DL","D_l")
bar.AttackTypeFlag("DL",ATK_UNIQUE) 

bar.AddAttack("DB","D_b")
bar.AttackTypeFlag("DB",ATK_UNIQUE) 

#Dodge attacks
bar.AddAttack("DR_G_2H","g2h_d_r")
bar.AssignTrail("DR_G_2H","","EstelaAmarilla1")
bar.AddLevels("g2h_d_r",2,40)
bar.AttackTypeFlag("DR",ATK_UNIQUE) 

bar.AddAttack("DL_G_2H","g2h_d_l")
bar.AssignTrail("DL_G_2H","","EstelaAmarilla1")
bar.AddLevels("g2h_d_l",2,40)
bar.AttackTypeFlag("DL",ATK_UNIQUE) 

bar.AddAttack("DR_G_AXE","g_d_r_axe")
bar.AssignTrail("DR_G_AXE","","EstelaAmarilla1")
bar.AddLevels("g_d_r_axe",2,40)
bar.AttackTypeFlag("DR",ATK_UNIQUE) 

bar.AddAttack("DL_G_AXE","g_d_l_axe")
bar.AssignTrail("DL_G_AXE","","EstelaAmarilla1")
bar.AddLevels("g_d_l_axe",2,40)
bar.AttackTypeFlag("DL",ATK_UNIQUE) 


#GI "group"
bar.AddAttack("GI_1H","Bar_g_07")
bar.AttackWindow("Bar_g_07",0.010,0.900,"GI_1H_Window")
bar.AddLevels("Bar_g_07",0,40)
#bar.AttackTypeFlag("GI_1H",ATK_UNIQUE) #If only one attack given , UNIQUE flag is applied

###############################
# GRUPOS DE GOLPES SELECTIVOS #
###############################

#GM1 group
bar.AddAttack("GM1_1H","Bar_g_18")
bar.AddLevels("Bar_g_18",0,40)

#GM2 group
bar.AddAttack("GM2_1H","Bar_g_17")
bar.AddLevels("Bar_g_17",0,40)

#GM3 group
bar.AddAttack("GM3_1H","Bar_g_16")
bar.AddLevels("Bar_g_16",0,40)

#GM4 group
bar.AddAttack("GM4_1H","Bar_g_11")
bar.AddLevels("Bar_g_11",0,40)

#COMBO QUEENSWORD
bar.AddAttack("GM5_1H","Bar_g_06lowkata_new")
bar.AttackWindow("Bar_g_06lowkata_new",0.001,0.900,"GM5_1H_Window")
bar.AssignTrail("GM5_1H","","EstelaRoja1")
bar.AddLevels("Bar_g_06lowkata_new",10,40)


#GI meta-group
bar.MetaAttack("GIM_1H","GI_1H")
bar.MetaAttack("GIM_1H","GM1_1H")
bar.MetaAttack("GIM_1H","GM2_1H")
bar.MetaAttack("GIM_1H","GM3_1H")
bar.MetaAttack("GIM_1H","GM4_1H")
bar.MetaAttack("GIM_1H","GM5_1H")


#GM meta-group
bar.MetaAttack("GM","GM1_1H")
bar.MetaAttack("GM","GM2_1H")
bar.MetaAttack("GM","GM3_1H")
bar.MetaAttack("GM","GM4_1H")
bar.MetaAttack("GM","GM5_1H")


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
# GOLPES SELECTIVOS #
#####################

#GM1
bar.AllowAttack("GM1_1H","A+F","","GM,GM","","1H")
bar.AllowAttack("GM1_1H","&A+F","","GM,GM","","1H")

#GM2
bar.AllowAttack("GM2_1H","A+R","","GM,GM","","1H")
bar.AllowAttack("GM2_1H","&A+R","","GM,GM","","1H")					

#GM3
bar.AllowAttack("GM3_1H","A+L","","GM,GM","","1H")
bar.AllowAttack("GM3_1H","&A+L","","GM,GM","","1H")	

#COMBO QUEENSWORD
bar.AllowAttack("GM5_1H","R+B","GM3_1H","","","QueenSword")					

#GM4
bar.AllowAttack("GM4_1H","A+B","","GM,GM","","1H")
bar.AllowAttack("GM4_1H","&A+B","","GM,GM","","1H")


#GI
bar.AllowAttack("GI_1H","A","","GIM_1H","GIM_1H_Window","1H")




#################################################################################################
#################################################################################################
#################################################################################################
#
#
#
#  2 handed weapons attacks
#
#
#
#################################################################################################
#################################################################################################
#################################################################################################

#GI "group"
bar.AddAttack("GI_2H","Bar_g2h_08")
bar.AttackWindow("Bar_g2h_08",0.400,0.535,"GI_2H_Window")
bar.AddLevels("Bar_g2h_08",0,40)

#COMBO1 "group"
bar.AddAttack("GM1_2H","Bar_g2h_b6kata")
bar.AttackWindow("Bar_g2h_b6kata",0.443,0.569,"GM1_2H_Window")
bar.AddLevels("Bar_g2h_b6kata",0,40)

#COMBO1 "group"
bar.AddAttack("GM2_2H","Bar_g2h_b7")
bar.AttackWindow("Bar_g2h_b7",0.297,0.418,"GM2_2H_Window")
bar.AssignTrail("GM2_2H","","EstelaAmarilla1")
bar.AddLevels("Bar_g2h_b7",7,40)


#COMBO2 "group"
bar.AddAttack("GM7_2H","Bar_g2h_s7")
bar.AttackWindow("Bar_g2h_s7",0.402,0.662,"GM7_2H_Window")
bar.AddLevels("Bar_g2h_s7",0,40)

#COMBO2 "group"
bar.AddAttack("GM5_2H","Bar_g2h_02kata")
bar.AttackWindow("Bar_g2h_02kata",0.373,0.548,"GM5_2H_Window")
bar.AssignTrail("GM5_2H","","EstelaAmarilla1")
bar.AddLevels("Bar_g2h_02kata",1,40)


#COMBO3 "group"
bar.AddAttack("GM4_2H","Bar_g2h_11")
bar.AttackWindow("Bar_g2h_11",0.272,0.502,"GM4_2H_Window")
bar.AddLevels("Bar_g2h_11",0,40)

#COMBO3 "group"
bar.AddAttack("GM8_2H","Bar_g2h_01")
bar.AttackWindow("Bar_g2h_01",0.195,0.427,"GM8_2H_Window")
bar.AssignTrail("GM8_2H","","EstelaAmarilla1")
bar.AddLevels("Bar_g2h_01",5,40)


#COMBO4 "group"
bar.AddAttack("GM10_2H","Bar_g2h_12low")
bar.AttackWindow("Bar_g2h_12low",0.312,0.595,"GM10_2H_Window")
bar.AddLevels("Bar_g2h_12low",0,40)

#COMBO4 "group"
bar.AddAttack("GM11_2H","Bar_g2h_02low")
bar.AttackWindow("Bar_g2h_02low",0.280,0.525,"GM11_2H_Window")
bar.AssignTrail("GM11_2H","","EstelaAmarilla1")
bar.AddLevels("Bar_g2h_02low",6,40)


#COMBO CHAOSWORD
bar.AddAttack("GM6_2H","Bar_g2h_b6")
bar.AttackWindow("Bar_g2h_b6",0.363,0.508,"GM6_2H_Window")
bar.AssignTrail("GM6_2H","","EstelaRoja1")
bar.AddLevels("Bar_g2h_b6",4,40)

#COMBO4 DEATHSWORD
bar.AddAttack("GM12_2H","Bar_g2h_b6low")
bar.AttackWindow("Bar_g2h_b6low",0.338,0.470,"GM12_2H_Window")
bar.AssignTrail("GM12_2H","","EstelaRoja1")
bar.AddLevels("Bar_g2h_b6low",7,40)

#COMBO BIGSWORD2 "group"
bar.AddAttack("GM9_2H","Bar_g2h_b29")
bar.AttackWindow("Bar_g2h_b29",0.304,0.557,"GM9_2H_Window")
bar.AssignTrail("GM9_2H","","EstelaRoja1")
bar.AddLevels("Bar_g2h_b29",14,40)

#COMBO LONGSWORD "group"
bar.AddAttack("GM41_2H","Bar_g2h_13")
bar.AttackWindow("Bar_g2h_13",0.366,0.572,"GM41_2H_Window")
bar.AssignTrail("GM41_2H","","EstelaRoja1")
bar.AddLevels("Bar_g2h_13",9,40)

#COMBOFLATSWORD "group"
bar.AddAttack("GM42_2H","Bar_g2h_28")
bar.AttackWindow("Bar_g2h_28",0.427,0.512,"GM42_2H_Window")
bar.AssignTrail("GM42_2H","","EstelaRoja1")
bar.AddLevels("Bar_g2h_28",13,40)

#COMBOALFANJE "group"
bar.AddAttack("GM15_2H","Bar_g2h_s8")
bar.AttackWindow("Bar_g2h_s8",0.345,0.567,"GM15_2H_Window")
bar.AssignTrail("GM15_2H","","EstelaRoja1")
bar.AddLevels("Bar_g2h_s8",10,40)

#COMBOFIREBIGSWORD1 "group"
bar.AddAttack("GM44_2H","Bar_g2h_21_2")
bar.AttackWindow("Bar_g2h_21_2",0.186,0.610,"GM44_2H_Window")
bar.AssignTrail("GM44_2H","","EstelaRoja1")
bar.AddLevels("Bar_g2h_21_2",12,40)

#COMBOFIREBIGSWORD2 "group"
bar.AddAttack("GM45_2H","Bar_g2h_earthpow")
bar.AttackWindow("Bar_g2h_earthpow",0.620,0.732,"GM45_2H_Window")
bar.AssignTrail("GM45_2H","","EstelaRoja1")
bar.AddLevels("Bar_g2h_earthpow",17,40)

#COMBOSAWSWORD "group"
bar.AddAttack("GM40_2H","Bar_g2h_21_7")
bar.AttackWindow("Bar_g2h_21_7",0.534,0.772,"GM40_2H_Window")
bar.AssignTrail("GM40_2H","","EstelaRoja1")

if netgame.GetNetState() == 1:
	bar.AddLevels("Bar_g2h_21_7",18,18)
else:
	bar.AddLevels("Bar_g2h_21_7",18,40)



#COMBORAPIDOEXTRA1 "group"
bar.AddAttack("GM23_2H","Bar_g2h_21_6kata")
bar.AttackWindow("Bar_g2h_21_6kata",0.328,0.731,"GM23_2H_Window")
bar.AssignTrail("GM23_2H","","EstelaAmarilla1")
bar.AddLevels("Bar_g2h_21_6kata",8,40)

#COMBORAPIDOEXTRA2 "group"
bar.AddAttack("GM24_2H","Bar_g2h_26_b6")
bar.AttackWindow("Bar_g2h_26_b6",0.329,0.713,"GM24_2H_Window")
bar.AssignTrail("GM24_2H","","EstelaRoja1")
bar.AddLevels("Bar_g2h_26_b6",11,40)

#COMBOATAQUE180 "group"
bar.AddAttack("GM46_2H","Bar_g2h_back")
bar.AssignTrail("GM46_2H","","EstelaAmarilla1")
bar.AddLevels("Bar_g2h_back",3,40)





#GOLPEINICIOHACHA "group"
bar.AddAttack("GI_AXE","Bar_g_axe08")
bar.AttackWindow("Bar_g_axe08",0.218,0.435,"GI_AXE_Window")
bar.AddLevels("Bar_g_axe08",0,40)


#COMBOHACHA1 "group"
bar.AddAttack("GM17_AXE","Bar_g_axe18")
bar.AttackWindow("Bar_g_axe18",0.350,0.537,"GM17_AXE_Window")
bar.AddLevels("Bar_g_axe18",0,40)

#COMBOHACHA1 "group"
bar.AddAttack("GM18_AXE","Bar_g_axe01")
bar.AttackWindow("Bar_g_axe01",0.194,0.439,"GM18_AXE_Window")
bar.AssignTrail("GM18_AXE","","EstelaAmarilla1")
bar.AddLevels("Bar_g_axe01",7,40)


#COMBOHACHA2 "group"
bar.AddAttack("GM19_AXE","Bar_g_axe02")
bar.AttackWindow("Bar_g_axe02",0.183,0.483,"GM19_AXE_Window")
bar.AddLevels("Bar_g_axe02",0,40)


#COMBOHACHA3 "group"
bar.AddAttack("GM21_AXE","Bar_g_axe13")
bar.AttackWindow("Bar_g_axe13",0.348,0.600,"GM21_AXE_Window")
bar.AddLevels("Bar_g_axe13",0,40)


#COMBOHACHA4 "group"
bar.AddAttack("GM28_AXE","Bar_g_axe111")
bar.AttackWindow("Bar_g_axe111",0.299,0.604,"GM28_AXE_Window")
bar.AddLevels("Bar_g_axe111",0,40)


#COMBOALEATORIOEXTRA "group"
bar.AddAttack("GM31_AXE","Bar_g_axe31")
bar.AttackWindow("Bar_g_axe31",0.690,0.884,"GM31_AXE_Window")
bar.AssignTrail("GM31_AXE","","EstelaAmarilla1")
bar.AddLevels("Bar_g_axe31",10,40)


#COMBO ECLIPSE
bar.AddAttack("GM29_AXE","Bar_g_axe211")
bar.AttackWindow("Bar_g_axe211",0.411,0.703,"GM29_AXE_Window")
bar.AssignTrail("GM29_AXE","","EstelaRoja1")
bar.AddLevels("Bar_g_axe211",6,40)

#COMBO GUADANYA
bar.AddAttack("GM32_AXE","Bar_g_axe33")
bar.AttackWindow("Bar_g_axe33",0.001,0.900,"GM32_AXE_Window")
bar.AssignTrail("GM32_AXE","","EstelaRoja1")
bar.AddLevels("Bar_g_axe33",8,40)

#COMBO HACHA2HOJAS
bar.AddAttack("GM26_AXE","Bar_g_axe34")
bar.AttackWindow("Bar_g_axe34",0.414,0.607,"GM26_AXE_Window")
bar.AssignTrail("GM26_AXE","","EstelaRoja1")
bar.AddLevels("Bar_g_axe34",11,40)

#COMBO RHINOCLUB
bar.AddAttack("GM20_AXE","Bar_g_axe12")
bar.AttackWindow("Bar_g_axe12",0.235,0.564,"GM20_AXE_Window")
bar.AssignTrail("GM20_AXE","","EstelaRoja1")
if netgame.GetNetState() == 1:
	bar.AddLevels("Bar_g_axe12",15,15)
else:
	bar.AddLevels("Bar_g_axe12",15,40)

#COMBO HACHARRAJADA
bar.AddAttack("GM27_AXE","Bar_g_axe32")
bar.AttackWindow("Bar_g_axe32",0.452,0.614,"GM27_AXE_Window")
bar.AssignTrail("GM27_AXE","","EstelaRoja1")
if netgame.GetNetState() == 1:
	bar.AddLevels("Bar_g_axe32",17,17)
else:
	bar.AddLevels("Bar_g_axe32",17,40)

#COMBOICEAXE1 "group"
bar.AddAttack("GM36_AXE","Bar_g_axe30")
bar.AttackWindow("Bar_g_axe30",0.650,0.859,"GM36_AXE_Window")
bar.AssignTrail("GM36_AXE","","EstelaAzul1")
bar.AddLevels("Bar_g_axe30",12,40)




#GOLPESINARMA1 "group"
bar.AddAttack("GM37_NO","Bar_g_punch4")
bar.AddLevels("Bar_g_punch4",0,40)

#GOLPESINARMA2 "group"
bar.AddAttack("GM38_NO","Bar_g_punch2")
bar.AddLevels("Bar_g_punch2",0,40)

#GOLPESINARMA3 "group"
bar.AddAttack("GM39_NO","Bar_g_punch3")
bar.AddLevels("Bar_g_punch3",0,40)


#GOLPE Torpe Lanza
bar.AddAttack("GM47_SP","Bar_g_bad_spear")
bar.AddLevels("Bar_g_bad_spear",0,40)


#COMBO BLADEESTELA
bar.AddAttack("GM60_2H","Bar_g_magic2")
bar.AssignTrail("GM60_2H","","EstelaRoja1")
bar.AddLevels("Bar_g_magic2",18,40)

#COMBO BLADECONCENTRACION
bar.AddAttack("GM61_2H","Bar_g_magic")
bar.AssignTrail("GM61_2H","","EstelaRoja1")
bar.AddLevels("Bar_g_magic",19,40)

############################################################

#GAI meta-group
bar.MetaAttack("GIM_2H","GI_2H")
bar.MetaAttack("GIM_AXE","GI_AXE")
bar.MetaAttack("GIM_2H","GM1_2H")
bar.MetaAttack("GIM_2H","GM2_2H")
bar.MetaAttack("GIM_2H","GM4_2H")
bar.MetaAttack("GIM_2H","GM5_2H")
bar.MetaAttack("GIM_2H","GM6_2H")
bar.MetaAttack("GIM_2H","GM7_2H")
bar.MetaAttack("GIM_2H","GM8_2H")
bar.MetaAttack("GIM_2H","GM9_2H")
bar.MetaAttack("GIM_2H","GM10_2H")
bar.MetaAttack("GIM_2H","GM11_2H")
bar.MetaAttack("GIM_2H","GM12_2H")
bar.MetaAttack("GIM_2H","GM15_2H")
bar.MetaAttack("GIM_AXE","GM17_AXE")
bar.MetaAttack("GIM_AXE","GM18_AXE")
bar.MetaAttack("GIM_AXE","GM19_AXE")
bar.MetaAttack("GIM_AXE","GM20_AXE")
bar.MetaAttack("GIM_AXE","GM21_AXE")
bar.MetaAttack("GIM_2H","GM23_2H")
bar.MetaAttack("GIM_2H","GM24_2H")
bar.MetaAttack("GIM_AXE","GM26_AXE")
bar.MetaAttack("GIM_AXE","GM27_AXE")
bar.MetaAttack("GIM_AXE","GM28_AXE")
bar.MetaAttack("GIM_AXE","GM29_AXE")
bar.MetaAttack("GIM_AXE","GM31_AXE")
bar.MetaAttack("GIM_AXE","GM32_AXE")
bar.MetaAttack("GIM_AXE","GM36_AXE")
bar.MetaAttack("GIM_NO","GM37_NO")
bar.MetaAttack("GIM_NO","GM38_NO")
bar.MetaAttack("GIM_NO","GM39_NO")
bar.MetaAttack("GIM_2H","GM40_2H")
bar.MetaAttack("GIM_2H","GM41_2H")
bar.MetaAttack("GIM_2H","GM42_2H")
bar.MetaAttack("GIM_2H","GM44_2H")
bar.MetaAttack("GIM_2H","GM45_2H")
bar.MetaAttack("GIM_2H","GM46_2H")
bar.MetaAttack("GIM_SP","GM47_SP")
bar.MetaAttack("GIM_2H","GM60_2H")
bar.MetaAttack("GIM_2H","GM61_2H")

bar.MetaAttack("GOLPEINICIAL","GI_2H")
bar.MetaAttack("GOLPEINICIALHACHA","GI_AXE")

bar.MetaAttack("COMBO1","GM1_2H")
bar.MetaAttack("COMBO1","GM2_2H")

bar.MetaAttack("COMBO1","GM4_2H")
bar.MetaAttack("COMBO1","GM5_2H")
bar.MetaAttack("COMBO1","GM6_2H")

bar.MetaAttack("COMBO1","GM7_2H")
bar.MetaAttack("COMBO1","GM8_2H")
bar.MetaAttack("COMBO1","GM9_2H")

bar.MetaAttack("COMBO1","GM10_2H")
bar.MetaAttack("COMBO1","GM11_2H")
bar.MetaAttack("COMBO1","GM12_2H")

bar.MetaAttack("COMBO1","GM17_AXE")
bar.MetaAttack("COMBO1","GM18_AXE")

bar.MetaAttack("COMBO1","GM19_AXE")
bar.MetaAttack("COMBO1","GM20_AXE")

bar.MetaAttack("COMBO1","GM21_AXE")
bar.MetaAttack("COMBO1","GM26_AXE")
bar.MetaAttack("COMBO1","GM27_AXE")
bar.MetaAttack("COMBO1","GM28_AXE")
bar.MetaAttack("COMBO1","GM29_AXE")
bar.MetaAttack("COMBO1","GM31_AXE")
bar.MetaAttack("COMBO1","GM32_AXE")
bar.MetaAttack("COMBO1","GM36_AXE")
bar.MetaAttack("COMBO1","GM37_NO")
bar.MetaAttack("COMBO1","GM38_NO")
bar.MetaAttack("COMBO1","GM39_NO")

bar.MetaAttack("COMBOLONGSWORD","GM41_2H")
bar.MetaAttack("COMBOFLATSWORD","GM42_2H")
bar.MetaAttack("COMBOALFANJE","GM15_2H")
bar.MetaAttack("COMBOFIREBIGSWORD","GM44_2H")
bar.MetaAttack("COMBOFIREBIGSWORD","GM45_2H")

bar.MetaAttack("COMBO1","GM23_2H")
bar.MetaAttack("COMBO1","GM24_2H")
bar.MetaAttack("COMBOEXTRA1","GM31_AXE")
bar.MetaAttack("COMBO1","GM40_2H")
bar.MetaAttack("COMBO1","GM46_2H")
bar.MetaAttack("COMBO1","GM47_SP")
bar.MetaAttack("COMBO1","GM60_2H")
bar.MetaAttack("COMBO1","GM61_2H")



###########################################################

#GOLPEATAQUE180
bar.AllowAttack("GM46_2H","B+L+R","","","","2W")

#Golpes en esquiva
bar.AllowAttack("DL_G_2H","A","DL","","","2W")

bar.AllowAttack("DR_G_2H","A","DR","","","2W")

bar.AllowAttack("DB_G_2H","A","DB","","","2W")

bar.AllowAttack("DL_G_AXE","A","DL","","","AXE")

bar.AllowAttack("DR_G_AXE","A","DR","","","AXE")

bar.AllowAttack("DB_G_AXE","A","DB","","","AXE")

#COMBO ESTELA
bar.AllowAttack("GM60_2H","&B","GI_2H","","","BladeSword2Barbarian")

#COMBO CONCENTRACION
bar.AllowAttack("GM61_2H","&A+F","GI_2H","","","BladeSword2Barbarian")


#GOLPE torpe Lanza
bar.AllowAttack("GM47_SP","A","","COMBO1","","SP")

#GOLPESINARMA1
bar.AllowAttack("GM37_NO","A","","COMBO1","","NO")

#GOLPESINARMA2
bar.AllowAttack("GM38_NO","A+B","","COMBO1","","NO")
bar.AllowAttack("GM38_NO","&A+B","","COMBO1","","NO")

#GOLPESINARMA3
bar.AllowAttack("GM39_NO","A+F","","COMBO1","","NO")
bar.AllowAttack("GM39_NO","&A+F","","COMBO1","","NO")

#COMBO FLATSWORD1
bar.AllowAttack("GM42_2H","R+L","GI_2H","","GI_2H_Window","FlatSword")

#COMBOFIREBIGSWORD
bar.AllowAttack("GM44_2H","B","GM23_2H","","GM23_2H_Window","FireBigSword")

#COMBOFIREBIGSWORD
bar.AllowAttack("GM45_2H","R+L","GM24_2H","","GM24_2H_Window","FireBigSword")




#COMBORAPIDOEXTRA2
bar.AllowAttack("GM24_2H","A","GM23_2H","","","2W")

#COMBORAPIDOEXTRA1
bar.AllowAttack("GM23_2H","F","GI_2H","GM23_2H","","2W")


#COMBO TECLA ARRIBA2
bar.AllowAttack("GM2_2H","A+F","GM1_2H","","GM1_2H_Window","2W")
bar.AllowAttack("GM2_2H","&A+F","GM1_2H","","GM1_2H_Window","2W")

#COMBO TECLA ARRIBA1
bar.AllowAttack("GM1_2H","A+F","","GM1_2H","GM2_2H_Window","2W")
bar.AllowAttack("GM1_2H","&A+F","","GM1_2H","GM2_2H_Window","2W")

#COMBO CHAOSWORD
bar.AllowAttack("GM6_2H","B","GM1_2H","","GM1_2H_Window","Chaosword")
bar.AllowAttack("GM6_2H","&B","GM1_2H","","GM1_2H_Window","Chaosword")

#COMBO DEATHSWORD
bar.AllowAttack("GM12_2H","F+B","GM1_2H","","GM1_2H_Window","DeathSword")

#COMBO BIGSWORD2
bar.AllowAttack("GM9_2H","B","GM1_2H","","","BigSword")

#COMBO SAWSWORD1
bar.AllowAttack("GM40_2H","R+L","GM1_2H","","GM1_2H_Window","SawSword")




#COMBO TECLA DERECHA2
bar.AllowAttack("GM5_2H","A+R","GM4_2H","","GM4_2H_Window","2W")
bar.AllowAttack("GM5_2H","&A+R","GM4_2H","","GM4_2H_Window","2W")

#COMBO TECLA DERECHA1
bar.AllowAttack("GM4_2H","A+R","","GM4_2H","GM5_2H_Window","2W")
bar.AllowAttack("GM4_2H","&A+R","","GM4_2H","GM5_2H_Window","2W")



#COMBO TECLA IZQUIERDA2
bar.AllowAttack("GM8_2H","A+L","GM7_2H","","GM7_2H_Window","2W")
bar.AllowAttack("GM8_2H","&A+L","GM7_2H","","GM7_2H_Window","2W")

#COMBO TECLA IZQUIERDA1
bar.AllowAttack("GM7_2H","A+L","","GM7_2H","GM8_2H_Window","2W")
bar.AllowAttack("GM7_2H","&A+L","","GM7_2H","GM8_2H_Window","2W")

#COMBO LONGSWORD1
bar.AllowAttack("GM41_2H","R","GM7_2H","","","LongSword")



#COMBO TECLA ABAJO2
bar.AllowAttack("GM11_2H","A+B","GM10_2H","","GM10_2H_Window","2W")
bar.AllowAttack("GM11_2H","&A+B","GM10_2H","","GM10_2H_Window","2W")

#COMBO TECLA ABAJO1
bar.AllowAttack("GM10_2H","A+B","","GM10_2H","GM11_2H_Window","2W")
bar.AllowAttack("GM10_2H","&A+B","","GM10_2H","GM11_2H_Window","2W")

#COMBO ALFANJE1
bar.AllowAttack("GM15_2H","F","GM11_2H","","","Alfanje")


#GI
bar.AllowAttack("GI_2H","A","","GIM_2H","GI_2H_Window","2W")



#COMBOALEATORIOEXTRA1
bar.AllowAttack("GM31_AXE","L+R","GM17_AXE","","GM17_AXE_Window","AXE")

#COMBOICEAXE
bar.AllowAttack("GM36_AXE","B+L","GI_AXE","","GI_AXE_Window","IceAxe")



#COMBOHACHA TECLA ARRIBA2
bar.AllowAttack("GM18_AXE","A+F","GM17_AXE","","GM17_AXE_Window","AXE")
bar.AllowAttack("GM18_AXE","&A+F","GM17_AXE","","GM17_AXE_Window","AXE")

#COMBOHACHA TECLA ARRIBA1
bar.AllowAttack("GM17_AXE","A+F","","GM17_AXE","GM18_AXE_Window","AXE")
bar.AllowAttack("GM17_AXE","&A+F","","GM17_AXE","GM18_AXE_Window","AXE")



#COMBOHACHA TECLA DERECHA1
bar.AllowAttack("GM19_AXE","A+R","","GM19_AXE","","AXE")
bar.AllowAttack("GM19_AXE","&A+R","","GM19_AXE","","AXE")

#COMBO GUADANYA
bar.AllowAttack("GM32_AXE","A+R","GM19_AXE","","","Guadanya")
bar.AllowAttack("GM32_AXE","&A+R","GM19_AXE","","","Guadanya")

#COMBO HACHARRAJADA
bar.AllowAttack("GM27_AXE","B+L","GM19_AXE","","","Hacharrajada")




#COMBOHACHA TECLA IZQUIERDA1
bar.AllowAttack("GM21_AXE","A+L","","GM21_AXE","","AXE")
bar.AllowAttack("GM21_AXE","&A+L","","GM21_AXE","","AXE")

#COMBO RHINOCLUB
bar.AllowAttack("GM20_AXE","A+L","GM21_AXE","","","RhinoClub")
bar.AllowAttack("GM20_AXE","&A+L","GM21_AXE","","","RhinoClub")

#COMBO HACHA2HOJAS
bar.AllowAttack("GM26_AXE","F+R","GM21_AXE","","","Hacha2hojas")


#COMBO ECLIPSE
bar.AllowAttack("GM29_AXE","A+B","GM28_AXE","","GM28_AXE_Window","Eclipse")
bar.AllowAttack("GM29_AXE","&A+B","GM28_AXE","","GM28_AXE_Window","Eclipse")

#COMBOHACHA TECLA ABAJO1
bar.AllowAttack("GM28_AXE","A+B","","GM28_AXE","","AXE")
bar.AllowAttack("GM28_AXE","&A+B","","GM28_AXE","","AXE")



#GI
bar.AllowAttack("GI_AXE","A","","GIM_AXE","GI_AXE_Window","AXE")