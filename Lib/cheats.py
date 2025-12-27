import Actions
import Bladex
import math
import CharStats
import darfuncs
import BBLib
import GotoMapVars

# import cheats
# cheats.ActivateMiscCheats()
# cheats.ActivateLaserEyes()
# cheats.ActivateWeaponGrow()
# cheats.ActivateGoreCheatsCheats()
# cheats.ActivateLevelCheats()
# 

#
# CHEAT NUMBER 1: SCALE WEAPONS AND SHIELDS
###################################################
def ScaleWeapon(scale):
	char = Bladex.GetEntity("Player1")
	weap = Bladex.GetEntity(char.InvRight)
	if weap and (char.InvRightBack==""):
		if (weap.Scale*scale > 5) or (weap.Scale*scale < 0.125):
			return
		Actions.RemoveFromInventory(char, weap,"DropRightEvent")
		weap.Scale = weap.Scale*scale
		Actions.TakeObject(char.Name, weap.Name)

def ScaleShield(scale):
	char = Bladex.GetEntity("Player1")
	weap = Bladex.GetEntity(char.InvLeft)
	if weap and (char.InvRightBack==""):
		if (weap.Scale*scale > 5) or (weap.Scale*scale < 0.125):
			return
		Actions.RemoveFromInventory(char, weap,"DropRightEvent")
		weap.Scale = weap.Scale*scale
		Actions.TakeObject(char.Name, weap.Name)


def BigSword():
	Actions.ReportMsg("Bigger :-)")
	ScaleWeapon(2.0)

def SmallSword():
	Actions.ReportMsg("Smaller :-(")
	ScaleWeapon(0.5)

def BigShield():
	Actions.ReportMsg("Bigger :-)")
	ScaleShield(2.0)

def SmallShield():
	Actions.ReportMsg("Smaller :-(")
	ScaleShield(0.5)

CHEAT_SCALE = 0
def ActivateWeaponGrow():
	global CHEAT_SCALE
	if CHEAT_SCALE:
		return
	else:
		CHEAT_SCALE = 1
	Bladex.AddInputAction("BigSword", 0)
	Bladex.AssocKey("BigSword", "Keyboard", "2", 1)
	Bladex.AddBoundFunc("BigSword", BigSword)
	
	Bladex.AddInputAction("SmallSword", 0)
	Bladex.AssocKey("SmallSword", "Keyboard", "1", 1)
	Bladex.AddBoundFunc("SmallSword", SmallSword)
	
	Bladex.AddInputAction("BigShield", 0)
	Bladex.AssocKey("BigShield", "Keyboard", "3", 1)
	Bladex.AddBoundFunc("BigShield", BigShield)
	
	Bladex.AddInputAction("SmallShield", 0)
	Bladex.AssocKey("SmallShield", "Keyboard", "4", 1)
	Bladex.AddBoundFunc("SmallShield", SmallShield)



#
# CHEAT NUMBER 2: Start Wars Stuff
###################################################

#
# LASER CHEAT
#

LASER_ACTIVATED = 1
def LaserCounterAttack(Side,dist):
	global laser
	if laser.Active == 0:
		return
	char = Bladex.GetEntity("Player1")
	if char.Data.selected_enemy:
		enemigo=Bladex.GetEntity(char.Data.selected_enemy[0])
		if enemigo:
			x,y,z = char.Position
			if Side == 1:
				ang = char.Angle
			else:
				ang = char.Angle+3.1415
			lp = x+math.cos(ang)*300,y,z+math.sin(ang)*300
			lt = enemigo.Position
			d1 = (dist+0.0)/10.0
			d2 = (dist+3.0)/10.0
			if   d1 < 0.0:
				d1 = 0.0
			elif d1 > 1.0:
				d1 = 9.0/10.0
			if   d2 < 0.0:
				d2 = 0.0
			elif d2 > 1.0:
				d2 = 9.0/10.0
			laser.Position = lp[0]-(lp[0]-lt[0])*d1,lp[1]-(lp[1]-lt[1])*d1,lp[2]-(lp[2]-lt[2])*d1
			laser.Target   = lp[0]-(lp[0]-lt[0])*d2,lp[1]-(lp[1]-lt[1])*d2,lp[2]-(lp[2]-lt[2])*d2
			dist = dist+1
			if dist >= 10:
				dist = 0
				Side = not Side
				can = CharStats.GetCharMaxLife(enemigo.Kind,enemigo.Level)/10.0
				if can<1.0:
					can = 1
				enemigo.Life = enemigo.Life-can				
				polvo=Bladex.CreateEntity("Polvo", "Entity Particle System D2", 0,0,0)
				polvo.Position=enemigo.Position
				polvo.ParticleType="Fire"
				polvo.YGravity=0.0
				polvo.Friction=0.1
				polvo.PPS=512
				polvo.Velocity=0.0, 0.0, 0.0
				polvo.RandomVelocity=45.0
				polvo.Time2Live = 10
				polvo.DeathTime=Bladex.GetTime()+3.0/60.0
				LaserSound.PlayStereo()
		else:
			laser.Active = 0
	else:
		laser.Active = 0
	
	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.025,   LaserCounterAttack,(Side,dist),"LaserBean")



def ActivateLaser():
	global Active
	laser.Active = 1
	LaserCounterAttack(0,0)
	Actions.ReportMsg("Laser bean!")

laser = 0
LaserSound = 0
CHEAT_LASER = 0
def ActivateLaserEyes():
	global CHEAT_LASER
	global laser
	global LaserSound
	
	if CHEAT_LASER:
		return
	else:
		CHEAT_LASER = 1

	Bladex.AddInputAction("StartLaser", 0)
	Bladex.AssocKey("StartLaser", "Keyboard", "K", 1)
	Bladex.AddBoundFunc("StartLaser", ActivateLaser)
	
	Bladex.AddInputAction("CreateLightSabre", 0)
	Bladex.AssocKey("CreateLightSabre", "Keyboard", "G", 1)
	Bladex.AddBoundFunc("CreateLightSabre", CreateLightSabre)
	
	
	# laser used to the chear
	char = Bladex.GetEntity("Player1")
	x,y,z = char.Position

	laser=Bladex.CreateEntity("Rayo1", "Entity ElectricBolt",x,y,z)
	laser.Target = x,y+1000,z
	laser.MaxAmplitude    = 20
	laser.MinSectorLength = 1000000
	laser.InnerGlowColor  = 255,64,64
	laser.CoreGlowColor   = 255,128,128
	laser.Active=0
	laser.Damage=0
	LaserSound                = Bladex.CreateSound("../../Sounds/Sesgado1.wav","Sesgado")
	LaserSound.MaxDistance = 1000000.0
	LaserSound.MinDistance = 1000000.0
	




#
# Light Sabre
#

def CreateLightSabre():
	char = Bladex.GetEntity("Player1")
	inv = char.GetInventory()
	if inv.nWeapons>4:
		Actions.ReportMsg("Drop a weapon to use the force!")
		return

	if not Bladex.GetEntity("LightSabre"):
		LightSabre = Bladex.CreateEntity("LightSabre","Espadaromana",0,0,0,"Weapon")
		darfuncs.ObjAlpha(LightSabre,0.0)
		Actions.TakeObject("Player1","LightSabre")
		darfuncs.SetHint(LightSabre,"Laser Sword")

		Light=Bladex.CreateEntity("LightSabreLaser", "Entity ElectricBolt",0,600,0)
		Light.Target          = 0,-400,0 #char.Position
		Light.MaxAmplitude    = 20
		Light.MinSectorLength = 1000000
		Light.InnerGlowColor  = 255,64,64
		Light.CoreGlowColor   = 255,128,128
		Light.FixedTarget     = 0
		Light.ETarget         = "LightSabre"
		Light.Active          = 1
		Light.Damage          = 0
		LightSabre.Link(Light)
		Actions.ReportMsg("The force is strong in you!")
	else:
		DeleteLightSabre()
		Actions.ReportMsg("The force has left you!")

def DeleteLightSabre():
	char = Bladex.GetEntity("Player1")
	inv = char.GetInventory()
	ls = Bladex.GetEntity("LightSabre")
	if ls:
		inv = char.GetInventory()
		if char.InvRight == "LightSabre":
			inv.LinkRightHand("None")
		if char.InvRightBack == "LightSabre":
			inv.LinkRightBack("None")
		inv.RemoveWeapon("LightSabre")
	
		Bladex.GetEntity("LightSabre").SubscribeToList("Pin")


#
# CHEAT NUMBER 3: Miscelanea
###################################################
CHEAT_MISC = 0
def ActivateMiscCheats():
	global CHEAT_MISC
	
	if CHEAT_MISC:
		return
	else:
		CHEAT_MISC = 1
	Bladex.AssocKey("ToggleInvincibility","Keyboard","F10")
	Bladex.AssocKey("Camera Left","Keyboard","F5")
	Bladex.AssocKey("Camera Right","Keyboard","F6")
	Bladex.AssocKey("Change Mov","Keyboard","P")



#
# CHEAT NUMBER 4: GoreCheats
###################################################
CHEAT_GORE = 0
def ActivateGoreCheatsCheats():
	global CHEAT_GORE
	
	if CHEAT_GORE:
		return
	else:
		CHEAT_GORE = 1

	Bladex.AddInputAction("SleepyHollow", 0)
	Bladex.AssocKey("SleepyHollow", "Keyboard", "H", 1)
	Bladex.AddBoundFunc("SleepyHollow", SleepyHollow)

	Bladex.AddInputAction("Mutational", 0)
	Bladex.AssocKey("Mutational", "Keyboard", "M", 1)
	Bladex.AddBoundFunc("Mutational", Mutational)

	Bladex.AddInputAction("Matrix", 0)
	Bladex.AssocKey("Matrix", "Keyboard", "X", 1)
	Bladex.AddBoundFunc("Matrix", Matrix)
	
	BBLib.ReadMMP('../../3dChars/Ork.mmp')
	BBLib.ReadMMP('../../3dChars/Skl.mmp')
	BBLib.ReadMMP('../../3dChars/Tkn.mmp')
	BBLib.ReadMMP('../../3dChars/Tkn.mmp')
	BBLib.ReadMMP('../../3dChars/DarkKnight.mmp')
	BBLib.ReadMMP('../../3dChars/rgn.mmp')
	
MatrixFX = 0
def Matrix():
	global MatrixFX
	if MatrixFX:
		darfuncs.StartMatrixFX()
		Actions.ReportMsg("Matrix FX activated")
	else:
		darfuncs.StopMatrixFX()
		Actions.ReportMsg("Matrix FX deactivated")
	MatrixFX = not MatrixFX

def SleepyHollow():
	char = Bladex.GetEntity("Player1")
	if char.Data.selected_enemy:
		enemigo=Bladex.GetEntity(char.Data.selected_enemy[0])
		if enemigo:
			if enemigo.SeverLimb(1):
				Actions.ReportMsg("Where is my head!")
			return
	if char.SeverLimb(1):
		Actions.ReportMsg("You need a pumpkin!")
	return

def Mutational():
	char = Bladex.GetEntity("Player1")
	
	if   char.MeshName == char.Kind:
		char.SetMesh("Skeleton")
	elif char.MeshName =="Skeleton":
		char.SetMesh("Knight_Traitor")
	elif char.MeshName =="Knight_Traitor":
		char.SetMesh("Ork")
	elif char.MeshName =="Ork":
		char.SetMesh("Dark_Knight")
	else:
		char.SetMesh(char.Kind)
	
	Actions.ReportMsg("New skin!")
	
#
# CHEAT NUMBER 5: LevelChangeCheats
###################################################
CHEAT_LEVEL = 0
def ActivateLevelCheats():
	global CHEAT_LEVEL
	
	if CHEAT_LEVEL:
		return
	else:
		CHEAT_LEVEL = 1

	Bladex.AddInputAction("NextLevel", 0)
	Bladex.AssocKey("NextLevel", "Keyboard", "F9", 1)
	Bladex.AddBoundFunc("NextLevel", NextLevel)

	Bladex.AddInputAction("LevelUp", 0)
	Bladex.AssocKey("LevelUp", "Keyboard", "F8", 1)
	Bladex.AddBoundFunc("LevelUp", LevelUp)


def NextLevel():
	char = Bladex.GetEntity("Player1")
	if char.Life > 0.0:		
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, GotoMapVars.EndOfLevel,(),"ChangingLevel")

def LevelUp():
	char = Bladex.GetEntity("Player1")
	if char.Level < 18:
		char.Level = char.Level+1
		char.Life  = CharStats.GetCharMaxLife(char.Kind,char.Level)
		Actions.ReportMsg("Level up!")

import whrandom
import Actions
import EnemyTypes
import CharData
import pocimac
import Reference
import ItemTypes

def DebugArena():
	char=Bladex.GetEntity("Player1")

	keys = Reference.DefaultObjectData.keys()

	keys = ["Gladius", "BladeSword"]

	char.Level=30
	pos=char.Position
	posy = pos[1]

	for i in range(2):
		x = pos[0] + whrandom.randint(-5000, 5000)
		y = pos[2] + whrandom.randint(-5000, 5000)
		r = whrandom.randint(0,len(keys) - 1)
		key = keys[r]
		if Reference.DefaultObjectData[key][0] == Reference.OBJ_WEAPON:
			try:
				weapon=Bladex.CreateEntity("MyWeapon" + str(i),key,x,posy,y,"Weapon")
				ItemTypes.ItemDefaultFuncs(weapon)
			except:
				pass

	keys = ["Lich","Minotaur","Ork","Skeleton","Great_Ork"]

	for i in range(2):
		r = whrandom.randint(0,len(keys) - 1)
		key = keys[r]
		pers=Bladex.CreateEntity("MyEnemy" + str(i),key,0,0,0,"Person")
		pers.Angle=4.73528938699
		pers.Level=10

		weapon=Bladex.CreateEntity("Weapon" + str(i),"Gladius",0,0,0,"Weapon")
		ItemTypes.ItemDefaultFuncs(weapon)
		Actions.TakeObject(pers.Name,"Weapon" + str(i))
		pers.ActionAreaMin=pow(2,0)
		pers.ActionAreaMax=pow(2,1)
		EnemyTypes.EnemyDefaultFuncs(pers)
		x = pos[0] + whrandom.randint(-5000, 5000)
		y = pos[2] + whrandom.randint(-5000, 5000)
		pers.Position = x, posy, y

	keys = Reference.HealthIncrease.keys()

	for i in range(2):
		r = whrandom.randint(0,len(keys) - 1)
		key = keys[r]
		x = pos[0] + whrandom.randint(-5000, 5000)
		y = pos[2] + whrandom.randint(-5000, 5000)
		Bladex.CreateEntity("MyFood" + str(i),key, x, posy, y,Reference.ObjType(key))
		pocimac.CreateFood("MyFood" + str(i))


def ActivateDebugArena():
	Bladex.AddInputAction("DebugArena", 0)
	Bladex.AssocKey("DebugArena", "Keyboard", "H", 1)
	Bladex.AddBoundFunc("DebugArena", DebugArena)


def Travel():
	player = Bladex.GetEntity("Player1")
	pos = player.Position
	entities = Bladex.GetEntitiesAt(pos[0], pos[1], pos[2], 1000000)
	random_entity_name = entities[whrandom.randint(0, len(entities) -1)]
	random_entity = Bladex.GetEntity(random_entity_name)
	pos = random_entity.Position
	player.Position = pos[0], pos[1] - 5000, pos[2]
	DebugArena()
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5,Travel,())


def ActivateTravel():
	Bladex.AddInputAction("Travel", 0)
	Bladex.AssocKey("Travel", "Keyboard", "T", 1)
	Bladex.AddBoundFunc("Travel", Travel)

