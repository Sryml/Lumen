import AuxFuncs
import Bladex


                  #################################
#-------------##### Apagado y encendido de luces  #####----------------#

LightDictionary={} # dictionary of functions

LightSpeed     =   0.02
LightSetInens  = 130.0 
LightSetRadius =   0.03
LightSetColor  = (255,165,64)

#
# Adds the predefined lights values
#---------------------------------------
def AddLightData(objname,Inens=LightSetInens,Radius=LightSetRadius,Color=LightSetColor):
   if(not LightDictionary.has_key( objname ) ):
     LightDictionary[objname] = Inens,Radius,Color

def GetLightData(objname):
   global LightSetRadius
   global LightSetInens
   global LightSetColor
   
   if(LightDictionary.has_key( objname ) ):
     LightSetInens  = LightDictionary[objname][0]
     LightSetRadius = LightDictionary[objname][1]
     LightSetColor  = LightDictionary[objname][2]





def SetLightSpeed(xxx):
  global LightSpeed
  LightSpeed = xxx

def SetLightInens(xxx):
  global LightSetInens
  LightSetInens = xxx

def SetLightRadius(xxx):
  global LightSetRadius
  LightSetRadius = xxx


#
# Cambia la intensidad de la antorcha
#------------------------------------------
def SetLightIntesity(LightName,Intens):
  global LightSetRadius
  global LightSetInens

  o = Bladex.GetEntity(LightName)
  o.Lights=[ (LightSetInens*Intens,LightSetRadius,LightSetColor) ]
  o.FiresIntensity=[ 20-20*Intens ]

#
# Obtiene la intensidad de la antorcha
#------------------------------------------
def GetLightIntesity(LightName):
  global LightSetRadius
  global LightSetInens
  
  o = Bladex.GetEntity(LightName)
  spot = AuxFuncs.GetSpot(o)

  spot.SizeFactor = spot.Intensity/LightSetInens

  return spot.Intensity/LightSetInens


Bladex.CreateTimer("LightTimer",0.2)


def TurnOffTimer(e_name, time):
  global LightSpeed
  
  Intesity = GetLightIntesity(e_name)-LightSpeed*4  
    
  if(Intesity<=0):
    o = Bladex.GetEntity(e_name)
    o.TimerFunc = ""    
    o.RemoveFromList("LightTimer")
    Intesity = 0
  
  SetLightIntesity(e_name,Intesity )

#
# Apaga lentamente una luz
#---------------------------
def TurnOffLight(LightName):

  o = Bladex.GetEntity(LightName)
  o.SubscribeToList("LightTimer")
  o.TimerFunc=TurnOffTimer


def TurnOnTimer(e_name, time):
  global LightSpeed
  global LightSetInens
  global LightSetRadius  
  global LightSetColor

  AuxLightSetInens  = LightSetInens
  AuxLightSetRadius = LightSetRadius
  GetLightData(e_name)

  Intesity = GetLightIntesity(e_name)+LightSpeed*4  
    
  if(Intesity>=1):
    o = Bladex.GetEntity(e_name)
    o.TimerFunc = ""
    o.RemoveFromList("LightTimer")
    Intesity = 1
    
  SetLightIntesity(e_name,Intesity )

  LightSetInens  = AuxLightSetInens
  LightSetRadius = AuxLightSetRadius


    
#
# Enciende lentamente una luz
#------------------------------
def TurnOnLight(LightName):
  global LightSetInens
  global LightSetRadius
  global LightSetColor

  GetLightData(LightName)
  AddLightData(LightName,LightSetInens,LightSetRadius,LightSetColor)
  
  o = Bladex.GetEntity(LightName)
  o.SubscribeToList("LightTimer")
  o.TimerFunc = TurnOnTimer

#-------------##### Apagado y encendido de luces  #####----------------#
                  #################################

def SaveData(filename):
  import cPickle
  import GameStateAux

  funcfile=open(filename,"wt")
  p=cPickle.Pickler(funcfile)
  p.persistent_id=GameStateAux.persistent_id
  d=(LightDictionary,
     LightSpeed,
     LightSetInens,
     LightSetRadius,
     LightSetColor,
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

  global LightDictionary
  global LightSpeed
  global LightSetInens
  global LightSetRadius
  global LightSetColor

  LightDictionary    = d[0]
  LightSpeed         = d[1]
  LightSetInens      = d[2]
  LightSetRadius     = d[3]
  LightSetColor      = d[4]

import GameState
GameState.ModulesToBeSaved.append(__import__(__name__))
