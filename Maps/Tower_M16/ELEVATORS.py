import Doors
import Doors
import Levers
import Locks
import Objects
import Sounds
import OnOff



###########################################
#######  ELEVATOR FINAL   #################


lael=Bladex.CreateEntity("lampelevator","Lamparaegipto",6710.276000,-90400.000,11086.586000)
lael.Static=1
lael.Scale=1.000000
lael.Orientation=0.707107,0.707107,0.000000,0.000000
lael.FiresIntensity=[ 0 ]
lael.Lights=[ (15.000000,0.031250,(255,171,79)) ]


laelmovil=Objects.CreateDinamicObject("lampelevator")

loopelevador=Sounds.CreateEntitySound("../../Sounds/drawbridge-loop.wav", "LoopElevador")
golpeelevador=Sounds.CreateEntitySound("../../Sounds/metal-lever3.wav", "GolpeElevador")


columnaelevador=Doors.CreateDoor("ColumnaElevador", (8000,-90000,9000), (0, -1, 0), 0, 21000, Doors.OPENED)

columnaelevador.opentype=Doors.AC_UNIF_DEC
columnaelevador.o_init_vel=0
columnaelevador.o_init_displ=500
columnaelevador.o_med_vel=-2000
columnaelevador.o_med_displ=20000
columnaelevador.o_end_vel=0
columnaelevador.o_end_displ=500

columnaelevador.closetype=Doors.AC_UNIF_DEC
columnaelevador.c_init_vel=0
columnaelevador.c_init_displ=500
columnaelevador.c_med_vel=2000
columnaelevador.c_med_displ=20000
columnaelevador.c_end_vel=0
columnaelevador.c_end_displ=500

elevInAction = 0

OnOff.AddLightData("brasania1", 10.0 ,0.070000 )
OnOff.AddLightData("brasania2", 10.0 ,0.070000 )

columnaelevador.OnEndCloseFunc	= ElevadorEndCloseFunc
columnaelevador.OnEndOpenFunc	= ElevadorEndOpenFunc

palancaelevador=Levers.PlaceLever("PalancaElevador", Levers.LeverType3, (10946.854188,-90345.706580,9154.946053), (0.5,0.5,0.5,-0.5), 1.0)
palancaelevador.mode=1

palancaelevador.OnTurnOnFunc=SubeElevadorPalanca
palancaelevador.OnTurnOnArgs=()



###########################################3
#######  ELEVATOR DEMONIOS   #################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


elevator2=Doors.CreateDoor("elevator2", (-26500,-79000,25500), (0,-1,0), 0, 9000, Doors.OPENED)


elevator2.opentype=Doors.UNIF
elevator2.o_med_vel=-2000
elevator2.o_med_displ=9000


elevator2.closetype=Doors.UNIF
elevator2.c_med_displ=9000
elevator2.c_med_vel=2000


elevator2.SetWhileOpenSound(maderadesliz)
elevator2.SetEndOpenSound(maderagolpe)

elevator2.SetWhileCloseSound(maderadesliz)
elevator2.SetEndCloseSound(maderagolpe)

##### Accionar elevator al accionar una palanca


palaeD1=Levers.PlaceLever("PALAED1",Levers.LeverType3,(-27819.923,-79563.432,27007.945),(0.653282,0.653282,-0.270598,0.270598),1.0)
palaeD1.mode=1

palaeD2=Levers.PlaceLever("PALAED2",Levers.LeverType3,(-27819.923,-88563.432,27007.945),(0.653282,0.653282,-0.270598,0.270598),1.0)
palaeD2.mode=1

palaeD3=Levers.PlaceLever("PALAED3",Levers.LeverType3,(-21812.814285,-79059.983362,20921.074613),(0.270598,0.270598,0.653282,-0.653282),1.0)
palaeD3.mode=1

palaeD2.OnTurnOnFunc=Abreelevator2
palaeD2.OnTurnOnArgs=()

palaeD3.OnTurnOnFunc=Abreelevator2
palaeD3.OnTurnOnArgs=()

palaeD1.OnTurnOffFunc=Cierraelevator2
palaeD1.OnTurnOffArgs=()



###########################################3
#######  ELEVATOR 2 PARTE   #################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


elevator3=Doors.CreateDoor("elevator3", (2000,-16000,24000), (0,-1,0), 0, 5750, Doors.OPENED)


elevator3.opentype=Doors.UNIF
elevator3.o_med_vel=-2000
elevator3.o_med_displ=5750


elevator3.closetype=Doors.UNIF
elevator3.c_med_displ=5750
elevator3.c_med_vel=2000


elevator3.SetWhileOpenSound(maderadesliz)
elevator3.SetEndOpenSound(maderagolpe)

elevator3.SetWhileCloseSound(maderadesliz)
elevator3.SetEndCloseSound(maderagolpe)

##### Accionar elevator al accionar una palanca


palaeP1=Levers.PlaceLever("PALAEP1",Levers.LeverType2,(2041.051836,-13138.727911,26109.637188),(0.707107,-0.000000,0.707107,0.000000),1.0)
palaeP1.mode=1

palaeP2=Levers.PlaceLever("PALAEP2",Levers.LeverType2,(-1191.767021,-13215.263833,21683.778303),(0.008727,0.000000,-0.999962,-0.000000),1.0)
palaeP2.mode=1

#palaeP2=Levers.PlaceLever("PALAEP2",Levers.LeverType2,(-18404.01,-88000,30222.21),(0.656592,0.649913,0.267288,-0.273967),1.0)
#palaeP2.mode=1



darfuncs. EnterSecEvent(-27738.0913588, -19306.4828945, 18197.2,eleto3)


palaeP2.OnTurnOnFunc=Abreelevator3
palaeP2.OnTurnOnArgs=()

palaeP1.OnTurnOffFunc=Cierraelevator3
palaeP1.OnTurnOffArgs=()
