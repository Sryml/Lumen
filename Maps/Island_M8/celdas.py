import Doors
import Levers
import Locks
import Objects
import Sounds
import Sparks




##########celdas con prisioneros


############################################################
#####--RASTRILLO---ENTRADA-AL RECINTO--------------#########
############################################################



sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")
#
rejasi=Bladex.CreateEntity("Rejasi1","Rastrillo",-1382.816000,490.112000,19359.053000)
rejasi.Scale=0.685153
rejasi.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetSparkling("Rejasi1")

rejasi1din=Objects.CreateDinamicObject("Rejasi1")

#
rejasi=Bladex.CreateEntity("Rejasi2","Rastrillo",-1339.435000,469.236000,13710.692000)
rejasi.Scale=0.685153
rejasi.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetSparkling("Rejasi2")

rejasi2din=Objects.CreateDinamicObject("Rejasi2")

#
rejasi=Bladex.CreateEntity("Rejasi3","Rastrillo",3111.141000,463.808000,19471.063000)
rejasi.Scale=0.685153
rejasi.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetSparkling("Rejasi3")

rejasi3din=Objects.CreateDinamicObject("Rejasi3")

#
rejasi=Bladex.CreateEntity("Rejasi4","Rastrillo",3152.981000,477.674000,13570.288000)
rejasi.Scale=0.685153
rejasi.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetSparkling("Rejasi4")

rejasi4din=Objects.CreateDinamicObject("Rejasi4")

##funciones abrir-cerrar##



###cerradura rastrillo###



cerramaz1=Locks.PlaceLock("cerramaz1","Cerraduracutre",(841.122168,1349.007243,18798.859471),(0.50,0.5,0.5,-0.5),2.5)
cerramaz1.key="llave"

cerramaz2=Locks.PlaceLock("cerramaz2","Cerraduracutre",(714.335216,1391.926368,14342.044003),(0.5,0.5,-0.5,0.5),2.5)
cerramaz2.key="llave"

cerramaz1.OnUnLockFunc=Abreladosr1
cerramaz1.OnUnLockArgs=()

cerramaz1.OnLockFunc=Cierraladosr1
cerramaz1.OnLockArgs=()

cerramaz2.OnUnLockFunc=Abreladosr2
cerramaz2.OnUnLockArgs=()

cerramaz2.OnLockFunc=Cierraladosr2
cerramaz2.OnLockArgs=()

darfuncs.SetHint(cerramaz1.obj,"Dungeon Lock")

darfuncs.SetHint(cerramaz2.obj,"Dungeon Lock")