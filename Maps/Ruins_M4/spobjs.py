import Bladex
import Sparks
import Breakings
import pocimac
import AuxFuncs
import ItemTypes
import Reference




#######################
#     Recompensas     #
#######################



o=Bladex.CreateEntity("NoName27","Pocima50",-39613.680917,-10690.274343,1900.230374,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreatePotion(o.Name)


pocima1001ruins=Bladex.CreateEntity("Pocima1001ruins","Pocima100",-46455.6790094, -1572.5458061, -43772.6385215,"Physic")
pocima1001ruins.Solid=0
pocima1001ruins.Scale=1.000000
pocima1001ruins.Orientation=0.585789263248, 0.129904508591, 0.77204811573, 0.209565058351
pocimac.CreatePotion(pocima1001ruins.Name)


o=Bladex.CreateEntity("NoName11","Pocima50",48656.9948734, 8919.92822193, -45314.7688104,"Physic")
o.Scale=1.000000
o.Orientation=0.450027525425, 0.50736105442, 0.608420550823, 0.412170380354
pocimac.CreatePotion(o.Name)


o=Bladex.CreateEntity("RuinsPocimaTodo","PocimaTodo",-57439.0869756, 5912.92466034, 4008.16368242,"Physic")
o.Scale=1.000000
o.Orientation=0.0437661856413, -0.510732352734, 0.852582097054, 0.101689338684
pocimac.CreatePotion(o.Name)

o=Bladex.CreateEntity("RuinsPowerPotion","PowerPotion",-43172.935000,-90.525000,-52217.920000,"Physic")
o.Scale=1.000000
o.Orientation=0.426321,-0.051214,-0.902332,-0.037735
pocimac.CreatePowerPotion(o.Name)

## pocima 100 escondida en barril junto a llave que da acceso a la puerta final

pocima1002ruins=Breakings.CreateHiddenObject("Pocima1002ruins","Pocima100",1.0,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pocima1002ruins.Solid=1
pocimac.CreatePotion(pocima1002ruins.Name)



###########
########### ARMAS EN EL NIVEL

arco1ruins=Bladex.CreateEntity("Arco1ruins","Arco",40173.416000,-3034.627000,56077.478000,"Weapon")
arco1ruins.Scale=1.000000
arco1ruins.Orientation=0.618221,0.281406,-0.250681,-0.689763
ItemTypes.ItemDefaultFuncs(arco1ruins)


carcaj1ruins=Bladex.CreateEntity("RuinsQuiverInvPrb1","Carcaj",43214.975606,536.809550,59346.945387,"Physic")
carcaj1ruins.Scale=1.000000
carcaj1ruins.Orientation=0.443797,0.889305,-0.092394,0.060363
ItemTypes.ItemDefaultFuncs(carcaj1ruins)
carcaj1ruins.Data.ArrowsLeft=10



arco2ruins=Bladex.CreateEntity("arco2ruins","Arco",-53407.412685,-32.165034,-42209.895929,"Weapon")
arco2ruins.Scale=1.000000
arco2ruins.Orientation=0.525146,0.462848,0.414983,0.581190
ItemTypes.ItemDefaultFuncs(arco2ruins)



carcaj2ruins=Bladex.CreateEntity("RuinsQuiverInvPrb2","Carcaj",-53186.175153,-116.539911,-42675.849839,"Physic")
carcaj2ruins.Scale=1.000000
carcaj2ruins.Orientation=0.498969,0.521817,-0.496193,-0.482214
ItemTypes.ItemDefaultFuncs(carcaj2ruins)
carcaj2ruins.Data.ArrowsLeft=10


ninjatoruins=Bladex.CreateEntity("Ninjatoruins","Ninjato",-6739.568698,-13062.191145,13760.718309,"Weapon")
ninjatoruins.Scale=1.000000
ninjatoruins.Orientation=0.592632,0.217037,-0.523381,0.572499
ItemTypes.ItemDefaultFuncs(ninjatoruins)


bicheroruins=Bladex.CreateEntity("BicheroRuins","Bichero",60320.925579,-3054.960160,-21859.243890,"Weapon")
bicheroruins.Scale=1.000000
bicheroruins.Orientation=0.511560,0.740538,0.327276,-0.287751
ItemTypes.ItemDefaultFuncs(bicheroruins)


eclipseruins=Bladex.CreateEntity("EclipseRuins","Eclipse",-53559.766729,-673.588001,-32508.547557,"Weapon")
eclipseruins.Scale=1.000000
eclipseruins.Orientation=0.325136,0.734934,-0.328469,0.496253
ItemTypes.ItemDefaultFuncs(eclipseruins)


deathswordruins=Bladex.CreateEntity("DeathSwordRuins","DeathSword",-59094.418991,5152.226795,4509.470673,"Weapon")
deathswordruins.Scale=1.000000
deathswordruins.Orientation=0.771815,0.547322,-0.233523,0.224067
ItemTypes.ItemDefaultFuncs(deathswordruins)


lanzaruins=Bladex.CreateEntity("LanzaRuins","Lanza",-46336.995294,-1537.999193,46686.249293,"Weapon")
lanzaruins.Scale=1.000000
lanzaruins.Orientation=0.019814,0.678891,-0.013098,-0.733855
ItemTypes.ItemDefaultFuncs(lanzaruins)






################

################ COMESTIBLES DENTRO DE BARRILES Y CAJAS


queso1=Breakings.CreateHiddenObject("Queso1", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
queso1.Solid=1
pocimac.CreateFood("Queso1")

hogaza1=Breakings.CreateHiddenObject("Hogaza1", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
hogaza1.Solid=1
pocimac.CreateFood("Hogaza1")

queso2=Breakings.CreateHiddenObject("Queso2", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
queso2.Solid=1
pocimac.CreateFood("Queso2")

queso3=Breakings.CreateHiddenObject("Queso3", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
queso3.Solid=1
pocimac.CreateFood("Queso3")

hogaza2=Breakings.CreateHiddenObject("Hogaza2", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
hogaza2.Solid=1
pocimac.CreateFood("Hogaza2")

hogaza3=Breakings.CreateHiddenObject("Hogaza3", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
hogaza3.Solid=1
pocimac.CreateFood("Hogaza3")

hogaza4=Breakings.CreateHiddenObject("Hogaza4", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
hogaza4.Solid=1
pocimac.CreateFood("Hogaza4")

hogaza5=Breakings.CreateHiddenObject("Hogaza5", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
hogaza5.Solid=1
pocimac.CreateFood("Hogaza5")

paletilla1=Breakings.CreateHiddenObject("Paletilla1", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
paletilla1.Solid=1
pocimac.CreateFood("Paletilla1")

paletilla2=Breakings.CreateHiddenObject("Paletilla2", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
paletilla2.Solid=1
pocimac.CreateFood("Paletilla2")

hogaza6=Breakings.CreateHiddenObject("Hogaza6", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
hogaza6.Solid=1
pocimac.CreateFood("Hogaza6")

paletilla3=Breakings.CreateHiddenObject("Paletilla3", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
paletilla3.Solid=1
pocimac.CreateFood("Paletilla3")






#############################
#     Objetos rompibles     #
#############################

o=Bladex.CreateEntity("Barril1","Barril",63701.864000,-2498.008000,-18551.098000,"Physic")
o.Scale=1.220190
o.Orientation=0.596368,0.596368,-0.379928,0.379928
Breakings.SetBreakable("Barril1", 10, 20,"Hogaza4")



o=Bladex.CreateEntity("Barril2","Barril",65189.367000,-2500.132000,-18975.377000,"Physic")
o.Scale=1.220190
o.Orientation=0.521334,0.521334,0.477714,-0.477714
Breakings.SetBreakable("Barril2", 10, 20,"Hogaza5")


o=Bladex.CreateEntity("Barril3","Barril",64496.895000,-2494.673000,-18556.523000,"Physic")
o.Scale=1.220190
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril3", 10, 20,"Paletilla1")




o=Bladex.CreateEntity("Cofre1","Cofre",-42912.082000,-1045.680000,49549.137000,"Physic")
o.Scale=1.000000
o.Orientation=0.500000,0.500000,0.500000,-0.500000
Breakings.SetBreakable("Cofre1", 10, 20,"Pocima1002ruins")

o=Bladex.CreateEntity("Barril4","Barril",-49550.532000,-1000.183000,37736.813000,"Physic")
o.Scale=1.220190
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril4", 10, 20)

o=Bladex.CreateEntity("Barril5","Barril",-49596.496000,-1001.927000,38480.950000,"Physic")
o.Scale=1.220190
o.Orientation=0.612373,0.612373,0.353553,-0.353553
Breakings.SetBreakable("Barril5", 10, 20)

o=Bladex.CreateEntity("Barril6","Barril",-36745.727000,-1003.586000,43954.929000,"Physic")
o.Scale=1.220190
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril6", 10, 20)

o=Bladex.CreateEntity("Barril7","Barril",-36656.612000,-996.057000,44717.578000,"Physic")
o.Scale=1.220190
o.Orientation=0.612373,0.612373,-0.353553,0.353553
Breakings.SetBreakable("Barril7", 10, 20)

o=Bladex.CreateEntity("Cofre2","Cofre",-47189.330000,-1954.911000,35659.219000,"Physic")
o.Scale=0.836017
o.Orientation=0.500000,0.500000,-0.500000,0.500000
Breakings.SetBreakable("Cofre2", 10, 20)

o=Bladex.CreateEntity("Cofre3","Cofre",-35868.816000,-1855.789000,47696.764000,"Physic")
o.Scale=0.665003
o.Orientation=0.500000,0.500000,0.500000,-0.500000
Breakings.SetBreakable("Cofre3", 10, 20,)

o=Bladex.CreateEntity("Cofre4","Cofre",-35678.597000,-1965.316000,46610.809000,"Physic")
o.Scale=0.861349
o.Orientation=0.000000,0.000000,0.707107,-0.707107
Breakings.SetBreakable("Cofre4", 10, 20)

o=Bladex.CreateEntity("Cofre5","Cofre",-38107.537000,-1040.815000,26443.196000,"Physic")
o.Scale=1.000000
o.Orientation=0.500000,0.500000,-0.500000,0.500000
Breakings.SetBreakable("Cofre5", 10, 20)

o=Bladex.CreateEntity("Cofre6","Cofre",-26895.272000,-1032.173000,38562.003000,"Physic")
o.Scale=1.000000
o.Orientation=0.500000,0.500000,0.500000,-0.500000
Breakings.SetBreakable("Cofre6", 10, 20)



o=Bladex.CreateEntity("Barril8","Barril",36493.554000,1523.246000,-2034.308000,"Physic")
o.Scale=1.160969
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril8",10,20,"Queso1")



o=Bladex.CreateEntity("Barril9","Barril",36485.751000,1519.395000,-1305.018000,"Physic")
o.Scale=1.160969
o.Orientation=0.640856,0.640856,-0.298836,0.298836
Breakings.SetBreakable("Barril9", 10, 20,"Hogaza1")



o=Bladex.CreateEntity("Barril10","Barril",-2090.006000,1619.796000,-36547.837000,"Physic")
o.Scale=1.220190
o.Orientation=0.000000,1.000000,0.000000,0.000000
Breakings.SetBreakable("Barril10",10,20,"Queso2")




o=Bladex.CreateEntity("Barril11","Barril",-1330.537000,1619.405000,-36560.097000,"Physic")
o.Scale=1.220190
o.Orientation=0.923880,0.000000,0.000000,-0.382683
Breakings.SetBreakable("Barril11", 10, 20,"Queso3")

o=Bladex.CreateEntity("Barril12","Barril",-1711.767000,1009.614000,-36537.427000,"Physic")
o.Scale=1.220190
o.Orientation=0.000000,0.707107,0.707107,0.000000
Breakings.SetBreakable("Barril12", 10, 20,"Hogaza2")

o=Bladex.CreateEntity("Barril13","Barril",-561.145000,1499.933000,-36481.715000,"Physic")
o.Scale=1.220190
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril13", 10, 20,"Hogaza3")



o=Bladex.CreateEntity("Barril14","Barril",54025.468000,-529.172000,35252.623000,"Physic")
o.Scale=1.282432
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril14", 10, 20,"Hogaza6")

o=Bladex.CreateEntity("Barril15","Barril",54341.566000,-534.369000,34460.710000,"Physic")
o.Scale=1.282432
o.Orientation=0.579228,0.579228,-0.405580,0.405580
Breakings.SetBreakable("Barril15", 10, 20,"Paletilla2")


o=Bladex.CreateEntity("Barril16","Barril",54905.327000,-527.886000,33892.820000,"Physic")
o.Scale=1.282432
o.Orientation=0.653282,0.653282,0.270598,-0.270598
Breakings.SetBreakable("Barril16", 10, 20,"Paletilla3")






################

################ COMESTIBLES DESPERDIGADOS POR AHI


o=Bladex.CreateEntity("vidilla1","Seta",42070.794578,1901.432532,3637.835825,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood("vidilla1")


o=Bladex.CreateEntity("vidilla2","Setas",42199.457837,1891.925774,3392.898596,"Physic")
o.Scale=1.000000
o.Orientation=0.092296,0.092296,0.701057,-0.701057
pocimac.CreateFood("vidilla2")


o=Bladex.CreateEntity("vidilla3","Setas",15511.337161,-109.852394,12394.214899,"Physic")
o.Scale=1.000000
o.Orientation=0.477714,0.477714,0.521334,-0.521334
pocimac.CreateFood("vidilla3")


o=Bladex.CreateEntity("vidilla4","Seta",63474.201720,-96.069753,6836.569313,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood("vidilla4")


o=Bladex.CreateEntity("vidilla5","Seta",63073.561726,-93.862237,6617.041948,"Physic")
o.Scale=1.000000
o.Orientation=0.405580,0.405580,0.579228,-0.579228
pocimac.CreateFood("vidilla5")


o=Bladex.CreateEntity("vidilla6","Setas",63116.022430,-98.795368,6881.135058,"Physic")
o.Scale=1.000000
o.Orientation=0.122788,0.122788,0.696364,-0.696364
pocimac.CreateFood("vidilla6")


o=Bladex.CreateEntity("vidilla7","Setas",66452.306465,-103.661304,6561.641047,"Physic")
o.Scale=1.000000
o.Orientation=0.640856,0.640856,-0.298836,0.298836
pocimac.CreateFood("vidilla7")


o=Bladex.CreateEntity("vidilla8","Seta",66458.701277,-96.585854,6254.845078,"Physic")
o.Scale=1.000000
o.Orientation=0.298836,0.298836,0.640856,-0.640856
pocimac.CreateFood("vidilla8")


o=Bladex.CreateEntity("vidilla9","Raiz",31606.581883,-25.0,30871.874397,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood("vidilla9")


o=Bladex.CreateEntity("vidilla10","Rabano",31465.136913,-11.320572,31276.025745,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood("vidilla10")


o=Bladex.CreateEntity("vidilla11","Rabano",31839.244853,-11.855223,30642.221048,"Physic")
o.Scale=1.000000
o.Orientation=0.521334,0.521334,0.477714,-0.477714
pocimac.CreateFood("vidilla11")


o=Bladex.CreateEntity("vidilla12","Rabano",31470.112884,-8.984234,31032.313173,"Physic")
o.Scale=1.000000
o.Orientation=0.061628,0.061628,0.704416,-0.704416
pocimac.CreateFood("vidilla12")


o=Bladex.CreateEntity("vidilla13","Rabano",31758.538779,-14.930136,30973.445244,"Physic")
o.Scale=1.000000
o.Orientation=0.183013,0.183013,0.683013,-0.683013
pocimac.CreateFood("vidilla13")


o=Bladex.CreateEntity("vidilla14","Raiz",-44031.584951,1965.608671,-3695.165157,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood("vidilla14")


o=Bladex.CreateEntity("vidilla15","Rabano",-43825.693468,1989.338728,-3776.924424,"Physic")
o.Scale=1.000000
o.Orientation=0.627211,0.627211,0.326506,-0.326506
pocimac.CreateFood("vidilla15")


o=Bladex.CreateEntity("vidilla16","Rabano",-44046.760838,1979.908720,-3451.776617,"Physic")
o.Scale=1.000000
o.Orientation=0.612372,0.612372,-0.353553,0.353553
pocimac.CreateFood("vidilla16")


o=Bladex.CreateEntity("vidilla17","Setas",-43382.015598,1907.888560,-3814.412950,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood("vidilla17")


o=Bladex.CreateEntity("vidilla18","Seta",-43308.399050,1910.516100,-4124.921313,"Physic")
o.Scale=1.000000
o.Orientation=0.612372,0.612372,0.353553,-0.353553
pocimac.CreateFood("vidilla18")


o=Bladex.CreateEntity("vidilla19","Pocima25",12715.972651,-1538.789334,-12656.329956,"Physic")
o.Scale=1.000000
o.Orientation=0.369679,-0.412552,-0.804297,0.215045
pocimac.CreatePotion("vidilla19")


o=Bladex.CreateEntity("vidilla20","Pocima25",4478.810479,-2542.879288,10712.833486,"Physic")
o.Scale=1.000000
o.Orientation=0.104868,-0.494696,-0.083491,0.858666
pocimac.CreatePotion("vidilla20")


o=Bladex.CreateEntity("vidilla21","Pocima50",-13187.121031,-12571.467255,6231.134605,"Physic")
o.Scale=1.000000
o.Orientation=0.930401,-0.051112,0.359371,0.050922
pocimac.CreatePotion("vidilla21")


o=Bladex.CreateEntity("vidilla22","Pocima50",25475.852817,-1819.561002,-39940.206339,"Physic")
o.Scale=1.000000
o.Orientation=0.717569,0.207695,0.494617,0.444198
pocimac.CreatePotion("vidilla22")


o=Bladex.CreateEntity("vidilla23","Raiz",63972.396772,-34.0,40274.053497,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood("vidilla23")


o=Bladex.CreateEntity("vidilla24","Rabano",64078.899906,-19.995281,40510.658123,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood("vidilla24")


o=Bladex.CreateEntity("vidilla25","Rabano",63695.753751,-13.920112,40258.759075,"Physic")
o.Scale=1.000000
o.Orientation=0.627211,0.627211,0.326506,-0.326506
pocimac.CreateFood("vidilla25")


o=Bladex.CreateEntity("vidilla26","Rabano",64063.594445,-16.318929,40837.427398,"Physic")
o.Scale=1.000000
o.Orientation=0.183013,0.183013,0.683013,-0.683013
pocimac.CreateFood("vidilla26")


o=Bladex.CreateEntity("vidilla27","Raiz",63868.286309,-31.0,40571.852858,"Physic")
o.Scale=1.000000
o.Orientation=0.477714,0.477714,0.521334,-0.521334
pocimac.CreateFood("vidilla27")


o=Bladex.CreateEntity("vidilla28","Rabano",63996.670075,-14.485228,41184.765305,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood("vidilla28")


o=Bladex.CreateEntity("vidilla29","Pocima50",45415.092506,1811.705795,-1303.031596,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreatePotion("vidilla29")


o=Bladex.CreateEntity("vidilla30","Pocima25",32461.041517,8962.141286,-56033.645234,"Physic")
o.Scale=1.000000
o.Orientation=0.597363,-0.098912,0.090521,-0.790683
pocimac.CreatePotion("vidilla30")


o=Bladex.CreateEntity("vidilla31","Setas",32709.168933,8891.029183,-56152.695374,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood("vidilla31")


o=Bladex.CreateEntity("vidilla32","Seta",32563.955907,8912.946254,-55724.241675,"Physic")
o.Scale=1.000000
o.Orientation=0.000000,0.000000,0.707107,-0.707107
pocimac.CreateFood("vidilla32")


o=Bladex.CreateEntity("vidilla33","Seta",32621.650305,8905.924439,-51551.304687,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood("vidilla33")


o=Bladex.CreateEntity("vidilla34","Setas",32826.095204,8896.946330,-51334.140506,"Physic")
o.Scale=1.000000
o.Orientation=0.212631,0.212631,0.674380,-0.674380
pocimac.CreateFood("vidilla34")


o=Bladex.CreateEntity("vidilla35","Setas",32627.177133,8896.201453,-51802.082678,"Physic")
o.Scale=1.000000
o.Orientation=0.454519,0.454519,0.541675,-0.541675
pocimac.CreateFood("vidilla35")






###############################
#     Objetos chispeantes     #
###############################

o=Bladex.CreateEntity("RastrilloTesoro","Rastrillo",-23444.753000,-3250.000000,23455.711000,"Physic")
o.Scale=1.138093
o.Orientation=0.653282,0.653282,-0.270598,0.270598
Sparks.SetMetalSparkling("RastrilloTesoro")

### El rastrillo del cementerio esta en el puertas.py



######################################
#     Objetos con luz especiales     #
######################################


o=Bladex.CreateEntity("NoName230","LamparaNegra",-13268.575000,-4498.125000,-3147.288000)
o.Scale=1.000000
o.Orientation=0.500000,0.500000,-0.500000,0.500000
o.FiresIntensity=[ 3 ]
o.Lights=[ (1.421363,0.031250,(255,170,80)) ]
luz=AuxFuncs.GetSpot(o)
luz.CastShadows=0

o=Bladex.CreateEntity("NoName231","LamparaNegra",-13265.150000,-4504.926000,3138.787000)
o.Scale=1.000000
o.Orientation=0.500000,0.500000,0.500000,-0.500000
o.FiresIntensity=[ 3 ]
o.Lights=[ (1.421363,0.031250,(255,170,80)) ]
luz=AuxFuncs.GetSpot(o)
luz.CastShadows=0






##################################
#     Restos tirados por ahi     #
##################################


o=Bladex.CreateEntity("Restoa1","Skull",49072.631330,8911.469324,-44990.783801,"Weapon")
o.Scale=1.000000
o.Orientation=0.084785,0.068129,-0.803192,0.585707


o=Bladex.CreateEntity("Restoa2","Costilla",49580.791043,8946.054787,-45061.129753,"Weapon")
o.Scale=1.295256
o.Orientation=0.512014,0.491321,0.571747,0.411766


o=Bladex.CreateEntity("Restoa3","Costilla",49234.327791,8994.551335,-44897.765713,"Weapon")
o.Scale=1.220190
o.Orientation=0.431446,0.545463,-0.446073,-0.563332


o=Bladex.CreateEntity("Restoa4","Femur",49667.774656,8975.739101,-44818.101316,"Weapon")
o.Scale=1.269735
o.Orientation=0.051344,-0.714854,0.075116,-0.693329


o=Bladex.CreateEntity("Restoa5","Femur",49456.645476,8939.882506,-44915.256620,"Weapon")
o.Scale=1.232392
o.Orientation=0.044416,-0.943259,0.028072,0.327875


o=Bladex.CreateEntity("Restoa9","Skull",-59039.539695,5897.283675,3623.928487,"Weapon")
o.Scale=1.115668
o.Orientation=0.718151,0.564299,-0.396830,0.091390


o=Bladex.CreateEntity("Restoa10","Costilla",-58804.838341,5994.892069,3852.353533,"Weapon")
o.Scale=1.430769
o.Orientation=0.248972,0.712140,-0.554693,-0.350977


o=Bladex.CreateEntity("Restoa11","Costilla",-58837.638706,5972.355059,3943.329907,"Weapon")
o.Scale=1.257163
o.Orientation=0.398560,0.390541,-0.428874,-0.710418


o=Bladex.CreateEntity("Restoa12","Costilla",-58795.223236,5920.455983,4075.938902,"Weapon")
o.Scale=1.220190
o.Orientation=0.295470,0.488909,0.813576,0.108445


o=Bladex.CreateEntity("Restoa13","Femur",-58614.428556,5945.232059,3995.939505,"Weapon")
o.Scale=1.269735
o.Orientation=0.069059,0.474683,0.052202,-0.875889


o=Bladex.CreateEntity("Restoa14","Femur",-58393.595536,5892.992839,4054.147633,"Weapon")
o.Scale=1.347849
o.Orientation=0.990432,-0.092044,0.058009,-0.084896


o=Bladex.CreateEntity("Restoa17","Skull",-47369.124228,-1598.939525,-42715.189716,"Weapon")
o.Scale=1.149474
o.Orientation=0.801291,0.598270,0.001096,0.002284


o=Bladex.CreateEntity("Restoa18","Femur",-47184.122448,-1525.026584,-43037.233910,"Weapon")
o.Scale=1.196147
o.Orientation=0.029921,-0.631648,-0.057451,0.772544


o=Bladex.CreateEntity("Restoa19","Femur",-47124.733677,-1587.052488,-43024.350475,"Weapon")
o.Scale=1.196147
o.Orientation=0.085444,0.466522,-0.880372,0.001307


o=Bladex.CreateEntity("Restoa21","TelaranyaCuadrada",-32002.175819,-2298.701438,-51338.339919)
o.Scale=2.026831
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1
o.Solid=0


o=Bladex.CreateEntity("Restoa22","TelaranyaEsquina",-29980.615176,-367.175804,-54833.111960)
o.Scale=1.244716
o.Orientation=0.304417,0.638224,-0.638224,0.304417
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1
o.Solid=0


o=Bladex.CreateEntity("Restoa23","TelaranyaTriangular",-38489.859475,-4832.856752,-52656.818090)
o.Scale=2.353088
o.Orientation=0.000000,0.707107,-0.707107,0.000000
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1
o.Solid=0


o=Bladex.CreateEntity("Restoa24","Femur",-27838.738653,-25.206469,-55521.783184,"Weapon")
o.Scale=1.321291
o.Orientation=0.032303,0.954529,-0.018007,-0.295817


o=Bladex.CreateEntity("Restoa25","Femur",-28000.710775,-59.079496,-55554.942939,"Weapon")
o.Scale=1.232392
o.Orientation=0.023972,0.482953,-0.076894,-0.871934


o=Bladex.CreateEntity("Restoa26","Femur",-27549.987773,-73.439646,-55343.135375,"Weapon")
o.Scale=1.196147
o.Orientation=0.142355,-0.655642,-0.284661,0.684717


o=Bladex.CreateEntity("Restoa27","Costilla",-27517.300233,-50.864152,-54862.921085,"Weapon")
o.Scale=1.308209
o.Orientation=0.563363,0.452103,0.531222,0.442751


o=Bladex.CreateEntity("Restoa28","Costilla",-27374.866638,-3.654761,-54943.841803,"Weapon")
o.Scale=1.282432
o.Orientation=0.273734,0.689824,-0.543273,-0.392513


o=Bladex.CreateEntity("Restoa29","Costilla",-27759.433179,-5.876134,-55082.251326,"Weapon")
o.Scale=1.430769
o.Orientation=0.144104,0.772122,-0.586892,-0.196519


o=Bladex.CreateEntity("Restoa30","Costilla",-27601.595681,-41.972352,-54880.882510,"Weapon")
o.Scale=1.388690
o.Orientation=0.449956,0.413887,-0.403649,-0.680665


o=Bladex.CreateEntity("Restoa32","Skull",-28490.400103,-101.738979,-55525.772334,"Weapon")
o.Scale=1.184304
o.Orientation=0.048786,-0.062651,0.816924,-0.571253


o=Bladex.CreateEntity("Restoa33","Skull",-43915.649869,-102.816508,-53169.384822,"Weapon")
o.Scale=1.257163
o.Orientation=0.518617,0.377993,-0.606808,0.468980


o=Bladex.CreateEntity("Restoa34","Costilla",-43162.123831,-55.581802,-53268.524110,"Weapon")
o.Scale=1.374941
o.Orientation=0.579257,0.413558,0.508786,0.484322


o=Bladex.CreateEntity("Restoa35","Costilla",-43063.293719,-89.237146,-53093.018013,"Weapon")
o.Scale=1.374941
o.Orientation=0.658788,-0.068149,-0.366296,0.653591


o=Bladex.CreateEntity("Restoa36","Costilla",-43264.563191,-83.513791,-53344.852427,"Weapon")
o.Scale=1.232392
o.Orientation=0.678127,0.518068,0.320934,0.410793


o=Bladex.CreateEntity("Restoa37","Costilla",-43338.340049,-83.181416,-53066.162612,"Weapon")
o.Scale=1.257163
o.Orientation=0.840089,0.249698,0.251235,0.410831


o=Bladex.CreateEntity("Restoa38","Costilla",-43446.806089,-88.000899,-53342.765881,"Weapon")
o.Scale=1.459527
o.Orientation=0.365869,0.676191,0.617562,0.165903


o=Bladex.CreateEntity("Restoa39","Femur",-44421.144370,-23.158668,-53596.649445,"Weapon")
o.Scale=1.282432
o.Orientation=0.076474,-0.003607,0.015713,-0.996941


o=Bladex.CreateEntity("Restoa40","Femur",-43775.976741,-23.110832,-53743.098937,"Weapon")
o.Scale=1.232392
o.Orientation=0.036214,0.970316,-0.076995,-0.226378


o=Bladex.CreateEntity("Restoa41","Femur",-43736.630476,-46.059341,-53402.566861,"Weapon")
o.Scale=1.321291
o.Orientation=0.137240,0.615408,-0.130163,-0.765177


o=Bladex.CreateEntity("Restob0","Piedra_10",58039.595479,-171.471330,4746.608305,"Physic")
o.Scale=1.308209
o.Orientation=0.704072,0.709903,-0.017452,0.003917


o=Bladex.CreateEntity("Restob1","Piedra_01",57709.809864,-77.446748,4315.169147,"Physic")
o.Scale=1.000000
o.Orientation=0.937416,-0.234092,0.023652,0.256696


o=Bladex.CreateEntity("Restob2","Piedra_01",61023.720171,-74.871033,13314.164518,"Physic")
o.Scale=1.000000
o.Orientation=0.943986,-0.233302,-0.033807,0.230907


o=Bladex.CreateEntity("Restob3","Piedra_09",61800.896239,-317.293477,12953.679176,"Physic")
o.Scale=1.612226
o.Orientation=0.682672,0.729662,-0.037309,0.012646


o=Bladex.CreateEntity("Restob4","Piedra_09",40826.061763,1809.852645,6038.339798,"Physic")
o.Scale=1.000000
o.Orientation=0.209996,-0.962827,-0.086732,0.146094


o=Bladex.CreateEntity("Restob5","Piedra_01",39001.131817,1909.730604,4977.307129,"Physic")
o.Scale=1.000000
o.Orientation=0.988979,-0.069841,-0.000718,0.130544


o=Bladex.CreateEntity("Restob9","Piedra_09",19459.788973,-295.423459,33808.619955,"Physic")
o.Scale=1.488864
o.Orientation=0.682691,0.729476,-0.040944,0.011051


o=Bladex.CreateEntity("Restob10","Piedra_01",19152.458478,-90.599452,34575.564167,"Physic")
o.Scale=1.000000
o.Orientation=0.989250,-0.068535,-0.000931,0.129179


o=Bladex.CreateEntity("Restob11","Piedra_01",10250.947192,1375.049463,38750.144347,"Physic")
o.Scale=1.000000
o.Orientation=0.195191,0.316639,-0.522938,-0.766927


o=Bladex.CreateEntity("Restob12","Piedra_10",12072.346506,524.651326,38915.895689,"Physic")
o.Scale=1.000000
o.Orientation=0.694556,0.642594,-0.317101,0.064120


o=Bladex.CreateEntity("Restob13","Piedra_10",22599.595098,-171.854729,44581.466489,"Physic")
o.Scale=1.295256
o.Orientation=0.703427,0.710380,-0.021561,0.009266


o=Bladex.CreateEntity("Restob14","Piedra_01",-22074.881717,-108.592203,43883.586228,"Physic")
o.Scale=1.244716
o.Orientation=0.987427,-0.076826,-0.052796,0.127664


o=Bladex.CreateEntity("Restob15","Piedra_01",-57479.381437,-87.280844,-1318.877809,"Physic")
o.Scale=1.000000
o.Orientation=0.967353,-0.150924,-0.136832,0.150757


o=Bladex.CreateEntity("Restob16","Piedra_10",-57380.959470,-203.443344,-1961.079694,"Physic")
o.Scale=1.694466
o.Orientation=0.122130,-0.188149,0.697608,0.680461


o=Bladex.CreateEntity("Restob17","Piedra_10",-40857.493887,500.992811,-11972.936215,"Physic")
o.Scale=1.474123
o.Orientation=0.808010,0.571020,-0.084644,0.117860


o=Bladex.CreateEntity("Restob18","Piedra_01",-40822.020365,425.197107,-12281.426990,"Physic")
o.Scale=1.000000
o.Orientation=0.863676,0.280218,-0.341181,0.243182


o=Bladex.CreateEntity("Restob19","Piedra_01",-38933.652312,-90.508566,-24984.160302,"Physic")
o.Scale=1.000000
o.Orientation=0.988686,-0.073142,-0.014608,0.130140


o=Bladex.CreateEntity("Restob20","Piedra_09",-39797.820327,-275.983603,-24512.663514,"Physic")
o.Scale=1.388690
o.Orientation=0.681460,0.731527,-0.020687,-0.007226


o=Bladex.CreateEntity("Restob21","Piedra_09",-21538.180087,-204.822537,-33200.997493,"Physic")
o.Scale=1.000000
o.Orientation=0.686211,0.726108,0.006281,-0.042921


o=Bladex.CreateEntity("Restob22","Piedra_01",-21151.052191,-87.285186,-33828.510261,"Physic")
o.Scale=0.932718
o.Orientation=0.987482,-0.062044,-0.080270,0.120776


o=Bladex.CreateEntity("Restob23","Piedra_01",-9832.769753,-77.872666,-60022.304667,"Physic")
o.Scale=1.051010
o.Orientation=0.941092,-0.245014,-0.041204,0.229381


o=Bladex.CreateEntity("Restob24","Piedra_10",-10330.397954,-221.969887,-60625.754107,"Physic")
o.Scale=1.711410
o.Orientation=0.704850,0.708469,-0.030983,0.017260


o=Bladex.CreateEntity("Restob25","Piedra_09",-7707.315858,-357.333204,-60528.639634,"Physic")
o.Scale=1.816697
o.Orientation=0.683687,0.729501,-0.013598,-0.014661


o=Bladex.CreateEntity("Restob26","Piedra_09",14470.079667,-184.742344,-54637.070251,"Physic")
o.Scale=1.430769
o.Orientation=0.681299,0.730957,-0.038418,0.007555


o=Bladex.CreateEntity("Restob28","Piedra_01",13894.066751,-3.619748,-53305.081018,"Physic")
o.Scale=1.347849
o.Orientation=0.954981,-0.176432,0.064824,0.229523


o=Bladex.CreateEntity("Restob29","Piedra_10",14533.483350,-181.855799,-53771.952670,"Physic")
o.Scale=2.216715
o.Orientation=0.703722,0.707757,-0.049291,0.037776


o=Bladex.CreateEntity("Restob30","Piedra_09",13851.156472,-624.547471,-54311.000130,"Physic")
o.Scale=2.424389
o.Orientation=0.007438,-0.848227,-0.018836,-0.529245


o=Bladex.CreateEntity("Restob31","Piedra_01",15561.473261,-92.649880,-54426.749851,"Physic")
o.Scale=1.000000
o.Orientation=0.987159,-0.063228,-0.087916,0.117429


o=Bladex.CreateEntity("Restob32","Piedra_01",14852.393424,-47.499130,-52867.409614,"Physic")
o.Scale=1.269735
o.Orientation=0.745812,-0.427809,-0.505546,-0.071876


o=Bladex.CreateEntity("Restob33","Piedra_01",19767.237335,-82.433964,-32683.330874,"Physic")
o.Scale=1.000000
o.Orientation=0.961565,-0.173261,0.026241,0.211389


o=Bladex.CreateEntity("Restob34","Piedra_01",-3341.312402,-116.224840,-17086.174555,"Physic")
o.Scale=1.430769
o.Orientation=0.973717,-0.137366,0.019735,0.180599


o=Bladex.CreateEntity("Restob35","Piedra_10",-2813.868578,-233.413691,-17784.194392,"Physic")
o.Scale=1.816697
o.Orientation=0.706960,0.706469,-0.028105,0.017833


o=Bladex.CreateEntity("Restob36","Piedra_09",-3864.971435,-163.924238,-18303.464114,"Physic")
o.Scale=0.896324
o.Orientation=0.247283,-0.953946,-0.116610,0.123453


o=Bladex.CreateEntity("Restob37","Piedra_09",15873.010066,-323.530551,-8350.314973,"Physic")
o.Scale=1.644632
o.Orientation=0.684215,0.728815,-0.025914,-0.002724


o=Bladex.CreateEntity("Restob38","Piedra_01",15641.210965,-94.036837,-7142.241064,"Physic")
o.Scale=1.000000
o.Orientation=0.987455,-0.075497,0.017634,0.137555


o=Bladex.CreateEntity("Restob39","Piedra_10",15402.851189,-166.965398,-9033.536380,"Physic")
o.Scale=1.257163
o.Orientation=0.709578,0.704231,0.011928,-0.020403


o=Bladex.CreateEntity("Restob40","Piedra_10",14768.041808,-1178.886952,-8625.693919,"Physic")
o.Scale=1.361327
o.Orientation=0.959565,-0.208564,0.022746,0.187667


o=Bladex.CreateEntity("Restob41","Piedra_10",47155.110962,-2642.041988,27543.933346,"Physic")
o.Scale=1.000000
o.Orientation=0.689785,0.723842,-0.014239,-0.006833


o=Bladex.CreateEntity("Restob42","Piedra_10",48339.276974,855.345817,27067.734994,"Physic")
o.Scale=1.000000
o.Orientation=0.687607,0.725473,-0.028746,-0.007752


o=Bladex.CreateEntity("Restob43","Piedra_01",48840.270949,856.887807,26732.389373,"Physic")
o.Scale=0.836017
o.Orientation=0.265478,-0.796069,0.508728,-0.192331


o=Bladex.CreateEntity("Restob44","Piedra_01",30406.425043,-80.651697,60590.627371,"Physic")
o.Scale=1.000000
o.Orientation=0.930676,-0.221288,-0.249747,0.150003


o=Bladex.CreateEntity("Restob45","Piedra_10",30746.651577,-136.418521,60234.649966,"Physic")
o.Scale=1.000000
o.Orientation=0.712127,0.701924,-0.011771,0.006247


o=Bladex.CreateEntity("Restob46","Piedra_10",22022.770869,-137.001364,51323.349388,"Physic")
o.Scale=1.000000
o.Orientation=0.707366,0.706305,-0.027645,0.001673


o=Bladex.CreateEntity("Restob47","Piedra_10",34457.430413,-139.693639,31432.325868,"Physic")
o.Scale=1.000000
o.Orientation=0.701889,0.710264,-0.049183,0.021391


o=Bladex.CreateEntity("Restob48","Piedra_10",29552.055228,-133.866404,27617.978513,"Physic")
o.Scale=1.000000
o.Orientation=0.708120,0.705987,-0.011069,0.005186


o=Bladex.CreateEntity("Restob49","Piedra_09",30174.111808,-205.076615,27284.758646,"Physic")
o.Scale=1.000000
o.Orientation=0.677635,0.734113,-0.042967,0.006576


o=Bladex.CreateEntity("Restob50","Piedra_09",24363.194774,-204.396145,45570.025039,"Physic")
o.Scale=1.000000
o.Orientation=0.683999,0.727442,-0.051764,0.017158


o=Bladex.CreateEntity("Restob51","Skull",43434.580719,-3110.306559,55041.274770,"Weapon")
o.Scale=1.282432
o.Orientation=0.201649,0.198471,0.790100,-0.543773


o=Bladex.CreateEntity("Restob52","Femur",43236.699758,-3023.374005,54403.146949,"Weapon")
o.Scale=1.308209
o.Orientation=0.032111,0.973356,-0.059521,-0.219099


o=Bladex.CreateEntity("Restob53","Femur",43576.142444,-3045.939533,54437.531834,"Weapon")
o.Scale=1.220190
o.Orientation=0.078857,-0.744262,0.033290,-0.662380


o=Bladex.CreateEntity("Restob54","TelaranyaEsquina",43392.971905,-6699.443346,52962.657437)
o.Scale=1.628348
o.Orientation=0.512917,-0.018510,-0.486740,0.706864
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1
o.Solid=0


o=Bladex.CreateEntity("Restob55","TelaranyaCuadrada",39270.304154,-6100.446230,57436.013445)
o.Scale=1.834864
o.Orientation=0.596368,0.596368,-0.379928,0.379928
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1
o.Solid=0


o=Bladex.CreateEntity("Restob56","TelaranyaTriangular",63392.015666,-806.228179,56615.736046)
o.Scale=1.374941
o.Orientation=0.653282,0.270598,-0.270598,-0.653282
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1
o.Solid=0


o=Bladex.CreateEntity("Restob57","TelaranyaCuadrada",58763.293719,-5082.021519,32241.774653)
o.Scale=2.871214
o.Orientation=0.653282,0.653282,-0.270598,0.270598
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1
o.Solid=0


o=Bladex.CreateEntity("Restob58","TelaranyaTriangular",39169.495296,-835.695023,4044.254576)
o.Scale=1.347849
o.Orientation=0.000000,0.000000,0.707107,0.707107
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1
o.Solid=0


o=Bladex.CreateEntity("Restob59","TelaranyaTriangular",4150.797231,-740.886918,39262.772944)
o.Scale=1.533978
o.Orientation=0.500000,-0.500000,0.500000,0.500000
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1
o.Solid=0


o=Bladex.CreateEntity("Restob60","TelaranyaCuadrada",-33485.650197,-4579.360358,23503.629375)
o.Scale=3.047852
o.Orientation=0.579228,0.405580,0.579228,-0.405580
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1
o.Solid=0


o=Bladex.CreateEntity("Restob61","TelaranyaTriangular",-52525.037866,-2530.197671,34979.939219)
o.Scale=1.564811
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1
o.Solid=0


o=Bladex.CreateEntity("Restob62","TelaranyaTriangular",11787.401348,-1435.130101,-40945.193516)
o.Scale=1.138093
o.Orientation=0.707107,0.000000,0.000000,-0.707107
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1
o.Solid=0


o=Bladex.CreateEntity("Restob63","TelaranyaTriangular",8580.263229,-333.126178,11226.123680)
o.Scale=1.321291
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1
o.Solid=0


o=Bladex.CreateEntity("Restob64","TelaranyaTriangular",-4594.312095,2978.491352,12473.679048)
o.Scale=1.967222
o.Orientation=0.707107,-0.000000,0.000000,-0.707107
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1
o.Solid=0


o=Bladex.CreateEntity("Restob66","TelaranyaTriangular",52383.253916,5122.064097,-58127.581771)
o.Scale=1.257163
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1
o.Solid=0


o=Bladex.CreateEntity("Restob67","TelaranyaTriangular",66385.245805,-5410.881177,-42919.917944)
o.Scale=2.194768
o.Orientation=0.707107,-0.000000,0.000000,-0.707107
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1
o.Solid=0


o=Bladex.CreateEntity("Restob69","Piedra_02",68539.714570,5861.989024,43604.908160,"Physic")
o.Scale=1.000000
o.Orientation=0.760213,0.630892,-0.081003,-0.132248


o=Bladex.CreateEntity("Restob70","Piedra_03",68331.831753,5903.750675,42853.601645,"Physic")
o.Scale=0.741923
o.Orientation=0.654189,0.750504,-0.019245,-0.091706


o=Bladex.CreateEntity("Restob72","Piedra_04",59448.444896,6410.487774,35474.481791,"Physic")
o.Scale=1.000000
o.Orientation=0.018505,0.965925,-0.081188,-0.245061


o=Bladex.CreateEntity("Restob73","Piedra_04",50914.389987,6727.648105,38566.519623,"Physic")
o.Scale=0.787566
o.Orientation=0.051004,0.970234,-0.089894,-0.219005


o=Bladex.CreateEntity("Restob74","Piedra_03",52302.855717,6891.235138,39192.006484,"Physic")
o.Scale=0.844377
o.Orientation=0.666063,0.740298,0.000875,-0.091203


o=Bladex.CreateEntity("Restob75","Piedra_03",44427.321828,7382.250345,22939.774962,"Physic")
o.Scale=1.000000
o.Orientation=0.644851,0.759655,-0.052524,-0.065827


o=Bladex.CreateEntity("Restob76","Piedra_02",44219.455680,7323.481823,23762.678331,"Physic")
o.Scale=1.347849
o.Orientation=0.761036,0.615217,0.005885,-0.205662


o=Bladex.CreateEntity("Restob78","Piedra_04",51454.519321,7164.378243,4571.091519,"Physic")
o.Scale=1.000000
o.Orientation=0.070666,0.971374,-0.100288,-0.203424


o=Bladex.CreateEntity("Restob79","Piedra_04",58243.742989,7174.331347,-7461.441190,"Physic")
o.Scale=1.000000
o.Orientation=0.142724,0.957303,-0.132846,-0.213429


o=Bladex.CreateEntity("Restob80","Piedra_03",58729.143427,7387.104942,-6422.201109,"Physic")
o.Scale=0.887449
o.Orientation=0.659458,0.747883,-0.035952,-0.067039


o=Bladex.CreateEntity("Restob81","Piedra_03",47673.728305,7379.516769,-19093.684710,"Physic")
o.Scale=1.000000
o.Orientation=0.643717,0.760255,-0.046522,-0.074005


o=Bladex.CreateEntity("Restob82","Piedra_02",46986.620778,7362.273664,-18519.158538,"Physic")
o.Scale=1.000000
o.Orientation=0.749048,0.644464,-0.088130,-0.125799


o=Bladex.CreateEntity("Restob83","Piedra_02",50990.647607,8329.945282,-30234.696027,"Physic")
o.Scale=1.282432
o.Orientation=0.763467,0.616201,-0.009065,-0.193217


o=Bladex.CreateEntity("Restob84","Piedra_02",54472.773592,8861.411744,-46649.489426,"Physic")
o.Scale=1.000000
o.Orientation=0.757422,0.634665,-0.074910,-0.133796


o=Bladex.CreateEntity("Restob85","Piedra_03",45314.273073,8811.678383,-43227.522017,"Physic")
o.Scale=1.661078
o.Orientation=0.640437,0.763264,-0.056090,-0.064208


o=Bladex.CreateEntity("Restob86","Piedra_03",46203.206029,8885.294380,-53493.408043,"Physic")
o.Scale=1.000000
o.Orientation=0.089202,-0.072527,-0.895975,-0.428967


o=Bladex.CreateEntity("Restob87","Piedra_02",45972.289544,8859.111812,-54221.833939,"Physic")
o.Scale=1.000000
o.Orientation=0.747286,0.646047,-0.074108,-0.136729


o=Bladex.CreateEntity("Restob89","Piedra_04",24223.454743,8665.821045,-57084.690214,"Physic")
o.Scale=1.000000
o.Orientation=0.035579,0.983295,-0.086869,-0.155945


o=Bladex.CreateEntity("Restob90","Piedra_03",23103.080276,8879.621630,-56712.370161,"Physic")
o.Scale=1.000000
o.Orientation=0.650310,0.754069,-0.039268,-0.083278


o=Bladex.CreateEntity("Restob91","Piedra_03",5443.030072,8840.551998,-62119.300811,"Physic")
o.Scale=1.361327
o.Orientation=0.639912,0.763799,-0.051772,-0.066652


o=Bladex.CreateEntity("Restob92","Piedra_02",-10791.968422,8800.410656,-44235.066573,"Physic")
o.Scale=1.503752
o.Orientation=0.749779,0.642591,-0.093514,-0.127135


o=Bladex.CreateEntity("Restob93","Piedra_04",-19012.086717,8702.475903,-51492.624074,"Physic")
o.Scale=1.000000
o.Orientation=0.242438,0.934478,-0.187972,-0.180668


o=Bladex.CreateEntity("Restob94","Piedra_04",-27694.037067,7718.859670,-58106.110901,"Physic")
o.Scale=1.295256
o.Orientation=0.663086,0.729899,-0.125513,-0.108679


o=Bladex.CreateEntity("Restob95","Piedra_02",-27476.575653,7873.789658,-56847.246751,"Physic")
o.Scale=0.844377
o.Orientation=0.753346,0.635536,-0.045179,-0.162858


o=Bladex.CreateEntity("Restob97","Piedra_04",-73388.008464,5664.732561,-26127.596642,"Physic")
o.Scale=1.000000
o.Orientation=0.042592,0.957322,-0.085458,-0.272795


o=Bladex.CreateEntity("Restob98","Piedra_02",-72664.747926,5853.435752,-26240.825282,"Physic")
o.Scale=0.803396
o.Orientation=0.676863,0.712982,-0.031626,-0.180313


o=Bladex.CreateEntity("Restob99","Piedra_02",-81502.056250,5864.666475,-19955.116098,"Physic")
o.Scale=1.000000
o.Orientation=0.763610,0.616984,-0.009167,-0.190124


o=Bladex.CreateEntity("Restob100","Piedra_02",-77045.753662,5854.458231,-1058.261259,"Physic")
o.Scale=1.000000
o.Orientation=0.750221,0.633120,-0.018088,-0.189736


o=Bladex.CreateEntity("Restob101","Piedra_03",-80717.648395,5850.268483,-3100.371791,"Physic")
o.Scale=1.282432
o.Orientation=0.641670,0.761748,-0.044016,-0.077862


o=Bladex.CreateEntity("Restob102","Piedra_03",-66076.035633,5877.181409,10683.089807,"Physic")
o.Scale=1.000000
o.Orientation=0.642137,0.761402,-0.036515,-0.081206


o=Bladex.CreateEntity("Restob103","Piedra_04",-65436.366018,5671.370998,9905.437854,"Physic")
o.Scale=1.000000
o.Orientation=0.119343,0.963670,-0.121753,-0.205607


o=Bladex.CreateEntity("Restob104","Piedra_04",-70704.306919,5700.840796,21639.608524,"Physic")
o.Scale=1.000000
o.Orientation=0.416325,0.876707,-0.177104,-0.163376


o=Bladex.CreateEntity("Restob105","Piedra_04",-54189.795040,5700.936118,11438.060924,"Physic")
o.Scale=1.000000
o.Orientation=0.247995,0.932652,-0.186920,-0.183631


o=Bladex.CreateEntity("Restob106","Piedra_03",-52629.415654,5878.718253,11587.836784,"Physic")
o.Scale=1.000000
o.Orientation=0.664786,0.743995,-0.037303,-0.056022


o=Bladex.CreateEntity("Restob107","Piedra_03",-40396.173133,6122.021887,12090.920598,"Physic")
o.Scale=1.000000
o.Orientation=0.628108,0.774110,-0.062165,-0.048679


o=Bladex.CreateEntity("Restob108","Piedra_04",-42386.349587,6029.255946,12005.588428,"Physic")
o.Scale=1.000000
o.Orientation=0.655733,0.735671,-0.153107,-0.073217


o=Bladex.CreateEntity("Restob109","TelaranyaCuadrada",-52680.914493,-4415.248313,-50645.295802)
o.Scale=2.194768
o.Orientation=0.653282,0.653282,0.270598,-0.270598
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1
o.Solid=0


o=Bladex.CreateEntity("Restob110","TelaranyaTriangular",-67857.721333,2358.921259,-33668.164906)
o.Scale=1.745810
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.CastShadows=0
o.Alpha=0.99
o.RasterMode="AdditiveAlpha"
o.SelfIlum=0.1
o.Solid=0





##############################
#     Objetos invisibles     #
##############################


o=Bladex.CreateEntity("BarraInv1","BarraCareto",46000.000000,-5600.000000,-13750.000000)
o.Scale=4.675337
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BarraInv2","BarraCareto",46000.000000,-5600.000000,13750.000000)
o.Scale=4.675337
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BarraInv3","BarraCareto",13750.000000,-5600.000000,46000.000000)
o.Scale=4.675337
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BarraInv4","BarraCareto",-13750.000000,-5600.000000,46000.000000)
o.Scale=4.675337
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BarraInv5","BarraCareto",-48000.000000,-5600.000000,13750.000000)
o.Scale=4.675337
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BarraInv6","BarraCareto",-48000.000000,-5600.000000,-13750.000000)
o.Scale=4.675337
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BarraInv7","BarraCareto",-13750.000000,-5600.000000,-46000.000000)
o.Scale=4.675337
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BarraInv8","BarraCareto",13750.000000,-5600.000000,-46000.000000)
o.Scale=4.675337
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BarraInvPir1","BarraCareto",-39687.127000,-13250.000000,3675.115000)
o.Scale=3.468740
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BarraInvPir2","BarraCareto",-38427.743472,-12976.773799,2427.333271)
o.Scale=2.928926
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BarraInv1Altar","BarraCareto",5799.351531,-4303.279582,-695.556468)
o.Scale=4.027099
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.ExclusionMask=2|4
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("BarraInv2Altar","BarraCareto",5799.352000,-4303.280000,703.443000)
o.Scale=4.027099
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.ExclusionMask=2|4
o.CastShadows=0
o.Alpha = 0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")
