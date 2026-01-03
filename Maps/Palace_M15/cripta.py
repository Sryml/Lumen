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
escalon1a=Doors.CreateDoor("Escalon1a", (-24200,7100,55800), (0,-1,0), 0, 300, Doors.CLOSED)

escalon1a.opentype=Doors.UNIF
escalon1a.o_med_vel=-500
escalon1a.o_med_displ=300

escalon1a.closetype=Doors.UNIF
escalon1a.c_med_vel=500
escalon1a.c_med_displ=300


#escalon 2a
escalon2a=Doors.CreateDoor("Escalon2a", (-24200,7100,56800), (0,-1,0), 0, 600, Doors.CLOSED)

escalon2a.opentype=Doors.UNIF
escalon2a.o_med_vel=-500
escalon2a.o_med_displ=600

escalon2a.closetype=Doors.UNIF
escalon2a.c_med_vel=500
escalon2a.c_med_displ=600


#escalon 3a
escalon3a=Doors.CreateDoor("Escalon3a", (-24200,7100,57800), (0,-1,0), 0, 900, Doors.CLOSED)

escalon3a.opentype=Doors.UNIF
escalon3a.o_med_vel=-500
escalon3a.o_med_displ=900

escalon3a.closetype=Doors.UNIF
escalon3a.c_med_vel=500
escalon3a.c_med_displ=900


#escalon 4a
escalon4a=Doors.CreateDoor("Escalon4a", (-24200,7100,58800), (0,-1,0), 0, 1200, Doors.CLOSED)

escalon4a.opentype=Doors.UNIF
escalon4a.o_med_vel=-500
escalon4a.o_med_displ=1200

escalon4a.closetype=Doors.UNIF
escalon4a.c_med_vel=500
escalon4a.c_med_displ=1200


#escalon 5a
escalon5a=Doors.CreateDoor("Escalon5a", (-24200,7100,59800), (0,-1,0), 0, 1500, Doors.CLOSED)

escalon5a.opentype=Doors.UNIF
escalon5a.o_med_vel=-500
escalon5a.o_med_displ=1500

escalon5a.closetype=Doors.UNIF
escalon5a.c_med_vel=500
escalon5a.c_med_displ=1500


#escalon 6a
escalon6a=Doors.CreateDoor("Escalon6a", (-24200,7100,60800), (0,-1,0), 0, 1800, Doors.CLOSED)

escalon6a.opentype=Doors.UNIF
escalon6a.o_med_vel=-500
escalon6a.o_med_displ=1800

escalon6a.closetype=Doors.UNIF
escalon6a.c_med_vel=500
escalon6a.c_med_displ=1800


#escalon 7a
escalon7a=Doors.CreateDoor("Escalon7a", (-24200,7100,61800), (0,-1,0), 0, 2100, Doors.CLOSED)

escalon7a.opentype=Doors.UNIF
escalon7a.o_med_vel=-500
escalon7a.o_med_displ=2100

escalon7a.closetype=Doors.UNIF
escalon7a.c_med_vel=500
escalon7a.c_med_displ=2100


#escalon 8a
escalon8a=Doors.CreateDoor("Escalon8a", (-24200,7100,62800), (0,-1,0), 0, 2400, Doors.CLOSED)

escalon8a.opentype=Doors.UNIF
escalon8a.o_med_vel=-500
escalon8a.o_med_displ=2400

escalon8a.closetype=Doors.UNIF
escalon8a.c_med_vel=500
escalon8a.c_med_displ=2400


#escalon 9a
escalon9a=Doors.CreateDoor("Escalon9a", (-24200,7100,63800), (0,-1,0), 0, 2700, Doors.CLOSED)

escalon9a.opentype=Doors.UNIF
escalon9a.o_med_vel=-500
escalon9a.o_med_displ=2700

escalon9a.closetype=Doors.UNIF
escalon9a.c_med_vel=500
escalon9a.c_med_displ=2700


#escalon 10a
escalon10a=Doors.CreateDoor("Escalon10a", (-24200,7100,64800), (0,-1,0), 0, 3000, Doors.CLOSED)

escalon10a.opentype=Doors.UNIF
escalon10a.o_med_vel=-500
escalon10a.o_med_displ=3000

escalon10a.closetype=Doors.UNIF
escalon10a.c_med_vel=500
escalon10a.c_med_displ=3000


#escalon 11a
escalon11a=Doors.CreateDoor("Escalon11a", (-24200,7100,65800), (0,-1,0), 0, 3300, Doors.CLOSED)

escalon11a.opentype=Doors.UNIF
escalon11a.o_med_vel=-500
escalon11a.o_med_displ=3300

escalon11a.closetype=Doors.UNIF
escalon11a.c_med_vel=500
escalon11a.c_med_displ=3300


#escalon 12a
escalon12a=Doors.CreateDoor("Escalon12a", (-24200,7100,66800), (0,-1,0), 0, 3600, Doors.CLOSED)

escalon12a.opentype=Doors.UNIF
escalon12a.o_med_vel=-500
escalon12a.o_med_displ=3600

escalon12a.closetype=Doors.UNIF
escalon12a.c_med_vel=500
escalon12a.c_med_displ=3600


#escalon 13a
escalon13a=Doors.CreateDoor("Escalon13a", (-24200,7100,67800), (0,-1,0), 0, 3900, Doors.CLOSED)

escalon13a.opentype=Doors.UNIF
escalon13a.o_med_vel=-500
escalon13a.o_med_displ=3900

escalon13a.closetype=Doors.UNIF
escalon13a.c_med_vel=500
escalon13a.c_med_displ=3900


#puerta cerrada
puertacer=Doors.CreateDoor("Puertacer", (-33600,-2000,62000), (0,1,0), 0, 6250, Doors.CLOSED)

puertacer.opentype=Doors.UNIF
puertacer.o_med_vel=-500
puertacer.o_med_displ=5000

puertacer.closetype=Doors.UNIF
puertacer.c_med_vel=500
puertacer.c_med_displ=5000


#funci�n que sube y baja los escalones de ambos tramos al unisono

#escalon13a.SetWhileOpenSound(maderadesliz)
#escalon13a.SetEndOpenSound(maderagolpe)

#escalon13a.SetWhileCloseSound(maderadesliz)
#escalon13a.SetEndCloseSound(maderagolpe)

blo=Bladex.CreateEntity("bloque","Bloque",-24214.880255,1504.992658,33951.570934,"Physic")
blo.Scale=1.644632
blo.Orientation=0.500000,0.500000,-0.500000,-0.500000
darfuncs.SetHint(blo,"Trigger")

button=Button.CreateButtonCombination(0,Descubre,"")
button.AddButton("bloque",3,(0,0,1),-400,1,0,0)

blo.Frozen=1



#################
### Muro falso
#################

sonidoroturamurofalso=Bladex.CreateSound("../../Sounds/single-boulder-impact.wav", "SonidoRoturaMuroFalso")

sectormurofalso=Bladex.GetSector(-24250, -1750, 33250)
sectormurofalso.Active=0

sectormurofalso.InitBreak((0.0, 0.0, 375.0), (800.0, 200.0, 0.0), (-200.0, 800.0, 0.0))

sectorrompemurofalso=Bladex.GetSector(-24250, -1750, 32750)
sectorrompemurofalso.ActiveSurface=0, 0, -1

######### Funcion: RompeMuroFalso

sectorrompemurofalso.OnHit=RompeMuroFalso



###################
### Zona secreta
###################

vigaseccen=Bladex.CreateEntity("VigaSecCen","Vigaro1",-24175.000000,9650.000000,81725.000000)
vigaseccen.Scale=0.932718
vigaseccen.Orientation=1.000000,0.000000,0.000000,0.000000

vigasecder=Bladex.CreateEntity("VigaSecDer","Vigaro2",-22681.250000,8500.000000,81425.000000)
vigasecder.Scale=0.932718
vigasecder.Orientation=0.000000,1.000000,0.000000,0.000000

vigasecizq=Bladex.CreateEntity("VigaSecIzq","Vigaro2",-25681.250000,8500.000000,81725.000000)
vigasecizq.Scale=0.932718
vigasecizq.Orientation=0.000000,0.000000,0.000000,-1.000000


######### Funcion: AbreZonaSecreta()
