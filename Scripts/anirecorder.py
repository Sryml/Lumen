import Bladex

record = 0
victim = "Player1"

Bladex.CreateTimer("AniMaker",1.0/24.0)

def snapShotTimer(strEntName, fTime):
	Bladex.TakeSnapShot()

def stopSnaps():
	global victim
	global record
	if (not record) : return
	record=0
	print("stop")
	char = Bladex.GetEntity(victim)
	char.TimerFunc=""
	char.RemoveFromList("AniMaker")
	
def startAnim(strAnimName):
	global victim
	char = Bladex.GetEntity(victim)
	char.LaunchAnimation(strAnimName)

def startSnaps():
	global victim
	global record
	if (record) : return
	record = 1
	print("start")
	char = Bladex.GetEntity(victim)	
	char.TimerFunc=snapShotTimer;
	char.SubscribeToList("AniMaker")

def animSnapShot( fTime , strAnimName ="", fLaunchDelay=0.0 ) :
	startSnaps()
	Bladex.AddScheduledFunc( Bladex.GetTime()+fTime, stopSnaps, () )
	if (strAnimName<>"") : Bladex.AddScheduledFunc( Bladex.GetTime()+fLaunchDelay, startAnim, (strAnimName,) )
	
def setVictim(strVictim):
	global victim
	victim=strVictim

# import anirecorder
# anirecorder.setVictim("Player1")
# anirecorder.animSnapShot( 10.0 , "Kgt_g_bad_sword2" )
