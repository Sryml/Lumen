##########################################
##########################################
#### 
####	ExtraDataFunc.py
####
##########################################
##########################################

import cPickle

def SaveExtraData(filename,data):
	file=open(filename,"wt")
	p=cPickle.Pickler(file)	
	p.dump(data)
	file.close()

def LoadExtraData(filename):
	file=open(filename,"rt")
	p=cPickle.Unpickler(file)
	data=p.load()
	file.close()

	return data
