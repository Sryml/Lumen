import darfuncs
import Ontake

nPocimac = -1
GottaAnObject = -1

def TakePoc():
	global nPocimac
	global LAST_ACTION

	nPocimac = nPocimac + 1
	char.Life = 15
	if nPocimac == 1:
		TutorialScorer.ShowBC("Objs1",0)
	elif nPocimac == 2:
		TutorialScorer.ShowUC("Objs3",2)
		LAST_ACTION = "drinking"

def ObjectsCheck():
	global LAST_ACTION
	global CallKey
	global GottaAnObject
	global nPocimac
	
	char = Bladex.GetEntity("Player1")
	
	if (string.find(char.AnimFullName, "eat") != -1):		
		if nPocimac == -1:
			TutorialScorer.ShowBC("Objs9",1)
			nPocimac = 0
			Bladex.GetEntity("poc1").PutToWorld()
			Bladex.GetEntity("poc2").PutToWorld()
			
		
	if (GottaAnObject==0) and char.InvRight and ((char.AnimFullName == 'WBK') or (char.AnimFullName == 'WLK')):
		TutorialScorer.ShowBC("Objs6",1)
		GottaAnObject=1

	if (GottaAnObject==1) and not char.InvRight:
		TutorialScorer.ShowBC("Objs7",0)
		cerradurp2.key="Llavep2"
		GottaAnObject=0

	if (GottaAnObject==-1) and not char.InvRight:
		GottaAnObject=0
		
	if LAST_ACTION == "drinking":
		if(nPocimac == 2) and (char.GetInventory().nObjects<=1):
			LAST_ACTION = "keyready"
			llavep2=Bladex.CreateEntity("Llavep2","Llavecutre",325347.707135,-6072.423105,116732.867860)
			llavep2.Static=0
			llavep2.Scale=1.05
			llavep2.Orientation=0.998865,-0.001117,-0.047581,-0.002111
			darfuncs.SetHint(llavep2,"Iron Key")
			Stars.Twinkle("Llavep2")
			TutorialScorer.ShowBC("Objs4",0)

	if LAST_ACTION == "keyready":
		if char.GetInventory().nKeys:
			if cerradurp2.key:
				TutorialScorer.ShowBC("Objs5",0)
			else:
				TutorialScorer.ShowBC("Objs8",0)
			LAST_ACTION = "gotakey"

	if LAST_ACTION == "gotakey":
		if puerta2.status:
			LAST_ACTION = "weapons"
			WeaponKey()
			
			
	
	if LAST_ACTION == "weapons":
		Bladex.AddScheduledFunc(Bladex.GetTime() + TIME_TO_CHECK, WeaponCheck, ())
		CallKey     = WeaponKey
	else:
		Bladex.AddScheduledFunc(Bladex.GetTime() + TIME_TO_CHECK, ObjectsCheck, ())


Ontake.AddOnTakeEvent("poc1",TakePoc)
Ontake.AddOnTakeEvent("poc2",TakePoc)

def ObjectsKey():
	global LAST_ACTION
	global nPocimac
	
	if (LAST_ACTION == "objects"):
		if nPocimac == -1:
			TutorialScorer.ShowBC("Objs0",0)
		else:
			TutorialScorer.ShowBC("Objs11",0)
	
	if LAST_ACTION == "drinking":
		TutorialScorer.ShowUC("Objs3",2)
	if LAST_ACTION == "gotakey":
		if cerradurp2.key:
			TutorialScorer.ShowBC("Objs5",0)
		else:
			TutorialScorer.ShowBC("Objs8",0)
	if LAST_ACTION == "keyready":
		TutorialScorer.ShowBC("Objs10",0)
			
	char = Bladex.GetEntity("Player1")
	GetReady((329072, -6112, 118755),3.1415)
	char.Life = 15

def JumpObjects():
	global LAST_ACTION
	global CallKey

	BurnCheck()
	CallKey     = ObjectsKey
	LAST_ACTION = "objects"

