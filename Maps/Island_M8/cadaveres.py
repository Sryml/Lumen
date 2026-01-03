import darfuncs
from math import pow
import EnemyTypes
import AniSound
import Sparks
import Actions
import pocimac
import Scorer
import Bladex
import GameText

darfuncs.ActualLevel = "MonkeyIsland"

## cabs troc al ppio del nivel

darfuncs.MuertoyTroceado(-149772.697231, 3447.83143969, 27355.5594149,"Knight_Traitor","Espadaelfica",(4,),0)

darfuncs.MuertoyTroceado(-147282.969109, 3147.5603764, 31986.2931443,"Knight_Traitor","",(4,),0)

darfuncs.MuertoyTroceado(-116281.423207, -1069.45965751, 38950.9275737,"Knight_Traitor","",(4,),0)

darfuncs.MuertoyTroceado(-94962.8033113, -1068.88315452, 35224.5628867,"Knight_Traitor","",(4,),0)

darfuncs.MuertoyTroceado(-96233.9046399, -1069.81838602, 28204.0966055,"Knight_Traitor","",(4,),0)


## cab troc inicial tras puente
darfuncs.MuertoyTroceado(-75422.918239, -914.885993878, 29577.0662696,"Knight_Traitor","",(4,),0)


## cab troc junto a cadalso
darfuncs.MuertoyTroceado(-66038.5082641, -509.987625779, -11465.127325,"Knight_Traitor","",(4,),0)


## cab troc inicial tras reja
darfuncs.MuertoyTroceado(-74319.0360326, -1110.62988227, 38079.3541747,"Knight_Traitor","",(4,),0)


## cab troc feliz1
darfuncs.MuertoyTroceado(-75968.7975731, -116.735703874, -25955.5095292,"Knight_Traitor","",(4,),0)


## cab troc feliz2
darfuncs.MuertoyTroceado(-77841.7963453, -111.600058336, -30821.9827165,"Knight_Traitor","",(4,),0)


## cab troc almena
darfuncs.MuertoyTroceado(-73463.9175743, -7870.33648198, 14583.5686346,"Knight_Traitor","",(4,),0)


## cab troc almena2
darfuncs.MuertoyTroceado(-70500.6242621, -7698.6669427, 64660.3236033,"Knight_Traitor","",(4,),0)


## cab troc frente a puerta gorda
darfuncs.MuertoyTroceado(-47660.8462498, -6102.25687565, 78001.3231146,"Knight_Traitor","",(4,),0)


## cab troc junto a zombi
darfuncs.MuertoyTroceado(-56417.401939, -5464.03183912, 29265.3955655,"Knight_Traitor","",(4,),0)


## caballero troceado junto a 2 zombies de espaldas
darfuncs.MuertoyTroceado(-30911.5475784, -5516.97662382, -15384.7960847,"Knight_Traitor","",(4,),0)


## cab troc 1 en primer patio 2 parte
darfuncs.MuertoyTroceado(-52285.6091376, -4534.55904079, -1992.98410512,"Knight_Traitor","",(4,),0)


## cab troc 2 en primer patio 2 parte
darfuncs.MuertoyTroceado(-52554.0970206, -5439.15933027, 9764.22675154,"Knight_Traitor","",(4,),0)


## cab troc 2 en segundo patio 2 parte
darfuncs.MuertoyTroceado(14796.6335789, 1700.18100549, -3849.72243017,"Knight_Traitor","Espadaelfica",(4,),0)


## cab troc 2 en pasaje semi secreto a zona interior
darfuncs.MuertoyTroceado(-61861.2921155, -7719.91382544, -17387.8264468,"Knight_Traitor","",(4,),0)


## cab troc 1 en area exterior "chimeneas"
darfuncs.MuertoyTroceado(-29832.2478351, 101.718596954, -37314.2801146,"Knight_Traitor","",(4,),0)


## cab troc 2 en area exterior "chimeneas"
darfuncs.MuertoyTroceado(-42466.8809197, 94.8669628653, -47849.4531867,"Knight_Traitor","",(4,),0)


## cab troc 3 en area exterior "chimeneas"
#darfuncs.MuertoyTroceado(-42475.8991394, 96.9170083294, -47898.938381,"Knight_Traitor","",(4,),0)


## cab troc 4 en area exterior "chimeneas"
#darfuncs.MuertoyTroceado(-42475.8991394, 96.9170083294, -47898.938381,"Knight_Traitor","",(4,),0)


## cab troc 5 en area exterior "chimeneas"
darfuncs.MuertoyTroceado(-30923.2120223, 100.425333626, -44564.2945642,"Knight_Traitor","",(4,),0)


## cab troc 6 en area exterior "chimeneas"
darfuncs.MuertoyTroceado(-38930.9030858, 124.381793954, -37753.048216,"Knight_Traitor","",(4,),0)

"""
## keleto troceado 1 en piscina verde
-28082.0196278, 4118.89695292, -14474.4298574


## keleto troceado 2 en piscina verde
-28189.3768547, 3364.81753959, -8217.70264225


## keleto troceado 3 en piscina verde
-29831.8372995, 3368.17024237, -6582.64862736


## keleto troceado 4 en piscina verde
-35519.8605605, 3367.75164207, -8621.11511986


## keleto troceado 5 en piscina verde
-49137.5494451, 3062.07523664, -12227.0559355


darfuncs.MuertoyTroceado(106491.067361, 5966.79911185, -23676.371382,"Ork","Hacha",(5,3))
darfuncs.MuertoyTroceado(116529.360884, 5969.88022067, -16772.3161455,"Enano2","",(4,))
darfuncs.MuertoyTroceado(102711.596507, 4619.18290938, -3925.59748387,"Enano2","Hacha",(7,))
darfuncs.MuertoyTroceado(92945.6584756, 4482.22221771, -4373.39763018,"Enano1","",(7,6))
darfuncs.MuertoyTroceado(96391.3798269, 4481.90476733, -52081.9143014,"Ork","",(8,),0)
darfuncs.MuertoyTroceado(101472.507155, 4911.89348965, -48208.5299767,"Enano2","Hacha",(3,))
darfuncs.MuertoyTroceado(90608.9675742, 3283.59541105, -19183.1578147,"Enano1","",(2,))
darfuncs.MuertoyTroceado(116364.72046, 5983.61502442, -31035.81042,"Enano1","Hacha",(2,))
darfuncs.MuertoyTroceado(107163.957337, 5981.42025684, -29476.6655148,"Enano2","",(2,))
darfuncs.MuertoyTroceado(106224.650377, 5983.62243726, -18107.271705,"Enano1","Hacha",(8,))
"""
