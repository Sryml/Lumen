import Language
import string
import os
import Lumenx

#
import typing

if typing.TYPE_CHECKING:
    apply = lambda fn, args=(), kwds={}: None
    execfile = lambda filename, globals=None, locals=None: None

ForeingDict = {}

if Language.Current != "English":
    filepath = "Data/Locale/" + Language.Current + "/MTexts.py"
    execfile(os.path.join(Lumenx.GetLumenRoot(), filepath), globals(), globals())


# Language.Current=Language.Current


def GetMenuText(item):
    if Language.Current != "English":
        TrWord = ForeingDict.get(item, None)
        if TrWord is None:
            TrWord = ForeingDict.get(string.lower(item), item)
        return TrWord
    return item


def GetInverseMenuText(item):
    if Language.Current != "English":
        for i in ForeingDict.keys():
            if item == ForeingDict[i]:
                return i
        return item
    else:
        return item


# def SetLanguage(l):
#   print "SetLanguage("+l+")"
#   print "This function does not work... yet"
