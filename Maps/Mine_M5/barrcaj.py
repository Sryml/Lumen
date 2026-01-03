

import Breakings
import Actions
BoxBurnTime = 6
BoxDestroyTime = 12
import Torchs
import pocimac


###3 BARRILES TRAS EL PRIMER PUENTE AL EMPEZAR


o=Bladex.CreateEntity("BarrInicio1","Barril",35996.121555,-17152.980528,-82570.102199,"Physic")
o.Scale=1.549318
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("pan2", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pan2")
Breakings.SetBreakable("BarrInicio1",12,100,"pan2")
Actions.SetBurnable("BarrInicio1",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("BarrInicio2","Barril",35364.639786,-17202.310437,-81637.973399,"Physic")
o.Scale=1.677689
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrInicio2",12,100)
Actions.SetBurnable("BarrInicio2",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("BarrInicio3","Barril",34301.149304,-16891.417152,-81376.937284,"Physic")
o.Scale=1.295256
o.Orientation=0.800554,0.181017,0.035918,0.570137
Breakings.SetBreakable("BarrInicio3",12,100)
Actions.SetBurnable("BarrInicio3",BoxBurnTime,BoxDestroyTime)



### 4 CAJAS FRENTE A ESCALERAS INCLINADAS, EN EXTERIOR


o=Bladex.CreateEntity("CajExt1","Cajon2",6570.227758,-7845.732001,-112173.890438,"Physic")
o.Scale=1.000000
o.Orientation=0.612372,0.612372,0.353553,-0.353553
pan=Breakings.CreateHiddenObject("pan1", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pan1")
Breakings.SetBreakable("CajExt1",12,100,"pan1")
Actions.SetBurnable("CajExt1",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("CajExt2","Cajon2",4781.496717,-7728.014017,-111619.505424,"Physic")
o.Scale=0.787566
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("pan3", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pan3")
Breakings.SetBreakable("CajExt2",12,100,"pan3")
Actions.SetBurnable("CajExt2",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("CajExt3","Cajon2",6716.830053,-8826.884694,-111688.677870,"Physic")
o.Scale=0.779768
o.Orientation=0.500000,0.500000,-0.500000,0.500000
pan=Breakings.CreateHiddenObject("ques111", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("ques111")
Breakings.SetBreakable("CajExt3",12,100,"ques111")
Actions.SetBurnable("CajExt3",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("CajExt4","Cajon2",6034.205035,-7852.244483,-109661.002963,"Physic")
o.Scale=1.000000
o.Orientation=0.690346,0.690346,0.153046,-0.153046
pan=Breakings.CreateHiddenObject("ques112", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("ques112")
Breakings.SetBreakable("CajExt4",12,100,"ques112")
Actions.SetBurnable("CajExt4",BoxBurnTime,BoxDestroyTime)


###5 BARRILES Y 3 CAJAS AL PRINCIPIO ZONA INTERIOR INICIO



o=Bladex.CreateEntity("BarrInt1","Barril",-9885.750719,-25135.239456,18014.056756,"Physic")
o.Scale=1.459527
o.Orientation=0.718412,-0.685815,0.079947,0.084564
pan=Breakings.CreateHiddenObject("ques113", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("ques113")
Breakings.SetBreakable("BarrInt1",12,100,"ques113")
Actions.SetBurnable("BarrInt1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrInt2","Barril",-9843.035307,-25366.678771,19120.900607,"Physic")
o.Scale=1.890462
o.Orientation=0.692618,0.718296,0.048360,-0.044627
Breakings.SetBreakable("BarrInt2",12,100)
Actions.SetBurnable("BarrInt2",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrInt3","Barril",-10636.653503,-25117.189714,18509.343552,"Physic")
o.Scale=1.321291
o.Orientation=0.675376,0.716148,-0.126195,0.122775
pan=Breakings.CreateHiddenObject("pan333", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pan333")
Breakings.SetBreakable("BarrInt3",12,100,"pan333")
Actions.SetBurnable("BarrInt3",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrInt4","Barril",-15571.976735,-25296.094526,21709.526365,"Physic")
o.Scale=1.580459
o.Orientation=0.690748,0.715436,0.075203,-0.073242
Breakings.SetBreakable("BarrInt4",12,100)
Actions.SetBurnable("BarrInt4",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrInt5","Barril",-17693.369829,-26113.430404,26194.673569,"Physic")
o.Scale=1.711410
o.Orientation=0.038300,0.537362,0.840956,0.050689
pan=Breakings.CreateHiddenObject("pan334", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pan334")
Breakings.SetBreakable("BarrInt5",12,100,"pan334")
Actions.SetBurnable("BarrInt5",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("CajInt1","Cajon2",-12434.109103,-26151.311740,27003.150405,"Physic")
o.Scale=1.000000
o.Orientation=0.692246,0.721566,0.011018,0.004076
Breakings.SetBreakable("CajInt1",12,100)
Actions.SetBurnable("CajInt1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajInt2","Cajon2",-12654.762299,-27146.357058,26990.340611,"Physic")
o.Scale=0.803396
o.Orientation=0.842060,0.019776,-0.538996,-0.005258
Breakings.SetBreakable("CajInt2",12,100)
Actions.SetBurnable("CajInt2",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("CajInt3","Cajon2",-12876.359967,-26001.615112,28370.466915,"Physic")
o.Scale=0.692005
o.Orientation=0.021351,-0.981346,-0.014843,0.190483
Breakings.SetBreakable("CajInt3",12,100)
Actions.SetBurnable("CajInt3",BoxBurnTime,BoxDestroyTime)


### 5 CAJAS OBSTRUYEN LA SALIDA A LA ZONA EXTERIOR PPAL


o=Bladex.CreateEntity("CajObst1","Cajon2",-27303.305374,-30597.313321,-6031.445584,"Physic")
o.Scale=1.000000
o.Orientation=0.500000,0.500000,-0.500000,0.500000
pan=Breakings.CreateHiddenObject("panobst1", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panobst1")
Breakings.SetBreakable("CajObst1",12,100,"panobst1")
Actions.SetBurnable("CajObst1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajObst2","Cajon2",-29313.624484,-30738.144127,-6953.909199,"Physic")
o.Scale=0.923483
o.Orientation=0.713305,0.700853,-0.000731,0.000731
pan=Breakings.CreateHiddenObject("panobst3", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panobst3")
Breakings.SetBreakable("CajObst2",12,100,"panobst3")
Actions.SetBurnable("CajObst2",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("CajObst4","Cajon2",-29359.166844,-31660.213364,-7052.565756,"Physic")
o.Scale=0.795442
o.Orientation=0.482517,-0.510624,0.512693,0.493545
Breakings.SetBreakable("CajObst4",12,100)
Actions.SetBurnable("CajObst4",BoxBurnTime,BoxDestroyTime)


##########RECORRIDO 1


###4 BARRILES Y 3 CAJAS OBSTRUYEN EL ACCESO AL ELEVADOR 

o=Bladex.CreateEntity("BarrElev1","Barril",-79931.087402,-26178.746189,-22339.575725,"Physic")
o.Scale=1.612226
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panBarrElev1", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panBarrElev1")
Breakings.SetBreakable("BarrElev1",12,100,"panBarrElev1")
Actions.SetBurnable("BarrElev1",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("CajElev1","Cajon2",-80081.659352,-26268.316800,-21125.033256,"Physic")
o.Scale=1.000000
o.Orientation=0.701502,0.704455,0.070341,0.081789
pan=Breakings.CreateHiddenObject("panCajElev1", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panCajElev1")
Breakings.SetBreakable("CajElev1",12,100,"panCajElev1")
Actions.SetBurnable("CajElev1",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("CajElev2","Cajon2",-79444.468456,-26625.428943,-19725.372179,"Physic")
o.Scale=1.000000
o.Orientation=0.599504,0.261282,-0.226621,0.721782
pan=Breakings.CreateHiddenObject("panCajElev2", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panCajElev2")
Breakings.SetBreakable("CajElev2",12,100,"panCajElev2")
Actions.SetBurnable("CajElev2",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("CajElev3","Cajon2",-79461.279616,-27432.237475,-21376.286287,"Physic")
o.Scale=1.000000
o.Orientation=0.368127,0.665391,-0.493308,0.422356
pan=Breakings.CreateHiddenObject("panCajElev3", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panCajElev3")
Breakings.SetBreakable("CajElev3",12,100)
Actions.SetBurnable("CajElev3",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrElev2","Barril",-78501.584949,-26386.689898,-22418.823448,"Physic")
o.Scale=2.130220
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrElev2",12,100)
Actions.SetBurnable("BarrElev2",BoxBurnTime,BoxDestroyTime)


###5 BARRILES TRAS ZONA ARAÑAS, JUNTO A CARRETILLA VOLCADA

o=Bladex.CreateEntity("BarrCarr1","Barril",-134975.150503,-10585.687843,6263.980910,"Physic")
o.Scale=1.388690
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("pancarr1", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pancarr1")
Breakings.SetBreakable("BarrCarr1",12,100,"pancarr1")
Actions.SetBurnable("BarrCarr1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrCarr2","Barril",-135579.588418,-10605.367089,5447.338129,"Physic")
o.Scale=1.445076
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("pancarr2", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pancarr2")
Breakings.SetBreakable("BarrCarr2",12,100,"pancarr2")
Actions.SetBurnable("BarrCarr2",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrCarr3","Barril",-140497.571475,-10320.477132,10015.937511,"Physic")
o.Scale=1.000000
o.Orientation=0.096016,-0.252719,0.962614,-0.016993
pan=Breakings.CreateHiddenObject("pancarr3", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pancarr3")
Breakings.SetBreakable("BarrCarr3",12,100,"pancarr3")
Actions.SetBurnable("BarrCarr3",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrCarr4","Barril",-135716.601258,-10569.233933,6457.619561,"Physic")
o.Scale=1.347849
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrCarr4",12,100)
Actions.SetBurnable("BarrCarr4",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrCarr5","Barril",-141467.369031,-10311.353055,9886.935012,"Physic")
o.Scale=1.000000
o.Orientation=0.339111,0.618208,-0.342611,-0.620838
Breakings.SetBreakable("BarrCarr5",12,100)
Actions.SetBurnable("BarrCarr5",BoxBurnTime,BoxDestroyTime)



### 8 CAJAS TRAS ENCONTRAR PRIMERA GEMA


o=Bladex.CreateEntity("CajGem0","Cajon2",-125911.349248,-13851.602058,54087.589274,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("pangem0", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pangem0")
Breakings.SetBreakable("CajGem0",12,100,"pangem0")
Actions.SetBurnable("CajGem0",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("CajGem1","Cajon2",-125717.184212,-14373.346701,52415.599215,"Physic")
o.Scale=1.295256
o.Orientation=0.686941,0.169623,0.170334,0.685804
pan=Breakings.CreateHiddenObject("pangem1", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pangem1")
Breakings.SetBreakable("CajGem1",12,100,"pangem1")
Actions.SetBurnable("CajGem1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajGem2","Cajon2",-121388.877305,-14097.990644,47093.242176,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("CajGem2",12,100)
Actions.SetBurnable("CajGem2",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajGem3","Cajon2",-120584.048785,-14125.954085,45122.730197,"Physic")
o.Scale=1.257163
o.Orientation=0.451609,0.557776,-0.435792,0.543158
Breakings.SetBreakable("CajGem3",12,100)
Actions.SetBurnable("CajGem3",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("CajGem4","Cajon2",-121258.409928,-14012.106400,38407.825298,"Physic")
o.Scale=0.852821
o.Orientation=0.638224,0.638224,-0.304417,0.304417
Breakings.SetBreakable("CajGem4",12,100)
Actions.SetBurnable("CajGem4",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("CajGem5","Cajon2",-121077.848611,-15051.072223,38589.815044,"Physic")
o.Scale=1.000000
o.Orientation=0.704416,0.704416,-0.061628,0.061628
pan=Breakings.CreateHiddenObject("pangem5", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pangem5")
Breakings.SetBreakable("CajGem5",12,100,"pangem5")
Actions.SetBurnable("CajGem5",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("CajGem6","Cajon2",-124235.140943,-14109.718796,31669.878191,"Physic")
o.Scale=1.196147
o.Orientation=0.647193,0.683993,0.190450,-0.277531
Breakings.SetBreakable("CajGem6",12,100)
Actions.SetBurnable("CajGem6",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajGem7","Cajon2",-122241.962788,-13893.821209,34736.740165,"Physic")
o.Scale=1.000000
o.Orientation=0.605184,-0.488267,0.491677,0.391920
Breakings.SetBreakable("CajGem7",12,100)
Actions.SetBurnable("CajGem7",BoxBurnTime,BoxDestroyTime)


##8 BARRILES Y 4 CAJAS EN FINAL DE RECORRIDO 1, JUNTO A ELEVADOR


o=Bladex.CreateEntity("BarrFin11","Barril",-91351.481248,-15102.341183,2402.163821,"Physic")
o.Scale=1.430769
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panfin11", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panfin11")
Breakings.SetBreakable("BarrFin11",12,100,"panfin11")
Actions.SetBurnable("BarrFin11",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrFin12","Barril",-91263.051493,-15110.286404,3420.523225,"Physic")
o.Scale=1.445076
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panfin12", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panfin12")
Breakings.SetBreakable("BarrFin12",12,100,"panfin12")
Actions.SetBurnable("BarrFin12",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BarrFin13","Barril",-91308.631898,-15166.467372,4607.908353,"Physic")
o.Scale=1.580459
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrFin13",12,100)
Actions.SetBurnable("BarrFin13",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("BarrFin14","Barril",-92363.827835,-15145.126445,2354.958251,"Physic")
o.Scale=1.533978
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrFin14",12,100)
Actions.SetBurnable("BarrFin14",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("BarrFin15","Barril",-92197.264553,-15018.414561,3524.483460,"Physic")
o.Scale=1.220190
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrFin15",12,100)
Actions.SetBurnable("BarrFin15",BoxBurnTime,BoxDestroyTime)
###

o=Bladex.CreateEntity("CajaFin11","Cajon2",-100237.110213,-16099.831249,9036.738226,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("CajaFin11",12,100)
Actions.SetBurnable("CajaFin11",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("CajaFin12","Cajon2",-100138.244251,-16095.619438,7440.882761,"Physic")
o.Scale=1.000000
o.Orientation=0.303317,0.303406,-0.639339,0.638114
Breakings.SetBreakable("CajaFin12",12,100)
Actions.SetBurnable("CajaFin12",BoxBurnTime,BoxDestroyTime)

####ESTAS
o=Bladex.CreateEntity("CajaFin13","Cajon2",-95864.653183,-15007.193430,15100.806877,"Physic")
o.Scale=0.844377
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panfin13", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panfin13")
Breakings.SetBreakable("CajaFin13",12,100,"panfin13")
Actions.SetBurnable("CajaFin13",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajaFin14","Cajon2",-96390.080790,-15863.578533,15292.970475,"Physic")
o.Scale=0.698925
o.Orientation=0.495618,0.495618,-0.504344,0.504344
Breakings.SetBreakable("CajaFin14",12,100)
Actions.SetBurnable("CajaFin14",BoxBurnTime,BoxDestroyTime)
###
o=Bladex.CreateEntity("BarrFin16","Barril",-104440.924562,-16042.518083,14090.300736,"Physic")
o.Scale=1.282432
o.Orientation=0.708180,0.705947,0.008128,-0.007318
Breakings.SetBreakable("BarrFin16",12,100)
Actions.SetBurnable("BarrFin16",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("BarrFin18","Barril",-105908.836646,-16166.904919,14714.218139,"Physic")
o.Scale=1.580459
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panfin18", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panfin18")
Breakings.SetBreakable("BarrFin18",12,100,"panfin18")
Actions.SetBurnable("BarrFin18",BoxBurnTime,BoxDestroyTime)







##########RECORRIDO 2
##########RECORRIDO 2

o=Bladex.CreateEntity("Barrtarari1","Barril",-75041.791614,-26081.150553,-62919.999870,"Physic")
o.Scale=1.374941
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("tarari1", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("tarari1")
Breakings.SetBreakable("Barrtarari1",12,100,"tarari1")
Actions.SetBurnable("Barrtarari1",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("Barrtarari2","Barril",-74376.519936,-26145.611540,-61952.196701,"Physic")
o.Scale=1.533978
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("tarari2", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("tarari2")
Breakings.SetBreakable("Barrtarari2",12,100,"tarari2")
Actions.SetBurnable("Barrtarari2",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("Barrtarari3","Barril",-74176.095721,-26036.695484,-63007.772777,"Physic")
o.Scale=1.269735
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("tarari3", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("tarari3")
Breakings.SetBreakable("Barrtarari3",12,100,"tarari3")
Actions.SetBurnable("Barrtarari3",BoxBurnTime,BoxDestroyTime)



##########RECORRIDO 3
##########RECORRIDO 3


### 7 BARRILES Y 7 CAJAS CERCA DE VIA MUERTA



o=Bladex.CreateEntity("BarrVia1","Barril",-19914.452041,-17140.545942,-154593.454485,"Physic")
o.Scale=1.518790
o.Orientation=0.477714,0.477714,-0.521334,0.521334
pan=Breakings.CreateHiddenObject("panvia1", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panvia1")
Breakings.SetBreakable("BarrVia1",12,100,"panvia1")
Actions.SetBurnable("BarrVia1",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("BarrVia2","Barril",-19173.856455,-17174.762188,-153877.215896,"Physic")
o.Scale=1.612226
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panvia2", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panvia2")
Breakings.SetBreakable("BarrVia2",12,100,"panvia2")
Actions.SetBurnable("BarrVia2",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrVia3","Barril",-12407.786975,-17077.475342,-155015.699214,"Physic")
o.Scale=1.374941
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrVia3",12,100)
Actions.SetBurnable("BarrVia3",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajVia1","Cajon2",-11482.822502,-17096.922436,-153950.141711,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("CajVia1",12,100)
Actions.SetBurnable("CajVia1",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("BarrVia4","Barril",-12621.963704,-17185.955698,-148804.539735,"Physic")
o.Scale=1.628348
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrVia4",12,100)
Actions.SetBurnable("BarrVia4",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrVia5","Barril",-13654.247316,-17090.561265,-149351.543605,"Physic")
o.Scale=1.402577
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrVia5",12,100)
Actions.SetBurnable("BarrVia5",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrVia6","Barril",-15941.409305,-16908.997062,-150372.623827,"Physic")
o.Scale=1.402577
o.Orientation=0.416557,0.559371,-0.378486,-0.608550
Breakings.SetBreakable("BarrVia6",12,100)
Actions.SetBurnable("BarrVia6",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajVia2","Cajon2",-18412.997355,-17102.336573,-159630.932202,"Physic")
o.Scale=1.000000
o.Orientation=0.690346,0.690346,0.153046,-0.153046
Breakings.SetBreakable("CajVia2",12,100)
Actions.SetBurnable("CajVia2",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajVia3","Cajon2",-18715.609437,-18085.279867,-159592.466616,"Physic")
o.Scale=0.772048
o.Orientation=0.627211,0.627211,-0.326506,0.326506
Breakings.SetBreakable("CajVia3",12,100)
Actions.SetBurnable("CajVia3",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajVia4","Cajon2",11213.031230,-17102.839458,-148977.061026,"Physic")
o.Scale=1.000000
o.Orientation=0.690346,0.690346,0.153046,-0.153046
Breakings.SetBreakable("CajVia4",12,100)
Actions.SetBurnable("CajVia4",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajVia5","Cajon2",11102.512740,-18128.301301,-148967.891080,"Physic")
o.Scale=0.844377
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("CajVia5",12,100)
Actions.SetBurnable("CajVia5",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajVia6","Cajon2",13249.615543,-17102.059713,-149870.374326,"Physic")
o.Scale=1.000000
o.Orientation=0.579228,0.579228,-0.405580,0.405580
Breakings.SetBreakable("CajVia6",12,100)
Actions.SetBurnable("CajVia6",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajVia7","Cajon2",20511.352806,-17098.308435,-156689.122103,"Physic")
o.Scale=1.000000
o.Orientation=0.241845,0.241845,-0.664463,0.664463
Breakings.SetBreakable("CajVia7",12,100)
Actions.SetBurnable("CajVia7",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BarrVia7","Barril",20465.480127,-17035.158649,-155178.694295,"Physic")
o.Scale=1.269735
o.Orientation=0.440147,0.440686,0.555168,-0.551230
Breakings.SetBreakable("BarrVia7",12,100)
Actions.SetBurnable("BarrVia7",BoxBurnTime,BoxDestroyTime)


### 12 BARRILES Y 8 CAJAS ANTES DE POZO DE LAS ARAÑAS GUARDANDO LA GEMA


o=Bladex.CreateEntity("BarrArac1","Barril",57023.462256,-5011.154764,-184272.020489,"Physic")
o.Scale=1.816697
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panarac1", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panarac1")
Breakings.SetBreakable("BarrArac1",12,100,"panarac1")
Actions.SetBurnable("BarrArac1",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("BarrArac2","Barril",56847.864078,-5007.799475,-185475.868488,"Physic")
o.Scale=1.798710
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panarac2", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panarac2")
Breakings.SetBreakable("BarrArac2",12,100,"panarac2")
Actions.SetBurnable("BarrArac2",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("BarrArac3","Barril",57271.205025,-4870.262902,-186602.306610,"Physic")
o.Scale=1.474123
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrArac3",12,100)
Actions.SetBurnable("BarrArac3",BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("BarrArac4","Barril",67395.612471,-4888.709071,-189623.887008,"Physic")
o.Scale=1.518790
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrArac4",12,100)
Actions.SetBurnable("BarrArac4",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("BarrArac5","Barril",52777.413453,-4544.738604,-196016.959268,"Physic")
o.Scale=1.816697
o.Orientation=0.634742,0.361450,0.532862,0.427217
Breakings.SetBreakable("BarrArac5",12,100)
Actions.SetBurnable("BarrArac5",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("BarrArac6","Barril",54455.813844,-4853.606198,-194355.407102,"Physic")
o.Scale=2.047099
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrArac6",12,100)
Actions.SetBurnable("BarrArac6",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrArac7","Barril",48071.744671,-4783.070882,-217488.147025,"Physic")
o.Scale=1.871744
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrArac7",12,100)
Actions.SetBurnable("BarrArac7",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("BarrArac8","Barril",45946.704128,-4788.133417,-217541.073816,"Physic")
o.Scale=1.871744
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrArac8",12,100)
Actions.SetBurnable("BarrArac8",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("BarrArac9","Barril",44360.335955,-4541.289664,-217383.233383,"Physic")
o.Scale=1.282432
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrArac9",12,100)
Actions.SetBurnable("BarrArac9",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("BarrArac10","Barril",46981.575648,-4639.143234,-216757.933983,"Physic")
o.Scale=1.518790
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrArac10",12,100)
Actions.SetBurnable("BarrArac10",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("BarrArac11","Barril",45303.611387,-4643.772904,-216432.509638,"Physic")
o.Scale=1.533978
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrArac11",12,100)
Actions.SetBurnable("BarrArac11",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("BarrArac12","Barril",46169.549404,-4441.977312,-215096.042385,"Physic")
o.Scale=1.549318
o.Orientation=0.135418,0.684360,0.130044,0.704557
Breakings.SetBreakable("BarrArac12",12,100)
Actions.SetBurnable("BarrArac12",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("CajArac1","Cajon2",68849.802461,-4967.220085,-188465.551320,"Physic")
o.Scale=1.196147
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("CajArac1",12,100)
Actions.SetBurnable("CajArac1",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("CajArac2","Cajon2",68167.148052,-6183.822901,-188191.422986,"Physic")
o.Scale=1.000000
o.Orientation=0.500000,0.500000,-0.500000,0.500000
Breakings.SetBreakable("CajArac2",12,100)
Actions.SetBurnable("CajArac2",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("CajArac3","Cajon2",55128.064079,-4598.067667,-192616.783970,"Physic")
o.Scale=1.000000
o.Orientation=0.664463,0.664463,0.241845,-0.241845
Breakings.SetBreakable("CajArac3",12,100)
Actions.SetBurnable("CajArac3",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("CajArac4","Cajon2",40888.020571,-4600.609089,-203750.426713,"Physic")
o.Scale=1.000000
o.Orientation=0.653282,0.653282,-0.270598,0.270598
Breakings.SetBreakable("CajArac4",12,100)
Actions.SetBurnable("CajArac4",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("CajArac5","Cajon2",39839.041732,-4878.013485,-205419.954890,"Physic")
o.Scale=1.000000
o.Orientation=0.505532,0.492444,0.487940,0.513665
Breakings.SetBreakable("CajArac5",12,100)
Actions.SetBurnable("CajArac5",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("CajArac6","Cajon2",40639.426595,-4817.076858,-208074.044981,"Physic")
o.Scale=1.374941
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("CajArac6",12,100)
Actions.SetBurnable("CajArac6",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajArac7","Cajon2",42849.622927,-5091.922533,-202877.167820,"Physic")
o.Scale=1.257163
o.Orientation=0.500000,0.500000,0.500000,0.500000
Breakings.SetBreakable("CajArac7",12,100)
Actions.SetBurnable("CajArac7",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("CajArac8","Cajon2",38496.605387,-5059.445956,-208037.433996,"Physic")
o.Scale=1.220190
o.Orientation=0.194199,0.679979,0.680257,0.192784
Breakings.SetBreakable("CajArac8",12,100)
Actions.SetBurnable("CajArac8",BoxBurnTime,BoxDestroyTime)


###ULTIMOS 5 CAJAS Y 6 BARRILES RECORRIDO 3



o=Bladex.CreateEntity("BarrFin1","Barril",35209.026323,-5233.943737,-205803.046241,"Physic")
o.Scale=1.745810
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrFin1",12,100)
Actions.SetBurnable("BarrFin1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrFin2","Barril",36430.057131,-5428.356291,-204823.310850,"Physic")
o.Scale=2.216715
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrFin2",12,100)
Actions.SetBurnable("BarrFin2",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrFin3","Barril",36746.354251,-5124.022638,-197214.844448,"Physic")
o.Scale=1.474123
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrFin3",12,100)
Actions.SetBurnable("BarrFin3",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("BarrFin4","Barril",37178.018949,-4929.113446,-197925.433302,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("BarrFin4",12,100)
Actions.SetBurnable("BarrFin4",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("BarrFin5","Barril",17971.740558,-5117.702165,-185186.109716,"Physic")
o.Scale=1.474123
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panfin142", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panfin142")
Breakings.SetBreakable("BarrFin5",12,100,"panfin142")
Actions.SetBurnable("BarrFin5",BoxBurnTime,BoxDestroyTime)




o=Bladex.CreateEntity("BarrFin6","Barril",18170.310484,-6204.359026,-184693.099456,"Physic")
o.Scale=1.269735
o.Orientation=0.800927,0.595212,0.053384,0.037270
pan=Breakings.CreateHiddenObject("panfin112", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panfin112")
Breakings.SetBreakable("BarrFin6",12,100,"panfin112")
Actions.SetBurnable("BarrFin6",BoxBurnTime,BoxDestroyTime)



o=Bladex.CreateEntity("CajFin1","Cajon2",10003.357767,-5098.094684,-192252.043292,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pan=Breakings.CreateHiddenObject("panfin122", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panfin122")
Breakings.SetBreakable("CajFin1",12,100,"panfin122")
Actions.SetBurnable("CajFin1",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajFin2","Cajon2",8569.091889,-5011.433364,-191780.802827,"Physic")
o.Scale=0.844377
o.Orientation=0.596368,0.596368,-0.379928,0.379928
pan=Breakings.CreateHiddenObject("panfin132", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panfin132")
Breakings.SetBreakable("CajFin2",12,100,"panfin132")
Actions.SetBurnable("CajFin2",BoxBurnTime,BoxDestroyTime)


o=Bladex.CreateEntity("CajFin4","Cajon2",35381.709462,-5177.545882,-195772.046054,"Physic")
o.Scale=1.138093
o.Orientation=0.666249,0.665389,0.238235,-0.237934
Breakings.SetBreakable("CajFin4",12,100)
Actions.SetBurnable("CajFin4",BoxBurnTime,BoxDestroyTime)


#### 97 ITEMS EN TOTAL

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