import Reference
#import Select
import Change
import Actions
import Doors
import Levers
import Locks
import Objects
import Sounds
import Bladex
import ReadGSFile
import Button
import AuxFuncs
import EnemyTypes
#import AniSound
import Ontake
import Stars
import darfuncs

###Rastrillo trampa LlaveGas de oro


##### Rastrillo #####

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")



rastrillomovil=Bladex.CreateEntity("RastrilloMovil","Rastrillo",325902.027381,4018.483890,-210965.412381)
rastrillomovil.Static=1
rastrillomovil.Scale=1
rastrillomovil.Orientation=0.707107,0.707107,0.000000,0.000000

rastrillomovildin=Objects.CreateDinamicObject("RastrilloMovil")




###LlaveGas cobre oxidada abrerastrillo###


CerraduraGas=Locks.PlaceLock("CerraduraGas","Cerraduracobox",(323043.904114,8800.149830,-210244.081568),(0.500000,0.500000,-0.500000,0.500000),1.518790)
CerraduraGas.key="LlaveGas1"
darfuncs.SetHint(CerraduraGas.obj,"Jara Lock")


lg=Bladex.CreateEntity("LlaveGas1","Llavecobox",336415.68096, 15765.993886, -228882.31374)
lg.Static=0
lg.Scale=1
lg.Orientation=0.967782,0.005159,-0.251736,-0.000391
darfuncs.SetHint(lg,"Jara Key")
Stars.Twinkle("LlaveGas1")



###puerta trampa gas

puertagas=Doors.CreateDoor("Puertagas", (325000,10000,-203000), (0,-1,0), 0, 6100, Doors.OPENED)


puertagas.opentype=Doors.UNIF
puertagas.o_med_vel=-1500
puertagas.o_med_displ=6100


puertagas.closetype=Doors.UNIF
puertagas.c_med_vel=5000
puertagas.c_med_displ=6100


#----------------------------------------------------

LlaveGas=Bladex.CreateEntity("GoldKey","Llavecobox",325790.258850,8967.515210,-207507.532230)
LlaveGas.Static=0
LlaveGas.Scale=1.361327
LlaveGas.Orientation=0.989348,-0.000972,-0.145522,-0.003460
darfuncs.SetHint(LlaveGas,"Atysi Key")
Stars.Twinkle("GoldKey")

p1=Bladex.CreateEntity(Bladex.GenerateEntityName(),"Lanzapivotes",330869.901000,8755.472000,-206121.342000)
p1.Solid=0
p1.Scale=2.625265
p1.Orientation=0.500000,0.500000,0.500000,-0.500000


p2=Bladex.CreateEntity(Bladex.GenerateEntityName(),"Lanzapivotes",330897.009000,8758.668000,-208509.195000)
p2.Solid=0
p2.Scale=2.651518
p2.Orientation=0.508650,0.508650,0.491198,-0.491198


p3=Bladex.CreateEntity(Bladex.GenerateEntityName(),"Lanzapivotes",320906.051000,8750.892000,-208504.262000)
p3.Solid=0
p3.Scale=2.678033
p3.Orientation=0.495618,0.495618,-0.504344,0.504344


p4=Bladex.CreateEntity(Bladex.GenerateEntityName(),"Lanzapivotes",320892.621000,8753.158000,-206128.294000)
p4.Solid=0
p4.Scale=2.651518
p4.Orientation=0.482246,0.482246,-0.517145,0.517145



Gas1 = CreateGas(322500,8600,-206000,0)
Gas2 = CreateGas(322500,8600,-208500,0)
Gas3 = CreateGas(329000,8600,-206000,0)
Gas4 = CreateGas(329000,8600,-208500,0)



GasCounter = 0

SetGasSpeed(0)

Bladex.CreateTimer("GasTimer",0.05)

sectOutGas=Bladex.GetSector(324467.8, 8677.1, -211230.1)






Ontake.AddOnTakeEvent("GoldKey",StartSecuence0)

# punto para tomar el sector
# (324467.8, 8677.1, -211230.1)


CreaOrco(1,325753+800, -1000, -211227,0)
CreaOrco(0,325753-600, -1000, -211227,0)



_OrcoFuckOff=Bladex.CreateSound("../../Sounds/esfuerzo-orco-golpe-cabeza.wav","OrcoFuckOff")
_OrcoFuckOff.MinDistance=10000.0
_OrcoFuckOff.MaxDistance=100000.0

_OrcoDancing=Bladex.CreateSound("../../Sounds/esfuerzo-orco-corto-6.wav","OrcoDancing")
_OrcoDancing.MinDistance=10000.0
_OrcoDancing.MaxDistance=100000.0


_GasSound=Bladex.CreateSound("../../Sounds/woodenplatform-loop.wav","GasSound")
_GasSound.MinDistance=10000.0
_GasSound.MaxDistance=100000.0



####################################
#     --------------               #
#    ( Codemonsters )              #
#     --------------               #
#        because Rebel Act rulez   #
####################################


darfuncs.EnterSecEvent(330967, 13929, -215231,CaeElOtroIdiota)

darfuncs.EnterSecEvent(328410, 11029, -195085,CaeElOtroIdiota)

darfuncs.EnterSecEvent(321186, 8930, -225628,CaeElOtroIdiota)

darfuncs.EnterSecEvent(339271, 8623, -233775,MuestraPobreIdiota0)

#sectoractivagas=Bladex.GetSector(330151, 8942, -234932)
#sectoractivagas.OnEnter=iniciagas

darfuncs.EnterSecEvent(330151,  8942, -234932,iniciagas)
darfuncs.EnterSecEvent(349986, 15874, -229334,iniciagas)

#sectoractivagas2=Bladex.GetSector(349986, 15874, -229334)
#sectoractivagas2.OnEnter=iniciagas


#sectordesactivagas=Bladex.GetSector(318247, 9180, -234475)
#sectordesactivagas.OnEnter=finalizagas


import darfuncs
CreaPobreIdiota()
CreaPobreIdiota0()