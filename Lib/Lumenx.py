# Author: Sryml
# Email: sryml@hotmail.com
# Python Version: 1.5.2
# License: MIT

import __main__
import sys

if not __main__.__dict__.get("isLumen"):
    sys.path.append(__file__[:-14] + "../Lib/PythonLib")
#
import os

ModListPath = "Mods"

CLASSIC_VER = 0
V109_VER = 1
MAJOR_VER = 2

MAX_FLOAT = 1.79769313486e308


# private database
class _DATA:
    control_character = "Player1"
    config = {}
    config_default = {
        "Language": "English",
        "BasicClone": "Default",
        "InventoryStyle": "Improved",
        "InventoryActivatedByFocus": "Weapon",
        "InventoryActivatedByNumbers": "Object",
        "GrillableLimb": "Enabled",
        "DodgeByMouseMovement": "Disabled",
        "ArcheryTrajectory": "Enabled",
        "AimingPerspective": "Nearest",
        "Kgt1HMastery": "Enabled",
        "Cache": "Disabled",
        "AssetAnimation": [],
        "AssetImage": [],
        "AssetModel": [],
        "AssetSound": [],
        "AssetOther": [],
        # debug
        "print_conflicting_sound": "Disabled",
    }
    map_list = {
        "": {
            "barb_m1": "Kashgar",
            "ragnar_m2": "Tabriz",
            "dwarf_m3": "Khazel Zalam",
            "ruins_m4": "Marakamda",
            "mine_m5": "Mines of Kelbegen",
            "labyrinth_m6": "Fortress of Tell Halaf",
            "tomb_m7": "Tombs of Ephyra",
            "island_m8": "Island of Karum",
            "orc_m9": "Shalatuwar Fortress",
            "orlok_m10": "The Gorge of Orlok",
            "ice_m11": "Fortress of Nemrut",
            "btomb_m12": "The Oasis of Nejeb",
            "desert_m13": "Temple of Al Farum",
            "volcano_m14": "Forge of Xshathra",
            "palace_m15": "The Temple of Ianna",
            "tower_m16": "Tower of Dal Gurak",
            "chaos_m17": "The Abyss",
            #
            "palace_back": "The Temple of Ianna (Back)",
            "mine_back": "Mines of Kelbegen (Back)",
            "labyrinth_back": "Fortress of Tell Halaf (Back)",
            "tomb_back": "Tombs of Ephyra (Back)",
            "ice_back": "Fortress of Nemrut (Back)",
            "btomb_back": "The Oasis of Nejeb (Back)",
            "desert_back": "Temple of Al Farum (Back)",
        }
    }
    #
    game_version = 1
    is_saved_game = 0
    save_dir = ""
    current_map = ""
    current_mod = ""
    current_mod_menu = ""
    # map_list_path = "Maps"
    postload_callbacks = {}
    preload_callbacks = {}
    mod_root = ""
    lumen_root = ""
    blade_root = ""
    asset_path = []  # Normalized path
    AssetAnimationPath = []
    AssetImagePath = []
    AssetModelPath = []
    AssetSoundPath = []
    AssetOtherPath = []
    #
    res_mmps = []
    res_bmps = {}
    res_alpha_bmps = {}
    #
    bod_inspector_loaded = 0
    opened_files_delta = 0  # 修正量
    nsave_num = 0
    listener_pos = (1, 0, 0, 0)
    BodLink = {}
    anm_event_funcs = {}
    sampled_animations = {}
    py_sounds = {}
    last_input_set = ""


######### Initialization #########


def __fn():
    # Use setattr to pass the editor's syntax check
    setattr(sys.modules["__builtin__"], "True", (1 == 1))
    setattr(sys.modules["__builtin__"], "False", (1 == 0))

    current_dir = os.getcwd()
    _DATA.lumen_root = lumen_root = os.path.relpath(__file__[:-14], current_dir)
    _DATA.blade_root = blade_root = os.path.normpath(lumen_root + "/..")
    _DATA.mod_root = mod_root = "..\\.."
    #
    f = open(lumen_root + "/Config/Lumen.cfg", "a+")
    try:
        _DATA.config = eval(f.read())
    except:
        pass
    f.close()
    for k in _DATA.config_default.keys():
        if not _DATA.config.has_key(k):
            _DATA.config[k] = _DATA.config_default[k]

    #
    root_paths = []
    if mod_root == lumen_root:
        _DATA.current_mod = ""
        _DATA.asset_path = [lumen_root, blade_root]
    else:
        _DATA.current_mod = os.path.basename(os.path.abspath(mod_root))
        root_paths.append(mod_root)
        _DATA.asset_path = [mod_root, lumen_root, blade_root]
    # _DATA.current_map = os.path.basename(current_dir)

    root_paths.append(lumen_root)
    root_paths.append(blade_root)

    #
    paths = [
        "Bin",
        "Stats",
        "Scripts",
        "Scripts/Combos",
        "Scripts/Combos/%s" % _DATA.config["Language"],
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

    for root in root_paths:
        if root != blade_root:
            sys.path.append(root)
        for p in paths:
            sys.path.append(os.path.join(root, p))
    #
    import Bladex, string

    Bladex.SetCallCheck(0)
    _DATA.current_mod = string.lower(_DATA.current_mod)

    # If it is not the first time to start from Lumen.exe
    if not __main__.__dict__.get("isLumen"):
        f_name = "2ea5b509-3c98-5063-95c2-cae184dc13fd"  # by uuid.uuid5(uuid.NAMESPACE_OID,"Lumen:Port")
        path = os.path.join(lumen_root, f_name)
        if os.path.exists(path):
            f = open(path, "r")
            ServicePort = f.readline()[:-1]
            f.close()
        else:
            ServicePort = "17018"
        Bladex.SetStringValue("Lumen:ServicePort", ServicePort)
    #
    if hasattr(Bladex, "SetBloom"):
        _DATA.game_version = MAJOR_VER
    elif hasattr(Bladex, "TriggerEvent"):
        _DATA.game_version = V109_VER
    else:
        _DATA.game_version = CLASSIC_VER

    _DATA.is_saved_game = __main__.__dict__.get("IsSavedGame", 0)
    _DATA.save_dir = __main__.__dict__.get("save_dir", "")
    #
    if _DATA.save_dir:
        del __main__.__dict__["save_dir"]


__fn()


# python3-like print function
def printx(*values, **kwargs):
    """sep=" ", end="\\n", file=None, flush=0"""
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
    if flush:
        file.flush()


# sys.modules["__builtin__"].printx = printx  # type: ignore

######### Initialization End #########


import string
import imp
import re
import typing
import struct
import copy
import pprint
import types

#
import Bladex
import BInput


#
if typing.TYPE_CHECKING:
    apply = lambda fn, args=(), kwds={}: None
    execfile = lambda filename, globals=None, locals=None: None
    cmp = lambda x, y: None


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
        self.NameList = []

    def Decorator(self, obj, name):
        RawFunc = self.RawFunc
        if hasattr(obj, name):
            setattr(RawFunc, name, getattr(obj, name))
        setattr(obj, name, getattr(self, name))
        self.NameList.append(name)

    # builtin module
    def execfile(self, filename, globals=None, locals=None):
        from LumenLib import BUtils

        filename = AutomatedAssets(filename)
        if globals is None or locals is None:
            ret = BUtils.get_tb_namespace()
            if globals is None:
                globals = ret[0]
            if locals is None:
                locals = ret[1]
        return self.RawFunc.execfile(filename, globals, locals)

    def type(self, obj):
        if getattr(obj, "__class__", None) == B_PyEntity_Proxy:
            obj = obj.target
        elif obj == self.type:
            obj = self.RawFunc.type
        # elif self.RawFunc.type(obj) in (types.FunctionType, types.MethodType):
        #     name = obj.__name__
        #     if name in self.NameList or name in globals()["__bladex_decorators"]:
        #         return types.BuiltinFunctionType

        return self.RawFunc.type(obj)

    def isinstance(self, obj, cls):
        if getattr(obj, "__class__", None) == B_PyEntity_Proxy:
            obj = obj.target

        return self.RawFunc.isinstance(obj, cls)

    def getattr(self, obj, name, default=Ellipsis):
        # 大概率存在则使用try
        try:
            return self.RawFunc.getattr(obj, name)
        except:
            if default is not Ellipsis:
                return default
            Raisex(AttributeError, "object has no attribute '%s'" % name)

    def enumerate(self, obj):
        return map(lambda x, y: (x, y), range(len(obj)), obj)

    def zip(self, *args):
        result = []
        iterables = map(lambda x: (len(x), x), args)  # type: list # type: ignore
        for idx in range(iterables[0][0]):
            sub = []
            abort = 0
            for length, obj in iterables:
                if idx >= length:
                    abort = 1
                    break
                sub.append(obj[idx])

            if abort:
                break
            result.append(tuple(sub))
        return result

    # BBLibc module
    def B_BitMap24_ReadFromBMP(self, this, arg0):
        arg0 = AutomatedAssets(arg0)
        return self.RawFunc.B_BitMap24_ReadFromBMP(this, arg0)

    def B_BitMap24_ReadFromJPEG(self, this, arg0):
        arg0 = AutomatedAssets(arg0)
        return self.RawFunc.B_BitMap24_ReadFromJPEG(this, arg0)

    def B_BitMap24_ReadFromFile(self, this, arg0):
        arg0 = AutomatedAssets(arg0)
        return self.RawFunc.B_BitMap24_ReadFromFile(this, arg0)

    def ReadBOD(self, path):
        path = AutomatedAssets(path)
        return self.RawFunc.ReadBOD(path)

    def ReadMMP(self, path, save=1):
        path = string.replace(path, "\\", "/")
        if save and path not in _DATA.res_mmps:
            _DATA.res_mmps.append(path)
        path = AutomatedAssets(path)
        return self.RawFunc.ReadMMP(path)

    def GetCurrentLanguage(self):
        return _DATA.config["Language"]

    def GetnOpenedInputFiles(self):
        return self.RawFunc.GetnOpenedInputFiles() + _DATA.opened_files_delta

    # BUIxc module
    def B_FontServer_CreateBFont(self, this, arg0, *args):
        arg0 = AutomatedAssets(arg0)
        return apply(self.RawFunc.B_FontServer_CreateBFont, (this, arg0) + args)

    def new_B_TextWidget(self, arg0, arg1, arg2, arg3, arg4, *args):
        arg4 = AutomatedAssets(arg4)
        return apply(
            self.RawFunc.new_B_TextWidget, (arg0, arg1, arg2, arg3, arg4) + args
        )

    def new_B_BitmapWidget(self, arg0, arg1, arg2, arg3, arg4, *args):
        args = tuple(map(AutomatedAssets, args))
        return apply(
            self.RawFunc.new_B_BitmapWidget, (arg0, arg1, arg2, arg3, arg4) + args
        )

    # Traps_C module
    def LoadMaxPath(self, cam_file_name, start, end):
        cam_file_name = AutomatedAssets(cam_file_name)
        return self.RawFunc.LoadMaxPath(cam_file_name, start, end)


def __empty_func(*args, **kwargs):
    return "empty_func"


# Backup Bladex functions to Bladex_raw
__bladex_decorators = [
    "ActivateInput",
    "AddBoundFunc",
    "AddInputAction",
    "AddMusicEventADPCM",
    "AddMusicEventMP3",
    "AddMusicEventWAV",
    "AssocKey",
    "BodInspector",
    "CreateEntity",
    "CreateSound",
    "DeactivateInput",
    "DeleteEntity",
    "GetCurrentMap",
    "GetEntity",
    "GetListenerPosition",
    "GetResolution",
    "GetTimeActionHeld",
    "LoadAnmRaceData",
    "LoadLevel",
    "LoadSampledAnimation",
    "LoadSoundDataBase",
    "LoadWorld",
    "ReadAlphaBitMap",
    "ReadBitMap",
    "ReadLevel",
    "RemoveBoundFunc",
    "RemoveInputAction",
    "SaveAnmRaceData",
    "SetCurrentMap",
    "SetGhostSectorGroupSound",
    "SetGhostSectorSound",
    "SetListenerPosition",
    "ShowCriticalWarning",
    "TriggerEvent",
]
for __fn in __bladex_decorators:  # type: ignore
    Bladex_raw.__dict__[__fn] = Bladex.__dict__.get(__fn, __empty_func)  # type: ignore


# -----------------------------
# 私有函数
# -----------------------------
def _SoundManager(file_name, sound_name, resolved_conflict=1):
    """0=not exist, 1=exist, 2=conflict"""
    status = 0
    if not file_name or (not sound_name):
        return (0, sound_name)

    new_snd = string.lower(os.path.normpath(file_name))
    if Bladex.GetSound(sound_name):
        exist_snd = _DATA.py_sounds.get(sound_name, "Unknown Sound")
        if new_snd == exist_snd:
            status = 1
        elif resolved_conflict:
            status = 2
            # 名称冲突的情况
            if GetConfig("print_conflicting_sound") == "Enabled":
                printx(
                    "Warning: conflict sound resolved (%s):\n%s <==> %s"
                    % (sound_name, repr(exist_snd), repr(new_snd))
                )
            idx = 1
            sound_name = _name = os.path.splitext(os.path.basename(new_snd))[0]
            while 1:
                if _DATA.py_sounds.get(sound_name) == new_snd:
                    status = 1
                    break
                if Bladex.GetSound(sound_name) or Bladex_raw.GetEntity(sound_name):
                    sound_name = "%s.%03d" % (_name, idx)
                    idx = idx + 1
                else:
                    break
            # printx("New Name:", sound_name)
        else:
            status = 1
            if GetConfig("print_conflicting_sound") == "Enabled":
                printx(
                    "Warning: conflict sound unresolved (%s):\n%s <==> %s"
                    % (sound_name, repr(exist_snd), repr(new_snd))
                )

    if status != 1:
        _DATA.py_sounds[sound_name] = new_snd

    return (status, sound_name)


######### Proxy
class B_PyEntity_Proxy:
    def __init__(self, target):
        self.target = target  # type: Bladex._entity.B_PyEntity | None
        # self.is_proxy = 1

    def __getattr__(self, attr):
        if not self.__dict__.get("target", 1):
            Raisex(AttributeError, "B_PyEntity_Proxy has no attribute '%s'" % attr)
        if attr == "__methods__":  # for dir()
            return dir(self.target)

        return getattr(self.target, attr)

    def __setattr__(self, attr, value):
        if not self.__dict__.get("target", 1):
            Raisex(AttributeError, "B_PyEntity_Proxy has no attribute '%s'" % attr)
        if attr == "target":
            self.__dict__[attr] = value
        # elif attr == "Animation":
        #     self.__dict__["Set%s" % attr](attr, value)
        else:
            setattr(self.target, attr, value)

    #
    def __getstate__(self):
        return getattr(self.target, "Name", None)

    def __setstate__(self, state):
        ent_name = state
        #
        if ent_name is None:
            self.target = None
        else:
            self.target = Bladex_raw.GetEntity(ent_name)

    # for bool test
    def __nonzero__(self):
        return hasattr(self.target, "Name")

    def __cmp__(self, other):
        if getattr(other, "__class__", None) == B_PyEntity_Proxy:
            other = other.target

        return cmp(self.target, other)

    def __repr__(self):
        return "<B_PyEntity_Proxy for %s>" % getattr(self.target, "Name", "destroyed")

    # -----------------------------
    def Abs2RelVector(self, *args):
        if len(args) == 1 and hasattr(args[0], "target"):
            args = (args[0].target,)
        return apply(self.target.Abs2RelVector, args)

    def CanISee(self, entity):
        entity = entity.target
        return self.target.CanISee(entity)

    def CanISeeFrom(self, entity, x, y, z):
        entity = entity.target
        return self.target.CanISeeFrom(entity, x, y, z)

    def Chase(self, enemy, action_area):
        enemy = enemy.target
        return self.target.Chase(enemy, action_area)

    def CheckAnimCol(self, anm_name, obj, unknown):
        obj = obj.target
        return self.target.CheckAnimCol(anm_name, obj, unknown)

    def ExcludeHitFor(self, entity):
        entity = entity.target
        return self.target.ExcludeHitFor(entity)

    def ExcludeHitInAnimationFor(self, entity):
        entity = entity.target
        return self.target.ExcludeHitInAnimationFor(entity)

    def Link(self, child):
        child = child.target
        return self.target.Link(child)

    def LinkAnchors(self, entity_anchor, child, child_anchor):
        child = child.target
        return self.target.LinkAnchors(entity_anchor, child, child_anchor)

    def LinkToNode(self, child, node):
        child = child.target
        return self.target.LinkToNode(child, node)

    def Rel2AbsVector(self, *args):
        if len(args) == 1 and hasattr(args[0], "target"):
            args = (args[0].target,)
        return apply(self.target.Rel2AbsVector, args)

    def SQDistance2(self, entity):
        entity = entity.target
        return self.target.SQDistance2(entity)

    def SetActiveEnemy(self, entity):
        entity = getattr(entity, "target", entity)
        return self.target.SetActiveEnemy(entity)

    def SetEnemy(self, enemy):
        enemy = enemy.target
        return self.target.SetEnemy(enemy)

    def Unlink(self, child):
        child = child.target
        return self.target.Unlink(child)

    # -----------------------------
    def SetSound(self, file_name):
        me = self.target
        resolved_conflict = 0
        status, sound_name = _SoundManager(file_name, me.Name, resolved_conflict)
        file_name = AutomatedAssets(file_name, multi_ext=1)
        if status == 2 and resolved_conflict:
            me.SetSound(file_name)
            o = Bladex.CreateEntity(sound_name, "Entity Sound", 0, 0, 0)
            o.Position = me.Position
            self.target = o
            # for attr in (
            #     "BaseVolume",
            #     "MaxDistance",
            #     "MinDistance",
            #     "Pitch",
            #     "SendNotify",
            #     "Volume",
            # ):
            #     setattr(o, attr, getattr(me, attr))
        return self.target.SetSound(file_name)

    def SetMaxCamera(self, cam_file_name, start, end):
        cam_file_name = AutomatedAssets(cam_file_name)
        return self.target.SetMaxCamera(cam_file_name, start, end)

    def AddAnmEventFunc(self, anm_event, func):
        if not self:
            return 0

        me = self.target
        name = me.Name
        if not _DATA.anm_event_funcs.has_key(name):
            _DATA.anm_event_funcs[name] = {}
        # Override event function
        _DATA.anm_event_funcs[name][anm_event] = func

        return me.AddAnmEventFunc(anm_event, func)

    def DelAnmEventFunc(self, anm_event):
        if not self:
            return 0

        me = self.target
        name = me.Name
        if not _DATA.anm_event_funcs.has_key(name):
            _DATA.anm_event_funcs[name] = {}
        if _DATA.anm_event_funcs[name].has_key(anm_event):
            del _DATA.anm_event_funcs[name][anm_event]

        return me.DelAnmEventFunc(anm_event)

    def SubscribeToList(self, name):
        if not self:
            return 0

        me = self.target

        def _on_destroy(this, ent_name):
            if _DATA.anm_event_funcs.has_key(ent_name):
                del _DATA.anm_event_funcs[ent_name]
            this.target = None

        if name == "Pin":
            Bladex.AddScheduledFunc(-1, _on_destroy, (self, me.Name), GetNSaveName())

        return me.SubscribeToList(name)

    def LaunchAnimation(self, anm_name):
        ret = self.target.LaunchAnimation(anm_name)
        if not ret and string.lower(anm_name) == "rlx":
            ret = self.target.LaunchAnimation("Rlx_no")
        if not ret:
            prefix = self.target.CharTypeExt[:3] + "_"
            full_anm_name = anm_name
            if full_anm_name[:4] != prefix:
                full_anm_name = prefix + full_anm_name
            else:
                anm_name = anm_name[4:]

            file_path = AutomatedAssets("../../Anm/%s.bmv" % anm_name)
            if not os.path.exists(file_path):
                file_path = AutomatedAssets("../../Anm/%s.bmv" % full_anm_name)

            Bladex.LoadSampledAnimation(file_path, full_anm_name, 0, self.target.Kind)
            ret = self.target.LaunchAnimation(full_anm_name)
        return ret

    def LaunchAnmType(self, anm_type, *args):
        ret = apply(self.target.LaunchAnmType, (anm_type,) + args)
        if not ret and string.lower(anm_type) == "rlx":
            ret = apply(self.target.LaunchAnmType, ("Rlx_no",) + args)
        if not ret:
            prefix = self.target.CharTypeExt[:3] + "_"
            full_anm_name = anm_type
            if full_anm_name[:4] != prefix:
                full_anm_name = prefix + full_anm_name
            else:
                anm_type = anm_type[4:]

            file_path = AutomatedAssets("../../Anm/%s.bmv" % anm_type)
            if not os.path.exists(file_path):
                file_path = AutomatedAssets("../../Anm/%s.bmv" % full_anm_name)

            Bladex.LoadSampledAnimation(file_path, full_anm_name, 0, self.target.Kind)
            ret = apply(self.target.LaunchAnmType, (full_anm_name,) + args)
        return ret

    # -----------------------------
    # def SetAnimation(self, attr, value):
    #     if not _DATA.sampled_animations.has_key(value):
    #         Bladex.LoadSampledAnimation(
    #             "../../Anm/%s" % value, value, 0, self.target.Kind
    #         )
    #     setattr(self.target, attr, value)

    # -----------------------------
    # Added
    # -----------------------------
    def Rel2AbsPoint4Anchor(self, x, y, z, anchor):
        from LumenLib import mathutils

        me = self.target
        vx = me.GetDummyAxis(anchor, 1, 0, 0)
        vy = me.GetDummyAxis(anchor, 0, 1, 0)
        vz = me.GetDummyAxis(anchor, 0, 0, 1)
        matrix = mathutils.Matrix((vx, vy, vz)).transposed().to_4x4()
        matrix.SetTranslation(me.GraspPos(anchor))
        location = matrix * mathutils.Vector((x, y, z))

        return location.to_tuple()

    def Rel2AbsVector4Anchor(self, x, y, z, anchor):
        me = self.target
        vector = me.GetDummyAxis(anchor, x, y, z)

        return vector

    def Abs2RelPoint4Anchor(self, x, y, z, anchor):
        from LumenLib import mathutils

        me = self.target
        vx = me.GetDummyAxis(anchor, 1, 0, 0)
        vy = me.GetDummyAxis(anchor, 0, 1, 0)
        vz = me.GetDummyAxis(anchor, 0, 0, 1)
        q = mathutils.Matrix((vx, vy, vz)).transposed().to_quaternion().inverted()
        vector = mathutils.Vector((x, y, z)) - mathutils.Vector(me.GraspPos(anchor))
        vector = q * vector

        return vector.to_tuple()

    def Abs2RelVector4Anchor(self, x, y, z, anchor):
        from LumenLib import mathutils

        me = self.target
        vx = me.GetDummyAxis(anchor, 1, 0, 0)
        vy = me.GetDummyAxis(anchor, 0, 1, 0)
        vz = me.GetDummyAxis(anchor, 0, 0, 1)
        q = mathutils.Matrix((vx, vy, vz)).transposed().to_quaternion().inverted()
        vector = q * mathutils.Vector((x, y, z))

        return vector.to_tuple()


######### Function Start
def ActivateInput():
    InputManager = BInput.InputManager
    IAS = InputManager.GetInputActionsSet()
    if IAS != "EmptySet":
        return 0
    InputManager.SetInputActionsSet(_DATA.last_input_set)
    return 1
    # Bladex_raw.ActivateInput()


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


def AddMapList(map_list, mod_dir):
    mod_dir = string.lower(mod_dir)
    new_map_list = {}
    for k, v in map_list.items():
        new_map_list[string.lower(k)] = v
    if not _DATA.map_list.has_key(mod_dir):
        _DATA.map_list[mod_dir] = {}
    _DATA.map_list[mod_dir].update(new_map_list)


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
    base, ext = os.path.splitext(file)
    ext_raw = ""
    if string.lower(ext) == ".mp3":
        ext_raw = ext
        file = "%s.ogg" % base
    file = AutomatedAssets(file)
    if ext_raw:
        file = "%s%s" % (os.path.splitext(file)[0], ext_raw)
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
    base, ext = os.path.splitext(file)
    ext_raw = ""
    if string.lower(ext) == ".mp3":
        ext_raw = ext
        file = "%s.ogg" % base
    file = AutomatedAssets(file)
    if ext_raw:
        file = "%s%s" % (os.path.splitext(file)[0], ext_raw)
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
    base, ext = os.path.splitext(file)
    ext_raw = ""
    if string.lower(ext) == ".mp3":
        ext_raw = ext
        file = "%s.ogg" % base
    file = AutomatedAssets(file)
    if ext_raw:
        file = "%s%s" % (os.path.splitext(file)[0], ext_raw)
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
    list_ = _DATA.postload_callbacks.get(map_path, [])
    list_.append(fn)
    _DATA.postload_callbacks[map_path] = list_


def AddPreloadCB(map_path, fn):
    """AddPreloadCB("Barb_M1", fn)\n
    AddPreloadCB("Demo:M1", fn)\n
    Args:
        map_path (str)\n
        fn (function)
    """
    list_ = _DATA.preload_callbacks.get(map_path, [])
    list_.append(fn)
    _DATA.preload_callbacks[map_path] = list_


def AssocControl():
    from LumenLib import BODLoader

    DefControl = 1
    ControlFile = os.path.join(GetLumenRoot(), "Config/Control.py")
    mod_info = BODLoader.GetModInfo(GetCurrentMod())
    if mod_info.get("PrivateControl") == 1:
        if os.path.isfile("../../Config/Control.py"):
            DefControl = 0
            ControlFile = "../../Config/Control.py"
    elif os.path.isfile(ControlFile):
        DefControl = 0

    if DefControl:
        execfile("../../Scripts/DefControl.py")
        printx("BladeInit -> Executed DefControl.py")
    else:
        execfile(ControlFile)
        printx("BladeInit -> Executed Control.py")


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


def AutomatedAssets(path, root_priority=[], multi_ext=0):
    """AutomatedAssets("../../3DObjs/3dObjs.mmp")\n"""
    if path == "":
        return path
    #
    base_path = os.path.relpath(path, _DATA.mod_root)
    if base_path is None:
        return path
    #
    result = re.match(r"^(\.\.[/\\])*", base_path).group(0)
    # result = string.replace(result, "\\", "/")  # type: ignore
    base_root = os.path.normpath(os.path.join(_DATA.mod_root, result))
    base_root_len = len(base_root)
    if result:
        for root in _DATA.asset_path:
            num = len(root)
            if num >= base_root_len:
                base_root = root
                base_root_len = num
                break
        base_path = os.path.relpath(path, base_root)
    #
    base, ext = os.path.splitext(base_path)
    ext = string.lower(ext)
    check_ext = [ext]
    #
    if ext == ".bmv":
        root_priority = root_priority + _DATA.AssetAnimationPath
    elif ext in (".bmp", ".jpg", ".jpeg", ".png", ".mmp"):
        root_priority = root_priority + _DATA.AssetImagePath
    elif ext == ".bod":
        root_priority = root_priority + _DATA.AssetModelPath
    elif ext in (".wav", ".mp3", ".ogg"):
        root_priority = root_priority + _DATA.AssetSoundPath
        if multi_ext:
            check_ext = [".ogg", ".wav", ".mp3"]  # 优先检查ogg版本
            # idx = check_ext.index(ext)
            # check_ext[0], check_ext[idx] = check_ext[idx], check_ext[0]
    else:
        root_priority = root_priority + _DATA.AssetOtherPath
    #
    new_path = path
    exists = 0
    for root in root_priority:
        if not root:
            continue
        # if root == base_root or os.path.commonprefix([root, base_root]) != root:
        for e in check_ext:
            _path = os.path.join(root, "%s%s" % (base, e))
            if os.path.exists(_path):
                new_path = _path
                exists = 1
                break
        if exists:
            break
    #
    if not exists and (not os.path.exists(new_path)):
        for root in _DATA.asset_path:
            if len(root) < base_root_len:
                continue
            #
            for e in check_ext:
                new_path = os.path.join(root, "%s%s" % (base, e))
                if os.path.exists(new_path):
                    exists = 1
                    break
            if exists:
                break

    #
    return new_path


def BodInspector():
    import BBLib
    import LoadBar

    if _DATA.bod_inspector_loaded:
        return

    _DATA.opened_files_delta = BBLib.GetnOpenedInputFiles()
    LoadBar.opened_files_delta = _DATA.opened_files_delta
    if LoadBar.ProgressBarInst and LoadBar.ProgressBarInst.filehook:
        BBLib.RemoveOnOpenInputFileFunc()
    for root_dir in _DATA.asset_path:
        if not root_dir:
            continue
        AutoLoadAssets(os.path.join(root_dir, "3DChars"))
        AutoLoadAssets(os.path.join(root_dir, "3DObjs"))
        # BodLink = os.path.join(root_dir, "BodLink.list")
        # if os.path.isfile(BodLink):
        #     f = open(BodLink, "rt")
        #     line = f.readline()
        #     while line:
        #         f_path = string.strip(line)
        #         if f_path:
        #             BBLib.ReadBOD(f_path)
        #             f.readline()
        #             # BBLib.LoadBOD(string.strip(f.readline()))
        #         line = f.readline()
        #     f.close()
        # else:
        #     BodLink = open(os.path.join(root_dir, "BodLink.list"), "wt+")
        #     AutoLoadAssets(os.path.join(root_dir, "3DChars"), BodLink)
        #     AutoLoadAssets(os.path.join(root_dir, "3DObjs"), BodLink)
        #     tell = BodLink.tell()
        #     BodLink.close()
        #     if tell == 0:
        #         os.remove(BodLink.name)
    #
    _DATA.bod_inspector_loaded = 1
    BBLib.ResetnOpenedInputFiles()
    if LoadBar.ProgressBarInst and LoadBar.ProgressBarInst.filehook:
        BBLib.SetOnOpenInputFileFunc(LoadBar.ProgressBarInst.BarIncrement)


def AutoLoadAssets(root_dir, BodLink=None):
    import BBLib

    if not os.path.isdir(root_dir):
        return

    dirs = []
    for f_name in os.listdir(root_dir):
        f_path = os.path.join(root_dir, f_name)
        if os.path.isdir(f_path):
            dirs.append(f_path)
            continue

        name, ext = os.path.splitext(string.lower(f_name))
        if ext == ".bod" and (not _DATA.BodLink.has_key(name)):
            _DATA.BodLink[name] = 1
            f_path = string.replace(f_path, "\\", "/")
            BBLib.ReadBOD(f_path)

            if BodLink is not None:
                bodfile = open(f_path, "rb")
                size = struct.unpack("I", bodfile.read(4))[0]
                kind = struct.unpack("%ds" % size, bodfile.read(size))[0]
                bodfile.close()

                # BBLib.LoadBOD(kind)
                BodLink.write(f_path + "\n")
                BodLink.write(kind + "\n")

    for i in dirs:
        AutoLoadAssets(i, BodLink)


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
    # if kind == "Entity Sound":
    #     return B_PyEntity_Proxy(ret)
    # return ret
    return B_PyEntity_Proxy(ret)


def CreateSound(file_name, sound_name):
    status, sound_name = _SoundManager(file_name, sound_name)
    if status == 1:
        return Bladex.GetSound(sound_name)
    #
    file_name = AutomatedAssets(file_name, multi_ext=1)
    return Bladex_raw.CreateSound(file_name, sound_name)


def DeactivateInput():
    InputManager = BInput.InputManager
    IAS = InputManager.GetInputActionsSet()
    if IAS == "EmptySet":
        return 0
    _DATA.last_input_set = IAS
    Bladex_raw.DeactivateInput()
    Bladex_raw.ActivateInput()
    InputManager.SetInputActionsSet("EmptySet")
    return 1


def DeleteEntity(arg):
    if getattr(arg, "__class__", None) == B_PyEntity_Proxy:
        me = arg.target
        arg.target = None
    else:
        me = Bladex_raw.GetEntity(arg)
    #
    if me is not None:
        if _DATA.anm_event_funcs.has_key(me.Name):
            del _DATA.anm_event_funcs[me.Name]

        return Bladex_raw.DeleteEntity(me)
    return 0


def GetAlphaBMPFiles():
    return _DATA.res_alpha_bmps


def GetBladeRoot():
    """Returns the root path of Blade"""
    return _DATA.blade_root


def GetBMPFiles():
    return _DATA.res_bmps


def GetConfig(key=None):
    if key is None:
        return _DATA.config
    return _DATA.config.get(key)


def GetControlCharacter():
    return Bladex.GetEntity(_DATA.control_character)


def GetCurrentMap():
    return _DATA.current_map


def GetCurrentMod():
    return _DATA.current_mod


def GetCurrentModMenu():
    return _DATA.current_mod_menu


def GetDefaultConfig(key=None):
    if key is None:
        return _DATA.config_default
    return _DATA.config_default.get(key)


def GetEntity(arg):
    if arg is None:
        return None
    ret = Bladex_raw.GetEntity(arg)
    if ret is None:
        return None
    return B_PyEntity_Proxy(ret)


def GetGameVersion():
    return _DATA.game_version


def GetInventoryStyle():
    return _DATA.config["InventoryStyle"]


def GetListenerPosition():
    return _DATA.listener_pos


def GetLumenRoot():
    """Returns the root path of Lumen"""
    return _DATA.lumen_root


def GetMapList(mod_dir=""):
    mod_dir = string.lower(mod_dir)
    return _DATA.map_list.get(mod_dir, {})


def GetMapListItem(map_dir, mod_dir):
    mod_dir = string.lower(mod_dir)
    map_dir = string.lower(map_dir)
    return _DATA.map_list.get(mod_dir, {}).get(map_dir, "")


def GetMapListPath():
    return _DATA.map_list_path


def GetMMPFiles():
    return _DATA.res_mmps


def GetModRoot():
    """Returns the root path of the current mod"""
    return _DATA.mod_root


def GetNSaveName():
    _DATA.nsave_num = _DATA.nsave_num + 1
    return "[NSAVE]%d" % _DATA.nsave_num


def GetPostloadCB(map_path):
    return _DATA.postload_callbacks.get(map_path, [])


def GetPreloadCB(map_path):
    return _DATA.preload_callbacks.get(map_path, [])


def GetResolution():
    import Raster

    if _DATA.game_version == CLASSIC_VER:
        return Raster.GetWindowSize()
    return Bladex_raw.GetResolution()


def GetServicePort():
    ret = Bladex.GetStringValue("Lumen:ServicePort")
    return int(ret)


def GetTimeActionHeld(action_name):
    """Return the amount of milliseconds a key has been hald down, or zero if it is currently considered released"""
    action_name = BInput.GetInternalName(
        BInput.GetInputManager().GetInputActions().ID, action_name
    )
    return Bladex_raw.GetTimeActionHeld(action_name)  # type: ignore


def InventoryActivatedByFocus():
    return _DATA.config["InventoryActivatedByFocus"]


def InventoryActivatedByNumbers():
    return _DATA.config["InventoryActivatedByNumbers"]


def IsCacheEnabled():
    return _DATA.config["Cache"] == "Enabled"


def IsSavedGame():
    return _DATA.is_saved_game


def LinkAbs(parent, child):
    # type: (Bladex._entity.B_PyEntity, Bladex._entity.B_PyEntity) -> ...
    """Absolute link two entities"""
    pos = child.Position
    child.Position = parent.Abs2RelPoint(pos[0], pos[1], pos[2])
    parent.Link(child)


def LoadAnmRaceData(file_name):
    if IsCacheEnabled():
        return Bladex_raw.LoadAnmRaceData(file_name)
    return 0


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
    import MemPersistence

    if map_dir == "":
        return

    map_list_path = "Maps"
    lumen_root = _DATA.lumen_root

    mod_dir = string.lower(mod_dir)
    if mod_dir:
        # for filename in os.listdir(os.path.join(lumen_root, ModListPath)):
        #     if string.lower(filename) == mod_dir:
        #         mod_dir = filename
        #         break
        mod_root = os.path.join(lumen_root, ModListPath, mod_dir)
        new_lumen_root = "..\\..\\..\\.."
    else:
        mod_root = lumen_root
        new_lumen_root = "..\\.."

    map_dir = string.lower(map_dir)
    map_path = ""
    for filename in os.listdir(os.path.join(mod_root, map_list_path)):
        if string.lower(filename) == map_dir:
            map_path = os.path.join(mod_root, map_list_path, filename)
            break

    if not (map_path and os.path.isdir(map_path)):
        printx("Map directory not found!")
        return
    cfg_file = os.path.join(map_path, "Cfg.py")
    if not os.path.isfile(cfg_file):
        printx("Cfg.py file not found!")
        return
    #
    if map_dir == "casa":
        MemPersistence.Delete("2DMapValues")
        MemPersistence.Delete("MainChar")
    new_mod_root = "..\\.."
    new_blade_root = new_lumen_root + "\\.."

    # sys_init = os.path.join(root_path, "Lib/sys_init.py")
    execstr = [
        "import Bladex",
        "import sys",
        "import time",
        "Bladex.SetTime(0.0)",
        "Bladex.SetSaveInfo((1, (0,)))",  # 用于Bladex.GenerateEntityName的计数
        "b3028472_681f_5be2_8aeb_c7011b166583=time.time()",
        "Bladex.SetAppMode('Game')",
        "Bladex.KillMusic()",
        "Bladex.ShutDownSoundChannels()",
        "Bladex.PauseSoundSystem()",
        "Bladex.BeginLoadGame()",
        #
        "isLumen = 1",
        # "current_map = '%s'" % map_dir,
        # "current_mod = '%s'" % mod_dir,
        # "map_list_path = '%s'" % map_list_path,
        # "mod_path = '%s'" % mod_root,
        # "root_path = '%s'" % lumen_absroot,
        # "sys.path.insert(0,'.')",
        # "sys.path.append('../../Bin')",
        # "sys.path.append('../../Scripts')",
    ]
    if new_mod_root != new_lumen_root:
        execstr = execstr + [
            "sys.path.append('%s/Lib')" % new_mod_root,
            "sys.path.append('%s/Lib/PythonLib')" % new_mod_root,
        ]

    execstr = execstr + [
        "sys.path.append('%s/Lib')" % new_lumen_root,
        "sys.path.append('%s/Lib/PythonLib')" % new_lumen_root,
        # "sys.path.append('%s/../Lib')" % new_lumen_root,
        "sys.path.append('%s/Lib/PythonLib')" % new_blade_root,
        "sys.path.append('%s/Lib/PythonLib/Plat-Win')" % new_blade_root,
        # "sys.path.append('../../Lib/PythonLib/Idle')",
        # "sys.path.append('../../Lib/PythonLib/lib-tk')",
        # "sys.path.append('../../Lib/PythonLib/DLLs')",
        # "sys.path.append('../../Lib/PythonLib/Pmw')",
        # "sys.path.append('../../Lib/PythonLib/Pmw/Pmw_0_8')",
        # "sys.path.append('../../Lib/PythonLib/Pmw/Pmw_0_8/lib')",
        # "lumen_root = %s" % repr(new_blade_root),
        "import Lumenx",
        # "Lumenx.SetCurrentMap(%s)" % repr(map_dir),
        # "Lumenx.SetCurrentMod(%s)" % repr(mod_dir),
        # "Lumenx.SetMapListPath(map_list_path)",
        # "Lumenx.SetModRoot(%s)" % repr(mod_root),
        # "Lumenx.SetLumenRoot(%s)" % repr(lumen_root),
        # "Lumenx.SetBladeRoot(%s)" % repr(blade_root),
        #
        # "execfile('%s')" % sys_init,
        "Lumenx.SetListenerPosition(1)",
        "execfile('Cfg.py')",
        "isMenuAppMode =  Bladex.GetAppMode() == 'Menu'",
        "Bladex.ResumeSoundSystem()",
        "Bladex.DoneLoadGame()",
        "isMenuAppMode and Bladex.SetAppMode('Menu')",
        "b3028472_681f_5be2_8aeb_c7011b166583 = round(time.time() - b3028472_681f_5be2_8aeb_c7011b166583, 3)",
        "Lumenx.printx('Load Time = %s' % b3028472_681f_5be2_8aeb_c7011b166583, flush=1)",
        # "import Actions;Actions.ReportMsg('Load Time = %s' % b3028472_681f_5be2_8aeb_c7011b166583)",
        "del b3028472_681f_5be2_8aeb_c7011b166583",
        "del isMenuAppMode",
        "Bladex.SetTime(0.0)",
    ]
    #
    import SplashImage
    import Language

    scr_name = "../../Data/Locale/" + Language.Current + "/Image/Cerrando_hi.jpg"
    SplashImage.ShowImage(scr_name, 0)
    #
    Bladex.BeginLoadGame()
    os.chdir(map_path)
    Bladex.CloseLevel(
        string.join(execstr, ";"), ""
    )  # map_name is empty, make sure to load a brand new one.


def LoadSampledAnimation(file, anm_name, *args):
    # type=0, race_name="", interp=20):
    file = AutomatedAssets(file)
    ret = apply(Bladex_raw.LoadSampledAnimation, (file, anm_name) + args)
    if ret == 1:
        _DATA.sampled_animations[anm_name] = args and args[0] or 0
    return ret


def LoadSoundDataBase(file_name):
    ret = Bladex_raw.LoadSoundDataBase(file_name)
    # for n in range(Bladex.nSounds()):
    #     sound_name = Bladex.GetSoundName(n)
    #     file_name = Bladex.GetSoundFileName(n)
    return ret


def LoadWorld(file_name):
    file_name = AutomatedAssets(file_name)
    return Bladex_raw.LoadWorld(file_name)


def Raisex(exc, msg=""):
    exec("raise %s, %s" % (exc, repr(msg)))


def ReadAlphaBitMap(file_name, internal_name, save=1):
    if save and _DATA.res_alpha_bmps.get(internal_name) is None:
        _DATA.res_alpha_bmps[internal_name] = file_name
    file_name = AutomatedAssets(file_name)
    return Bladex_raw.ReadAlphaBitMap(file_name, internal_name)


def ReadBitMap(file_name, internal_name, save=1):
    if save and _DATA.res_bmps.get(internal_name) is None:
        _DATA.res_bmps[internal_name] = file_name
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
            val = re.split(r"\s+", val)[0]
            val = string.replace(val, "\\\\", "/")
            val = string.replace(val, "\\", "/")
            if key != "GammaC":
                if key in ("Bitmaps", "WorldDome"):
                    if val not in _DATA.res_mmps:
                        _DATA.res_mmps.append(val)
                #
                val = os.path.relpath(AutomatedAssets(val), current_dir)
            new_lines.append("%s -> %s\n" % (key, val))
    #
    lvl_name = "7c3460c1-cc3c-5b9e-a038-1ff69ff753c9"  # uuid.uuid5(uuid.NAMESPACE_OID,"Lumen:ReadLevel")
    lvl_path = os.path.join(_DATA.lumen_root, lvl_name)
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


def SaveAnmRaceData(file_name, race):
    if IsCacheEnabled():
        return Bladex_raw.SaveAnmRaceData(file_name, race)


def SaveConfig(config):
    _DATA.config = copy.deepcopy(config)
    pp = pprint.PrettyPrinter(indent=4)
    f = open(_DATA.lumen_root + "/Config/Lumen.cfg", "wt")
    f.write(pp.pformat(config))
    f.close()
    printx("Lumen: Config saved.")


def SetAfterFrameFunc2(name, callback, t_frame):
    AfterFrameFunc2(name, callback, t_frame)


def SetBladeRoot(path):
    _DATA.blade_root = path


def SetControlCharacter(ent):
    if type(ent) == type(Bladex.GetEntity("Camera")):
        _DATA.control_character = ent.Name


def SetCurrentMap(map_dir):
    _DATA.current_map = map_dir
    return Bladex_raw.SetCurrentMap(map_dir)


def SetCurrentMod(mod_dir):
    _DATA.current_mod = mod_dir


def SetCurrentModMenu(mod_dir):
    _DATA.current_mod_menu = mod_dir


def SetData(name, value):
    _DATA.__dict__[name] = value


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


def SetListenerPosition(mode, x=0, y=0, z=0):
    _DATA.listener_pos = (mode, x, y, z)
    return Bladex_raw.SetListenerPosition(mode, x, y, z)


def SetLumenRoot(path):
    _DATA.lumen_root = path


def SetMapListPath(path):
    _DATA.map_list_path = path


def SetModRoot(path):
    _DATA.mod_root = path


def ShowCriticalWarning(*args):
    """Compatible with classic version"""
    return apply(Bladex_raw.ShowCriticalWarning, args)


def TriggerEvent(achv_idx):
    import Reference

    Reference.debugprint("Activated Achievement: %s" % achv_idx)
    return Bladex_raw.TriggerEvent(achv_idx)


######### Function End


# -----------------------------
# Class Start
# -----------------------------


class AfterFrameFunc2:
    def __init__(self, name, callback, t_frame):
        self.current_frame = 0
        self.name = name
        self.callback = callback
        self.t_frame = t_frame

        Bladex.SetAfterFrameFunc(self.name, self.AfterFrameFunc)

    def AfterFrameFunc(self, time):
        if self.current_frame >= self.t_frame:
            Bladex.RemoveAfterFrameFunc(self.name)
            self.callback()
        else:
            self.current_frame = self.current_frame + 1


# class CameraData:
#     def __init__(self, me):
#         # type: (Bladex._entity.B_Entity_Camera) -> None
#         me.PViewType = 0

#     def __getstate__(self):
#         me = Bladex.GetEntity("Camera")
#         return (me.PViewType, me.Position, me.TPos)

#     def __setstate__(self, parms):
#         Bladex.AddScheduledFunc(
#             Bladex.GetTime(), self.Restore, (parms,), "CameraData.Restore[NSAVE]"
#         )

#     def Restore(self, parms):
#         me = Bladex.GetEntity("Camera")
#         me.PViewType = parms[0]
#         me.SType = 0
#         me.TType = 0
#         me.Position = parms[1]
#         me.TPos = parms[2]
#         me.SetPersonView(GetControlCharacter().Name)


# -----------------------------
# Class End
# -----------------------------

# hook Bladex functions
for __fn in __bladex_decorators:  # type: ignore
    Bladex.__dict__[__fn] = globals()[__fn]  # type: ignore

# hook other functions
import BBLibc, BUIxc, Traps_C

FunctionDecorator = __FunctionDecorator()
for obj, name in (
    (sys.modules["__builtin__"], "execfile"),
    (sys.modules["__builtin__"], "type"),
    (sys.modules["__builtin__"], "isinstance"),
    (sys.modules["__builtin__"], "getattr"),
    (sys.modules["__builtin__"], "enumerate"),
    (sys.modules["__builtin__"], "zip"),
    (BBLibc, "B_BitMap24_ReadFromBMP"),
    (BBLibc, "B_BitMap24_ReadFromJPEG"),
    (BBLibc, "B_BitMap24_ReadFromFile"),
    (BBLibc, "ReadBOD"),
    (BBLibc, "ReadMMP"),
    (BBLibc, "GetCurrentLanguage"),
    (BBLibc, "GetnOpenedInputFiles"),
    (BUIxc, "B_FontServer_CreateBFont"),
    (BUIxc, "new_B_TextWidget"),
    (BUIxc, "new_B_BitmapWidget"),
    (Traps_C, "LoadMaxPath"),
):
    FunctionDecorator.Decorator(obj, name)

#
SetCurrentMap(os.path.basename(os.getcwd()))

# Clean up
del __fn, obj, name

# ----------------------------------
import GameState
import GameStateAux

if IsSavedGame():
    GameStateAux.InitConstantDatabase(_DATA.save_dir)


def SaveData():
    return (_DATA.anm_event_funcs,)


def LoadData(data):
    _DATA.anm_event_funcs = data[0]
    for ent_name, event_funcs in _DATA.anm_event_funcs.items():
        ent = Bladex_raw.GetEntity(ent_name)
        if ent:
            for anm_event, func in event_funcs.items():
                ent.AddAnmEventFunc(anm_event, func)
        else:
            del _DATA.anm_event_funcs[ent_name]


def SaveConstData():
    return _DATA.py_sounds


def LoadConstData(data):
    _DATA.py_sounds = data


GameState.ModulesToBeSaved.append(sys.modules[__name__])
GameStateAux.LoadConstData(__name__)

#  _    _   _ __  __ _____ _   _
# | |  | | | |  \/  | ____| \ | |
# | |  | | | | |\/| |  _| |  \| |
# | |__| |_| | |  | | |___| |\  |
# |_____\___/|_|  |_|_____|_| \_|
#

"""
ActivateInput
AddBoundFunc
AddInputAction
AddMapList
AddMusicEventADPCM
AddMusicEventMP3
AddMusicEventWAV
AddPostloadCB
AddPreloadCB
AssocControl
AssocKey
AutomatedAssets
BodInspector
CallPostloadCB
CallPreloadCB
ConnectionService
CreateEntity
CreateSound
DeactivateInput
DeleteEntity
GetAlphaBMPFiles
GetBladeRoot
GetBMPFiles
GetConfig
GetControlCharacter
GetCurrentMap
GetCurrentMod
GetCurrentModMenu
GetDefaultConfig
GetEntity
GetGameVersion
GetInventoryStyle
GetListenerPosition
GetLumenRoot
GetMapList
GetMapListItem
GetMapListPath
GetMMPFiles
GetModRoot
GetNSaveName
GetPostloadCB
GetPreloadCB
GetResolution
GetServicePort
GetTimeActionHeld
InventoryActivatedByFocus
InventoryActivatedByNumbers
IsCacheEnabled
IsSavedGame
LinkAbs
LoadAnmRaceData
LoadComponent
LoadLevel
LoadSampledAnimation
LoadSoundDataBase
LoadWorld
printx
Raisex
ReadAlphaBitMap
ReadBitMap
ReadLevel
RemoveBoundFunc
RemoveInputAction
SaveAnmRaceData
SaveConfig
SetAfterFrameFunc2
SetBladeRoot
SetControlCharacter
SetCurrentMap
SetCurrentMod
SetCurrentModMenu
SetData
SetGhostSectorGroupSound
SetGhostSectorSound
SetListenerPosition
SetLumenRoot
SetMapListPath
SetModRoot
ShowCriticalWarning
TriggerEvent
"""
