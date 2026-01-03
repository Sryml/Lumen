import Breakings
import Actions
BoxBurnTime = 6
BoxDestroyTime = 12
import pocimac


Breakings.SetBreakable("mesa1",8,12)
Breakings.SetBreakable("mesa2",8,12)
Breakings.SetBreakable("mesa3",8,12)
Breakings.SetBreakable("mesa4",8,12)
Breakings.SetBreakable("mesa5",8,12)

#Breakings.SetBreakable("meson1",8,12)
#Breakings.SetBreakable("meson2",8,12)

#Breakings.SetBreakable("armero1",8,12)


#Breakings.SetBreakable("cofre1",8,12)

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
Breakings.SetBreakable("cajon6",8,12)
Actions.SetBurnable("cajon6",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("cajon7",8,12)
Actions.SetBurnable("cajon7",BoxBurnTime,BoxDestroyTime)
#
pan=Breakings.CreateHiddenObject("QUESO", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("QUESO")
Breakings.SetBreakable("cajon8",8,12,"QUESO")
Actions.SetBurnable("cajon8",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("cajon9",8,12)
Actions.SetBurnable("cajon9",BoxBurnTime,BoxDestroyTime)
#



Breakings.SetBreakable("silla1",8,12)
Breakings.SetBreakable("silla2",8,12)
Breakings.SetBreakable("silla3",8,12)
Breakings.SetBreakable("silla4",8,12)
Breakings.SetBreakable("silla5",8,12)
Breakings.SetBreakable("silla6",8,12)
Breakings.SetBreakable("silla7",8,12)
Breakings.SetBreakable("silla8",8,12)
Breakings.SetBreakable("silla9",8,12)
Breakings.SetBreakable("silla10",8,12)
Breakings.SetBreakable("silla11",8,12)
Breakings.SetBreakable("silla12",8,12)
Breakings.SetBreakable("silla13",8,12)


Breakings.SetBreakable("barril1",8,12)
Actions.SetBurnable("barril1",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("barril2",8,12)
Actions.SetBurnable("barril2",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("barril3",8,12)
Actions.SetBurnable("barril3",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("barril4",8,12)
Actions.SetBurnable("barril4",BoxBurnTime,BoxDestroyTime)
#
pan=Breakings.CreateHiddenObject("CARNE", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreateFood("CARNE")
Breakings.SetBreakable("barril5",8,12,"CARNE")
Actions.SetBurnable("barril5",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("barril6",8,12)
Actions.SetBurnable("barril6",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("cajah1",8,12)
Actions.SetBurnable("cajah1",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("cajah2",8,12)
Actions.SetBurnable("cajah2",BoxBurnTime,BoxDestroyTime)
#
#
Actions.SetBurnable("cajai1",BoxBurnTime,BoxDestroyTime)






Breakings.SetBreakable("tinaja1",8,12)
Breakings.SetBreakable("tinaja2",8,12)

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
