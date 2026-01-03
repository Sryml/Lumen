import Breakings
import Actions
BoxBurnTime = 6
BoxDestroyTime = 12
import Torchs
import pocimac

#########ALMACEN##########
#########################
o=Bladex.CreateEntity("CAJAL1","Cajon2",-25624.477682,48761.425391,14197.777993,"Physic")
o.Scale=1.244716
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("CAJAL1",12,100)
Actions.SetBurnable("CAJAL1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CAJAL2","Cajon2",-25323.050671,47380.301120,14304.157633,"Physic")
o.Scale=1.244716
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("pan2", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pan2")
Breakings.SetBreakable("CAJAL2",12,100,"pan2")
Actions.SetBurnable("CAJAL2",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARAL3","Barril",-22570.711477,48880.780610,13851.877367,"Physic")
o.Scale=1.474123
o.Orientation=0.704729,0.709367,0.008311,-0.009275
Breakings.SetBreakable("BARAL3",12,100)
Actions.SetBurnable("BARAL3",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARAL4","Barril",-23079.462584,48932.158951,14573.332608,"Physic")
o.Scale=1.347849
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("pan1", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pan1")
Breakings.SetBreakable("BARAL4",12,100,"pan1")
Actions.SetBurnable("BARAL4",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARAL5","Barril",-25874.361496,48669.084614,11984.176556,"Physic")
o.Scale=1.986894
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("pan3", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pan3")
Breakings.SetBreakable("BARAL5",12,100,"pan3")
Actions.SetBurnable("BARAL5",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARAL6","Barril",-25682.699642,48854.946749,10128.856050,"Physic")
o.Scale=1.533978
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARAL6",12,100)
Actions.SetBurnable("BARAL6",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARAL7","Barril",-24607.585943,48941.122560,10810.605457,"Physic")
o.Scale=1.321291
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARAL7",12,100)
Actions.SetBurnable("BARAL7",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARAL8","Barril",-24560.263661,48784.165853,11897.865443,"Physic")
o.Scale=1.711410
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARAL8",12,100)
Actions.SetBurnable("BARAL8",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("TINAL9","Tinaja",-13538.612546,48434.210670,14557.570679,"Physic")
o.Scale=1.388690
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("ques111", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("ques111")
Breakings.SetBreakable("TINAL9",12,100,"ques111")


o=Bladex.CreateEntity("TINAL11","Tinaja",-14408.219252,48724.055752,12748.281106,"Physic")
o.Scale=1.000000
o.Orientation=0.104517,0.104517,0.699340,-0.699340
Breakings.SetBreakable("TINAL11",12,100)





#######9 BARRILES + 2 CAJONES EN LA GARITA
"""
o=Bladex.CreateEntity("CAJGAR1","Cajon2",49150.637361,49204.572110,-3493.554491,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("CAJGAR1",12,100)
Actions.SetBurnable("CAJGAR1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARGAR1","Barril",49375.651996,49286.257646,-4612.688549,"Physic")
o.Scale=1.220190
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("ques113", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("ques113")
Breakings.SetBreakable("BARGAR1",12,100,"ques113")
Actions.SetBurnable("BARGAR1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARGAR2","Barril",50835.999159,49284.225866,-3593.415287,"Physic")
o.Scale=1.220190
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARGAR2",12,100)
Actions.SetBurnable("BARGAR2",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BARGAR3","Barril",50452.015688,49363.257091,-4477.456967,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARGAR3",12,100)
Actions.SetBurnable("BARGAR3",BoxBurnTime,BoxDestroyTime)
"""

o=Bladex.CreateEntity("CAJGAR2","Cajon2",55678.921091,49061.234559,-4360.791337,"Physic")
o.Scale=1.244716
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("pan333", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pan333")
Breakings.SetBreakable("CAJGAR2",12,100,"pan333")
Actions.SetBurnable("CAJGAR2",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARGAR4","Barril",55883.254306,47874.241750,-4283.729225,"Physic")
o.Scale=1.295256
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARGAR4",12,100)
Actions.SetBurnable("BARGAR4",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARGAR5","Barril",55064.858760,47988.147082,-4423.514730,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARGAR5",12,100)
Actions.SetBurnable("BARGAR5",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARGAR6","Barril",55646.912553,49259.333414,-6411.520537,"Physic")
o.Scale=1.282432
Breakings.SetBreakable("BARGAR6",12,100)
Actions.SetBurnable("BARGAR6",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARGAR7","Barril",56268.417491,49375.439644,-6015.837907,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("pan334", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pan334")
Breakings.SetBreakable("BARGAR7",12,100,"pan334")
Actions.SetBurnable("BARGAR7",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARGAR8","Barril",56574.756924,49213.145726,-7139.744773,"Physic")
o.Scale=1.388690
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARGAR8",12,100)
Actions.SetBurnable("BARGAR8",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARGAR9","Barril",56311.798096,49246.154071,-8081.798402,"Physic")
o.Scale=1.308209
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARGAR9",12,100)
Actions.SetBurnable("BARGAR9",BoxBurnTime,BoxDestroyTime)



######8 BARRILES + 9 TINAJAS EN LA SALA DE VIGIA DETRAS DEL COMEDOR. PLANTA BAJA

o=Bladex.CreateEntity("TINVIG1","Tinaja",16955.382718,30856.008046,21680.586486,"Physic")
o.Scale=1.488864
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panobst3", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panobst3")
Breakings.SetBreakable("TINVIG1",12,100,"panobst3")



o=Bladex.CreateEntity("TINVIG2","Tinaja",18245.622553,31128.364162,21111.376565,"Physic")
o.Scale=1.126825
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("TINVIG2",12,100)



o=Bladex.CreateEntity("TINVIG3","Tinaja",16829.916145,31003.372514,20261.228810,"Physic")
o.Scale=1.295256
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("TINVIG3",12,100)



o=Bladex.CreateEntity("BARVIG1","Barril",19922.725455,31407.335687,21584.691496,"Physic")
o.Scale=1.402577
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARVIG1",12,100)
Actions.SetBurnable("BARVIG1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARVIG2","Barril",19827.901356,31461.821665,20767.560961,"Physic")
o.Scale=1.269735
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARVIG2",12,100)
Actions.SetBurnable("BARVIG2",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARVIG3","Barril",18981.790984,31441.017951,20250.085077,"Physic")
o.Scale=1.334504
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("pancarr1", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pancarr1")
Breakings.SetBreakable("BARVIG3",12,100,"pancarr1")
Actions.SetBurnable("BARVIG3",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARVIG4","Barril",11421.101317,31373.011723,21499.061157,"Physic")
o.Scale=1.488864
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARVIG4",12,100)
Actions.SetBurnable("BARVIG4",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARVIG5","Barril",10324.830875,31414.977100,21309.367110,"Physic")
o.Scale=1.388690
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARVIG5",12,100)
Actions.SetBurnable("BARVIG5",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARVIG6","Barril",11529.729854,31471.598025,20554.291358,"Physic")
o.Scale=1.244716
o.Orientation=0.702860,0.708392,0.041620,-0.049366
pan=Breakings.CreateHiddenObject("pancarr3", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pancarr3")
Breakings.SetBreakable("BARVIG6",12,100,"pancarr3")
Actions.SetBurnable("BARVIG6",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("TINVIG4","Tinaja",8805.235353,31012.506923,21329.221584,"Physic")
o.Scale=1.282432
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("TINVIG4",12,100)



o=Bladex.CreateEntity("TINVIG5","Tinaja",3344.138403,31025.587498,21750.454615,"Physic")
o.Scale=1.269735
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("TINVIG5",12,100)



o=Bladex.CreateEntity("TINVIG6","Tinaja",2218.062761,31046.841310,21229.535103,"Physic")
o.Scale=1.244716
o.Orientation=0.541675,0.541675,0.454519,-0.454519
Breakings.SetBreakable("TINVIG6",12,100)



o=Bladex.CreateEntity("TINVIG7","Tinaja",3635.633157,30974.226106,20205.565574,"Physic")
o.Scale=1.334504
o.Orientation=0.553388,0.553388,0.440184,-0.440184
Breakings.SetBreakable("TINVIG7",12,100)



o=Bladex.CreateEntity("BARVIG7","Barril",442.466235,31423.938431,21206.267147,"Physic")
o.Scale=1.361327
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("pangem0", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pangem0")
Breakings.SetBreakable("BARVIG7",12,100,"pangem0")
Actions.SetBurnable("BARVIG7",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARVIG8","Barril",1321.521583,31418.733782,20650.233803,"Physic")
o.Scale=1.374941
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARVIG8",12,100)
Actions.SetBurnable("BARVIG8",BoxBurnTime,BoxDestroyTime)



##########BARRILES Y TINAJAS EN EL COMEDOR

o=Bladex.CreateEntity("BTCOM1","Tinaja",15932.347297,30866.742008,39537.441568,"Physic")
o.Scale=1.474123
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BTCOM1",12,100)



o=Bladex.CreateEntity("BTCOM2","Tinaja",16620.636686,30966.300105,40843.707085,"Physic")
o.Scale=1.347849
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("pangem1", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pangem1")
Breakings.SetBreakable("BTCOM2",12,100,"pangem1")



o=Bladex.CreateEntity("BTCOM3","Tinaja",17184.342397,30845.677341,38335.772495,"Physic")
o.Scale=1.503752
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BTCOM3",12,100)


o=Bladex.CreateEntity("BTCOM4","Tinaja",16762.211804,25019.549480,36005.703348,"Physic")
o.Scale=1.269735
o.Orientation=0.703538,0.701732,0.079124,-0.079663
Breakings.SetBreakable("BTCOM4",12,100)



o=Bladex.CreateEntity("BTCOM5","Tinaja",18082.932502,24898.544568,36093.077067,"Physic")
o.Scale=1.430769
o.Orientation=0.649014,0.649583,0.283486,-0.276513
pan=Breakings.CreateHiddenObject("pangem5", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pangem5")
Breakings.SetBreakable("BTCOM5",12,100,"pangem5")



o=Bladex.CreateEntity("BTCOM6","Barril",16225.325665,31342.061648,42641.724209,"Physic")
o.Scale=1.564811
o.Orientation=0.706445,0.707098,0.021490,-0.022042
Breakings.SetBreakable("BTCOM6",12,100)
Actions.SetBurnable("BTCOM6",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BTCOM7","Barril",15843.632508,31339.731550,43727.127963,"Physic")
o.Scale=1.580459
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panfin11", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panfin11")
Breakings.SetBreakable("BTCOM7",12,100,"panfin11")
Actions.SetBurnable("BTCOM7",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BTCOM8","Barril",17369.549323,31429.774792,41879.697177,"Physic")
o.Scale=1.347849
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BTCOM8",12,100)
Actions.SetBurnable("BTCOM8",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BTCOM9","Barril",17860.253180,31613.588556,43448.885638,"Physic")
o.Scale=1.282432
o.Orientation=0.827249,0.025289,0.047144,0.559283
Breakings.SetBreakable("BTCOM9",12,100)
Actions.SetBurnable("BTCOM9",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BTCOM10","Barril",16774.795252,31676.858013,44877.167745,"Physic")
o.Scale=1.000000
o.Orientation=0.712432,-0.119163,-0.673012,0.159048
pan=Breakings.CreateHiddenObject("panfin12", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panfin12")
Breakings.SetBreakable("BTCOM10",12,100,"panfin12")
Actions.SetBurnable("BTCOM10",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BTCOM11","Barril",3689.855460,31352.967552,40698.018695,"Physic")
o.Scale=1.533978
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panfin13", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panfin13")
Breakings.SetBreakable("BTCOM11",12,100,"panfin13")
Actions.SetBurnable("BTCOM11",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BTCOM12","Barril",3603.599773,31385.219353,41858.240033,"Physic")
o.Scale=1.459527
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BTCOM12",12,100)
Actions.SetBurnable("BTCOM12",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BTCOM13","Barril",2548.986727,31415.300612,41238.035346,"Physic")
o.Scale=1.388690
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panfin18", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panfin18")
Breakings.SetBreakable("BTCOM13",12,100,"panfin18")
Actions.SetBurnable("BTCOM13",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BTCOM14","Barril",3228.370494,31601.018238,43561.493413,"Physic")
o.Scale=1.321291
o.Orientation=0.582448,0.401992,-0.591741,-0.386004
Breakings.SetBreakable("BTCOM14",12,100)
Actions.SetBurnable("BTCOM14",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BTCOM15","Barril",2275.273815,31607.761581,42505.451416,"Physic")
o.Scale=1.334504
o.Orientation=0.539786,0.254502,-0.170543,-0.784076
Breakings.SetBreakable("BTCOM15",12,100)
Actions.SetBurnable("BTCOM15",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BTCOM16","Barril",4534.738960,31696.133281,41171.210556,"Physic")
o.Scale=1.000000
o.Orientation=0.214847,0.182853,0.020725,0.959154
pan=Breakings.CreateHiddenObject("panarac1", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panarac1")
Breakings.SetBreakable("BTCOM16",12,100,"panarac1")
Actions.SetBurnable("BTCOM16",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BTCOM17","Barril",-1013.975137,31382.690981,38207.456147,"Physic")
o.Scale=1.474123
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BTCOM17",12,100)
Actions.SetBurnable("BTCOM17",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BTCOM18","Barril",-755.561885,31428.059020,40769.869612,"Physic")
o.Scale=1.347849
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panarac2", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panarac2")
Breakings.SetBreakable("BTCOM18",12,100,"panarac2")
Actions.SetBurnable("BTCOM18",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BTCOM19","Tinaja",-421.152820,30943.625706,39325.398407,"Physic")
o.Scale=1.374941
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BTCOM19",12,100)


o=Bladex.CreateEntity("BTCOM20","Tinaja",3080.276995,30909.712501,39326.856102,"Physic")
o.Scale=1.416603
o.Orientation=0.651013,0.653977,-0.274234,0.270726
Breakings.SetBreakable("BTCOM20",12,100)


o=Bladex.CreateEntity("BTCOM21","Tinaja",2949.990127,25030.941309,36337.681017,"Physic")
o.Scale=1.257163
o.Orientation=0.521334,0.521334,-0.477714,0.477714
Breakings.SetBreakable("BTCOM21",12,100)


o=Bladex.CreateEntity("BTCOM22","Tinaja",1591.700773,25032.916162,36577.662219,"Physic")
o.Scale=1.257163
o.Orientation=0.643440,0.643440,-0.293232,0.293232
Breakings.SetBreakable("BTCOM22",12,100)


############## MAZMORRAS. BARRILES #######

o=Bladex.CreateEntity("BARMAZ0","Barril",17514.249968,45429.813363,33887.835763,"Physic")
o.Scale=1.347849
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARMAZ0",12,100)
Actions.SetBurnable("BARMAZ0",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARMAZ1","Barril",18615.879012,45349.072463,34437.635963,"Physic")
o.Scale=1.549318
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARMAZ1",12,100)
Actions.SetBurnable("BARMAZ1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BARMAZ2","Barril",18408.861363,45334.088224,33291.088805,"Physic")
o.Scale=1.580459
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARMAZ2",12,100)
Actions.SetBurnable("BARMAZ2",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BARMAZ3","Barril",17006.995369,45574.874853,33019.008344,"Physic")
o.Scale=1.374941
o.Orientation=0.862658,-0.086525,-0.466558,0.175092
Breakings.SetBreakable("BARMAZ3",12,100)
Actions.SetBurnable("BARMAZ3",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BARMAZ4","Barril",16817.907126,45394.287054,32028.389115,"Physic")
o.Scale=1.430769
o.Orientation=0.705168,0.708980,-0.007403,0.005561
Breakings.SetBreakable("BARMAZ4",12,100)
Actions.SetBurnable("BARMAZ4",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BARMAZ5","Barril",17155.539766,44754.604516,33376.408358,"Physic")
o.Scale=1.184304
o.Orientation=0.811159,0.579022,0.075356,0.032811
Breakings.SetBreakable("BARMAZ5",12,100)
Actions.SetBurnable("BARMAZ5",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BARMAZ6","Barril",1561.799880,45574.621553,33200.338059,"Physic")
o.Scale=1.459527
o.Orientation=0.393557,0.582555,-0.377808,-0.602498
Breakings.SetBreakable("BARMAZ6",12,100)
Actions.SetBurnable("BARMAZ6",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BARMAZ7","Barril",2217.768215,45586.310262,34208.978590,"Physic")
o.Scale=1.416603
o.Orientation=0.384439,0.598584,-0.401645,-0.576702
Breakings.SetBreakable("BARMAZ7",12,100)
Actions.SetBurnable("BARMAZ7",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BARMAZ8","Barril",3028.125685,45403.176102,32550.902333,"Physic")
o.Scale=1.416603
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARMAZ8",12,100)
Actions.SetBurnable("BARMAZ8",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BARMAZ9","Barril",2917.450767,45417.880775,33459.564199,"Physic")
o.Scale=1.549318
o.Orientation=0.474195,0.573218,0.093319,0.661704
Breakings.SetBreakable("BARMAZ9",12,100)
Actions.SetBurnable("BARMAZ9",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BARMAZ10","Barril",2198.988044,45619.817360,32152.065395,"Physic")
o.Scale=1.321291
o.Orientation=0.009798,0.981602,-0.190639,-0.004327
Breakings.SetBreakable("BARMAZ10",12,100)
Actions.SetBurnable("BARMAZ10",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BARMAZ11","Barril",3075.878429,44555.242725,33283.509043,"Physic")
o.Scale=1.000000
o.Orientation=0.732680,0.341561,0.051800,-0.586372
Breakings.SetBreakable("BARMAZ11",12,100)
Actions.SetBurnable("BARMAZ11",BoxBurnTime,BoxDestroyTime)

############## MAZMORRAS. TINAJAS EN LA CASA DEL ORCO JEFE #######

o=Bladex.CreateEntity("TINJEF1","Tinaja",9023.727887,46480.180722,68539.389007,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("TINJEF1",12,100)


o=Bladex.CreateEntity("TINJEF2","Tinaja",10570.382133,46383.791788,68562.091001,"Physic")
o.Scale=1.126825
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("TINJEF2",12,100)


o=Bladex.CreateEntity("TINJEF3","Tinaja",9830.112794,46476.740215,67769.391717,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("TINJEF3",12,100)



o=Bladex.CreateEntity("TINJEF4","Tinaja",12230.027293,46228.409807,68514.886283,"Physic")
o.Scale=1.334504
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("TINJEF4",12,100)





o=Bladex.CreateEntity("BARRILARM1","Barril",-7170.865000,26089.993000,54869.452000,"Physic")
o.Scale=1.445076
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panBARRILARM1", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panBARRILARM1")
Breakings.SetBreakable("BARRILARM1",12,100,"panBARRILARM1")

o=Bladex.CreateEntity("BARRILARM3","Barril",-5565.323000,25927.914000,56390.190000,"Physic")
o.Scale=1.834864
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BARRILARM3",12,100)

o=Bladex.CreateEntity("BARRILARM2","Barril",-6421.400000,26308.007000,55387.516000,"Physic")
o.Scale=1.269735
o.Orientation=0.974853,-0.018459,-0.109093,0.193442
Breakings.SetBreakable("BARRILARM2",12,100)





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