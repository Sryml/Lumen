import Doors
import Objects
import Sounds
import Levers


############################################################
########ELEVADOR DE LA ZONA SECRETA

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puertar1=Doors.CreateDoor("Puertar1", (30750,0,6500), (0,-1,0), 0, 15000, Doors.CLOSED)
puertar1.Squezze = 0

puertar1.opentype=Doors.UNIF
puertar1.o_med_vel=-1800
puertar1.o_med_displ=15000

puertar1.closetype=Doors.UNIF
puertar1.c_med_vel=1800
puertar1.c_med_displ=15000




puertar1.SetWhileOpenSound(maderadesliz)
puertar1.SetEndOpenSound(maderagolpe)

puertar1.SetWhileCloseSound(maderadesliz)
puertar1.SetEndCloseSound(maderagolpe)

##### Accionar puertas al accionar una palanca


palanr1=Levers.PlaceLever("Palanr1",Levers.LeverType3,(28128.528128,-9203.505474,6462.543220),(0.500000,0.500000,-0.500000,0.500000),1.0)
palanr1.mode=1

palanr1.OnTurnOnFunc=AbrePuertar1
palanr1.OnTurnOnArgs=()
###########################
palanr2=Levers.PlaceLever("Palanr2",Levers.LeverType3,(28052.885259,5777.768855,6463.605856),(0.500000,0.500000,-0.500000,0.500000),1.0)
palanr2.mode=1

palanr2.OnTurnOffFunc=CierraPuertar1
palanr2.OnTurnOffArgs=()
