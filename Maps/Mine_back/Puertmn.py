import Doors
import Levers
import Locks
import Objects
import Sounds
import Button
import darfuncs
import Stars


#######################################################
########## PUERTA DE LA SALA DE LA TABLILLA ###########
#######################################################

#maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
#maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
maderadesliz=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "MaderaGolpe")

maderadesliz2=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz2")
maderagolpe2=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe2")

#escalon 1a
puerta1a=Doors.CreateDoor("Puerta1a", (93000,-20000,-164750), (0,1,0), 0, 4500, Doors.CLOSED)

puerta1a.opentype=Doors.UNIF
puerta1a.o_med_vel=-500
puerta1a.o_med_displ=4500

puerta1a.closetype=Doors.UNIF
puerta1a.c_med_vel=3900
puerta1a.c_med_displ=4500




o=Bladex.CreateEntity("bloque1","Bloque",94777.786102,-19044.803706,-162374.223081)
o.Static=0
o.Scale=1.000000
o.Orientation=0.500000,0.500000,0.500000,-0.500000

button=Button.CreateButtonCombination(0,Abrep1,"")
button.AddButton("bloque1",3,(0,0,1),400,0,0,1)



sc=Bladex.GetSector(86000,-20000,-164550)
sc.OnEnter=Cierrap1
