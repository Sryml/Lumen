import Bladex
import dust
import darfuncs
import ReadGSFile

Lucex=Bladex.CreateEntity("hkgfoweua","Entity Spot",-62843, 19379, -37748)
Lucex.Color=251,159,30
Lucex.Intensity=15
Lucex.Precission=0.1
Lucex.CastShadows=1
Lucex.Visible=0
Lucex.Flick=1

RodFire=Bladex.CreateEntity("cyioj", "Entity Particle System D1", -62843, 19679, -37748)
RodFire.ParticleType="Flame"
RodFire.YGravity=-4000.0
RodFire.Friction=0.12
RodFire.PPS=100
RodFire.Velocity= 0.0, -2000.0, 0.0
RodFire.Time2Live=15
RodFire.RandomVelocity=45


###	EN TEMPLO INTERIOR

Lucesub2=Bladex.CreateEntity("lucesub2","Entity Spot",-24875, 9500, 40250)
Lucesub2.Color=251,159,30
Lucesub2.Intensity=1
Lucesub2.Precission=0.1
Lucesub2.CastShadows=0
Lucesub2.Visible=1
Lucesub2.Flick=1

subFire2=Bladex.CreateEntity("subfire2", "Entity Particle System D1", -24875, 10230, 40250)
subFire2.ParticleType="LargeFire"
subFire2.YGravity=-4000.0
subFire2.Friction=0.12
subFire2.PPS=100
subFire2.Velocity= 0.0, -500.0, 0.0
subFire2.Time2Live=32
subFire2.RandomVelocity=40




fsa = dust.RemueveTierraGen(-54250,-300,750  ,900,750, 256, "LargeFire",32,-1)

fsa[0].YGravity=-4000.0
fsa[1].YGravity=-4000.0
fsa[1].Velocity= 0.0, -500.0, 0.0
# fsa[0].SubscribeToList("Pin") fsa[1].SubscribeToList("Pin")


##########################################################################################3
##
##		para que quemen los fuegos


import darfuncs
import ReadGSFile
# leer los sectores fantasma

res=ReadGSFile.ReadGhostSectorFile("fuegos.sf")
for igs in res:
   Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

# asignarles el fuego
darfuncs.FireOnGS("Fuego1")
darfuncs.FireOnGS("Fuego2")
darfuncs.FireOnGS("Fuego3")
darfuncs.FireOnGS("Fuego4")
darfuncs.FireOnGS("Fuego5")