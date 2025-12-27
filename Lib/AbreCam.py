import Bladex
import netgame
import AuxFuncs

PTS=[]

def AddNode(Source,Target,time=2):
	global PTS
	
	PTS.append(Source,Target,time)

def ResetNode():
	global PTS
	global Counter
	global auxi1
	global auxi2
	global CallBack
	global LastTime
	
	PTS=[]
	Counter = 0
	auxi1 = (0,0,0)
	auxi2 = (0,0,0)
	CallBack = None
	LastTime = 2
	
def SaveNode(time = 2):
	global PTS
	
	cam=Bladex.GetEntity("Camera")
	PTS.append(cam.Position, cam.TPos, time)

def ChNode(idx,time = 2):
	global PTS
	
	cam=Bladex.GetEntity("Camera")
	PTS[idx]=(cam.Position, cam.TPos, time)	

def ZoomNode(idx,Zoom=0.5):
	global PTS
	n = PTS[idx]
	iZoom = 1.0 - Zoom
	PTS[idx] = (n[0][0]*iZoom+n[1][0]*Zoom, n[0][1]*iZoom+n[1][1]*Zoom, n[0][2]*iZoom+n[1][2]*Zoom), n[1], n[2]

	
Counter = 0
auxi1 = (0,0,0)
auxi2 = (0,0,0)
CallBack = None
LastTime = 2

def GetTime(tupla):
	if(len(tupla)==2):
		return 2
	else:
		if(len(tupla)!=3):
			tupla[3]()
		return tupla[2]
	
def FinalAbrePuerta():
	global CallBack
	# retornar la camara a su posicion inicial  
	Cam = Bladex.GetEntity("Camera")
	Cam.SetPersonView("Player1")
	Cam.Cut()
	Bladex.ActivateInput()
	if netgame.GetNetState() == 0:
		import Scorer
		Scorer.SetVisible(1)
	if CallBack:
		CallBack()
		CallBack = None
	
def LoopAbrePuerta():
	global auxi1
	global auxi2
	global Counter
	global PTS
	global LastTime

	cam=Bladex.GetEntity("Camera")
	opos=cam.Position
	tpos=cam.TPos

	if Counter == len(PTS):
		Counter = 0
		if LastTime != 0:
			AuxFuncs.MoveCamFromTo(opos[0], opos[1], opos[2],auxi1[0], auxi1[1], auxi1[2], tpos[0],tpos[1], tpos[2],auxi2[0], auxi2[1], auxi2[2], LastTime, FinalAbrePuerta)
		else:
			FinalAbrePuerta()
	else:
		Point   = PTS[Counter][0]
		Target  = PTS[Counter][1]	
		Counter = Counter + 1 
		AuxFuncs.MoveCamFromTo(opos[0], opos[1], opos[2], Point[0], Point[1], Point[2], tpos[0],tpos[1], tpos[2],Target[0], Target[1], Target[2], GetTime(PTS[Counter-1]), LoopAbrePuerta)

def AbreCam():
	global auxi1
	global auxi2
	global Counter
	global PTS
	
	Counter = 0
	
	Point   = PTS[Counter][0]
	Target  = PTS[Counter][1]	
	Counter = Counter + 1 
	
	# camarita
	Bladex.DeactivateInput()
	if netgame.GetNetState() == 0:
		import Scorer
		Scorer.SetVisible(0)
	cam=Bladex.GetEntity("Camera")
	auxi1=cam.Position
	auxi2=cam.TPos
	if(GetTime(PTS[Counter-1])):
		AuxFuncs.MoveCamFromTo(auxi1[0], auxi1[1], auxi1[2], Point[0], Point[1], Point[2], auxi2[0],auxi2[1], auxi2[2],Target[0], Target[1], Target[2], GetTime(PTS[Counter-1]), LoopAbrePuerta)
	else:
		cam.SType    = 0
		cam.TType    = 0
		cam.Position = Point
		cam.TPos     = Target
		LoopAbrePuerta()


def SaveData(filename):
  import cPickle
  import GameStateAux

  funcfile=open(filename,"wt")
  p=cPickle.Pickler(funcfile)
  p.persistent_id=GameStateAux.persistent_id
  d=(Counter,
     auxi1,
     auxi2,
     CallBack,
     LastTime,
     PTS,
    )
  p.dump(d)
  funcfile.close()


def LoadData(filename):
  import cPickle
  import GameStateAux

  funcfile=open(filename,"rt")
  p=cPickle.Unpickler(funcfile)
  p.persistent_load=GameStateAux.persistent_load
  d=p.load()
  funcfile.close()
  print d

  global Counter
  global auxi1
  global auxi2
  global CallBack
  global LastTime
  global PTS

  Counter    = d[0]
  auxi1      = d[1]
  auxi2      = d[2]
  CallBack   = d[3]
  LastTime   = d[4]
  PTS        = d[5]

import GameState
GameState.ModulesToBeSaved.append(__import__(__name__))
