import Bladex
import AuxFuncs
import EnemyTypes
import Sparks
import Actions
import math
import Breakings
import pocimac
import Reference
import Enm_Def
import ItemTypes
import darfuncs




####################################
#     Muerto en derrumbamiento     #
####################################

mderr=Bladex.CreateEntity("MuertoDerr", "Knight_Traitor", -15922, -8122, 6600,"Person")
mderr.Angle=3.14159
mderr.Data=Enm_Def.NPCPerson(mderr)
mderr.Blind=1
mderr.Deaf=1
mderr.MeshName="NP_Knight"

### Funcion: Muere2(person)

### Funcion: MuereCaballeroDerr()

MuereCaballeroDerr()



############################################
#     Muerto con llave aposentos duque     #
############################################

mllave=Bladex.CreateEntity("MuertoLlave", "Knight_Traitor", 76, -11121, 19633,"Person")
mllave.Angle=3.14159/2.0
mllave.Data=Enm_Def.NPCPerson(mllave)
mllave.Blind=1
mllave.Deaf=1
mllave.MeshName="NP_Knight"

### Funcion: MuereCaballeroLlave()

MuereCaballeroLlave()



######################################################
#     Muertos camino de la llave aposentos duque     #
######################################################

m1cllave=Bladex.CreateEntity("Muerto1CaminoLlave", "Knight_Traitor", 22172.3739963, -9119.51617909, 5836.31961147,"Person")
m1cllave.Angle=3.14159/4.0
m1cllave.Data=Enm_Def.NPCPerson(m1cllave)
m1cllave.Blind=1
m1cllave.Deaf=1
m1cllave.MeshName="NP_Knight"

### Funcion: MuereCaballero1CaminoLlave()

MuereCaballero1CaminoLlave()


m2cllave=Bladex.CreateEntity("Muerto2CaminoLlave", "Knight_Traitor", 18275.5435651, -9121.43292714, 17199.6363731,"Person")
m2cllave.Angle=0.0
m2cllave.Data=Enm_Def.NPCPerson(m2cllave)
m2cllave.Blind=1
m2cllave.Deaf=1
m2cllave.MeshName="NP_Knight"

### Funcion: MuereCaballero2CaminoLlave()

MuereCaballero2CaminoLlave()




#############################
#     Restos de batalla     #
#############################

darfuncs.MuertoyTroceado(22762.8333387, 427.1, 56986.4914147, "Great_Ork", "Gladius", (1,), 3.6252364721)
#armamuertoexpl1=Bladex.CreateEntity("LabyrArmaMuertoExpl1", "Gladius", 0, 0, 0,"Weapon")
#ItemTypes.ItemDefaultFuncs(armamuertoexpl1)

#saquitomuertoexpl1=Bladex.CreateEntity("Saquitomuertoexpl1","Saquito",0,0,0,"Physic")
#saquitomuertoexpl1.Solid=0
#saquitomuertoexpl1.Scale=1.220190
#pocimac.CreatePotion("Saquitomuertoexpl1")

#muertoexpl1=Bladex.CreateEntity("MuertoExpl1", "Great_Ork", 22762.8333387, 427.1, 56986.4914147,"Person")
#muertoexpl1.Angle=3.6252364721
#Actions.TakeObject(muertoexpl1.Name, armamuertoexpl1.Name)
#Actions.TakeObject(muertoexpl1.Name, saquitomuertoexpl1.Name)
#EnemyTypes.EnemyDefaultFuncs(muertoexpl1)



darfuncs.MuertoyTroceado(21856.1135961, -3122.9, 65230.50303, "Ork", "Gladius", (6,), 4.11387105001)
#armamuertoexpl2=Bladex.CreateEntity("LabyrArmaMuertoExpl2", "Gladius", 0, 0, 0,"Weapon")
#ItemTypes.ItemDefaultFuncs(armamuertoexpl2)

#muertoexpl2=Bladex.CreateEntity("MuertoExpl2", "Ork", 21856.1135961, -3122.9, 65230.50303,"Person")
#muertoexpl2.Angle=4.11387105001
#Actions.TakeObject(muertoexpl2.Name, armamuertoexpl2.Name)
#EnemyTypes.EnemyDefaultFuncs(muertoexpl2)



darfuncs.MuertoyTroceado(24462.3531825, 427.1, 52967.7155989, "Ork", "Gladius", (2,), 0.421446120263)
#armamuertoexpl3=Bladex.CreateEntity("LabyrArmaMuertoExpl3", "Gladius", 0, 0, 0,"Weapon")
#ItemTypes.ItemDefaultFuncs(armamuertoexpl3)

#muertoexpl3=Bladex.CreateEntity("MuertoExpl3", "Ork", 24462.3531825, 427.1, 52967.7155989,"Person")
#muertoexpl3.Angle=0.421446120263
#Actions.TakeObject(muertoexpl3.Name, armamuertoexpl3.Name)
#EnemyTypes.EnemyDefaultFuncs(muertoexpl3)



darfuncs.MuertoyTroceado(-5184.27382867, 677.1, -50070.0213544, "Ork", "Gladius", (3,), 5.04592805016)
#armamuertoexpl4=Bladex.CreateEntity("LabyrArmaMuertoExpl4", "Gladius", 0, 0, 0,"Weapon")
#ItemTypes.ItemDefaultFuncs(armamuertoexpl4)

#muertoexpl4=Bladex.CreateEntity("MuertoExpl4", "Ork", -5184.27382867, 677.1, -50070.0213544,"Person")
#muertoexpl4.Angle=5.04592805016
#Actions.TakeObject(muertoexpl4.Name, armamuertoexpl4.Name)
#EnemyTypes.EnemyDefaultFuncs(muertoexpl4)



#darfuncs.MuertoyTroceado(-5184.27382867, 677.1, -50070.0213544, "Ork", "Gladius", (5,), 5.04592805016)
#armamuertoexpl5=Bladex.CreateEntity("LabyrArmaMuertoExpl5", "Gladius", 0, 0, 0,"Weapon")
#ItemTypes.ItemDefaultFuncs(armamuertoexpl5)

#muertoexpl5=Bladex.CreateEntity("MuertoExpl5", "Ork", -5184.27382867, 677.1, -50070.0213544,"Person")
#muertoexpl5.Angle=5.04592805016
#Actions.TakeObject(muertoexpl5.Name, armamuertoexpl5.Name)
#EnemyTypes.EnemyDefaultFuncs(muertoexpl5)



darfuncs.MuertoyTroceado(-63184.6282865, -822.9, -17923.0444385, "Great_Ork", "Gladius", (3,), 3.20980137659)
#armamuertoexpl6=Bladex.CreateEntity("LabyrArmaMuertoExpl6", "Gladius", 0, 0, 0,"Weapon")
#ItemTypes.ItemDefaultFuncs(armamuertoexpl6)

#muertoexpl6=Bladex.CreateEntity("MuertoExpl6", "Great_Ork", -63184.6282865, -822.9, -17923.0444385,"Person")
#muertoexpl6.Angle=3.20980137659
#Actions.TakeObject(muertoexpl6.Name, armamuertoexpl6.Name)
#EnemyTypes.EnemyDefaultFuncs(muertoexpl6)



darfuncs.MuertoyTroceado(7207.73695806, -1322.9, 25043.2790502, "Ork", "Gladius", (4,), 0.289919754025)
#armamuertoexpl7=Bladex.CreateEntity("LabyrArmaMuertoExpl7", "Gladius", 0, 0, 0,"Weapon")
#ItemTypes.ItemDefaultFuncs(armamuertoexpl7)

#muertoexpl7=Bladex.CreateEntity("MuertoExpl7", "Ork", 7207.73695806, -1322.9, 25043.2790502,"Person")
#muertoexpl7.Angle=0.289919754025
#Actions.TakeObject(muertoexpl7.Name, armamuertoexpl7.Name)
#EnemyTypes.EnemyDefaultFuncs(muertoexpl7)



darfuncs.MuertoyTroceado(-6482.02630097, -1322.9, 26090.4510005, "Ork", "Gladius", (4,), 5.22748736786)
#armamuertoexpl8=Bladex.CreateEntity("LabyrArmaMuertoExpl8", "Gladius", 0, 0, 0,"Weapon")
#ItemTypes.ItemDefaultFuncs(armamuertoexpl8)

#muertoexpl8=Bladex.CreateEntity("MuertoExpl8", "Ork", -6482.02630097, -1322.9, 26090.4510005,"Person")
#muertoexpl8.Angle=5.22748736786
#Actions.TakeObject(muertoexpl8.Name, armamuertoexpl8.Name)
#EnemyTypes.EnemyDefaultFuncs(muertoexpl8)



darfuncs.MuertoyTroceado(4631.7951937, -11322.9, 160.647533788, "Great_Ork", "Gladius", (3,), 1.6087156958)
#armamuertoint1=Bladex.CreateEntity("LabyrArmamuertoint1", "Gladius", 0, 0, 0,"Weapon")
#ItemTypes.ItemDefaultFuncs(armamuertoint1)

#muertoint1=Bladex.CreateEntity("MuertoInt1", "Great_Ork", 4631.7951937, -11322.9, 160.647533788,"Person")
#muertoint1.Angle=1.6087156958
#Actions.TakeObject(muertoint1.Name, armamuertoint1.Name)
#EnemyTypes.EnemyDefaultFuncs(muertoint1)



darfuncs.MuertoyTroceado(-13176.3804173, -10572.9, -2489.03053946, "Ork", "Gladius", (6,), 2.19288423389)
#armamuertoint2=Bladex.CreateEntity("LabyrArmamuertoint2", "Gladius", 0, 0, 0,"Weapon")
#ItemTypes.ItemDefaultFuncs(armamuertoint2)

#muertoint2=Bladex.CreateEntity("MuertoInt2", "Ork", -13176.3804173, -10572.9, -2489.03053946,"Person")
#muertoint2.Angle=2.19288423389
#Actions.TakeObject(muertoint1.Name, armamuertoint2.Name)
#EnemyTypes.EnemyDefaultFuncs(muertoint2)








######## Funcion: MuertosyTroceados()



#Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, MuertosyTroceados, ())



