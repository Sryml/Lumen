import Doors
import Sounds


maderadeslizk=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-deslizando-2.wav", "MaderaDesliz")
maderadeslizk.MaxDistance=20000
maderadeslizk.MinDistance=1000
maderadeslizk.Volume=1.0

maderagolpek=Sounds.CreateEntitySound("../../Sounds/M-CIERRE-GATE.wav", "MaderaGolpe")
maderagolpek.MaxDistance=25000
maderagolpek.MinDistance=2000
maderagolpek.Volume=1.0
#1
Puerta1Pulsa=Doors.CreateDoor("Puerta1Pulsa", (-55000,-10000,-81900), (0,1,0), 0, 4000, Doors.CLOSED)
Puerta1Pulsa.opentype=Doors.UNIF
Puerta1Pulsa.o_med_vel=-400
Puerta1Pulsa.o_med_displ=4000

Puerta1Pulsa.closetype=Doors.AC
Puerta1Pulsa.c_med_vel=400
Puerta1Pulsa.c_init_displ=4000


Puerta1Pulsa.SetWhileOpenSound(maderadeslizk)
Puerta1Pulsa.SetEndOpenSound(maderagolpek)





#oco1=Bladex.CreateEntity("PuCombi1","Bloque",-39502.664977,-9321.878672,-81612.478760)
oco1=Bladex.CreateEntity("PuCombi1","AdoquinRuna",-39502.664977,-9321.878672,-82100.0)
oco1.Static=0
oco1.Scale=1
oco1.ExclusionGroup=1
oco1.Orientation=0.500000,0.500000,-0.500000,0.500000
darfuncs.SetHint(oco1,"Trigger")

#oco2=Bladex.CreateEntity("PuCombi2","Bloque",-38519.195205,-9321.801077,-81588.524726)
oco2=Bladex.CreateEntity("PuCombi2","AdoquinRuna",-38519.195205,-9321.801077,-82100.0)
oco2.Static=0
oco2.Scale=1
oco2.ExclusionGroup=1
oco2.Orientation=0.500000,0.500000,-0.500000,0.500000
darfuncs.SetHint(oco2,"Trigger")

#oco3=Bladex.CreateEntity("PuCombi3","Bloque",-37566.578113,-9319.309549,-81624.586320)
oco3=Bladex.CreateEntity("PuCombi3","AdoquinRuna",-37566.578113,-9319.309549,-82100.0)
oco3.Static=0
oco3.Scale=1
oco3.ExclusionGroup=1
oco3.Orientation=0.500000,0.500000,-0.500000,0.500000
darfuncs.SetHint(oco3,"Trigger")


CoButton = Button.CreateButtonCombination(1,AbrirPuerta,ResetCombinado)
CoButton.AddButton("PuCombi1",2,(0,0,-1),400,1,0,0)
CoButton.AddButton("PuCombi2",2,(0,0,-1),400,3,0,0)
CoButton.AddButton("PuCombi3",2,(0,0,-1),400,2,0,0)
