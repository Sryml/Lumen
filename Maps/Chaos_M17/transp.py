# Positions to the teletransportation
#
# Position Two:
#        (421804, 65177, -12212)
# Position One:
#        (421110, 95177,  23395)
#
#        By Jose Dario Halle Cano

import Doors
import PhantonFX
import darfuncs
import Bladex
import Actions
import Sounds
import ItemTypes
import dust
import AbreCam

execfile("transpdes.py")

#----------------------------------------------------------------

#------------------------------------------------------------------------#
#                  Puerta de salida del bucle en zona superior
#------------------------------------------------------------------------#


spuertaizq= Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav",    "Spuertaizq")
spuertaizq.MaxDistance=50000
spuertaizq.MinDistance=15000
spuertaizq.Volume=1.0

finspuertaizq= Sounds.CreateEntitySound("../../Sounds/mechanism8.wav",         "Finspuertaizq")
finspuertaizq.MaxDistance=50000
finspuertaizq.MinDistance=15000
finspuertaizq.Volume=1.0



puertaizq=Doors.CreateDoor("Puertaizq", (421000,65000,-25000), (1,0,0), 0, 2000, Doors.CLOSED)
puertaizq.Squezze=1

puertaizq.opentype=Doors.UNIF
puertaizq.o_med_vel=-500
puertaizq.o_med_displ=2000


puertaizq.closetype=Doors.UNIF
puertaizq.c_med_vel=500
puertaizq.c_med_displ=2000

puertaizq.SetWhileOpenSound(spuertaizq)
puertaizq.SetEndOpenSound(finspuertaizq)
puertaizq.SetWhileCloseSound(spuertaizq)
puertaizq.SetEndCloseSound(finspuertaizq)

###### Definici�n de la puerta 4 derecha


spuertader= Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav",    "Spuertader")
spuertader.MaxDistance=50000
spuertader.MinDistance=15000
spuertader.Volume=1.0

finspuertader= Sounds.CreateEntitySound("../../Sounds/mechanism8.wav",         "Finspuertader")
finspuertader.MaxDistance=50000
finspuertader.MinDistance=15000
finspuertader.Volume=1.0

puertader=Doors.CreateDoor("Puertader", (423000,65000,-25000), (-1,0,0), 0, 2000, Doors.CLOSED)
puertader.Squezze=1

puertader.opentype=Doors.UNIF
puertader.o_med_vel=-500
puertader.o_med_displ=2000


puertader.closetype=Doors.UNIF
puertader.c_med_vel=500
puertader.c_med_displ=2000

puertader.SetWhileOpenSound(spuertader)
puertader.SetEndOpenSound(finspuertader)
puertader.SetWhileCloseSound(spuertader)
puertader.SetEndCloseSound(finspuertader)



sbucleinfi= Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav",    "Sbucleinfi")
sbucleinfi.MaxDistance=50000
sbucleinfi.MinDistance=15000
sbucleinfi.Volume=1.0


bucleinfi=Doors.CreateDoor("Bucleinfi", (420000,95000,27000), (1,0,0), 0, 2000, Doors.OPENED)
bucleinfi.Squezze=1


bucleinfi.opentype=Doors.UNIF
bucleinfi.o_med_vel=-2100
bucleinfi.o_med_displ=2000


bucleinfi.closetype=Doors.UNIF
bucleinfi.c_med_vel=2100
bucleinfi.c_med_displ=2000

bucleinfi.SetWhileOpenSound(sbucleinfi)
bucleinfi.SetWhileCloseSound(sbucleinfi)


sbucleinfd= Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav",    "Sbucleinfd")
sbucleinfd.MaxDistance=50000
sbucleinfd.MinDistance=15000
sbucleinfd.Volume=1.0

bucleinfd=Doors.CreateDoor("Bucleinfd", (422000,95000,27000), (-1,0,0), 0, 2000, Doors.OPENED)
bucleinfd.Squezze=1

bucleinfd.opentype=Doors.UNIF
bucleinfd.o_med_vel=-2100
bucleinfd.o_med_displ=2000


bucleinfd.closetype=Doors.UNIF
bucleinfd.c_med_vel=2100
bucleinfd.c_med_displ=2000

bucleinfd.SetWhileOpenSound(sbucleinfd)
bucleinfd.SetWhileCloseSound(sbucleinfd)

###########
###########

sbuclesupi= Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav",    "Sbuclesupi")
sbuclesupi.MaxDistance=50000
sbuclesupi.MinDistance=15000
sbuclesupi.Volume=1.0

buclesupi=Doors.CreateDoor("Buclesupi", (421000,65000,-16000), (1,0,0), 0, 2000, Doors.OPENED)
buclesupi.Squezze=1

buclesupi.opentype=Doors.UNIF
buclesupi.o_med_vel=-2000
buclesupi.o_med_displ=2000


buclesupi.closetype=Doors.UNIF
buclesupi.c_med_vel=2000
buclesupi.c_med_displ=2000

buclesupi.SetWhileOpenSound(sbuclesupi)
buclesupi.SetWhileCloseSound(sbuclesupi)


sbuclesupd= Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav",    "Sbuclesupd")
sbuclesupd.MaxDistance=50000
sbuclesupd.MinDistance=15000
sbuclesupd.Volume=1.0

buclesupd=Doors.CreateDoor("Buclesupd", (423000,65000,-16000), (-1,0,0), 0, 2000, Doors.OPENED)
buclesupd.Squezze=1

buclesupd.opentype=Doors.UNIF
buclesupd.o_med_vel=-2000
buclesupd.o_med_displ=2000


buclesupd.closetype=Doors.UNIF
buclesupd.c_med_vel=2000
buclesupd.c_med_displ=2000

buclesupd.SetWhileOpenSound(sbuclesupd)
buclesupd.SetWhileCloseSound(sbuclesupd)

P1=Bladex.GetSector(421110, 95177,  23395)
P2=Bladex.GetSector(421804, 65177, -12212)

# jump to the sector P1

P2.OnEnter=SaltaPrimero
P1.OnEnter=SaltaSegundo

CamIn1 =Bladex.GetSector(421595, 95177, 30789)
CamOut1=Bladex.GetSector(419727, 95177, 35034)

CamIn1.OnEnter  = CamSet1
CamOut1.OnEnter = CamBack

# sector de mover la camara  (422184, 65177, -20431)
# sector de volver la camara (423183, 65177, -27634)
# Posicion de la camara      (421663, 60618,-10103)
# Cambia el punto de vista




CamIn2 =Bladex.GetSector(422184, 65177, -20431)
CamOut2=Bladex.GetSector(423183, 65177, -27634)

CamIn2.OnEnter  = CamSet2
CamOut2.OnEnter = CamBack




#  /--------------------------------------------------------------------\  #
# |                        Enemigos del Bucle                            | #
#  \--------------------------------------------------------------------/  #

IsEnBucle = [   1,   1,   1,   1,   1]
BucleList = [None,None,None,None,None]


EnCounter = 0 # Number of Enemies actives
VampiroIs = 1

#sonidobucle=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-deslizando-2.wav", "Sonidobucle")
#sonidobucle.Volume=1; sonidobucle.MinDistance=4000; sonidobucle.MaxDistance=90000;

ESPECTRO_SEC = 10
Bladex.CreateEntity("Espectro","Espectro",0,0,0).SubscribeToList("Pin")



# e = SaleEspectro(char.Position[0],char.Position[1],char.Position[2])

TrapArena=Bladex.GetSector(420944, 77177, 2795)

TrapArena.OnEnter = EntraArena
TrapArena.OnLeave = SaleArena

_AppearsCagazo=Bladex.CreateSound("../../Sounds/AparicionEnric2.wav","AppearsCagazo")
_AppearsCagazo.MaxDistance=200000.0
_AppearsCagazo.MinDistance=20000.0

CreaVampiro()

CosoCounter = 0

# Bladex.GetEntity(char.ActiveEnemy).Life = 0
#----------------------------------------------------------------------#