######################################################
#
# Create sets of attacks
#
#        - KGT -
#
######################################################



import Bladex


ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2



# Predeclare & link all my combos into ATTACKING action event tables
Bladex.SetActionEventTable("Knight","g_08","ATTACKING")
Bladex.SetActionEventTable("Knight","g_01","ATTACKING")
Bladex.SetActionEventTable("Knight","g_02","ATTACKING")
Bladex.SetActionEventTable("Knight","g_05","ATTACKING")
Bladex.SetActionEventTable("Knight","g_06","ATTACKING")
Bladex.SetActionEventTable("Knight","g_07","ATTACKING")
Bladex.SetActionEventTable("Knight","g_09","ATTACKING")
Bladex.SetActionEventTable("Knight","g_01a","ATTACKING")
Bladex.SetActionEventTable("Knight","g_02a","ATTACKING")
Bladex.SetActionEventTable("Knight","g_05a","ATTACKING")
Bladex.SetActionEventTable("Knight","g_06a","ATTACKING")
Bladex.SetActionEventTable("Knight","g_07a","ATTACKING")
Bladex.SetActionEventTable("Knight","g_09a","ATTACKING")
Bladex.SetActionEventTable("Knight","g_13","ATTACKING")
Bladex.SetActionEventTable("Knight","g_14","ATTACKING")
Bladex.SetActionEventTable("Knight","g_16","ATTACKING")
Bladex.SetActionEventTable("Knight","g_17","ATTACKING")
Bladex.SetActionEventTable("Knight","g_21","ATTACKING")
Bladex.SetActionEventTable("Knight","g_22","ATTACKING")
Bladex.SetActionEventTable("Knight","g_23","ATTACKING")
Bladex.SetActionEventTable("Knight","g_26","ATTACKING")
Bladex.SetActionEventTable("Knight","g_27","ATTACKING")
Bladex.SetActionEventTable("Knight","g_31","ATTACKING")
Bladex.SetActionEventTable("Knight","g_magic","ATTACKING")
Bladex.SetActionEventTable("Knight","g_magic2","ATTACKING")

Bladex.SetActionEventTable("Knight","g_08_new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_01_7_new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_01_new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_18_11_22_new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_07_new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_s3_new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_12_new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_02_new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_12_7_s1new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_sb25_new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_b06_new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_19_bs1_new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_01low_new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_22lowkata_new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_s28kata_new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_06lowkata_new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_09_07_s6low_new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_28new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_b32kata_new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_3s9_6new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_s19_new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_29_3new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_21_6_s8new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_32_5_3new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_27kata_new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_s22low_new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_22kata_23_new","ATTACKING")
Bladex.SetActionEventTable("Knight","g_back","ATTACKING")

Bladex.SetActionEventTable("Knight","g_punch1","ATTACKING")
Bladex.SetActionEventTable("Knight","g_punch2","ATTACKING")
Bladex.SetActionEventTable("Knight","g_kick","ATTACKING")

# clumsy attacks
Bladex.SetActionEventTable("Knight","g_bad_axe", "ATTACKING_NOMOVE")
Bladex.SetActionEventTable("Knight","g_bad_spear", "ATTACKING_NOMOVE")
Bladex.SetActionEventTable("Knight","g_bad_sword", "ATTACKING_NOMOVE")
Bladex.SetActionEventTable("Knight","g_bad_no", "ATTACKING_NOMOVE")
Bladex.SetActionEventTable("Knight","g_bad_1h", "ATTACKING_NOMOVE")
Bladex.SetActionEventTable("Knight","g_bad_sword2","ATTACKING_NOMOVE")
Bladex.SetActionEventTable("Knight","g_bad_sword3","ATTACKING_NOMOVE")
Bladex.SetActionEventTable("Knight","g_bad_spear2","ATTACKING_NOMOVE")

# Draw attacks
Bladex.SetActionEventTable("Knight","g_draw_rlx", "ATTACKING")
Bladex.SetActionEventTable("Knight","g_draw_run", "ATTACKING")

#Dodge->attacks
Bladex.SetActionEventTable("Knight","g_d_r", "ATTACKING")
Bladex.SetActionEventTable("Knight","g_d_l", "ATTACKING")


# Predeclare & link all my dodges into DODGES action event tables
Bladex.SetActionEventTable("Knight","D_r", "DODGING")
Bladex.SetActionEventTable("Knight","D_l", "DODGING")
Bladex.SetActionEventTable("Knight","D_b", "DODGING")


#########################################################################################33


kgt=Bladex.GetCharType("Knight_N","Kgt_N")


#
#Dodge groups
#

#Dodges themselves
kgt.AddAttack("DR","D_r")
#kgt.AttackWindow("D_r",0.315,0.510,"GI_1H_Window") # O lo que sea
kgt.AttackTypeFlag("DR",ATK_UNIQUE) 

kgt.AddAttack("DL","D_l")
kgt.AttackTypeFlag("DL",ATK_UNIQUE) 

kgt.AddAttack("DB","D_b")
kgt.AttackTypeFlag("DB",ATK_UNIQUE) 

#Dodge attacks
kgt.AddAttack("DR_G_1H","g_d_r")
kgt.AssignTrail("DR_G_1H","","EstelaAmarilla1")
kgt.AddLevels("g_d_r",1,40)
kgt.AttackTypeFlag("DR",ATK_UNIQUE) 

kgt.AddAttack("DL_G_1H","g_d_l")
kgt.AssignTrail("DL_G_1H","","EstelaAmarilla1")
kgt.AddLevels("g_d_l",1,40)
kgt.AttackTypeFlag("DL",ATK_UNIQUE) 

#kgt.AddAttack("DB_G_1H","D_b_g")
#kgt.AttackTypeFlag("DB",ATK_UNIQUE) 




#GI "group"
kgt.AddAttack("GI_1H","Kgt_g_08_new")
kgt.AttackWindow("Kgt_g_08_new",0.001,0.900,"GI_1H_Window")
#kgt.AttackTypeFlag("GI_1H",ATK_UNIQUE) #If only one attack given , UNIQUE flag is applied


###############################
# GRUPOS DE GOLPES SELECTIVOS #
###############################

#COMBO1 group
kgt.AddAttack("GM1_1H","Kgt_g_07_new")
kgt.AttackWindow("Kgt_g_07_new",0.309,0.531,"GM1_1H_Window")
kgt.AddLevels("Kgt_g_07_new",0,40)
kgt.AddEnergyLevel("Kgt_g_07_new", 0)

#COMBO1 group
kgt.AddAttack("GM2_1H","Kgt_g_s3_new")
kgt.AttackWindow("Kgt_g_s3_new",0.338,0.525,"GM2_1H_Window")
kgt.AssignTrail("GM2_1H","","EstelaAmarilla1")
kgt.AddLevels("Kgt_g_s3_new",7,40)
kgt.AddEnergyLevel("Kgt_g_s3_new", 0)


#COMBO2 group
kgt.AddAttack("GM3_1H","Kgt_g_12_new")
kgt.AttackWindow("Kgt_g_12_new",0.345,0.550,"GM3_1H_Window")
kgt.AddLevels("Kgt_g_12_new",0,40)
kgt.AddEnergyLevel("Kgt_g_12_new", 0)

#COMBO2 group
kgt.AddAttack("GM4_1H","Kgt_g_02_new")
kgt.AttackWindow("Kgt_g_02_new",0.341,0.567,"GM4_1H_Window")
kgt.AssignTrail("GM4_1H","","EstelaAmarilla1")
kgt.AddLevels("Kgt_g_02_new",4,40)
kgt.AddEnergyLevel("Kgt_g_02_new", 0)


#COMBO3 group
kgt.AddAttack("GM6_1H","Kgt_g_b06_new")
kgt.AttackWindow("Kgt_g_b06_new",0.455,0.600,"GM6_1H_Window")
kgt.AddLevels("Kgt_g_b06_new",0,40)
kgt.AddEnergyLevel("Kgt_g_b06_new", 0)

#COMBO3 group
kgt.AddAttack("GM7_1H","Kgt_g_19_bs1_new")
kgt.AttackWindow("Kgt_g_19_bs1_new",0.548,0.694,"GM7_1H_Window")
kgt.AssignTrail("GM7_1H","","EstelaAmarilla1")
kgt.AddLevels("Kgt_g_19_bs1_new",5,40)
kgt.AddEnergyLevel("Kgt_g_19_bs1_new", 0)


#COMBO4 group
kgt.AddAttack("GM8_1H","Kgt_g_01low_new")
kgt.AttackWindow("Kgt_g_01low_new",0.395,0.510,"GM8_1H_Window")
kgt.AddLevels("Kgt_g_01low_new",0,40)
kgt.AddEnergyLevel("Kgt_g_01low_new", 0)

#COMBO4 group
kgt.AddAttack("GM9_1H","Kgt_g_22lowkata_new")
kgt.AttackWindow("Kgt_g_22lowkata_new",0.496,0.636,"GM9_1H_Window")
kgt.AssignTrail("GM9_1H","","EstelaAmarilla1")
kgt.AddLevels("Kgt_g_22lowkata_new",6,40)
kgt.AddEnergyLevel("Kgt_g_22lowkata_new", 0)



#COMBO GLADIUS
kgt.AddAttack("GM38_1H","Kgt_g_28new")
kgt.AttackWindow("Kgt_g_28new",0.001,0.900,"GM38_1H_Window")
kgt.AssignTrail("GM38_1H","","EstelaRoja1")
kgt.AddLevels("Kgt_g_28new",3,40)
kgt.AddEnergyLevel("Kgt_g_28new", 0)

#COMBO ESPADAFILO
kgt.AddAttack("GM16_1H","Kgt_g_09_07_s6low_new")
kgt.AttackWindow("Kgt_g_09_07_s6low_new",0.445,0.560,"GM16_1H_Window")
kgt.AssignTrail("GM16_1H","","EstelaRoja1")
kgt.AddLevels("Kgt_g_09_07_s6low_new",17,40)
kgt.AddEnergyLevel("Kgt_g_09_07_s6low_new", 0)

#COMBO CIMITARRA
kgt.AddAttack("GM18_1H","Kgt_g_18_11_22_new")
kgt.AttackWindow("Kgt_g_18_11_22_new",0.630,0.770,"GM18_1H_Window")
kgt.AssignTrail("GM18_1H","","EstelaRoja1")
kgt.AddLevels("Kgt_g_18_11_22_new",14,40)
kgt.AddEnergyLevel("Kgt_g_18_11_22_new", 0)

#COMBO ESPADACURVA
kgt.AddAttack("GM5_1H","Kgt_g_sb25_new")
kgt.AttackWindow("Kgt_g_sb25_new",0.472,0.626,"GM5_1H_Window")
kgt.AssignTrail("GM5_1H","","EstelaRoja1")
kgt.AddLevels("Kgt_g_sb25_new",11,40)
kgt.AddEnergyLevel("Kgt_g_sb25_new", 0)

#COMBO MAZA3
kgt.AddAttack("GM17_1H","Kgt_g_b32kata_new")
kgt.AttackWindow("Kgt_g_b32kata_new",0.610,0.810,"GM17_1H_Window")
kgt.AssignTrail("GM17_1H","","EstelaRoja1")
kgt.AddLevels("Kgt_g_b32kata_new",15,40)
kgt.AddEnergyLevel("Kgt_g_b32kata_new", 0)

#COMBO MAZA
kgt.AddAttack("GM20_1H","Kgt_g_01_new")
kgt.AttackWindow("Kgt_g_01_new",0.185,0.400,"GM20_1H_Window")
kgt.AssignTrail("GM20_1H","","EstelaRoja1")
kgt.AddLevels("Kgt_g_01_new",6,40)
kgt.AddEnergyLevel("Kgt_g_01_new", 0)

#COMBO HOOKSWORD
kgt.AddAttack("GM39_1H","Kgt_g_s22low_new")
kgt.AttackWindow("Kgt_g_s22low_new",0.001,0.900,"GM39_1H_Window")
kgt.AssignTrail("GM39_1H","","EstelaRoja1")
kgt.AddLevels("Kgt_g_s22low_new",10,40)
kgt.AddEnergyLevel("Kgt_g_s22low_new", 0)

#COMBO DAGESSE
kgt.AddAttack("GM25_1H","Kgt_g_s19_new")
kgt.AttackWindow("Kgt_g_s19_new",0.508,0.696,"GM25_1H_Window")
kgt.AssignTrail("GM25_1H","","EstelaRoja1")
kgt.AddLevels("Kgt_g_s19_new",13,40)
kgt.AddEnergyLevel("Kgt_g_s19_new", 0)

#COMBO ESPADA
kgt.AddAttack("GM21_1H","Kgt_g_29_3new")
kgt.AttackWindow("Kgt_g_29_3new",0.484,0.674,"GM21_1H_Window")
kgt.AssignTrail("GM21_1H","","EstelaRoja1")
kgt.AddLevels("Kgt_g_29_3new",18,40)
kgt.AddEnergyLevel("Kgt_g_29_3new", 0)

#COMBO QUEENSWORD
kgt.AddAttack("GM19_1H","Kgt_g_06lowkata_new")
kgt.AttackWindow("Kgt_g_06lowkata_new",0.068,0.560,"GM19_1H_Window")
kgt.AssignTrail("GM19_1H","","EstelaRoja1")
kgt.AddLevels("Kgt_g_06lowkata_new",10,40)
kgt.AddEnergyLevel("Kgt_g_06lowkata_new", 0)

#COMBO ICESWORD
kgt.AddAttack("GM37_1H","Kgt_g_12_7_s1new")
kgt.AttackWindow("Kgt_g_12_7_s1new",0.508,0.612,"GM37_1H_Window")
kgt.AssignTrail("GM37_1H","","EstelaAzul1")
kgt.AddLevels("Kgt_g_12_7_s1new",17,40)
kgt.AddEnergyLevel("Kgt_g_12_7_s1new", 0)

#COMBO MAZA2
kgt.AddAttack("GM22_1H","Kgt_g_21_6_s8new")
kgt.AttackWindow("Kgt_g_21_6_s8new",0.562,0.674,"GM22_1H_Window")
kgt.AssignTrail("GM22_1H","","EstelaRoja1")
kgt.AddLevels("Kgt_g_21_6_s8new",9,40)
kgt.AddEnergyLevel("Kgt_g_21_6_s8new", 0)

#COMBO ESPADAELFICA
kgt.AddAttack("GM34_1H","Kgt_g_32_5_3new")
kgt.AttackWindow("Kgt_g_32_5_3new",0.508,0.706,"GM34_1H_Window")
kgt.AssignTrail("GM34_1H","","EstelaRoja1")
kgt.AddLevels("Kgt_g_32_5_3new",8,40)
kgt.AddEnergyLevel("Kgt_g_32_5_3new", 0)

#COMBO ESPADAROMANA
kgt.AddAttack("GM35_1H","Kgt_g_27kata_new")
kgt.AttackWindow("Kgt_g_27kata_new",0.427,0.670,"GM35_1H_Window")
kgt.AssignTrail("GM35_1H","","EstelaRoja1")
kgt.AddLevels("Kgt_g_27kata_new",7,40)
kgt.AddEnergyLevel("Kgt_g_27kata_new", 0)

#COMBO DOUBLESWORD
kgt.AddAttack("GM40_1H","Kgt_g_22kata_23_new")
kgt.AttackWindow("Kgt_g_22kata_23_new",0.001,0.900,"GM40_1H_Window")
kgt.AssignTrail("GM40_1H","","EstelaRoja1")
kgt.AddLevels("Kgt_g_22kata_23_new",16,40)
kgt.AddEnergyLevel("Kgt_g_22kata_23_new", 0)

#COMBO ESPADAFIRESWORD
kgt.AddAttack("GM36_1H","Kgt_g_s28kata_new")
kgt.AttackWindow("Kgt_g_s28kata_new",0.600,0.821,"GM36_1H_Window")
kgt.AssignTrail("GM36_1H","","EstelaRoja1")
kgt.AddLevels("Kgt_g_s28kata_new",12,40)
kgt.AddEnergyLevel("Kgt_g_s28kata_new", 0)


#COMBOHACHATORPE group
kgt.AddAttack("GM10_AXE","Kgt_g_bad_axe")
kgt.AttackWindow("Kgt_g_bad_axe",0.435,0.643,"GM10_AXE_Window")
kgt.AssignTrail("GM10_AXE","","EstelaAmarilla1")
kgt.AddLevels("Kgt_g_bad_axe",0,8)
kgt.AddEnergyLevel("Kgt_g_bad_axe", 0)

#COMBOESPADATORPE1 group
kgt.AddAttack("GM11_2W","Kgt_g_bad_sword")
kgt.AttackWindow("Kgt_g_bad_sword",0.225,0.575,"GM11_2W_Window")
kgt.AddLevels("Kgt_g_bad_sword",0,40)
kgt.AddEnergyLevel("Kgt_g_bad_sword", 0)

#COMBOESPADATORPE2 group
kgt.AddAttack("GM12_2W","Kgt_g_bad_sword2")
kgt.AttackWindow("Kgt_g_bad_sword2",0.464,0.741,"GM12_2W_Window")
kgt.AddLevels("Kgt_g_bad_sword2",0,40)
kgt.AddEnergyLevel("Kgt_g_bad_sword2", 0)

#COMBOESPADATORPE2 group
kgt.AddAttack("GM13_2W","Kgt_g_bad_sword3")
kgt.AttackWindow("Kgt_g_bad_sword3",0.427,0.807,"GM13_2W_Window")
kgt.AddLevels("Kgt_g_bad_sword3",0,40)
kgt.AddEnergyLevel("Kgt_g_bad_sword3", 0)

#COMBOLANZATORPE1 group
kgt.AddAttack("GM14_SP","Kgt_g_bad_spear")
kgt.AttackWindow("Kgt_g_bad_spear",0.283,0.519,"GM14_SP_Window")
kgt.AddLevels("Kgt_g_bad_spear",0,40)
kgt.AddEnergyLevel("Kgt_g_bad_spear", 0)

#COMBOLANZATORPE2 group
kgt.AddAttack("GM15_SP","Kgt_g_bad_spear2")
kgt.AttackWindow("Kgt_g_bad_spear2",0.461,0.748,"GM15_SP_Window")
kgt.AddLevels("Kgt_g_bad_spear2",0,40)
kgt.AddEnergyLevel("Kgt_g_bad_spear2", 0)

#COMBOEXTRA1 group
kgt.AddAttack("GM23_1H","Kgt_g_01_7_new")
kgt.AttackWindow("Kgt_g_01_7_new",0.461,0.655,"GM23_1H_Window")
kgt.AssignTrail("GM23_1H","","EstelaAmarilla1")
kgt.AddLevels("Kgt_g_01_7_new",2,40)
kgt.AddEnergyLevel("Kgt_g_01_7_new", 0)

#COMBOEXTRA2 group
kgt.AddAttack("GM24_1H","Kgt_g_3s9_6new")
kgt.AttackWindow("Kgt_g_3s9_6new",0.427,0.675,"GM24_1H_Window")
kgt.AddLevels("Kgt_g_3s9_6new",11,40)
kgt.AssignTrail("GM24_1H","","EstelaRoja1")
kgt.AddEnergyLevel("Kgt_g_3s9_6new", 0)


#COMBOGIRO180 group
kgt.AddAttack("GM26_1H","Kgt_g_back")
#kgt.AttackWindow("Kgt_g_back",0.001,0.900,"GM26_1H_Window")
kgt.AddLevels("Kgt_g_back",3,40)
kgt.AddEnergyLevel("Kgt_g_back", 0)





#COMBOARMAENANO1 group
kgt.AddAttack("GM27_1H","Kgt_g_08")
kgt.AttackWindow("Kgt_g_08",0.001,0.900,"GM27_1H_Window")
kgt.AddLevels("Kgt_g_08",0,40)
kgt.AddEnergyLevel("Kgt_g_08", 0)

#COMBOARMAENANO2 group
kgt.AddAttack("GM28_1H","Kgt_g_02")
kgt.AttackWindow("Kgt_g_02",0.001,0.900,"GM28_1H_Window")
kgt.AddLevels("Kgt_g_02",0,40)
kgt.AddEnergyLevel("Kgt_g_02", 0)

#COMBOARMAENANO3 group
kgt.AddAttack("GM29_1H","Kgt_g_07")
kgt.AttackWindow("Kgt_g_07",0.001,0.900,"GM29_1H_Window")
kgt.AddLevels("Kgt_g_07",0,40)
kgt.AddEnergyLevel("Kgt_g_07", 0)

#COMBOARMAENANO4 group
kgt.AddAttack("GM30_1H","Kgt_g_06")
kgt.AttackWindow("Kgt_g_06",0.001,0.900,"GM30_1H_Window")
kgt.AddLevels("Kgt_g_06",0,40)
kgt.AddEnergyLevel("Kgt_g_06", 0)

#COMBOARMAENANO5 group
kgt.AddAttack("GM31_1H","Kgt_g_05")
kgt.AttackWindow("Kgt_g_05",0.001,0.900,"GM31_1H_Window")
kgt.AddLevels("Kgt_g_05",0,40)
kgt.AddEnergyLevel("Kgt_g_05", 0)




#GOLPESINARMA1 "group"
kgt.AddAttack("GM32_NO","Kgt_g_punch1")
kgt.AddLevels("Kgt_g_punch1",0,40)
kgt.AddEnergyLevel("Kgt_g_punch1", 0)

#GOLPESINARMA2 "group"
kgt.AddAttack("GM33_NO","Kgt_g_punch2")
kgt.AddLevels("Kgt_g_punch2",0,40)
kgt.AddEnergyLevel("Kgt_g_punch2", 0)



########################################
# GRUPO DE LANZAR ESTELAS y MAGIAS     #
########################################
#ESTELA1
kgt.AddAttack("GM50_1H","Kgt_g_magic")
kgt.AssignTrail("GM50_1H","","EstelaRoja1")
kgt.AddLevels("Kgt_g_magic",19,40)
kgt.AddEnergyLevel("Kgt_g_magic", 0)

#CONCENTRACION1 ENERGIA
kgt.AddAttack("GM51_1H","Kgt_g_magic2")
kgt.AssignTrail("GM51_1H","","EstelaRoja1")
kgt.AddLevels("Kgt_g_magic2",18,40)
kgt.AddEnergyLevel("Kgt_g_magic2", 0)

######################################################################
#GAI meta-group
kgt.MetaAttack("GIM_1H","GI_1H")
kgt.MetaAttack("GIM_1H","GM1_1H")
kgt.MetaAttack("GIM_1H","GM2_1H")
kgt.MetaAttack("GIM_1H","GM3_1H")
kgt.MetaAttack("GIM_1H","GM4_1H")
kgt.MetaAttack("GIM_1H","GM5_1H")
kgt.MetaAttack("GIM_1H","GM6_1H")
kgt.MetaAttack("GIM_1H","GM7_1H")
kgt.MetaAttack("GIM_1H","GM8_1H")
kgt.MetaAttack("GIM_1H","GM9_1H")
kgt.MetaAttack("GIM_AXE","GM10_AXE")
kgt.MetaAttack("GIM_2W","GM11_2W")
kgt.MetaAttack("GIM_2W","GM12_2W")
kgt.MetaAttack("GIM_2W","GM13_2W")
kgt.MetaAttack("GIM_SP","GM14_SP")
kgt.MetaAttack("GIM_SP","GM15_SP")
kgt.MetaAttack("GIM_1H","GM16_1H")
kgt.MetaAttack("GIM_1H","GM17_1H")
kgt.MetaAttack("GIM_1H","GM18_1H")
kgt.MetaAttack("GIM_1H","GM19_1H")
kgt.MetaAttack("GIM_1H","GM20_1H")
kgt.MetaAttack("GIM_1H","GM21_1H")
kgt.MetaAttack("GIM_1H","GM22_1H")
kgt.MetaAttack("GIM_1H","GM23_1H")
kgt.MetaAttack("GIM_1H","GM24_1H")
kgt.MetaAttack("GIM_1H","GM25_1H")
kgt.MetaAttack("GIM_1H","GM26_1H")
kgt.MetaAttack("GIM_1H","GM27_1H")
kgt.MetaAttack("GIM_1H","GM28_1H")
kgt.MetaAttack("GIM_1H","GM29_1H")
kgt.MetaAttack("GIM_1H","GM30_1H")
kgt.MetaAttack("GIM_1H","GM31_1H")
kgt.MetaAttack("GIM_NO","GM32_NO")
kgt.MetaAttack("GIM_NO","GM33_NO")
kgt.MetaAttack("GIM_1H","GM34_1H")
kgt.MetaAttack("GIM_1H","GM35_1H")
kgt.MetaAttack("GIM_1H","GM36_1H")
kgt.MetaAttack("GIM_1H","GM37_1H")
kgt.MetaAttack("GIM_1H","GM38_1H")
kgt.MetaAttack("GIM_1H","GM39_1H")
kgt.MetaAttack("GIM_1H","GM40_1H")
kgt.MetaAttack("GIM_1H","GM50_1H")
kgt.MetaAttack("GIM_1H","GM51_1H")


kgt.MetaAttack("GOLPEINICIAL","GI_1H")

#GM meta-group
kgt.MetaAttack("COMBO1","GM1_1H")
kgt.MetaAttack("COMBO1","GM2_1H")
kgt.MetaAttack("COMBO1","GM3_1H")
kgt.MetaAttack("COMBO1","GM4_1H")
kgt.MetaAttack("COMBO1","GM5_1H")
kgt.MetaAttack("COMBO1","GM6_1H")
kgt.MetaAttack("COMBO1","GM7_1H")
kgt.MetaAttack("COMBO1","GM8_1H")
kgt.MetaAttack("COMBO1","GM9_1H")
kgt.MetaAttack("COMBO1","GM10_AXE")
kgt.MetaAttack("COMBO1","GM11_2W")
kgt.MetaAttack("COMBO1","GM12_2W")
kgt.MetaAttack("COMBO1","GM13_2W")
kgt.MetaAttack("COMBO1","GM14_SP")
kgt.MetaAttack("COMBO1","GM15_SP")
kgt.MetaAttack("COMBO1","GM16_1H")
kgt.MetaAttack("COMBO1","GM17_1H")
kgt.MetaAttack("COMBO1","GM18_1H")
kgt.MetaAttack("COMBO1","GM19_1H")
kgt.MetaAttack("COMBO1","GM20_1H")
kgt.MetaAttack("COMBO1","GM21_1H")
kgt.MetaAttack("COMBO1","GM22_1H")
kgt.MetaAttack("COMBO1","GM23_1H")
kgt.MetaAttack("COMBO1","GM24_1H")
kgt.MetaAttack("COMBO1","GM25_1H")
kgt.MetaAttack("COMBO1","GM26_1H")
kgt.MetaAttack("ARMAENANO","GM27_1H")
kgt.MetaAttack("ARMAENANO","GM28_1H")
kgt.MetaAttack("ARMAENANO","GM29_1H")
kgt.MetaAttack("ARMAENANO","GM30_1H")
kgt.MetaAttack("ARMAENANO","GM31_1H")
kgt.MetaAttack("COMBO1","GM32_NO")
kgt.MetaAttack("COMBO1","GM33_NO")
kgt.MetaAttack("COMBO1","GM34_1H")
kgt.MetaAttack("COMBO1","GM35_1H")
kgt.MetaAttack("COMBO1","GM36_1H")
kgt.MetaAttack("COMBO1","GM37_1H")
kgt.MetaAttack("COMBO1","GM38_1H")
kgt.MetaAttack("COMBO1","GM39_1H")
kgt.MetaAttack("COMBO1","GM40_1H")
kgt.MetaAttack("COMBO1","GM50_1H")
kgt.MetaAttack("COMBO1","GM51_1H")

#kgt.MetaAttack("ESTELA1","GMG1_1H")
#kgt.MetaAttack("CONCENTRACION1","GMG2_1H")



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
# *(optional) Kind of weapon 
#		"1H"   -> One handed (default value)
#		"2W"   -> Two handed sword
#		"AXE"  -> Two handed axe
#		"SP"   -> Two handed spear
#



###########################################################

#COMBOGIRO180
kgt.AllowAttack("GM26_1H","L+R+B","","","","1H")

kgt.AllowAttack("GM27_1H","A","DL","ARMAENANO","","Alabarda")
kgt.AllowAttack("GM27_1H","A","DR","ARMAENANO","","Alabarda")
kgt.AllowAttack("GM27_1H","A","DB","ARMAENANO","","Alabarda")

#Golpes en esquiva
kgt.AllowAttack("DL_G_1H","A","DL","","","1H")
#kgt.AllowAttack("DL_G_1H","A+L","DL","","","1H")
#kgt.AllowAttack("DL_G_1H","&A+L","DL","","","1H")

kgt.AllowAttack("DR_G_1H","A","DR","","","1H")
#kgt.AllowAttack("DR_G_1H","A+R","DR","","","1H")
#kgt.AllowAttack("DR_G_1H","&A+R","DR","","","1H")

kgt.AllowAttack("DB_G_1H","A","DB","","","1H")
#kgt.AllowAttack("DB_G_1H","A+B","DB","","","1H")
#kgt.AllowAttack("DB_G_1H","&A+B","DB","","","1H")



#LANZAR ESTELA
kgt.AllowAttack("GM51_1H","&B","GI_1H","","","BladeSword2")

#CONCENTRACION
kgt.AllowAttack("GM50_1H","&A+F","GI_1H","","","BladeSword2")



#GOLPESINARMA1
kgt.AllowAttack("GM32_NO","A+B","","COMBO1","","NO")
kgt.AllowAttack("GM32_NO","&A+B","","COMBO1","","NO")

#GOLPESINARMA1
kgt.AllowAttack("GM33_NO","A+L","","COMBO1","","NO")
kgt.AllowAttack("GM33_NO","&A+L","","COMBO1","","NO")

#GOLPESINARMA1
kgt.AllowAttack("GM33_NO","A+R","","COMBO1","","NO")
kgt.AllowAttack("GM33_NO","&A+R","","COMBO1","","NO")

#GOLPESINARMA1
kgt.AllowAttack("GM33_NO","A","","COMBO1","","NO")




#COMBOHACHATORPE
kgt.AllowAttack("GM10_AXE","A","","","","AXE")

#COMBOESPADATORPE2
kgt.AllowAttack("GM12_2W","A","GM11_2W","","GM11_2W_Window","2W")

#COMBOESPADATORPE3
kgt.AllowAttack("GM13_2W","A","GM12_2W","","GM12_2W_Window","2W")

#COMBOESPADATORPE1
kgt.AllowAttack("GM11_2W","A","","COMBO1,COMBO1,COMBO1","GM13_2W_Window","2W")

#COMBOLANZATORPE2
kgt.AllowAttack("GM15_SP","A","GM14_SP","","GM14_SP_Window","SP")

#COMBOLANZATORPE1
kgt.AllowAttack("GM14_SP","A","","COMBO1,COMBO1,COMBO1","GM15_SP_Window","SP")






#COMBOMARTILLOCRUSHHAMMER_ARMA_ENANO
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","CrushHammer")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","CrushHammer")

#COMBOMARTILLOCRUSHHAMMER_ARMA_ENANO
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","CrushHammer")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","CrushHammer")

#COMBOMARTILLOCRUSHHAMMER_ARMA_ENANO
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","CrushHammer")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","CrushHammer")

#COMBOMARTILLOCRUSHHAMMER_ARMA_ENANO
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","CrushHammer")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","CrushHammer")

#COMBOMARTILLOCRUSHHAMMER_ARMA_ENANO
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","CrushHammer")



#COMBOFIREAXE_ARMA_ENANO
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","FireAxe")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","FireAxe")

#COMBOFIREAXE_ARMA_ENANO
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","FireAxe")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","FireAxe")

#COMBOFIREAXE_ARMA_ENANO
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","FireAxe")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","FireAxe")

#COMBOFIREAXE_ARMA_ENANO
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","FireAxe")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","FireAxe")

#COMBOFIREAXE_ARMA_ENANO
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","FireAxe")



#COMBOICEHAMMER_ARMA_ENANO
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","IceHammer")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","IceHammer")

#COMBOICEHAMMER_ARMA_ENANO
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","IceHammer")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","IceHammer")

#COMBOICEHAMMER_ARMA_ENANO
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","IceHammer")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","IceHammer")

#COMBOICEHAMMER_ARMA_ENANO
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","IceHammer")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","IceHammer")

#COMBOICEHAMMER_ARMA_ENANO
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","IceHammer")



#COMBOHACHA_ARMA_ENANO
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","Hacha")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","Hacha")

#COMBOHACHA_ARMA_ENANO
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","Hacha")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","Hacha")

#COMBOHACHA_ARMA_ENANO
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","Hacha")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","Hacha")

#COMBOHACHA_ARMA_ENANO
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","Hacha")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","Hacha")

#COMBOHACHA_ARMA_ENANO
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","Hacha")



#COMBOHACHA5_ARMA_ENANO
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","Hacha5")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","Hacha5")

#COMBOHACHA5_ARMA_ENANO
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","Hacha5")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","Hacha5")

#COMBOHACHA5_ARMA_ENANO
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","Hacha5")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","Hacha5")

#COMBOHACHA5_ARMA_ENANO
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","Hacha5")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","Hacha5")

#COMBOHACHA5_ARMA_ENANO
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","Hacha5")



#COMBOHACHA4_ARMA_ENANO
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","Hacha4")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","Hacha4")

#COMBOHACHA4_ARMA_ENANO
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","Hacha4")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","Hacha4")

#COMBOHACHA4_ARMA_ENANO
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","Hacha4")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","Hacha4")

#COMBOHACHA4_ARMA_ENANO
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","Hacha4")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","Hacha4")

#COMBOHACHA4_ARMA_ENANO
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","Hacha4")



#COMBOHACHA3_ARMA_ENANO
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","Hacha3")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","Hacha3")

#COMBOHACHA3_ARMA_ENANO
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","Hacha3")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","Hacha3")

#COMBOHACHA3_ARMA_ENANO
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","Hacha3")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","Hacha3")

#COMBOHACHA3_ARMA_ENANO
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","Hacha3")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","Hacha3")

#COMBOHACHA3_ARMA_ENANO
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","Hacha3")



#COMBOHACHA6_ARMA_ENANO
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","Hacha6")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","Hacha6")

#COMBOHACHA6_ARMA_ENANO
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","Hacha6")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","Hacha6")

#COMBOHACHA6_ARMA_ENANO
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","Hacha6")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","Hacha6")

#COMBOHACHA6_ARMA_ENANO
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","Hacha6")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","Hacha6")

#COMBOHACHA6_ARMA_ENANO
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","Hacha6")



#COMBOHACHA2_ARMA_ENANO
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","Hacha2")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","Hacha2")

#COMBOHACHA2_ARMA_ENANO
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","Hacha2")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","Hacha2")

#COMBOHACHA2_ARMA_ENANO
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","Hacha2")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","Hacha2")

#COMBOHACHA2_ARMA_ENANO
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","Hacha2")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","Hacha2")

#COMBOHACHA2_ARMA_ENANO
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","Hacha2")



#COMBOGARROTE_ARMA_ENANO
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","Garrote")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","Garrote")

#COMBOGARROTE_ARMA_ENANO
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","Garrote")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","Garrote")

#COMBOGARROTE_ARMA_ENANO
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","Garrote")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","Garrote")

#COMBOGARROTE_ARMA_ENANO
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","Garrote")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","Garrote")

#COMBOGARROTE_ARMA_ENANO
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","Garrote")



#COMBOMARTILLO_ARMA_ENANO
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","Martillo")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","Martillo")

#COMBOMARTILLO_ARMA_ENANO
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","Martillo")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","Martillo")

#COMBOMARTILLO_ARMA_ENANO
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","Martillo")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","Martillo")

#COMBOMARTILLO_ARMA_ENANO
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","Martillo")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","Martillo")

#COMBOMARTILLO_ARMA_ENANO
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","Martillo")



#COMBOMARTILLO2_ARMA_ENANO
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","Martillo2")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","Martillo2")

#COMBOMARTILLO2_ARMA_ENANO
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","Martillo2")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","Martillo2")

#COMBOMARTILLO2_ARMA_ENANO
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","Martillo2")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","Martillo2")

#COMBOMARTILLO2_ARMA_ENANO
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","Martillo2")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","Martillo2")

#COMBOMARTILLO2_ARMA_ENANO
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","Martillo2")



#COMBOGARROPIN_ARMA_ENANO
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","Garropin")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","Garropin")

#COMBOGARROPIN_ARMA_ENANO
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","Garropin")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","Garropin")

#COMBOGARROPIN_ARMA_ENANO
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","Garropin")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","Garropin")

#COMBOGARROPIN_ARMA_ENANO
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","Garropin")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","Garropin")

#COMBOGARROPIN_ARMA_ENANO
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","Garropin")



#COMBOMAZADOBLE_ARMA_ENANO
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","MazaDoble")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","MazaDoble")

#COMBOMAZADOBLE_ARMA_ENANO
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","MazaDoble")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","MazaDoble")

#COMBOMAZADOBLE_ARMA_ENANO
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","MazaDoble")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","MazaDoble")

#COMBOMAZADOBLE_ARMA_ENANO
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","MazaDoble")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","MazaDoble")

#COMBOMAZADOBLE_ARMA_ENANO
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","MazaDoble")



#COMBOGARROTE2_ARMA_ENANO
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","Garrote2")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","Garrote2")

#COMBOGARROTE2_ARMA_ENANO
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","Garrote2")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","Garrote2")

#COMBOGARROTE2_ARMA_ENANO
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","Garrote2")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","Garrote2")

#COMBOGARROTE2_ARMA_ENANO
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","Garrote2")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","Garrote2")

#COMBOGARROTE2_ARMA_ENANO
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","Garrote2")



#COMBOMARTILLO3_ARMA_ENANO
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","Martillo3")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","Martillo3")

#COMBOMARTILLO3_ARMA_ENANO
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","Martillo3")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","Martillo3")

#COMBOMARTILLO3_ARMA_ENANO
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","Martillo3")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","Martillo3")

#COMBOMARTILLO3_ARMA_ENANO
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","Martillo3")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","Martillo3")

#COMBOMARTILLO3_ARMA_ENANO
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","Martillo3")


#COMBOALABARDA_ARMA_MAL_USO
kgt.AllowAttack("GM27_1H","A+F","","ARMAENANO","","Alabarda")
kgt.AllowAttack("GM27_1H","&A+F","","ARMAENANO","","Alabarda")

#COMBOALABARDA_ARMA_MAL_USO
kgt.AllowAttack("GM27_1H","A+B","","ARMAENANO","","Alabarda")
kgt.AllowAttack("GM27_1H","&A+B","","ARMAENANO","","Alabarda")

#COMBOALABARDA_ARMA_MAL_USO
kgt.AllowAttack("GM27_1H","A+L","","ARMAENANO","","Alabarda")
kgt.AllowAttack("GM27_1H","&A+L","","ARMAENANO","","Alabarda")

#COMBOALABARDA_ARMA_MAL_USO
kgt.AllowAttack("GM27_1H","A+R","","ARMAENANO","","Alabarda")
kgt.AllowAttack("GM27_1H","&A+R","","ARMAENANO","","Alabarda")

#COMBOALABARDA_ARMA_MAL_USO
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","Alabarda")



#COMBOCUCHILLO_ARMA_MAL_USO
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","Cuchillo")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","Cuchillo")

#COMBOCUCHILLO_ARMA_MAL_USO
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","Cuchillo")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","Cuchillo")

#COMBOCUCHILLO_ARMA_MAL_USO
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","Cuchillo")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","Cuchillo")

#COMBOCUCHILLO_ARMA_MAL_USO
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","Cuchillo")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","Cuchillo")

#COMBOCUCHILLO_ARMA_MAL_USO
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","Cuchillo")



#COMBODAGA_ARMA_MAL_USO
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","Daga")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","Daga")

#COMBODAGA_ARMA_MAL_USO
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","Daga")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","Daga")

#COMBODAGA_ARMA_MAL_USO
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","Daga")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","Daga")

#COMBODAGA_ARMA_MAL_USO
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","Daga")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","Daga")
#COMBODAGA_ARMA_MAL_USO
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","Daga")



#COMBOVARITA7_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","Varita7")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","Varita7")

#COMBOVARITA7_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","Varita7")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","Varita7")

#COMBOVARITA7_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","Varita7")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","Varita7")

#COMBOVARITA7_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","Varita7")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","Varita7")

#COMBOVARITA7_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","Varita7")



#COMBOVARITA6_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","Varita6")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","Varita6")

#COMBOVARITA6_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","Varita6")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","Varita6")

#COMBOVARITA6_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","Varita6")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","Varita6")

#COMBOVARITA6_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","Varita6")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","Varita6")

#COMBOVARITA6_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","Varita6")



#COMBOVARITA5_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","Varita5")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","Varita5")

#COMBOVARITA5_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","Varita5")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","Varita5")

#COMBOVARITA5_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","Varita5")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","Varita5")

#COMBOVARITA5_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","Varita5")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","Varita5")

#COMBOVARITA5_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","Varita5")



#COMBOVARITA2_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","Varita2")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","Varita2")

#COMBOVARITA2_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","Varita2")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","Varita2")

#COMBOVARITA2_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","Varita2")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","Varita2")

#COMBOVARITA2_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","Varita2")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","Varita2")

#COMBOVARITA2_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","Varita2")



#COMBOVARITA1_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","Varita1")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","Varita1")

#COMBOVARITA1_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","Varita1")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","Varita1")

#COMBOVARITA1_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","Varita1")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","Varita1")

#COMBOVARITA1_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","Varita1")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","Varita1")

#COMBOVARITA1_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","Varita1")



#COMBOESPADAMAGICA1_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","EspadaMagica1")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","EspadaMagica1")

#COMBOESPADAMAGICA1_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","EspadaMagica1")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","EspadaMagica1")

#COMBOESPADAMAGICA1_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","EspadaMagica1")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","EspadaMagica1")

#COMBOESPADAMAGICA1_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","EspadaMagica1")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","EspadaMagica1")

#COMBOESPADAMAGICA1_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","EspadaMagica1")



#COMBOESPADAMAGICA2_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","EspadaMagica2")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","EspadaMagica2")

#COMBOESPADAMAGICA2_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","EspadaMagica2")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","EspadaMagica2")

#COMBOESPADAMAGICA2_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","EspadaMagica2")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","EspadaMagica2")

#COMBOESPADAMAGICA2_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","EspadaMagica2")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","EspadaMagica2")

#COMBOESPADAMAGICA2_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","EspadaMagica2")



#COMBOESPADAMAGICA3_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","EspadaMagica3")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","EspadaMagica3")

#COMBOESPADAMAGICA3_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","EspadaMagica3")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","EspadaMagica3")

#COMBOESPADAMAGICA3_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","EspadaMagica3")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","EspadaMagica3")

#COMBOESPADAMAGICA3_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","EspadaMagica3")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","EspadaMagica3")

#COMBOESPADAMAGICA3_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","EspadaMagica3")



#COMBOVAMPWEAPON_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","VampWeapon")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","VampWeapon")

#COMBOVAMPWEAPON_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","VampWeapon")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","VampWeapon")

#COMBOVAMPWEAPON_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","VampWeapon")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","VampWeapon")

#COMBOVAMPWEAPON_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","VampWeapon")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","VampWeapon")

#COMBOVAMPWEAPON_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","VampWeapon")



#COMBOBASTON3_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM28_1H","A+F","","ARMAENANO","","Baston3")
kgt.AllowAttack("GM28_1H","&A+F","","ARMAENANO","","Baston3")

#COMBOBASTON3_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM29_1H","A+B","","ARMAENANO","","Baston3")
kgt.AllowAttack("GM29_1H","&A+B","","ARMAENANO","","Baston3")

#COMBOBASTON3_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM30_1H","A+L","","ARMAENANO","","Baston3")
kgt.AllowAttack("GM30_1H","&A+L","","ARMAENANO","","Baston3")

#COMBOBASTON3_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM31_1H","A+R","","ARMAENANO","","Baston3")
kgt.AllowAttack("GM31_1H","&A+R","","ARMAENANO","","Baston3")

#COMBOBASTON3_ARMA_MAGICAS_MALAS
kgt.AllowAttack("GM27_1H","A","","ARMAENANO","","Baston3")






#COMBO GLADIUS
kgt.AllowAttack("GM38_1H","F+L","GI_1H","","GI_1H_Window","Gladius")

#COMBO MAZA
kgt.AllowAttack("GM20_1H","B+R","GI_1H","","GI_1H_Window","Maza")

#COMBO ESPADAFILO
kgt.AllowAttack("GM16_1H","L+B","GI_1H","","GI_1H_Window","Espadafilo")

#COMBO DAGESSE
kgt.AllowAttack("GM25_1H","B","GI_1H","","GI_1H_Window","Dagesse")

#COMBO ESPADAELFICA
kgt.AllowAttack("GM34_1H","F+R","GI_1H","","GI_1H_Window","Espadaelfica")

#COMBO ESPADAFIRESWORD
kgt.AllowAttack("GM36_1H","B","GM23_1H","","GM23_1H_Window","FireSword")

#COMBO CIMITARRA
kgt.AllowAttack("GM18_1H","F","GM23_1H","","","Cimitarra")

#COMBO ICESWORD
kgt.AllowAttack("GM37_1H","R+L","GM23_1H","","GM23_1H_Window","IceSword")

#COMBOEXTRA2
kgt.AllowAttack("GM24_1H","&A","GM23_1H","","GM23_1H_Window","1H")

#COMBOEXTRA1
kgt.AllowAttack("GM23_1H","F+B","GIM_1H","COMBO1,COMBO1,COMBO1//ARMAENANO","GIM_1H_Window","1H")



#COMBO TECLA ARRIBA2
kgt.AllowAttack("GM2_1H","A+F","GM1_1H","","GM1_1H_Window","1H")
kgt.AllowAttack("GM2_1H","&A+F","GM1_1H","","GM1_1H_Window","1H")

#COMBO TECLA ARRIBA1
kgt.AllowAttack("GM1_1H","A+F","","GM1_1H//ARMAENANO","GM2_1H_Window","1H")
kgt.AllowAttack("GM1_1H","&A+F","","GM1_1H//ARMAENANO","GM2_1H_Window","1H")

#COMBO HOOKSWORD
kgt.AllowAttack("GM39_1H","B","GM1_1H","","","HookSword")

#COMBO ESPADA
kgt.AllowAttack("GM21_1H","L+R","GM1_1H","","GM1_1H_Window","Espada")


#COMBO TECLA DERECHA2
kgt.AllowAttack("GM4_1H","A+R","GM3_1H","","GM3_1H_Window","1H")
kgt.AllowAttack("GM4_1H","&A+R","GM3_1H","","GM3_1H_Window","1H")

#COMBO TECLA DERECHA1
kgt.AllowAttack("GM3_1H","A+R","","GM3_1H//ARMAENANO","GM4_1H_Window","1H")
kgt.AllowAttack("GM3_1H","&A+R","","GM3_1H//ARMAENANO","GM4_1H_Window","1H")

#COMBO ESPADACURVA
kgt.AllowAttack("GM5_1H","L","GM3_1H","","","Espadacurva")

#COMBO DOUBLESWORD
kgt.AllowAttack("GM40_1H","L","GM4_1H","","GM4_1H_Window","DoubleSword")


#COMBO TECLA IZQUIERDA2
kgt.AllowAttack("GM7_1H","A+L","GM6_1H","","GM6_1H_Window","1H")
kgt.AllowAttack("GM7_1H","&A+L","GM6_1H","","GM6_1H_Window","1H")

#COMBO TECLA IZQUIERDA1
kgt.AllowAttack("GM6_1H","A+L","","GM6_1H//ARMAENANO","GM7_1H_Window","1H")
kgt.AllowAttack("GM6_1H","&A+L","","GM6_1H//ARMAENANO","GM7_1H_Window","1H")

#COMBO ESPADAROMANA
kgt.AllowAttack("GM35_1H","F","GM6_1H","","","Espadaromana")

#COMBO QUEENSWORD
kgt.AllowAttack("GM19_1H","B+R","GM6_1H","","GM6_1H_Window","QueenSword")


#COMBO TECLA ABAJO2
kgt.AllowAttack("GM9_1H","A+B","GM8_1H","","GM8_1H_Window","1H")
kgt.AllowAttack("GM9_1H","&A+B","GM8_1H","","GM8_1H_Window","1H")

#COMBO TECLA ABAJO1
kgt.AllowAttack("GM8_1H","A+B","","GM8_1H//ARMAENANO","GM9_1H_Window","1H")
kgt.AllowAttack("GM8_1H","&A+B","","GM8_1H//ARMAENANO","GM9_1H_Window","1H")

#COMBO MAZA2
kgt.AllowAttack("GM22_1H","F","GM8_1H","","","Maza2")

#COMBO MAZA3
kgt.AllowAttack("GM17_1H","R+F","GM8_1H","","GM8_1H_Window","Maza3")



#GI
kgt.AllowAttack("GI_1H","A","","GIM_1H","GIM_1H_Window","1H")







