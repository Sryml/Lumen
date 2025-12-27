#
#  Libreria para simplificar el manejo de musicas ambientes
#
import Bladex
import darfuncs

def LaunchMusicEvent(musicname):
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent(musicname))

AsociatedMusic = {}
def OnEnterSectorMusic(id):
	global AsociatedMusic
	
	if AsociatedMusic.has_key(id):
		music = AsociatedMusic[id]		
		Bladex.AddScheduledFunc(Bladex.GetTime(),LaunchMusicEvent,(music,))
	else:
		music = None

	for key in AsociatedMusic.keys():
		if AsociatedMusic[key] != music:
			darfuncs.EnterSecIdEvent(key,OnEnterSectorMusic)

def Music2Sector(sec,music):
	global AsociatedMusic
	
	id = darfuncs.GetSectorIdx(sec)
	if not AsociatedMusic.has_key(id):
		darfuncs.EnterSecIdEvent(id,OnEnterSectorMusic)
	
	if music:
		AsociatedMusic[id] = music
	else:
		if AsociatedMusic.has_key(id):
			del AsociatedMusic[id]

##################################################################################

MusicChanges = {}
def OnEnterMusicChange(id):
	global MusicChanges
	
	for mtr in MusicChanges[id]:
		if len(mtr)==2:
			Music2Sector(mtr[0],mtr[1])
		else:
			LaunchMusicEvent(mtr[0])
	
	del MusicChanges[id]
	
	for key in MusicChanges.keys():
		darfuncs.EnterSecIdEvent(key,OnEnterMusicChange)


def ModifyMusicEvent(sec,tarsec,music=None):
	global MusicChanges
	
	id = darfuncs.GetSectorIdx(sec)
	ev = darfuncs.GetSectorIdx(tarsec),music
	if not MusicChanges.has_key(id):
		MusicChanges[id] = [ev]
		darfuncs.EnterSecIdEvent(id,OnEnterMusicChange)
	else:
		MusicChanges[id].append(ev)
	
def AddPrelude(sec,Prelude):
	global MusicChanges
	
	id = darfuncs.GetSectorIdx(sec)
	ev = (Prelude,)
	if not MusicChanges.has_key(id):
		MusicChanges[id] = [ev]
		darfuncs.EnterSecIdEvent(id,OnEnterMusicChange)
	else:
		MusicChanges[id].append(ev)


def SaveData(filename):
  import cPickle
  import GameStateAux

  funcfile=open(filename,"wt")
  p=cPickle.Pickler(funcfile)
  p.persistent_id=GameStateAux.persistent_id
  d=(AsociatedMusic,MusicChanges)
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

  global AsociatedMusic
  global MusicChanges

  AsociatedMusic=d[0]
  MusicChanges=d[1]

import GameState
GameState.ModulesToBeSaved.append(__import__(__name__))
