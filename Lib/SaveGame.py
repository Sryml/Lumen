#  _    _   _ __  __ _____ _   _
# | |  | | | |  \/  | ____| \ | |
# | |  | | | | |\/| |  _| |  \| |
# | |__| |_| | |  | | |___| |\  |
# |_____\___/|_|  |_|_____|_| \_|
#
# Change list:
# * Refactor
#

import MenuText
import Bladex
import Lumenx
import netwidgets
import MenuWidget
import os
import time
import string
import Reference
import AuxFuncs
import stat
import Language
import BCopy

MFontScale = Language.MFontScale
printx = Lumenx.printx
EMPTY_SLOT = MenuText.GetMenuText("<Empty Slot>")
DATE_FORMAT = MenuText.GetMenuText("%d/%m %H:%M")
EMPTY_IMAGE = "../../Data/Empty.BMP"
SaveCounter = []

for i in range(2):
    SaveCounter.append("Awesome!")

for i in range(3):
    SaveCounter.append("Heroic")

for i in range(4):
    SaveCounter.append("Bold")

for i in range(5):
    SaveCounter.append("Normal")

for i in range(6):
    SaveCounter.append("Cautious")

for i in range(7):
    SaveCounter.append("Overcautious")

SaveCounter.append("Lame")
#
# Utils to save/load games.
#


def ElUsuarioPresionaLaTeclaEscape(Salio):
    return 1


def LoadGameAux(slot_num):
    import Language
    import SplashImage

    # by Sryml: start
    save_dir = "../../Save/SaveGame%s_files" % (slot_num,)
    save_file = os.path.join(save_dir, "SaveGame%s.py" % (slot_num,))
    file_data_aux = open("%s/%saux" % (save_dir, "aux"), "rt")
    lines = file_data_aux.readlines()
    file_data_aux.close()
    map_dir = string.strip(lines[2])
    mod_dir = string.strip(lines[3])
    printx("%s, %s" % (repr(mod_dir), map_dir))

    lines = ["import sys", "isLumen = 1"]
    lumen_root = Lumenx.GetLumenRoot()
    if mod_dir:
        mod_root = os.path.join(lumen_root, Lumenx.ModListPath, mod_dir)
        new_lumen_root = "..\\..\\..\\.."
    else:
        mod_root = lumen_root
        new_lumen_root = "..\\.."
    map_path = os.path.join(mod_root, "Maps", map_dir)
    #
    new_mod_root = "..\\.."
    new_blade_root = new_lumen_root + "\\.."
    if new_mod_root != new_lumen_root:
        lines.append("sys.path.append('%s/Lib')" % new_mod_root)
        lines.append("sys.path.append('%s/Lib/PythonLib')" % new_mod_root)

    scr_name = "../../Data/Menu/Save/" + Language.Current + "/Cerrando_hi.jpg"
    SplashImage.ShowImage(scr_name, 0)
    Bladex.BeginLoadGame()
    prev_map_root = os.path.normpath(os.getcwd() + "\\..")
    os.chdir(map_path)
    new_map_dir = os.path.relpath(os.getcwd(), prev_map_root)

    lines = lines + [
        "sys.path.append('%s/Lib')" % new_lumen_root,
        "sys.path.append('%s/Lib/PythonLib')" % new_lumen_root,
        "sys.path.append('%s/Lib/PythonLib')" % new_blade_root,
        "sys.path.append('%s/Lib/PythonLib/Plat-Win')" % new_blade_root,
        "import Lumenx",
        "execfile('../../Scripts/sys_init.py')",
        "InNewMap = %d"
        % (string.lower(new_map_dir) != string.lower(Lumenx.GetCurrentMap())),
        "execfile(%s)" % (repr(string.replace(save_file, "\\", "/")),),
    ]

    Bladex.CloseLevel(string.join(lines, ";"), new_map_dir)
    # by Sryml: end


def LoadGameFromDisk(menu_class):
    LoadGameAux(menu_class.MenuDescr["Clave"])


def SaveGameToDisk(menu_class):
    import Menu
    import Scorer
    import MenuText
    import GameText
    import GotoMapVars

    global SaveGameString

    # Back to game
    Menu._MainMenu.DeActivateMenuItem()
    Menu._MainMenu.DeActivateMenuItem()
    Menu._MainMenu.DeActivateMenuItem()
    Menu._MainMenu.DeActivateMenuItem()

    clave = menu_class.MenuDescr["Clave"]
    save_dir = "../../Save/SaveGame%s_files" % (clave,)

    # save Screen shoot
    Scorer.SetVisible(0)
    Bladex.SaveScreenShot("../../Save/Temp.BMP", 288, 162)  # 160, 120
    SaveGameString = (
        "import GameState;state=GameState.WorldState();state.GetState();state.SaveState(%s);state=None;GameState=None;"
        % repr(save_dir)
    )

    # Save the game
    Bladex.PauseSoundSystem()
    Bladex.StopTime()
    Bladex.SetRunString(
        SaveGameString
        + "Scorer.SetVisible(1);Bladex.RestartTime();Bladex.ResumeSoundSystem()"
    )


def GetBack(menu_class):
    import Menu

    Menu._MainMenu.DeActivateMenuItem()


# SaveBitmaps = (
#     ("1", "../../Save/1.BMP"),
#     ("2", "../../Save/2.BMP"),
#     ("3", "../../Save/3.BMP"),
#     ("4", "../../Save/4.BMP"),
#     ("5", "../../Save/5.BMP"),
#     ("6", "../../Save/6.BMP"),
#     ("7", "../../Save/7.BMP"),
#     ("8", "../../Save/8.BMP"),
# )

SAVEGAMEIMAGE = "0"
LOADGAMEIMAGE = "0"


def GetSaveGameImage():
    return SAVEGAMEIMAGE


def GetLoadGameImage():
    return LOADGAMEIMAGE


def FocusOnBitmap(menu_class=0, parametro=0):
    import Menu

    clave = menu_class.MenuDescr["Clave"]
    netwidgets.ChangePlayer(clave)
    label = Menu.GetMenuWidget("Current Selection", menu_class.Parent)
    if label:
        label.Text = MenuText.GetMenuText("Current Selection") + ": " + clave


# called when the menu is called


# ----------------------------------
# by Sryml: start
# ----------------------------------
def ReviveSave(this):
    import MemPersistence

    for exec_str in this.MenuDescr["ReviveExecStr"]:
        eval(exec_str)
    Lumenx.LoadLevel(this.MenuDescr["ReviveMapDir"], this.MenuDescr["ReviveModDir"])


def GetSaveDesc():
    import GameText
    import GotoMapVars

    char = Bladex.GetEntity("Player1")
    kind = char.Kind
    if string.upper(kind[-2:]) == "_N":
        kind = kind[:-2]
    cadtime = time.strftime(DATE_FORMAT, time.localtime(time.time()))
    mapname = Lumenx.GetCurrentMap()
    #
    Reference.TimesSaved = Reference.TimesSaved + 1
    nMaps = 1
    for v in GotoMapVars.VisitedMaps:
        if v:
            nMaps = nMaps + 1
    vismap = (Reference.TimesSaved - 1) / nMaps
    if vismap >= len(SaveCounter):
        DisgustingMessage = SaveCounter[-1]
    else:
        DisgustingMessage = SaveCounter[vismap]
    #
    ret = (
        'MenuText.GetMenuText(GameText.MapDescriptor(%s)) + " - Lv.%d " + MenuText.GetMenuText(%s) + " - %s - %d " + (MenuText.GetMenuText(%s))'
        % (
            repr(mapname),
            char.Level + 1,
            repr(kind),
            cadtime,
            Reference.TimesSaved,
            repr(DisgustingMessage),
        )
    )
    return ret


def CreateSLMenu(menu_class):
    import GameText
    import Menu

    SaveMenu = Menu.GetMenuWidget("SAVE GAME", menu_class)
    LoadMenu = Menu.GetMenuWidget("LOAD GAME", menu_class)
    if not (SaveMenu and LoadMenu):
        return
    #
    revive_descr = MenuText.GetMenuText("Restarting can revive this save!")
    SaveBitmaps = [("0", EMPTY_IMAGE, EMPTY_SLOT)]
    mod = menu_class.Menudesc.get("Mod", "")
    #
    save_root = os.path.join(Lumenx.GetLumenRoot(), mod, "Save")
    if not os.path.exists(save_root):
        os.mkdir(save_root)
    #
    SaveListDescr = [
        {
            "Name": "Title",
            "Text": MenuText.GetMenuText("SAVE GAME"),
            "VSep": "0.05%",
            "Font": Language.FontTitle,
            "Focusable": 0,
        },
        {
            "Name": "GameList",
            "Kind": netwidgets.B_ImageListWidget,
            "ImageList": SaveBitmaps,
            "MaxHeight": 162,
            # "GetCharType": GetSaveGameImage,
            "VSep": 6,
        },
    ]
    LoadListDescr = [SaveListDescr[0].copy(), SaveListDescr[1].copy()]
    LoadListDescr[0]["Text"] = MenuText.GetMenuText("LOAD GAME")
    # LoadListDescr[1]["GetCharType"] = GetLoadGameImage
    LoadListDescr.append(
        {
            "Name": "Restart",
            "Text": MenuText.GetMenuText("Restart")
            + ' "'
            + GameText.MapDescriptor(Bladex.GetCurrentMap())
            + '"',
            "VSep": "0.4em",
            "Clave": "0",
            "FocusCallBack": FocusOnBitmap,
            "FontScale": MFontScale["M"],
            "Command": RestartLevel,
        }
    )
    #
    save_count = 0
    for slot_num in range(1, 13):
        need_revive = 0
        restartable = 0
        map_dir = ""
        mod_dir = ""
        exec_str = []
        screenshot = EMPTY_IMAGE
        slot_name = EMPTY_SLOT
        #
        dir_name = "SaveGame%d_files" % (slot_num,)
        filename = "SaveGame%d.py" % (slot_num,)
        save_dir = os.path.join(save_root, dir_name)
        save_file = os.path.join(save_dir, filename)
        aux_file = os.path.join(save_dir, "auxaux")

        if os.path.isfile(aux_file):
            file_data_aux = open(aux_file, "rt")
            lines = file_data_aux.readlines()
            file_data_aux.close()
            if string.find(lines[0], "LUMEN FLAG") != -1:
                map_dir = string.strip(lines[2])
                mod_dir = string.strip(lines[3])
            else:
                map_dir = string.strip(lines[0])
            #
            if not os.path.isfile(save_file) and mod == "":
                # compatible saves
                need_revive = 1
                save_file = os.path.join(save_root, filename)  # classic save
                if not os.path.isfile(save_file):
                    save_file = os.path.join(save_dir, "SaveGame.py")  # major save
            #
            if os.path.isfile(save_file):
                f = open(save_file, "r")
                line = f.readline()
                while line:
                    if string.find(line, "MemPersistence.Store") != -1:
                        exec_str.append(line[:-1])
                        if len(exec_str) == 2:
                            break
                    line = f.readline()
                f.close()
                #
                if mod_dir:
                    map_path = os.path.join(
                        Lumenx.GetLumenRoot(), "Mods", mod_dir, "Maps", map_dir
                    )
                else:
                    map_path = os.path.join(Lumenx.GetLumenRoot(), "Maps", map_dir)
                if len(exec_str) == 2 and os.path.isdir(map_path):
                    restartable = 1
                #
                if not need_revive:
                    save_count = save_count + 1
                    slot_name = eval(string.strip(lines[1]))
                    screenshot = os.path.join(save_dir, "Screenshot.BMP")
                    if not os.path.isfile(screenshot):
                        screenshot = EMPTY_IMAGE
                elif restartable:
                    save_count = save_count + 1
                    slot_name = "[%s]" % revive_descr
        # ----------------------------------
        clave = str(slot_num)
        SaveBitmaps.append((clave, screenshot, slot_name))
        save_val = {
            "Name": "Slot %s" % clave,
            "Text": slot_name,
            "VSep": "0.2em",
            "FontScale": MFontScale["M"],
            "FocusCallBack": FocusOnBitmap,
            "Clave": clave,
            "iFocus": 2,
            "ListDescr": [
                {
                    "Name": MenuText.GetMenuText("Overwrite a previously saved game?"),
                    "VSep": "0.208%",
                    "Font": Language.FontTitle,
                    "Focusable": 0,
                },
                {
                    "Name": MenuText.GetMenuText("Yes"),
                    "VSep": "2em",
                    "Command": SaveGameToDisk,
                    "FontScale": MFontScale["M"],
                    "Clave": clave,
                },
                {
                    "Name": MenuText.GetMenuText("No"),
                    "VSep": "0.5em",
                    "FontScale": MFontScale["M"],
                    "Command": GetBack,
                },
                {"Name": "Back", "Kind": MenuWidget.B_BackBlank},
            ],
        }
        load_val = BCopy.deepcopy(save_val)
        load_val["iFocus"] = 3
        load_val["ListDescr"][0]["Name"] = MenuText.GetMenuText("ARE YOU SURE?")
        load_val["ListDescr"][1]["Command"] = LoadGameFromDisk
        load_val["ListDescr"][1]["VSep"] = "0.5em"
        load_val["ListDescr"].insert(
            1,
            {
                "Name": MenuText.GetMenuText("Restart"),
                "VSep": "2em",
                "Command": ReviveSave,
                "Clave": clave,
                "FontScale": MFontScale["M"],
                "ReviveExecStr": exec_str,
                "ReviveMapDir": map_dir,
                "ReviveModDir": mod_dir,
            },
        )

        # ----------------------------------
        if slot_num == 1:
            save_val["VSep"] = "0.8em"
            load_val["VSep"] = "0.8em"
        if slot_name == EMPTY_SLOT:
            del save_val["ListDescr"]
            save_val["Command"] = SaveGameToDisk
            #
            load_val["Focusable"] = 0
        elif need_revive:
            load_val["ListDescr"][2]["Focusable"] = 0
        if not restartable:
            load_val["ListDescr"][1]["Focusable"] = 0
        #
        SaveListDescr.append(save_val)
        LoadListDescr.append(load_val)

    # ----------------------------------
    label = {
        "Name": "Current Selection",
        "Text": MenuText.GetMenuText("Current Selection"),
        "FontScale": Language.MFontScale["M"],
        "VSep": Menu.NoteOptionVSep,
        "Focusable": 0,
    }
    SaveListDescr.append(label)
    SaveListDescr.append(Menu.BackOption)
    SaveListDescr.append({"Name": "Back", "Kind": MenuWidget.B_BackBlank})
    LoadListDescr.append(label.copy())
    LoadListDescr.append(Menu.BackOption)
    LoadListDescr.append({"Name": "Back", "Kind": MenuWidget.B_BackBlank})

    if Bladex.GetEntity("Player1").Life <= 0:
        SaveMenu.Focusable = 0
    else:
        SaveMenu.MenuDescr["ListDescr"] = SaveListDescr
    if save_count == 0:
        LoadMenu.Focusable = 0
    else:
        LoadMenu.MenuDescr["ListDescr"] = LoadListDescr
    #
    if Lumenx.GetCurrentMap() == "Casa" or Lumenx.GetCurrentMod() != mod_dir:
        SaveMenu.Focusable = 0
        LoadListDescr[2]["Focusable"] = 0  # restart option
    #
    Reference.debugprint("Find %d saved games." % save_count)


# ----------------------------------
# by Sryml: end
# ----------------------------------


def CreateSaveMenu():
    import Menu
    import GameText

    index = InspectSaveList()

    if AllEmpty and not GameText.MapList.has_key(string.upper(Bladex.GetCurrentMap())):
        try:
            Menu.GetMenuItem(["GAME", "LOAD GAME"])[
                "Kind"
            ] = MenuWidget.B_MenuItemTextNoFXNoFocus
        except:
            pass
        try:
            del Menu.GetMenuItem(["GAME", "LOAD GAME"])["ListDescr"]
        except:
            pass
    else:
        try:
            CreateMenu("LOAD GAME", 0)
        except:
            pass
        try:
            del Menu.GetMenuItem(["GAME", "LOAD GAME"])["Kind"]
        except:
            pass

    if (Bladex.GetEntity("Player1").Life <= 0) or not GameText.MapList.has_key(
        string.upper(Bladex.GetCurrentMap())
    ):
        try:
            Menu.GetMenuItem(["GAME", "SAVE GAME"])[
                "Kind"
            ] = MenuWidget.B_MenuItemTextNoFXNoFocus
        except:
            pass
    else:
        try:
            del Menu.GetMenuItem(["GAME", "SAVE GAME"])["Kind"]
        except:
            pass
        try:
            CreateMenu("SAVE GAME", 1)
        except:
            pass

        try:
            Menu.GetMenuItem(["GAME"])["iFocus"] = 1
        except:
            pass

    try:
        if GameText.MapList.has_key(string.upper(Bladex.GetCurrentMap())):
            Menu.GetMenuItem(["GAME", "LOAD GAME"])["iFocus"] = index[0] + 1
        else:
            Menu.GetMenuItem(["GAME", "LOAD GAME"])["iFocus"] = index[0]
    except:
        pass

    try:
        Menu.GetMenuItem(["GAME", "SAVE GAME"])["iFocus"] = index[1]
    except:
        pass


def InspectSaveList():
    global SaveBitmaps
    global AllEmpty
    global FirstSaved
    global SAVEGAMEIMAGE
    global LOADGAMEIMAGE

    FirstSaved = None
    AllEmpty = 1

    lasttime = 0
    indexsel = 1

    firstime = 10000000000000.0
    indexselfirst = 2

    FirstEmptySlot = -1

    SaveBitmaps = []
    path = "../../Save/"

    try:
        os.mkdir(path)
    except:
        pass

    ListDir = []
    for filename in os.listdir(path):
        ListDir.append(string.upper(filename))

    for i in range(6):
        cad = repr(i + 1) + ".BMP"
        if cad in ListDir:
            file = open(path + repr(i + 1) + ".sv", "r")
            name = file.readline()

            file.close()

            # try:
            #     printx(name)
            # except:
            #     SaveBitmaps.append((repr(i + 1), "../../Data/Empty.BMP", EMPTY_SLOT))
            #     if FirstEmptySlot == -1:
            #         FirstEmptySlot = i + 2
            #     continue

            SaveBitmaps.append((repr(i + 1), path + cad, name))
            AllEmpty = 0
            if not FirstSaved:
                FirstSaved = repr(i + 1)
            filetime = os.stat(path + cad)[stat.ST_MTIME]
            if lasttime < filetime:
                lasttime = filetime
                indexsel = i + 2
            if firstime > filetime:
                firstime = filetime
                indexselfirst = i + 2
        else:
            SaveBitmaps.append((repr(i + 1), "../../Data/Empty.BMP", EMPTY_SLOT))
            if FirstEmptySlot == -1:
                FirstEmptySlot = i + 2

    SaveBitmaps.append(("0", "../../Data/Empty.BMP", EMPTY_SLOT))
    if FirstEmptySlot == -1:
        FirstEmptySlot = indexselfirst
        SAVEGAMEIMAGE = repr(indexselfirst - 1)
    else:
        SAVEGAMEIMAGE = "0"

    LOADGAMEIMAGE = repr(indexsel - 1)

    return indexsel, FirstEmptySlot


def RestartLevel(menu_class):
    Bladex.LoadLevel(Bladex.GetCurrentMap())


def MenuStart(EntityName):
    import AuxFuncs

    Bladex.GetEntity(EntityName).Freeze()
    printx(EntityName, "is  death")
    if AuxFuncs.FadeActive:
        ActivaMenuDeRegreso()
    else:
        AuxFuncs.FadeTo(1.0, 1.0)
        Bladex.AddScheduledFunc(Bladex.GetTime() + 1.0, ActivaMenuDeRegreso, ())


def ActivaMenuDeRegreso():
    import Menu

    if Bladex.GetEntity("Player1").Life <= 0:
        Menu.GetMenuItem(["BACK TO GAME"])[
            "Kind"
        ] = (
            MenuWidget.B_MenuItemTextNoFXNoFocus
        )  # :TODO: crash with TypeError : expected integer index
        Menu.EscapeFunction = ElUsuarioPresionaLaTeclaEscape

    Menu.Desc1["iFocus"] = 0
    Menu.GetMenuItem(["GAME"])["iFocus"] = 2

    Menu.ActivateMenu()
    Menu._MainMenu.ActivateMenuItem()
    Menu._MainMenu.ActivateMenuItem()


def CreateMenu(MenuName, SaveFlag):
    import Menu
    import MenuText
    import GameText

    global EmptyImage

    menuItem = Menu.GetMenuItem(["GAME", MenuName])

    if menuItem == 1:
        return

    Save_Menu = []

    EmptyImage = (not SaveFlag) and GameText.MapList.has_key(
        string.upper(Bladex.GetCurrentMap())
    )

    Save_Menu.append(
        {
            "Name": MenuText.GetMenuText(MenuName),
            "VSep": 30,
            "Font": Menu.MenuFontBig,
            "Kind": MenuWidget.B_MenuItemTextNoFXNoFocus,
        }
    )

    if SaveFlag:
        Save_Menu.append(
            {
                "Name": "GameList",
                "Kind": netwidgets.B_ImageListWidget,
                "ImageList": SaveBitmaps,
                "MaxHeight": 90,
                "GetCharType": GetSaveGameImage,
                "VSep": 10,
            }
        )
    else:
        Save_Menu.append(
            {
                "Name": "GameList",
                "Kind": netwidgets.B_ImageListWidget,
                "ImageList": SaveBitmaps,
                "MaxHeight": 90,
                "GetCharType": GetLoadGameImage,
                "VSep": 10,
            }
        )

    if EmptyImage:
        Save_Menu.append(
            {
                "Name": MenuText.GetMenuText("Restart")
                + ' "'
                + GameText.MapDescriptor(Bladex.GetCurrentMap())
                + '"',
                "VSep": -10,
                "Clave": "0",
                "FocusCallBack": FocusOnBitmap,
                # "Font"           : Menu.MenuFontMed,
                "Kind": MenuWidget.B_MenuItemTextNoFX,
                "FontScale": MFontScale["M"],
                "Command": RestartLevel,
            }
        )

    ####################################
    for i in range(6):
        SaveGameName = SaveBitmaps[i][2]
        if SaveFlag:
            val = {
                "Name": SaveGameName,
                "VSep": 10,
                # "Font"           : Menu.MenuFontMed,
                "FontScale": MFontScale["M"],
                "FocusCallBack": FocusOnBitmap,
                "Clave": repr(i + 1),
                "iFocus": 2,
                "ListDescr": [
                    {
                        "Name": MenuText.GetMenuText(
                            "Overwrite a previously saved game?"
                        ),
                        "VSep": 200,
                        "Font": Menu.MenuFontBig,
                        "Kind": MenuWidget.B_MenuItemTextNoFXNoFocus,
                    },
                    {
                        "Name": MenuText.GetMenuText("Yes"),
                        "VSep": 20,
                        "Command": SaveGameToDisk,
                        #  "Font"    : Menu.MenuFontMed,
                        "FontScale": MFontScale["M"],
                        "Clave": repr(i + 1),
                    },
                    {
                        "Name": MenuText.GetMenuText("No"),
                        "VSep": 10,
                        #  "Font":Menu.MenuFontMed,
                        "FontScale": MFontScale["M"],
                        "Command": GetBack,
                    },
                    {"Name": "Back", "Kind": MenuWidget.B_BackBlank},
                ],
            }
            if i == 0:
                val["VSep"] = 10
            if SaveGameName == EMPTY_SLOT:
                del val["ListDescr"]
                val["Command"] = SaveGameToDisk
            Save_Menu.append(val)
        else:
            val = {
                "Name": SaveGameName,
                "VSep": 10,
                # "Font"           : Menu.MenuFontMed,
                "FontScale": MFontScale["M"],
                "FocusCallBack": FocusOnBitmap,
                "Clave": repr(i + 1),
                "iFocus": 2,
                "ListDescr": [
                    {
                        "Name": MenuText.GetMenuText("ARE YOU SURE?"),
                        "VSep": 200,
                        "Font": Menu.MenuFontBig,
                        "Kind": MenuWidget.B_MenuItemTextNoFXNoFocus,
                    },
                    {
                        "Name": MenuText.GetMenuText("Yes"),
                        "VSep": 20,
                        "Command": LoadGameFromDisk,
                        #  "Font"    : Menu.MenuFontMed,
                        "FontScale": MFontScale["M"],
                        "Clave": repr(i + 1),
                    },
                    {
                        "Name": MenuText.GetMenuText("No"),
                        "VSep": 10,
                        #  "Font":Menu.MenuFontMed,
                        "FontScale": MFontScale["M"],
                        "Command": GetBack,
                    },
                    {"Name": "Back", "Kind": MenuWidget.B_BackBlank},
                ],
            }
            if i == 0 and not EmptyImage:
                val["VSep"] = 10

            if SaveGameName == EMPTY_SLOT:
                val["Kind"] = MenuWidget.B_MenuItemTextNoFXNoFocus
            Save_Menu.append(val)

    ####################################

    Save_Menu.append(Menu.BackOption)
    Save_Menu.append({"Name": "Back", "Kind": MenuWidget.B_BackBlank})

    menuItem["ListDescr"] = Save_Menu
