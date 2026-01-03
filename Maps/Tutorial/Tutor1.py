import darfuncs
import Levers


def JumpCheck():
	global LAST_ACTION
	global CallKey
	
	char = Bladex.GetEntity("Player1")
	
	if LAST_ACTION == "doors":

		Bladex.AddScheduledFunc(Bladex.GetTime() + TIME_TO_CHECK, DoorCheck, ())
		CallKey     = DoorKey
	else:
		Bladex.AddScheduledFunc(Bladex.GetTime() + TIME_TO_CHECK, JumpCheck, ())
	
def JumpKey():
	global LAST_ACTION
	
	if LAST_ACTION == "jump":
		TutorialScorer.ShowBC("Jump1",0)
		GetReady((209667, 1387, 63831),0)
	elif LAST_ACTION == "longjump":
		TutorialScorer.ShowBC("Jump2",0)
		GetReady((211187, 1387, 72217),0.4)
	elif LAST_ACTION == "climb":
		TutorialScorer.ShowBC("Jump3",0)
		GetReady((208452, 1887, 95431),6)		


def SaltoLargo():
	global LAST_ACTION
	
	if LAST_ACTION == "jump":
		TutorialScorer.ShowBC("Exelent",0)
		LAST_ACTION = "longjump"
	else:
		darfuncs.EnterSecIdEvent((212250,0,75000),SaltoLargo)

SaltoLargo()


def Trepa():
	global LAST_ACTION
	
	if LAST_ACTION == "longjump":
		TutorialScorer.ShowBC("Exelent",0)
		LAST_ACTION = "climb"
	else:
		darfuncs.EnterSecIdEvent((209250,0,103000),Trepa)

Trepa()


def FinSaltos():
	global LAST_ACTION
	
	if LAST_ACTION == "climb":
		TutorialScorer.ShowBC("Exelent",0)
		LAST_ACTION = "doors"
	else:
		darfuncs.EnterSecIdEvent((256250,0,127000),FinSaltos)

FinSaltos()
