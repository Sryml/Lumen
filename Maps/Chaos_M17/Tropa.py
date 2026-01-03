########################################################################################################
####                                   Tropa de esqueletos en el puente                             ####
########################################################################################################
import darfuncs
import EnemyTypes
import Sounds
import Doors
import darfuncs
import Actions
import OnOff

_SndQueleto1=Bladex.CreateSound("../../Sounds/M-paso-hueso-arena4.wav","SndQueleto1")
_SndQueleto1.MinDistance=10000.0
_SndQueleto1.MaxDistance=100000.0


_SndQueleto2=Bladex.CreateSound("../../Sounds/M-paso-hueso-arena5.wav","SndQueleto2")
_SndQueleto2.MinDistance=10000.0
_SndQueleto2.MaxDistance=100000.0

Pto1 = 528174, 86835, 3558
Pto2 = 517394, 86085, -6374
Pto3 = 501777, 85335, -4751


bigdoori= Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav",    "Bigdoori")
bigdoori.MaxDistance=50000
bigdoori.MinDistance=15000
bigdoori.Volume=1.0

finbigdoori= Sounds.CreateEntitySound("../../Sounds/mechanism8.wav",         "Finbigdoori")
finbigdoori.MaxDistance=50000
finbigdoori.MinDistance=15000
finbigdoori.Volume=1.0

abismoii=Doors.CreateDoor("Abismoii", (526000,88000,18000), (1,0,0), 0, 3687.5, Doors.OPENED)



abismoii.opentype=Doors.UNIF
abismoii.o_med_vel=-800
abismoii.o_med_displ=3687.5


abismoii.closetype=Doors.UNIF
abismoii.c_med_vel=800
abismoii.c_med_displ=3687.5


abismoii.SetWhileOpenSound(bigdoori)
abismoii.SetEndOpenSound(finbigdoori)

abismoii.SetWhileCloseSound(bigdoori)
abismoii.SetEndCloseSound(finbigdoori)


##hoja derecha


bigdoord= Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav",    "Bigdoord")
bigdoord.MaxDistance=50000
bigdoord.MinDistance=15000
bigdoord.Volume=1.0

finbigdoord= Sounds.CreateEntitySound("../../Sounds/mechanism8.wav",         "Finbigdoord")
finbigdoord.MaxDistance=50000
finbigdoord.MinDistance=15000
finbigdoord.Volume=1.0


abismodd=Doors.CreateDoor("Abismodd", (530000,88000,18000), (-1,0,0), 0, 3687.5, Doors.OPENED)



abismodd.opentype=Doors.UNIF
abismodd.o_med_vel=-800
abismodd.o_med_displ=3687.5


abismodd.closetype=Doors.UNIF
abismodd.c_med_vel=800
abismodd.c_med_displ=3687.5


abismodd.SetWhileOpenSound(bigdoord)
abismodd.SetEndOpenSound(finbigdoord)

abismodd.SetWhileCloseSound(bigdoord)
abismodd.SetEndCloseSound(finbigdoord)


#funci�n que abre y cierra las hojas de la puerta unisono


################################################################################################################
NumQueletum = 0

CreaEsqueleto(1,528271,87405,13257,19)
CreaEsqueleto(2,532323,87163,6279,19)
CreaEsqueleto(3,526952,87219,9463,18)
CreaEsqueleto(4,529601,87199,10900,18)

Bladex.AddCombustionDataFor("Skeleton", "Fire", 250, 400, 4, 1, 3, 144000) # se extinguira en 40 horas!


TropaSector=Bladex.GetSector(479388, 84335, 11731)
TropaSector.OnEnter = TropelFurioso



########NUEVO NUEVO NUEVO NUEVO


##nombre lampara que debe apagarse al lanzarse esqueletos corriendo: "Egipto3"

##nombre lampara que debe apagarse al salir kaos 1 y kaos 2: "Egipto4"



nchaosk1=Bladex.CreateEntity("NChaosK1", "ChaosKnight", 524495.459195, 87122.946728, 9463.80253264,"Person")
nchaosk1.Angle=3.09108795697
nchaosk1.SetOnFloor()
nchaosk1.Level=11
EnemyTypes.EnemyDefaultFuncs(nchaosk1)

nchaosk1.Data.DamageFactorNone=0.15
nchaosk1.Data.DamageFactorLight=0.35
nchaosk1.Data.DamageFactorHeavy=0.35
nchaosk1.Data.PrepareWeapons("Espadon", "Escudon")
#chaosk1.Data.PrepareDisappearance()
darfuncs.HideBadGuy(nchaosk1.Name)



nchaosk2=Bladex.CreateEntity("NChaosK2", "ChaosKnight", 531565.583726, 87146.419675, 9467.11029756,"Person")
nchaosk2.Angle=2.91502000808
nchaosk2.SetOnFloor()
nchaosk2.Level=12
EnemyTypes.EnemyDefaultFuncs(nchaosk2)

nchaosk2.Data.DamageFactorNone=0.15
nchaosk2.Data.DamageFactorLight=0.35
nchaosk2.Data.DamageFactorHeavy=0.35
nchaosk2.Data.PrepareWeapons("Espadon", "Escudon")
#chaosk2.Data.PrepareDisappearance()
darfuncs.HideBadGuy(nchaosk2.Name)

NCHKAS=2

nchaosk1.ImDeadFunc=AbrirSiMueren
nchaosk2.ImDeadFunc=AbrirSiMueren
