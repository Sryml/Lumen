import Language
import string
import typing

if typing.TYPE_CHECKING:
   ForeingDict = {}


if Language.Current != "English":
	execfile("../../Data/Menu/"+Language.Current+".py")


Language.Current=Language.Current


def GetMenuText(item):
  if Language.Current!="English":
    TrWord = ForeingDict.get(item,None)
    if TrWord is None:
      TrWord = ForeingDict.get(string.lower(item),item)
    return TrWord
  return item



def GetInverseMenuText(item):
  if Language.Current!="English":
    for i in ForeingDict.keys():
      if item==ForeingDict[i]:
        return i
    return item
  else:
    return item



def SetLanguage(l):
  print "SetLanguage("+l+")"
  print "This function does not work... yet"