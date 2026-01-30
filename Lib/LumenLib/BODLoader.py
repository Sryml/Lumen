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
import BCopy
import Menu
import MenuWidget

from Lumenx import printx, Raisex
from LumenLib import UtilsWidget

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
    return this.Options.index(_DATA.menu_config["InventoryActivatedByFocus"])


def SetInvActivatedByFocus(option):
    _DATA.menu_config["InventoryActivatedByFocus"] = option
    OnChangeMenu()


def GetInvActivatedByNumbersOption(this):
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
                    "Name": "InventoryStyle",
                    "Text": MenuText.GetMenuText("Inventory Style") + ":",
                    "Font": Language.FontCommon,
                    "FontScale": Language.MFontScale["M"],
                    "VSep": "0.208%",
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
                    "Focusable": _DATA.menu_config["InventoryStyle"] == "Improved",
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
                    "Focusable": _DATA.menu_config["InventoryStyle"] == "Improved",
                },
                {
                    "Name": "Cache",
                    "Text": MenuText.GetMenuText("Cache") + ":",
                    "Font": Language.FontCommon,
                    "FontScale": Language.MFontScale["M"],
                    "VSep": "0.7em",
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
