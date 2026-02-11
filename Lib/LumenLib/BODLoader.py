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

import os
import string
import traceback
import time
import typing

from Lumenx import printx, Raisex
from LumenLib import UtilsWidget

if typing.TYPE_CHECKING:
    apply = lambda fn, args=(), kwds={}: None
    execfile = lambda filename, globals=None, locals=None: None

# ----------------------------------
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

LUMEN_ROOT = Lumenx.GetLumenRoot()


# private database
class _DATA:
    menu_config = BCopy.deepcopy(Lumenx.GetConfig())
    mod_info = {}
    mod_list = []


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
def InitMenu(this):
    global DESCR_WRAPPED
    if not DESCR_WRAPPED:
        DESCR_WRAPPED = 1
        if string.lower(Lumenx.GetCurrentMap()) == "casa":
            DescrWrap()


def LeaveMenu(this):
    if _DATA.menu_config != Lumenx.GetConfig():
        Lumenx.SaveConfig(_DATA.menu_config)
        if _DATA.menu_config["Language"] != Language.Current:
            Lumenx.LoadLevel("Casa")


def OnChangeMenu():
    if _DATA.menu_config != Lumenx.GetConfig():
        Menu.GetMenuWidget("NOTE")[0].SetVisible(1)
    else:
        Menu.GetMenuWidget("NOTE")[0].SetVisible(0)


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


#
def GetCacheOption(this):
    return this.Options.index(_DATA.menu_config["Cache"])


def SetCache(option):
    _DATA.menu_config["Cache"] = option
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
def GetModList():
    return _DATA.mod_list


def GetModInfo(mod_dir):
    mod_dir = string.lower(mod_dir)
    return _DATA.mod_info.get(mod_dir, {})


def AddMod(mod_dir, mod_root, BLModInfo):
    mod_dir = string.lower(mod_dir)
    name_space = {}

    execfile(BLModInfo, name_space, name_space)
    CloneEnvironment = name_space["CloneEnvironment"]
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

    # 复制引擎需要的文件
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
            if not os.path.exists(dst):
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

    mod_info = {
        "Name": name_space["ModName"],
        "Desc": GameText.Textos.get(name_space["ModDesc"], ""),
        "Version": name_space["ModVersion"],
        "Author": name_space["ModAuthor"],
        "AuthorInfo": name_space["ModAuthorInfo"],
        "Show": show,
    }
    _DATA.mod_list.append(mod_dir)
    _DATA.mod_info[mod_dir] = mod_info


def Init():
    ModListPath = os.path.join(Lumenx.GetLumenRoot(), "Mods")
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
    ModMenu["ListDescr"][0]["ListDescr"][0]["Text"] = (
        MenuText.GetMenuText("Total Mods") + ": " + str(len(GetModList()))
    )
    # 描述包装
    # if Language.Current == "English":
    #     Bladex.SetAfterFrameFunc("[BODLoader]DescrWrap[NSAVE]", DescrWrapAfterFrame)


# def DescrWrapAfterFrame(t):
#     if not globals().has_key("DescrWrap_Start"):
#         globals()["DescrWrap_Start"] = time.time()
#         return
#     if time.time() - globals()["DescrWrap_Start"] < 0.3:
#         return
#     Bladex.RemoveAfterFrameFunc("[BODLoader]DescrWrap[NSAVE]")
#     DescrWrap()


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
# def GetModMenu():

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
            "VSep": "0.208%",
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
                    "VSep": "0.1346f",
                    # "VIndicator": BUIx.B_FrameWidget.B_FR_VRelative,
                    # "VAnchor": BUIx.B_FrameWidget.B_FR_VCenter,
                    # "ListDescr": [],
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
                    "VSep": "0.208%",
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
                    "VSep": "1em",
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
                {
                    "Name": "Cache",
                    "Text": MenuText.GetMenuText("Cache") + ":",
                    "Font": Language.FontCommon,
                    "FontScale": Language.MFontScale["M"],
                    "VSep": "1em",
                    "Kind": MenuWidget.B_MenuItemOption,
                    "Options": ["Enabled", "Disabled"],
                    "SelOptionFunc2": GetCacheOption,
                    "Command": SetCache,
                },
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
        BackImageBannerItem,
    ],
}
# return ModMenu
# -------------------------------------
Init()
