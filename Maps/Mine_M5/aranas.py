
#########################################################
#														#
# Ara�as					(3 ara�as y 3 camaras )		#
#														#
# (Yuio)												#
#														#
#########################################################

import Bladex
import Sounds

import Reference
import Select
import Change
import Actions
import Bladex
import EnemyTypes
import darfuncs

SoundDesliz=Sounds.CreateEntitySound('../../sounds/M-desliz-arana.wav', 'SoundDesliz')
SoundDesliz.Volume = 1.0
SoundDesliz.MinDistance=15000
SoundDesliz.MaxDistance=30000

SoundCaida1=Sounds.CreateEntitySound('../../sounds/M-paso3tie.wav', 'SoundGolpe')
SoundCaida1.Volume = 1.0
SoundCaida1.MinDistance=5000
SoundCaida1.MaxDistance=10000

SoundCaida2=Sounds.CreateEntitySound('../../sounds/M-paso3tie.wav', 'SoundGolpe')
SoundCaida2.Volume = 1.0
SoundCaida2.MinDistance=5000
SoundCaida2.MaxDistance=10000

SoundCaida3=Sounds.CreateEntitySound('../../sounds/M-paso3tie.wav', 'SoundGolpe')
SoundCaida3.Volume = 1.0
SoundCaida3.MinDistance=5000
SoundCaida3.MaxDistance=10000


########################## ghost sector para la deteccion del inicio de la animacion #######

res=ReadGSFile.ReadGhostSectorFile("arana.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

char.SendTriggerSectorMsgs=1
#esp=Bladex.GetEntity("WeaponInvPrb1")
#esp.SendTriggerSectorMsgs=1

########################## las 3 ara�as-actor #############################################


#char.Position=-124953.977,-19139.791+2000,-34780.535+2000

spiderA = Bladex.CreateEntity("spiderA","Spidersmall",char.Position[0],char.Position[1],char.Position[2])
spiderA.Position=char.Position
spiderA.Person = 1
darfuncs.HideBadGuy(spiderA.Name)

spiderB = Bladex.CreateEntity("spiderB","Spidersmall",char.Position[0],char.Position[1],char.Position[2])
spiderB.Position=char.Position
spiderB.Person = 1
darfuncs.HideBadGuy(spiderB.Name)

spiderC = Bladex.CreateEntity("spiderC","Spidersmall",char.Position[0],char.Position[1],char.Position[2])
spiderC.Position=char.Position
spiderC.Person = 1
darfuncs.HideBadGuy(spiderC.Name)



####################### start play ########################################################

smallSpidersScene = 0


#Bladex.CreateEntity("torcha","Antorcha",-128110.203, -19178, -34928.453)
Bladex.SetTriggerSectorFunc("arana", "OnEnter", startSpiderScenePlay )
