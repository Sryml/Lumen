# solo para dos jugadores modo Kombat
def AhoraSiEncarate(EntityName):	
	CHAR = Bladex.GetEntity(EntityName)
	if PJ[0] != EntityName :
		CHAR.SetActiveEnemy(Bladex.GetEntity(PJ[0]))
	else:
		CHAR.SetActiveEnemy(Bladex.GetEntity(PJ[1]))

def Encarate(EntityName):
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.125, AhoraSiEncarate,(EntityName,))

def xxxSwitchFragViewer(xx=0,xxx=0,xxxxx=0):
	NetScorer.SwitchFragViewer()

def NetBinds(PlayerName):
	Bladex.AddBoundFunc("SelectEnemy",Encarate)
	Bladex.AddBoundFunc("Show Scorer", DefArgWrapper (PlayerName, xxxSwitchFragViewer))

netgame.Bind("SelectEnemy",   Encarate,0)