import darfuncs

def DoorCheck():
	global LAST_ACTION
	global CallKey
	global palanrsi1
	
	char = Bladex.GetEntity("Player1")
	
	if LAST_ACTION == "lookdoor":
		if char.Data.selected_entity:
			o = Bladex.GetEntity(char.Data.selected_entity[0])
			if o:
				if o.Kind=='Palanca3':
					TutorialScorer.ShowBC("Doors2",0)
					LAST_ACTION = "pulllever"
	if LAST_ACTION == "pulllever":
		if palanrsi1.state:
			TutorialScorer.ShowBC("Exelent",0)
			LAST_ACTION = "button1"
			palanrsi1.obj.SelfIlum = 0
	if LAST_ACTION == "button1":			
		if puertasub1.status:
			Bladex.GetEntity("blosu1").SelfIlum = 0
			Bladex.GetEntity("blosu2").SelfIlum = 0
			TutorialScorer.ShowBC("Exelent",0)
			LAST_ACTION = "burn"

	if LAST_ACTION == "burn":
		Bladex.AddScheduledFunc(Bladex.GetTime() + TIME_TO_CHECK, BurnCheck, ())
		CallKey     = BurnKey
	else:
		Bladex.AddScheduledFunc(Bladex.GetTime() + TIME_TO_CHECK, DoorCheck, ())
	
def DoorKey():
	global LAST_ACTION
	global palanrsi1
	
	if (LAST_ACTION=="doors") or (LAST_ACTION=="lookdoor") or (LAST_ACTION=="pulllever"):
		TutorialScorer.ShowBC("Doors1",0)
		GetReady((259071, -112, 128677),4.5)
		if (LAST_ACTION=="doors"):
			palanrsi1=Levers.PlaceLever("PalanRsi1",Levers.LeverType3,(264872.543696,-168.153978,132269.811808),(0.653282,0.653282,0.270598,-0.270598),1.0)
			palanrsi1.mode=3
			palanrsi1.OnTurnOnFunc=Abrerejas
			palanrsi1.OnTurnOnArgs=()
			
			palanrsi1.OnTurnOffFunc=Cierrarejas
			palanrsi1.OnTurnOffArgs=()
			palanrsi1.obj.SelfIlum = -1
		LAST_ACTION="lookdoor"
				
	elif (LAST_ACTION=="button1"):		
		GetReady((282860, -362, 127889),4.5)
		TutorialScorer.ShowBC('Doors3',0)
		Bladex.GetEntity("blosu1").SelfIlum = -1
		Bladex.GetEntity("blosu2").SelfIlum = -1
