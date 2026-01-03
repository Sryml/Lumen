import TutorialScorer
import acts
import BInput
import Bladex
import Reference
import Scorer
import AuxFuncs

TIME_TO_CHECK = 0.05
SLEEPWALKER = ['WLK','WBK']

#
# Used to Check if the lesson is ready
#######################################
def BasicCheck():
	global LAST_ACTION
	global CallKey
	global SLEEPWALKER
	
	char = Bladex.GetEntity("Player1")
	
	if LAST_ACTION == "start":
		if char.AnimFullName in SLEEPWALKER:
			SLEEPWALKER.remove(char.AnimFullName)
			if len(SLEEPWALKER)==0:
				TutorialScorer.ShowBC("Walk2",0)
				LAST_ACTION = "run"
	if LAST_ACTION == "run":
		if  char.AnimFullName == 'JOG':
			TutorialScorer.ShowBC("Exelent",0)
			LAST_ACTION = "180g"
	elif LAST_ACTION == "180g":
		if  char.AnimFullName[len(char.AnimFullName)-4:] == 'turn':
			TutorialScorer.ShowBC("Exelent",0)
			LAST_ACTION = "sneak"
	elif LAST_ACTION == "sneak":
		if  char.AnimFullName == 'SNK':
			TutorialScorer.ShowBC("Exelent",0)
			LAST_ACTION = "hit"
	elif LAST_ACTION == "hit":
		if string.find(char.AnimFullName, "_g_") != -1:
			TutorialScorer.ShowBC("Jump0",0)
			LAST_ACTION = "jump"
			CallKey     = JumpKey

	if LAST_ACTION == "jump":
		Bladex.AddScheduledFunc(Bladex.GetTime() + TIME_TO_CHECK, JumpCheck, ())
	else:
		Bladex.AddScheduledFunc(Bladex.GetTime() + TIME_TO_CHECK, BasicCheck, ())
	#print char.AnimFullName[len(char.AnimFullName)-5:len(char.AnimFullName)-1]
	
#
# Used to Restart Lessons
############################
def GetReady(pos,ang):
	# camera to player
	cam = Bladex.GetEntity("Camera")

	cam.Cut()
	AuxFuncs.FadeFrom(1.0,0.0,0,0,0)

	char = Bladex.GetEntity("Player1")
	char.UnFreeze()
	char.Alpha    = 1
	char.SelfIlum = 0
	char.Wuea=Reference.WUEA_ENDED	
	char.LaunchAnmType("Rlx")
	char.Data.ReSpawn("Player1")
	char.Position = pos
	char.Angle    = ang
	Scorer.SetVisible(0)
	cam.SetPersonView("Player1")
	Bladex.AddScheduledFunc(Bladex.GetTime() + 1.0, Scorer.SetVisible, (1,))
	Bladex.ActivateInput()
	

def BasicKey():
	global LAST_ACTION
	
	if (LAST_ACTION == "run"):
		TutorialScorer.ShowBC("Walk2",0)
		GetReady((198292, 1387, 29627),0)
		LAST_ACTION = "run"
	elif LAST_ACTION == "180g":
		TutorialScorer.ShowBC("Walk3",0)
	elif LAST_ACTION == "sneak":
		TutorialScorer.ShowBC("Walk4",0)
	elif LAST_ACTION == "hit":
		TutorialScorer.ShowBC("Walk5",0)

def TutorKey():
	global CallKey
	char = Bladex.GetEntity("Player1")
	if( string.find(char.AnimFullName, "tke"  )==-1 
	and string.find(char.AnimFullName, "eat"  )==-1 
	and string.find(char.AnimFullName, "drp"  )==-1 
	and string.find(char.AnimFullName, "drink")==-1 
	and string.find(char.AnimFullName, "key"  )==-1 
	and string.find(char.AnimFullName, "fire" )==-1 
	and string.find(char.AnimFullName, "1tw"  )==-1 ):
		CallKey()
	

def StartTutorial():
	#### Disable the Travel Book ####
	Bladex.RemoveInputAction("LaunchTravel")
	Bladex.RemoveBoundFunc("LaunchTravel",acts.ExecTravelBookNP)
	
	#### F1 is "Tutorial" ####	
	Bladex.AddInputAction("Tutorial", 0)	
	Bladex.AssocKey("Tutorial", "Keyboard", "F1", ON_PRESS)
	Bladex.AssocKey("Tutorial", "Gamepad", "ButtonBack", ON_PRESS)
	Bladex.AddBoundFunc("Tutorial", TutorKey)
	TutorialScorer.wMultiText.SetColor(255,255,255)
	TutorialScorer.ShowBC("Walk1",0)
	BasicCheck()





LAST_ACTION = "start"
CallKey     = BasicKey
StartTutorial()

def NoneFunc():
	pass

def RestoreCallKey(LastCallKey):
	global CallKey
	CallKey = LastCallKey
	TutorialScorer.ShowBC("death",0)

def MuereMiNene(charname):
	global CallKey
	
	LastCallKey = CallKey
	CallKey = NoneFunc
	Bladex.AddScheduledFunc(Bladex.GetTime() + 15, RestoreCallKey, (LastCallKey,))
	

char.ImDeadFunc = MuereMiNene