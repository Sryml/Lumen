import Doors
import Levers
import Locks
import Objects
import Sounds
import Button
import darfuncs





#########
#########


###trampa cripta

###tramo A. La escalera baja

#maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
#maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


#escalon 1a
puerta1a=Doors.CreateDoor("Puerta1a", (-32671,0,-8170), (1,0,0), 0, 2250, Doors.CLOSED)

puerta1a.opentype=Doors.UNIF
puerta1a.o_med_vel=-500
puerta1a.o_med_displ=2250

puerta1a.closetype=Doors.UNIF
puerta1a.c_med_vel=900
puerta1a.c_med_displ=2250


#escalon 2a
puerta2a=Doors.CreateDoor("Puerta2a", (-15671,0,-8170), (1,0,0), 0, 2250, Doors.CLOSED)

puerta2a.opentype=Doors.UNIF
puerta2a.o_med_vel=-500
puerta2a.o_med_displ=2250

puerta2a.closetype=Doors.UNIF
puerta2a.c_med_vel=800
puerta2a.c_med_displ=2250


blopagua1=Bladex.CreateEntity("bloque1","Bloque",-18175.232732,178.216445,-9827.716734,"Physic")
blopagua1.Scale=1.000000
blopagua1.Orientation=0.500000,0.500000,0.500000,-0.500000
darfuncs.SetHint(blopagua1,"Trigger")

blopagua2=Bladex.CreateEntity("bloque2","Bloque",-30415.844325,178.838128,-9764.368176,"Physic")
blopagua2.Scale=1.000000
blopagua2.Orientation=0.500000,0.500000,0.500000,-0.500000
darfuncs.SetHint(blopagua2,"Trigger")

button=Button.CreateButtonCombination(0,Abrep1,"")
button.AddButton("bloque1",3,(0,0,1),400,0,0,1)
button.AddButton("bloque2",3,(0,0,1),400,0,0,1)

blopagua1.Frozen=1
blopagua2.Frozen=1


############
############################
############Subida al puente#######
#################
#######################

#escalon 1a
puertasub1=Doors.CreateDoor("Puertasub1", (13750,0,221500), (0,-1,0), 0, 4750, Doors.CLOSED)

puertasub1.opentype=Doors.UNIF
puertasub1.o_med_vel=-500
puertasub1.o_med_displ=2750

puertasub1.closetype=Doors.UNIF
puertasub1.c_med_vel=900
puertasub1.c_med_displ=2750


#escalon 2a
puertasub2=Doors.CreateDoor("Puertasub2", (13750,0,211250), (0,-1,0), 0, 4750, Doors.CLOSED)

puertasub2.opentype=Doors.UNIF
puertasub2.o_med_vel=-500
puertasub2.o_med_displ=2750

puertasub2.closetype=Doors.UNIF
puertasub2.c_med_vel=800
puertasub2.c_med_displ=2750


blosu1=Bladex.CreateEntity("blosu1","Bloque",6742.043000,10733.373000,207865.494000,"Physic")
blosu1.Scale=1.000000
blosu1.Orientation=0.504344,0.504344,0.495618,-0.495618
darfuncs.SetHint(blosu1,"Trigger")

blosu2=Bladex.CreateEntity("blosu2","Bloque",6737.787000,10739.837000,226757.226000,"Physic")
blosu2.Scale=1.000000
blosu2.Orientation=0.500000,0.500000,0.500000,-0.500000
darfuncs.SetHint(blosu2,"Trigger")

button=Button.CreateButtonCombination(0,Abresub,"")
button.AddButton("blosu1",2,(0,0,-1),400,0,0,1)
button.AddButton("blosu2",2,(0,0,1),400,0,0,1)

blosu1.Frozen=1
blosu2.Frozen=1


#################
#######################

#escalon 1a
puerta4=Doors.CreateDoor("Puerta4", (16750,5000,180500), (1,0,0), 0, 5500, Doors.OPENED)

puerta4.opentype=Doors.UNIF
puerta4.o_med_vel=-500
puerta4.o_med_displ=5500

puerta4.closetype=Doors.UNIF
puerta4.c_med_vel=900
puerta4.c_med_displ=5550


#################
#######################PUERTA DE LA LLAVE DE LA ARANA


puertaRANA=Doors.CreateDoor("PuertaRANA", (-11250,0,177750), (0,0,1), 0, 2750, Doors.CLOSED)
puertaRANA1=Doors.CreateDoor("PuertaRANA1", (-11250,0,180250), (0,0,-1), 0, 2750, Doors.CLOSED)

puertaRANA.opentype=Doors.UNIF
puertaRANA.o_med_vel=-500
puertaRANA.o_med_displ=2750

puertaRANA1.opentype=Doors.UNIF
puertaRANA1.o_med_vel=-500
puertaRANA1.o_med_displ=2750


#################
#######################PUERTA DEL GOLEM


puertaGOL=Doors.CreateDoor("PuertaGOL", (-15850,-100,12850), (1,0,0), 0, 3500, Doors.CLOSED)

puertaGOL.opentype=Doors.UNIF
puertaGOL.o_med_vel=-500
puertaGOL.o_med_displ=3500


#################
#######################PUERTAS DE LA LLAVE NEGRA

puertaNEGRAdesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "PuertaNEGRADesliz")
puertaNEGRAgolpe=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe2.wav", "PuertaNEGRAGolpe")
puertaNEGRAdesliz.Pitch=1.6
puertaNEGRAgolpe.Pitch=1.2

puertaNEGRA2desliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "PuertaNEGRA2Desliz")
puertaNEGRA2golpe=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe2.wav", "PuertaNEGRA2Golpe")
puertaNEGRA2desliz.Pitch=1.3
puertaNEGRA2golpe.Pitch=1.1


#escalon 1a
puertaNEGRA=Doors.CreateDoor("PuertaNEGRA", (-53050,-2000,177000), (0,1,0), 0, 4000, Doors.OPENED)

puertaNEGRA.opentype=Doors.UNIF
puertaNEGRA.o_med_vel=-500
puertaNEGRA.o_med_displ=4000

puertaNEGRA.closetype=Doors.UNIF
puertaNEGRA.c_med_vel=3000
puertaNEGRA.c_med_displ=4000

puertaNEGRA.SetWhileCloseSound(puertaNEGRAdesliz)
puertaNEGRA.SetEndCloseSound(puertaNEGRAgolpe)

puertaNEGRA.Squezze=1


#escalon 2a
puertaNEGRA2=Doors.CreateDoor("PuertaNEGRA2", (-53050,-2000,172000), (0,1,0), 0, 4000, Doors.OPENED)

puertaNEGRA2.opentype=Doors.UNIF
puertaNEGRA2.o_med_vel=-500
puertaNEGRA2.o_med_displ=4000

puertaNEGRA2.closetype=Doors.UNIF
puertaNEGRA2.c_med_vel=2200
puertaNEGRA2.c_med_displ=4000

puertaNEGRA2.SetWhileCloseSound(puertaNEGRA2desliz)
puertaNEGRA2.SetEndCloseSound(puertaNEGRA2golpe)

puertaNEGRA2.Squezze=1


darfuncs.EnterSecEvent(-60000,-1100,172000,CierraPuertaNegra)
darfuncs.EnterSecEvent(-60000,-1100,178000,CierraPuertaNegra)
