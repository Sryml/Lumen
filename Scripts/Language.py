

import BBLib
import os


#Current = "Spanish"
#Current = "English"
Current = BBLib.GetCurrentLanguage()

if Current == "Chinese":
    MapaDeLetras = "../../Data/fontCN32.fnt"
    MapaDeLetrasHi = "../../Data/fontCN42.fnt"
    LetrasMenu = "../../Data/fontCN18.fnt"
    LetrasMenuSmall="../../Data/fontCN32.fnt"
    LetrasMenuBig="../../Data/fontCN32.fnt"
    MenuGrasHi="../../Data/fontCN72.fnt"
    CtrlMenu="../../Data/fontCN16.fnt"
elif Current == "Russian":
    MapaDeLetras = "../../Data/fontRu16.fnt"
    MapaDeLetrasHi = "../../Data/fontRu32.fnt"
    LetrasMenu = "../../Data/fontRu16.fnt"
    LetrasMenuSmall="../../Data/fontRu16.fnt"
    LetrasMenuBig="../../Data/fontRu30.fnt"
    MenuGrasHi="../../Data/fontRu100.fnt"
else:
    MapaDeLetrasHi = "../../Data/Mapa de letras_hi.bmp"
    MapaDeLetras = "../../Data/Mapa de letras.bmp"
    LetrasMenu = "../../Data/Letras menu med.bmp"
    LetrasMenuSmall="../../Data/Letras menu peq.bmp"
    LetrasMenuBig="../../Data/letras_menu_gra.bmp"
    MenuGrasHi="../../Data/letras_menu_gras_hi.bmp"

def CheckFallback():
    if not os.path.exists("../../SOUNDS/"+Current+"/kashgar-antepasados.ogg"):
        return "EnglishUs"
    return Current
