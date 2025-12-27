import Language



if Language.Current != "English":
	execfile("../../Data/Menu/"+Language.Current+".py")


Language.Current=Language.Current


def GetMenuText(item):
  if Language.Current!="English":
    TrWord=item
    try:
      TrWord=ForeingDict[item]
    except:
      pass
    return TrWord
  else:
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