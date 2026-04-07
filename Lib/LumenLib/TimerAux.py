import Bladex
import Lumenx
import InitDataField
import ObjStore
import GameState
import GameStateAux
import Reference

import sys
import traceback

#
import typing

if typing.TYPE_CHECKING:
    apply = lambda fn, args=(), kwds={}: None
    execfile = lambda filename, globals=None, locals=None: None
    cmp = lambda x, y: None


# ----------------------------------
SubscribedLists = {}


def CreateTimer(timer_name, period):
    if not SubscribedLists.has_key(timer_name):
        Bladex.CreateTimer(timer_name, period)
        SubscribedLists[timer_name] = []
        o = Bladex.CreateEntity(timer_name, "GhostPointer", 0, 0, 0)
        InitDataField.Initialise(o, Name=timer_name)
        o.Alpha = 0
        o.RemoveFromWorld()
        o.SubscribeToList(timer_name)
        o.TimerFunc = TimerFunc
        return 1
    return 0


def TimerFunc(ent_name, time):
    o = Bladex.GetEntity(ent_name)
    timer_name = o.Data.Name
    l = SubscribedLists.get(timer_name, [])
    for func, args, kwds in l:
        try:
            apply(func, (time,) + args, kwds)
        except:
            if Reference.DEBUG_INFO:
                traceback.print_exc()


def SubscribeToList(timer_name, func, func_args=(), func_kwds={}):
    l = SubscribedLists.get(timer_name)
    item = (func, func_args, func_kwds)
    if (l is None) or (item in l):
        return 0
    l.append(item)
    return 1


def RemoveFromList(timer_name, func, func_args, func_kwds):
    l = SubscribedLists.get(timer_name)
    item = (func, func_args, func_kwds)
    if (l is None) or (item not in l):
        return 0
    l.remove(item)
    return 1


# ----------------------------------
def SaveData(filename):
    GameStateAux.SaveData(filename, SubscribedLists)


def LoadData(filename):
    global SubscribedLists
    SubscribedLists = GameStateAux.LoadData(filename)
    # Reference.debugprint("%s LoadData done." % __name__)


GameState.ModulesToBeSaved.append(sys.modules[__name__])
