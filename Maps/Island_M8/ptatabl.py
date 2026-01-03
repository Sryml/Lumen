import Bladex
import Doors
import Levers
import Locks
import Objects
import Sounds
import Button





######################################
########-------PUERTA DOBLE A TABLILLA------#######
######################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "MaderaGolpe")


puertadoble1=Doors.CreateDoor("PuertaDoble1", (-7500,5000,-3200), (0,0,-1), 0, 2250, Doors.CLOSED)


puertadoble1.opentype=Doors.UNIF
puertadoble1.o_med_vel=-400
puertadoble1.o_med_displ=2250

puertadoble1.closetype=Doors.UNIF
puertadoble1.c_med_displ=2250
puertadoble1.c_med_vel=400


puertadoble1.SetWhileOpenSound(maderadesliz)
puertadoble1.SetEndOpenSound(maderagolpe)

puertadoble1.SetWhileCloseSound(maderadesliz)
puertadoble1.SetEndCloseSound(maderagolpe)

#####
puertadoble2=Doors.CreateDoor("PuertaDoble2", (-7500,5000,-5000), (0,0,1), 0, 2250, Doors.CLOSED)

puertadoble2.opentype=Doors.UNIF
puertadoble2.o_med_vel=-400
puertadoble2.o_med_displ=2250

puertadoble2.closetype=Doors.UNIF
puertadoble2.c_med_displ=2250
puertadoble2.c_med_vel=400


#puertadoble2.SetWhileOpenSound(maderadesliz)
#puertadoble2.SetEndOpenSound(maderagolpe)

#puertadoble2.SetWhileCloseSound(maderadesliz)
#puertadoble2.SetEndCloseSound(maderagolpe)

##### Abrir puertas al accionar un pulsador




#if ExisteObjeto(["Tablilla1","Tablilla2","Tablilla3","Tablilla4","Tablilla5","Tablilla6","Tablilla7","Tablilla8","Tablilla9","Tablilla0"]): PonerBotonTablilla()
PonerBotonTablilla()
