import Bladex
import Breakings
import Actions
import pocimac
import ItemTypes
import Sparks
import Reference




#################################
#          comestibles          #
#################################


o=Bladex.CreateEntity("NoName7","Hogaza",-10575.196000,1014.859000,-56116.277000,"Physic")
o.Scale=1.000000
o.Orientation=0.653282,0.653282,0.270598,-0.270598
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("NoName8","Queso",-10620.957000,1021.476000,-55763.666000,"Physic")
o.Scale=1.000000
o.Orientation=0.664463,0.664463,-0.241845,0.241845
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("NoName0","Paletilla",-65847.015000,256.979000,-16371.787000,"Physic")
o.Scale=1.000000
o.Orientation=0.988857,-0.140943,0.005091,-0.047653
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("Queso5","Queso",-52428.916000, -5971.705000, 25195.128000,"Physic")
o.Scale=1.000000
o.Orientation=0.454519,0.454519,0.541675,0.541675
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("Paletilla11","Paletilla",-59394.624000,-6235.012000,-27196.302000,"Physic")
o.Scale=1.000000
o.Orientation=0.130526,0.991445,0.000000,0.000000
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("NoName5","Hogaza",4491.245490,-17724.234459,14285.041229,"Physic")
o.Scale=1.000000
o.Orientation=0.673898,0.701287,-0.085375,0.216264
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("NoName6","Queso",4783.562521,-17705.449289,14159.520976,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,-0.000000,0.000000
pocimac.CreateFood(o.Name)




#############################
#     Objetos rompibles     #
#############################

BoxBurnTime = 6
BoxDestroyTime = 12

o=Bladex.CreateEntity("Barril1","Barril",-27154.907000,1151.346000,55067.713000,"Physic")
o.Scale=1.430769
o.Orientation=0.707107,0.707107,0.000000,0.000000

queso=Breakings.CreateHiddenObject("queso", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
queso.Solid=1
queso.Static=0
pocimac.CreateFood("queso")
Breakings.SetBreakable("Barril1",10,20,"queso")
Actions.SetBurnable("Barril1",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("Armero5","Armero",-17430.095000,-7832.826000,58284.176000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Armero6","Armero",-19978.118000,-7839.799000,58345.653000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cofre7","Cofre",-11953.033000,-7485.093000,52392.178000,"Physic")
o.Scale=0.869963
o.Orientation=0.270598,0.270598,-0.653282,0.653282
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja9","Tinaja",26537.463000,-7404.899000,61801.618000,"Physic")
o.Scale=1.000000
o.Orientation=0.850904,0.060749,-0.029993,0.520934
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Armero10","Armero",19348.459000,-7833.078000,58311.012000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril11","Barril",11733.745000,-7616.096000,52716.263000,"Physic")
o.Scale=1.474123
o.Orientation=0.707107,0.707107,0.000000,0.000000

jamon=Breakings.CreateHiddenObject("jamon3", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
jamon.Solid=1
jamon.Static=0
pocimac.CreateFood("jamon3")
Breakings.SetBreakable("Barril11",10,20,"jamon3")
Actions.SetBurnable("Barril11",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("Cofre12","Cofre",17253.664000,-7476.331000,58339.757000,"Physic")
o.Scale=0.852821
o.Orientation=0.500000,0.500000,0.500000,-0.500000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril23","Barril",59545.096000,-56.460000,27294.671000,"Physic")
o.Scale=1.308209
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril24","Barril",58698.767000,104.997000,27161.915000,"Physic")
o.Scale=1.282432
o.Orientation=0.003182,0.998728,-0.048763,-0.012464

jamon=Breakings.CreateHiddenObject("jamon", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
jamon.Solid=1
jamon.Static=0
pocimac.CreateFood("jamon")
Breakings.SetBreakable("Barril24",10,20,"jamon")
Actions.SetBurnable("Barril24",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("Barril28","Barril",49606.706000,-6250.753000,17406.356000,"Physic")
o.Scale=1.172579
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Armero29","Armero",49511.906000,-6583.400000,20516.173000,"Physic")
o.Scale=1.000000
o.Orientation=0.500000,0.500000,-0.500000,0.500000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja30","Tinaja",64713.401000,-6519.105000,14131.236000,"Physic")
o.Scale=1.000000
o.Orientation=0.706316,0.707840,0.004485,-0.007796
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril31","Barril",62023.823000,-51.807000,-26075.260000,"Physic")
o.Scale=1.321291
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cofre32","Cofre",65972.743000,-6190.706000,-16868.650000,"Physic")
o.Scale=0.787566
o.Orientation=0.000000,0.000000,0.707107,-0.707107
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Armero34","Armero",51000.112000,-6586.546000,-13837.005000,"Physic")
o.Scale=1.000000
o.Orientation=0.648459,0.648459,-0.281958,0.281958
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon36","Cajon",65888.347000,30.823000,-19503.729000,"Physic")
o.Scale=0.772048
o.Orientation=0.500000,0.500000,-0.500000,0.500000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajama37","Cajama",59418.518000,-33.847000,-10420.309000,"Physic")
o.Scale=1.232392
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon240","Cajon2",59208.767000,92.799000,-27024.381000,"Physic")
o.Scale=0.764404
o.Orientation=0.079848,-0.078944,-0.704441,-0.700824
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja44","Tinaja",20852.043000,979.640000,-58305.547000,"Physic")
o.Scale=1.000000
o.Orientation=0.454519,0.454519,0.541675,-0.541675

jamon=Breakings.CreateHiddenObject("jamon2", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
jamon.Solid=1
jamon.Static=0
pocimac.CreateFood("jamon2")
Breakings.SetBreakable("Tinaja44",10,20,"jamon2")
Actions.SetBurnable("Tinaja44",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("Barril45","Barril",23919.151000,1239.927000,-51268.841000,"Physic")
o.Scale=1.196147
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril46","Barril",23324.042000,1229.999000,-50803.978000,"Physic")
o.Scale=1.220190
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Armero50","Armero",19633.300000,-7835.500000,-58341.817000,"Physic")
o.Scale=1.000000
o.Orientation=0.000000,0.000000,0.707107,-0.707107
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Armero51","Armero",17954.591000,-7835.359000,-58352.860000,"Physic")
o.Scale=1.000000
o.Orientation=0.000000,0.000000,0.707107,-0.707107
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cofre52","Cofre",27306.933000,-7499.424000,-55791.487000,"Physic")
o.Scale=0.896324
o.Orientation=0.000000,0.000000,0.707107,-0.707107
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril56","Barril",-26870.858000,1358.740000,-56867.218000,"Physic")
o.Scale=1.282432
o.Orientation=0.389743,-0.474530,-0.747180,0.254253
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Armero58","Armero",-20022.970000,-7835.388000,-58333.504000,"Physic")
o.Scale=1.000000
o.Orientation=0.000000,0.000000,0.707107,-0.707107
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Armero59","Armero",-17360.382000,-7835.387000,-58333.187000,"Physic")
o.Scale=1.000000
o.Orientation=0.000000,0.000000,0.707107,-0.707107
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon260","Cajon2",-10670.638000,-7477.500000,-54983.326000,"Physic")
o.Scale=0.787566
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja62","Tinaja",-12248.754000,-7770.055000,-52388.314000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja66","Tinaja",-51894.399000,-6479.648000,-13134.065000,"Physic")
o.Scale=1.000000
o.Orientation=0.644088,0.683423,0.276991,0.203369
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Armero67","Armero",-65967.887000,-6580.660000,-20651.453000,"Physic")
o.Scale=1.000000
o.Orientation=0.500000,0.500000,-0.500000,0.500000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Armero68","Armero",-65900.751000,-6609.791000,-16868.505000,"Physic")
o.Scale=1.000000
o.Orientation=0.481356,0.511905,-0.489393,0.516473
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon270","Cajon2",-50212.192000,-23.601000,-20648.394000,"Physic")
o.Scale=0.878663
o.Orientation=0.696364,0.696364,-0.122788,0.122788
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon73","Cajon",-56536.404000,-59.692000,-26829.001000,"Physic")
o.Scale=0.932718
o.Orientation=0.699593,0.698963,-0.104173,0.105682
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon274","Cajon2",-64467.232000,-9.752000,-23521.772000,"Physic")
o.Scale=0.852821
o.Orientation=0.653282,0.653282,0.270598,-0.270598
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon77","Cajon",-65582.886000,71.628000,-20561.023000,"Physic")
o.Scale=0.772048
o.Orientation=0.000000,0.582843,-0.004098,0.812574
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajama81","Cajama",-57955.024000,65.780000,-10408.958000,"Physic")
o.Scale=1.000000
o.Orientation=0.560986,0.560986,-0.430459,0.430459
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril86","Barril",-57942.322000,-29.133000,27274.625000,"Physic")
o.Scale=1.257163
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja94","Tinaja",-53405.905000,-273.566000,26017.596000,"Physic")
o.Scale=1.000000
o.Orientation=0.624770,0.620128,-0.334444,0.336527
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja95","Tinaja",-61947.254000,-267.747000,25975.978000,"Physic")
o.Scale=1.000000
o.Orientation=0.596368,0.596368,-0.379928,0.379928
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja98","Tinaja",-65853.667000,-268.045000,16816.153000,"Physic")
o.Scale=1.000000
o.Orientation=0.000000,0.000000,0.707107,-0.707107
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril101","Barril",-64600.035000,-6246.162000,23520.074000,"Physic")
o.Scale=1.172579
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Armero102","Armero",-64535.406000,-6587.466000,13878.229000,"Physic")
o.Scale=1.000000
o.Orientation=0.270598,0.270598,-0.653282,0.653282
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Armero103","Armero",-50922.065000,-6583.315000,13886.353000,"Physic")
o.Scale=1.000000
o.Orientation=0.270598,0.270598,0.653282,-0.653282
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja104","Tinaja",-65873.115000,-6522.944000,16651.802000,"Physic")
o.Scale=1.000000
o.Orientation=0.000000,0.000000,0.707107,-0.707107
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon2105","Cajon2",-13730.960000,-598.066000,17517.889000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon108","Cajon",17930.957000,-595.522000,13662.166000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cofre118","Cofre",-62240.662000,-6206.360000,25713.167000,"Physic")
o.Scale=0.819544
o.Orientation=0.653282,0.653282,0.270598,-0.270598
Breakings.SetBreakable(o.Name, 10, 20)




###############################
#     Objetos chispeantes     #
###############################

o=Bladex.CreateEntity("Yunque1","Yunque",-49592.946000,181.893000,20174.426000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.682644,0.683246,0.187057,-0.179390
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Yunque2","Yunque",-11762.627000,1405.372000,-53709.437000)
o.Static=1
o.Scale=1.115668
o.Orientation=0.696364,0.696364,0.122788,-0.122788
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Reja1","Reja",0.000000,1150.000000,-39168.049000)
o.Static=1
o.Scale=1.503752
o.Orientation=1.000000,0.000000,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Argolla1","Argolla",-20999.761000,-500.000000,53195.499000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Argolla2","Argolla",-16505.810000,-500.000000,53198.963000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Argolla3","Argolla",16518.216000,-250.000000,53193.742000)
o.Static=1
o.Scale=1.104622
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Argolla4","Argolla",20998.171000,-250.000000,53187.909000)
o.Static=1
o.Scale=1.104622
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Argolla5","Argolla",60747.152000,-1750.000000,14808.928000)
o.Static=1
o.Scale=1.220190
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Argolla6","Argolla",64829.572000,-1750.000000,15364.123000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.500000,0.500000,0.500000,-0.500000
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Argolla7","Argolla",64807.748000,-1750.000000,22118.733000)
o.Static=1
o.Scale=1.220190
o.Orientation=0.500000,0.500000,-0.500000,0.500000
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Argolla8","Argolla",50683.857000,-1750.000000,22133.948000)
o.Static=1
o.Scale=1.208109
o.Orientation=0.500000,0.500000,0.500000,-0.500000
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Argolla9","Argolla",64814.746000,-1750.000000,-15336.828000)
o.Static=1
o.Scale=1.208109
o.Orientation=0.500000,0.500000,0.500000,-0.500000
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Argolla10","Argolla",55417.202000,-1750.000000,-17125.947000)
o.Static=1
o.Scale=1.208109
o.Orientation=0.653282,0.653282,0.270598,-0.270598
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Argolla11","Argolla",60761.774000,-1750.000000,-11300.081000)
o.Static=1
o.Scale=1.208109
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Argolla12","Argolla",20999.181000,-500.000000,-53188.539000)
o.Static=1
o.Scale=1.257163
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Argolla13","Argolla",16504.863000,-500.000000,-53190.098000)
o.Static=1
o.Scale=1.257163
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Argolla14","Argolla",-16506.724000,-250.000000,-53185.988000)
o.Static=1
o.Scale=1.208109
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Argolla15","Argolla",-21000.626000,-250.000000,-53185.963000)
o.Static=1
o.Scale=1.220190
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Argolla16","Argolla",-54554.739000,-2156.114000,-21239.102000)
o.Static=1
o.Scale=1.138093
o.Orientation=0.653282,0.653282,0.270598,-0.270598
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Argolla17","Argolla",-60757.359000,-2000.000000,11312.828000)
o.Static=1
o.Scale=1.208109
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Argolla18","Argolla",-64814.798000,-2000.000000,15371.104000)
o.Static=1
o.Scale=1.208109
o.Orientation=0.500000,0.500000,-0.500000,0.500000
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Argolla19","Argolla",2581.573000,-19500.000000,16716.670000)
o.Static=1
o.Scale=1.208109
o.Orientation=0.653282,0.653282,0.270598,-0.270598
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Argolla20","Argolla",-2591.573000,-19500.000000,16707.069000)
o.Static=1
o.Scale=1.208109
o.Orientation=0.653282,0.653282,-0.270598,0.270598
Sparks.SetMetalSparkling(o.Name)


### Los rastrillos estan en el puertas.py




##############################
#     Objetos invisibles     #
##############################


o=Bladex.CreateEntity("BloquePiedras1a","Bloque",-43165.65, 96.401, 25724.363)
o.Scale=6.2
o.Orientation=0.270598,0.653282,0.653282,0.270598
o.CastShadows=0
o.Alpha = 0
o.ExclusionMask=2
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloquePiedras1b","Bloque",-43165.65, -4520.0, 25724.363)
o.Scale=6.2
o.Orientation=0.270598,0.653282,0.653282,0.270598
o.CastShadows=0
o.Alpha = 0
o.ExclusionMask=2
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloquePiedras1c","Bloque",-45828.583877,-4102.057195,28588.911849)
o.Scale=9.197427
o.Orientation=0.653282,0.653282,-0.270598,0.270598
o.CastShadows=0
o.Alpha = 0
o.ExclusionMask=2
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloquePiedras3","Bloque",155.236000,3176.932000,-22699.996000)
o.Scale=7.537701
o.Orientation=0.500000,0.500000,0.500000,0.500000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloqueRejaa","Bloque",0.000000,1700.000000,-39500.000000)
o.Scale=2.376619
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloqueRejab","Bloque",0.000000,1700.000000,-38350.000000)
o.Scale=2.376619
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

### Bloqueadores en canales

o=Bladex.CreateEntity("BloqueCan0","Bloque",-13429.718000,1820.000000,-38751.743000)
o.Scale=2.522829
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloqueCan1","Bloque",-16289.610000,1820.000000,-37971.130000)
o.Scale=2.928926
o.Orientation=0.653282,0.270598,-0.270598,-0.653282
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloqueCan2","Bloque",-38075.209000,1670.000000,-16190.490000)
o.Scale=2.958215
o.Orientation=0.653282,0.270598,-0.270598,-0.653282
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloqueCan3","Bloque",-38698.774000,1820.000000,-14111.211000)
o.Scale=2.522829
o.Orientation=0.500000,0.500000,0.500000,0.500000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloqueCan4","Bloque",-38808.021000,1970.000000,-1764.792000)
o.Scale=2.522829
o.Orientation=0.500000,0.500000,0.500000,0.500000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloqueCan5","Bloque",-38823.717000,1970.000000,1761.073000)
o.Scale=2.522829
o.Orientation=0.500000,0.500000,0.500000,0.500000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloqueCan6","Bloque",-38703.469000,1820.000000,14106.718000)
o.Scale=2.522829
o.Orientation=0.500000,0.500000,0.500000,0.500000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloqueCan7","Bloque",-37966.681000,1820.000000,16233.760000)
o.Scale=3.078330
o.Orientation=0.653282,0.270598,0.270598,0.653282
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloqueCan8","Bloque",-16173.646272,1773.970530,38076.451876)
o.Scale=2.987797
o.Orientation=0.653282,0.270598,0.270598,0.653282
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloqueCan9","Bloque",-14066.187463,1835.751352,38747.987579)
o.Scale=2.522829
o.Orientation=0.500000,0.500000,0.500000,0.500000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloqueCan10","Bloque",14070.073833,1822.780939,38733.129840)
o.Scale=2.522829
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloqueCan11","Bloque",16214.321243,1702.483959,37967.791423)
o.Scale=3.140205
o.Orientation=0.270598,0.653282,0.653282,0.270598
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloqueCan12","Bloque",38075.117891,1707.826866,16157.963991)
o.Scale=3.047852
o.Orientation=0.270598,0.653282,0.653282,0.270598
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloqueCan13","Bloque",38793.974132,1823.828964,14106.731793)
o.Scale=2.522829
o.Orientation=0.500000,0.500000,0.500000,0.500000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloqueCan14","Bloque",38940.120816,1982.347664,1740.040496)
o.Scale=2.599273
o.Orientation=0.500000,0.500000,0.500000,0.500000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloqueCan15","Bloque",38810.076237,1985.516318,-1766.859979)
o.Scale=2.522829
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloqueCan16","Bloque",38685.356196,1827.529347,-14108.788973)
o.Scale=2.522829
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloqueCan17","Bloque",38078.578091,1802.394113,-16169.442540)
o.Scale=3.017675
o.Orientation=0.653282,0.270598,0.270598,0.653282
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloqueCan18","Bloque",16153.964589,1630.888212,-38089.186641)
o.Scale=3.078330
o.Orientation=0.270598,0.653282,-0.653282,-0.270598
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloqueCan19","Bloque",13435.917977,1824.987580,-38753.954983)
o.Scale=2.548057
o.Orientation=0.500000,0.500000,0.500000,0.500000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")





############################
#          restos          #
############################


o=Bladex.CreateEntity("Resto0","Skull",24503.5331984, 10899.2736671, -17754.9490121,"Weapon")
o.Scale=1.220190
o.Orientation=0.80048084259, 0.567273318768, 0.18814599514, -0.0450829863548

o=Bladex.CreateEntity("Resto1","Femur",23738.721893,11061.170099,-17403.491777,"Weapon")
o.Scale=1.232392
o.Orientation=0.334678,0.871605,0.182422,-0.308250

o=Bladex.CreateEntity("Resto2","Femur",23630.709097,10935.973259,-18514.728065,"Weapon")
o.Scale=1.160969
o.Orientation=0.937252,-0.002771,-0.347479,-0.028461

o=Bladex.CreateEntity("Resto3","Femur",23668.668243,10942.523299,-18240.563075,"Weapon")
o.Scale=1.160969
o.Orientation=0.083478,0.882071,0.045257,-0.461448

o=Bladex.CreateEntity("Resto4","Costilla",23645.536226,10948.481077,-17888.657177,"Weapon")
o.Scale=1.282432
o.Orientation=0.380742,0.550672,0.661955,0.337063

o=Bladex.CreateEntity("Resto5","Costilla",23662.483735,10972.295496,-18004.020945,"Weapon")
o.Scale=1.257163
o.Orientation=0.470781,0.601125,-0.365722,-0.532223

o=Bladex.CreateEntity("Resto6","Costilla",23568.097451,10963.090162,-17757.886872,"Weapon")
o.Scale=1.208109
o.Orientation=0.389108,0.613475,-0.630508,-0.273318

o=Bladex.CreateEntity("Resto7","TelaranyaTriangular",23731.443188,6524.823973,-17901.489204)
o.Scale=2.047099
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1

o=Bladex.CreateEntity("Resto8","TelaranyaTriangular",21896.870357,6380.128351,-1974.756876)
o.Scale=1.763268
o.Orientation=0.000000,0.000000,0.707107,0.707107
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1

o=Bladex.CreateEntity("Resto9","Piedra_10",21006.778351,10858.861546,-19232.829952,"Physic")
o.Scale=1.000000
o.Orientation=0.684609,0.728474,-0.025102,0.002345

o=Bladex.CreateEntity("Resto10","Piedra_10",20578.759519,10839.827724,-19388.169603,"Physic")
o.Scale=1.196147
o.Orientation=0.545801,0.554731,-0.443058,0.445055

o=Bladex.CreateEntity("Resto11","Tabla_rota",20454.248322,10215.001970,-18705.636678,"Physic")
o.Scale=1.416603
o.Orientation=0.610807,0.604943,0.363482,0.358941

o=Bladex.CreateEntity("Resto12","Tabla_rota2",24429.225383,10946.341057,3176.173592,"Physic")
o.Scale=1.361327
o.Orientation=0.032072,-0.034723,-0.705515,-0.707117

o=Bladex.CreateEntity("Resto13","Piedra_01",23776.157051,10916.480962,3461.741291,"Physic")
o.Scale=1.000000
o.Orientation=0.968905,-0.157322,-0.009722,0.190731

o=Bladex.CreateEntity("Resto14","Piedra_09",24394.591659,10741.092363,3688.233513,"Physic")
o.Scale=1.282432
o.Orientation=0.681814,0.731321,-0.007905,-0.015408

o=Bladex.CreateEntity("Resto15","Tabla_rota",21057.209818,10145.971177,3715.379518,"Physic")
o.Scale=1.430769
o.Orientation=0.091200,0.698039,0.703227,-0.099482

o=Bladex.CreateEntity("Resto16","Tabla_rota",24529.407626,10638.739133,-22118.412917,"Physic")
o.Scale=1.580459
o.Orientation=0.659539,0.563817,-0.235139,0.437981

o=Bladex.CreateEntity("Resto17","Piedra_01",24034.814973,10829.969917,-21174.713009,"Physic")
o.Scale=1.000000
o.Orientation=0.852133,0.520780,0.018128,-0.048258

o=Bladex.CreateEntity("Resto18","Piedra_01",24461.867863,10734.540639,-21245.987935,"Physic")
o.Scale=1.518790
o.Orientation=0.656008,0.633452,-0.305068,0.274455

o=Bladex.CreateEntity("Resto19","Vigaro2",25346.679410,9099.964780,-28772.620605,"Physic")
o.Scale=0.671653
o.Orientation=0.896838,0.103601,0.316036,0.291667

o=Bladex.CreateEntity("Resto20","Piedra_09",25642.935414,10228.153856,-27831.460962,"Physic")
o.Scale=1.361327
o.Orientation=0.684060,0.728965,-0.024892,-0.007244

o=Bladex.CreateEntity("Resto21","Piedra_09",10696.895245,9761.174588,-28409.703208,"Physic")
o.Scale=1.000000
o.Orientation=0.204423,-0.924524,-0.208242,-0.245158

o=Bladex.CreateEntity("Resto22","Piedra_09",9228.976554,9103.437282,-26038.779613,"Physic")
o.Scale=1.232392
o.Orientation=0.463101,0.512898,-0.505064,0.517090

o=Bladex.CreateEntity("Resto23","Piedra_01",9466.225175,9190.700593,-26431.249440,"Physic")
o.Scale=0.869963
o.Orientation=0.743045,0.566227,-0.309408,0.177589

o=Bladex.CreateEntity("Resto24","Tabla_rota",11740.414176,9501.030954,-28974.017054,"Physic")
o.Scale=1.244716
o.Orientation=0.717663,0.330652,0.152057,0.593723

o=Bladex.CreateEntity("Resto25","Piedra_01",13536.951597,7456.414713,-23268.889793,"Physic")
o.Scale=1.000000
o.Orientation=0.987823,-0.068613,0.020817,0.138074

o=Bladex.CreateEntity("Resto26","Tabla_rota2",13079.341614,3787.883368,-29356.044586,"Physic")
o.Scale=1.580459
o.Orientation=0.707213,0.111364,0.042916,0.696854

o=Bladex.CreateEntity("Resto27","Piedra_09",13245.568401,4072.007233,-29006.303911,"Physic")
o.Scale=0.827740
o.Orientation=0.704515,0.708005,-0.048436,0.006463

o=Bladex.CreateEntity("Resto28","Tabla_rota",1711.822337,4895.095793,-33235.166071,"Physic")
o.Scale=1.947745
o.Orientation=0.386508,0.385103,0.591573,0.593590

o=Bladex.CreateEntity("Resto29","Piedra_09",1007.524362,1753.261732,-41853.899987,"Physic")
o.Scale=1.220190
o.Orientation=0.683003,0.727610,-0.054880,0.032850

o=Bladex.CreateEntity("Resto30","Tabla_xl",404.310366,2172.514909,-45497.905317,"Physic")
o.Scale=1.890462
o.Orientation=0.696348,0.692013,-0.132778,-0.136336

o=Bladex.CreateEntity("Resto31","Tabla_xl",34.902617,1938.443658,-44880.871920,"Physic")
o.Scale=1.728525
o.Orientation=0.707107,0.707107,0.000000,0.000000

o=Bladex.CreateEntity("Resto32","Vigaro1",2977.448948,4485.766858,-54996.805135,"Physic")
o.Scale=0.671653
o.Orientation=0.201058,0.837516,0.109530,-0.496130

o=Bladex.CreateEntity("Resto33","Piedra_09",12657.478280,1588.198898,-48501.131913,"Physic")
o.Scale=2.109128
o.Orientation=0.681841,0.731087,-0.024315,-0.003675

o=Bladex.CreateEntity("Resto34","Piedra_01",11464.046732,1911.304235,-48308.317541,"Physic")
o.Scale=1.172579
o.Orientation=0.951094,-0.193310,0.052614,0.235124

o=Bladex.CreateEntity("Resto35","Piedra_09",-33897.605129,1404.854761,-43080.511740,"Physic")
o.Scale=3.078330
o.Orientation=0.682448,0.728837,0.019840,-0.051657

o=Bladex.CreateEntity("Resto36","Piedra_09",-35022.957701,1485.367736,-42200.801202,"Physic")
o.Scale=2.109128
o.Orientation=0.558543,0.430499,-0.429355,0.564230

o=Bladex.CreateEntity("Resto37","Piedra_10",-34845.606532,663.987426,-42610.199931,"Physic")
o.Scale=3.333391
o.Orientation=0.658989,0.728929,0.039707,-0.181163

o=Bladex.CreateEntity("Resto38","Vigaro2",-34356.460839,595.393717,-41686.684764,"Physic")
o.Scale=0.698925
o.Orientation=0.890971,0.392794,0.217010,0.069214

o=Bladex.CreateEntity("Resto39","Tabla_rota",-32910.464540,1917.875129,-44245.105852,"Physic")
o.Scale=2.329790
o.Orientation=0.707091,0.706909,-0.012176,0.012388

o=Bladex.CreateEntity("Resto40","Piedra_09",-31168.753824,1656.991243,-22667.295047,"Physic")
o.Scale=1.745810
o.Orientation=0.683063,0.730009,-0.013183,-0.018389

o=Bladex.CreateEntity("Resto41","Piedra_01",-30551.125973,1828.959277,-23110.523038,"Physic")
o.Scale=1.000000
o.Orientation=0.854984,0.500542,-0.128434,0.044316

o=Bladex.CreateEntity("Resto42","TelaranyaTriangular",628.823755,3491.261450,-40663.974018)
o.Scale=1.000000
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1

o=Bladex.CreateEntity("Resto43","TelaranyaTriangular",-634.741516,3494.057776,-43132.098501)
o.Scale=1.000000
o.Orientation=0.000000,0.000000,0.707107,0.707107
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1

o=Bladex.CreateEntity("Resto44","Tabla_xl",26939.306034,1947.285512,-50369.785227,"Physic")
o.Scale=1.295256
o.Orientation=0.707107,0.707107,0.000000,0.000000

o=Bladex.CreateEntity("Resto45","Tabla_l",27003.889028,1854.883521,-50332.227555,"Physic")
o.Scale=1.374941
o.Orientation=0.708216,0.699997,-0.064439,0.065432

o=Bladex.CreateEntity("Resto46","Tabla_l",26959.202743,1734.191284,-50451.338105,"Physic")
o.Scale=1.388690
o.Orientation=0.035933,0.034733,0.738440,-0.672465

o=Bladex.CreateEntity("Resto47","Tabla_xl",26882.846440,1640.750493,-50410.741966,"Physic")
o.Scale=1.000000
o.Orientation=0.677032,0.735933,0.004508,0.003165

o=Bladex.CreateEntity("Resto48","Tabla_xl",26923.660712,1630.442340,-49712.435378,"Physic")
o.Scale=2.088246
o.Orientation=0.459628,-0.551007,-0.540400,-0.439433

o=Bladex.CreateEntity("Resto49","Piedra_09",26142.957596,1704.917010,-49678.580554,"Physic")
o.Scale=1.488864
o.Orientation=0.683846,0.728597,0.011623,-0.036973

o=Bladex.CreateEntity("Resto50","Piedra_09",25400.319330,1827.029268,-49589.663938,"Physic")
o.Scale=0.844377
o.Orientation=0.062340,-0.809607,-0.051370,-0.581387

o=Bladex.CreateEntity("Resto51","Tabla_rota",32186.582761,1239.618665,-21022.614630,"Physic")
o.Scale=1.533978
o.Orientation=0.476811,0.705341,0.522369,0.047706

o=Bladex.CreateEntity("Resto52","Tabla_rota2",32976.323655,1940.053639,-20835.102499,"Physic")
o.Scale=1.549318
o.Orientation=0.634544,0.639072,-0.306076,0.308639

o=Bladex.CreateEntity("Resto53","Piedra_10",32559.099748,1804.938143,-20731.493857,"Physic")
o.Scale=1.149474
o.Orientation=0.090808,0.928658,0.093645,0.347244

o=Bladex.CreateEntity("Resto54","Vigaro2",34421.927982,1601.480441,39395.473158,"Physic")
o.Scale=0.705914
o.Orientation=0.700605,0.700808,-0.092622,0.097171

o=Bladex.CreateEntity("Resto55","Tabla_rota",33409.863282,1578.267412,40178.282673,"Physic")
o.Scale=1.374941
o.Orientation=0.093679,-0.227868,-0.709904,0.659800

o=Bladex.CreateEntity("Resto56","Vigaro1",33180.912059,1221.645274,39355.809070,"Physic")
o.Scale=0.720103
o.Orientation=0.500708,0.627915,0.365949,-0.470209

o=Bladex.CreateEntity("Resto70","TelaranyaTriangular",-563.667027,1689.636627,-18989.215742)
o.Scale=1.890462
o.Orientation=0.000000,0.000000,0.707107,0.707107
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1

o=Bladex.CreateEntity("Resto71","TelaranyaCuadrada",4366.685605,1497.327613,-15427.697358)
o.Scale=3.538461
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1
