import darfuncs
import DefaultSelectionData
def BurnCheck():
	global LAST_ACTION
	global CallKey
	
	char = Bladex.GetEntity("Player1")
	
	if LAST_ACTION == "burn":
		if char.Data.selected_entity:
			o = Bladex.GetEntity(char.Data.selected_entity[0])
			if o:
				if (o.Kind=='Antorcha') and (Bladex.GetTime()-DefaultSelectionData.stime<=TIME_TO_CHECK*2):
					TutorialScorer.ShowBC("Burn2",0)
					LAST_ACTION = "taketorch"

		if char.InvRight:
			if (Bladex.GetEntity(char.InvRight).Kind == 'Antorcha'):
				TutorialScorer.ShowBC("Burn3",0)
				LAST_ACTION = "turnon"
					
					
	
	if LAST_ACTION == "taketorch":		
		if char.InvRight:
			if Bladex.GetEntity(char.InvRight).Kind == 'Antorcha':
				TutorialScorer.ShowBC("Burn3",0)
				LAST_ACTION = "turnon"
	
	if LAST_ACTION == "turnon":		
		if char.Data.selected_entity:
			if char.Data.selected_entity[0]=='ap2':
				TutorialScorer.ShowBC("Burn4",0)
				LAST_ACTION = "useturnon"
	
	if LAST_ACTION == "turnon":		
		if char.Data.selected_entity:
			if char.Data.selected_entity[0]=='ap2':
				TutorialScorer.ShowBC("Burn4",0)
				LAST_ACTION = "useturnon"

	if LAST_ACTION == "useturnon":
		if char.InvRight:
			if Bladex.GetEntity(char.InvRight).FiresIntensity[0] < 20 :
				TutorialScorer.ShowBC("Burn5",0)
				LAST_ACTION = "enciendelos"
		else:
			LAST_ACTION = "burn"
			TutorialScorer.ShowBC('Error',0)
	
	if LAST_ACTION == "enciendelos":
		if not Bladex.GetEntity('cir1'):
			Bladex.GetEntity('kaja2').ExclusionMask=0
			TutorialScorer.ShowBC('Burn8',0)
			palancap1.obj.SelfIlum = -1
			LAST_ACTION = "TerminaKema"
	
	if LAST_ACTION == "TerminaKema":
		if palancap1.state:
			palancap1.obj.SelfIlum = 0
			LAST_ACTION = "objects"
			TutorialScorer.ShowBC("Objs0",0)
			
			

	if LAST_ACTION == "objects":
		Bladex.AddScheduledFunc(Bladex.GetTime() + TIME_TO_CHECK, ObjectsCheck, ())
		Bladex.GetEntity("Player1").Life = 15
		CallKey     = ObjectsKey
	else:
		Bladex.AddScheduledFunc(Bladex.GetTime() + TIME_TO_CHECK, BurnCheck, ())
	
def BurnKey():
	global LAST_ACTION
	
	if (LAST_ACTION=="burn") or (LAST_ACTION == "taketorch"):
		TutorialScorer.ShowBC("Burn1",0)
		GetReady((290875.48911, -362.071110004, 127359.200542),4.5)
		LAST_ACTION = "burn"
	elif (LAST_ACTION=="turnon") or (LAST_ACTION == "useturnon"):		
		GetReady((298216, 7, 129114),4.5)
		TutorialScorer.ShowBC("Burn3",0)
		LAST_ACTION="turnon"
		
def JumpBurn():
	global LAST_ACTION
	global CallKey

	BurnCheck()
	CallKey     = BurnKey
	LAST_ACTION = "burn"
	