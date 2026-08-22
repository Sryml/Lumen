


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





def SaveData():
  d=(InitTakeDictionary,)
  return d



def LoadData(d):
  global InitTakeDictionary

  InitTakeDictionary=d[0]



import GameState
GameState.ModulesToBeSaved.append(__import__(__name__))
