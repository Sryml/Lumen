# Author: Sryml
# Email: sryml@hotmail.com
# Python Version: 1.5.2
# License: MIT

import __main__
import os
import sys

ModListPath = "Mods"


# private database
class __data:
    current_map = ""
    current_mod = ""
    # map_list_path = "Maps"
    postload_callbacks = {}
    preload_callbacks = {}
    mod_root = ""
    lumen_root = ""
    blade_root = ""
    asset_path = ()
    asset_path_model = ""
    server_port = 0


######### Initialization #########


def __fn():
    setattr(sys.modules["__builtin__"], "True", (1 == 1))
    setattr(sys.modules["__builtin__"], "False", (1 == 0))

    current_dir = os.getcwd()
    # If it is not the first time to start from Lumen.exe
    if not __main__.__dict__.get("isLumenLoadLevel"):
        f_name = "2ea5b509-3c98-5063-95c2-cae184dc13fd"  # by uuid.uuid5(uuid.NAMESPACE_OID,"Lumen:Port")
        f = open("../../" + f_name, "r")
        __data.server_port = int(f.readline()[:-1])
        __data.lumen_root = os.path.normpath(f.readline()[:-1])
        f.close()
    else:
        __data.server_port = __main__.__dict__["server_port"]
        __data.lumen_root = __main__.__dict__["lumen_root"]
    lumen_root = __data.lumen_root

    __data.blade_root = blade_root = os.path.normpath(lumen_root + "/..")
    __data.mod_root = mod_root = os.path.abspath(os.path.join(current_dir, "../.."))

    if mod_root == lumen_root:
        __data.current_mod = ""
        ModRelpath = ""
        __data.asset_path = (lumen_root, blade_root)
    else:
        __data.current_mod = os.path.basename(mod_root)
        ModRelpath = os.path.relpath(mod_root, current_dir)
        __data.asset_path = (mod_root, lumen_root, blade_root)
    __data.current_map = os.path.basename(current_dir)

    LumenRelpath = os.path.relpath(lumen_root, current_dir)
    BladeRelpath = os.path.relpath(blade_root, current_dir)

    #
    paths = [
        "Bin",
        "Stats",
        "Scripts",
        "Scripts/Combos",
        "Scripts/Biped",
        "Lib",
        "Lib/AnmSets",
        "Lib/Widgets",
        "Lib/PythonLib",
        "Lib/PythonLib/Plat-Win",
        # "Lib/PythonLib/Idle')",
        "Lib/PythonLib/lib-tk')",
        "Lib/PythonLib/DLLs')",
        "Lib/PythonLib/Pmw')",
        # "Lib/PythonLib/Pmw/Pmw_0_8')",
        # "Lib/PythonLib/Pmw/Pmw_0_8/lib')",
    ]

    sys.path = ["."]

    for root in (
        ModRelpath,
        LumenRelpath,
        BladeRelpath,
    ):
        if not root:
            continue
        for p in paths:
            sys.path.append(os.path.join(root, p))


__fn()


# python3-like print function
def printx(*values, **kwargs):
    import string

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


# sys.modules["__builtin__"].printx = printx  # type: ignore

######### Initialization End #########


import string
import imp
import re
import typing
import struct

#
import Bladex
import BInput

#
if typing.TYPE_CHECKING:
    apply = lambda fn, args=(), kwds={}: fn(args, kwds)


#
def Wrapper(func, *args, **kwargs):
    def wrapped(func=func, args=args, kwargs=kwargs):
        return apply(func, args, kwargs)

    return wrapped


# Store original function
sys.modules["Bladex_raw"] = imp.new_module("Bladex_raw")
import Bladex_raw


class __FunctionDecorator:
    def __init__(self):
        self.RawFunc = imp.new_module("RawFunc")

    def Decorator(self, obj, name):
        RawFunc = self.RawFunc
        setattr(RawFunc, name, getattr(obj, name))
        setattr(obj, name, getattr(self, name))

    # builtin module
    def execfile(self, filename, globals=None, locals=None):
        filename = AutomatedAssets(filename)
        if not (globals and locals):
            try:
                1 / 0
            except ZeroDivisionError:
                if not globals:
                    globals = sys.exc_info()[2].tb_frame.f_back.f_globals
                if not locals:
                    locals = sys.exc_info()[2].tb_frame.f_back.f_locals
        return self.RawFunc.execfile(filename, globals, locals)


def __empty_func(*args, **kwargs):
    return "empty_func"


# Backup Bladex functions to Bladex_raw
__bladex_decorators = [
    "AddBoundFunc",
    "AddInputAction",
    "AddMusicEventADPCM",
    "AddMusicEventMP3",
    "AddMusicEventWAV",
    "AssocKey",
    "BodInspector",
    "CreateEntity",
    "CreateSound",
    "GetCurrentMap",
    "GetEntity",
    "GetTimeActionHeld",
    "LoadLevel",
    "LoadSampledAnimation",
    "LoadWorld",
    "ReadAlphaBitMap",
    "ReadBitMap",
    "ReadLevel",
    "RemoveBoundFunc",
    "RemoveInputAction",
    "SetGhostSectorGroupSound",
    "SetGhostSectorSound",
]
for __fn in __bladex_decorators:  # type: ignore
    Bladex_raw.__dict__[__fn] = Bladex.__dict__.get(__fn, __empty_func)  # type: ignore


######### Proxy
class B_PyEntity_Proxy:
    def __init__(self, target):
        self.target = target
        self.is_proxy = 1

    def __getstate__(self):
        return hasattr(self.target, "Name") and self.target.Name or None

    def __setstate__(self, state):
        if state:
            self.target = Bladex.GetEntity(state)
        else:
            self.target = None
        self.is_proxy = 1

    def __getattr__(self, attr):
        return getattr(self.target, attr)

    def __setattr__(self, attr, value):
        if attr in ("target", "is_proxy"):
            self.__dict__[attr] = value
        else:
            setattr(self.target, attr, value)

    def __repr__(self):
        return "<B_PyEntity_Proxy for %s>" % (
            hasattr(self.target, "Name") and self.target.Name or "destroyed"
        )

    def SetSound(self, file_name):
        file_name = AutomatedAssets(file_name)
        return self.target.SetSound(file_name)

    def SetMaxCamera(self, cam_file_name, start, end):
        cam_file_name = AutomatedAssets(cam_file_name)
        return self.target.SetMaxCamera(cam_file_name, start, end)


######### Function Start
def AddBoundFunc(action_name, proc):
    IActions = BInput.GetInputManager().GetInputActions()
    action_name = BInput.GetInternalName(IActions.ID, action_name)
    Bladex_raw.AddBoundFunc(action_name, proc)  # type: ignore
    return 1


def AddInputAction(action_name, npi):
    val = BInput.GetInputManager().AddInputAction(action_name, npi, dict_only=1)
    if not val:
        return 0

    IActions = BInput.GetInputManager().GetInputActions()
    action_name = BInput.GetInternalName(IActions.ID, action_name)
    Bladex_raw.AddInputAction(action_name, npi)  # type: ignore
    return 1


def AddMusicEventADPCM(
    event_name,
    file,
    f_in,
    f_out,
    volume,
    priority,
    background,
    loop,
    unknown=0,
):
    file = AutomatedAssets(file)
    return Bladex_raw.AddMusicEventADPCM(
        event_name, file, f_in, f_out, volume, priority, background, loop, unknown
    )


def AddMusicEventMP3(
    event_name,
    file,
    f_in,
    f_out,
    volume,
    priority,
    background,
    loop,
    unknown=0,
):
    file = AutomatedAssets(file)
    return Bladex_raw.AddMusicEventMP3(
        event_name, file, f_in, f_out, volume, priority, background, loop, unknown
    )


def AddMusicEventWAV(
    event_name,
    file,
    f_in,
    f_out,
    volume,
    priority,
    background,
    loop,
    opened=0,
):
    file = AutomatedAssets(file)
    return Bladex_raw.AddMusicEventWAV(
        event_name, file, f_in, f_out, volume, priority, background, loop, opened
    )


def AddPostloadCB(map_path, fn):
    """AddPostloadCB("Barb_M1", fn)\n
    AddPostloadCB("Demo:M1", fn)\n
    Args:
        map_path (str)\n
        fn (function)
    """
    list_ = __data.postload_callbacks.get(map_path, [])
    list_.append(fn)
    __data.postload_callbacks[map_path] = list_


def AddPreloadCB(map_path, fn):
    """AddPreloadCB("Barb_M1", fn)\n
    AddPreloadCB("Demo:M1", fn)\n
    Args:
        map_path (str)\n
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
    Bladex_raw.AssocKey(action_name, device, key, on_press)  # type: ignore
    return 1


def AutomatedAssets(path, root_priority=""):
    """AutomatedAssets("../../3DObjs/3dObjs.mmp")\n"""
    if path == "":
        return path
    #
    ext = os.path.splitext(path)[1]
    check_ext = ""
    if string.lower(ext) in (".wav", ".mp3"):
        check_ext = ".ogg"
    #
    base_path = os.path.relpath(path, __data.mod_root)
    result = re.match(r"^(\.\.[/\\])*", base_path).group(0)
    result = string.replace(result, "\\", "/")  # type: ignore
    parent_path = os.path.normpath(os.path.join(__data.mod_root, result))
    for root in (root_priority,) + __data.asset_path:
        if not root:
            continue
        if (
            root == parent_path
            or os.path.commonprefix([root, parent_path]) != parent_path
        ):
            new_path = os.path.join(root, base_path)
            if os.path.exists(new_path):
                return new_path
            elif check_ext:
                new_path = os.path.splitext(new_path)[0] + check_ext
                if os.path.exists(new_path):
                    return new_path
    #
    return path


def BodInspector():
    import BBLib

    for root_dir in (__data.asset_path_model,) + __data.asset_path:
        if not root_dir:
            continue
        BodLink = os.path.join(root_dir, "BodLink.list")
        if os.path.isfile(BodLink):
            f = open(BodLink, "rt")
            f_path = f.readline()
            while f_path:
                # [:-1] is used to remove \n
                BBLib.ReadBOD(f_path[:-1])
                BBLib.LoadBOD(f.readline()[:-1])
                f_path = f.readline()
            f.close()
        else:
            BodLink = open(os.path.join(root_dir, "BodLink.list"), "wt+")
            AutoLoadAssets(os.path.join(root_dir, "3DChars"), BodLink)
            AutoLoadAssets(os.path.join(root_dir, "3DObjs"), BodLink)
            tell = BodLink.tell()
            BodLink.close()
            if tell == 0:
                os.remove(BodLink.name)


def AutoLoadAssets(root_dir, BodLink, depth=0):
    import BBLib

    if not os.path.isdir(root_dir):
        return

    dirs = []
    for f_name in os.listdir(root_dir):
        f_path = os.path.join(root_dir, f_name)
        if os.path.isdir(f_path):
            dirs.append(f_path)
            continue

        ext = os.path.splitext(f_name)[1]
        ext = string.lower(ext)
        if ext == ".bod":
            bodfile = open(f_path, "rb")
            size = struct.unpack("I", bodfile.read(4))[0]
            kind = struct.unpack("%ds" % size, bodfile.read(size))[0]
            bodfile.close()

            BBLib.ReadBOD(f_path)
            BBLib.LoadBOD(kind)
            if BodLink:
                BodLink.write(f_path + "\n")
                BodLink.write(kind + "\n")

    for i in dirs:
        AutoLoadAssets(i, BodLink, depth + 1)


def CallPostloadCB():
    pass


def CallPreloadCB():
    pass


def ConnectionService():
    """Connect to LumenService"""
    pass


def CreateEntity(name, kind, x, y, z, *args):
    # parent_class="", mesh_name=""
    ret = apply(
        Bladex_raw.CreateEntity,
        (name, kind, x, y, z) + args,
    )
    if kind == "Entity Sound":
        return B_PyEntity_Proxy(ret)
    return ret


def CreateSound(file_name, sound_name):
    file_name = AutomatedAssets(file_name)
    return Bladex_raw.CreateSound(file_name, sound_name)


def GetBladeRoot():
    """Returns the root path of Blade"""
    return __data.blade_root


def GetCurrentMap():
    return __data.current_map


def GetCurrentMod():
    return __data.current_mod


def GetEntity(arg):
    ret = Bladex_raw.GetEntity(arg)
    if ret and ret.Kind in ("Entity Sound", "Entity Camera"):
        return B_PyEntity_Proxy(ret)
    return ret


def GetLumenRoot():
    """Returns the root path of Lumen"""
    return __data.lumen_root


def GetMapListPath():
    return __data.map_list_path


def GetModRoot():
    """Returns the root path of the current mod"""
    return __data.mod_root


def GetPostloadCB(map_path):
    return __data.postload_callbacks.get(map_path, [])


def GetPreloadCB(map_path):
    return __data.preload_callbacks.get(map_path, [])


def GetTimeActionHeld(action_name):
    """Return the amount of milliseconds a key has been hald down, or zero if it is currently considered released"""
    action_name = BInput.GetInternalName(
        BInput.GetInputManager().GetInputActions().ID, action_name
    )
    return Bladex_raw.GetTimeActionHeld(action_name)  # type: ignore


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
    if map_dir == "":
        return

    lumen_root = __data.lumen_root
    map_list_path = "Maps"
    if mod_dir:
        mod_root = os.path.join(lumen_root, ModListPath, mod_dir)
    else:
        mod_root = lumen_root
    blade_root = os.path.normpath(lumen_root + "/..")

    map_path = os.path.join(mod_root, map_list_path, map_dir)
    cfg_file = os.path.join(map_path, "Cfg.py")
    if not os.path.isfile(cfg_file):
        printx("Cfg.py file not found!")
        return

    # sys_init = os.path.join(root_path, "Lib/sys_init.py")
    execstr = [
        "import Bladex",
        "import sys",
        "Bladex.BeginLoadGame()",
        #
        "isLumenLoadLevel = 1",
        # "current_map = '%s'" % map_dir,
        # "current_mod = '%s'" % mod_dir,
        # "map_list_path = '%s'" % map_list_path,
        # "mod_path = '%s'" % mod_root,
        # "root_path = '%s'" % lumen_absroot,
        # "sys.path.insert(0,'.')",
        # "sys.path.append('../../Bin')",
        # "sys.path.append('../../Scripts')",
    ]
    if mod_root != lumen_root:
        execstr = execstr + [
            "sys.path.append('%s/Lib')" % mod_root,
            "sys.path.append('%s/Lib/PythonLib')" % mod_root,
        ]

    execstr = execstr + [
        "sys.path.append('%s/Lib')" % lumen_root,
        "sys.path.append('%s/Lib/PythonLib')" % lumen_root,
        # "sys.path.append('%s/../Lib')" % lumen_root,
        "sys.path.append('%s/Lib/PythonLib')" % blade_root,
        "sys.path.append('%s/Lib/PythonLib/Plat-Win')" % blade_root,
        # "sys.path.append('../../Lib/PythonLib/Idle')",
        # "sys.path.append('../../Lib/PythonLib/lib-tk')",
        # "sys.path.append('../../Lib/PythonLib/DLLs')",
        # "sys.path.append('../../Lib/PythonLib/Pmw')",
        # "sys.path.append('../../Lib/PythonLib/Pmw/Pmw_0_8')",
        # "sys.path.append('../../Lib/PythonLib/Pmw/Pmw_0_8/lib')",
        "server_port = %d" % __data.server_port,
        "lumen_root = %s" % repr(lumen_root),
        "import Lumenx",
        # "Lumenx.SetCurrentMap(%s)" % repr(map_dir),
        # "Lumenx.SetCurrentMod(%s)" % repr(mod_dir),
        # "Lumenx.SetMapListPath(map_list_path)",
        # "Lumenx.SetModRoot(%s)" % repr(mod_root),
        # "Lumenx.SetLumenRoot(%s)" % repr(lumen_root),
        # "Lumenx.SetBladeRoot(%s)" % repr(blade_root),
        # "del map_dir, current_mod",
        #
        # "execfile('%s')" % sys_init,
        "execfile('%s')" % cfg_file,
        "Bladex.DoneLoadGame()",
    ]
    Bladex.BeginLoadGame()
    os.chdir(map_path)
    Bladex.CloseLevel(string.join(execstr, ";"), map_dir)  # type: ignore


def LoadSampledAnimation(file, anm_name, *args):
    # type=0, race_name="", interp=20):
    file = AutomatedAssets(file)
    return apply(Bladex_raw.LoadSampledAnimation, (file, anm_name) + args)


def LoadWorld(file_name):
    file_name = AutomatedAssets(file_name)
    return Bladex_raw.LoadWorld(file_name)


def Raisex(exc, msg=""):
    return "raise %s, %s" % (exc, repr(msg))


def ReadAlphaBitMap(file_name, internal_name):
    file_name = AutomatedAssets(file_name)
    return Bladex_raw.ReadAlphaBitMap(file_name, internal_name)


def ReadBitMap(file_name, internal_name):
    file_name = AutomatedAssets(file_name)
    return Bladex_raw.ReadBitMap(file_name, internal_name)


def ReadLevel(file_name):
    file_name = AutomatedAssets(file_name)
    if not os.path.isfile(file_name):
        return
    #
    new_lines = []
    f = open(file_name, "rt")
    lines = f.readlines()
    f.close()
    current_dir = os.getcwd()
    #
    for line in lines:
        line = string.strip(line)
        if not line:
            continue
        # ignore comments
        if line[0] != "#":
            lst = tuple(map(string.strip, string.split(line, " ->")))
            if len(lst) != 2:
                continue
            key, val = lst
            if key != "GammaC":
                val = os.path.relpath(AutomatedAssets(lst[1]), current_dir)
            new_lines.append("%s -> %s\n" % (key, val))
    #
    lvl_name = "7c3460c1-cc3c-5b9e-a038-1ff69ff753c9"  # uuid.uuid5(uuid.NAMESPACE_OID,"Lumen:ReadLevel")
    lvl_path = os.path.join(__data.lumen_root, lvl_name)
    f = open(lvl_path, "wt")
    f.writelines(new_lines)
    f.close()
    ret = Bladex_raw.ReadLevel(lvl_path)
    os.remove(lvl_path)
    return ret

    # import BBLib
    # #
    # funcs = {
    #     "Bitmaps": BBLib.ReadMMP,
    #     "BOD": BBLib.ReadBOD,
    #     "GammaC": None,
    #     "World": LoadWorld,
    #     "WorldDome": BBLib.ReadMMP,
    # }
    # #
    # f = open(file_name, "rt")
    # lines = f.readlines()
    # f.close()
    # for line in lines:
    #     line = string.strip(line)
    #     if not line:
    #         continue
    #     # ignore comments
    #     if line[0] != "#":
    #         lst = tuple(map(string.strip, string.split(line, " ->")))
    #         if len(lst) != 2:
    #             continue
    #         key, val = lst
    #         fn = funcs.get(key)
    #         if fn is not None:
    #             fn(val)


def RemoveBoundFunc(action_name, proc):
    IActions = BInput.GetInputManager().GetInputActions()
    action_name = BInput.GetInternalName(IActions.ID, action_name)
    Bladex_raw.RemoveBoundFunc(action_name, proc)  # type: ignore
    return 1


def RemoveInputAction(action_name):
    IActions = BInput.GetInputManager().GetInputActions()
    val = IActions.RemoveAction(action_name, dict_only=1)
    if not val:
        return 0

    action_name = BInput.GetInternalName(IActions.ID, action_name)
    Bladex_raw.RemoveInputAction(action_name)  # type: ignore
    return 1


def SetBladeRoot(path):
    __data.blade_root = path


def SetCurrentMap(map_dir):
    __data.current_map = map_dir


def SetCurrentMod(mod_dir):
    __data.current_mod = mod_dir


def SetGhostSectorGroupSound(
    group_name,
    file_name,
    volume=1.0,
    base_volume=1.0,
    min_dist=1000.0,
    max_dist=20000.0,
    scale=1.0,
):
    file_name = AutomatedAssets(file_name)
    return Bladex_raw.SetGhostSectorGroupSound(
        group_name, file_name, volume, base_volume, min_dist, max_dist, scale
    )


def SetGhostSectorSound(
    group_name,
    file_name,
    volume=1.0,
    base_volume=1.0,
    min_dist=1000.0,
    max_dist=20000.0,
    v_max_dist=10000.0,
    scale=1.0,
):
    file_name = AutomatedAssets(file_name)
    return Bladex_raw.SetGhostSectorSound(
        group_name,
        file_name,
        volume,
        base_volume,
        min_dist,
        max_dist,
        v_max_dist,
        scale,
    )


def SetLumenRoot(path):
    __data.lumen_root = path


def SetMapListPath(path):
    __data.map_list_path = path


def SetModRoot(path):
    __data.mod_root = path


######### Function End

# hook Bladex functions
for __fn in __bladex_decorators:  # type: ignore
    Bladex.__dict__[__fn] = globals()[__fn]  # type: ignore

FunctionDecorator = __FunctionDecorator()
for obj, name in ((sys.modules["__builtin__"], "execfile"),):
    FunctionDecorator.Decorator(obj, name)

# Clean up
del __fn, __bladex_decorators, obj, name

#########


"""
AddBoundFunc
AddInputAction
AddMusicEventADPCM
AddMusicEventMP3
AddMusicEventWAV
AddPostloadCB
AddPreloadCB
AssocKey
AutomatedAssets
BodInspector
CallPostloadCB
CallPreloadCB
ConnectionService
CreateEntity
CreateSound
GetBladeRoot
GetCurrentMap
GetCurrentMod
GetEntity
GetLumenRoot
GetMapListPath
GetModRoot
GetPostloadCB
GetPreloadCB
GetTimeActionHeld
LoadComponent
LoadLevel
LoadSampledAnimation
LoadWorld
printx
Raisex
ReadAlphaBitMap
ReadBitMap
ReadLevel
RemoveBoundFunc
RemoveInputAction
SetBladeRoot
SetCurrentMap
SetCurrentMod
SetGhostSectorGroupSound
SetGhostSectorSound
SetLumenRoot
SetMapListPath
SetModRoot
"""
