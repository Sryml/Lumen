import Bladex
import Breakings
import Actions
import pocimac
import ItemTypes
import Sparks
import Reference




###########################
#          armas          #
###########################


naginatalabyr=Bladex.CreateEntity("Naginatalabyr","Naginata",19747.450129,-7972.752803,58023.800010,"Weapon")
naginatalabyr.Scale=1.000000
naginatalabyr.Orientation=0.991942,-0.126433,-0.008029,0.000602
ItemTypes.ItemDefaultFuncs(naginatalabyr)


carcajlabyr1=Bladex.CreateEntity("Carcajlabyr1","Carcaj",51548.294771,-6272.977772,-13225.137996,"Physic")
carcajlabyr1.Scale=1.000000
carcajlabyr1.Orientation=0.764372,0.486959,-0.356433,0.227073
ItemTypes.ItemDefaultFuncs (carcajlabyr1)
carcajlabyr1.Data.ArrowsLeft=10


sablazolabyr=Bladex.CreateEntity("Sablazolabyr","Sablazo",-64316.738662,-6427.345132,14246.344962,"Weapon")
sablazolabyr.Scale=1.000000
sablazolabyr.Orientation=0.283702,0.733597,0.300472,-0.539504
ItemTypes.ItemDefaultFuncs(sablazolabyr)


lightedgelabyr=Bladex.CreateEntity("Lightedgelabyr","LightEdge",51118.641370,-6317.440514,-14242.977712,"Weapon")
lightedgelabyr.Scale=1.000000
lightedgelabyr.Orientation=0.541494,-0.797265,-0.098177,-0.248021
ItemTypes.ItemDefaultFuncs(lightedgelabyr)


hacha3labyr=Bladex.CreateEntity("Hacha3labyr","Hacha3",1441.565547,-16062.603448,191.117102,"Weapon")
hacha3labyr.Scale=1.000000
hacha3labyr.Orientation=0.624162,-0.406554,0.323081,0.583742
ItemTypes.ItemDefaultFuncs(hacha3labyr)

# Recompensa con caballero muerto en derrumbamiento
hacha4labyr=Bladex.CreateEntity("Hacha4labyr","Hacha4",-14434.1548566, -8041.84635847, 8155.56969715,"Weapon")
hacha4labyr.Scale=1.000000
hacha4labyr.Orientation=0.674680769444, -0.114416331053, 0.102876745164, -0.721894145012
ItemTypes.ItemDefaultFuncs(hacha4labyr)

# Recompensa tras cajas en la azotea
deathswordlabyr=Bladex.CreateEntity("DeathSwordlabyr","DeathSword",-236.760248311, -28533.4757424, 13640.8223077,"Weapon")
deathswordlabyr.Scale=1.000000
deathswordlabyr.Orientation=0.0104758068919, -0.531357526779, 0.00330057647079, 0.84707647562
ItemTypes.ItemDefaultFuncs(deathswordlabyr)

pocima50az=Bladex.CreateEntity("Pocima50az","Pocima50",-548.822694,-28750.852881,13272.683796)
pocima50az.Solid=0
pocima50az.Scale=1.308209
pocima50az.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreatePotion("Pocima50az")


guadanyalabyr=Bladex.CreateEntity("Guadanyalabyr","Guadanya",21916.345151,-912.791694,-13440.687603,"Weapon")
guadanyalabyr.Scale=1.000000
guadanyalabyr.Orientation=0.409208,0.499064,-0.697719,0.310921
ItemTypes.ItemDefaultFuncs(guadanyalabyr)


hacha3labyr2=Bladex.CreateEntity("Hacha3labyr2","Hacha3",-49861.191823,50.435098,19904.936718,"Weapon")
hacha3labyr2.Scale=1.000000
hacha3labyr2.Orientation=0.191160,0.340017,-0.765707,-0.511409
ItemTypes.ItemDefaultFuncs(hacha3labyr2)


maza2labyr=Bladex.CreateEntity("Maza2labyr","Maza2",-7480.438048,1911.737613,-49953.442978,"Weapon")
maza2labyr.Scale=1.000000
maza2labyr.Orientation=0.584163,0.221128,-0.768252,-0.140163
ItemTypes.ItemDefaultFuncs(maza2labyr)


espadaelficalabyr=Bladex.CreateEntity("EspadaElficalabyr","Espadaelfica",-1552.228804,-26536.100985,-17346.570668,"Weapon")
espadaelficalabyr.Scale=1.000000
espadaelficalabyr.Orientation=0.950610,0.138446,0.258204,-0.102487
ItemTypes.ItemDefaultFuncs(espadaelficalabyr)


espadaromanalabyr=Bladex.CreateEntity("EspadaRomanalabyr","Espadaromana",1715.763330,-1255.107109,-19553.158486,"Weapon")
espadaromanalabyr.Scale=1.000000
espadaromanalabyr.Orientation=0.245684,0.355436,-0.523098,0.734624
ItemTypes.ItemDefaultFuncs(espadaromanalabyr)


escudo2labyr=Bladex.CreateEntity("Escudo2labyr","Escudo2",1548.856737,-1251.815411,-18686.325978,"Weapon")
escudo2labyr.Scale=1.000000
escudo2labyr.Orientation=0.972779,-0.192110,0.068717,-0.109877
ItemTypes.ItemDefaultFuncs(escudo2labyr)


tridentelabyr=Bladex.CreateEntity("Tridentelabyr","Tridente",24459.103898,10952.527316,-18281.067069,"Weapon")
tridentelabyr.Scale=1.000000
tridentelabyr.Orientation=0.013972,-0.983883,0.019945,-0.177147
ItemTypes.ItemDefaultFuncs(tridentelabyr)






#################################
#          comestibles          #
#################################

o=Bladex.CreateEntity("NoName0","Manzana",58601.718000,400.279000,-10066.361000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("NoName1","Manzana",58646.050000,400.613000,-10167.196000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("NoName2","Manzana",58465.464000,391.395000,-10103.172000,"Physic")
o.Scale=1.000000
o.Orientation=0.110756,-0.699236,0.063591,0.703391
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("NoName3","Manzana",58534.941000,399.410000,-10186.789000,"Physic")
o.Scale=1.000000
o.Orientation=0.142604,0.968182,0.175408,-0.107328
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("NoName4","Manzana",-27124.660000,490.667000,-55336.217000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("NoName5","Manzana",-27255.286000,490.840000,-55327.781000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("NoName6","Manzana",-27172.946000,490.954000,-55187.493000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood(o.Name)


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


o=Bladex.CreateEntity("Manzana1","Manzana",-65559.3028506,-5885.18317289,17193.0203049,"Physic")
o.Scale=1.000000
o.Orientation=0.769029,0.635833,0.034616,-0.055780
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("Manzana2","Manzana",-65727.030289,-5878.92268262,17413.974181,"Physic")
o.Scale=1.000000
o.Orientation=0.775240,0.629946,-0.013428,-0.044619
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("Manzana3","Manzana",-65659.2367516,-5874.97229543,17284.0725646,"Physic")
o.Scale=1.000000
o.Orientation=0.090587,0.856244,-0.144685,-0.487552
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("Manzana4","Manzana",-65528.571000,-5806.530000,17046.699000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("Queso5","Queso",-52428.916000, -5971.705000, 25195.128000,"Physic")
o.Scale=1.000000
o.Orientation=0.454519,0.454519,0.541675,0.541675
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("NoName6","Manzana",49673.215000,-7338.148000,-16721.045000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,-0.000005,0.000005
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("NoName7","Manzana",49757.752000,-7338.064000,-16641.005000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("NoName8","Manzana",49821.323000,-7338.471000,-16800.476000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("NoName9","Manzana",49959.147000,-7339.966000,-16853.724000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000002,-0.000002
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("Paletilla11","Paletilla",-59394.624000,-6235.012000,-27196.302000,"Physic")
o.Scale=1.000000
o.Orientation=0.130526,0.991445,0.000000,0.000000
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("NoName1","Manzana",-3275.694013,-17096.893056,11126.474404,"Physic")
o.Scale=1.000000
o.Orientation=0.253426,0.957745,0.134134,0.022541
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("NoName2","Manzana",-3028.271107,-17055.761908,11065.732201,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("NoName3","Manzana",-2902.615607,-17055.153020,11250.896737,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood(o.Name)


o=Bladex.CreateEntity("NoName4","Manzana",-2784.035437,-17056.579703,10949.523707,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
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




o=Bladex.CreateEntity("Barril2","Barril",-26363.801000,1372.471000,55328.014000,"Physic")
o.Scale=1.334504
o.Orientation=0.046927,0.952075,0.194485,0.231360

pan=Breakings.CreateHiddenObject("pan", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pan")
Breakings.SetBreakable("Barril2",10,20,"pan")
Actions.SetBurnable("Barril2",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("Tinaja3","Tinaja",-20919.092000,979.622000,48967.166000,"Physic")
o.Scale=1.000000
o.Orientation=0.326506,0.326506,0.627211,-0.627211
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril4","Barril",-27151.251000,-7735.108000,55059.159000,"Physic")
o.Scale=1.763268
o.Orientation=0.701057,0.701057,-0.092296,0.092296
Breakings.SetBreakable(o.Name, 10, 20)

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

o=Bladex.CreateEntity("Tinaja8","Tinaja",27290.423000,-7776.108000,61375.767000,"Physic")
o.Scale=1.000000
o.Orientation=0.696364,0.696364,-0.122788,0.122788
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

o=Bladex.CreateEntity("Barril13","Barril",27069.738000,1313.382000,54936.667000,"Physic")
o.Scale=1.361327
o.Orientation=0.489130,0.510781,0.493644,0.506133
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril14","Barril",27015.788000,1326.838000,55822.059000,"Physic")
o.Scale=1.361327
o.Orientation=0.717529,0.123350,-0.672129,-0.134830
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril15","Barril",27129.117000,626.555000,55378.490000,"Physic")
o.Scale=1.361327
o.Orientation=0.478306,0.537917,0.495360,0.486299
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril16","Barril",59513.537000,92.357000,10390.290000,"Physic")
o.Scale=1.430769
o.Orientation=0.007673,0.978665,-0.201823,-0.037717
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril17","Barril",58620.738000,69.774000,10399.884000,"Physic")
o.Scale=1.402577
o.Orientation=0.976830,0.025196,0.087828,0.193533
Breakings.SetBreakable(o.Name, 10, 20)




o=Bladex.CreateEntity("Barril18","Barril",59066.803000,-633.166000,10371.221000,"Physic")
o.Scale=1.374941
o.Orientation=0.012202,-0.996449,0.039427,0.073395

queso=Breakings.CreateHiddenObject("queso2", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
queso.Solid=1
queso.Static=0
pocimac.CreateFood("queso2")
Breakings.SetBreakable("Barril18",10,20,"queso2")
Actions.SetBurnable("Barril18",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("Barril19","Barril",55187.522000,63.809000,18897.979000,"Physic")
o.Scale=1.459527
o.Orientation=0.398059,-0.491033,-0.725637,0.271821
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril20","Barril",49827.006000,62.863000,20565.164000,"Physic")
o.Scale=1.503752
o.Orientation=0.415233,0.554877,0.373717,0.616464
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril21","Barril",49841.304000,94.119000,19698.542000,"Physic")
o.Scale=1.430769
o.Orientation=0.138924,0.675725,0.134114,0.711414
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril22","Barril",51024.263000,-70.114000,20133.787000)
o.Static=0
o.Scale=1.361327
o.Orientation=0.317614,-0.366495,-0.594929,0.640985
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










o=Bladex.CreateEntity("Barril25","Barril",65667.881000,77.059000,20723.826000,"Physic")
o.Scale=1.459527
o.Orientation=0.415616,0.552410,0.369786,0.620777
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril26","Barril",65959.364000,113.168000,19747.147000,"Physic")
o.Scale=1.347849
o.Orientation=0.003569,0.980813,0.194091,0.017924
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril27","Barril",49781.860000,-6199.929000,16573.384000,"Physic")
o.Scale=1.416603
o.Orientation=0.515177,0.487461,0.499496,0.497471
Breakings.SetBreakable(o.Name, 10, 20)

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

o=Bladex.CreateEntity("Tinaja33","Tinaja",49774.338000,-6522.658000,-16766.378000,"Physic")
o.Scale=1.000000
o.Orientation=0.353553,0.353553,-0.612372,0.612373
Breakings.SetBreakable(o.Name, 10, 20)

pan2=Breakings.CreateHiddenObject("pan2", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan2.Solid=1
pan2.Static=0
pocimac.CreateFood("pan2")
Breakings.SetBreakable("Tinaja33",10,20,"pan2")
Actions.SetBurnable("Tinaja33",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("Armero34","Armero",51000.112000,-6586.546000,-13837.005000,"Physic")
o.Scale=1.000000
o.Orientation=0.648459,0.648459,-0.281958,0.281958
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon235","Cajon2",65428.376000,-95.571000,-20784.986000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon36","Cajon",65888.347000,30.823000,-19503.729000,"Physic")
o.Scale=0.772048
o.Orientation=0.500000,0.500000,-0.500000,0.500000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajama37","Cajama",59418.518000,-33.847000,-10420.309000,"Physic")
o.Scale=1.232392
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon238","Cajon2",61809.651000,-204.981000,-17382.101000,"Physic")
o.Scale=0.803396
o.Orientation=0.511903,0.491227,0.488812,0.507655
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon239","Cajon2",56246.944000,-2.986000,-27289.793000,"Physic")
o.Scale=0.836017
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon240","Cajon2",59208.767000,92.799000,-27024.381000,"Physic")
o.Scale=0.764404
o.Orientation=0.079848,-0.078944,-0.704441,-0.700824
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajama41","Cajama",59365.453000,-768.593000,-27115.388000,"Physic")
o.Scale=0.951466
o.Orientation=0.708564,0.698922,-0.067475,0.069936
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja42","Tinaja",49872.438000,109.616000,-20635.649000,"Physic")
o.Scale=1.000000
o.Orientation=0.296283,-0.481507,-0.780545,0.266676
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja43","Tinaja",49605.595000,-270.640000,-19833.177000,"Physic")
o.Scale=1.000000
o.Orientation=0.206015,0.201187,0.676273,-0.678039
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

o=Bladex.CreateEntity("Barril47","Barril",22852.928000,1240.070000,-50211.024000,"Physic")
o.Scale=1.196147
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril48","Barril",22970.723000,208.031000,-50460.891000,"Physic")
o.Scale=1.257163
o.Orientation=0.722658,0.690640,0.003246,-0.027763
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril49","Barril",24997.232000,1370.534000,-53733.562000,"Physic")
o.Scale=1.244716
o.Orientation=0.471759,0.453244,-0.687650,-0.314883
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

o=Bladex.CreateEntity("Tinaja53","Tinaja",-10505.938000,976.747000,-55003.587000,"Physic")
o.Scale=1.000000
o.Orientation=0.640856,0.640856,-0.298836,0.298836
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja54","Tinaja",-11403.193000,981.707000,-54906.328000,"Physic")
o.Scale=1.000000
o.Orientation=0.683013,0.683013,-0.183013,0.183013
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril55","Barril",-27217.072000,1139.435000,-55198.501000,"Physic")
o.Scale=1.459527
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril56","Barril",-26870.858000,1358.740000,-56867.218000,"Physic")
o.Scale=1.282432
o.Orientation=0.389743,-0.474530,-0.747180,0.254253
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril57","Barril",-26534.716000,1323.402000,-54865.078000,"Physic")
o.Scale=1.000000
o.Orientation=0.653143,0.652843,-0.271456,0.271129
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

o=Bladex.CreateEntity("Cajama61","Cajama",-10449.013000,-8286.853000,-55056.994000,"Physic")
o.Scale=0.905287
o.Orientation=0.693712,0.698817,0.119071,-0.127439
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja62","Tinaja",-12248.754000,-7770.055000,-52388.314000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja63","Tinaja",-12284.477000,-7402.917000,-53455.705000,"Physic")
o.Scale=1.000000
o.Orientation=0.517964,-0.251263,-0.253931,0.777238
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja64","Tinaja",-50879.856000,-6523.131000,-14113.098000,"Physic")
o.Scale=1.000000
o.Orientation=0.654730,0.652001,-0.271389,0.269392
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja65","Tinaja",-51877.768000,-6150.477000,-14124.173000,"Physic")
o.Scale=1.000000
o.Orientation=0.184935,-0.521967,-0.813853,0.176046
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

o=Bladex.CreateEntity("Cajama69","Cajama",-64570.637000,-6257.627000,-23452.824000,"Physic")
o.Scale=1.184304
o.Orientation=0.653088,0.653783,-0.270770,0.269681
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon270","Cajon2",-50212.192000,-23.601000,-20648.394000,"Physic")
o.Scale=0.878663
o.Orientation=0.696364,0.696364,-0.122788,0.122788
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon271","Cajon2",-49882.104000,-213.092000,-19260.455000,"Physic")
o.Scale=0.869963
o.Orientation=0.681226,0.184490,-0.188339,-0.682951
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon72","Cajon",-49900.650000,-1147.663000,-20469.370000,"Physic")
o.Scale=0.827740
o.Orientation=0.402125,0.915516,-0.007658,0.008213
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon73","Cajon",-56536.404000,-59.692000,-26829.001000,"Physic")
o.Scale=0.932718
o.Orientation=0.699593,0.698963,-0.104173,0.105682
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon274","Cajon2",-64467.232000,-9.752000,-23521.772000,"Physic")
o.Scale=0.852821
o.Orientation=0.653282,0.653282,0.270598,-0.270598
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon275","Cajon2",-64526.105000,-852.964000,-23369.058000,"Physic")
o.Scale=0.671653
o.Orientation=0.674380,0.674380,-0.212631,0.212631
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajama76","Cajama",-62025.184000,-11.230000,-25976.736000,"Physic")
o.Scale=1.000000
o.Orientation=0.004448,-0.999240,0.001282,0.038696
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon77","Cajon",-65582.886000,71.628000,-20561.023000,"Physic")
o.Scale=0.772048
o.Orientation=0.000000,0.582843,-0.004098,0.812574
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon278","Cajon2",-65822.053000,-161.088000,-19254.971000,"Physic")
o.Scale=0.741923
o.Orientation=0.694390,-0.059694,-0.062325,0.714405
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon279","Cajon2",-65513.306000,-1060.383000,-20078.036000,"Physic")
o.Scale=0.741923
o.Orientation=0.391762,0.511437,0.646485,-0.408671
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon280","Cajon2",-59212.641000,-310.875000,-10429.007000,"Physic")
o.Scale=1.000000
o.Orientation=0.494285,0.506631,-0.504452,-0.494506
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajama81","Cajama",-57955.024000,65.780000,-10408.958000,"Physic")
o.Scale=1.000000
o.Orientation=0.560986,0.560986,-0.430459,0.430459
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril82","Barril",-50776.676000,-11.001000,23291.890000,"Physic")
o.Scale=1.208109
o.Orientation=0.696364,0.696364,-0.122788,0.122788
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril83","Barril",-51255.846000,188.772000,23813.858000,"Physic")
o.Scale=1.061520
o.Orientation=0.090548,0.875029,-0.200864,-0.431020
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril84","Barril",-59496.706000,134.487000,27162.645000,"Physic")
o.Scale=1.257163
o.Orientation=0.009150,-0.975851,-0.218246,0.000200
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril85","Barril",-58694.054000,130.485000,27148.183000,"Physic")
o.Scale=1.257163
o.Orientation=0.555537,0.017710,0.013151,0.831199
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril86","Barril",-57942.322000,-29.133000,27274.625000,"Physic")
o.Scale=1.257163
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril87","Barril",-59080.619000,-529.318000,27186.616000,"Physic")
o.Scale=1.257163
o.Orientation=0.000000,0.999779,-0.010449,0.018228
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril88","Barril",-57860.877000,139.094000,24813.075000,"Physic")
o.Scale=1.257163
o.Orientation=0.162230,0.560649,0.115560,0.803741
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril89","Barril",-65644.757000,130.968000,20912.457000,"Physic")
o.Scale=1.257163
o.Orientation=0.399785,0.579934,0.384819,0.596458
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril90","Barril",-65732.654000,139.413000,20162.586000,"Physic")
o.Scale=1.257163
o.Orientation=0.140157,-0.683879,0.136143,-0.702944
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril91","Barril",-65775.764000,103.195000,19315.331000,"Physic")
o.Scale=1.257163
o.Orientation=0.488820,0.511083,0.493405,0.506361
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril92","Barril",-64743.006000,-28.308000,19712.947000,"Physic")
o.Scale=1.257163
o.Orientation=0.229059,0.398159,0.550249,0.697300
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Barril93","Barril",-65808.989000,-540.114000,20541.263000,"Physic")
o.Scale=1.257163
o.Orientation=0.461722,0.570846,0.428300,0.526790
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja94","Tinaja",-53405.905000,-273.566000,26017.596000,"Physic")
o.Scale=1.000000
o.Orientation=0.624770,0.620128,-0.334444,0.336527
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja95","Tinaja",-61947.254000,-267.747000,25975.978000,"Physic")
o.Scale=1.000000
o.Orientation=0.596368,0.596368,-0.379928,0.379928
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja96","Tinaja",-62440.493000,88.512000,24904.465000,"Physic")
o.Scale=1.000000
o.Orientation=0.209042,0.814045,0.528550,0.119447
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja97","Tinaja",-63247.594000,-269.936000,24841.705000,"Physic")
o.Scale=1.000000
o.Orientation=0.521334,0.521334,-0.477714,0.477714
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja98","Tinaja",-65853.667000,-268.045000,16816.153000,"Physic")
o.Scale=1.000000
o.Orientation=0.000000,0.000000,0.707107,-0.707107
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja99","Tinaja",-59162.431000,97.157000,10601.314000,"Physic")
o.Scale=1.000000
o.Orientation=0.804544,0.164733,0.125220,0.556680
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Tinaja100","Tinaja",-58304.555000,-267.689000,10239.975000,"Physic")
o.Scale=1.000000
o.Orientation=0.521334,0.521334,0.477714,-0.477714
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

o=Bladex.CreateEntity("Cajon2106","Cajon2",-15404.565000,-549.588000,18419.030000,"Physic")
o.Scale=0.914340
o.Orientation=0.653282,0.653282,0.270598,-0.270598
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon107","Cajon",-14456.1550833, -1616.83790637, 17828.836217,"Physic")
o.Scale=0.827740
o.Orientation=0.671693325043, 0.679212808609, 0.194087579846, -0.223221927881
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon108","Cajon",17930.957000,-595.522000,13662.166000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon2109","Cajon2",18094.570000,-762.450000,14986.453000,"Physic")
o.Scale=0.878663
o.Orientation=0.664463,0.241845,0.241845,0.664463
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Armero2110","Armero2",1429.182000,-16398.132000,143.288000,"Physic")
o.Scale=1.220190
o.Orientation=0.000000,0.000000,0.707107,-0.707107
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Armero2111","Armero2",-1379.182000,-16394.587000,150.201000,"Physic")
o.Scale=1.220190
o.Orientation=0.000000,0.000000,0.707107,-0.707107
Breakings.SetBreakable(o.Name, 10, 20)


o=Bladex.CreateEntity("Cofre112","Cofre",-550.000000,-17498.730000,17838.212000,"Physic")
o.Scale=0.896324
o.Orientation=0.500000,0.500000,0.500000,-0.500000

labyrpocimabarril=Breakings.CreateHiddenObject("LabyrPocimabarril", "PocimaTodo",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
labyrpocimabarril.Solid=1
labyrpocimabarril.Static=0
pocimac.CreatePotion("LabyrPocimabarril")
Breakings.SetBreakable("Cofre112",10,20,"LabyrPocimabarril")
Actions.SetBurnable("Cofre112",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("Tinaja113","Tinaja",943.671000,-17768.093000,17714.972000,"Physic")
o.Scale=1.000000
o.Orientation=0.627211,0.627211,-0.326506,0.326506
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Mesita114","Mesita",-7169.180000,-26394.055000,-10979.279000,"Physic")
o.Scale=1.196147
o.Orientation=0.500000,0.500000,0.500000,-0.500000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Mesa115","Mesa",0.000000,-26705.889000,-16682.467000,"Physic")
o.Scale=1.257163
o.Orientation=0.500000,0.500000,0.500000,-0.500000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon2116","Cajon2",6696.808888,-26530.883898,-7645.374016,"Physic")
o.Scale=0.887449
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajama117","Cajama",6882.410638,-27420.922834,-7657.599521,"Physic")
o.Scale=1.000000
o.Orientation=0.688372,0.688894,-0.160509,0.160639
Breakings.SetBreakable(o.Name, 10, 20)


o=Bladex.CreateEntity("Cofre118","Cofre",-62240.662000,-6206.360000,25713.167000,"Physic")
o.Scale=0.819544
o.Orientation=0.653282,0.653282,0.270598,-0.270598
Breakings.SetBreakable(o.Name, 10, 20)


##
###### Cajas de la azotea
##

o=Bladex.CreateEntity("Cajon2119","Cajon2",-543.590276,-29098.177567,12289.530929,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon2120","Cajon2",1134.566629,-29381.602699,12515.511279,"Physic")
o.Scale=1.000000
o.Orientation=0.302095,0.646191,0.638287,0.289424
Breakings.SetBreakable(o.Name, 10, 20)

o=Bladex.CreateEntity("Cajon121","Cajon",-132.685476,-30028.899360,12231.480407,"Physic")
o.Scale=0.705914
o.Orientation=0.430459,0.430459,-0.560986,0.560986
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

o=Bladex.CreateEntity("BloquePiedras2a","Bloque",-17940.639000,-10100.683000,5737.932000)
o.Scale=6.116318
o.Orientation=0.270598,0.653282,0.653282,0.270598
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloquePiedras2b","Bloque",-20514.632000,-11016.103000,8006.089000)
o.Scale=5.374180
o.Orientation=0.653282,0.270598,-0.270598,-0.653282
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BloquePiedras2c","Bloque",-17940.639000,-14600.683000,5737.932000)
o.Scale=6.116318
o.Orientation=0.270598,0.653282,0.653282,0.270598
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

o=Bladex.CreateEntity("TablaTrono1","Tabla_xl",0.000000,-9700.000000,-5750.000000)
o.Scale=6.557520
o.Orientation=0.000000,1.000000,0.000000,0.000000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("TablaTrono2","Tabla_xl",6125.000000,-8250.000000,-8000.000000)
o.Scale=1.986894
o.Orientation=0.000000,0.707107,0.000000,0.707107
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("TablaTrono3","Tabla_xl",-6125.000000,-8250.000000,-8000.000000)
o.Scale=2.006763
o.Orientation=0.000000,0.707107,0.000000,0.707107
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("TablaRejas1","Tabla_xl",0.000000,-12500.000000,2750.000000)
o.Scale=5.164481
o.Orientation=0.000000,1.000000,0.000000,0.000000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("TablaRejas2","Tabla_xl",0.000000,-11780.000000,-1575.000000)
o.Scale=4.865175
o.Orientation=0.000000,1.000000,0.000000,0.000000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("TablaEstantes1","Tabla_xl",-5720.000000,-29380.000000,-6800.000000)
o.Scale=4.675337
o.Orientation=0.707107,-0.000000,-0.000000,0.707107
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("TablaEstantes2","Tabla_xl",-4260.000000,-29380.000000,-6800.000000)
o.Scale=4.675337
o.Orientation=0.000000,0.707107,-0.707107,0.000000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("TablaEstantes3","Tabla_xl",4260.000000,-29380.000000,-6800.000000)
o.Scale=4.675337
o.Orientation=0.707107,-0.000000,-0.000000,0.707107
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("TablaEstantes4","Tabla_xl",5720.000000,-29380.000000,-6800.000000)
o.Scale=4.675337
o.Orientation=0.000000,0.707107,0.707107,0.000000
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

o=Bladex.CreateEntity("Resto57","Tabla_rota",15211.576250,-9649.399347,3061.933149,"Physic")
o.Scale=1.402577
o.Orientation=0.540093,0.591818,0.543698,-0.249887

o=Bladex.CreateEntity("Resto58","Tabla_xl",16429.165482,-10166.943668,2737.952374,"Physic")
o.Scale=1.295256
o.Orientation=0.277071,0.705287,-0.651331,-0.039623

o=Bladex.CreateEntity("Resto59","Piedra_01",15874.211326,-9416.238187,3016.903222,"Physic")
o.Scale=1.445076
o.Orientation=0.122013,0.612305,0.164944,0.763537

o=Bladex.CreateEntity("Resto60","Tabla_rota",-14732.503228,-9527.646673,-6176.423435,"Physic")
o.Scale=1.503752
o.Orientation=0.543916,-0.058442,-0.456019,0.701987

o=Bladex.CreateEntity("Resto61","Tabla_rota2",-14555.903749,-8797.617998,-5555.169217,"Physic")
o.Scale=1.196147
o.Orientation=0.467409,-0.468451,-0.530198,-0.530069

o=Bladex.CreateEntity("Resto62","Tabla_rota",5580.853725,-29402.342405,10675.119689,"Physic")
o.Scale=1.780901
o.Orientation=0.054882,-0.531264,-0.708218,0.461707

o=Bladex.CreateEntity("Resto63","Tabla_xl",5133.237996,-28563.351551,11298.989110,"Physic")
o.Scale=1.612226
o.Orientation=0.664463,0.664463,0.241845,-0.241845

o=Bladex.CreateEntity("Resto64","Tabla_l",5072.504545,-28669.364075,11344.831674,"Physic")
o.Scale=1.445076
o.Orientation=0.640856,0.640856,0.298836,-0.298836

o=Bladex.CreateEntity("Resto65","TelaranyaTriangular",8541.861870,-28913.188383,-8167.334945)
o.Scale=1.172579
o.Orientation=0.707107,-0.000000,0.000000,-0.707107
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1

o=Bladex.CreateEntity("Resto66","TelaranyaCuadrada",11120.730369,-29512.457816,-5724.357573)
o.Scale=3.538461
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1

o=Bladex.CreateEntity("Resto67","Tabla_rota",13427.891035,-6970.535751,-10962.848477,"Physic")
o.Scale=1.694466
o.Orientation=0.543059,0.208744,0.453244,0.675339

o=Bladex.CreateEntity("Resto68","Piedra_01",13725.107784,-6199.064755,-11440.792798,"Physic")
o.Scale=1.184304
o.Orientation=0.735300,0.442444,0.418193,-0.297813

o=Bladex.CreateEntity("Resto69","TelaranyaCuadrada",13229.857238,-9658.751563,-13202.945453)
o.Scale=1.694466
o.Orientation=0.664463,0.664463,-0.241845,0.241845
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1

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






#############################
#      restos de armas      #
#############################


o=Bladex.CreateEntity("LabyrRestoArma0","Escudo5",-50664.795406,1781.457762,8035.767895,"Weapon")
o.Scale=1.000000
o.Orientation=0.331258,0.270939,-0.896299,0.116227
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrRestoArma1","Gladius",-50251.636387,1993.120627,7462.056661,"Weapon")
o.Scale=1.000000
o.Orientation=0.998792,-0.013745,-0.000055,-0.047179
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrRestoArma2","Escudo5Pieza1",-31837.077474,1971.727513,24585.761980,"Physic")
o.Scale=1.000000
o.Orientation=0.613221,0.351583,0.364209,0.606383

o=Bladex.CreateEntity("LabyrRestoArma3","Escudo5Pieza2",-31943.850060,1948.125295,25000.150183,"Physic")
o.Scale=1.000000
o.Orientation=0.790550,0.101328,0.205853,0.567792

o=Bladex.CreateEntity("LabyrRestoArma4","Hacha",-30873.291207,1966.087597,23672.252887,"Weapon")
o.Scale=1.000000
o.Orientation=0.460076,-0.535081,-0.480809,0.520424
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrRestoArma5","Hacha",-3756.476733,-7046.901924,56184.473214,"Weapon")
o.Scale=1.000000
o.Orientation=0.285233,-0.674300,-0.610729,0.301615
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrRestoArma6","Escudo2Pieza1",-4798.657287,-7044.980382,56641.483628,"Physic")
o.Scale=1.000000
o.Orientation=0.134372,-0.690437,0.702666,-0.107246

o=Bladex.CreateEntity("LabyrRestoArma7","Escudo2Pieza2",-4263.155749,-7093.389596,56729.633869,"Physic")
o.Scale=1.000000
o.Orientation=0.209940,0.768398,0.604371,-0.015014

o=Bladex.CreateEntity("LabyrRestoArma8","Escudo2",24074.473479,-7296.299379,62093.739696,"Weapon")
o.Scale=1.000000
o.Orientation=0.961578,-0.261319,-0.077144,0.033584
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrRestoArma9","ChaoswordPieza1",23660.466590,-7033.061057,62627.153213,"Physic")
o.Scale=1.000000
o.Orientation=0.699408,0.714335,0.020961,0.010670

o=Bladex.CreateEntity("LabyrRestoArma10","ChaoswordPieza2",23122.919974,-7036.904787,62490.029662,"Physic")
o.Scale=1.000000
o.Orientation=0.428666,0.428354,0.540688,-0.583451

o=Bladex.CreateEntity("LabyrRestoArma11","HachaPieza1",22545.126459,-1846.056616,66188.707604,"Physic")
o.Scale=1.000000
o.Orientation=0.015740,-0.978783,0.201800,-0.031826

o=Bladex.CreateEntity("LabyrRestoArma12","HachaPieza2",22178.640308,-1843.646844,65870.177028,"Physic")
o.Scale=1.000000
o.Orientation=0.379796,0.613386,-0.537535,-0.436540

o=Bladex.CreateEntity("LabyrRestoArma13","Escudo5Pieza1",24283.848463,1971.629166,30925.999553,"Physic")
o.Scale=1.000000
o.Orientation=0.198326,-0.674009,-0.682762,0.200538

o=Bladex.CreateEntity("LabyrRestoArma14","Escudo5Pieza2",24448.415500,1952.487935,30754.903940,"Physic")
o.Scale=1.000000
o.Orientation=0.388263,-0.488888,-0.711109,0.323365

o=Bladex.CreateEntity("LabyrRestoArma15","Gladius",23567.596999,1988.596172,30384.862629,"Weapon")
o.Scale=1.000000
o.Orientation=0.007381,-0.056871,-0.998236,-0.015355
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrRestoArma16","Hacha",55503.920636,-6041.812858,-1305.289904,"Weapon")
o.Scale=1.000000
o.Orientation=0.623902,0.259251,-0.239555,-0.697244
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrRestoArma17","Escudo2Pieza2",55516.570253,-6105.949099,-2468.591121,"Physic")
o.Scale=1.000000
o.Orientation=0.243444,0.667225,-0.662318,-0.238496

o=Bladex.CreateEntity("LabyrRestoArma19","Escudo2Pieza1",55144.977377,-6035.306943,-2865.651977,"Physic")
o.Scale=1.000000
o.Orientation=0.142489,0.694246,-0.691084,-0.141851

o=Bladex.CreateEntity("LabyrRestoArma20","Bo",51697.392141,-6721.338828,-13136.765220,"Weapon")
o.Scale=1.000000
o.Orientation=0.306899,-0.218248,-0.921998,-0.090008
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrRestoArma21","BoPieza2",32185.805900,1915.468963,-22528.795123,"Physic")
o.Scale=1.000000
o.Orientation=0.176965,0.383481,-0.701300,0.574285

o=Bladex.CreateEntity("LabyrRestoArma22","BoPieza1",32161.418859,1964.153650,-22258.933892,"Physic")
o.Scale=1.000000
o.Orientation=0.512347,-0.352692,0.489994,-0.610749

o=Bladex.CreateEntity("LabyrRestoArma23","MazaPieza1",32276.786789,1964.860212,-23682.553778,"Physic")
o.Scale=1.000000
o.Orientation=0.077745,-0.904083,-0.378936,0.181653

o=Bladex.CreateEntity("LabyrRestoArma24","MazaPieza2",32310.520462,1882.152761,-23680.685855,"Physic")
o.Scale=1.000000
o.Orientation=0.773423,-0.250392,-0.487906,0.317912

o=Bladex.CreateEntity("LabyrRestoArma25","Escudo2Pieza1",30845.487777,1958.816290,-23277.736528,"Physic")
o.Scale=1.000000
o.Orientation=0.654807,-0.229004,-0.253641,0.674130

o=Bladex.CreateEntity("LabyrRestoArma26","Escudo2Pieza2",30915.321410,1893.670216,-23868.637783,"Physic")
o.Scale=1.000000
o.Orientation=0.470216,0.527587,-0.527192,-0.471823

o=Bladex.CreateEntity("LabyrRestoArma28","Escudo1Pieza1",15362.279731,-4870.880924,-66236.887835,"Physic")
o.Scale=1.000000
o.Orientation=0.647111,0.028944,-0.197612,-0.735771

o=Bladex.CreateEntity("LabyrRestoArma29","Escudo1Pieza2",14837.003798,-4860.574771,-65906.173572,"Physic")
o.Scale=1.000000
o.Orientation=0.640731,0.300984,-0.303962,-0.637557

o=Bladex.CreateEntity("LabyrRestoArma30","Gladius",14274.128069,-4994.059941,-65722.627682,"Weapon")
o.Scale=1.000000
o.Orientation=0.936955,0.173307,-0.289710,0.090268
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrRestoArma31","Lanza",-17.451373,-7739.240090,-61070.922304,"Weapon")
o.Scale=1.000000
o.Orientation=0.222640,0.854224,0.426257,-0.197579
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrRestoArma32","Escudo5Pieza1",-1398.943003,-7028.418215,-61223.116265,"Physic")
o.Scale=1.000000
o.Orientation=0.469346,0.526877,0.537140,0.462164

o=Bladex.CreateEntity("LabyrRestoArma33","Escudo5Pieza2",-765.871228,-7046.659020,-60820.038166,"Physic")
o.Scale=1.000000
o.Orientation=0.593536,0.323454,0.527727,0.514389

o=Bladex.CreateEntity("LabyrRestoArma35","Maza",-21824.493558,-7077.284411,-52809.341769,"Weapon")
o.Scale=1.000000
o.Orientation=0.547957,0.317680,-0.751904,-0.182930
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrRestoArma36","MazaPieza2",-42184.567855,1862.926036,-10056.169555,"Physic")
o.Scale=1.000000
o.Orientation=0.129688,0.375158,0.908845,0.128212

o=Bladex.CreateEntity("LabyrRestoArma37","MazaPieza1",-42110.637745,1968.777996,-9998.864755,"Physic")
o.Scale=1.000000
o.Orientation=0.255164,0.127906,-0.955436,-0.075321

o=Bladex.CreateEntity("LabyrRestoArma38","Escudo1Pieza1",-41016.859558,1953.871620,-9369.336769,"Physic")
o.Scale=1.000000
o.Orientation=0.551387,0.565448,0.386821,0.476036

o=Bladex.CreateEntity("LabyrRestoArma39","Escudo1Pieza2",-40687.425278,1938.176707,-9826.327485,"Physic")
o.Scale=1.000000
o.Orientation=0.233472,-0.667877,0.667096,-0.233265

o=Bladex.CreateEntity("LabyrRestoArma40","Chaosword",-49468.711204,-466.493866,-21210.114884,"Weapon")
o.Scale=1.000000
o.Orientation=0.969059,0.086967,-0.225864,-0.048438
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrRestoArma41","Hacha5",-22416.611714,-73.756812,11046.662367,"Weapon")
o.Scale=1.000000
o.Orientation=0.173757,0.692086,0.659848,0.235426
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrRestoArma42","HachaPieza1",-19873.702379,-66.757499,-15980.476056,"Physic")
o.Scale=1.000000
o.Orientation=0.978798,0.010626,0.146282,-0.142980

o=Bladex.CreateEntity("LabyrRestoArma43","HachaPieza2",-20194.605731,-46.183888,-15724.325481,"Physic")
o.Scale=1.000000
o.Orientation=0.634156,0.214535,-0.135406,-0.730401

o=Bladex.CreateEntity("LabyrRestoArma44","Escudo2Pieza2",-19621.350593,-104.904046,-14660.807672,"Physic")
o.Scale=1.000000
o.Orientation=0.406116,0.580885,-0.576906,-0.405983

o=Bladex.CreateEntity("LabyrRestoArma45","Escudo2Pieza1",-19949.699482,-47.200333,-14130.262634,"Physic")
o.Scale=1.000000
o.Orientation=0.658293,0.250926,-0.293708,-0.646082

o=Bladex.CreateEntity("LabyrRestoArma46","Escudo2Pieza1",6056.705419,-77.561779,-30775.702404,"Physic")
o.Scale=1.000000
o.Orientation=0.696137,-0.048374,0.145577,-0.701327

o=Bladex.CreateEntity("LabyrRestoArma47","Escudo2Pieza2",5165.816837,-106.710565,-30947.478553,"Physic")
o.Scale=1.000000
o.Orientation=0.481351,0.522444,-0.517689,-0.476814

o=Bladex.CreateEntity("LabyrRestoArma48","Hacha5",13292.642322,-9041.644257,-15211.477390,"Weapon")
o.Scale=1.000000
o.Orientation=0.541152,0.461196,0.505113,0.489196
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrRestoArma50","Escudo1Pieza1",12153.738854,-9065.080764,-16277.573797,"Physic")
o.Scale=1.000000
o.Orientation=0.659057,0.349759,0.402220,0.530595

o=Bladex.CreateEntity("LabyrRestoArma51","Escudo1Pieza2",12437.236357,-9061.434119,-15699.363952,"Physic")
o.Scale=1.000000
o.Orientation=0.669400,-0.229689,0.229831,-0.668076

o=Bladex.CreateEntity("LabyrRestoArma52","Escudo1",8217.041280,-9056.817929,14623.428458,"Weapon")
o.Scale=1.000000
o.Orientation=0.912381,0.259022,0.163749,0.271394
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("LabyrRestoArma53","Hacha5Pieza2",8060.408103,-8539.099791,13809.870792,"Physic")
o.Scale=1.000000
o.Orientation=0.254428,-0.614742,0.701273,-0.256076

o=Bladex.CreateEntity("LabyrRestoArma54","Hacha5Pieza1",8026.099933,-8784.490870,13825.733512,"Physic")
o.Scale=1.000000
o.Orientation=0.507468,-0.095889,0.854652,-0.053398
