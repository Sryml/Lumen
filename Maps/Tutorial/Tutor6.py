#
# La armeria
#
import darfuncs
import Ontake
import string
import ItemTypes
import CharStats
import Reference

def GetArrowState(char):
	inv = char.GetInventory()
	qvn = inv.GetSelectedQuiver()
	if qvn:
		qvr = Bladex.GetEntity(qvn)
		gotarrows = qvr.Data.NumberOfArrows()>0
	else:
		gotarrows = 0
	return (char.InvRight and (Bladex.GetEntity(char.InvRight).Kind == "Flecha")) or gotarrows

def BowCheck():
	global LAST_ACTION
	global CallKey
	
	char = Bladex.GetEntity("Player1")
	
	if LAST_ACTION == "bow":
		if GotABow and GotAQuiver:
			LAST_ACTION = "bowsetup"
			TutorialScorer.ShowBC("Bow1",1)

	if LAST_ACTION == "bowsetup":
		if (char.InvLeft=="Arco") and (char.InvRight):
			if Bladex.GetEntity(char.InvRight).Kind == "Flecha":
				LAST_ACTION = "arrowready"
				BowKey()
	
	if LAST_ACTION == "arrowready": 
		if string.find(char.AnimFullName, "_b3")!=-1:
			TutorialScorer.ShowBC("Bow4",1)
			LAST_ACTION = "launchit"
		else:
			if GetArrowState(char):
					TutorialScorer.ShowBC("Bow2",1)
			else:
					TutorialScorer.ShowBC("Bow3",1)
					CreaCarcaj()

	if LAST_ACTION == "launchit":
		if string.find(char.AnimFullName, "_b3")==-1:
			TutorialScorer.ShowBC("Bow2",1)
			LAST_ACTION = "arrowready"
	
	
	if LAST_ACTION == "WaitForNext" or LAST_ACTION == "EndOfTutorial":
		if not GetArrowState(char):
			TutorialScorer.ShowBC("Bow3",1)
			CreaCarcaj()
		
	Bladex.AddScheduledFunc(Bladex.GetTime() + TIME_TO_CHECK, BowCheck, ())


def ElGranFinalDelComienzo():
	char = Bladex.GetEntity("Player1")

	if char.Kind[0] == "B":
		Bladex.LoadLevel("Barb_M1")
	elif char.Kind[0] == "K":
		Bladex.LoadLevel("Ragnar_M2")
	elif char.Kind[0] == "D":
		Bladex.LoadLevel("Dwarf_M3")
	elif char.Kind[0] == "A":
		Bladex.LoadLevel("Ruins_M4")
	else:
		print "ERROR ! THE CHARKIND DOES NOT EXIST!"


def BowKey():
	global LAST_ACTION
	global showmsg
	
	char = Bladex.GetEntity("Player1")
	
	
	inv = char.GetInventory()
	if LAST_ACTION == "bow":
		GetReady((494722, 8886, 41864),-3.14159/2)
		TutorialScorer.ShowBC("Bow",0)
	
	if LAST_ACTION == "bowsetup":
		GetReady((494722, 8886, 41864),-3.14159/2)
		TutorialScorer.ShowBC("Bow1",0)
		
	if LAST_ACTION == "arrowready":
		GetReady((504935, 8985, 29529),-3.14159/2)
		TutorialScorer.ShowBC("Bow2",1)
	
	if LAST_ACTION == "EndOfTutorial":
		TutorialScorer.ShowBC("Final",1)
		LAST_ACTION == "TeJodes"
		Scorer.SetVisible(0)
		Bladex.DeactivateInput()
		AuxFuncs.FadeTo(5.0,5.0,0,0,0)
		Bladex.AddScheduledFunc(Bladex.GetTime() + 8.0, ElGranFinalDelComienzo, ())
		





GotABow    = 0
GotAQuiver = 1

def CojeArco():
	global GotABow
	GotABow = 1

def CojeCarcaj():
	global GotAQuiver
	GotAQuiver = 1

def CreaArco():
	o=Bladex.CreateEntity("Arco","Arco",501916.279512,9002.826906,43593.373290,"Weapon")
	ItemTypes.ItemDefaultFuncs (o)
	o.Scale=1.000000
	o.Orientation=0.609264,0.477714,-0.358884,0.521334
	Ontake.AddOnTakeEvent(o.Name,  CojeArco)

def CreaCarcaj():
	global GotAQuiver
	global LAST_ACTION
	if GotAQuiver:
		o=Bladex.CreateEntity("Carcaj","Carcaj",500470.777385,9946.213216,42917.831194)
		o.Scale=1.000000
		o.Orientation=0.003808,0.497074,0.021758,-0.867427
		ItemTypes.ItemDefaultFuncs (o)
		o.Data.ArrowsLeft=10
		Ontake.AddOnTakeEvent(o.Name,  CojeCarcaj)
		GotAQuiver = 0
		LAST_ACTION ="bow"
		return o.Name

xx = LAST_ACTION
CreaArco()
CreaCarcaj()
LAST_ACTION =xx

_EN_EL_BLANCO  =  1785
_BUEN_TIRO     =  23850
_CERCA_PERO_NO =  71514
_PRINCIPANTE   = 191011
_SI_PERO_NO    = 439940




def FlechazoALaDiana(stick,sticker,x,y,z,xc,yc,zc,wcx,wcy,wcz,wdx,wdy,wdz):
	print sticker,x,y,z
	global LAST_ACTION
	
	distance = (Diana.Position[1]-y)**2+(Diana.Position[2]-z)**2
	if distance <1785:
		TutorialScorer.ShowBC("Bow5",1)
		LAST_ACTION = "EndOfTutorial"
	elif distance <23850:
		TutorialScorer.ShowBC("Bow6",1)
		LAST_ACTION = "EndOfTutorial"
	elif distance <71514:
		TutorialScorer.ShowBC("Bow7",1)
		LAST_ACTION = "EndOfTutorial"
	elif distance <191011:
		TutorialScorer.ShowBC("Bow8",1)
		LAST_ACTION = "EndOfTutorial"
	elif distance <439940:
		TutorialScorer.ShowBC("Bow9",1)
		LAST_ACTION = "WaitForNext"
	else:
		TutorialScorer.ShowBC("Bow10",1)
		LAST_ACTION = "WaitForNext"
	

Diana = Bladex.CreateEntity("Diana","AdoquinRuna", 526246, 7948, 30025,"Physic")
Diana.Scale = 3
Diana.HitFunc = FlechazoALaDiana

def GoBow():
	global LAST_ACTION
	global CallKey

	BowCheck()
	CallKey     = BowKey
	LAST_ACTION = "bow"
