import Breakings
import Bladex


#######################################################
# 
#######################################################

# flame barriles
object_kind="Barril"
particle_type="LargeFire"
min_d=230.0
max_d=430.0
flame_h=4.0
flame_s=1.0
speed=1.5
time2live=1000000			# 10 Seconds

Bladex.AddCombustionDataFor(object_kind, particle_type, min_d, max_d, flame_h, flame_s, speed, time2live)


# flame MADEROS
object_kind="Astillas1"
particle_type="LargeFire"
min_d=780.0
max_d=830.0
flame_h=4.0
flame_s=1.0
speed=1.5
time2live=1000000			# 10 Seconds


Bladex.AddCombustionDataFor(object_kind, particle_type, min_d, max_d, flame_h, flame_s, speed, time2live)

# flame CAJAS
object_kind="Cajon2"
particle_type="LargeFire"
min_d=600.0
max_d=400.0
flame_h=4.0
flame_s=1.0
speed=1.5
time2live=1000000			# 10 Seconds


Bladex.AddCombustionDataFor(object_kind, particle_type, min_d, max_d, flame_h, flame_s, speed, time2live)

##################################################
#######-----HOGUERA-EN--EL--EXTERIOR----------------#######
##################################################

luz1=Bladex.CreateEntity("Luz2","Entity Spot",-22002.502064,139.566095,19997.919699)
luz1.Color=223,117,0
luz1.Intensity=10
luz1.Precission=0.1


Ho11=Bladex.CreateEntity("NoName1","Astillas2",-22186.821937,693.899645,21034.593225)
Ho11.Scale=1.000000
Ho11.Orientation=0.230136,0.205367,-0.658441,0.686525



Ho12=Bladex.CreateEntity("Ho12","Barril",-22527.324224,358.961850,19336.204336)
Ho12.Static=1
Ho12.Scale=2.238882
Ho12.Orientation=0.739505,0.373385,-0.106981,-0.549792
Ho12.CatchOnFire (0,0,0)
Ho12.CastShadows=0

Ho13=Bladex.CreateEntity("Ho13","Barril",-21630.575825,384.487915,20332.398554)
Ho13.Scale=1.474123
Ho13.Orientation=0.697833,0.497760,-0.419300,-0.299084
Ho13.CatchOnFire (0,0,0)
Ho13.CastShadows=0


Ho14=Bladex.CreateEntity("NoName4","Astillas1",-22685.946864,77.420842,21334.664248)
Ho14.Scale=1.000000
Ho14.Orientation=0.853023,0.497221,-0.122502,0.100581
Ho14.CastShadows=0
Ho14.CatchOnFire (0,0,0)

Ho15=Bladex.CreateEntity("NoName5","Tabla_rota",-20070.291724,958.169052,18830.845918)
Ho15.Static=1
Ho15.Scale=1.000000
Ho15.Orientation=0.005818,0.005536,-0.705174,0.708989



Ho16=Bladex.CreateEntity("NoName7","Hoguera",-21989.758678,799.089736,18329.270653)
Ho16.Scale=1.000000
Ho16.Orientation=0.707107,0.707107,0.000000,0.000000
Ho16.FiresIntensity=[ 7 ]
Ho16.Lights=[ (0.000000,0.031250,(255,196,128)) ]



Ho=Bladex.CreateEntity("NoName8","Hoguera",-22848.611676,824.094528,20906.855661)
Ho.Scale=1.184304
Ho.Orientation=0.707107,0.707107,0.000000,0.000000
Ho.FiresIntensity=[ 4 ]
Ho.Lights=[ (0.000000,0.031250,(255,196,128)) ]


Ho=Bladex.CreateEntity("NoName10","Tabla_xlpieza2",-21493.662366,912.325041,19757.444143)
Ho.Scale=1.295256
Ho.Orientation=0.024678,0.024678,0.706676,0.706676


Ho=Bladex.CreateEntity("NoName11","Astillas3",-17092.779391,752.275483,21784.259911)
Ho.Scale=1.000000
Ho.Orientation=0.707107,0.707107,0.000000,0.000000


#o=Bladex.CreateEntity("NoName12","Antorcha",-22002.502064,139.566095,19997.919699)
#o.Scale=1.000000
#o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.FiresIntensity=[ 43 ]
#o.Lights=[ (10.000000,0.100000,(223,117,0)) ]



#################################################
#######-----HOGUERA-EN--LA--PLATAFORMA----DERECHA------------------###
#################################################

luz2=Bladex.CreateEntity("Luz2","Entity Spot",12026.279589,191.550249,-20831.999111)
luz2.Color=223,117,0
luz2.Intensity=10
luz2.Precission=0.1

Ho21=Bladex.CreateEntity("Ho21","Barril",12546.578240,444.074308,-21117.532956)
Ho21.Scale=1.628348
Ho21.Orientation=0.971132,0.132817,-0.028770,0.196049
Ho21.CastShadows=0
Ho21.CatchOnFire (0,0,0)

o=Bladex.CreateEntity("NoName1","Hoguera",11779.736758,740.405041,-21200.556913)
o.Scale=1.374941
o.Orientation=0.703851,0.699340,0.104517,-0.067773
o.FiresIntensity=[ 6 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]



o=Bladex.CreateEntity("NoName2","Astillas2",11719.141837,537.879312,-20661.104191)
o.Scale=1.104622
o.Orientation=0.623949,0.717771,0.202733,-0.233218


o=Bladex.CreateEntity("NoName3","Hoguera",13154.327847,785.241290,-20992.975858)
o.Scale=1.082857
o.Orientation=0.627211,0.627211,0.326506,-0.326506
o.FiresIntensity=[ 6 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("NoName4","Tabla_xlpieza2",13649.919909,686.066156,-20630.234381)
o.Scale=1.282432
o.Orientation=0.771147,-0.505485,0.217352,0.320275


Ho22=Bladex.CreateEntity("Ho22","Barril",12246.103115,-47.524446,-20038.991996)
Ho22.Scale=1.711410
Ho22.Orientation=0.526247,0.465198,0.433804,0.564331
Ho22.CastShadows=0
Ho22.CatchOnFire (0,0,0)

o=Bladex.CreateEntity("NoName6","Tabla_xlpieza2",14180.770767,939.766945,-23684.350732)
o.Scale=1.416603
o.Orientation=0.691655,0.691655,-0.147016,0.147016


#o=Bladex.CreateEntity("NoName7","Antorcha",12026.279589,191.550249,-20831.999111)
#o.Scale=1.000000
#o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.FiresIntensity=[ 38 ]
#o.Lights=[ (10.000000,0.031250,(253,133,0)) ]


Ho23=Bladex.CreateEntity("Ho23","Astillas1",13357.053236,413.082439,-20557.524953)
Ho23.Scale=0.734577
Ho23.Orientation=0.480648,0.543273,-0.456118,0.515547
Ho22.CatchOnFire (0,0,0)

o=Bladex.CreateEntity("NoName9","Astillas1",10382.565113,929.953746,-22662.447688)
o.Scale=0.705914
o.Orientation=0.352183,-0.332619,0.605900,0.631044


#################################################
#######-----HOGUERA-DELANTE--DE--LA--TABLILLA--------------###
#################################################

luz3=Bladex.CreateEntity("Luz3","Entity Spot",109070.224533,2059.126660,5161.237354)
luz3.Color=223,117,0
luz3.Intensity=25
luz3.Precission=0.15

#o=Bladex.CreateEntity("NoName0","Antorcha",109070.224533,2059.126660,5161.237354)
#o.Scale=1.000000
#o.Orientation=0.707107,0.707107,0.000000,0.000000
#o.FiresIntensity=[ 38 ]
#o.Lights=[ (10.000000,0.100000,(236,124,0)) ]


Ho31=Bladex.CreateEntity("Ho31","Astillas1",109451.684492,2524.544140,5046.717988)
Ho31.Scale=0.632728
Ho31.Orientation=0.590506,0.601982,-0.384157,0.375955
Ho31.CastShadows=0
Ho31.CatchOnFire (0,0,0)

Ho32=Bladex.CreateEntity("Ho32","Astillas1",108504.205447,2405.944181,5294.572904)
Ho32.Scale=0.727304
Ho32.Orientation=0.451281,-0.606784,0.633430,0.164088
Ho32.CastShadows=0
Ho32.CatchOnFire (0,0,0)

o=Bladex.CreateEntity("NoName3","Astillas2",108876.581429,2353.425683,4887.252576)
o.Scale=0.658419
o.Orientation=0.359121,0.387104,-0.689214,0.496152
o.CastShadows=0

o=Bladex.CreateEntity("NoName4","Tabla_rota",109858.295858,2441.135427,5355.448788)
o.Scale=1.334504
o.Orientation=0.700225,0.700225,0.098410,0.098410


o=Bladex.CreateEntity("NoName5","Hoguera",109780.618193,2542.384725,5623.050093)
o.Scale=1.040604
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 9 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("NoName6","Hoguera",108956.448657,2500.543743,4554.789480)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 10 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("NoName7","Tabla_xlpieza2",106720.154921,2654.605568,4414.231700)
o.Scale=1.000000
o.Orientation=0.336443,0.331560,-0.624292,0.622201



o=Bladex.CreateEntity("NoName8","Tabla_xlpieza2",109725.370443,2656.658631,2729.890490)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



###############################################################33

import darfuncs
import ReadGSFile
# leer los sectores fantasma

res=ReadGSFile.ReadGhostSectorFile("fuego.sf")
for igs in res:
   Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

# asignarles el fuego
darfuncs.FireOnGS("fuego0")
darfuncs.FireOnGS("fuego1")
darfuncs.FireOnGS("fuego2")
darfuncs.FireOnGS("fuego3")
darfuncs.FireOnGS("fuego4")
darfuncs.FireOnGS("fuego5")




##############################################33
#####    BLOQUEO DERRUMBAMIENTO

o=Bladex.CreateEntity("pulga14","Bloque",49225.165615,4463.827759,48779.960497)
o.Scale=4.865175
o.Orientation=0.500000,0.500000,0.500000,0.500000
#o=Bladex.CreateEntity("pulga14","Adoquinpulsador",-223772.333500,-3912.320080,212445.188088)
#o.Scale=13.693716
#o.Orientation=0.298886,-0.654288,0.658982,-0.219811
o.Solid=1
o.Alpha = 0
o.CastShadows=0
