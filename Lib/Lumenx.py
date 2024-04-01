import Bladex
import BODLoader
import os

ModListPath = "Mods"

__override_funcs = ["GetCurrentMap", "ReadAlphaBitMap", "ReadBitMap"]


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


for __fn in __override_funcs:
    __Bladex.__dict__[__fn] = Bladex.__dict__[__fn]


# Function
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

    root_path = GetRootPath()
    mod_path = "."
    if mod_dir:
        __data.map_list_path = BODLoader.BLModInfo[mod_dir]["MapListPath"]
        mod_path = os.path.join(ModListPath, mod_dir)
    map_path = os.path.join(root_path, mod_path, __data.map_list_path, map_dir)
    cfg_file = os.path.join(map_path, "Cfg.py")
    if not os.path.exists(cfg_file) or (not os.path.isfile(cfg_file)):
        print("Cfg.py file not found!")
        return

    sys_init = os.path.join(root_path, "Lib/sys_init.py")
    execstr = (
        "import Bladex",
        "import sys",
        "Bladex.BeginLoadGame()",
        "root_path = '%s'" % root_path,
        "current_map = '%s'" % map_dir,
        "current_mod = '%s'" % mod_dir,
        # "sys.path.insert(0,'.')",
        # "sys.path.append('../../Bin')",
        # "sys.path.append('../../Scripts')",
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
        "Lumenx.SetRootPath(root_path)",
        "Lumenx.SetCurrentMap(current_map)",
        "Lumenx.SetCurrentMod(current_mod)",
        "del root_path, current_map, current_mod",
        "execfile('%s')" % sys_init,
        "execfile('%s')" % cfg_file,
        "Bladex.DoneLoadGame()",
    )
    Bladex.BeginLoadGame()
    os.chdir(map_path)
    Bladex.CloseLevel(string.join(execstr, ";"), map_dir)


def ReadAlphaBitMap():
    pass


def ReadBitMap():
    pass


def SetCurrentMap(map_dir):
    __data.current_map = map_dir


def SetCurrentMod(mod_dir):
    __data.current_mod = mod_dir


def SetRootPath(path):
    __data.root_path = os.path.normpath(path)


# Override function
for __fn in __override_funcs:
    Bladex.__dict__[__fn] = globals()[__fn]


"""
AddPostloadCB
AddPreloadCB
CallPostloadCB
CallPreloadCB
GetCurrentMap
GetCurrentMod
GetMapListPath
GetPostloadCB
GetPreloadCB
GetRootPath
LoadLevel
ReadAlphaBitMap
ReadBitMap
SetCurrentMap
SetCurrentMod
SetRootPath
"""
