#  _    _   _ __  __ _____ _   _
# | |  | | | |  \/  | ____| \ | |
# | |  | | | | |\/| |  _| |  \| |
# | |__| |_| | |  | | |___| |\  |
# |_____\___/|_|  |_|_____|_| \_|
#

import Bladex
import Lumenx
import MenuText
import Language
import BBLib
import BUIx
import Raster
import UtilsWidget
import BCopy
import Menu
import MenuWidget

from Lumenx import printx, Raisex

# ----------------------------------
BackImage = BBLib.B_BitMap24()
BackImageBanner = BBLib.B_BitMap24()
BackImage.ReadFromFile("../../Data/menu_mod.jpg")
BackImageBanner.ReadFromFile("../../Data/menu_mod_with_banner.jpg")


# private database
class _DATA:
    menu_config = BCopy.deepcopy(Lumenx.GetConfig())
    mod_info = {}


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

BackImage = {
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
# def InitMenu(this):
#     _DATA.menu_config = BCopy.deepcopy(Lumenx.GetConfig())


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
def Init():
    pass


# ----------------------------------
# def GetModMenu():

ModMenu = {
    "Name": "MODS",
    "Text": MenuText.GetMenuText("MODS"),
    # "FrameKind": MenuWidget.B_MenuTree,
    "Font": Language.FontTitle,
    "VSep": 8,
    # "Command": InitMenu,
    "OnLeave": LeaveMenu,
    "ListDescr": [
        {
            "Name": "ALL MODS",
            "Text": MenuText.GetMenuText("ALL MODS"),
            "Font": Language.FontTitle,
            "VSep": "0.208%",
            "ListDescr": [],
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
                    "Name": "Cache",
                    "Text": MenuText.GetMenuText("Cache") + ":",
                    "Font": Language.FontCommon,
                    "FontScale": Language.MFontScale["M"],
                    "VSep": "0.208%",  # "1em",
                    "Kind": MenuWidget.B_MenuItemOption,
                    "Options": ["Enabled", "Disabled"],
                    "SelOptionFunc2": GetCacheOption,
                    "Command": SetCache,
                },
                NoteLabel,
                BackOptionCommon,
                BackImage,
            ],
        },
        {
            "Name": "Basic Clone",
            "Text": MenuText.GetMenuText("Basic Clone") + ":",
            "Font": Language.FontTitle,
            "VSep": "1em",
            "Kind": MenuWidget.B_MenuItemOption,
            "Options": [],
            "SelOptionFunc2": GetBasicCloneOption,
            "Command": SetBasicClone,
        },
        NoteLabel,
        BackOption,
        BackImage,
    ],
}
# return ModMenu
