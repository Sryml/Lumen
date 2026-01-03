import Doors
import Levers
import Locks
import Objects
import Sounds


###puertas asociadas a bucle

##puerta doble inferior

bucle1a=Doors.CreateDoor("Bucle1a", (420000,96000,27000), (-1,0,0), 0, 2000, Doors.OPENED)


bucle1a.opentype=Doors.UNIF
bucle1a.o_med_vel=-4000
bucle1a.o_med_displ=2000


bucle1a.closetype=Doors.UNIF
bucle1a.c_med_vel=4000
bucle1a.c_med_displ=2000


bucle2a=Doors.CreateDoor("Bucle2a", (422500,96000,27000), (1,0,0), 0, 2000, Doors.OPENED)


bucle2a.opentype=Doors.UNIF
bucle2a.o_med_vel=-4000
bucle2a.o_med_displ=2000


bucle2a.closetype=Doors.UNIF
bucle2a.c_med_vel=4000
bucle2a.c_med_displ=2000