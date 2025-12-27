


import sys

sys.path.append("../../Stats")

from CharData import CharMaxLifeValue
from CharData import CharMaxEnergyValue
from CharData import CharDamageData
from CharData import CharDefenseData
from CharData import CharExperienceCost
from CharData import CharExperienceReward
from CharData import CharResistances
from CharData import CharAccuracy


sys.path.remove("../../Stats")
# Si alguien sabe alguna forma mejor de hacer que solamente se pueda importar desde este archivo que lo haga
 

__MAX_LEVEL=19

def GetMaxLevel():
	return __MAX_LEVEL



def GetCharMaxLife(charkind,level):
  if level>__MAX_LEVEL:
    level=__MAX_LEVEL
  try:
    return CharMaxLifeValue[charkind][level]
  except:
    return CharMaxLifeValue['Default'][level]

def GetCharMaxEnergy(charkind,level):
  if level>__MAX_LEVEL:
    level=__MAX_LEVEL
  try:
    return CharMaxEnergyValue[charkind][level]
  except:
    return CharMaxEnergyValue['Default'][level]



def GetCharDamageData(charkind,level):
  if level>__MAX_LEVEL:
    level=__MAX_LEVEL
  try:
    return CharDamageData[charkind][level]
  except:
    try:
      return CharDamageData['Default'][level]
    except:
      return 0.0


def GetCharDefenseData(charkind,level):
  if level>__MAX_LEVEL:
    level=__MAX_LEVEL
  try:
    return CharDefenseData[charkind][level]
  except:
    try:
      return CharDefenseData['Default'][level]
    except:
      return 0.0




def GetCharExperienceCost(charkind,level):
  if level>__MAX_LEVEL:
    level=__MAX_LEVEL
  try:
    return CharExperienceCost[charkind][level]
  except:
    return CharExperienceCost['Default'][level]





def GetCharExperienceReward(charkind,level):
  # print "GetCharExperienceReward()",charkind,level
  if level>__MAX_LEVEL:
    level=__MAX_LEVEL
  try:
    return CharExperienceReward[charkind][level]
  except:
    return CharExperienceReward['Default'][level]

def GetCharResistances(charkind):  
  try:
    return CharResistances[charkind]
  except:
    return CharResistances['Default']

def GetCharAccuracy(charkind,level):
  if level>__MAX_LEVEL:
    level=__MAX_LEVEL
  try:
    return CharAccuracy[charkind][level]
  except:
    return CharAccuracy['Default'][level]
