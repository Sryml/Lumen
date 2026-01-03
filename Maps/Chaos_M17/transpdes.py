###Bucle en escaleras

###tramo A. La escalera baja

#escalon 1a


escalon1a=Doors.CreateDoor("Escalon1a", (424000,81500,24000), (0,-1,0), 0, 1000, Doors.CLOSED)


escalon1a.opentype=Doors.UNIF
escalon1a.o_med_vel=-500
escalon1a.o_med_displ=1000


escalon1a.closetype=Doors.UNIF
escalon1a.c_med_vel=500
escalon1a.c_med_displ=1000


#escalon 2a


escalon2a=Doors.CreateDoor("Escalon2a", (426000,82000,24000), (0,-1,0), 0, 2000, Doors.CLOSED)


escalon2a.opentype=Doors.UNIF
escalon2a.o_med_vel=-500
escalon2a.o_med_displ=2000


escalon2a.closetype=Doors.UNIF
escalon2a.c_med_vel=500
escalon2a.c_med_displ=2000


#escalon 3a


escalon3a=Doors.CreateDoor("Escalon3a", (428000,82500,23000), (0,-1,0), 0, 3000, Doors.CLOSED)


escalon3a.opentype=Doors.UNIF
escalon3a.o_med_vel=-500
escalon3a.o_med_displ=3000


escalon3a.closetype=Doors.UNIF
escalon3a.c_med_vel=500
escalon3a.c_med_displ=3000


#escalon 4a


escalon4a=Doors.CreateDoor("Escalon4a", (429000,83000,21000), (0,-1,0), 0, 4000, Doors.CLOSED)


escalon4a.opentype=Doors.UNIF
escalon4a.o_med_vel=-500
escalon4a.o_med_displ=4000


escalon4a.closetype=Doors.UNIF
escalon4a.c_med_vel=500
escalon4a.c_med_displ=4000


#escalon 5a

sescalon5a= Sounds.CreateEntitySound("../../Sounds/puerta-piedra-deslizando-2.wav",    "Sescalon5a")
sescalon5a.MaxDistance=50000
sescalon5a.MinDistance=15000
sescalon5a.Volume=1.0

escalon5a=Doors.CreateDoor("Escalon5a", (429000,83500,20000), (0,-1,0), 0, 5000, Doors.CLOSED)


escalon5a.opentype=Doors.UNIF
escalon5a.o_med_vel=-500
escalon5a.o_med_displ=5000


escalon5a.closetype=Doors.UNIF
escalon5a.c_med_vel=500
escalon5a.c_med_displ=5000

escalon5a.SetWhileOpenSound(sescalon5a)



###tramo B. La escalera baja

#escalon 1b


escalon1b=Doors.CreateDoor("Escalon1b", (420000,81500,24000), (0,-1,0), 0, 1000, Doors.OPENED)


escalon1b.opentype=Doors.UNIF
escalon1b.o_med_vel=-500
escalon1b.o_med_displ=1000


escalon1b.closetype=Doors.UNIF
escalon1b.c_med_vel=500
escalon1b.c_med_displ=1000


#escalon 2b


escalon2b=Doors.CreateDoor("Escalon2b", (418000,82000,24000), (0,-1,0), 0, 2000, Doors.OPENED)


escalon2b.opentype=Doors.UNIF
escalon2b.o_med_vel=-500
escalon2b.o_med_displ=2000


escalon2b.closetype=Doors.UNIF
escalon2b.c_med_vel=500
escalon2b.c_med_displ=2000


#escalon 3b


escalon3b=Doors.CreateDoor("Escalon3b", (416000,82500,23000), (0,-1,0), 0, 3000, Doors.OPENED)


escalon3b.opentype=Doors.UNIF
escalon3b.o_med_vel=-500
escalon3b.o_med_displ=3000


escalon3b.closetype=Doors.UNIF
escalon3b.c_med_vel=500
escalon3b.c_med_displ=3000


#escalon 4b


escalon4b=Doors.CreateDoor("Escalon4b", (414000,83000,21000), (0,-1,0), 0, 4000, Doors.OPENED)


escalon4b.opentype=Doors.UNIF
escalon4b.o_med_vel=-500
escalon4b.o_med_displ=4000


escalon4b.closetype=Doors.UNIF
escalon4b.c_med_vel=500
escalon4b.c_med_displ=4000


#escalon 5b


escalon5b=Doors.CreateDoor("Escalon5b", (414000,83500,20000), (0,-1,0), 0, 5000, Doors.OPENED)


escalon5b.opentype=Doors.UNIF
escalon5b.o_med_vel=-500
escalon5b.o_med_displ=5000


escalon5b.closetype=Doors.UNIF
escalon5b.c_med_vel=500
escalon5b.c_med_displ=5000



#funci�n que sube y baja los escalones de ambos tramos al unisono

# Target =
#   Cam1 = C(412614, 82609, 16909) T(421759, 80432, 22937)
#   Cam2 = C(422362, 72746, 25179) T(421759, 80432, 22937)
#   Cam3 = C(426736, 78226, 23577) T(431532, 82430, 16320)
