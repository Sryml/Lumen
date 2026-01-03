####################################################
###---PUERTA---TORRE--3�-PLANTA--Y--SIGUIENTES---###
####################################################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta8=Doors.CreateDoor("Puerta8", (-14750,-26000,31000), (0,1,0), 1000, 4500, Doors.CLOSED)


puerta8.opentype=Doors.UNIF
puerta8.o_med_vel=-500
puerta8.o_med_displ=3500


puerta8.closetype=Doors.AC
puerta8.c_init_displ=3500
puerta8.c_med_vel=8000


puerta8.SetWhileOpenSound(maderadesliz)
puerta8.SetEndOpenSound(maderagolpe)

puerta8.SetWhileCloseSound(maderadesliz)
puerta8.SetEndCloseSound(maderagolpe)


###########################################


cerradurp8=Locks.PlaceLock("cerradurp8","Cerraduracutre",(-13848.165294,-23522.101741,32405.821862),(0.707080,0.707080,-0.006,-0.006),2.54)
cerradurp8.key="llave8"

def AbrePuertaLlave8():
	puerta8.OpenDoor()

def CierraPuertaLlave8():
	puerta1.CloseDoor()

cerradurp8.OnUnLockFunc=AbrePuertaLlave8
cerradurp8.OnUnLockArgs=()

cerradurp8.OnLockFunc=CierraPuertaLlave8
cerradurp8.OnLockArgs=()


o=Bladex.CreateEntity("llave8","Llavecutre",-12628.242792,-22272.365901,31232.800632)
o.Static=0
o.Scale=1.0
o.Orientation=0.006559,-0.975726,-0.006481,-0.218802