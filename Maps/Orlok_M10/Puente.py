import Bladex
import AuxFuncs
import EnemyTypes
import Sparks
import Actions
import math
import Breakings
import Doors
import Sounds
import LevelFuncs

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 12
expected_player_lvl_max= 16

lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)



####################
##	Enemigos
####################


## 2 Orcos guardando el puente armados con cimitarras. Areas 1 y 2

#orco puente 1

arma=Bladex.CreateEntity("OrlokArmaOrcoPuente1", "Maza2", 0.0, 0.0, 0.0, "Weapon")
ItemTypes.ItemDefaultFuncs(arma)
orcopuente1=Bladex.CreateEntity("OrlokOrcoPuente1", "Ork", -47000, -31500, -54500, "Person")
orcopuente1.Position=-49500, -31500, -55500
orcopuente1.Angle=3.14159
orcopuente1.Level=lvl_control.GiveLevel(6,10)
Actions.TakeObject(orcopuente1.Name, arma.Name)
orcopuente1.ActionAreaMin=math.pow(2,0)
orcopuente1.ActionAreaMax=math.pow(2,1)
EnemyTypes.EnemyDefaultFuncs(orcopuente1)
orcopuente1.Blind=1
orcopuente1.Deaf=1
orcopuente1.SetOnFloor()


#orco puente 2

arma=Bladex.CreateEntity("OrlokArmaOrcoPuente2", "Hacha4", 0.0, 0.0, 0.0, "Weapon")
ItemTypes.ItemDefaultFuncs(arma)
orcopuente2=Bladex.CreateEntity("OrlokOrcoPuente2", "Ork", -52000, -31500, -55000, "Person")
orcopuente2.Position=-51000, -31500, -54000
orcopuente2.Angle=3.14159
orcopuente2.Level=lvl_control.GiveLevel(7,11)
Actions.TakeObject(orcopuente2.Name, arma.Name)
orcopuente2.ActionAreaMin=math.pow(2,0)
orcopuente2.ActionAreaMax=math.pow(2,1)
EnemyTypes.EnemyDefaultFuncs(orcopuente2)
orcopuente2.Blind=1
orcopuente2.Deaf=1
orcopuente2.SetOnFloor()


##################
##	Varios
##################

### Puerta guarida

deslizpuertapuente=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizPuertaPuente")
golpepuertapuente=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe2.wav", "GolpePuertaPuente")

deslizpuertapuente.Volume=0.5
golpepuertapuente.Volume=0.5

puertapuente=Doors.CreateDoor("PuertaPuente", (-49750, -31500, -57250), (-1, 0, 0), 0, 2000, Doors.CLOSED)

puertapuente.opentype=Doors.AC_UNIF
puertapuente.o_init_vel=0
puertapuente.o_init_displ=250
puertapuente.o_med_vel=-1000
puertapuente.o_med_displ=1750

puertapuente.closetype=Doors.AC_UNIF
puertapuente.c_init_vel=0
puertapuente.c_init_displ=250
puertapuente.c_med_vel=1000
puertapuente.c_med_displ=1750

puertapuente.SetWhileOpenSound(deslizpuertapuente)
puertapuente.SetEndOpenSound(golpepuertapuente)

puertapuente.SetWhileCloseSound(deslizpuertapuente)
puertapuente.SetEndCloseSound(golpepuertapuente)


### Sector puente

puente=Bladex.GetSector(-47000.0, -31000.0, -68000.0)



############################
##	Funcionamiento
############################


######## Funcion: DespiertaOrcoPuente(person)

######## Funcion: ColocacionOrcosPuente()

######## Funcion: AparecenOrcosPuente(sec_index, ent_name)

puente.OnEnter=AparecenOrcosPuente
