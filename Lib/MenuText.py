import Language
import string
import os
import Lumenx

from LumenLib import BUtils

#
import typing

if typing.TYPE_CHECKING:
    apply = lambda fn, args=(), kwds={}: None
    execfile = lambda filename, globals=None, locals=None: None

ForeingDict = BUtils.Dictionary()

if Language.Current != "English":
    name_space = {}
    filepath = "Data/Locale/" + Language.Current + "/MTexts.py"
    execfile(os.path.join(Lumenx.GetLumenRoot(), filepath), name_space, name_space)
    ForeingDict.update(name_space.get("ForeingDict", {}))
    del name_space


# Language.Current=Language.Current


def GetMenuText(item):
    # type: (str) -> str
    if Language.Current != "English":
        TrWord = ForeingDict.get(item, None)
        if TrWord is None:
            TrWord = ForeingDict.get(string.lower(item), item)
        return TrWord # type: ignore
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
