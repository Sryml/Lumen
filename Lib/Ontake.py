


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









def SaveData():
  d=(TakeDictionary,)
  return d



def LoadData(d):
  global TakeDictionary

  TakeDictionary=d[0]


import GameState
GameState.ModulesToBeSaved.append(__import__(__name__))



