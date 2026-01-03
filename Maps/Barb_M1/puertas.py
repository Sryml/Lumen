import Doors
import Levers
import Locks
import Objects
import Sounds
import Sparks
import Sounds
import Button


"""
#abajo
#palancapuerta=PlaceLever("PalancaPuerta",LeverType2,(-59363.418000,-31570.327000,168183.110000),(0.608738,-0.005312,0.793323,0.006923),1.0)

#arriba
palancapuerta=PlaceLever("PalancaPuerta",LeverType2,(-72631.123609,-36199.342302,174304.409580),(0.000000,0.000000,0.707107,-0.707107),1.0)
palancapuerta.mode=0

losapuerta=CreateDoor("LosaPuerta", (-50750,-33000,166000), (0,1,0), 500, 4300, CLOSED)
losapuerta.opentype=AC_UNIF_DEC
losapuerta.o_init_vel=0
losapuerta.o_init_displ=250
losapuerta.o_med_vel=-1000
losapuerta.o_med_displ=2250
losapuerta.o_end_vel=0
losapuerta.o_end_displ=500

palancapuerta.OnTurnOnFunc=SubeLosaPuerta
palancapuerta.OnTurnOnArgs=()
"""

############################################################
############################################################
####-----PUERTA---GALERIA-SECRETA----------------------#####
############################################################
############################################################

ptadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
ptadesliz.MaxDistance=25000
ptadesliz.MinDistance=4000
ptadesliz.Volume=1.0


ptagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
ptagolpe.MaxDistance=25000
ptagolpe.MinDistance=4000
ptagolpe.Volume=1.0

puertar1=Doors.CreateDoor("Puertar1", (-50750,-33000,166000), (0,1,0), 500, 4300, Doors.CLOSED)


puertar1.opentype=Doors.UNIF
puertar1.o_med_vel=-800
puertar1.o_med_displ=3800


puertar1.closetype=Doors.AC
puertar1.c_init_displ=3800
puertar1.c_med_vel=8000


puertar1.SetWhileOpenSound(ptadesliz)
puertar1.SetEndOpenSound(ptagolpe)

puertar1.SetWhileCloseSound(ptadesliz)
puertar1.SetEndCloseSound(ptagolpe)

##### Accionar puertas al accionar una palanca


#palanr1=Levers.PlaceLever("PALAP1",Levers.LeverType2,(-59363.418000,-31570.327000,168183.110000),(0.430459,0.430459,0.560986,-0.560986),1.0)
palanr1=Levers.PlaceLever("PALAP1",Levers.LeverType2,(-72631.123609,-36199.342302,174304.409580),(0.000000,0.000000,0.707107,-0.707107),1.0)
palanr1.mode=2

palanr1.OnTurnOnFunc=AbrePuertar1
palanr1.OnTurnOnArgs=()

palanr1.OnTurnOffFunc=CierraPuertar1
palanr1.OnTurnOffArgs=()



############################################
####### PUERTA A LOS MONOLITOS   ###########
"""
piedradesliz=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "MaderaDesliz")
piedragolpe=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "MaderaGolpe")

ptatrampa=Doors.CreateDoor("ptatrampa", (125000,-55000,170500), (0,-1,0), 0, 5300, Doors.CLOSED)


ptatrampa.opentype=Doors.UNIF
ptatrampa.o_med_vel=-1000
ptatrampa.o_med_displ=5300


ptatrampa.closetype=Doors.AC
ptatrampa.c_init_displ=5300
ptatrampa.c_med_vel=5000


ptatrampa.SetWhileOpenSound(piedradesliz)
ptatrampa.SetEndOpenSound(piedragolpe)

ptatrampa.SetWhileCloseSound(piedradesliz)
ptatrampa.SetEndCloseSound(piedragolpe)


o=Bladex.CreateEntity("pedroloco2","Bloque",177106.956739,-50518.341847,167128.569178)
o.Static=0
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
darfuncs.SetHint(o,"Trigger")


button2=Button.CreateButtonCombination(0,Abrepta,"")
button2.AddButton("pedroloco2",3,(1,0,0),400,0,0,1)


####### PUERTA TRAMPA DE LAS TUMBAS   ###########


piedradesliz2=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "MaderaDesliz")
piedragolpe2=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "MaderaGolpe")

ptatrampa2=Doors.CreateDoor("ptatrampa2", (158750,-51000,159125), (0,1,0), 0, 3300, Doors.OPENED)


ptatrampa2.opentype=Doors.UNIF
ptatrampa2.o_med_vel=-1000
ptatrampa2.o_med_displ=3300


ptatrampa2.closetype=Doors.AC
ptatrampa2.c_init_displ=3300
ptatrampa2.c_med_vel=6000


ptatrampa2.SetWhileOpenSound(piedradesliz2)
ptatrampa2.SetEndOpenSound(piedragolpe2)

ptatrampa2.SetWhileCloseSound(piedradesliz2)
ptatrampa2.SetEndCloseSound(piedragolpe2)



####### PUERTA DEL PULSADOR   ###########


piedradesliz3=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "MaderaDesliz")
piedragolpe3=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "MaderaGolpe")

ptatrampa3=Doors.CreateDoor("ptatrampa2", (170625,-52000,167125), (0,1,0), 0, 4300, Doors.CLOSED)


ptatrampa3.opentype=Doors.UNIF
ptatrampa3.o_med_vel=-1000
ptatrampa3.o_med_displ=4300


ptatrampa3.closetype=Doors.AC
ptatrampa3.c_init_displ=4300
ptatrampa3.c_med_vel=6000


ptatrampa3.SetWhileOpenSound(piedradesliz2)
ptatrampa3.SetEndOpenSound(piedragolpe2)

ptatrampa3.SetWhileCloseSound(piedradesliz2)
ptatrampa3.SetEndCloseSound(piedragolpe2)

"""

########    PUERTAS SALA GRANDE



piedradesliz1=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "MaderaDesliz")
piedradesliz1.MaxDistance=20000
piedradesliz1.MinDistance=2000
piedradesliz1.Volume=1.0

piedragolpe1=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "MaderaGolpe")
piedragolpe1.MaxDistance=20000
piedragolpe1.MinDistance=2000
piedragolpe1.Volume=1.0

#1
puertasag1=Doors.CreateDoor("Puertasag1", (120750,-55000,176500), (0,-1,0), 0, 5300, Doors.OPENED)
puertasag1.Squezze = 1

puertasag1.opentype=Doors.UNIF
puertasag1.o_med_vel=-900
puertasag1.o_med_displ=5300

puertasag1.closetype=Doors.AC
puertasag1.c_init_displ=5300
puertasag1.c_med_vel=6000



puertasag1.SetWhileOpenSound(piedradesliz1)
puertasag1.SetEndOpenSound(piedragolpe1)

puertasag1.SetWhileCloseSound(piedradesliz1)
puertasag1.SetEndCloseSound(piedragolpe1)


#####

serB1=Bladex.GetSector(118500,-55000,180000)

serB1.OnEnter=CierraPuertasag


##############################################################
#####	PRIMERA PUERTA DE KASHGAR
##############################################################

ptapieD=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-deslizando-2.wav", "MaderaDesliz")
ptapieD.MaxDistance=20000
ptapieD.MinDistance=3000
ptapieD.Volume=1.0

ptapieG=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "MaderaGolpe")
ptapieG.MaxDistance=20000
ptapieG.MinDistance=3000
ptapieG.Volume=1.0

ptapie=Doors.CreateDoor("ptapie", (-85000,-14000,-50750), (0,1,0), 0, 5300, Doors.CLOSED)


ptapie.opentype=Doors.UNIF
ptapie.o_med_vel=-1000
ptapie.o_med_displ=5300


ptapie.closetype=Doors.AC
ptapie.c_init_displ=5300
ptapie.c_med_vel=5000


ptapie.SetWhileOpenSound(ptapieD)
ptapie.SetEndOpenSound(ptapieG)

ptapie.SetWhileCloseSound(ptapieD)
ptapie.SetEndCloseSound(ptapieG)



o=Bladex.CreateEntity("pedroloco3","Bloque",-84506.152786,-15273.861743,-54829.253154)
o.Scale=1.000000
o.Orientation=0.624338,0.624338,-0.331967,0.331967
darfuncs.SetHint(o,"Trigger")

button3=Button.CreateButtonCombination(0,Abreptapie,"")
button3.AddButton("pedroloco3",3,(2,0,3),200,0,0,1)


############################################################
####-----PUERTA---TORRETA ----------------------------#####
############################################################
############################################################

ptamaddesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
ptamaddesliz.MaxDistance=25000
ptamaddesliz.MinDistance=2000
ptamaddesliz.Volume=1.0


ptamadgolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
ptamadgolpe.MaxDistance=25000
ptamadgolpe.MinDistance=2000
ptamadgolpe.Volume=1.0

ptamad1=Doors.CreateDoor("ptamad1", (-60000,-15000,43625), (1,0,0), 500, 2250, Doors.CLOSED)


ptamad1.opentype=Doors.UNIF
ptamad1.o_med_vel=-800
ptamad1.o_med_displ=2250


ptamad1.closetype=Doors.AC
ptamad1.c_init_displ=2250
ptamad1.c_med_vel=8000


ptamad1.SetWhileOpenSound(ptamaddesliz)
ptamad1.SetEndOpenSound(ptamadgolpe)

ptamad1.SetWhileCloseSound(ptamaddesliz)
ptamad1.SetEndCloseSound(ptamadgolpe)

##### Abrir puerta al accionar una palanca

#palanm1=Levers.PlaceLever("PALAm1",Levers.LeverType2,(-57233.923540,-13512.075393,42982.886313),(0.006171,0.707080,0.006171,-0.707080),1.0)
palanm1=Levers.PlaceLever("PALAm1",Levers.LeverType2,(-57233.923540,-13512.075393,42982.886313),(0.707107,-0.000000,0.707107,0.000000),1.0)
palanm1.mode=2

palanm1.OnTurnOnFunc=Abreptamad1
palanm1.OnTurnOnArgs=()

palanm1.OnTurnOffFunc=Cierraptamad1
palanm1.OnTurnOffArgs=()


############################################################
####-----PUERTA--DE--LA--CASA-DEL--RIO-----------------#####
############################################################
############################################################

ptamaddesliz2=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
ptamaddesliz2.MaxDistance=25000
ptamaddesliz2.MinDistance=2000
ptamaddesliz2.Volume=1.0


ptamadgolpe2=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
ptamadgolpe2.MaxDistance=25000
ptamadgolpe2.MinDistance=2000
ptamadgolpe2.Volume=1.0

ptamad2=Doors.CreateDoor("ptamad2", (-188000,-13000,169000), (0,1,0), 500, 4000, Doors.CLOSED)


ptamad2.opentype=Doors.UNIF
ptamad2.o_med_vel=-800
ptamad2.o_med_displ=3500


ptamad2.closetype=Doors.AC
ptamad2.c_init_displ=3500
ptamad2.c_med_vel=8000


ptamad2.SetWhileOpenSound(ptamaddesliz)
ptamad2.SetEndOpenSound(ptamadgolpe)

ptamad2.SetWhileCloseSound(ptamaddesliz)
ptamad2.SetEndCloseSound(ptamadgolpe)

##### Abrir puerta al accionar una palanca

palanm2=Levers.PlaceLever("PALAm2",Levers.LeverType2,(-190001.287885,-11445.975594,171449.132513),(0.190802,0.001665,0.981590,-0.008566),1.0)
palanm2.mode=2

palanm2.OnTurnOnFunc=Abreptamad2
palanm2.OnTurnOnArgs=()

palanm2.OnTurnOffFunc=Cierraptamad2
palanm2.OnTurnOffArgs=()



############################################################
####-------PUERTA--DE--LA--CASA-DEL--TECHO-INCLINADO---#####
############################################################
############################################################

ptamaddesliz3=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
ptamaddesliz3.MaxDistance=25000
ptamaddesliz3.MinDistance=2000
ptamaddesliz3.Volume=1.0


ptamadgolpe3=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
ptamadgolpe3.MaxDistance=25000
ptamadgolpe3.MinDistance=2000
ptamadgolpe3.Volume=1.0

ptamad3=Doors.CreateDoor("ptamad3", (-120875,-25000,153375), (-1,0,1), 0, 2828.4, Doors.CLOSED)


ptamad3.opentype=Doors.UNIF
ptamad3.o_med_vel=-800
ptamad3.o_med_displ=2828.4


ptamad3.closetype=Doors.AC
ptamad3.c_init_displ=2828.4
ptamad3.c_med_vel=8000


ptamad3.SetWhileOpenSound(ptamaddesliz)
ptamad3.SetEndOpenSound(ptamadgolpe)

ptamad3.SetWhileCloseSound(ptamaddesliz)
ptamad3.SetEndCloseSound(ptamadgolpe)

##### Abrir puerta al accionar una palanca

palanm3=Levers.PlaceLever("PALAm3",Levers.LeverType2,(-119401.733865,-24577.127525,150619.118882),(.000000,0.382683,0.000000,-0.923880),1.0)
palanm3.mode=2

palanm3.OnTurnOnFunc=Abreptamad3
palanm3.OnTurnOnArgs=()

palanm3.OnTurnOffFunc=Cierraptamad3
palanm3.OnTurnOffArgs=()