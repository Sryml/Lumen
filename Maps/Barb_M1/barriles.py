

import Breakings
import Actions
BoxBurnTime = 6
BoxDestroyTime = 12
import Torchs
import pocimac


#################################################
###    Barriles primera caseta     ##############
#################################################

#Torchs.SetUsable("dantorcha1",3,3,50)
#Torchs.SetUsable("antorchaen1",3,3,-1)


#######1
pan=Breakings.CreateHiddenObject("pancom11", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pancom11")
Actions.SetBurnable("barcas11",BoxBurnTime,BoxDestroyTime)
Breakings.SetBreakable("barcas11",12,100,"pancom11")

########2
Breakings.SetBreakable("barcas12",12,100)
Actions.SetBurnable("barcas12",BoxBurnTime,BoxDestroyTime)

#######3
pan=Breakings.CreateHiddenObject("pancom13", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pancom13")
Breakings.SetBreakable("barcas13",12,100,"pancom13")
Actions.SetBurnable("barcas13",BoxBurnTime,BoxDestroyTime)

#######3
Breakings.SetBreakable("cajcas11",12,100)
Actions.SetBurnable("cajcas11",BoxBurnTime,BoxDestroyTime)

########################################
###      cajas en segunda caseta     ###
########################################


###1


pan=Breakings.CreateHiddenObject("pancom21", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pancom21")

o=Bladex.CreateEntity("cajacas21","Cajon2",-54257.811159,-11595.905065,-29141.436099,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("cajacas21",12,100,"pancom21")
Actions.SetBurnable("cajacas21",BoxBurnTime,BoxDestroyTime)

###2

o=Bladex.CreateEntity("cajacas22","Cajon2",-54145.630660,-11704.475168,-27142.932227,"Physic")
o.Scale=1.184304
o.Orientation=0.589646,0.589646,-0.390278,0.390278
Breakings.SetBreakable("cajacas22",12,100)
Actions.SetBurnable("cajacas21",BoxBurnTime,BoxDestroyTime)

####################################################
####    cajas en casa del moco               #######
####################################################

Breakings.SetBreakable("cajase1",12,100)
Actions.SetBurnable("cajase1",BoxBurnTime,BoxDestroyTime)
#
pan=Breakings.CreateHiddenObject("panse2", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panse2")

Breakings.SetBreakable("cajase2",12,100,"panse2")
Actions.SetBurnable("cajase2",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("cajase3",12,100)
Actions.SetBurnable("cajase3",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("cajase4",12,100)
Actions.SetBurnable("cajase4",BoxBurnTime,BoxDestroyTime)
#
#Breakings.SetBreakable("cajabse5",12,100)
Actions.SetBurnable("cajabse5",BoxBurnTime,BoxDestroyTime)
#
#Breakings.SetBreakable("cajabse6",12,100)
Actions.SetBurnable("cajabse6",BoxBurnTime,BoxDestroyTime)
#

################################################################
####    cajas para romper en la casa de trepar           #######
################################################################

#
Breakings.SetBreakable("cajonpu1",12,100)
Actions.SetBurnable("cajonpu1",BoxBurnTime,BoxDestroyTime)

#
Breakings.SetBreakable("cajonpu2",12,100)
Actions.SetBurnable("cajonpu2",BoxBurnTime,BoxDestroyTime)

#
Breakings.SetBreakable("cajonpu3",12,100)
Actions.SetBurnable("cajonpu3",BoxBurnTime,BoxDestroyTime)

#
Breakings.SetBreakable("cajonpu4",12,100)
Actions.SetBurnable("cajonpu4",BoxBurnTime,BoxDestroyTime)

#
Breakings.SetBreakable("cajonpu5",12,100)
Actions.SetBurnable("cajonpu5",BoxBurnTime,BoxDestroyTime)

#
Breakings.SetBreakable("cajonpu6",12,100)
Actions.SetBurnable("cajonpu6",BoxBurnTime,BoxDestroyTime)

#
Breakings.SetBreakable("cajonpu7",12,100)
Actions.SetBurnable("cajonpu7",BoxBurnTime,BoxDestroyTime)



####################################################
####    tinajas en la casa del rio           #######
####################################################

####1
pan=Breakings.CreateHiddenObject("pancom31", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pancom31")

o=Bladex.CreateEntity("tincas31","Tinaja",-192278.495802,-10769.776788,160836.728708,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("tincas31",10,60,"pancom31")

####2
o=Bladex.CreateEntity("tincas32","Tinaja",-191355.387131,-10760.608748,161131.519326,"Physic")
o.Scale=1.000000
o.Orientation=0.478123,0.855413,-0.019047,0.198254


queso=Breakings.CreateHiddenObject("queso32", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
queso.Solid=1
queso.Static=0
pocimac.CreateFood("queso32")
Breakings.SetBreakable("tincas32",10,60,"queso32")

####3
o=Bladex.CreateEntity("tincas33","Tinaja",-191065.084981,-10414.603190,162373.302315,"Physic")
o.Scale=1.000000
o.Orientation=0.825261,-0.032532,-0.523695,0.208876
Breakings.SetBreakable("tincas33",10,60)

#####  PLANTA BAJA ###############

####1
o=Bladex.CreateEntity("barcas31","Barril",-196152.724268,-2539.324552,165714.823857,"Physic")
o.Scale=2.006763
o.Orientation=0.707107,0.707107,0.000000,0.00000

Breakings.SetBreakable("barcas31",10,60)
Actions.SetBurnable("barcas31",BoxBurnTime,BoxDestroyTime)


####2
o=Bladex.CreateEntity("barcas32","Barril",-196156.334361,-2541.679624,167773.118881,"Physic")
o.Scale=2.006763
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("barcas32",10,60)
Actions.SetBurnable("barcas32",BoxBurnTime,BoxDestroyTime)

####################################################
#####     Caseta de la escalera                 ####
####################################################

####1
o=Bladex.CreateEntity("tincas61","Tinaja",-138139.683007,-19594.115410,177258.099367,"Physic")
o.Scale=1.000000
o.Orientation=0.289885,-0.478920,-0.787681,0.257219
Breakings.SetBreakable("tincas61",10,60)

####2
o=Bladex.CreateEntity("tincas62","Tinaja",-139083.857151,-19971.853454,177541.021288,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("tincas62",10,60)

####3
o=Bladex.CreateEntity("tincas63","Tinaja",-140139.927933,-19616.703004,178614.700228,"Physic")
o.Scale=1.000000
o.Orientation=0.843011,0.024238,-0.017279,0.537072
Breakings.SetBreakable("tincas63",10,60)


###################################################
####     tinajas en el almacen                 ####
###################################################

####1
o=Bladex.CreateEntity("tincas81","Tinaja",-122415.285186,-23772.495031,173020.163138,"Physic")
o.Scale=1.000000
o.Orientation=0.602908,0.602908,0.369462,-0.369462
Breakings.SetBreakable("tincas81",10,60)

####2
o=Bladex.CreateEntity("tincas82","Tinaja",-121856.111696,-23771.672242,171828.369297,"Physic")
o.Scale=1.000000
o.Orientation=0.606109,0.606109,0.364187,-0.364187

Breakings.SetBreakable("tincas82",10,60)

####3
o=Bladex.CreateEntity("tincas83","Tinaja",-121415.562985,-23768.837211,170805.189009,"Physic")
o.Scale=1.000000
o.Orientation=0.491198,0.491198,0.508650,-0.508650
Breakings.SetBreakable("tincas83",10,60)

####4
o=Bladex.CreateEntity("tincas84","Tinaja",-120591.474081,-23406.944286,171751.269138,"Physic")
o.Scale=1.000000
o.Orientation=0.313681,0.774215,0.460815,0.299742
Breakings.SetBreakable("tincas84",10,60)

####5
o=Bladex.CreateEntity("tincas85","Tinaja",-120471.817827,-23419.573686,169676.240226,"Physic")
o.Scale=1.000000
o.Orientation=0.125668,-0.667117,-0.208443,0.704070
Breakings.SetBreakable("tincas85",10,60)

#############   CAJAS    ##############

####1

o=Bladex.CreateEntity("cajcas81","Cajon2",-122834.481560,-24168.945273,187856.623625,"Physic")
o.Scale=1.184304
o.Orientation=0.623450,0.700050,0.333521,0.100019
Breakings.SetBreakable("cajcas81",10,60)
Actions.SetBurnable("cajcas81",BoxBurnTime,BoxDestroyTime)

####2
o=Bladex.CreateEntity("cajcas82","Cajon2",-123476.992296,-23871.005817,186120.963230,"Physic")
o.Scale=1.000000
o.Orientation=0.241185,0.664574,0.664899,0.240996
Breakings.SetBreakable("cajcas82",10,60)
Actions.SetBurnable("cajcas82",BoxBurnTime,BoxDestroyTime)

####3
o=Bladex.CreateEntity("cajcas83","Cajon2",-120129.248117,-23601.874579,186996.942073,"Physic")
o.Scale=1.000000
o.Orientation=0.692911,0.692911,0.140974,-0.140974
Breakings.SetBreakable("cajcas83",10,60)
Actions.SetBurnable("cajcas83",BoxBurnTime,BoxDestroyTime)

####4
o=Bladex.CreateEntity("cajcas84","Cajon2",-113055.877792,-23760.104939,183298.579019,"Physic")
o.Scale=1.269735
o.Orientation=0.683013,0.683013,0.183013,-0.183013
Breakings.SetBreakable("cajcas84",10,60)
Actions.SetBurnable("cajcas84",BoxBurnTime,BoxDestroyTime)

##############   BARRILES   ####################


####1
o=Bladex.CreateEntity("barcas81","Barril",-119146.216762,-23646.361170,181740.885991,"Physic")
o.Scale=1.533978
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("barcas81",10,60)
Actions.SetBurnable("barcas81",BoxBurnTime,BoxDestroyTime)

####2
o=Bladex.CreateEntity("barcas82","Barril",-115035.471964,-23721.418600,185086.405280,"Physic")
o.Scale=1.728525
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("barcas82",10,60)
Actions.SetBurnable("barcas82",BoxBurnTime,BoxDestroyTime)

######################################

####CAJON TORRE PUERTA

queso=Breakings.CreateHiddenObject("quesoto", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
queso.Solid=1
pocimac.CreateFood("quesoto")

Breakings.SetBreakable("cajonto1",12,30,"quesoto")
#Breakings.SetBreakable("cajonto1",12,30)
Actions.SetBurnable("cajonto1",BoxBurnTime,BoxDestroyTime)


####CAJONES SUBIDA AL POBLADO

#
pan=Breakings.CreateHiddenObject("pancajon1", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("pancajon1")

Breakings.SetBreakable("cajon1",12,30,"pancajon1")
Actions.SetBurnable("cajon1",BoxBurnTime,BoxDestroyTime)

#
pan=Breakings.CreateHiddenObject("pancajon2", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("pancajon2")

Breakings.SetBreakable("cajon2",12,30,"pancajon2")
Actions.SetBurnable("cajon2",BoxBurnTime,BoxDestroyTime)

#
Breakings.SetBreakable("cajon3",12,30)
Actions.SetBurnable("cajon3",BoxBurnTime,BoxDestroyTime)



Breakings.SetBreakable("cajon4",12,30)
Actions.SetBurnable("cajon4",BoxBurnTime,BoxDestroyTime)

Breakings.SetBreakable("Miguelin",12,30)
Actions.SetBurnable("Miguelin",BoxBurnTime,BoxDestroyTime)


####casa-gruta-pueblo1
Breakings.SetBreakable("cajon5",12,30)
Actions.SetBurnable("cajon5",BoxBurnTime,BoxDestroyTime)

Breakings.SetBreakable("cajon6",12,30)
Actions.SetBurnable("cajon6",BoxBurnTime,BoxDestroyTime)


Breakings.SetBreakable("cajon7",12,30)
Actions.SetBurnable("cajon7",BoxBurnTime,BoxDestroyTime)

Breakings.SetBreakable("cajon8",12,30)
Actions.SetBurnable("cajon8",BoxBurnTime,BoxDestroyTime)

Breakings.SetBreakable("cajon9",12,30)
Actions.SetBurnable("cajon9",BoxBurnTime,BoxDestroyTime)


###	CASA-GRUTA-PUEBLO 2

#
Breakings.SetBreakable("barril1",12,30)
Actions.SetBurnable("barril1",BoxBurnTime,BoxDestroyTime)

#
pan=Breakings.CreateHiddenObject("panbarril2", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("panbarril2")

Breakings.SetBreakable("barril2",12,30,"panbarril2")
Actions.SetBurnable("barril2",BoxBurnTime,BoxDestroyTime)

#
Breakings.SetBreakable("barril3",12,30)
Actions.SetBurnable("barril3",BoxBurnTime,BoxDestroyTime)

#
carne=Breakings.CreateHiddenObject("carnebarril4", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
carne.Solid=1
pocimac.CreateFood("carnebarril4")

Breakings.SetBreakable("barril4",12,30,"carnebarril4")
Actions.SetBurnable("barril4",BoxBurnTime,BoxDestroyTime)



#
Breakings.SetBreakable("barril5",12,30)
Actions.SetBurnable("barril5",BoxBurnTime,BoxDestroyTime)

#
Breakings.SetBreakable("barril6",12,30)
Actions.SetBurnable("barril6",BoxBurnTime,BoxDestroyTime)

###2º PISO CASA ESCALERA
#
pan=Breakings.CreateHiddenObject("panbarril7", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("panbarril7")

Breakings.SetBreakable("barril7",12,30,"panbarril7")
Actions.SetBurnable("barril7",BoxBurnTime,BoxDestroyTime)

#
Breakings.SetBreakable("barril8",12,30)
Actions.SetBurnable("barril8",BoxBurnTime,BoxDestroyTime)



Breakings.SetBreakable("tinaja1",12,30)
Actions.SetBurnable("tinaja1",BoxBurnTime,BoxDestroyTime)



Breakings.SetBreakable("mesa1",10,15)

Breakings.SetBreakable("mesa2",10,15)

Breakings.SetBreakable("cofre1",10,15)


Bladex.AddCombustionDataFor("Caja_i_i", "LargeFire", 250, 400, 4, 1, 1, (BoxBurnTime+BoxDestroyTime)*2)
Bladex.AddCombustionDataFor("Cajon2", "LargeFire", 250, 400, 4, 1, 1, (BoxBurnTime+BoxDestroyTime)*2)
Bladex.AddCombustionDataFor("CajonPieza1", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza2", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza3", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza4", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza5", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza6", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza7", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza8", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza9", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza10", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza11", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza12", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza13", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza14", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza15", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza16", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza17", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza18", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("Barril", "LargeFire", 250, 400, 4, 1.5, 1, (BoxBurnTime+BoxDestroyTime)*3)
Bladex.AddCombustionDataFor("BarrilPieza1", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza2", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza3", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza4", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza5", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza6", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
