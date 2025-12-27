#################################################################
###                                                            ##
###  If you cast a spell from the hidden past on the darker    ##
###  site at the godess place, nevermind the doomed place of   ##
###  the damns and unholls bones.                              ##
###                                        NoSenseMan          ##
#################################################################

import darfuncs
import Bladex
import Damage
import AbreCam
import Actions
import EnemyTypes
import PhantonFX
import GenFX
import ItemTypes
import Reference
import Auras
import Blood
import Menu
import types
import AuxFuncs


def GetSectorIdx(pos):
	if type(pos)==types.StringType:
		return pos
	else:
		return Bladex.GetSector(pos[0],pos[1],pos[2]).Index


############################
#                          #
#  CHAOS KNIGHT GENERATOR  #
#                          #
############################


_AppearsCagazo=Bladex.CreateSound("../../Sounds/AparicionEnric2.wav","AppearsCagazo")
_AppearsCagazo.MaxDistance=200000.0
_AppearsCagazo.MinDistance=20000.0

ChaosKnightActivated = 1

def MuereCaos(caosname):
	chaosk1 = Bladex.GetEntity(caosname)
	chaosk1.Data.PrepareDisappearance()
	chaosk1.Data.Disappear(caosname)



def ChaosAbreCam(per):
	AbreCam.PTS=[]

	AbreCam.PTS.append((per.Position[0]-3000,per.Position[1]-1000, per.Position[2]-3000),per.Position,0.01)
	AbreCam.PTS.append((per.Position[0]-3000,per.Position[1]-1000, per.Position[2]+3000),per.Position,3.5)
	AbreCam.PTS.append((per.Position[0]+3000,per.Position[1]-1000, per.Position[2]+3000),per.Position,3.5)
	AbreCam.PTS.append((per.Position[0]+3000,per.Position[1]-1000, per.Position[2]-3000),per.Position,3.5)
	AbreCam.PTS.append((per.Position[0]-3000,per.Position[1]-1000, per.Position[2]-3000),per.Position,3.5)
	AbreCam.LastTime = 0.01

	AbreCam.AbreCam()


def CreateChaosKnightBak(Position,Angle):
	global CHAOS_KNIGHT_POSITION
	global CHAOS_KNIGHT_ANGLE
	global CHAOS_KNIGHT_ACTIVATE
	global CHAOS_KNIGHT_DEACTIVATE
	global CHAOS_KNIGHT_LEVEL

	chaosk1       = Bladex.CreateEntity("ChaosKnightBak", "ChaosKnight", Position[0], Position[1], Position[2],"Person")
	chaosk1.ActionAreaMin=pow(2,0)
	chaosk1.ActionAreaMax=pow(2,1)
	chaosk1.Angle = Angle
	chaosk1.Level = CHAOS_KNIGHT_LEVEL
	EnemyTypes.EnemyDefaultFuncs(chaosk1)
	chaosk1.ImDeadFunc = MuereCaos

	chaosk1.Data.DamageFactorNone=0.15
	chaosk1.Data.DamageFactorLight=0.35
	chaosk1.Data.DamageFactorHeavy=0.35
	chaosk1.Data.PrepareWeapons("Espadon", "Escudon")
	chaosk1.SetOnFloor()
	darfuncs.HideBadGuy(chaosk1.Name)


def ParticulateAppears(PersonName = "Player1"):
	wps=Bladex.CreateEntity(PersonName+"WPS", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
	wps.PersonName=PersonName
	wps.ParticleType="EnergyConc"
	wps.Time2Live=60
	wps.RandomVelocity=0
	wps.Velocity=0,0,0
	wps.NormalVelocity=-5.0
	wps.YGravity=0
	wps.DeathTime=Bladex.GetTime()+1.5
	wps.PPS=600
	Bladex.GetEntity(PersonName).Alpha = 0.0
	PhantonFX.Delta = 0.015
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, PhantonFX.AppearsChar,(PersonName,))

def AppearsChaosKnightBak():
	global CHAOS_KNIGHT_POSITION
	global CHAOS_KNIGHT_ANGLE
	global CHAOS_KNIGHT_ACTIVATE
	global CHAOS_KNIGHT_DEACTIVATE
	global CHAOS_KNIGHT_LEVEL
	global EXEC_IN_CHAOS_KNIGHT_APPEARING
	global ChaosKnightActivated

	if not ChaosKnightActivated:
		return

	chaosk1 = Bladex.GetEntity("ChaosKnightBak")
	darfuncs.UnhideBadGuy(chaosk1.Name)
	Bladex.AddScheduledFunc(Bladex.GetTime()+15.0, darfuncs.UnhideBadGuy,(chaosk1.Name,))
	chaosk1.Blind=1
	chaosk1.Deaf=1
	chaosk1.Alpha = 0.0
	chaosk1.Data.Appear()
	ChaosAbreCam(chaosk1)
	ParticulateAppears(chaosk1.Name)
	Actions.TurnToFaceEntityNow("ChaosKnightBak","Player1")

	for pos in CHAOS_KNIGHT_DEACTIVATE:
		darfuncs.EnterSecIdEvent(pos,TranslateChaos)
	if EXEC_IN_CHAOS_KNIGHT_APPEARING:
		EXEC_IN_CHAOS_KNIGHT_APPEARING()


def ParticulateDisappears(PersonName = "Player1"):
	wps=Bladex.CreateEntity(PersonName+"WPS", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
	wps.PersonName=PersonName
	wps.ParticleType="EnergyDissip"
	wps.Time2Live=60
	wps.RandomVelocity=0
	wps.Velocity=0,0,0
	wps.NormalVelocity=5.0
	wps.YGravity=0
	wps.DeathTime=Bladex.GetTime()+1.5
	wps.PPS=600
	Bladex.GetEntity(PersonName).Alpha = 1.0
	PhantonFX.Delta  = 0.015
	PhantonFX.SecAgo = 0
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, PhantonFX.DisappearsChar,(PersonName,BorraCaos))

def BorraCaos(ent):
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.2, PrepareChaosAppears2,())
	ch = Bladex.GetEntity("ChaosKnightBak")
	ch.Data.InteruptActions("ChaosKnightBak")
	darfuncs.HideBadGuy("ChaosKnightBak")

def TranslateChaos():
	chaosk1 = Bladex.GetEntity("ChaosKnightBak")
	if chaosk1:
		if chaosk1.Life > 0:
			chaosk1.Freeze()
			ParticulateDisappears("ChaosKnightBak")

def AppearsChaosKnightBak2():
	global CHAOS_KNIGHT_POSITION
	global CHAOS_KNIGHT_ANGLE
	global CHAOS_KNIGHT_ACTIVATE
	global CHAOS_KNIGHT_DEACTIVATE
	global CHAOS_KNIGHT_LEVEL
	global ChaosKnightActivated

	if not ChaosKnightActivated:
		return

	chaosk1 = Bladex.GetEntity("ChaosKnightBak")
	darfuncs.UnhideBadGuy(chaosk1.Name)
	ParticulateAppears(chaosk1.Name)
	Actions.TurnToFaceEntityNow("ChaosKnightBak","Player1")
	for pos in CHAOS_KNIGHT_DEACTIVATE:
		darfuncs.EnterSecIdEvent(pos,TranslateChaos)


def DeactivateChaosWeapon(EntityName, EventName):


	if EventName=="ChkDisapR":
		weapon=Bladex.GetEntity(Bladex.GetEntity(EntityName).InvRight)
	else:
		weapon=Bladex.GetEntity(Bladex.GetEntity(EntityName).InvLeft)

	weapon.RasterMode  ="Read"
	weapon.Alpha       = 0

	wps=Bladex.CreateEntity("WPS", "Entity Particle System Dobj", 0.0, 0.0, 0.0)
	wps.ObjectName=weapon.Name
	wps.ParticleType="EnergyDissip"
	wps.PPS=400
	wps.YGravity=0.0
	wps.Friction=0.0
	wps.Velocity=0.0, 0.0, 0.0
	wps.RandomVelocity=2.0
	wps.NormalVelocity=6.0
	wps.Time2Live=60
	wps.DeathTime=Bladex.GetTime()+1.5

def PrepareChaosAppears2():
	global CHAOS_KNIGHT_POSITION
	global CHAOS_KNIGHT_ANGLE
	global CHAOS_KNIGHT_ACTIVATE
	global CHAOS_KNIGHT_DEACTIVATE
	global CHAOS_KNIGHT_LEVEL

	pers=Bladex.CreateEntity("ChaosKnightBak","ChaosKnight",CHAOS_KNIGHT_POSITION[0],CHAOS_KNIGHT_POSITION[1],CHAOS_KNIGHT_POSITION[2],"Person")
	pers.ActionAreaMin=pow(2,0)
	pers.ActionAreaMax=pow(2,1)
	pers.Angle    = CHAOS_KNIGHT_ANGLE

	EnemyTypes.EnemyDefaultFuncs(pers)

	pers.Data.PrepareWeapons("Espadon", "Escudon")
	Actions.TakeObject(pers.Name,"EspadonChaosKnightBak")
	Actions.TakeObject(pers.Name,"EscudonChaosKnightBak")

	pers.ImDeadFunc = MuereCaos



	pers.AddAnmEventFunc("ChkDisapL", DeactivateChaosWeapon)
	pers.AddAnmEventFunc("ChkDisapR", DeactivateChaosWeapon)

	pers.SetOnFloor()
	darfuncs.HideBadGuy(pers.Name)

	for pos in CHAOS_KNIGHT_ACTIVATE:
		darfuncs.EnterSecIdEvent(pos,AppearsChaosKnightBak2)

#
# Interface
#

CHAOS_KNIGHT_LEVEL             = 15
CHAOS_KNIGHT_POSITION          = 300029.603984, 8180.76682918, -1209.8189804
CHAOS_KNIGHT_ANGLE             = 0
CHAOS_KNIGHT_ACTIVATE          = []
CHAOS_KNIGHT_DEACTIVATE        = []
TIME_BEFORE_PLAYER_APPEARING   = 1.5
EXEC_IN_PLAYER_APPEARING       = ""
EXEC_IN_CHAOS_KNIGHT_APPEARING = ""

def PlayerAppears():
	import Scorer
	global EXEC_IN_PLAYER_APPEARING

	darfuncs.UnhideBadGuy("Player1")
	GenFX.PersonMagicallyAppearing()
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, Bladex.ActivateInput, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, Scorer.SetVisible, (1,))
	if EXEC_IN_PLAYER_APPEARING:
		EXEC_IN_PLAYER_APPEARING()

def PrevPlayerAppears():
	import Scorer

	global TIME_BEFORE_PLAYER_APPEARING

	darfuncs.HideBadGuy("Player1")
	Scorer.SetVisible(0)
	Bladex.DeactivateInput()
	AuxFuncs.FadeFrom(2.0, TIME_BEFORE_PLAYER_APPEARING)

	Bladex.AddScheduledFunc(Bladex.GetTime()+TIME_BEFORE_PLAYER_APPEARING+2.0, PlayerAppears, ())

def PrepareChaosAppears():
	global CHAOS_KNIGHT_POSITION
	global CHAOS_KNIGHT_ANGLE
	global CHAOS_KNIGHT_ACTIVATE
	global CHAOS_KNIGHT_DEACTIVATE
	global CHAOS_KNIGHT_LEVEL

	CreateChaosKnightBak(CHAOS_KNIGHT_POSITION,CHAOS_KNIGHT_ANGLE)
	Blood.Evaporation = 1
	#Menu.BackMap()

	Bladex.AddScheduledFunc(Bladex.GetTime(), PrevPlayerAppears, ())

	for pos in CHAOS_KNIGHT_ACTIVATE:
		darfuncs.EnterSecIdEvent(pos,AppearsChaosKnightBak)

def AddChaosAppearsSector(x,y,z):
	global CHAOS_KNIGHT_ACTIVATE

	CHAOS_KNIGHT_ACTIVATE.append(Bladex.GetSector(x,y,z).Index)

def AddChaosAppearsTSector(id):
	global CHAOS_KNIGHT_ACTIVATE

	CHAOS_KNIGHT_ACTIVATE.append(id)

def AddChaosDisappearsSector(x,y,z):
	global CHAOS_KNIGHT_DEACTIVATE

	CHAOS_KNIGHT_DEACTIVATE.append(Bladex.GetSector(x,y,z).Index)

def AddChaosDisappearsTSector(id):
	global CHAOS_KNIGHT_DEACTIVATE

	CHAOS_KNIGHT_DEACTIVATE.append(id)

def DeactivateChaos():
	global ChaosKnightActivated

	ChaosKnightActivated = 0

def AddChaosDeactivationTs(id):
	darfuncs.EnterSecIdEvent(id,DeactivateChaos)



############################
#                          #
#      Little demons       #
#            &             #
#         Vampires         #
#                          #
############################


##### Appears FX #####

Bladex.ReadBitMap("../../Data/SmokePrtl3.bmp","SmokePart3")
Bladex.AddParticleGType("DeathCloud","SmokePart3",Reference.B_PARTICLE_GTYPE_MUL,16)


for i in range(16):
	aux=(16.0-i)/16
	r=255
	g=255
	b=255
	a=0
	if aux < 0.5:
		size = aux*512
	else:
		size = (1-aux)*512
	Bladex.SetParticleGVal("DeathCloud",i,r,g,b,a,size)

def DeathAppears(PersonName = "Player1",pos=(0,0,0)):
	time=Bladex.GetTime()
	aura=Auras.MakeAura(PersonName,0.4,   ( 50, 1.0 , 0.0, 0, 0, 0), (), (), (2,  0.9, 0.9, 0.0, 0.9, 0.0  ,  0.9, 0.9, 0.0, 0.9, 0.8))
	aura.Data.AddEvent(time+0.2,          (150, 0.5 , 0.0, 0, 0, 0), (), (), (2,  0.9, 0.9, 0.0, 0.9, 0.0  ,  0.9, 0.9, 0.0, 0.9, 0.8))
	aura.Data.AddEvent(time+0.4,          (200, 0.01, 0.0, 0, 0, 0), (), (), (2,  0.9, 0.9, 0.0, 0.9, 0.0  ,  0.9, 0.9, 0.0, 0.9, 0.8))

	wps=Bladex.CreateEntity(PersonName+"WPS", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
	wps.PersonName=PersonName
	wps.ParticleType="DeathCloud"
	wps.Time2Live=16
	wps.RandomVelocity=2.0
	wps.Velocity=0,0,0
	wps.NormalVelocity=20
	wps.YGravity=0
	wps.DeathTime=Bladex.GetTime()+0.25
	wps.PPS=1024
	per = Bladex.GetEntity(PersonName)
	darfuncs.UnhideBadGuy(per.Name)
	per.Alpha = 1.0
	per.Wuea=Reference.WUEA_ENDED
	per.LaunchAnmType("rlx")
	per.Position = pos
	per.SetOnFloor()
	per.SetActiveEnemy("Player1")
	Actions.TurnToFaceEntityNow(per.Name,"Player1")
	_AppearsCagazo.Play(per.Position[0], per.Position[1], per.Position[2], 0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, per.ResetChase,())

def DeathDisappears(PersonName = "Player1"):
	wps=Bladex.CreateEntity(PersonName+"WPS", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
	wps.PersonName=PersonName
	wps.ParticleType="DeathCloud"
	wps.Time2Live=16
	wps.RandomVelocity=2.0
	wps.Velocity=0,0,0
	wps.NormalVelocity=2
	wps.YGravity=0
	wps.DeathTime=Bladex.GetTime()+0.25
	wps.PPS=1024
	per = Bladex.GetEntity(PersonName)
	per.Data.InteruptActions(per.Name)
	darfuncs.HideBadGuy(per.Name)
	_AppearsCagazo.Play(per.Position[0], per.Position[1], per.Position[2], 0)



##### Sector controllers #####

SECTOR_PROCS       = {}

LastSectorIdx      = None
SECTOR_COUNT       = {}

def RemoveSector(idx):
	global SECTOR_PROCS

	if SECTOR_PROCS.has_key(idx):
		del  SECTOR_PROCS[idx]

def AddSectorCount(pos,Demons,Vampires):
	global SECTOR_COUNT

	idx = GetSectorIdx(pos)
	SECTOR_COUNT[idx] = [Demons,Vampires,[]]
	return idx

def AddSectorDelete(idx,pos):
	global SECTOR_COUNT

	SECTOR_COUNT[idx][2].append(GetSectorIdx(pos))

def OnEnterSectorProc(sector):
	global SECTOR_PROCS
	global SECTOR_COUNT
	global LastSectorIdx

	if SECTOR_PROCS.has_key(sector):
		if SECTOR_COUNT.has_key(sector):
			LastSectorIdx = sector

		for i in SECTOR_PROCS[sector]:
			apply(i[0],i[1])

		for i in SECTOR_PROCS.keys():
			if i != sector:
				darfuncs.EnterSecIdEvent(i,OnEnterSectorProc)

def ActivateSectorProcs():
	global SECTOR_PROCS

	for i in SECTOR_PROCS.keys():
		darfuncs.EnterSecIdEvent(i,OnEnterSectorProc)

def AddSectorFunction(pos,func,param):
	global SECTOR_PROCS

	idx = GetSectorIdx(pos)
	if SECTOR_PROCS.has_key(idx):
		SECTOR_PROCS[idx].append((func,param))
	else:
		SECTOR_PROCS[idx] =[(func,param)]

##### Enemies controller #####
L_Vamp             = []
L_Little_Demon     = []

def AddVampires(Num,ValidPos,Level):
	global L_Vamp

	for i in range(Num):
		pers=Bladex.CreateEntity("VMP_"+`Level`+"_"+`i`,"Vamp",ValidPos[0],ValidPos[1],ValidPos[2],"Person")
		pers.Angle=6.26312373572
		pers.Level=Level

		Cimitarra1=Bladex.CreateEntity("VampWeapon"+`Level`+"_"+`i`,"VampWeapon",0,0,0,"Weapon")
		VampShield=Bladex.CreateEntity("VampShield"+`Level`+"_"+`i`,"VampShield",0,0,0,"Weapon")
		ItemTypes.ItemDefaultFuncs(Cimitarra1)
		ItemTypes.ItemDefaultFuncs(VampShield)
		Actions.TakeObject(pers.Name,Cimitarra1.Name)
		Actions.TakeObject(pers.Name,VampShield.Name)

		#pers.ActionAreaMin=pow(2,2)
		#pers.ActionAreaMax=pow(2,3)
		EnemyTypes.EnemyDefaultFuncs(pers)
		pers.SetOnFloor()
		darfuncs.HideBadGuy(pers.Name)
		pers.ImDeadFunc = MuerteBichoMolesto

		L_Vamp.append([pers.Name,0])

def AddDemons(Num,ValidPos,Level):
	global L_Little_Demon

	for i in range(Num):
		pers=Bladex.CreateEntity("Little_Demon_"+`Level`+"_"+`i`,"Little_Demon",ValidPos[0],ValidPos[1],ValidPos[2],"Person")
		pers.Angle=6.26312373572
		pers.Level=Level
		#pers.ActionAreaMin=pow(2,2)
		#pers.ActionAreaMax=pow(2,3)
		EnemyTypes.EnemyDefaultFuncs(pers)
		pers.SetOnFloor()
		pers.ImDeadFunc = MuerteBichoMolesto
		darfuncs.HideBadGuy(pers.Name)

		L_Little_Demon.append([pers.Name,0])

# Aparicion de un enemigo
def EnemyAppear(List,Position,Time):
	EneName = None
	for i in List:
		if not i[1]:
			i[1]    = 1
			EneName = i[0]
			break
	if EneName:
		Actions.TurnToFaceEntityNow(EneName,"Player1")
		Bladex.GetEntity(EneName).Position = Position
		#darfuncs.HideBadGuy(EneName)
		Bladex.AddScheduledFunc(Bladex.GetTime()+Time, DeathAppears,(EneName,Position))
		print "EnemyAppear ",EneName


def HideEnemies():
	print "HideEnemies"
	global L_Little_Demon
	global L_Vamp

	for i in L_Vamp:
		if i[1]:
			DeathDisappears(i[0])
			i[1] = 0
	for i in L_Little_Demon:
		if i[1]:
			DeathDisappears(i[0])
			i[1] = 0


def HideEnemiesSector(pos):
	AddSectorFunction(pos,HideEnemies,())


def AddVampireAppears(secPos,enePos,Time):
	global L_Vamp
	AddSectorFunction(secPos,EnemyAppear,(L_Vamp,enePos,Time))

def AddDemonAppears(secPos,enePos,Time):
	global L_Little_Demon
	AddSectorFunction(secPos,EnemyAppear,(L_Little_Demon,enePos,Time))

def MuerteBichoMolesto(Name):
	global L_Little_Demon
	global L_Vamp
	global SECTOR_COUNT
	global LastSectorIdx

	me = Bladex.GetEntity(Name)
	if me.Kind == "Vamp":
		for i in L_Vamp:
			if i[0]==Name:
				L_Vamp.remove(i)
				break

		DeathDisappears(Name)
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, me.SubscribeToList,("Pin",))
		SECTOR_COUNT[LastSectorIdx][1] = SECTOR_COUNT[LastSectorIdx][1]-1
		if SECTOR_COUNT[LastSectorIdx][1] == 0:
			for idsec in SECTOR_COUNT[LastSectorIdx][2]:
				RemoveSector(idsec)
			ActivateSectorProcs()

	else:
		for i in L_Little_Demon:
			if i[0]==Name:
				L_Little_Demon.remove(i)
				break
		me.Data.ImDeadFunc(Name)
		SECTOR_COUNT[LastSectorIdx][0] = SECTOR_COUNT[LastSectorIdx][0]-1
		if SECTOR_COUNT[LastSectorIdx][0] == 0:
			for idsec in SECTOR_COUNT[LastSectorIdx][2]:
				RemoveSector(idsec)
			ActivateSectorProcs()




def SaveData(filename):
  import cPickle
  import GameStateAux

  funcfile=open(filename,"wt")
  p=cPickle.Pickler(funcfile)
  p.persistent_id=GameStateAux.persistent_id
  d=(_AppearsCagazo,ChaosKnightActivated,CHAOS_KNIGHT_LEVEL,
     CHAOS_KNIGHT_POSITION,CHAOS_KNIGHT_ANGLE,CHAOS_KNIGHT_ACTIVATE,
     CHAOS_KNIGHT_DEACTIVATE,TIME_BEFORE_PLAYER_APPEARING,
     EXEC_IN_PLAYER_APPEARING,EXEC_IN_CHAOS_KNIGHT_APPEARING,
     SECTOR_PROCS,LastSectorIdx,SECTOR_COUNT,L_Vamp,L_Little_Demon)


  p.dump(d)
  funcfile.close()



def LoadData(filename):
  import cPickle
  import GameStateAux

  global _AppearsCagazo
  global ChaosKnightActivated
  global CHAOS_KNIGHT_LEVEL
  global CHAOS_KNIGHT_POSITION
  global CHAOS_KNIGHT_ANGLE
  global CHAOS_KNIGHT_ACTIVATE
  global CHAOS_KNIGHT_DEACTIVATE
  global TIME_BEFORE_PLAYER_APPEARING
  global EXEC_IN_PLAYER_APPEARING
  global EXEC_IN_CHAOS_KNIGHT_APPEARING
  global SECTOR_PROCS
  global LastSectorIdx
  global SECTOR_COUNT
  global L_Vamp
  global L_Little_Demon

  funcfile=open(filename,"rt")
  p=cPickle.Unpickler(funcfile)
  p.persistent_load=GameStateAux.persistent_load
  d=p.load()
  funcfile.close()
  print d


  _AppearsCagazo                 = d[ 0]
  ChaosKnightActivated           = d[ 1]
  CHAOS_KNIGHT_LEVEL             = d[ 2]
  CHAOS_KNIGHT_POSITION          = d[ 3]
  CHAOS_KNIGHT_ANGLE             = d[ 4]
  CHAOS_KNIGHT_ACTIVATE          = d[ 5]
  CHAOS_KNIGHT_DEACTIVATE        = d[ 6]
  TIME_BEFORE_PLAYER_APPEARING   = d[ 7]
  EXEC_IN_PLAYER_APPEARING       = d[ 8]
  EXEC_IN_CHAOS_KNIGHT_APPEARING = d[ 9]
  SECTOR_PROCS                   = d[10]
  LastSectorIdx                  = d[11]
  SECTOR_COUNT                   = d[12]
  L_Vamp                         = d[13]
  L_Little_Demon                 = d[14]


###
### Sample of Enemies at back map
###
##
##import BackMisc
##
###
### CHAOS KNIGHT
###
##
##BackMisc.CHAOS_KNIGHT_LEVEL       = 1
##BackMisc.CHAOS_KNIGHT_POSITION    = 16230.9184998, -735.695860989, 39699.5778343
##BackMisc.CHAOS_KNIGHT_ANGLE       = 0
##
##BackMisc.AddChaosDisappearsSector(15239.4035073, -2747.16516658, 57256.1186163)
##BackMisc.AddChaosDisappearsSector(253.269773313, -2663.49693091, 39305.8229719)
##BackMisc.AddChaosDisappearsSector(15874.8334796, -1229.29468164, 19106.6487786)
##BackMisc.AddChaosDisappearsSector(29467.4856681, -2729.42212464, 39537.9079875)
##
##BackMisc.AddChaosAppearsSector(16230.9184998, -735.695860989, 39699.5778343)
##
##BackMisc.AddChaosDeactivationTs("ChauCaos")
##
##BackMisc.PrepareChaosAppears()
##
###
### Vampire and demons
###
##
##BackMisc.AddVampires(5,(15159, -1133, 1923),0)
##BackMisc.AddDemons(5,(15159, -1133, 1923),0)
##
##idx = BackMisc.AddSectorCount(   (15417, -2189, 53450),1,1)
##BackMisc.AddSectorDelete(idx,(15417, -2189, 53450))
##
##BackMisc.HideEnemiesSector((15417, -2189, 53450))
##BackMisc.AddDemonAppears  ((15417, -2189, 53450),( 9325, -2669, 59723),0.1)
##BackMisc.AddDemonAppears  ((15417, -2189, 53450),(25242, -2690, 59909),0.5)
##BackMisc.AddVampireAppears((15417, -2189, 53450),(16000, -2671, 65675),1.0)
##
##BackMisc.HideEnemiesSector((15703, -690, 42391))
##
##BackMisc.ActivateSectorProcs()
### BackMisc.EnemyAppear(BackMisc.L_Little_Demon,( 9325, -2669, 59723),0.1)
### BackMisc.HideEnemies()
### BackMisc.L_Little_Demon
### BackMisc.L_Vamp
##
##def CambiaSangre(pos,c,dc):
##	for l in Bladex.GetEntitiesAt(pos[0],pos[1],pos[2],10000):
##		o = Bladex.GetEntity(l)
##		if o.Kind == 'Entity Pool':
##			print o.Color,o.DeepColor
##			o.DeepColor = dc
##			o.Color     = c
##
##CambiaSangre(char.Position,(0,0,0),(0,0,0))
##
##

import GameState
GameState.ModulesToBeSaved.append(__import__(__name__))
