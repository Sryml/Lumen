import Breakings
import Actions
BoxBurnTime = 6
BoxDestroyTime = 12
import Torchs
import pocimac


####################################################
####-1ª--SALA-CON-VIDRIERA-EN-MURALLA---------######
####################################################

#1

poc=Breakings.CreateHiddenObject("popo1", "Pocima50",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
poc.Solid=1
pocimac.CreatePotion("popo1")

o=Bladex.CreateEntity("CAJA11","Cajon2",-26961.470165,-5195.470624,78547.893326,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable("CAJA11",12,30,"popo1")
Actions.SetBurnable("CAJA11",BoxBurnTime,BoxDestroyTime)

#2
o=Bladex.CreateEntity("CAJA12","Cajon2",-26101.323726,-5480.158171,80059.198376,"Physic")
o.Scale=1.000000
o.Orientation=0.527758,0.473931,0.479821,0.516365

Breakings.SetBreakable("CAJA12",12,30)
Actions.SetBurnable("CAJA12",BoxBurnTime,BoxDestroyTime)

#3
o=Bladex.CreateEntity("CAJA13","Cajon2",-27623.674788,-6283.875057,78842.990538,"Physic")
o.Scale=0.923483
o.Orientation=0.710187,0.699482,0.015079,-0.078306

Breakings.SetBreakable("CAJA13",12,30)
Actions.SetBurnable("CAJA13",BoxBurnTime,BoxDestroyTime)


#4
o=Bladex.CreateEntity("CAJA14","Cajon2",-24475.674659,-5118.976426,80467.366447,"Physic")
o.Scale=0.861349
o.Orientation=0.707107,0.707107,0.000000,0.000000

Actions.SetBurnable("CAJA14",BoxBurnTime,BoxDestroyTime)
pan=Breakings.CreateHiddenObject("panC14", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panC14")
Breakings.SetBreakable("CAJA14",12,30,"panC14")


#5
o=Bladex.CreateEntity("BARRIL15","Barril",-20483.279639,-5243.170262,78502.674472,"Physic")
o.Scale=1.533978
o.Orientation=0.707107,0.707107,0.000000,0.000000

Breakings.SetBreakable("BARRIL15",12,30)
Actions.SetBurnable("BARRIL15",BoxBurnTime,BoxDestroyTime)


#6
o=Bladex.CreateEntity("BARRIL16","Barril",-20362.679004,-5258.113548,77164.445880,"Physic")
o.Scale=1.564811
o.Orientation=0.707107,0.707107,0.000000,0.000000

Breakings.SetBreakable("BARRIL16",12,30)
Actions.SetBurnable("BARRIL16",BoxBurnTime,BoxDestroyTime)


#7
pan=Breakings.CreateHiddenObject("QUESOso", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pocimac.CreateFood("QUESOso")

o=Bladex.CreateEntity("BARRIL17","Barril",-21310.656941,-5018.345883,77833.834181,"Physic")
o.Scale=1.308209
o.Orientation=0.238065,0.677716,0.649910,0.248280

Breakings.SetBreakable("BARRIL17",12,30,"QUESOso")
Actions.SetBurnable("BARRIL17",BoxBurnTime,BoxDestroyTime)

####################################################
####---------2ª--SALA-BAJO-LA-MURALLA---------######
####################################################

#1
o=Bladex.CreateEntity("CAJON21","Cajon2",-75797.454765,-601.101199,39609.865654,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000

Breakings.SetBreakable("CAJON21",12,30)
Actions.SetBurnable("CAJON21",BoxBurnTime,BoxDestroyTime)

#2
o=Bladex.CreateEntity("CAJON22","Cajon2",-76292.393687,-872.201970,41263.926037,"Physic")
o.Scale=1.000000
o.Orientation=0.500000,0.500000,0.500000,0.500000


Actions.SetBurnable("CAJON22",BoxBurnTime,BoxDestroyTime)
pan=Breakings.CreateHiddenObject("panC22", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panC22")
Breakings.SetBreakable("CAJON22",12,30,"panC22")

#3
o=Bladex.CreateEntity("CAJON23","Cajon2",-76274.014742,-831.870695,42947.571401,"Physic")
o.Scale=1.000000
o.Orientation=0.452256,0.600241,-0.526589,0.397341

Breakings.SetBreakable("CAJON23",12,30)
Actions.SetBurnable("CAJON23",BoxBurnTime,BoxDestroyTime)

#4
o=Bladex.CreateEntity("BARRIL24","Barril",-76464.549334,-1659.309935,40288.483296,"Physic")
o.Scale=1.308209
o.Orientation=0.774840,0.629127,-0.028253,-0.054994

Breakings.SetBreakable("BARRIL24",12,30)
Actions.SetBurnable("BARRIL24",BoxBurnTime,BoxDestroyTime)

#5
o=Bladex.CreateEntity("BARRIL25","Barril",-75320.475464,-423.930399,40955.762631,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000

Breakings.SetBreakable("BARRIL25",12,30)
Actions.SetBurnable("BARRIL25",BoxBurnTime,BoxDestroyTime)


#### eskeletos


Breakings.SetBreakable("skeleto1",12,30)



###bloqueo

o=Bladex.CreateEntity("NoName0","Bloque",-25096.904422,-11764.848923,66515.117929)
o.Scale=6.364665
o.Orientation=0.517145,0.517145,-0.482246,0.482246
o.Solid=1
o.Alpha = 0
o.CastShadows=0
Reference.EntitiesSelectionData[o.Name]=(0,0,"")