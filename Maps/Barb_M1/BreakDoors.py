import EnmGenRnd
import ReadGSFile
import Actions


res=ReadGSFile.ReadGhostSectorFile("rompepuertas.sf")

for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

Bladex.SetTriggerSectorFunc("casaredonda", "OnEnter", LichBreakDoor)
Bladex.SetTriggerSectorFunc("casa3pisos", "OnEnter", LichBreakDoor2)


b1 = SetupBreakSector((-137250,-25000,173125),(-138000,-25000,173500),(-1,0,0),3,(100,0,0),(0,2000,0),(0,0,500))
b1.ActivatePolvo((-137550,-23700,174375),(-137550,-28000,174375), (-138000,-23700,171875),(-138000,-28000,171875),(300,0,0))

b2 = SetupBreakSector((-150625,-21000,172000),(-150250,-21000,171000),(-1,0,0),1,(100,0,0),(0,2000,0),(0,0,500))
b3 = SetupBreakSector((-150625,-21000,171000),(-150250,-21000,171000),(-1,0,0),1,(100,0,0),(0,2000,0),(0,0,500))
b3.ActivatePolvo((-149800,-19500,172250),(-149800,-23000,172250), (-149800,-19500,169750),(-149800,-2300,169750),(-800,0,0))

#doorenm1 = EnmGenRnd.CreateEnemy((-152000,-20300,171500),"Gen11Lich_07", "Lich", "Hacha5", 0, "Escudo5", 1)

Espada20=Bladex.CreateEntity("m1doorenm1Espada","Hacha5",0,0,0,"Weapon")
escudo20=Bladex.CreateEntity("m1doorenm1Escudo","Escudo5",0,0,0)
Sparks.MakeShield("m1doorenm1Escudo")
Breakings.SetBreakableWS("m1doorenm1Escudo")
Breakings.SetBreakableWS("m1doorenm1Espada")

pers=Bladex.CreateEntity("doorenm1","Lich",-152000,-20300,171500,"Person")
pers.Angle = 4.6
pers.Level=0
Actions.TakeObject(pers.Name,"m1doorenm1Espada")
Actions.TakeObject(pers.Name,"m1doorenm1Escudo")
pers.ActionAreaMin=pow(2,15)
pers.ActionAreaMax=pow(2,15)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()



b4 = SetupBreakSector((-175000,-15000,185750),(-174750,-15000,186000),(1,0,0),0,(100,0,0),(0,2000,0),(0,0,500))
b4.ActivatePolvo((-175500,-12800,187500),(-175500,-17000,187500), (-174500,-17000,184500),(-174500,-12800,184500),(-300,0,0))

b5 = SetupBreakSector((-149250,-21000,201000),(-149250,-21000,201000),(1,0,0),0,(100,0,0),(0,2000,0),(0,0,500))
b5.ActivatePolvo((-149500,-19400,202500),(-149500,-23400,202500), (-149625,-19400,200000),(-149625,-23400,200000),(300,0,0))

#doorenm2 = EnmGenRnd.CreateEnemy((-148200,-20490,201100),"Gen11Lich_08", "Lich", "Hacha5", 0, "Escudo5", 1)

Espada20=Bladex.CreateEntity("m1doorenm2Espada","Hacha5",0,0,0,"Weapon")
escudo20=Bladex.CreateEntity("m1doorenm2Escudo","Escudo5",0,0,0)
Sparks.MakeShield("m1doorenm2Escudo")
Breakings.SetBreakableWS("m1doorenm2Escudo")
Breakings.SetBreakableWS("m1doorenm2Espada")

pers=Bladex.CreateEntity("doorenm2","Lich",-148200,-20490,201100,"Person")
pers.Angle = 1.6
pers.Level=0
Actions.TakeObject(pers.Name,"m1doorenm2Espada")
Actions.TakeObject(pers.Name,"m1doorenm2Escudo")
pers.ActionAreaMin=pow(2,15)
pers.ActionAreaMax=pow(2,15)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()