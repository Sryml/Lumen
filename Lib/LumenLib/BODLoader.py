#  _    _   _ __  __ _____ _   _
# | |  | | | |  \/  | ____| \ | |
# | |  | | | | |\/| |  _| |  \| |
# | |__| |_| | |  | | |___| |\  |
# |_____\___/|_|  |_|_____|_| \_|
#

import Bladex
import Lumenx
import MenuText
import GameText
import Language
import BBLib
import BUIx
import Raster
import BCopy
import shutil
import Reference
import Menu
import MenuWidget
import MemPersistence

import os
import string
import traceback
import time
import typing
import pprint

from Lumenx import printx, Raisex
from LumenLib import UtilsWidget

if typing.TYPE_CHECKING:
    apply = lambda fn, args=(), kwds={}: None
    execfile = lambda filename, globals=None, locals=None: None

# ----------------------------------
LUMEN_ROOT = Lumenx.GetLumenRoot()

f = open(LUMEN_ROOT + "/version", "r")
VERSION = string.strip(f.readline())
VERSION_DATE = string.strip(f.readline())
f.close()

BackImage = BBLib.B_BitMap24()
BackImageBanner = BBLib.B_BitMap24()
BackImage.ReadFromFile("../../Data/menu_mod.jpg")
BackImageBanner.ReadFromFile("../../Data/menu_mod_with_banner.jpg")

#
GRID_SIZE = (4, 3)
BORDER_SIZE = (464, 504)
BORDER_GAP = 38
DESC_MARGIN = 0.036
DESC_MAXLINES = 5
DESCR_WRAPPED = 0
#


# private database
class _DATA:
    menu_config = BCopy.deepcopy(Lumenx.GetConfig())
    mod_info = {}
    mod_list = []
    selected_map = ""
    character = ""
    character_skin = 0
    skin_available = 1


# ----------------------------------
BackOption = {
    "Name": "BACK",
    "Text": MenuText.GetMenuText("BACK"),
    "Font": Language.FontTitle,
    "VSep": Menu.BackOptionVSep,
    "Command": Menu.BackMenu,
}
BackOptionCommon = BCopy.deepcopy(BackOption)
BackOptionCommon["Font"] = Language.FontCommon

BackImageItem = {
    "Name": "Back",
    "Image": BackImage,
    "Kind": MenuWidget.B_BackImageWidget,
}

BackImageBannerItem = {
    "Name": "Back",
    "Image": BackImageBanner,
    "Kind": MenuWidget.B_BackImageWidget,
}

NoteLabel = {
    "Name": "NOTE",
    "Text": MenuText.GetMenuText(
        "Note: Current changes are not saved and will be saved when exiting this menu."
    ),
    "Font": Language.FontCommon,
    "FontScale": Language.MFontScale["M"],
    "VSep": Menu.NoteOptionVSep,
    "Color": Language.FontColor.Yellow,
    "Focusable": 0,
    "Visible": 0,
}


# ----------------------------------
# Start Game Option
# ----------------------------------
def GetCharType(this):
    return this.Options.index(_DATA.character)


def SetCharType(option):
    _DATA.character_skin = 0
    _DATA.character = option
    Menu.GetMenuWidget("CharPreview")[0].SetBitmap(
        UtilsWidget.CHARACTER[_DATA.character][_DATA.character_skin]
    )
    Menu.GetMenuWidget("Character Skin")[0].Focusable = (
        len(UtilsWidget.CHARACTER[_DATA.character]) > 1 and _DATA.skin_available
    )


def NextSkin(this):
    _DATA.character_skin = (_DATA.character_skin + 1) % len(
        UtilsWidget.CHARACTER[_DATA.character]
    )
    Menu.GetMenuWidget("CharPreview")[0].SetBitmap(
        UtilsWidget.CHARACTER[_DATA.character][_DATA.character_skin]
    )


def PreviousSkin(this):
    _DATA.character_skin = (_DATA.character_skin - 1) % len(
        UtilsWidget.CHARACTER[_DATA.character]
    )
    Menu.GetMenuWidget("CharPreview")[0].SetBitmap(
        UtilsWidget.CHARACTER[_DATA.character][_DATA.character_skin]
    )


def GetSelectedMap(this):
    _DATA.selected_map = this.Options[0]
    return 0


def SetSelectedMap(option):
    _DATA.selected_map = option


def StartGame(this):
    map_dir = ""
    mod_dir = Lumenx.GetCurrentModMenu()
    MapList = Lumenx.GetMapList(mod_dir)
    default_map = 0
    if string.lower(_DATA.selected_map) == "default":
        default_map = 1
    else:
        for k, v in MapList.items():
            if v == _DATA.selected_map:
                map_dir = k
                break
    if map_dir or default_map:
        MemPersistence.Delete("2DMapValues")
        MemPersistence.Delete("MainChar")
        #
        character = UtilsWidget.CHARACTER
        MemPersistence.Store(
            "SelectedChar",
            (
                character[_DATA.character][0],
                character[_DATA.character][_DATA.character_skin],
            ),
        )
        if not default_map:
            Lumenx.LoadLevel(map_dir, mod_dir)
        else:
            maps = {
                "Sargon": "ragnar_m2",
                "Naglfar": "dwarf_m3",
                "Zoe": "ruins_m4",
                "Tukaram": "barb_m1",
            }
            Lumenx.LoadLevel(maps[_DATA.character], mod_dir)


def SetStartGameOption(this):
    options = []
    map_name = []
    mod_dir = Lumenx.GetCurrentModMenu()

    _DATA.skin_available = this.MenuDescr.get("SkinAvailable", 1)
    optional_map = this.MenuDescr.get("OptionalMap", [])
    optional_char = this.MenuDescr.get(
        "OptionalChar", ["Sargon", "Naglfar", "Zoe", "Tukaram"]
    )
    banner = this.MenuDescr.get("Banner")
    background = this.MenuDescr.get(
        "Background",
        {
            "Name": "BackColor",
            "Kind": UtilsWidget.B_BackColor,
        },
    )
    startgame_command = this.MenuDescr.get("StartGameCommand", StartGame)

    _DATA.character = optional_char[0]
    _DATA.character_skin = 0
    if banner:
        options.append(banner)

    for map_dir in optional_map:
        name = Lumenx.GetMapListItem(map_dir, mod_dir)
        if name:
            map_name.append(name)

    if map_name:
        if len(map_name) > 1:
            map_option = {
                "Name": "Map",
                "Text": MenuText.GetMenuText("Map") + ": ",
                "VSep": "0.015%",
                "FontScale": Language.MFontScale["M"],
                "Kind": MenuWidget.B_MenuItemOption,
                "Options": map_name,
                "SelOptionFunc2": GetSelectedMap,
                "Command": SetSelectedMap,
            }
        else:
            map_option = None

        options = options + [
            {
                "Name": "Character",
                "Text": "",
                "VSep": Menu.FirstOptionVSep,
                "FontScale": Language.MFontScale["M"],
                "Kind": MenuWidget.B_MenuItemOption,
                "Options": optional_char,
                "SelOptionFunc2": GetCharType,
                "Command": SetCharType,
                "Focusable": len(optional_char) > 1,
            },
            {
                "Name": "CharPreview",
                "Kind": UtilsWidget.B_BitmapWidget,
                "VSep": "0.01%",
                "GetImageName": lambda this: UtilsWidget.CHARACTER[_DATA.character][
                    _DATA.character_skin
                ],
                "Size": (200, 200),
                "FitHeight": "0.19%",
                "Focusable": 0,
            },
            {
                "Name": "Character Skin",
                "Text": "< " + MenuText.GetMenuText("Next Skin") + " >",
                "VSep": "0.01%",
                "FontScale": Language.MFontScale["M"],
                "Command": NextSkin,
                "LeftCommand": NextSkin,
                "RightCommand": PreviousSkin,
                "Focusable": len(UtilsWidget.CHARACTER[_DATA.character]) > 1
                and _DATA.skin_available,
            },
            map_option,
            {
                "Name": "Start",
                "Text": MenuText.GetMenuText("Start"),
                "FontScale": Language.MFontScale["M"],
                "VSep": "0.015%",
                "Command": startgame_command,
            },
        ]
    #
    options = options + [
        BackOptionCommon,
        background,
    ]
    this.MenuDescr["ListDescr"] = options


# ----------------------------------
# Menu Option
# ----------------------------------
def InitMenu(this):
    global DESCR_WRAPPED
    if not DESCR_WRAPPED:
        DESCR_WRAPPED = 1
        if Bladex.GetStringValue("BODLoader.DescrWrap") is None:
            DescrWrap()
            Bladex.SetStringValue("BODLoader.DescrWrap", "")


def LeaveMenu(this):
    if _DATA.menu_config != Lumenx.GetConfig():
        Lumenx.SaveConfig(_DATA.menu_config)
        if _DATA.menu_config["Language"] != Language.Current:
            Lumenx.LoadLevel("Casa")


def EnterCurrentMod(this):
    options = ("MODS", "ALL MODS")
    for name in options:
        frame = Menu._MainMenu.MenuStack.Top()
        w, idx = Menu.GetMenuWidget(name, frame)
        frame.SetFocus_Idx(idx)
        w.ActivateItem(1)
    w = Menu.GetMenuWidget("MODS LIST")[0]
    sw, idx = Menu.GetMenuWidget(_DATA.mod_info[Lumenx.GetCurrentMod()]["Name"], w)
    w.SetFocus_Idx(idx, update_page=1)
    if Bladex.GetEntity("Player1").Life <= 0:
        Menu.GetMenuItem(["BACK TO GAME"], sw.MenuDescr)["Focusable"] = 0
        # sw.MenuDescr["NameFocus"] = "LOAD GAME"
    sw.ActivateItem(1)


def OnChangeMenu():
    if _DATA.menu_config != Lumenx.GetConfig():
        Menu.GetMenuWidget("NOTE")[0].SetVisible(1)
    else:
        Menu.GetMenuWidget("NOTE")[0].SetVisible(0)


def OnEnterModMenu(this):
    import SaveGame

    Lumenx.SetCurrentModMenu(this.Menudesc.get("ModDir", ""))
    #
    start_game = Menu.GetMenuWidget("START GAME", this)[0]
    if start_game:
        SetStartGameOption(start_game)
    #
    SaveGame.CreateSLMenu(this)


def OnLeaveModMenu(this):
    Lumenx.SetCurrentModMenu("")


#
def GetInvStyleOption(this):
    return this.Options.index(_DATA.menu_config["InventoryStyle"])


def SetInvStyle(option):
    _DATA.menu_config["InventoryStyle"] = option
    Menu.GetMenuWidget("InventoryActivatedByFocus")[0].Focusable = option == "Improved"
    Menu.GetMenuWidget("InventoryActivatedByNumbers")[0].Focusable = (
        option == "Improved"
    )
    OnChangeMenu()


def GetInvActivatedByFocusOption(this):
    this.Focusable = _DATA.menu_config["InventoryStyle"] == "Improved"
    return this.Options.index(_DATA.menu_config["InventoryActivatedByFocus"])


def SetInvActivatedByFocus(option):
    _DATA.menu_config["InventoryActivatedByFocus"] = option
    OnChangeMenu()


def GetInvActivatedByNumbersOption(this):
    this.Focusable = _DATA.menu_config["InventoryStyle"] == "Improved"
    return this.Options.index(_DATA.menu_config["InventoryActivatedByNumbers"])


def SetInvActivatedByNumbers(option):
    _DATA.menu_config["InventoryActivatedByNumbers"] = option
    OnChangeMenu()


def GetAimingPerspectiveOption(this):
    return this.Options.index(_DATA.menu_config["AimingPerspective"])


def SetAimingPerspective(option):
    _DATA.menu_config["AimingPerspective"] = option
    OnChangeMenu()


#
def GetEnableOption(this):
    return this.Options.index(_DATA.menu_config[this.MenuDescr["Name"]])


def SetEnable(option, this):
    _DATA.menu_config[this.MenuDescr["Name"]] = option
    OnChangeMenu()


#
def GetBasicCloneOption(this):
    return 0


def SetBasicClone(option):
    OnChangeMenu()


#
def SetLanguage(option):
    _DATA.menu_config["Language"] = option
    OnChangeMenu()


def GetLanguage(this):
    return this.Options.index(Language.Current)


# ----------------------------------
# Function
# ----------------------------------
def GetModList():
    return _DATA.mod_list


def GetModInfo(mod_dir):
    mod_dir = string.lower(mod_dir)
    return _DATA.mod_info.get(mod_dir, {})


def GetBackToGameItem(
    VSep=Menu.LastOptionVSep,
    Font=Language.FontTitle,
    FontScale=Language.MFontScale["L"],
):
    ret = {
        "Name": "BACK TO GAME",
        "Text": MenuText.GetMenuText("BACK TO GAME"),
        "VSep": VSep,
        "Font": Font,
        "FontScale": FontScale,
        "Command": Menu.BackToGame,
    }

    return ret


def GenEnableOption(name, text="", VSep="0.7em"):
    if text == "":
        text = name
    return {
        "Name": name,
        "Text": MenuText.GetMenuText(text) + ":",
        "Font": Language.FontCommon,
        "FontScale": Language.MFontScale["M"],
        "VSep": VSep,
        "Kind": MenuWidget.B_MenuItemOption,
        "Options": ["Enabled", "Disabled"],
        "SelOptionFunc2": GetEnableOption,
        "Command2": SetEnable,
    }


def IsModInstalled(mod_dir):
    return _DATA.mod_info[mod_dir]["Installed"]


def IsModEnabled(mod_dir):
    return _DATA.mod_info[mod_dir]["Enabled"]


def SetInstallMod(mod_dir):
    mod_info = _DATA.mod_info[mod_dir]
    if mod_info["Installed"] != -1:
        Installed = not mod_info["Installed"]
        mod_info["Installed"] = Installed
        mod_info["Enabled"] = Installed

        EnableMod(Installed, mod_info)
        SaveModInfo()


def SetEnableMod(mod_dir):
    mod_info = _DATA.mod_info[mod_dir]
    if mod_info["Installed"] == 1:
        Enabled = not mod_info["Enabled"]
        mod_info["Enabled"] = Enabled

        EnableMod(Enabled, mod_info)
        SaveModInfo()


def LoadMod(mod_info):
    # Reference.debugprint("[BODLoader] Load mod: %s" % mod_info["Name"])
    EnableMod(mod_info["Enabled"], mod_info)


def EnableMod(Enabled, mod_info):
    mod_dir = mod_info["ModDir"]
    mod_root = os.path.join(LUMEN_ROOT, "Mods", mod_dir)
    if Enabled:
        exec_file = os.path.join(mod_root, "BLModInit.py")
    else:
        exec_file = os.path.join(mod_root, "BLModShut.py")

    if os.path.isfile(exec_file):
        try:
            execfile(exec_file, {}, {})
            if Enabled:
                Reference.debugprint("[BODLoader] Enabled mod: %s" % mod_info["Name"])
            else:
                Reference.debugprint("[BODLoader] Disabled mod: %s" % mod_info["Name"])
        except:
            traceback.print_exc()


def AddMod(mod_dir, mod_root, BLModInfo):
    os.makedirs(os.path.join(mod_root, "Config"), exist_ok=True)
    mod_dir = string.lower(mod_dir)
    name_space = {"MOD_ROOT": mod_root, "MOD_DIR": mod_dir}

    execfile(BLModInfo, name_space, name_space)
    CloneEnvironment = name_space.get("CloneEnvironment", 1)
    MapList = name_space.get("MapList", {})
    Lumenx.AddMapList(MapList, mod_dir)
    #
    GTexts = os.path.join(mod_root, "Data/Locale/English/GTexts.py")
    if os.path.isfile(GTexts):
        execfile(GTexts, name_space, name_space)
    GameText.Textos.update(name_space.get("Textos", {}))
    if Language.Current != "English":
        GTexts = os.path.join(mod_root, "Data/Locale/%s/GTexts.py" % Language.Current)
        MTexts = os.path.join(mod_root, "Data/Locale/%s/MTexts.py" % Language.Current)
        for file in (GTexts, MTexts):
            if os.path.isfile(file):
                execfile(file, name_space, name_space)
        GameText.Textos.update(name_space.get("Textos", {}))
        MenuText.ForeingDict.update(name_space.get("ForeingDict", {}))

    # XXX 需要优化，通过IPC调用外部python程序复制引擎需要的文件
    if CloneEnvironment:
        os.makedirs(os.path.join(mod_root, "Data/ControlFonts"), exist_ok=True)
        os.makedirs(os.path.join(mod_root, "Sounds"), exist_ok=True)
        for file in (
            "Data/ControlFonts/glyphs_gamepad_font.png",
            "Data/ControlFonts/glyphs_keyboard_font.bmp",
            "Data/ControlFonts/glyphs_playstation_font.png",
            "Data/ControlFonts/glyphs_steamDeck_font.bmp",
            "Data/ControlFonts/glyphs_xbox_font.png",
            #
            "Data/FontTitle_8bpp.fnt",
            "Data/FontTitle_8bpp_0.png",
            "Data/FontCommon_8bpp.fnt",
            "Data/FontCommon_8bpp_0.png",
            #
            "Sounds/M-FUEGO-ANTORCHA3.wav",
        ):
            dst = os.path.join(mod_root, file)
            # if not os.path.exists(dst):
            shutil.copy(os.path.join(LUMEN_ROOT, file), dst)

    #
    if string.lower(name_space["ModVersion"][0]) == "v":
        name_space["ModVersion"] = name_space["ModVersion"][1:]

    show = (None, 0, 0)
    img_file = os.path.join(mod_root, "show.jpg")
    if os.path.isfile(img_file):
        img = BBLib.B_BitMap24()
        img.ReadFromFile(img_file)
        size = UtilsWidget.ResizeImage(img.GetDimension(), (464, 261))
        show = (img, size[0], size[1])

    BLModInit = os.path.join(mod_root, "BLModInit.py")
    Enabled = _DATA.mod_info.get(mod_dir, {}).get("Enabled", 0)
    Installed = _DATA.mod_info.get(mod_dir, {}).get("Installed", -1)
    if not os.path.isfile(BLModInit):
        Installed = -1
    elif Installed == -1:
        Installed = 0
    # BLModInit文件被用户意外删除的情况
    if Installed != 1:
        Enabled = 0

    mod_info = name_space.get("ModMenu", {})
    mod_info.update(
        {
            "Name": name_space["ModName"],
            "ModDir": mod_dir,
            "Desc": GameText.Textos.get(name_space["ModDesc"], ""),
            "Version": name_space["ModVersion"],
            "Author": name_space["ModAuthor"],
            "AuthorInfo": name_space["ModAuthorInfo"],
            #
            "AssetAnimation": name_space.get("AssetAnimation", []),
            "AssetImage": name_space.get("AssetImage", []),
            "AssetModel": name_space.get("AssetModel", []),
            "AssetSound": name_space.get("AssetSound", []),
            "AssetOther": name_space.get("AssetOther", []),
            #
            "GameBasics": name_space.get("GameBasics", 0),
            "PrivateControl": name_space.get("PrivateControl", 0),
            "CloneEnvironment": CloneEnvironment,
            #
            "Show": show,
            "OnLeaveMode": "to_parent",
            "OnLeave": OnLeaveModMenu,
            #
            "Installed": Installed,
            "Enabled": Enabled,
            # "DisableCallback": name_space.get("DisableCallback", None),
        }
    )
    _DATA.mod_list.append(mod_dir)
    _DATA.mod_info[mod_dir] = mod_info


def SaveModInfo():
    save_keys = (
        "Name",
        # "ModDir",
        "Desc",
        "Version",
        "Author",
        "AuthorInfo",
        "Installed",
        "Enabled",
    )
    mod_info = {}
    for mod_dir in _DATA.mod_list:
        info = {}
        for key in _DATA.mod_info[mod_dir].keys():
            if key in save_keys:
                info[key] = _DATA.mod_info[mod_dir][key]
        mod_info[mod_dir] = info
    #
    pp = pprint.PrettyPrinter(indent=4)
    f = open(os.path.join(LUMEN_ROOT, "Config/BLData.cfg"), "w")
    f.write(pp.pformat(mod_info))
    f.close()


def Init():
    f = open(os.path.join(LUMEN_ROOT, "Config/BLData.cfg"), "a+")
    try:
        _DATA.mod_info = eval(f.read())
    except:
        pass
    f.close()
    Bladex.DeleteStringValue("BODLoader.DescrWrap")
    #
    ModListPath = os.path.join(LUMEN_ROOT, "Mods")
    for mod_dir in os.listdir(ModListPath):
        mod_root = os.path.join(ModListPath, mod_dir)
        if not os.path.isdir(mod_root):
            continue
        BLModInfo = os.path.join(mod_root, "BLModInfo.py")
        if not os.path.isfile(BLModInfo):
            continue
        #
        Reference.debugprint("[BODLoader] Found mod: " + mod_dir)
        try:
            AddMod(mod_dir, mod_root, BLModInfo)
        except:
            traceback.print_exc()

    #
    def compare(x, y):
        if _DATA.mod_info[x]["Name"] < _DATA.mod_info[y]["Name"]:
            return -1  # x 应该排在 y 前面
        elif _DATA.mod_info[x]["Name"] > _DATA.mod_info[y]["Name"]:
            return 1  # x 应该排在 y 后面
        else:
            return 0

    _DATA.mod_list.sort(compare)  # type: ignore
    #
    nMods = len(_DATA.mod_list)
    ModMenu["ListDescr"][0]["ListDescr"][0]["Text"] = (
        MenuText.GetMenuText("Total Mods") + ": " + str(nMods)
    )

    for k in _DATA.mod_info.keys():
        if k not in _DATA.mod_list:
            del _DATA.mod_info[k]
    SaveModInfo()
    #
    for mod_info in _DATA.mod_info.values():
        Installed = mod_info["Installed"]
        if Installed == 1:
            LoadMod(mod_info)


def DescrWrap():
    view_size = Raster.GetSize()
    border_size = UtilsWidget.AdaptResolution(BORDER_SIZE, (3840, 2160), view_size)
    border_scale = border_size[0] / float(BORDER_SIZE[0])
    MaxWidth = BORDER_SIZE[0] * (1 - DESC_MARGIN * 2) * border_scale
    font_scale = Language.FontScale["M"] * 0.8
    font_behaviour = Language.font_behaviour_common
    for mod_dir, mod_info in _DATA.mod_info.items():
        desc = mod_info["Desc"]
        if desc == "":
            continue
        # screen_scale = Raster.GetUnscaledSize()[0] / float(Raster.GetSize()[0])
        lines = UtilsWidget.WrapText(
            desc,
            MaxWidth,
            font_scale,
            font_behaviour,
        )
        mod_info["Desc"] = string.join(lines[:DESC_MAXLINES], "\n")
    # Reference.debugprint("[BODLoader] Description wrapped")


# ----------------------------------
# Menu Tree
# ----------------------------------

ModMenu = {
    "Name": "MODS",
    "Text": MenuText.GetMenuText("MODS"),
    # "FrameKind": MenuWidget.B_MenuTree,
    "Font": Language.FontTitle,
    "VSep": 8,
    "Command": InitMenu,
    "OnLeave": LeaveMenu,
    "ListDescr": [
        {
            "Name": "ALL MODS",
            "Text": MenuText.GetMenuText("ALL MODS"),
            "Font": Language.FontTitle,
            # "Size": (640, 480),
            "VSep": Menu.FirstOptionVSep,
            "ListDescr": [
                {
                    "Name": "Total Mods",
                    "Font": Language.FontTitle,
                    # "FontScale": Language.MFontScale["M"],
                    "VSep": "0.0673f",
                    "VAnchor": BUIx.B_FrameWidget.B_FR_VCenter,
                    "Focusable": 0,
                },
                {
                    "Name": "MODS LIST",
                    "Kind": UtilsWidget.B_ModGridWidget,
                    "Floating": 1,
                    "VSep": "0.1346%",
                    # "VIndicator": BUIx.B_FrameWidget.B_FR_VRelative,
                    # "VAnchor": BUIx.B_FrameWidget.B_FR_VCenter,
                },
                {
                    "Name": "BackColor",
                    "Kind": UtilsWidget.B_BackColor,
                    "Alpha": 0.4,
                },
                BackImageItem,
            ],
            # "Size": ("auto", 480),
            # "SizeFor": (CLASSIC_VER,),
        },
        {
            "Name": "OPTIONS",
            "Text": MenuText.GetMenuText("OPTIONS"),
            "Font": Language.FontTitle,
            "VSep": "1em",
            "OnLeave": LeaveMenu,
            "ListDescr": [
                {
                    "Name": "Basic Clone",
                    "Text": MenuText.GetMenuText("Basic Clone") + ":",
                    "Font": Language.FontCommon,
                    "FontScale": Language.MFontScale["M"],
                    "VSep": Menu.FirstOptionVSep,
                    "Kind": MenuWidget.B_MenuItemOption,
                    "Options": ["Default"],
                    "SelOptionFunc2": GetBasicCloneOption,
                    "Command": SetBasicClone,
                },
                {
                    "Name": "InventoryStyle",
                    "Text": MenuText.GetMenuText("Inventory Style") + ":",
                    "Font": Language.FontCommon,
                    "FontScale": Language.MFontScale["M"],
                    "VSep": "0.7em",
                    "Kind": MenuWidget.B_MenuItemOption,
                    "Options": ["Original", "Improved"],
                    "SelOptionFunc2": GetInvStyleOption,
                    "Command": SetInvStyle,
                },
                {
                    "Name": "InventoryActivatedByFocus",
                    "Text": MenuText.GetMenuText("Activated By Focus") + ":",
                    "Font": Language.FontCommon,
                    "FontScale": Language.MFontScale["M"],
                    "VSep": 0,
                    "Kind": MenuWidget.B_MenuItemOption,
                    "Options": ["Weapon", "Shield", "Object"],
                    "SelOptionFunc2": GetInvActivatedByFocusOption,
                    "Command": SetInvActivatedByFocus,
                },
                {
                    "Name": "InventoryActivatedByNumbers",
                    "Text": MenuText.GetMenuText("Activated By Numbers") + ":",
                    "Font": Language.FontCommon,
                    "FontScale": Language.MFontScale["M"],
                    "VSep": 0,
                    "Kind": MenuWidget.B_MenuItemOption,
                    "Options": ["Weapon", "Shield", "Object"],
                    "SelOptionFunc2": GetInvActivatedByNumbersOption,
                    "Command": SetInvActivatedByNumbers,
                },
                GenEnableOption("GrillableLimb", "Grillable Limb", VSep="0.7em"),
                GenEnableOption(
                    "DodgeByMouseMovement", "Dodge By Mouse Movement", VSep="0"
                ),
                GenEnableOption(
                    "ArcheryTrajectory", "Archery Trajectory", VSep="0.7em"
                ),
                {
                    "Name": "AimingPerspective",
                    "Text": MenuText.GetMenuText("Aiming Perspective") + ":",
                    "Font": Language.FontCommon,
                    "FontScale": Language.MFontScale["M"],
                    "VSep": 0,
                    "Kind": MenuWidget.B_MenuItemOption,
                    "Options": ["Nearest", "Maintain Current"],
                    "SelOptionFunc2": GetAimingPerspectiveOption,
                    "Command": SetAimingPerspective,
                },
                GenEnableOption("Cache", VSep="0.7em"),
                NoteLabel,
                BackOptionCommon,
                BackImageBannerItem,
            ],
        },
        {
            "Name": "Developer Features",
            "Text": MenuText.GetMenuText("Developer Features"),
            "Font": Language.FontTitle,
            "VSep": "1em",
            "OnLeave": LeaveMenu,
            "ListDescr": [],
        },
        NoteLabel,
        BackOption,
        {
            "Name": "Version",
            "Text": "%s: %s (%s)"
            % (MenuText.GetMenuText("Version"), VERSION, VERSION_DATE),
            "Font": Language.FontCommon,
            "FontScale": Language.MFontScale["S"],
            "VSep": "0.959f",
            "Focusable": 0,
        },
        BackImageBannerItem,
    ],
}

# -------------------------------------
