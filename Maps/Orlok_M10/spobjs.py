import Bladex
import Breakings
import Actions
import pocimac
import Sparks
import AuxFuncs
import ItemTypes
import Reference



###########################
#          armas          #
###########################

o=Bladex.CreateEntity("OrlokArmaduraMedEnano","ArmaduraEnanoMedia",3857.823376,-32747.894247,75920.897919, "Physic")
o.Scale=1.000000
o.Orientation=0.628734,0.623054,-0.331088,0.326923
o.Solid=0

o=Bladex.CreateEntity("OrlokIceHammer","IceHammer",31913.694874,-32406.006365,67735.981498, "Weapon")
o.Scale=1.000000
o.Orientation=0.891291,0.342145,-0.272388,-0.119754
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("OrlokIceSword","IceSword",6014.649732,-41309.743628,98672.566793, "Weapon")
o.Scale=1.000000
o.Orientation=0.509958,-0.607744,-0.466338,-0.391304
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("OrlokHacharrajada","Hacharrajada",-19677.120551,-33756.101731,89266.793433, "Weapon")
o.Scale=1.000000
o.Orientation=0.344970,0.777322,-0.345382,0.396835
ItemTypes.ItemDefaultFuncs(o)



#################################
#          comestibles          #
#################################

o=Bladex.CreateEntity("Orlok1Pocima200","Pocima200",-38860.768970,-45082.985900,-23564.502849, "Physic")
o.Solid=0
o.Scale=1.000000
o.Orientation=0.965642,-0.105300,0.236281,0.024861
pocimac.CreatePotion("Orlok1Pocima200")

o=Bladex.CreateEntity("Orlok3Pocima200","Pocima200",39896.201029,-40999.847191,65227.811527, "Physic")
o.Solid=0
o.Scale=1.184304
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreatePotion("Orlok3Pocima200")

o=Bladex.CreateEntity("OrlokPowerPotion","PowerPotion",-41295.357805,-41079.653781,80194.451614, "Physic")
o.Solid=0
o.Scale=1.000000
o.Orientation=0.055950,-0.995731,-0.052688,-0.051116
pocimac.CreatePowerPotion("OrlokPowerPotion")

o=Bladex.CreateEntity("QuesoFort","Queso",46650.0, -33286.6796875, 61250.0,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreateFood(o.Name)

o=Bladex.CreateEntity("PaletillaFort","Paletilla",46907.5134852, -33287.5349749, 61345.2556147,"Physic")
o.Scale=1.000000
o.Orientation=0.662496507168, 0.702073931694, 0.127271860838, 0.228018581867
pocimac.CreateFood(o.Name)

o=Bladex.CreateEntity("SaquitoInic","Saquito",-45720.0, -30187.109375, -53900.0,"Physic")
o.Scale=1.2
o.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreatePotion(o.Name)

o=Bladex.CreateEntity("Paletilla1Fin","Paletilla",51553.1033126, -32088.3663294, 146087.243918,"Physic")
o.Scale=1.2
o.Orientation=0.642938137054, 0.67936694622, 0.138279542327, 0.325530201197
pocimac.CreateFood(o.Name)

o=Bladex.CreateEntity("Paletilla2Fin","Paletilla",51882.3489676, -32092.390054, 146153.745887,"Physic")
o.Scale=1.2
o.Orientation=0.556301772594, -0.739841282368, 0.358233332634, 0.121787004173
pocimac.CreateFood(o.Name)



##########################
#        hogueras        #
##########################

o=Bladex.CreateEntity("Hoguera1","Hoguera",-23853.013000,-33243.675000,93468.152000)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (6.000000,0.031250,(255,180,96)) ]
AuxFuncs.SetRadialFireDamageObject(o.Name)

o=Bladex.CreateEntity("Hoguera2","Hoguera",-49631.775000,-30235.636000,-53618.576000)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (2.000000,0.031250,(255,180,96)) ]
AuxFuncs.SetRadialFireDamageObject(o.Name)

o=Bladex.CreateEntity("Hoguera3","Hoguera",48783.848000,-32244.430000,151083.825000)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 3 ]
o.Lights=[ (4.000000,0.031250,(255,180,96)) ]
AuxFuncs.SetRadialFireDamageObject(o.Name)



#############################
#     Objetos rompibles     #
#############################

BoxBurnTime = 6
BoxDestroyTime = 12

o=Bladex.CreateEntity("NoName28","Cajama",4612.580000,-33017.744000,60771.661000,"Physic")
o.Scale=1.208109
o.Orientation=0.500000,0.500000,-0.500000,0.500000
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName29","Cajama",5658.581000,-32974.647000,60837.105000,"Physic")
o.Scale=1.093685
o.Orientation=0.704893,0.709296,-0.004986,0.000046
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName30","Cajama",10399.036000,-33062.916000,60920.729000,"Physic")
o.Scale=1.321291
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName31","Cajama",5054.504000,-32939.100000,64113.375000,"Physic")
o.Scale=1.257163
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName32","Cajama",5032.076000,-33746.036000,64183.847000,"Physic")
o.Scale=1.072135
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName33","Cajama",3417.411000,-32935.039000,61521.473000,"Physic")
o.Scale=1.010000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName34","Cajama",10466.436000,-33904.479000,60839.744000,"Physic")
o.Scale=1.093685
o.Orientation=0.705493,0.708707,0.001154,-0.003437
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName35","Cajama",9323.344000,-33008.109000,60733.012000,"Physic")
o.Scale=1.184304
o.Orientation=0.500000,0.500000,-0.500000,0.500000
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName36","Cajama",5020.179000,-34488.770000,64267.739000,"Physic")
o.Scale=0.869963
o.Orientation=0.953717,0.000000,-0.300706,0.000000
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName37","Cajon",10592.427000,-32940.966000,62200.083000,"Physic")
o.Scale=0.734577
o.Orientation=0.500000,0.500000,-0.500000,0.500000
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName38","Cajon",6881.605000,-32995.450000,60723.627000,"Physic")
o.Scale=0.827740
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName41","Tinaja",10429.226000,-33270.129000,65523.482000,"Physic")
o.Scale=1.000000
o.Orientation=0.541675,0.541675,-0.454519,0.454519
Breakings.SetBreakable(o.Name,10,20)

o=Bladex.CreateEntity("NoName136","Barril",3325.105000,-33004.858000,68253.554000,"Physic")
o.Scale=1.184304
o.Orientation=0.690346,0.690346,-0.153046,0.153046
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName137","Barril",4053.935000,-33000.704000,68291.456000,"Physic")
o.Scale=1.172579
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName139","Armero",3676.863000,-33333.016000,73774.584000,"Physic")
o.Scale=1.000000
o.Orientation=0.500000,0.500000,-0.500000,0.500000
Breakings.SetBreakable(o.Name,10,20)


# Recompensa en cofre
o=Breakings.CreateHiddenObject("OrlokPocima50", "Pocima50",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
o.Solid=1
pocimac.CreatePotion("OrlokPocima50")


o=Bladex.CreateEntity("CofreConPocima50","Cofre",5594.771000,-33004.787000,77285.070000,"Physic")
o.Scale=0.905287
o.Orientation=0.500000,0.500000,0.500000,-0.500000
Breakings.SetBreakable(o.Name,10,20,"OrlokPocima50")

o=Bladex.CreateEntity("NoName154","Barril",46254.327000,-33025.078000,76224.518000,"Physic")
o.Scale=1.232392
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName155","Barril",46280.053000,-33019.852000,75437.069000,"Physic")
o.Scale=1.220190
o.Orientation=0.653282,0.653282,-0.270598,0.270598
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName159","Tinaja",45763.683000,-33275.847000,71302.991000,"Physic")
o.Scale=1.000000
o.Orientation=0.430459,0.430459,-0.560986,0.560986
Breakings.SetBreakable(o.Name,10,20)

o=Bladex.CreateEntity("NoName160","Tinaja",44831.588000,-33276.744000,71312.097000,"Physic")
o.Scale=1.000000
o.Orientation=0.379928,0.379928,-0.596368,0.596368
Breakings.SetBreakable(o.Name,10,20)

o=Bladex.CreateEntity("NoName166","Barril",45837.282000,-32897.185000,65719.689000,"Physic")
o.Scale=1.232392
o.Orientation=0.000000,0.714523,-0.699607,0.002734
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName167","Barril",45010.405000,-32825.561000,65676.466000,"Physic")
o.Scale=1.220190
o.Orientation=0.011440,0.978941,-0.195471,-0.057751
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName168","Barril",45355.867000,-33477.227000,65683.636000,"Physic")
o.Scale=1.232392
o.Orientation=0.012236,-0.977846,-0.208105,0.018952
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName169","Cajama",46776.372000,-32930.443000,61520.721000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName170","Cajama",45618.162000,-33038.663000,60758.462000,"Physic")
o.Scale=1.244716
o.Orientation=0.500000,0.500000,-0.500000,0.500000
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName171","Cajama",45605.297000,-33812.488000,60812.401000,"Physic")
o.Scale=0.980296
o.Orientation=0.373831,0.381740,-0.599438,0.595986
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName172","Cajon2",39733.339000,-33021.070000,60733.925000,"Physic")
o.Scale=0.861349
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName177","Tinaja",39520.435000,-33271.908000,61721.672000,"Physic")
o.Scale=1.000000
o.Orientation=0.236530,0.238103,-0.665625,0.666561
Breakings.SetBreakable(o.Name,10,20)

o=Bladex.CreateEntity("NoName178","Tinaja",39502.348000,-33276.029000,62629.980000,"Physic")
o.Scale=1.000000
o.Orientation=0.212631,0.212631,-0.674380,0.674380
Breakings.SetBreakable(o.Name,10,20)

o=Bladex.CreateEntity("NoName180","Cofre",42672.642000,-41795.193000,76304.472000,"Physic")
o.Scale=0.980296
o.Orientation=0.000000,0.000000,0.707107,-0.707107
Breakings.SetBreakable(o.Name,10,20)

o=Bladex.CreateEntity("NoName188","Armero",7026.715000,-41590.382000,60662.152000,"Physic")
o.Scale=1.000000
o.Orientation=0.005748,0.005730,-0.703413,0.710735
Breakings.SetBreakable(o.Name,10,20)

o=Bladex.CreateEntity("NoName192","Meson",42939.793000,-41307.694000,61123.091000,"Physic")
o.Scale=0.896324
o.Orientation=0.500000,0.500000,-0.500000,0.500000
Breakings.SetBreakable(o.Name,10,20)

o=Bladex.CreateEntity("NoName219","Barril",-44791.175000,-30430.852000,-52052.278000,"Physic")
o.Scale=1.000000
o.Orientation=0.706219,0.704636,-0.050560,0.046757
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName220","Barril",-45036.587000,-30315.219000,-51438.327000,"Physic")
o.Scale=1.000000
o.Orientation=0.474778,0.516323,0.438321,0.562024
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName223","Cajama",-53868.418000,-30435.858000,-55379.708000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName224","Cajama",-53748.281000,-31072.603000,-55293.948000,"Physic")
o.Scale=0.827740
o.Orientation=0.696364,0.696364,-0.122788,0.122788
Breakings.SetBreakable(o.Name,10,20)
Actions.SetBurnable(o.Name,BoxBurnTime,BoxDestroyTime)

o=Bladex.CreateEntity("NoName227","Cofre",-46267.846000,-30457.007000,-54752.067000,"Physic")
o.Scale=0.827740
o.Orientation=0.122788,0.122788,-0.696364,0.696364
Breakings.SetBreakable(o.Name,10,20)



###############################
#     Objetos chispeantes     #
###############################

o=Bladex.CreateEntity("Baranda1","Varillaancha",25000.000000,-42250.000000,65000.000000)
o.Scale=1.871744
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name)

o=Bladex.CreateEntity("Baranda2","Varillaancha",25000.000000,-42250.000000,73000.000000)
o.Scale=1.871744
o.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling(o.Name)



##############################
#     Objetos invisibles     #
##############################


o=Bladex.CreateEntity("Inv1","Bloque",-65775.712850,-32396.304254,-77286.732693)
o.Scale=8.081435
o.Orientation=0.162670,0.688141,0.688141,0.162670
o.CastShadows=0
o.Alpha = 0
o.ExclusionMask=4
Reference.EntitiesSelectionData[o.Name]=(0,0,"")

o=Bladex.CreateEntity("Inv2","PasarelaCorta",33250.000000,-40540.000000,72570.000000) # -43450
o.Scale=1.474123
o.Orientation=0.000000,0.707107,-0.707107,0.000000
o.CastShadows=0
o.Alpha = 0
o.ExclusionMask=2|4

o=Bladex.CreateEntity("Inv3","PasarelaCorta",33200.000000,-40540.000000,65430.409000)
o.Scale=1.474123
o.Orientation=0.707107,-0.000000,0.000000,-0.707107
o.CastShadows=0
o.Alpha = 0
o.ExclusionMask=2|4

o=Bladex.CreateEntity("Inv4","PasarelaCorta",16800.000000,-40540.000000,65417.414000)
o.Scale=1.474123
o.Orientation=0.707107,0.000000,0.000000,-0.707107
o.CastShadows=0
o.Alpha = 0
o.ExclusionMask=2|4

o=Bladex.CreateEntity("Inv5","PasarelaCorta",16800.000000,-40540.000000,72584.912000)
o.Scale=1.474123
o.Orientation=0.000000,0.707107,0.707107,0.000000
o.CastShadows=0
o.Alpha = 0
o.ExclusionMask=2|4

o=Bladex.CreateEntity("InvBaranda1","PasarelaCorta",25000.000000,-42750.000000,65300.000000)
o.Scale=1.000000
o.Orientation=0.000000,0.707107,-0.707107,0.000000
o.CastShadows=0
o.Alpha = 0
o.ExclusionMask=2|4

o=Bladex.CreateEntity("InvBaranda2","PasarelaCorta",25000.000000,-42750.000000,72700.000000)
o.Scale=1.000000
o.Orientation=0.707107,0.000000,-0.000000,0.707107
o.CastShadows=0
o.Alpha = 0
o.ExclusionMask=2|4
