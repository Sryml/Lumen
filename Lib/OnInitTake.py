


InitTakeDictionary={} # Diccionario de funciones a lanzar al intentar coger determinados objetos


# Funciones para gestionar dicho diccionario

def AddOnInitTakeEvent(objname, funct, flag=0):
	InitTakeDictionary[objname]=[funct, flag]

def DelOnInitTakeEvent(objname):
	if(InitTakeDictionary.has_key(objname)):
		del InitTakeDictionary[objname] 


# Funcion para lanzar funciones asociadas al intento de coger un determinado objeto

def OnInitTakeFunc(objname):
	if(InitTakeDictionary.has_key(objname)):
		InitTakeDictionary[objname][0]()
		return InitTakeDictionary[objname][1]





def SaveData(filename):
  import cPickle
  import GameStateAux

  funcfile=open(filename,"wt")
  p=cPickle.Pickler(funcfile)
  p.persistent_id=GameStateAux.persistent_id
  d=(InitTakeDictionary,)
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

  global InitTakeDictionary


  InitTakeDictionary=d[0]



import GameState
GameState.ModulesToBeSaved.append(__import__(__name__))
