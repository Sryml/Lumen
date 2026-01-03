import Bladex
import EnmGenRnd
import AuxFuncs
import ReadGSFile
import Doors
import Button
import Sounds
import Breakings
import Actions
import EnemyTypes

#####################################################
####### PUERTA A LOS MONOLITOS del final  ###########

piedradesliz1=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "MaderaDesliz")
piedradesliz1.MaxDistance=35000
piedradesliz1.MinDistance=5000
piedradesliz1.Volume=1.0

piedragolpe1=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "MaderaGolpe")
piedragolpe1.MaxDistance=30000
piedragolpe1.MinDistance=5000
piedragolpe1.Volume=1.0

ptatrampa=Doors.CreateDoor("ptatrampa", (125000,-55000,170500), (0,-1,0), 0, 5300, Doors.CLOSED)
ptatrampa.Squezze = 1

ptatrampa.opentype=Doors.UNIF
ptatrampa.o_med_vel=-500
ptatrampa.o_med_displ=5000

ptatrampa.closetype=Doors.AC
ptatrampa.c_init_displ=5000
ptatrampa.c_med_vel=9000

ptatrampa.SetWhileOpenSound(piedradesliz1)
ptatrampa.SetEndOpenSound(piedragolpe1)
ptatrampa.SetWhileCloseSound(piedradesliz1)
ptatrampa.SetEndCloseSound(piedragolpe1)

o=Bladex.CreateEntity("pedroloco2","Bloque",177106.956739,-50518.341847,167128.569178)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
darfuncs.SetHint(o,"Trigger")


button2=Button.CreateButtonCombination(0,Abrepta,"")
button2.AddButton("pedroloco2",3,(1,0,0),400,0,0,1)


##########################################################
#######	PUERTA DE LA TRAMPA DE LAS TUMBAS DEL FINAL  #####
#de entrada
piedradesliz2=Sounds.CreateEntitySound("../../Sounds/puerta-pie-cerr-no-loop-rebote.wav", "MaderaDesliz")
piedradesliz2.MaxDistance=30000
piedradesliz2.MinDistance=3000
piedradesliz2.Volume=1.0

piedragolpe2=Sounds.CreateEntitySound("../../Sounds/Blade-menu-hit.wav", "MaderaGolpe")
piedragolpe2.MaxDistance=30000
piedragolpe2.MinDistance=3000
piedragolpe2.Volume=1.0

ptatrampa2=Doors.CreateDoor("ptatrampa2", (158750,-51000,159125), (0,1,0), 0, 3300, Doors.OPENED)
ptatrampa2.Squezze = 1

ptatrampa2.opentype=Doors.UNIF
ptatrampa2.o_med_vel=-1000
ptatrampa2.o_med_displ=3300
ptatrampa2.closetype=Doors.AC
ptatrampa2.c_init_displ=3300
ptatrampa2.c_med_vel=8000
ptatrampa2.OnEndCloseFunc = LineaPolvoGen
ptatrampa2.SetWhileOpenSound(piedradesliz2)
ptatrampa2.SetEndOpenSound(piedragolpe2)
ptatrampa2.SetWhileCloseSound(piedradesliz2)
ptatrampa2.SetEndCloseSound(piedragolpe2)



####### PUERTA DEL PULSADOR   ###########
#alpulsador
piedradesliz3=Sounds.CreateEntitySound("../../Sounds/puerta-pie-desliz-no-loop.wav", "MaderaDesliz")
piedradesliz3.MaxDistance=30000
piedradesliz3.MinDistance=3000
piedradesliz3.Volume=1.0

piedragolpe3=Sounds.CreateEntitySound("../../Sounds/Blade-menu-hit.wav", "MaderaGolpe")
piedragolpe3.MaxDistance=30000
piedragolpe3.MinDistance=3000
piedragolpe3.Volume=1.0

ptatrampa3=Doors.CreateDoor("ptatrampa3", (170625,-52000,167125), (0,1,0), 0, 4300, Doors.CLOSED)

ptatrampa3.opentype=Doors.UNIF
ptatrampa3.o_med_vel=-1000
ptatrampa3.o_med_displ=4300
ptatrampa3.closetype=Doors.AC
ptatrampa3.c_init_displ=4300
ptatrampa3.c_med_vel=6000
ptatrampa3.SetWhileOpenSound(piedradesliz3)
ptatrampa3.SetEndOpenSound(piedragolpe3)
ptatrampa3.SetWhileCloseSound(piedradesliz3)
ptatrampa3.SetEndCloseSound(piedragolpe3)


res=ReadGSFile.ReadGhostSectorFile("trampatumba.sf")

for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

res=ReadGSFile.ReadGhostSectorFile("EXTERIOR.sf")

for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

char.SendTriggerSectorMsgs=1



CreateArenilla(55,42,42)


Bladex.AddParticleGType("Tierra3","GenericParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	aux=(60-i)/60
	r=40
	g=30
	b=0
	a=255*(1.0-aux/2.0)
	size=60.0*(1.0-aux)
	Bladex.SetParticleGVal("Tierra3",i,r,g,b,a,size)



Bladex.SetTriggerSectorFunc("Trampatumb", "OnEnter", ActivateTrampaTumba)
Bladex.SetTriggerSectorFunc("EXTSF4", "OnEnter", ActivateTrampaTumbaCircular)


#################   TRAMPA AL FINAL DENTRO DE LA TUMBA   #######

generadorT1           = EnmGenRnd.CreateEnemiesGenerator(5, 2)
generadorT1.Level=1
generadorT1.VirGenPos = 158000,-50000,165000
generadorT1.CallBak   = CBgeneradorT1

generadorT1.AddPoint((158000,-48000,165000),("m1Gen11Skl_1", "Skeleton", "Hacha", 0, "Escudo5", 1), "Skl_appears1",3)
generadorT1.AddPoint((163250,-48000 + 300,162000),("m1Gen11Ork_2", "Skeleton", "Maza", 0, "Escudo5", 1), "Skl_appears1",3)
generadorT1.AddPoint((161000,-48000,167000),("m1Gen11Skl_3", "Skeleton", "Maza", 0, "Escudo2", 1), "Skl_appears1",3)
generadorT1.AddPoint((159000,-48000 + 300,171000),("m1Gen11Ork_4", "Skeleton", "Maza", 0, "Escudo1", 1), "Skl_appears1",3)
generadorT1.AddPoint((164000,-48000,169000),("m1Gen11Skl_5", "Skeleton", "Gladius", 0, "Escudo2", 1), "Skl_appears1",3)
#generadorT1.AddPoint((166000,-48000 + 300,165000),("m1Gen11Ork_6", "Skeleton", "Garrote", 0, "Escudo2", 1), "Lch_appears1",1)

generadorT1.InitGenFunc=SaltaTierraGen
generadorT1.FinishGenFunc=Abrepta3
generadorT1.DifTime = 0.6
generadorT1.Activate()

#############	PRIMER GENERADOR TRAS LAS BOLAS ######################

generadorT2 = EnmGenRnd.CreateEnemiesGenerator(4, 2)
generadorT2.Level=1
generadorT2.VirGenPos = 68500,-51800,108500
generadorT2.CallBak = CBgeneradorT2

generadorT2.AddPoint((68500,-50800,108500),("m1Gen12Skl_1", "Skeleton", "Hacha", 0, "Escudo2", 1), "Skl_appears1",2)
generadorT2.AddPoint((73000,-50800 + 300,112500),("m1Gen12Ork_2", "Lich", "Garrote", 0, "Escudo5", 1), "Lch_appears1",0)
generadorT2.AddPoint((68000,-50800,112750),("m1Gen12Skl_3", "Skeleton", "Hacha", 0, "Escudo2", 1), "Skl_appears1",2)
generadorT2.AddPoint((64500,-50800 + 300,118500),("m1Gen12Ork_4", "Lich", "Hacha", 0, "Escudo5", 1), "Lch_appears1",0)
generadorT2.AddPoint((64750,-50800,114750),("m1Gen12Skl_5", "Lich", "Garrote", 0, "Escudo5", 1), "Lch_appears1",0)
generadorT2.AddPoint((71500,-50800 + 300,115500),("m1Gen12Ork_6", "Lich", "Hacha", 0, "Escudo5", 1), "Lch_appears1",0)

generadorT2.InitGenFunc=SaltaTierraGen
generadorT2.Activate()




monolitoenm1 = EnmGenRnd.CreateEnemy((157500,-49400,145000),"monolitoenm1", "Lich", "Hacha", 0, "Escudo5", 1)
monolitoenm1.ActionAreaMin=pow(2,2)
monolitoenm1.ActionAreaMax=pow(2,1)
monolitoenm2 = EnmGenRnd.CreateEnemy((160000,-49400,152500),"monolitoenm2", "Lich", "Hacha", 0, "Escudo5", 1)
monolitoenm2.ActionAreaMin=pow(2,2)
monolitoenm2.ActionAreaMax=pow(2,1)
monolitoenm3 = EnmGenRnd.CreateEnemy((133500,-49400,156500),"monolitoenm3", "Lich", "Hacha", 0, "Escudo5", 1)
monolitoenm3.ActionAreaMin=pow(2,2)
monolitoenm3.ActionAreaMax=pow(2,1)
monolitoenm4 = EnmGenRnd.CreateEnemy((144000,-49400,155000),"monolitoenm4", "Lich", "Hacha", 0, "Escudo5", 1)
monolitoenm4.ActionAreaMin=pow(2,2)
monolitoenm4.ActionAreaMax=pow(2,1)


###########  PRIMER GENERADOR EN EL PUEBLO #########
generadorT3 = EnmGenRnd.CreateEnemiesGenerator(6, 2)
generadorT3.Level=1
generadorT3.VirGenPos = 167020, -49627, 164713
generadorT3.CallBak = CBgeneradorT3

generadorT3.AddPoint((-184500,-9500,173000),("m1Gen32Skl_1", "Lich", "Garrote", 0, "Escudo5", 1), "Lch_appears1",0)
generadorT3.AddPoint((-175500,-9500,159000),("m1Gen32Ork_2", "Lich", "", 0, "", 0), "Lch_appears1",0)
generadorT3.AddPoint((-186000,-9500,158000),("m1Gen32Skl_3", "Lich", "Garrote", 0, "", 0), "Lch_appears1",0)
generadorT3.AddPoint((-184000,-9500,174000),("m1Gen32Skl_4", "Lich", "", 0, "", 0), "Lch_appears1",0)
generadorT3.AddPoint((-182000,-9500,152000),("m1Gen32Skl_5", "Lich", "", 0, "", 0), "Lch_appears1",0)
generadorT3.AddPoint((-177000,-9500,166500),("m1Gen32Skl_6", "Lich", "Hacha", 0, "", 0), "Lch_appears1",0)

generadorT3.InitGenFunc=SaltaTierraGen
generadorT3.Activate()


###SEGUNDO GENERADOR DEL PUEBLO
#segunda plataforma
generadorT4 = EnmGenRnd.CreateEnemiesGenerator(4, 1)
generadorT4.Level=1
generadorT4.VirGenPos = -172000,-13500,193000
generadorT4.CallBak = CBgeneradorT4

generadorT4.AddPoint((-172000,-11500,193000),("m1Gen42Skl_1", "Lich", "Hacha", 0, "", 0), "Lch_appears1",0)
generadorT4.AddPoint((-163000,-11500,180000),("m1Gen42Ork_2", "Lich", "", 0, "Escudo2", 1), "Lch_appears1",0)
generadorT4.AddPoint((-162000,-11500,191000),("m1Gen42Ork_3", "Lich", "Garrote", 0, "Escudo5", 1), "Lch_appears1",0)
generadorT4.AddPoint((-170000,-11500,186000),("m1Gen42Ork_4", "Lich", "", 0, "", 0), "Lch_appears1",0)

generadorT4.InitGenFunc=SaltaTierraGen
generadorT4.Activate()

###	tercera plataforma
generadorT5 = EnmGenRnd.CreateEnemiesGenerator(6, 3)
generadorT5.Level=1
generadorT5.VirGenPos = -177000,-16500,215000
generadorT5.CallBak = CBgeneradorT5

generadorT5.AddPoint((-177000,-14500,215000),("m1Gen52Skl_1", "Lich", "Hacha", 0, "Escudo5", 1), "Lch_appears1",0)
generadorT5.AddPoint((-181000,-14500,221000),("m1Gen52Skl_2", "Lich", "Garrote", 0, "", 0), "Lch_appears1",0)
generadorT5.AddPoint((-175000,-14500,209000),("m1Gen52Skl_3", "Lich", "", 0, "", 0), "Lch_appears1",1)
generadorT5.AddPoint((-186500,-14500,200500),("m1Gen52Skl_4", "Lich", "Hacha", 0, "Escudo2", 1), "Lch_appears1",0)
generadorT5.AddPoint((-173000,-14500,200500),("m1Gen52Skl_5", "Lich", "", 0, "Escudo5", 1), "Lch_appears1",1)
generadorT5.AddPoint((-182000,-14500,213000),("m1Gen52Skl_6", "Lich", "Hacha", 0, "", 0), "Lch_appears1",1)

generadorT5.InitGenFunc=SaltaTierraGen
generadorT5.Activate()



SecGen3 = Bladex.GetSector(-181000,-12000,155000)
SecGen3.OnEnter = ActivateGen3

SecGen4 = Bladex.GetSector(-172000,-15000,193000)
SecGen4.OnEnter = ActivateGen4

SecGen5 = Bladex.GetSector(-180500,-18000,203000)
SecGen5.OnEnter = ActivateGen5