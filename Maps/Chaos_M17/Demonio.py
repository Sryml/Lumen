import Sounds
import Doors
import Reference
import PhantonFX
import EnemyTypes
########################################################################

_SndLdm1=Bladex.CreateSound("../../Sounds/yeti-growl.wav","SndLdm1")
_SndLdm1.MinDistance= 500000
_SndLdm1.MaxDistance=5000000

_SndLdm2=Bladex.CreateSound("../../Sounds/yeti-growl2.wav","SndLdm2")
_SndLdm2.MinDistance= 500000
_SndLdm2.MaxDistance=5000000

_SndLdmOstia=Bladex.CreateSound("../../Sounds/deputamadre.wav","SndLdmOstia")
_SndLdmOstia.MinDistance= 500000
_SndLdmOstia.MaxDistance=5000000

Bladex.AddParticleGType("Energia3","GenericParticle",B_PARTICLE_GTYPE_ADD,80)

for i in range(80):
	if i>60:
		traux=1-((i-60.0)/20.0) #va de 0 a 1
	elif i<20:
		traux=i/20.0 #va de 1 a 0
	else:
		traux=1.0
	r=255
	g=80
	b=100
	a=255.0*traux
	size=20.0
	Bladex.SetParticleGVal("Energia3",i,r,g,b,a,size)


Bladex.AddParticleGType("Energia2","GenericParticle",B_PARTICLE_GTYPE_ADD,120)

for i in range(120):
	if i>90:
		traux=1-((i-90.0)/30.0) #va de 0 a 1
	elif i<20:
		traux=i/20.0 #va de 1 a 0
	else:
		traux=1.0
	r=100
	g=100
	b=255
	a=255.0*traux
	size=20.0
	Bladex.SetParticleGVal("Energia2",i,r,g,b,a,size)


Bladex.AddParticleGType("FuegoInvocacion","FireParticle",B_PARTICLE_GTYPE_ADD,120)

for i in range(120):
	if i<40:
		traux=i/40.0 #va de 1 a 0
	else:
		traux=1.0
	r=150
	g=100
	b=255
	a=255.0*traux
	size=400.0
	Bladex.SetParticleGVal("FuegoInvocacion",i,r,g,b,a,size)

NumDemMuer = 2


insecDem2       = 0
secDem2         = Bladex.GetSector(476347.827342, 84085.2, 21154.9966901)

secDem2.OnEnter = InCoso
secDem2.OnLeave = OutCoso

CreacionDemonio("uno")
CreacionDemonio("dos")


######################################################################################
bigdoori= Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav",    "Bigdoori")
bigdoori.MaxDistance=50000
bigdoori.MinDistance=15000
bigdoori.Volume=1.0

finbigdoori= Sounds.CreateEntitySound("../../Sounds/mechanism8.wav",         "Finbigdoori")
finbigdoori.MaxDistance=50000
finbigdoori.MinDistance=15000
finbigdoori.Volume=1.0



abismoi=Doors.CreateDoor("Abismoi", (476000,84000,14000), (0.707,0,0.707), 0, 3975, Doors.CLOSED)



abismoi.opentype=Doors.UNIF
abismoi.o_med_vel=-800
abismoi.o_med_displ=3975


abismoi.closetype=Doors.UNIF
abismoi.c_med_vel=800
abismoi.c_med_displ=3975


abismoi.SetWhileOpenSound(bigdoori)
abismoi.SetEndOpenSound(finbigdoori)

abismoi.SetWhileCloseSound(bigdoori)
abismoi.SetEndCloseSound(finbigdoori)


##hoja derecha

bigdoord= Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav",    "Bigdoord")
bigdoord.MaxDistance=50000
bigdoord.MinDistance=15000
bigdoord.Volume=1.0

finbigdoord= Sounds.CreateEntitySound("../../Sounds/mechanism8.wav",         "Finbigdoord")
finbigdoord.MaxDistance=50000
finbigdoord.MinDistance=15000
finbigdoord.Volume=1.0


abismod=Doors.CreateDoor("Abismod", (478000,84000,16000), (-0.707,0,-0.707), 0, 3975, Doors.CLOSED)



abismod.opentype=Doors.UNIF
abismod.o_med_vel=-800
abismod.o_med_displ=3975


abismod.closetype=Doors.UNIF
abismod.c_med_vel=800
abismod.c_med_displ=3975


abismod.SetWhileOpenSound(bigdoord)
abismod.SetEndOpenSound(finbigdoord)

abismod.SetWhileCloseSound(bigdoord)
abismod.SetEndCloseSound(finbigdoord)


#funci�n que abre y cierra las hojas de la puerta unisono

import EnemyTypes

######################################################################################


demonio=Bladex.CreateEntity("DemonioMaldito", "Little_Demon", 0, 0, 0,"Person")
demonio.Blind = 1
demonio.Deaf  = 1
demonio.Level=16
demonio.RemoveFromWorld()
EnemyTypes.EnemyDefaultFuncs(demonio)
demonio.ImDeadFunc=MuerteDemonio


ELDEMOSEC=Bladex.GetSector(452518, 83274, 23680)
ELDEMOSEC.OnEnter = ElDemonio