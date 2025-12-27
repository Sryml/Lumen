


TakeDictionary={} # dictionary of functions

#
#   This function adds an event to the dictionary
#############################################################
def AddOnTakeEvent(objname, funct):
  TakeDictionary[objname] = funct
  
#
#   This function adds an event to the dictionary
#############################################################
def DelOnTakeEvent(objname):
  if( TakeDictionary.has_key( objname ) ):
    del  TakeDictionary[objname] 

#
#   This function call an object if is added to the inventory.
#  The name of the object is the only parameter
#############################################################
def OnTakeFunc(objname):
  if( TakeDictionary.has_key( objname ) ):
    TakeDictionary[ objname ]()









def SaveData(filename):
  import cPickle
  import GameStateAux

  funcfile=open(filename,"wt")
  p=cPickle.Pickler(funcfile)
  p.persistent_id=GameStateAux.persistent_id
  d=(TakeDictionary,)
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

  global TakeDictionary


  TakeDictionary=d[0]


import GameState
GameState.ModulesToBeSaved.append(__import__(__name__))



