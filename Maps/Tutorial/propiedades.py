from math import pow
import EnemyTypes
import Actions
import Bladex
import pdb
import Reference
import Breakings
import AniSound
import math
import AuxFuncs
import Torchs
import pocimac
import ItemTypes
import Sparks
BoxBurnTime = 6
BoxDestroyTime = 12

###########
###########CHISPAS EN LOS PELELES
Sparks.SetSparkling("pele1")
Sparks.SetSparkling("pele2")

#
# Trampa para que se pueda encarar con el pelele
#
x,y,z = Bladex.GetEntity("pele1").Position
aranya = Bladex.CreateEntity("Tramposienta","Spidersmall",x+300,y,z-500,"Person")
aranya.Freeze()
aranya.Alpha       = 0
aranya.CastShadows = 0

###########
### ARMAS




o=Bladex.CreateEntity("Amz_Kgt_Dwf_Bar_W","Alabarda",434439.060032,4479.151023,56734.477671,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o.Scale=1.000000
o.Orientation=0.073215,0.116264,0.693050,0.707675
darfuncs.SetHint(o,"Designed for everybody")



o=Bladex.CreateEntity("Amz_W","Bo",434108.889258,4928.742051,57685.467192,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o.Scale=1.000000
o.Orientation=0.893528,-0.035539,0.441606,0.073004
darfuncs.SetHint(o,"Designed for Amazons")


o=Bladex.CreateEntity("Bar_W","Chaosword",434152.097906,5134.565700,58453.155555,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o.Scale=1.000000
o.Orientation=0.667921,-0.165278,0.699988,0.191263
darfuncs.SetHint(o,"Designed for Barbarians")



o=Bladex.CreateEntity("Dwf_Kgt_1","Escudo1",437992.862876,4527.723125,74048.457540,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("Dwf_Kgt_2","Escudo5",439533.562798,4575.089251,74100.693623,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("Dwf_Kgt_3","Escudo3",430162.957535,4537.562633,74072.649938,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("Dwf_w","Hacha",433983.225108,5491.313240,57937.257923,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o.Scale=1.000000
o.Orientation=0.222619,0.023567,-0.707585,-0.670231
darfuncs.SetHint(o,"Designed for Dwarfs")


o=Bladex.CreateEntity("None_Weapon","Martillo2",434733.016662,5506.074505,57756.453564,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o.Scale=1.000000
o.Orientation=0.681549,0.118299,0.711757,-0.122063
darfuncs.SetHint(o,"Advanced Weapon")

o=Bladex.CreateEntity("Kgt_w","Gladius",434000.481111,5492.061768,56905.505259,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o.Scale=1.000000
o.Orientation=0.479020,0.557272,-0.411620,0.539033
darfuncs.SetHint(o,"Designed for Knights")








Bladex.AddCombustionDataFor("Caja_i_r", "BigFire", 750, 950, 2, 2, 2, (BoxBurnTime+BoxDestroyTime)*2)
Bladex.AddCombustionDataFor("Cajon2", "LargeFire", 250, 400, 4, 1, 1, (BoxBurnTime+BoxDestroyTime)*2)
Bladex.AddCombustionDataFor("CajonPieza1", "LargeFire", 500,1100, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza2",  "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza3",  "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza4",  "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza5",  "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza6",  "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza7",  "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza8",  "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza9",  "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza10", "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza11", "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza12", "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza13", "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza14", "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza15", "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza16", "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza17", "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza18", "LargeFire", 500, 800, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("Barril", "LargeFire", 250, 400, 4, 1.5, 1, (BoxBurnTime+BoxDestroyTime)*3)
Bladex.AddCombustionDataFor("BarrilPieza1", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza2", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza3", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza4", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza5", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza6", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
######################antorchas de la sala secreta de la cripta

Torchs.SetUsable("a1",3,3,-1)
Torchs.SetUsable("a2",3,3,-1)
Torchs.SetUsable("a3",3,3,-1)






########en la pared

Torchs.SetUsable("ap1",3,3,-1)
Torchs.SetUsable("ap2",3,3,-1)





####cajas quemables

Actions.SetBurnable("cir1",BoxBurnTime,BoxDestroyTime)
darfuncs.SetHint(Bladex.GetEntity("cir1"),"Flammable")

####barriles de la entrada
Breakings.SetBreakable("barent1",12,100)
Actions.SetBurnable("barent1",BoxBurnTime,BoxDestroyTime)
darfuncs.SetHint(Bladex.GetEntity("barent1"),"Flammable and Breakable")

Breakings.SetBreakable("barent2",12,100)
Actions.SetBurnable("barent2",BoxBurnTime,BoxDestroyTime)
darfuncs.SetHint(Bladex.GetEntity("barent2"),"Flammable and Breakable")

Breakings.SetBreakable("barent3",12,100)
Actions.SetBurnable("barent3",BoxBurnTime,BoxDestroyTime)
darfuncs.SetHint(Bladex.GetEntity("barent3"),"Flammable and Breakable")

Breakings.SetBreakable("barent4",12,100)
Actions.SetBurnable("barent4",BoxBurnTime,BoxDestroyTime)
darfuncs.SetHint(Bladex.GetEntity("barent4"),"Flammable and Breakable")

Breakings.SetBreakable("barent5",12,100)
Actions.SetBurnable("barent5",BoxBurnTime,BoxDestroyTime)
darfuncs.SetHint(Bladex.GetEntity("barent5"),"Flammable and Breakable")

darfuncs.SetHint(Bladex.GetEntity("kaja1"),"Indestructible")
darfuncs.SetHint(Bladex.GetEntity("kaja2"),"Indestructible")
darfuncs.SetHint(Bladex.GetEntity("kaja3"),"Indestructible")

####barriles de la cocina
Breakings.SetBreakable("barcoc1",12,100)
Actions.SetBurnable("barcoc1",BoxBurnTime,BoxDestroyTime)

Breakings.SetBreakable("barcoc2",12,100)
Actions.SetBurnable("barcoc2",BoxBurnTime,BoxDestroyTime)

Breakings.SetBreakable("barcoc3",12,100)
Actions.SetBurnable("barcoc3",BoxBurnTime,BoxDestroyTime)

Breakings.SetBreakable("barcoc4",12,100)
Actions.SetBurnable("barcoc4",BoxBurnTime,BoxDestroyTime)

############# Barriles del final

Breakings.SetBreakable("barfin1",12,100)
Breakings.SetBreakable("barfin2",12,100)
Breakings.SetBreakable("barfin3",12,100)
Breakings.SetBreakable("barfin4",12,100)
Breakings.SetBreakable("barfin5",12,100)
Breakings.SetBreakable("barfin6",12,100)

Breakings.SetBreakable("barc1",12,100)
Breakings.SetBreakable("barc2",12,100)
Breakings.SetBreakable("barc3",12,100)

#############cofres
Breakings.SetBreakable("cofre1",12,100)
Breakings.SetBreakable("cofre2",12,100)

#############bancos
Breakings.SetBreakable("banco1",12,100)
Breakings.SetBreakable("banco4",12,100)
Breakings.SetBreakable("banco5",12,100)

#######comida

o=Bladex.CreateEntity("queso1","Queso",325244.142888,-6129.002726,118956.316419)
o.Static=0
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood("queso1")


o=Bladex.CreateEntity("pale1","Paletilla",325292.124417,-6128.124330,119313.660343)
o.Static=0
o.Scale=1.000000
o.Orientation=0.419381,0.715762,0.513915,-0.218391
pocimac.CreateFood("pale1")

o=Bladex.CreateEntity("manz1","Manzana",325095.364080,-6163.646666,120185.453511)
o.Static=0
o.Scale=1.361327
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood("manz1")


o=Bladex.CreateEntity("manz2","Manzana",325036.364726,-6206.395214,120308.552589)
o.Static=0
o.Scale=1.257163
o.Orientation=0.816491,-0.506960,0.243362,0.130800
pocimac.CreateFood("manz2")


o=Bladex.CreateEntity("manz3","Manzana",324941.244634,-6184.622552,120198.252095)
o.Static=0
o.Scale=1.416603
o.Orientation=0.342460,0.927151,-0.149883,0.025421
pocimac.CreateFood("manz3")


o=Bladex.CreateEntity("manz4","Manzana",325039.011740,-6241.251225,120073.818036)
o.Static=0
o.Scale=1.361327
o.Orientation=0.362519,0.573004,-0.283724,-0.678047
pocimac.CreateFood("manz4")


o=Bladex.CreateEntity("raba1","Rabano",325187.344196,-6263.951331,120351.339084)
o.Static=0
o.Scale=1.000000
o.Orientation=0.993637,0.038339,0.086382,-0.061276
pocimac.CreateFood("raba1")

#########pocimas

pocimac.CreatePotion("poc1")
pocimac.CreatePotion("poc2")





gar=Bladex.CreateEntity("gar1","Gargola",264075.318000,-18046.321000,134015.541000)
gar.Static=0
gar.Scale=6.623096
gar.Orientation=0.579228,0.579228,0.405580,-0.405580
gar.CastShadows=0

##########


pea=Bladex.CreateEntity("peana1","Peanapiedra",387360.542000,-16119.301000,56461.816000)
pea.Static=0
pea.Scale=7.689208
pea.Orientation=0.491198,0.491198,0.508650,-0.508650
pea.CastShadows=0

pea=Bladex.CreateEntity("peana2","Peanapiedra",384407.512000,-11242.968000,60352.518000)
pea.Static=0
pea.Scale=6.756220
pea.Orientation=0.080047,-0.104517,0.702561,-0.699340
pea.CastShadows=0

pea=Bladex.CreateEntity("peana3","Peanapiedra",399909.907000,-16223.758000,56904.019000)
pea.Static=0
pea.Scale=6.116318
pea.Orientation=0.537688,0.537688,0.459229,-0.459229
pea.CastShadows=0

pea=Bladex.CreateEntity("peana4","Peanapiedra",375377.435000,-16112.426000,56717.359000)
pea.Static=0
pea.Scale=8.409574
pea.Orientation=0.521334,0.521334,0.477714,-0.477714
pea.CastShadows=0

pea=Bladex.CreateEntity("NoName6","Adoquinpulsador",387288.319000,573.118000,57195.067000)
pea.Static=0
pea.Scale=1.661078
pea.Orientation=0.491198,0.491198,0.508650,-0.508650
pea.CastShadows=0

pea=Bladex.CreateEntity("NoName7","Adoquinpulsador",374930.479000,587.479000,52643.412000)
pea.Static=0
pea.Scale=1.580459
pea.Orientation=0.707107,0.707107,0.000000,0.000000
pea.CastShadows=0

pea=Bladex.CreateEntity("NoName8","Adoquinpulsador",374925.188000,551.082000,56903.390000)
pea.Static=0
pea.Scale=2.599273
pea.Orientation=0.495618,0.495618,0.504344,-0.504344
pea.CastShadows=0

pea=Bladex.CreateEntity("NoName9","Adoquinpulsador",374937.058000,-407.005000,57148.602000)
pea.Static=0
pea.Scale=1.184304
pea.Orientation=0.707107,0.707107,0.000000,0.000000
pea.CastShadows=0

pea=Bladex.CreateEntity("NoName10","Adoquinpulsador",384237.485000,-3552.370000,59775.837000)
pea.Static=0
pea.Scale=2.151522
pea.Orientation=0.491198,0.491198,0.508650,-0.508650
pea.CastShadows=0


pea=Bladex.CreateEntity("peana5","Peanapiedra",399254.836000,-15622.462000,46762.527000)
pea.Static=0
pea.Scale=6.892020
pea.Orientation=0.463904,0.463904,0.533660,-0.533660
pea.CastShadows=0

pea=Bladex.CreateEntity("peana6","Peanapiedra",387091.799000,-16504.055000,34085.334000)
pea.Static=0
pea.Scale=6.239256
pea.Orientation=0.504344,0.504344,-0.495618,0.495618
pea.CastShadows=0

pea=Bladex.CreateEntity("NoName2","Adoquinpulsador",384868.060000,-8458.083000,30549.089000)
pea.Static=0
pea.Scale=1.890462
pea.Orientation=0.293232,0.293232,-0.643440,-0.643440
pea.CastShadows=0

##########

import darfuncs
import ReadGSFile
# leer los sectores fantasma

res=ReadGSFile.ReadGhostSectorFile("quema.sf")
for igs in res:
   Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

# asignarles el fuego
darfuncs.FireOnGS("Hoguera")

char.SendTriggerSectorMsgs=1





