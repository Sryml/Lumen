import Breakings
import Actions
BoxBurnTime = 6
BoxDestroyTime = 12
import Torchs
import pocimac



############################################
#          #     #               #         #
#                      #                   #
############################################

#Breakings.SetBreakable("tmesa1",8,12)
Breakings.SetBreakable("skeleto1",8,12)
Breakings.SetBreakable("skeleto2",8,12)
Breakings.SetBreakable("skeleto3",8,12)
Breakings.SetBreakable("skeleto4",8,12)
Breakings.SetBreakable("skeleto5",8,12)


Breakings.SetBreakable("armero1",8,12)
Breakings.SetBreakable("armero2",8,12)

#Breakings.SetBreakable("cofre1",8,12)

Breakings.SetBreakable("CAJAH1",8,12)
Breakings.SetBreakable("CAJAH2",8,12)



Breakings.SetBreakable("cajon1",8,12)
Actions.SetBurnable("cajon1",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("cajon2",8,12)
Actions.SetBurnable("cajon2",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("cajon3",8,12)
Actions.SetBurnable("cajon3",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("cajon4",8,12)
Actions.SetBurnable("cajon4",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("cajon5",8,12)
Actions.SetBurnable("cajon5",BoxBurnTime,BoxDestroyTime)
#
Actions.SetBurnable("cajon6",BoxBurnTime,BoxDestroyTime)
pan=Breakings.CreateHiddenObject("panc6", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panc6")
Breakings.SetBreakable("cajon6",8,12,"panc6")
#
Breakings.SetBreakable("cajon7",8,12)
Actions.SetBurnable("cajon7",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("cajon8",8,12)
Actions.SetBurnable("cajon8",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("cajon9",8,12)
Actions.SetBurnable("cajon9",BoxBurnTime,BoxDestroyTime)
#
Actions.SetBurnable("cajon10",BoxBurnTime,BoxDestroyTime)
pan=Breakings.CreateHiddenObject("panc10", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panc10")
Breakings.SetBreakable("cajon10",8,12,"panc10")
#
Breakings.SetBreakable("cajon11",8,12)
Actions.SetBurnable("cajon11",BoxBurnTime,BoxDestroyTime)
#
Actions.SetBurnable("cajon12",BoxBurnTime,BoxDestroyTime)
pan=Breakings.CreateHiddenObject("panc12", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panc12")
Breakings.SetBreakable("cajon12",8,12,"panc12")
#
Breakings.SetBreakable("cajon13",8,12)
Actions.SetBurnable("cajon13",BoxBurnTime,BoxDestroyTime)
#
Actions.SetBurnable("cajon14",BoxBurnTime,BoxDestroyTime)
pan=Breakings.CreateHiddenObject("panc14", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panc14")
Breakings.SetBreakable("cajon14",8,12,"panc14")
#
Breakings.SetBreakable("cajon15",8,12)
Actions.SetBurnable("cajon15",BoxBurnTime,BoxDestroyTime)



Breakings.SetBreakable("barril1",8,12)
Actions.SetBurnable("barril1",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("barril2",8,12)
Actions.SetBurnable("barril2",BoxBurnTime,BoxDestroyTime)
#
Actions.SetBurnable("barril3",BoxBurnTime,BoxDestroyTime)
pan=Breakings.CreateHiddenObject("panb3", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("panb3")
Breakings.SetBreakable("barril3",8,12,"panb3")
#
Breakings.SetBreakable("barril4",8,12)
Actions.SetBurnable("barril4",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("barril5",8,12)
Actions.SetBurnable("barril5",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("barril6",8,12)
Actions.SetBurnable("barril6",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("barril7",8,12)
Actions.SetBurnable("barril7",BoxBurnTime,BoxDestroyTime)



Breakings.SetBreakable("tinaja1",8,12)
#
Breakings.SetBreakable("tinaja2",8,12)
#
pan=Breakings.CreateHiddenObject("pant3", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("pant3")
Breakings.SetBreakable("tinaja3",8,12,"pant3")


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
