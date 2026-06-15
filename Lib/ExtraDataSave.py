##########################################
##########################################
#### 
####	ExtraDataFunc.py
####
##########################################
##########################################

import cPickle

def SaveExtraData(filename,data):
	import GameStateAux
	file=open(filename,"wt")
	p=cPickle.Pickler(file)	
	p.persistent_id=GameStateAux.persistent_id
	p.dump(data)
	file.close()

def LoadExtraData(filename):
	import GameStateAux
	file=open(filename,"rt")
	p=cPickle.Unpickler(file)
	p.persistent_load=GameStateAux.persistent_load
	data=p.load()
	file.close()

	return data
