import Bladex
import Sounds
import Objects
import Levers


MESSAGE_START_WEAPON=7
MESSAGE_STOP_WEAPON=8



########################################
#     Pincho de la entrada secreta     #
########################################


pinchodeslizando=Sounds.CreateEntitySound("../../Sounds/pincho-desliz.wav", "PinchoDeslizando")
pinchogolpeando=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "PinchoGolpeando")

pincholab=Bladex.CreateEntity("PinchoLab", "PinchoManuel", 3622.0, -29950.0, 65972.0, "Weapon")
pincholab.Scale=1.5
pincholab.Orientation=0.500000,0.500000,0.500000,0.500000
pincholab.Solid=0
pincholab.Frozen=1

pincholabdin=Objects.CreateDinamicObject("PinchoLab")

pincholabactivado=0

######## Funcion: Solidifica(pincho)

######## Funcion: LanzaPinchoLab()

######## Funcion: RecogePinchoLab()

######## Funcion: ActivaPinchoLab()

######## Funcion: DesactivaPinchoLab()

palancalab=Levers.PlaceLever("PalancaLab", Levers.LeverType3, (403.5, -33250.0, 74416.5), (0.067773, 0.067773, 0.703851, -0.703851), 1.0)
palancalab.mode=0

palancalab.OnTurnOnFunc=ActivaPinchoLab
palancalab.OnTurnOnArgs=()

palancalab.OnTurnOffFunc=DesactivaPinchoLab
palancalab.OnTurnOffArgs=()




######################################
#     Pinchos del derrumbamiento     #
######################################


o=Bladex.CreateEntity("PinchoDerr0","PinchoMiguel",-65597.479000,-27025.412000,3922.220000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000

o=Bladex.CreateEntity("PinchoDerr1","PinchoMiguel",-65559.287000,-26879.311000,4617.535000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.683013,0.683013,0.183013,-0.183013

o=Bladex.CreateEntity("PinchoDerr2","PinchoMiguel",-64802.149000,-27031.581000,4175.198000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.579228,0.579228,0.405580,-0.405580

o=Bladex.CreateEntity("PinchoDerr3","PinchoMiguel",-65098.327000,-27028.638000,3375.139000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.696364,0.696364,0.122788,-0.122788

o=Bladex.CreateEntity("PinchoDerr4","PinchoMiguel",-64405.502000,-26879.595000,3535.985000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000

o=Bladex.CreateEntity("PinchoDerr5","PinchoMiguel",-65530.988000,-27026.168000,2804.991000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000

o=Bladex.CreateEntity("PinchoDerr6","PinchoMiguel",-66014.803000,-26931.553000,3489.081000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.627211,0.627211,0.326506,-0.326506

o=Bladex.CreateEntity("PinchoDerr7","PinchoMiguel",-66270.203000,-27031.655000,4290.241000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000

o=Bladex.CreateEntity("PinchoDerr8","PinchoMiguel",-66939.429000,-26878.060000,4390.847000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.683013,0.683013,0.183013,-0.183013

o=Bladex.CreateEntity("PinchoDerr9","PinchoMiguel",-66689.402000,-27028.570000,3617.713000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000

o=Bladex.CreateEntity("PinchoDerr10","PinchoMiguel",-66143.253000,-27027.938000,2869.647000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000

o=Bladex.CreateEntity("PinchoDerr11","PinchoMiguel",-66461.873000,-27029.513000,2164.899000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.541675,0.541675,0.454519,-0.454519

o=Bladex.CreateEntity("PinchoDerr12","PinchoMiguel",-66937.450000,-26926.265000,2915.361000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.683013,0.683013,0.183013,-0.183013

o=Bladex.CreateEntity("PinchoDerr13","PinchoMiguel",-67392.858000,-27027.810000,3888.002000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000


### Muerte al caer en los pinchos del derrumbamiento

######## Funcion: MuertePinchos(trsector_name, entity_name)

Bladex.SetTriggerSectorFunc("TrampaPinchos", "OnEnter", MuertePinchos)
