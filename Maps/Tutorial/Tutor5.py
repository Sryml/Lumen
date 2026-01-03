#
# La armeria
#
import darfuncs
import Ontake
import string
import ItemTypes
import CharStats
import Reference

showmsg = 0
def WeaponCheck():
	global LAST_ACTION
	global CallKey
	global showmsg
	
	char = Bladex.GetEntity("Player1")
	
	if LAST_ACTION == "facing":
		if (char.ActiveEnemy=='Tramposienta') and (showmsg==''):
			TutorialScorer.ShowBC("Weapons13",0)
			showmsg='Tramposienta'
		if (char.ActiveEnemy!='Tramposienta') and (showmsg=='Tramposienta'):
			TutorialScorer.ShowBC("Weapons15",0)
			LAST_ACTION = "moving"
			
	if LAST_ACTION == "strafe":
		anix =         string.find(char.AnimFullName, "_d_l") != -1
		anix = anix or string.find(char.AnimFullName, "_d_b") != -1
		anix = anix or string.find(char.AnimFullName, "_d_r") != -1
		
		if anix and not (char.AnimFullName in showmsg):
			showmsg.append(char.AnimFullName)
			if len(showmsg) == 3:
				TutorialScorer.ShowBC('Exelent',0)
				LAST_ACTION = "fight"
				char.PartialLevel = CharStats.GetCharExperienceCost(char.CharType,0)-5
				Scorer.SetLevelBarValue(char.PartialLevel)
				
	if (LAST_ACTION == "fight") and (TutorialScorer.LastText != "Exelent"):
		if (char.GetInventory().GetActiveWeapon() == myw.Name) and (not UsaEscudo or char.InvLeft!=""):
			if showmsg==None:
				TutorialScorer.ShowBC('Weapons18',0)
				showmsg = []
			if char.AnimFullName == 'Rlx_vt':
				TutorialScorer.ShowBC('Weapons7',0)
			else:
				if string.find(char.AnimFullName, "_g") != -1:
					if not (char.AnimFullName in showmsg):
						showmsg.append(char.AnimFullName)
						if len(showmsg) == 4:
							TutorialScorer.ShowBC('Weapons19',0)
							LAST_ACTION = "killhim"
		else:
			showmsg=None
			if UsaEscudo and char.InvLeft=="" and char.InvRight==myw.Name:
				TutorialScorer.ShowBC('Weapons22',0)
			else:
				TutorialScorer.ShowBC('Weapons17',0)
					
	if LAST_ACTION == "bow":
		Bladex.AddScheduledFunc(Bladex.GetTime() + TIME_TO_CHECK, BowCheck, ())
		CallKey     = BowKey
	else:
		Bladex.AddScheduledFunc(Bladex.GetTime() + TIME_TO_CHECK, WeaponCheck, ())



def WeaponKey():
	global LAST_ACTION
	global showmsg
	
	char = Bladex.GetEntity("Player1")
	
	inv = char.GetInventory()
	if LAST_ACTION == "weapons":
		if inv.nWeapons or inv.nShields:
			if inv.nWeapons >= 3:
				if inv.nShields:
					if inv.nShields >= 2:
						LAST_ACTION = "facing"
					else:
						TutorialScorer.ShowBC("Weapons11",0)
				else:	
					
					TutorialScorer.ShowBC("Weapons10",0)
			else:
				if inv.nWeapons == 0:
					TutorialScorer.ShowBC("Weapons",0)
				elif inv.nWeapons == 1:
					TutorialScorer.ShowBC("Weapons9",0)
				elif inv.nWeapons == 2:
					TutorialScorer.ShowBC("Weapons23",0)
		else:
			TutorialScorer.ShowBC("Weapons",0)
		GetReady((433856, 4887, 63629),3.1415)
	
	if LAST_ACTION == "facing":
		GetReady((435507.111341, 4887.9288938, 40805.077143),0)
		char.SetActiveEnemy("")
		TutorialScorer.ShowBC("Weapons12",0)
		showmsg = ""

	if LAST_ACTION == "moving":
		GetReady((435507.111341, 4887.9288938, 40805.077143),0)		
		TutorialScorer.ShowBC('Weapons14',0)
		Bladex.AddScheduledFunc(Bladex.GetTime() + 1.0, CambiaAEsquivas, ())

	if LAST_ACTION == "strafe":
		GetReady((435507.111341, 4887.9288938, 40805.077143),0)		
		TutorialScorer.ShowBC('Weapons16',0)
		showmsg = []

	if LAST_ACTION == "fight":
		GetReady((435507.111341, 4887.9288938, 40805.077143),0)		
		showmsg = None
		TutorialScorer.LastText = ""
	
	if LAST_ACTION == "killhim":
		GetReady((469420, 9112, 62754),3.1415)
		pers=Bladex.GetEntity("kgt1")
		pers.Position = 469468, 9112, 44647
		pers.SetOnFloor()
		char.SetActiveEnemy("kgt1")
		enuno.UnhideBadGuys(1)
		TutorialScorer.ShowBC('Weapons20',0)

	if LAST_ACTION == "killthem":
		GetReady((469420, 9112, 62754),3.1415)
		endos.UnhideBadGuys(2)
		pers=Bladex.GetEntity("kgt2")
		pers.Position = 469468-3000, 9112, 44647
		pers.SetOnFloor()
		char.SetActiveEnemy("kgt2")

		pers=Bladex.GetEntity("kgt3")
		pers.Position = 469468+3000, 9112, 44647
		pers.SetOnFloor()

		TutorialScorer.ShowBC('Weapons21',0)
		
		


def CambiaAEsquivas():
	global LAST_ACTION
	global showmsg
	
	LAST_ACTION = "strafe"
	showmsg = []
	TutorialScorer.LastText = ""
		

def ArmaBuena():
	TutorialScorer.ShowBC("Weapons2",0)
	TutorialScorer.LoadTBSamples()

def ArmaMala():
	TutorialScorer.ShowBC("Weapons1",0)

def ArmaPotente():
	TutorialScorer.ShowBC("Weapons6",0)

def ArmaParaTodos():
	TutorialScorer.ShowBC("Weapons3",0)

def EscudoBonito():
	TutorialScorer.ShowBC("Weapons5",0)


Ontake.AddOnTakeEvent("Amz_Kgt_Dwf_Bar_W",  ArmaParaTodos)
Ontake.AddOnTakeEvent("None_Weapon",        ArmaPotente)
Ontake.AddOnTakeEvent("Dwf_Kgt_1",          EscudoBonito)
Ontake.AddOnTakeEvent("Dwf_Kgt_2",          EscudoBonito)
Ontake.AddOnTakeEvent("Dwf_Kgt_3",          EscudoBonito)

UsaEscudo = 0

if char.Kind[0] == "K":
	Ontake.AddOnTakeEvent("Amz_W",              ArmaMala)
	Ontake.AddOnTakeEvent("Bar_W",              ArmaMala)
	Ontake.AddOnTakeEvent("Dwf_w",              ArmaMala)
	Ontake.AddOnTakeEvent("Kgt_w",              ArmaBuena)
	myw = Bladex.GetEntity("Kgt_w")
	UsaEscudo = 1
if char.Kind[0] == "D":
	Ontake.AddOnTakeEvent("Amz_W",              ArmaMala)
	Ontake.AddOnTakeEvent("Bar_W",              ArmaMala)
	Ontake.AddOnTakeEvent("Dwf_w",              ArmaBuena)
	Ontake.AddOnTakeEvent("Kgt_w",              ArmaMala)
	myw = Bladex.GetEntity("Dwf_w")
	UsaEscudo = 1
if char.Kind[0] == "B":
	Ontake.AddOnTakeEvent("Amz_W",              ArmaMala)
	Ontake.AddOnTakeEvent("Bar_W",              ArmaBuena)
	Ontake.AddOnTakeEvent("Dwf_w",              ArmaMala)
	Ontake.AddOnTakeEvent("Kgt_w",              ArmaMala)
	myw = Bladex.GetEntity("Bar_W")
	UsaEscudo = 0
if char.Kind[0] == "A":
	Ontake.AddOnTakeEvent("Amz_W",              ArmaBuena)
	Ontake.AddOnTakeEvent("Bar_W",              ArmaMala)
	Ontake.AddOnTakeEvent("Dwf_w",              ArmaMala)
	Ontake.AddOnTakeEvent("Kgt_w",              ArmaMala)
	myw = Bladex.GetEntity("Amz_W")
	UsaEscudo = 0

def MuereMalo1():
	global LAST_ACTION
	LAST_ACTION = "killthem"
	TutorialScorer.ShowBC('Weapons24',1)
	TutorialScorer.LoadTBSamples()
	



enuno = darfuncs.E_Grup()

Gladius=Bladex.CreateEntity("TutGladius3","Gladius",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (Gladius)
escudo=Bladex.CreateEntity("TutEsc3kgt","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (escudo)
pers=Bladex.CreateEntity("kgt1","Knight_Traitor",469468, 9112, 44647,"Person")
pers.Angle=0
Actions.TakeObject(pers.Name,Gladius.Name)
Actions.TakeObject(pers.Name,escudo.Name)
EnemyTypes.EnemyDefaultFuncs(pers)
enuno.AddGuy(pers.Name)

enuno.HideBadGuys()
enuno.OnDeath = MuereMalo1


def MuereMalo2():
	global LAST_ACTION
	LAST_ACTION = "bow"
	TutorialScorer.ShowBC('Weapons25',0)



endos = darfuncs.E_Grup()

Gladius=Bladex.CreateEntity("TutGladius3","Gladius",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (Gladius)
escudo=Bladex.CreateEntity("TutEsc3kgt","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (escudo)
pers=Bladex.CreateEntity("kgt2","Knight_Traitor",469468, 9112, 44647,"Person")
pers.Angle=0
Actions.TakeObject(pers.Name,Gladius.Name)
Actions.TakeObject(pers.Name,escudo.Name)
EnemyTypes.EnemyDefaultFuncs(pers)
endos.AddGuy(pers.Name)

Gladius=Bladex.CreateEntity("TutGladius3","Gladius",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (Gladius)
escudo=Bladex.CreateEntity("TutEsc3kgt","Escudo5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (escudo)
pers=Bladex.CreateEntity("kgt3","Knight_Traitor",469468, 9112, 44647,"Person")
pers.Angle=0
Actions.TakeObject(pers.Name,Gladius.Name)
Actions.TakeObject(pers.Name,escudo.Name)
EnemyTypes.EnemyDefaultFuncs(pers)
endos.AddGuy(pers.Name)

endos.HideBadGuys()
endos.OnDeath = MuereMalo2


def JumpWeapon():
	global LAST_ACTION
	global CallKey

	WeaponCheck()
	CallKey     = WeaponKey
	LAST_ACTION = "weapons"	

Bladex.ReadBitMap("../../Data/Icons/pelele.bmp","PeleleIcon")
Reference.EnemiesDefaultScorerData['Spidersmall']=("PeleleIcon","Borgula")
