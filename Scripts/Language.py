#  _    _   _ __  __ _____ _   _
# | |  | | | |  \/  | ____| \ | |
# | |  | | | | |\/| |  _| |  \| |
# | |__| |_| | |  | | |___| |\  |
# |_____\___/|_|  |_|_____|_| \_|
#
# Change list:
# * Refactor text UI
#

import Lumenx
import BBLib
import BUIx
import os

from Lumenx import printx, Raisex

AvailableLanguages = [
    "Chinese",
    "English",
    "French",
    "German",
    "Italian",
    "Russian",
    "Spanish",
]


class FontColor:
    Focused = (252, 247, 167)
    Unfocused = (207, 144, 49)
    Unfocusable = (125, 91, 36)
    Red = (200, 0, 0)
    Green = (0, 200, 0)
    Blue = (0, 128, 255)
    Yellow = (210, 210, 0)
    LightBlue = (0, 160, 220)
    Cyan = (119, 241, 252)
    Magenta = (210, 0, 210)
    White = (200, 200, 200)
    Black = (0, 0, 0)


# Menu Font Scale
MFontScale = {"L": 0.65, "M": 0.44, "S": 0.32}
# Game Font Scale
FontScale = MFontScale.copy()
if Lumenx.GetGameVersion() != Lumenx.CLASSIC_VER:
    for k in FontScale.keys():
        FontScale[k] = round(FontScale[k] / 1.5, 2)


FontTitle = ""
FontCommon = ""

Current = BBLib.GetCurrentLanguage()
# Current = "Russian"
# Current = "Spanish"
# Current = "English"
# Current = "Chinese"

if Lumenx.GetGameVersion() == Lumenx.CLASSIC_VER:
    FontTitle = os.path.join(Lumenx.GetLumenRoot(), "Data/FontTitleC.bmp")
    FontCommon = os.path.join(Lumenx.GetLumenRoot(), "Data/FontCommonC.bmp")
elif Lumenx.GetGameVersion() == Lumenx.V109_VER:
    if Current == "English":
        FontTitle = "../../Data/FontTitle_8bpp.fnt"
        FontCommon = "../../Data/FontCommon_8bpp.fnt"
    elif Current in ("Chinese", "Russian"):
        FontTitle = "../../Data/FontCommon_8bpp.fnt"
        FontCommon = "../../Data/FontCommon_8bpp.fnt"
    else:
        FontTitle = os.path.join(Lumenx.GetLumenRoot(), "Data/FontTitle.bmp")
        FontCommon = os.path.join(Lumenx.GetLumenRoot(), "Data/FontCommon.bmp")
else:
    assert False, "Unsupported game version"

if FontTitle[-4:] == ".fnt":
    UpArrow = "½"
    DownArrow = "¾"
else:
    UpArrow = chr(189)
    DownArrow = chr(190)

# if Current == "Chinese":
#     MapaDeLetras = "../../Data/fontCN32.fnt"
#     MapaDeLetrasHi = "../../Data/fontCN42.fnt"
#     LetrasMenu = "../../Data/fontCN18.fnt"
#     LetrasMenuSmall = "../../Data/fontCN32.fnt"
#     LetrasMenuBig = "../../Data/fontCN32.fnt"
#     MenuGrasHi = "../../Data/fontCN72.fnt"
#     CtrlMenu = "../../Data/fontCN16.fnt"
# elif Current == "Russian":
#     MapaDeLetras = "../../Data/fontRu16.fnt"
#     MapaDeLetrasHi = "../../Data/fontRu32.fnt"
#     LetrasMenu = "../../Data/fontRu16.fnt"
#     LetrasMenuSmall="../../Data/fontRu16.fnt"
#     LetrasMenuBig="../../Data/fontRu30.fnt"
#     MenuGrasHi="../../Data/fontRu100.fnt"
# else:
#     MapaDeLetrasHi = "../../Data/Mapa de letras_hi.bmp"
#     MapaDeLetras = "../../Data/Mapa de letras.bmp"
#     LetrasMenu = "../../Data/Letras menu med.bmp"
#     LetrasMenuSmall="../../Data/Letras menu peq.bmp"
#     LetrasMenuBig="../../Data/letras_menu_gra.bmp"
#     MenuGrasHi="../../Data/letras_menu_gras_hi.bmp"

#
font_server_behaviour = BUIx.B_FontServer()
font_behaviour_title = font_server_behaviour.CreateBFont(FontTitle)
font_behaviour_common = font_server_behaviour.CreateBFont(FontCommon)
#


def CheckFallback():
    if not os.path.exists("../../SOUNDS/" + Current + "/kashgar-antepasados.ogg"):
        return "EnglishUs"
    return Current
