import Breakings
import Actions
BoxBurnTime = 6
BoxDestroyTime = 12
import Torchs
import pocimac




comida=Breakings.CreateHiddenObject("Comida1", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
comida.Solid=1
comida.Static=0
pocimac.CreateFood("Comida1")

o=Bladex.CreateEntity("Tinaja1","Tinaja",311190.023000,230.010000,-200136.879000)
o.Static=0
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Tinaja1",10,20,"Comida1")
Actions.SetBurnable("Tinaja1",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("Tinaja2","Tinaja",311436.521000,-231.825000,-201603.152000)
o.Static=0
o.Scale=1.612226
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Tinaja2",12,100)




comida=Breakings.CreateHiddenObject("Comida2", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
comida.Solid=1
comida.Static=0
pocimac.CreateFood("Comida2")

o=Bladex.CreateEntity("Tinaja3","Tinaja",310233.719000,128.390000,-200866.500000)
o.Static=0
o.Scale=1.126825
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Tinaja3",12,100)
Breakings.SetBreakable("Tinaja3",10,20,"Comida2")
Actions.SetBurnable("Tinaja3",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("Tinaja4","Tinaja",310501.541000,539.167000,-202136.917000)
o.Static=0
o.Scale=1.000000
o.Orientation=0.795796,0.286868,-0.337253,-0.413129
Breakings.SetBreakable("Tinaja4",12,100)




o=Bladex.CreateEntity("Barril1","Barril",293666.999000,333.582000,-192691.594000)
o.Static=0
o.Scale=1.580459
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril1",12,100)
Actions.SetBurnable("Barril1",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("Barril2","Barril",294216.578000,491.875000,-191752.553000)
o.Static=0
o.Scale=1.196147
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril2",12,100)
Actions.SetBurnable("Barril2",BoxBurnTime,BoxDestroyTime)



comida=Breakings.CreateHiddenObject("Comida3", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
comida.Solid=1
comida.Static=0
pocimac.CreateFood("Comida3")

o=Bladex.CreateEntity("Barril3","Barril",294751.809000,613.962000,-192411.406000)
o.Static=0
o.Scale=1.208109
o.Orientation=0.657185,0.221560,0.211448,0.688701
Breakings.SetBreakable("Barril3",10,20,"Comida3")
Actions.SetBurnable("Barril3",BoxBurnTime,BoxDestroyTime)




comida=Breakings.CreateHiddenObject("Comida4", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
comida.Solid=1
comida.Static=0
pocimac.CreateFood("Comida4")

o=Bladex.CreateEntity("Barril4","Barril",296179.992000,574.600000,-191621.246000)
o.Static=0
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril4",10,20,"Comida4")
Actions.SetBurnable("Barril4",BoxBurnTime,BoxDestroyTime)


pocima=Breakings.CreateHiddenObject("Pocimabarril", "Pocima50",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pocima.Solid=1
pocima.Static=0
pocimac.CreatePotion("Pocimabarril")

o=Bladex.CreateEntity("Cofre1","Cofre",295217.427000,448.063000,-200247.955000)
o.Static=0
o.Scale=1.000000
o.Orientation=0.500000,0.500000,-0.500000,0.500000
Breakings.SetBreakable("Cofre1",10,20,"Pocimabarril")
Actions.SetBurnable("Cofre1",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("Tinaja5","Tinaja",293803.228000,215.526000,-199734.319000)
o.Static=0
o.Scale=1.000000
o.Orientation=0.715410,0.696277,-0.022162,0.053806
Breakings.SetBreakable("Tinaja5",12,100)




o=Bladex.CreateEntity("Tinaja6","Tinaja",293864.297000,390.517000,-198965.236000)
o.Static=0
o.Scale=0.779768
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Tinaja6",12,100)




o=Bladex.CreateEntity("Barril5","Barril",339370.200827,366.075648,-203989.668343)
o.Static=0
o.Scale=1.503752
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril5",12,100)
Actions.SetBurnable("Barril5",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("Barril6","Barril",339382.334179,-664.839120,-203997.497879)
o.Static=0
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril6",12,100)
Actions.SetBurnable("Barril6",BoxBurnTime,BoxDestroyTime)




comida=Breakings.CreateHiddenObject("Comida5", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
comida.Solid=1
comida.Static=0
pocimac.CreateFood("Comida5")

o=Bladex.CreateEntity("Barril7","Barril",340574.827042,295.686730,-204463.006901)
o.Static=0
o.Scale=1.677689
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril7",10,20,"Comida5")
Actions.SetBurnable("Barril7",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("Barril8","Barril",341874.043359,-102.130693,-203715.019886)
o.Static=0
o.Scale=2.651518
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril8",12,100)
Actions.SetBurnable("Barril8",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("Barril9","Barril",340329.131462,212.206779,-202970.491242)
o.Static=0
o.Scale=1.890462
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril9",12,100)
Actions.SetBurnable("Barril9",BoxBurnTime,BoxDestroyTime)



comida=Breakings.CreateHiddenObject("Comida6", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
comida.Solid=1
comida.Static=0
pocimac.CreateFood("Comida6")

o=Bladex.CreateEntity("Tinaja7","Tinaja",342352.737147,228.437423,-201986.693785)
o.Static=0
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Tinaja7",10,20,"Comida6")
Actions.SetBurnable("Tinaja7",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("Tinaja8","Tinaja",339325.855139,-198.332592,-200447.535028)
o.Static=0
o.Scale=1.564811
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Tinaja8",12,100)





o=Bladex.CreateEntity("Barril10","Barril",389389.735476,9245.729,-204858.540551)
o.Static=0
o.Scale=1.798710
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril10",12,100)
Actions.SetBurnable("Barril10",BoxBurnTime,BoxDestroyTime)



comida=Breakings.CreateHiddenObject("Comida7", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
comida.Solid=1
comida.Static=0
pocimac.CreateFood("Comida7")

o=Bladex.CreateEntity("Barril11","Barril",389644.078069,9340.936,-205936.630763)
o.Static=0
o.Scale=1.564811
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril11",12,100,"Comida7")
Actions.SetBurnable("Barril10",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("Barril12","Barril",388862.271281,9574.856,-205601.829110)
o.Static=0
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril12",12,100)
Actions.SetBurnable("Barril12",BoxBurnTime,BoxDestroyTime)





o=Bladex.CreateEntity("Barril13","Barril",392192.725972,20073.490119,-216820.026145)
o.Static=0
o.Scale=2.216715
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril13",12,100)
Actions.SetBurnable("Barril13",BoxBurnTime,BoxDestroyTime)



comida=Breakings.CreateHiddenObject("Comida8", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
comida.Solid=1
comida.Static=0
pocimac.CreateFood("Comida8")

o=Bladex.CreateEntity("Barril14","Barril",393632.407002,20215.006806,-216723.711690)
o.Static=0
o.Scale=1.871744
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril14",12,100,"Comida8")
Actions.SetBurnable("Barril14",BoxBurnTime,BoxDestroyTime)



comida=Breakings.CreateHiddenObject("Comida9", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
comida.Solid=1
comida.Static=0
pocimac.CreateFood("Comida9")

o=Bladex.CreateEntity("Barril15","Barril",394202.689166,20636.920430,-217726.284298)
o.Static=0
o.Scale=1.244716
o.Orientation=0.053996,-0.924854,-0.184966,0.327898
Breakings.SetBreakable("Barril15",12,100,"Comida9")
Actions.SetBurnable("Barril15",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("Barril16","Barril",394964.073601,20266.279005,-218412.506212)
o.Static=0
o.Scale=1.745810
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril16",12,100)
Actions.SetBurnable("Barril16",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("Barril17","Barril",392639.095929,20044.439550,-218359.069200)
o.Static=0
o.Scale=2.283884
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril17",12,100)
Actions.SetBurnable("Barril17",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("Barril18","Barril",392293.596811,20312.002869,-219587.627638)
o.Static=0
o.Scale=1.628348
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril18",12,100)
Actions.SetBurnable("Barril18",BoxBurnTime,BoxDestroyTime)





o=Bladex.CreateEntity("Barril19","Barril",393671.709595,20450.172982,-219499.258941)
o.Static=0
o.Scale=1.728525
o.Orientation=0.486971,0.512952,0.494401,0.505279
Breakings.SetBreakable("Barril19",12,100)
Actions.SetBurnable("Barril19",BoxBurnTime,BoxDestroyTime)


comida=Breakings.CreateHiddenObject("Comida10", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
comida.Solid=1
comida.Static=0
pocimac.CreateFood("Comida10")

o=Bladex.CreateEntity("Barril20","Barril",395011.884013,20505.795881,-219790.483144)
o.Static=0
o.Scale=1.172579
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril20",12,100,"Comida10")
Actions.SetBurnable("Barril20",BoxBurnTime,BoxDestroyTime)


comida=Breakings.CreateHiddenObject("Comida11", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
comida.Solid=1
comida.Static=0
pocimac.CreateFood("Comida11")

o=Bladex.CreateEntity("Tinaja9","Tinaja",334496.545223,15464.557368,-224008.241665)
o.Static=0
o.Scale=1.347849
Breakings.SetBreakable("Tinaja9",12,100,"Comida11")
Actions.SetBurnable("Tinaja9",BoxBurnTime,BoxDestroyTime)


comida=Breakings.CreateHiddenObject("Comida12", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
comida.Solid=1
comida.Static=0
pocimac.CreateFood("Comida12")

o=Bladex.CreateEntity("Tinaja10","Tinaja",334229.775090,15723.830066,-222934.551335)
o.Static=0
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Tinaja10",12,100,"Comida12")
Actions.SetBurnable("Tinaja10",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("Tinaja11","Tinaja",335965.682725,15379.803446,-223921.752711)
o.Static=0
o.Scale=1.459527
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Tinaja11",12,100)


comida=Breakings.CreateHiddenObject("Comida13", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
comida.Solid=1
comida.Static=0
pocimac.CreateFood("Comida13")

o=Bladex.CreateEntity("Tinaja12a","Tinaja",335228.932217,16027.132969,-222483.479635)
o.Static=0
o.Scale=1.196147
o.Orientation=0.319342,0.539827,0.768238,0.128134
Breakings.SetBreakable("Tinaja12a",12,100,"Comida13")
Actions.SetBurnable("Tinaja12a",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("Barril21","Barril",357120.522396,8975.298525,-234767.860251)
o.Static=0
o.Scale=1.728525
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril21",12,100)
Actions.SetBurnable("Barril21",BoxBurnTime,BoxDestroyTime)





o=Bladex.CreateEntity("Barril22","Barril",357833.272054,9077.336965,-233790.338908)
o.Static=0
o.Scale=1.488864
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril22",12,100)
Actions.SetBurnable("Barril22",BoxBurnTime,BoxDestroyTime)





o=Bladex.CreateEntity("Barril23","Barril",356160.465007,8892.432424,-235655.864041)
o.Static=0
o.Scale=1.928460
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril23",12,100)
Actions.SetBurnable("Barril23",BoxBurnTime,BoxDestroyTime)





o=Bladex.CreateEntity("Barril24","Barril",356668.246940,8864.328509,-233685.970366)
o.Static=0
o.Scale=1.986894
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril24",12,100)
Actions.SetBurnable("Barril24",BoxBurnTime,BoxDestroyTime)





o=Bladex.CreateEntity("Barril25","Barril",355594.164633,9063.473044,-234473.385602)
o.Static=0
o.Scale=1.503752
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril25",12,100)
Actions.SetBurnable("Barril25",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("Barril26","Barril",354965.527368,8912.244385,-236041.065596)
o.Static=0
o.Scale=1.871744
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril26",12,100)
Actions.SetBurnable("Barril26",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("Tinaja12","Tinaja",294390.953493,9227.034378,-202798.277969)
o.Static=0
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Tinaja12",12,100)


comida=Breakings.CreateHiddenObject("Comida14", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
comida.Solid=1
comida.Static=0
pocimac.CreateFood("Comida14")

o=Bladex.CreateEntity("Tinaja13","Tinaja",294347.071478,8975.005804,-201463.245069)
o.Static=0
o.Scale=1.334504
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Tinaja13",12,100,"Comida14")
Actions.SetBurnable("Tinaja13",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("Barril27","Barril",289167.222510,9199.550246,-184503.003465)
o.Static=0
o.Scale=1.909366
o.Orientation=0.708169,0.705910,-0.007476,0.011448
Breakings.SetBreakable("Barril27",12,100)
Actions.SetBurnable("Barril27",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("Barril28","Barril",295111.413539,9342.167140,-189131.450703)
o.Static=0
o.Scale=1.564811
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril28",12,100)
Actions.SetBurnable("Barril28",BoxBurnTime,BoxDestroyTime)



comida=Breakings.CreateHiddenObject("Comida15", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
comida.Solid=1
comida.Static=0
pocimac.CreateFood("Comida15")

o=Bladex.CreateEntity("Barril29","Barril",296488.982316,9124.173281,-189166.782756)
o.Static=0
o.Scale=2.088246
o.Orientation=0.706438,0.701264,0.067858,-0.067595
Breakings.SetBreakable("Barril29",12,100,"Comida15")
Actions.SetBurnable("Barril29",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("Barril30","Barril",339140.886337,428.347497,-202988.507573)
o.Static=0
o.Scale=1.361327
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("Barril30",12,100)
Actions.SetBurnable("Barril30",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("Cajon1","Cajon2",287401.199492,9401.411167,-192733.660301)
o.Static=0
o.Scale=1.000000
o.Orientation=0.504344,0.504344,-0.495618,0.495618
Breakings.SetBreakable("Cajon1",12,100)
Actions.SetBurnable("Cajon1",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("Cajon2","Cajon2",288724.263505,9125.262251,-192564.187009)
o.Static=0
o.Scale=1.000000
o.Orientation=0.534229,0.460786,0.464083,0.535633
Breakings.SetBreakable("Cajon2",12,100)
Actions.SetBurnable("Cajon2",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("Cajon3","Cajama",290771.476632,9444.520597,-184502.539326)
o.Static=0
o.Scale=1.295256
o.Orientation=0.622281,0.623707,0.335099,-0.333864
Breakings.SetBreakable("Cajon3",12,100)
Actions.SetBurnable("Cajon3",BoxBurnTime,BoxDestroyTime)













o=Bladex.CreateEntity("NoName16","Barril",320217.267726,44487.553021,-89166.346308)
o.Static=0
o.Scale=1.612226
o.Orientation=0.505681,0.492411,-0.502638,-0.499173
Breakings.SetBreakable("NoName16",12,100)
Actions.SetBurnable("NoName16",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("NoName17","Barril",321173.363194,44549.571153,-90367.976178)
o.Static=0
o.Scale=1.430769
o.Orientation=0.610886,0.338132,0.323480,0.638628
Breakings.SetBreakable("NoName17",12,100)
Actions.SetBurnable("NoName17",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("NoName18","Barril",318448.502552,44420.607185,-88869.527910)
o.Static=0
o.Scale=1.947745
o.Orientation=0.831100,-0.013317,-0.020138,0.555599
Breakings.SetBreakable("NoName18",12,100)
Actions.SetBurnable("NoName18",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("NoName19","Barril",318054.029652,44460.022330,-90515.117941)
o.Static=0
o.Scale=1.871744
o.Orientation=0.413159,0.559397,-0.378308,-0.610949
Breakings.SetBreakable("NoName19",12,100)
Actions.SetBurnable("NoName19",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("NoName20","Barril",316943.603250,44576.326096,-89258.576693)
o.Static=0
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("NoName20",12,100)
Actions.SetBurnable("NoName20",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("NoName21","Barril",319511.825005,44623.265926,-90571.626896)
o.Static=0
o.Scale=1.321291
o.Orientation=0.010171,-0.977517,-0.200295,0.065108
Breakings.SetBreakable("NoName21",12,100)
Actions.SetBurnable("NoName21",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("NoName23","Cajon2",340252.669870,1898.482250,-148197.839732)
o.Static=0
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("NoName23",12,100)
Actions.SetBurnable("NoName23",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("NoName24","Cajon2",339840.966878,1756.803924,-150446.134140)
o.Static=0
o.Scale=1.244716
o.Orientation=0.664463,0.664463,0.241845,-0.241845
Breakings.SetBreakable("NoName24",12,100)
Actions.SetBurnable("NoName24",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("NoName25","Cajon2",339886.932614,1972.430227,-146187.130287)
o.Static=0
o.Scale=0.878663
o.Orientation=0.653282,0.653282,0.270598,-0.270598
Breakings.SetBreakable("NoName25",12,100)
Actions.SetBurnable("NoName25",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("NoName27","Armero",310560.066356,-5836.530603,-154013.032416,"Physic")
o.Scale=1.000000
o.Orientation=0.482246,0.482246,-0.517145,0.517145
Breakings.SetBreakable("NoName27",12,100)



o=Bladex.CreateEntity("NoName28","Barril",310337.811734,-5595.979071,-152328.478693)
o.Static=0
o.Scale=1.416603
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("NoName28",12,100)
Actions.SetBurnable("NoName28",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("NoName29","Barril",309412.341532,-5425.983458,-152171.348146)
o.Static=0
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("NoName29",12,100)
Actions.SetBurnable("NoName29",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("NoName30","Barril",311193.593853,-5658.294816,-151470.334768)
o.Static=0
o.Scale=1.564811
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("NoName30",12,100)
Actions.SetBurnable("NoName30",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("NoName31","Barril",310113.614547,-5534.758141,-150864.627788)
o.Static=0
o.Scale=1.257163
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("NoName31",12,100)
Actions.SetBurnable("NoName31",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("NoName32","Barril",339288.012598,376.398787,-190168.864771)
o.Static=0
o.Scale=1.488864
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("NoName32",12,100)
Actions.SetBurnable("NoName32",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("NoName33","Barril",340809.345116,219.250439,-189561.784086)
o.Static=0
o.Scale=1.853212
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("NoName33",12,100)
Actions.SetBurnable("NoName33",BoxBurnTime,BoxDestroyTime)


pocima=Breakings.CreateHiddenObject("PocimaCofre", "PocimaTodo",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pocima.Solid=1
pocima.Static=0
pocimac.CreatePotion("PocimaCofre")


o=Bladex.CreateEntity("NoName35","Cofre",339906.388179,444.610813,-186149.829897)
o.Static=0
o.Scale=1.000000
o.Orientation=0.495618,0.495618,0.504344,-0.504344
Breakings.SetBreakable("NoName35",12,100,"PocimaCofre")
Actions.SetBurnable("NoName35",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("NoName37","Barril",341494.509600,576.814664,-186677.247322)
o.Static=0
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("NoName37",12,100)
Actions.SetBurnable("NoName37",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("NoName38","Barril",342064.758796,145.602973,-187882.908376)
o.Static=0
o.Scale=2.047099
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("NoName38",12,100)
Actions.SetBurnable("NoName38",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("NoName40","Armero",360638.810917,9166.880552,-216473.538215,"Physic")
o.Scale=1.000000
o.Orientation=0.500000,0.500000,-0.500000,0.500000
Breakings.SetBreakable("NoName40",12,100)


o=Bladex.CreateEntity("NoName43","Barril",361214.451862,9570.676492,-215104.217569)
o.Static=0
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("NoName43",12,100)
Actions.SetBurnable("NoName43",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("NoName44","Barril",361307.280166,9485.297915,-217937.596064)
o.Static=0
o.Scale=1.220190
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("NoName44",12,100)
Actions.SetBurnable("NoName44",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("NoName370","Armero",296347.811000,164.902000,-192740.087000,"Physic")
o.Scale=1.000000
o.Orientation=0.500000,0.500000,0.500000,-0.500000
Breakings.SetBreakable("NoName370",12,100)
