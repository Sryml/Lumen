import Doors
import Levers
import Locks
import Objects
import Sounds
import Sparks
import Button
import AniSound
import Reference
import EnemyTypes
import Breakings
import Stars
import darfuncs
import pocimac
import Ontake
import OnOff

#####################################
###      puerta del elevador      ###
#####################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta0=Doors.CreateDoor("Puerta0", (-29060,9000,57120), (0,1,0), 1500, 5200, Doors.OPENED)


puerta0.opentype=Doors.UNIF
puerta0.o_med_vel=-500
puerta0.o_med_displ=3700


puerta0.closetype=Doors.AC
puerta0.c_init_displ=3700
puerta0.c_med_vel=8000


puerta0.SetWhileOpenSound(maderadesliz)
puerta0.SetEndOpenSound(maderagolpe)


puerta0.SetWhileCloseSound(maderadesliz)
puerta0.SetEndCloseSound(maderagolpe)


_SndRugido=Sounds.CreateEntitySound("../../Sounds/rugido-demon2.wav","RugidoPuertice")
_SndRugido.MaxDistance=1000000.0


###llave0. La tiene un guardia###


cerradurp0=Locks.PlaceLock("cerradurp0","Cerraduracutre",(-25851.826201,9949.879220,55082.827184),(0.500000,0.500000,0.500000,-0.500000),3.0)
cerradurp0.key="llave0"


cerradurp0.OnUnLockFunc=AbrePuertaLlave0
cerradurp0.OnUnLockArgs=()

cerradurp0.OnLockFunc=CierraPuertaLlave0
cerradurp0.OnLockArgs=()

darfuncs.SetHint(cerradurp0.obj,"Store Lock")


############

cerradur11=Locks.PlaceLock("cerradur11","Cerraduracutre",(53631.611497,-1189.062591,88674.492274),(0.000000,0.000000,0.707107,-0.707107),3.0)
darfuncs.SetHint(cerradur11.obj,"Courtyard Lock")



###puerta de la sala de las vidrieras###############
##########################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puertavid=Doors.CreateDoor("Puertavid", (-11625,-3000,21937), (0,1,0), 2000, 7800, Doors.OPENED)


puertavid.opentype=Doors.UNIF
puertavid.o_med_vel=-500
puertavid.o_med_displ=5800


puertavid.closetype=Doors.AC
puertavid.c_init_displ=5800
puertavid.c_med_vel=8000

puertavid.SetWhileOpenSound(maderadesliz)
puertavid.SetEndOpenSound(maderagolpe)

puertavid.SetWhileCloseSound(maderadesliz)
puertavid.SetEndCloseSound(maderagolpe)

cerradurpvid=Locks.PlaceLock("cerradurpvid","Cerraduracutre",(-14191.233548,52.055610,24911.719622),(0.500000,0.500000,0.500000,-0.500000),3.0)
darfuncs.SetHint(cerradurpvid.obj,"Palace Lock")



#######################################################
########## PUERTA DE LA SALA DE LA TABLILLA ###########
#######################################################

piedradesliz=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "PiedraDesliz")
piedragolpe=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "PiedraGolpe")


#escalon 1a
puerta1a=Doors.CreateDoor("Puerta1a", (44680,-3500,17400), (0,1,0), 2000, 7000, Doors.CLOSED)

puerta1a.opentype=Doors.UNIF
puerta1a.o_med_vel=-500
puerta1a.o_med_displ=7000

puerta1a.closetype=Doors.UNIF
puerta1a.c_med_vel=900
puerta1a.c_med_displ=7000

puerta1a.SetWhileOpenSound(piedradesliz)
puerta1a.SetEndOpenSound(piedragolpe)


o=Bladex.CreateEntity("bloque1","Bloque",44815.936676,-9504.976973,26984.732126)
o.Static=0
o.Scale=1.780901
o.Orientation=0.500000,0.500000,0.500000,-0.500000





button=Button.CreateButtonCombination(0,Abrep1,"")
button.AddButton("bloque1",3,(0,0,1),-400,0,0,1)


#o=Bladex.CreateEntity("bloquet","Adoquinpulsador",44815.936676,-9504.976973,26984.732126)
#o.Static=0
#o.Scale=1.780901
#o.Orientation=0.500000,0.500000,0.500000,-0.500000
