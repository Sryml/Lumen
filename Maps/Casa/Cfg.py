import Lumenx
execfile("../../scripts/dserver.py")

if ContinueLoad:
	
	import Bladex
	import MemPersistence
	
	import LoadBar
	import Reference
	
	#lb=None
	
	#lb=LoadBar.DemoProgressBar(294,"Blade_progress.jpg",0)
	LoadBar.DemoProgressBar(220,"Blade_progress.jpg")
	
	execfile("../../Scripts/sys_init.py")
	
	Bladex.ReadLevel("casa.lvl")
	
	execfile("../../Scripts/BladeInit.py")
	
	execfile ("sonidos.py")
	execfile ("Sonidospuntuales.py")
	
	execfile ("sirena.py")
	# execfile ("selec.py")
	execfile ("selec_wide.py")
	execfile ("sol.py")
	execfile ("agua.py")
	execfile ("objs.py")
	
	Bladex.AddScheduledFunc(Bladex.GetTime(),SetCameraInicio,())
	
	import Scorer
	import Menu
	import MenuWidget
	
	Scorer.SetVisible(0)
	Bladex.SetListenerPosition(2)
	Menu.GetMenuItem(['GAME','SAVE GAME'])["Focusable"] = 0
	Menu.GetMenuItem(['GAME','START NEW GAME'])["Name"] = MenuText.GetMenuText("START GAME")
	Menu.ActivateMenu()
	
	if MemPersistence.Get("MapAlreadyLoaded"):
		Menu.LoadPlayerSelect(0)
	
	CurrentPerson = 3
	
	import Demo_Stuff
	
	Demo_Stuff.OnEnterDemo = OnEnterDemoCasa
	Demo_Stuff.OnExitDemo = OnLeaveDemoCasa
	
	#lb.Clear()
	#del lb
