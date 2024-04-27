# Author: Sryml
# Email: sryml@hotmail.com
# Python Version: 1.5.2
# License: MIT

import Bladex
import __main__
import os
import sys

ModListPath = "Mods"


######### Set sys.path
def __fn():
    paths = [
        "Bin",
        "Scripts",
        "Scripts/Combos",
        "Scripts/Biped",
        "Lib",
        "Lib/AnmSets",
        "Lib/Widgets",
        "Lib/PythonLib",
        "Lib/PythonLib/Idle')",
        "Lib/PythonLib/lib-tk')",
        "Lib/PythonLib/DLLs')",
        "Lib/PythonLib/Pmw')",
        "Lib/PythonLib/Pmw/Pmw_0_8')",
        "Lib/PythonLib/Pmw/Pmw_0_8/lib')",
    ]

    sys.path = ["."]

    # Determine if it is an original campaign
    if __main__.__dict__.get("current_mod", ""):
        ModRelpath = os.path.join("..", os.path.relpath(".", __main__.map_list_path))
        RootRelpath = os.path.join(ModRelpath, "..", os.path.relpath(".", ModListPath))
    else:
        ModRelpath = ""
        RootRelpath = "../.."
    OriginalRootRelpath = os.path.join(RootRelpath, "..")

    for root in (
        ModRelpath,
        RootRelpath,
        OriginalRootRelpath,
    ):
        if not ModRelpath:
            continue
        for p in paths:
            sys.path.append(os.path.join(root, p))


__fn()
######### sys.path setup completed


# Add True and False to __builtin__
# Use exec to be compatible with formatted documents
exec('sys.modules["__builtin__"].True = (1 == 1)')
exec('sys.modules["__builtin__"].False = (1 == 0)')


import BODLoader
import string
import BInput


# private database
class __data:
    current_map = ""
    current_mod = ""
    map_list_path = "Maps"
    postload_callbacks = {}
    preload_callbacks = {}
    root_path = os.path.normpath(os.path.join(os.getcwd(), "../.."))


# Store original function
class __Bladex:
    pass


__override_funcs = [
    "AddBoundFunc",
    "AddInputAction",
    "AssocKey",
    "GetCurrentMap",
    "GetTimeActionHeld",
    "ReadAlphaBitMap",
    "ReadBitMap",
    "RemoveBoundFunc",
    "RemoveInputAction",
]
for __fn in __override_funcs:  # type: ignore
    __Bladex.__dict__[__fn] = Bladex.__dict__[__fn]  # type: ignore


######### Function Start
def AddBoundFunc(action_name, proc):
    IActions = BInput.GetInputManager().GetInputActions()
    action_name = BInput.GetInternalName(IActions.ID, action_name)
    __Bladex.AddBoundFunc(action_name, proc)  # type: ignore
    return 1


def AddInputAction(action_name, npi):
    val = BInput.GetInputManager().AddInputAction(action_name, npi, dict_only=1)
    if not val:
        return 0

    IActions = BInput.GetInputManager().GetInputActions()
    action_name = BInput.GetInternalName(IActions.ID, action_name)
    __Bladex.AddInputAction(action_name, npi)  # type: ignore
    return 1


def AddPostloadCB(map_token, fn):
    """AddPostloadCB("Barb_M1", fn)\n
    AddPostloadCB("Demo:M1", fn)\n
    Args:
        map_token (str)\n
        fn (function)
    """
    list_ = __data.postload_callbacks.get(map_path, [])
    list_.append(fn)
    __data.postload_callbacks[map_path] = list_


def AddPreloadCB(map_token, fn):
    """AddPreloadCB("Barb_M1", fn)\n
    AddPreloadCB("Demo:M1", fn)\n
    Args:
        map_token (str)\n
        fn (function)
    """
    list_ = __data.preload_callbacks.get(map_path, [])
    list_.append(fn)
    __data.preload_callbacks[map_path] = list_


def AssocKey(action_name, device, key, on_press=1):
    val = BInput.GetInputManager().AssocKey(
        action_name, device, key, on_press, dict_only=1
    )
    if not val:
        return 0

    IActions = BInput.GetInputManager().GetInputActions()
    action_name = BInput.GetInternalName(IActions.ID, action_name)
    __Bladex.AssocKey(action_name, device, key, on_press)  # type: ignore
    return 1


def BladeRawInput(prompt=None):
    "Provides raw_input() for Blade"
    # flush stderr/out first.
    try:
        sys.stdout.flush()
        sys.stderr.flush()
    except:
        pass
    if prompt is None:
        prompt = ""
    ret = Bladex.Input(prompt)
    if ret == 0:
        exec(Raisex(KeyboardInterrupt, "operation cancelled"))
    return ret


def CallPostloadCB():
    pass


def CallPreloadCB():
    pass


def GetCurrentMap():
    return __data.current_map


def GetCurrentMod():
    return __data.current_mod


def GetMapListPath():
    return __data.map_list_path


def GetPostloadCB(map_path):
    return __data.postload_callbacks.get(map_path, [])


def GetPreloadCB(map_path):
    return __data.preload_callbacks.get(map_path, [])


def GetRootPath():
    """Returns the root path of Lumen"""
    return __data.root_path


def GetTimeActionHeld(action_name):
    """Return the amount of milliseconds a key has been hald down, or zero if it is currently considered released"""
    action_name = BInput.GetInternalName(
        BInput.GetInputManager().GetInputActions().ID, action_name
    )
    return __Bladex.GetTimeActionHeld(action_name)  # type: ignore


def LoadComponent(comps):
    import LoadBar


def LoadLevel(map_dir, mod_dir=""):
    # type: (str, str) -> None
    """
    LoadLevel("Barb_M1")\n
    LoadLevel("M1", "Demo")\n
    Args:
        map_dir (str): Map Directory\n
        mod_dir (str, optional): MOD Directory. Defaults to "".
    """
    global ModListPath

    if map_dir == "":
        return

    root_path = GetRootPath()
    if mod_dir:
        map_list_path = BODLoader.BLModInfo[mod_dir]["MapListPath"]
        mod_path = os.path.normpath(os.path.join(root_path, ModListPath, mod_dir))
    else:
        map_list_path = "Maps"
        mod_path = root_path

    map_path = os.path.join(mod_path, map_list_path, map_dir)
    cfg_file = os.path.join(map_path, "Cfg.py")
    if not os.path.exists(cfg_file) or (not os.path.isfile(cfg_file)):
        printx("Cfg.py file not found!")
        return

    # sys_init = os.path.join(root_path, "Lib/sys_init.py")
    execstr = (
        "import Bladex",
        "import sys",
        "Bladex.BeginLoadGame()",
        #
        "Lumen = 1",
        "current_map = '%s'" % map_dir,
        "current_mod = '%s'" % mod_dir,
        "map_list_path = '%s'" % map_list_path,
        "mod_path = '%s'" % mod_path,
        "root_path = '%s'" % root_path,
        # "sys.path.insert(0,'.')",
        # "sys.path.append('../../Bin')",
        # "sys.path.append('../../Scripts')",
        "sys.path.append(mod_path + '/Lib')",
        "sys.path.append(mod_path + '/Lib/PythonLib')",
        "sys.path.append(root_path + '/Lib')",
        "sys.path.append(root_path + '/Lib/PythonLib')",
        "sys.path.append(root_path + '/../Lib')",
        "sys.path.append(root_path + '/../Lib/PythonLib')",
        # "sys.path.append('../../Lib/PythonLib/Idle')",
        # "sys.path.append('../../Lib/PythonLib/lib-tk')",
        # "sys.path.append('../../Lib/PythonLib/DLLs')",
        # "sys.path.append('../../Lib/PythonLib/Pmw')",
        # "sys.path.append('../../Lib/PythonLib/Pmw/Pmw_0_8')",
        # "sys.path.append('../../Lib/PythonLib/Pmw/Pmw_0_8/lib')",
        "import Lumenx",
        "Lumenx.SetCurrentMap(current_map)",
        "Lumenx.SetCurrentMod(current_mod)",
        "Lumenx.SetMapListPath(map_list_path)",
        "Lumenx.SetRootPath(root_path)",
        "del root_path, mod_path, map_dir, current_mod, map_list_path",
        #
        # "execfile('%s')" % sys_init,
        "execfile('%s')" % cfg_file,
        "Bladex.DoneLoadGame()",
    )
    Bladex.BeginLoadGame()
    os.chdir(map_path)
    Bladex.CloseLevel(string.join(execstr, ";"), map_dir)  # type: ignore


# print function
def printx(*values, **kwargs):
    sep = kwargs.get("sep", " ")
    end = kwargs.get("end", "\n")
    file = kwargs.get("file", None)
    flush = kwargs.get("flush", 0)

    output = string.join(map(str, values), sep)  # type: ignore
    if file is None:
        file = sys.stdout
    file.write(output)
    file.write(end)
    # if flush:
    #     file.flush()


def Raisex(exc, msg=""):
    return "raise %s, %s" % (exc, repr(msg))


def ReadAlphaBitMap():
    pass


def ReadBitMap():
    pass


def RemoveBoundFunc(action_name, proc):
    IActions = BInput.GetInputManager().GetInputActions()
    action_name = BInput.GetInternalName(IActions.ID, action_name)
    __Bladex.RemoveBoundFunc(action_name, proc)  # type: ignore
    return 1


def RemoveInputAction(action_name):
    IActions = BInput.GetInputManager().GetInputActions()
    val = IActions.RemoveAction(action_name, dict_only=1)
    if not val:
        return 0

    action_name = BInput.GetInternalName(IActions.ID, action_name)
    __Bladex.RemoveInputAction(action_name)  # type: ignore
    return 1


def SetCurrentMap(map_dir):
    __data.current_map = map_dir


def SetCurrentMod(mod_dir):
    __data.current_mod = mod_dir


def SetMapListPath(path):
    __data.map_list_path = path


def SetRootPath(path):
    __data.root_path = os.path.normpath(path)


# from sys_init.py
def sys_init():
    # Loaded from original
    if not __main__.__dict__.get("Lumen"):
        SetCurrentMap(os.path.basename(os.getcwd()))

    # fmt: off
    import ConsoleOutput
    ConsoleOutput.InitConsole()
    # fmt: on

    sys.modules["__builtin__"].raw_input = BladeRawInput  # type: ignore
    sys.modules["__builtin__"].input = BladeRawInput  # type: ignore
    sys.setcheckinterval(100)  # type: ignore

    Bladex.CloseDebugChannel("DefaultChannel")

    BODLoader.init()

    printx("Executed Lumenx.sys_init")


######### Function End

# Override function
for __fn in __override_funcs:  # type: ignore
    Bladex.__dict__[__fn] = globals()[__fn]  # type: ignore


# Clean up
del __fn, __override_funcs

"""
AddBoundFunc
AddInputAction
AddPostloadCB
AddPreloadCB
AssocKey
BladeRawInput
CallPostloadCB
CallPreloadCB
GetCurrentMap
GetCurrentMod
GetMapListPath
GetPostloadCB
GetPreloadCB
GetRootPath
GetTimeActionHeld
LoadComponent
LoadLevel
printx
Raisex
ReadAlphaBitMap
ReadBitMap
RemoveBoundFunc
RemoveInputAction
SetCurrentMap
SetCurrentMod
SetMapListPath
SetRootPath
sys_init
"""
