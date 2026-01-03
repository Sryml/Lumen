#################################################
# Bichito zampon que se come la gema
#
# (Yuio) Mas bien conocido como "BugMaker"
#
#################################################


##       _||_
##       -||-
##    ____________
##   /            \
##  |  Aqui yace   |
##  | Yuio Capuio  |
##  |   El mejor   |
##  | Escritor de  |
##  |     Bugs     |
##  |Rest In Pieces|
##  |______________|
##  \***************\
##    \***************\
##      \***************\
##        \***************\


import Reference
import Select
import Doors
import Actions
import Change
import EnemyTypes

import ReadGSFile
import Scorer
import Ontake

res=ReadGSFile.ReadGhostSectorFile("bicho.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

char=Bladex.GetEntity("Player1")
char.SendTriggerSectorMsgs=1

# Bladex.GetEntity("GemaB").Position=char.Position[0] ,char.Position[1],char.Position[2]

############################################################3
#  Sonidos varios
############################################################3

_SndCorreGema=Bladex.CreateSound("../../Sounds/bug-laugh2.wav","Risoto2")
_SndCorreGema.MaxDistance=1000000.0
_SndSorpresaGema=Bladex.CreateSound("../../Sounds/bug-suprise.wav","chauloco")
_SndSorpresaGema.MaxDistance=1000000.0
_SndZampaGema=Bladex.CreateSound("../../Sounds/bugbite-bone.wav","nam")
_SndZampaGema.MaxDistance=1000000.0
_SndMorfaGema=Bladex.CreateSound("../../Sounds/bugbite-bone2.wav","rico")
_SndMorfaGema.MaxDistance=1000000.0
_SndEructaGema=Bladex.CreateSound("../../Sounds/bug-respiracion.wav","breeep")
_SndEructaGema.MaxDistance=1000000.0
_SndEscapaGema=Bladex.CreateSound("../../Sounds/bug-laugh2.wav","hastalavista")
_SndEscapaGema.MaxDistance=1000000.0

################## gema 4 azul ( Por colocar )


gemaBlue=Bladex.CreateEntity("GemaB","Gemaazul",-101863.141,-19350.848,-100658.969)
gemaBlue.RotateRel(0,0,0,1,0,0,1.57)
gemaBlue.Static=1
gemaBlue.Solid=0
gemaBlue.SelfIlum = -1
gemaBlue.Scale=1.082857
luz = Bladex.CreateEntity("GemaBLight","Entity Spot",-101863.141,-19350.848-100,-100658.969)
luz.Color = 74,89,128
luz.Intensity = 4
luz.CastShadows = 0
luz.Precission = 0.06
luz.Visible = 0
luz.Flick = 0

lightTimerStartTimeB=0

Bladex.CreateTimer("BLightTimerB",0.010)


bScenePlayed=0


Bladex.SetTriggerSectorFunc("bicho", "OnEnter", bSceneStart )


#