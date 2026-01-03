
#########################################################
#														#
# Elevador con Orko										#
#														#
# (Yuio)												#
#														#
#########################################################

import Doors
import Objects
import Sounds
import Levers
import Actions



################ ELEVADOR

o=Bladex.CreateEntity("OrcElev","PlataformaRail",-95328.082590,-14455.634799,-21039.515953)
o.Static=1
o.Scale=1.69527
o.Orientation=0.707107,0.707107,0.000000,0.000000

oElev=Objects.CreateDinamicObject("OrcElev")

loopelevador=Sounds.CreateEntitySound("../../Sounds/drawbridge-loop.wav", "LoopElevador")
golpeelevador=Sounds.CreateEntitySound("../../Sounds/metal-lever3.wav", "GolpeElevador")



################ COLUMNAS

colA = Doors.CreateDoor("OElevColA", (-94000,-20000,-21000), (0, -1, 0), 0, 11000, Doors.OPENED)
colA.opentype=Doors.AC_UNIF_DEC
colA.o_init_vel=0
colA.o_init_displ=500
colA.o_med_vel=-2000
colA.o_med_displ=10000
colA.o_end_vel=0
colA.o_end_displ=500
colA.closetype=Doors.AC_UNIF_DEC
colA.c_init_vel=0
colA.c_init_displ=500
colA.c_med_vel=5000
colA.c_med_displ=10000
colA.c_end_vel=0
colA.c_end_displ=500

colB = Doors.CreateDoor("OElevColB", (-96500,-20000,-21000), (0, -1, 0), 0, 11000, Doors.OPENED)
colB.opentype=Doors.AC_UNIF_DEC
colB.o_init_vel=0
colB.o_init_displ=500
colB.o_med_vel=-2000
colB.o_med_displ=10000
colB.o_end_vel=0
colB.o_end_displ=500
colB.closetype=Doors.AC_UNIF_DEC
colB.c_init_vel=0
colB.c_init_displ=500
colB.c_med_vel=3000
colB.c_med_displ=10000
colB.c_end_vel=0
colB.c_end_displ=500




################ CODIGO

oelInUse=0
orcOut=1



################ ASIGNACION DE EVENTOS

oelevDn=Levers.PlaceLever("OrcElevLevUp", Levers.LeverType3, (-92522.513557,-15488.607434,-20959.660403), (0.504344,0.504344,0.495618,-0.495618), 1.0)
oelevDn.mode=1
oelevDn.OnTurnOnFunc=upOElev
oelevDn.OnTurnOnArgs=()

oelevUp=Levers.PlaceLever("OrcElevLevDn", Levers.LeverType3, (-90505.406455,-26888.904306,-16908.808422), (0.707107,0.707107,0.000000, 0.000000), 1.0)
oelevUp.mode=1
oelevUp.OnTurnOnFunc=upOElev
oelevUp.OnTurnOnArgs=()
"""
orcElevSector=Bladex.GetSector(-83000,-27500,-21000)
orcElevSector.OnEnter=runOrcAndElev
"""