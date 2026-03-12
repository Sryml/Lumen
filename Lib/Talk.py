###########################################################################
# Talk System v 0.8  - by Masklin Jun-2003
###########################################################################
# 06.2024 Updated by Sryml

import Bladex
import Lumenx
import ScorerWidgets
import BUIx
import Raster
import Language
import BInput
import GameText
import B3DLib
import ObjStore

# import Menu
# import KeybWidget  # Must be after import Menu
import MenuText

import os
import string
import re
import whrandom
import typing

from LumenLib import UtilsWidget

printx = Lumenx.printx

if typing.TYPE_CHECKING:
    apply = lambda fn, args=(), kwds={}: None
    execfile = lambda filename, globals=None, locals=None: None

###########################################################################
# Global configuration
###########################################################################

# Enable this flag for extra debug messages:
Debug = 0

# Allow customization
if os.path.exists("../../Data/TSCustom.py"):
    execfile("../../Data/TSCustom.py")
    if Debug:
        printx("TS-DBG: Customized script loaded")

######### modified by sryml >>> start
CLASSIC_VER = Lumenx.CLASSIC_VER
MAJOR_VER = Lumenx.MAJOR_VER
GameVersion = Lumenx.GetGameVersion()
FontScale = Language.FontScale.copy()

CurrentResolution = ()

if GameVersion == CLASSIC_VER:
    vw, vh = Raster.GetSize()
    s = int(100 * (2.5 * (vh / 1440.0)))
    TSFontScale = FontScale["M"]
    TSFontScale_ = int(s * TSFontScale) / 100.0
else:
    TSFontScale = FontScale["M"]
    TSFontScale_ = TSFontScale

# configuration
if globals().get("TSCustomVers") != "1.0":
    TSmmp = "../../Data/TSWidgets.mmp"
    TSFont = Language.FontCommon

AnimSpeed = 6.0
AnimFPS = 60

TSTalkRange = 5000
TSHideDelay = 10.0
SelectNPCArea = 10000

MaxLines = "auto"  # type: int # type: ignore
TextVsep = "0em"  # Vertical Separation
TextMargin = {"top": 0.07, "right": 0.078, "bottom": 0.074, "left": 0.078}
ColorDlg = 255, 255, 255
ColorAns = 207, 144, 49
ColorAnsSelected = 252, 247, 167
HUDBrightness = 1.0

jMaxLines = "auto"  # type: int # type: ignore
jTextVsep = "0em"  # Vertical Separation
jTextMargin = {
    "top": 0.016,  # 0.076,
    "right": 0.107,
    "bottom": 0.075,
    "left": 0.107,
}  # "bottom": 0.084,
ColorjTitle = 255, 204, 51  # 201,62,39
ColorjText = 252, 247, 167
ColorjTextSelected = 255, 204, 51
jHUDBrightness = 0.628
#

font_behaviour = ScorerWidgets.font_server.CreateBFont(TSFont)

######### modified by sryml >>> end


SeeEvent = 1
NoWarning = 1


# rh, rv = Raster.GetSize()


if Language.Current == "Spanish":
    JournalTitle = "D I A R I O"
    # KBTalkLabel = "Hablar"
    # KBJournalLabel = "Diario"
else:
    JournalTitle = "J O U R N A L"
    # KBTalkLabel = "Talk"
    # KBJournalLabel = "Journal"


###########################################################################
# Utilities
###########################################################################
AnimFPS_T = 1.0 / AnimFPS


#########


def DynamicLayout():
    global CurrentResolution
    if GameVersion == CLASSIC_VER or CurrentResolution == Bladex.GetResolution():
        return

    CurrentResolution = Bladex.GetResolution()
    TSWidgets.Reset()
    TSWidgets.InitWidgets()


#########


def findall(pattern, source):
    pos = 0
    end = len(source)
    results = []
    p = re.compile(pattern)
    while pos <= end:
        regs = p.search(source, pos, end)
        if not regs:
            break
        results.append(regs.group())
        pos = max(regs.start() + 1, pos + 1)
    return results


import stat


def copyfile(src, dst):
    """Copy data from src to dst"""
    fsrc = None
    fdst = None
    try:
        fsrc = open(src, "rb")
        fdst = open(dst, "wb")
        while 1:
            buf = fsrc.read(16 * 1024)
            if not buf:
                break
            fdst.write(buf)
    finally:
        if fdst:
            fdst.close()
        if fsrc:
            fsrc.close()


def copystat(src, dst):
    """Copy all stat info (mode bits, atime and mtime) from src to dst"""
    st = os.stat(src)
    mode = stat.S_IMODE(st[stat.ST_MODE])
    os.utime(dst, (st[stat.ST_ATIME], st[stat.ST_MTIME]))
    os.chmod(dst, mode)


def copy2(src, dst):
    """Copy data and all stat info ("cp -p src dst").

    The destination may be a directory.

    """
    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
    copyfile(src, dst)
    copystat(src, dst)


def SelectNPC():
    import Enm_Def

    pj = Bladex.GetEntity("Player1")
    pjp = pj.Position
    enemyList = []
    for ename in Bladex.GetEntitiesAt(pjp[0], pjp[1], pjp[2], SelectNPCArea):
        ene = Bladex.GetEntity(ename)
        if ene.Person and ene.Life > 0 and pj.CanISee(ene) and ene.Name != "Player1":
            enemyList.append(ene.Name)
    if len(enemyList) == 0:
        return None
    enemyList.sort(Enm_Def.ChooseNearest)  # type: ignore
    return enemyList[0]


###########################################################################
# Keyboard
###########################################################################


# KEY_TALK = "T"
# KEY_JOURNAL = "J"


InputManager = BInput.GetInputManager()
CurrentIAS = InputManager.GetInputActionsSet()
# InputManager.SetInputActionsSet("Default")


def StartConversation():
    # modified by sryml
    if not ClsTSWidgets.inited:
        return

    DynamicLayout()
    pj = Bladex.GetEntity("Player1")
    personName = None
    if pj.Data.selected_enemy:
        personName = pj.Data.selected_enemy[0]
    else:
        personName = SelectNPC()
    if personName != None:
        if Debug:
            printx("TS-DBG: Start conversation with ", personName)
        tk = Bladex.GetEntity(personName)
        try:
            dlgId = tk.Data.dlgId
        except:
            dlgId = None
        if dlgId != None:
            TS.Say(tk.Name)
            TSWidgets.Enable()
        else:
            GameText.WriteTextAux(TSDB.IgnoreMe(), 4.0, 255, 255, 255, [])
    else:
        GameText.WriteTextAux(TSDB.ImAlone(), 4.0, 255, 255, 255, [])


def EnableJournal():
    # modified by sryml
    if not ClsTSWidgets.inited or (not TSDB.JrlTxt):
        return

    DynamicLayout()
    TSWidgets.jEnable()


InputManager.AddInputActionsSet("TalkSystem")
InputManager.SetInputActionsSet("TalkSystem")

Bladex.AddInputAction("TSRetrocede", 0)
Bladex.AddInputAction("TSAvanza", 0)
Bladex.AddInputAction("TSNext", 0)
# Bladex.AddInputAction("TSCancelar",0)
Bladex.AddInputAction("TSSelecciona", 0)


Bladex.AssocKey("TSRetrocede", "Mouse", "WheelUp")
Bladex.AssocKey("TSRetrocede", "Keyboard", "PgUp")
Bladex.AssocKey("TSAvanza", "Mouse", "WheelDown")
Bladex.AssocKey("TSAvanza", "Keyboard", "PgDown")
Bladex.AssocKey("TSNext", "Keyboard", "Tab")
Bladex.AssocKey("TSNext", "Mouse", "RightButton")
Bladex.AssocKey("TSSelecciona", "Keyboard", "Enter")
Bladex.AssocKey("TSSelecciona", "Mouse", "LeftButton")
# Bladex.AssocKey("TSCancelar","Keyboard","Esc")


def PressKeyUp():
    TSText.MoveUp()


def PressKeyDown():
    TSText.MoveDown()


def PressKeyNext():
    TSText.NextAnswer()


def PressKeyEsc():
    TSWidgets.Disable()


def PressKeyEnter():
    try:
        ansId = TSText.Line[TSText.Answers[TSText.CurrentAns]["LineInf"]]["ansId"]
        TS.AnswerDisable(TS.CurrentPerson, ansId)

        if TSDB.Ans[TS.CurrentPerson][ansId].has_key("DisableAns"):
            for DansId in TSDB.Ans[TS.CurrentPerson][ansId]["DisableAns"]:
                TS.AnswerDisable(TS.CurrentPerson, DansId)

        if TSDB.Ans[TS.CurrentPerson][ansId].has_key("NewDlg"):
            tk = Bladex.GetEntity(TS.CurrentPerson)  # type: ignore
            tk.Data.dlgId = TSDB.Ans[TS.CurrentPerson][ansId]["NewDlg"]

        if TSDB.Ans[TS.CurrentPerson][ansId].has_key("CallBack"):
            callBackFunc = (
                TSDB.Ans[TS.CurrentPerson][ansId]["CallBack"]
                + "('"
                + TS.CurrentPerson
                + "','"
                + ansId
                + "')"
            )
            try:
                if Debug:
                    printx("TS-DBG: Exec CallBack Func: ", callBackFunc)
                Func = TS.CallBackFuncs[TSDB.Ans[TS.CurrentPerson][ansId]["CallBack"]]
                Func(TS.CurrentPerson, ansId)
            except:
                printx("Talk System: Error executing function " + callBackFunc)
                import traceback

                traceback.print_exc()
                pass

        if TSDB.Ans[TS.CurrentPerson][ansId].has_key("Journal"):
            if Debug:
                printx(
                    "TS-DBG: Add Journal Entry: ",
                    TSDB.Ans[TS.CurrentPerson][ansId]["Journal"],
                )
            TSDB.AddToJournal(TSDB.Ans[TS.CurrentPerson][ansId]["Journal"])

        if Debug:
            printx("TS-DBG: Selected ", ansId, "...  Say ", ansId)
        if TSDB.Ans[TS.CurrentPerson][ansId]["NextDlg"]:
            TS.Say(TS.CurrentPerson, TSDB.Ans[TS.CurrentPerson][ansId]["NextDlg"])
        else:
            Bladex.AddScheduledFunc(
                Bladex.GetTime(), TSWidgets.Disable, (), "TS_Disable"
            )

    except:
        TSWidgets.Disable()


Bladex.AddBoundFunc("TSRetrocede", PressKeyUp)
Bladex.AddBoundFunc("TSAvanza", PressKeyDown)
Bladex.AddBoundFunc("TSNext", PressKeyNext)
# Bladex.AddBoundFunc("TSCancelar",PressKeyEsc)
Bladex.AddBoundFunc("TSSelecciona", PressKeyEnter)


InputManager.AddInputActionsSet("TSJournal")
InputManager.SetInputActionsSet("TSJournal")

Bladex.AddInputAction("TSJRetrocede", 0)
Bladex.AddInputAction("TSJAvanza", 0)
Bladex.AddInputAction("TSJPrev", 0)
Bladex.AddInputAction("TSJNext", 0)
Bladex.AddInputAction("TSJCancelar", 0)

Bladex.AddInputAction("TSDisableJournal", 0)

Bladex.AssocKey("TSJRetrocede", "Mouse", "WheelUp")
Bladex.AssocKey("TSJRetrocede", "Keyboard", "PgUp")
Bladex.AssocKey("TSJAvanza", "Mouse", "WheelDown")
Bladex.AssocKey("TSJAvanza", "Keyboard", "PgDown")
Bladex.AssocKey("TSJNext", "Keyboard", "Tab")
Bladex.AssocKey("TSJPrev", "Mouse", "LeftButton")
Bladex.AssocKey("TSJNext", "Mouse", "RightButton")
Bladex.AssocKey("TSJCancelar", "Keyboard", "Esc")

# Bladex.AssocKey("TSDisableJournal", "Keyboard", KEY_JOURNAL)


def jPressKeyUp():
    TSjText.MoveUp()


def jPressKeyDown():
    TSjText.MoveDown()


def jPressKeyPrev():
    TSjText.PrevEntry()


def jPressKeyNext():
    TSjText.NextEntry()


def DisableJournal():
    TSWidgets.jDisable()


Bladex.AddBoundFunc("TSJRetrocede", jPressKeyUp)
Bladex.AddBoundFunc("TSJAvanza", jPressKeyDown)
Bladex.AddBoundFunc("TSJPrev", jPressKeyPrev)
Bladex.AddBoundFunc("TSJNext", jPressKeyNext)
Bladex.AddBoundFunc("TSJCancelar", DisableJournal)
# Bladex.AddBoundFunc("TSJSelecciona", jPressKeyNext) # unused

Bladex.AddBoundFunc("TSDisableJournal", DisableJournal)

InputManager.SetInputActionsSet(CurrentIAS)

###########################################################################
# Sounds
###########################################################################

TSJ = Bladex.CreateSound("../../Sounds/M-DESENFUNDA-PIEDRA.wav", "TSJournal")
TSJ.Volume = 1.0
TSJ.MinDistance = 1000000.0
TSJ.MaxDistance = 2000000

TSJw = Bladex.CreateSound("../../Sounds/mechanism-operated-2.wav", "TSNewEntry")
TSJw.Volume = 1.0
TSJw.MinDistance = 1000000.0
TSJw.MaxDistance = 2000000

###########################################################################
# Custom classes
###########################################################################


class ClsTSDB:
    DataPath = "./TS/"
    Dlg = {}
    Ans = {}
    Var = {}
    Alone = []
    Ignore = []
    JrlTxt = {}
    JrlIds = []

    def __init__(self):
        self.ObjId = ObjStore.GetNewId()  # Para identificarlo al grabar/guardar
        ObjStore.ObjectsStore[self.ObjId] = self

    # def persistent_id(self):
    #     return self.ObjId

    def __getstate__(self):
        # modified by sryml
        return (
            2,
            # self.ObjId,
            self.Var,
            self.JrlIds,
            # GameStateAux.SaveNewMembers(self),
            # GameStateAux.SaveFunctionAux(self.InitGenFunc),
        )

    def __setstate__(self, parm):
        # modified by sryml
        # Restores data to the TSDB, after which it will be garbage collected.
        if parm[0] == 1:
            pass
            # GameStateAux.LoadFunctionAux(parm[13],self,"InitGenFunc")
        elif parm[0] == 2:
            TSDB.Var = parm[1]
            TSDB.JrlIds = parm[2]
            # GameStateAux.LoadNewMembers(self, parm[3])

    def Init(self, module=None):
        if module:
            self.DataPath = "../../" + module + "/TS/"

    def Clear(self):
        self.Dlg = {}
        self.Ans = {}
        TS.CallBackFunc = {}  # type: ignore

    def ClearVars(self):
        self.Var = {}

    def ClearJournal(self):
        self.JrlIds = []
        TSjText.Reset()

    def SetVar(self, name, value):
        self.Var[name] = value

    def GetVar(self, name):
        # modified by sryml
        return MenuText.GetMenuText(self.Var.get(name, name))

    def Load(self, filename):
        if os.path.exists(self.DataPath + Language.Current + "/" + filename + ".py"):
            try:
                execfile(self.DataPath + Language.Current + "/" + filename + ".py")
            except:
                printx(
                    "Talk System: Error loading " + Language.Current + " database: ",
                    filename,
                )
                import traceback

                traceback.print_exc()
                pass
        else:
            try:
                execfile(self.DataPath + "/" + filename + ".py")
            except:
                printx("Talk System: Error loading generic database: ", filename)
                import traceback

                traceback.print_exc()
                pass

    def Assign(self, person, dlgId, event=None):
        tk = Bladex.GetEntity(person)
        if tk:
            try:
                tk.Data.dlgId = dlgId
                if event:
                    if event == SeeEvent:
                        tk.Data.TSoldSeeFunc = tk.SeeFunc
                        tk.SeeFunc = TS.SeeFunc
            except:
                printx("Talk System: Error setting dlgId (" + dlgId + ") for ", person)
                import traceback

                traceback.print_exc()
                pass

    def ImAlone(self):
        try:
            return self.Alone[whrandom.randint(0, len(self.Alone) - 1)]
        except:
            return ""

    def IgnoreMe(self):
        try:
            return self.Ignore[whrandom.randint(0, len(self.Ignore) - 1)]
        except:
            return ""

    def Validate(self):
        printx("Validate TSDB: Current Database")
        for person in TSDB.Dlg.keys():
            printx("Validate TSDB: Processing ", person)
            printx("Validate TSDB:    Dlg Test")
            for dlgId in TSDB.Dlg[person].keys():
                printx("Validate TSDB:         dlgId ", dlgId)
                for ansId in TSDB.Dlg[person][dlgId]["Answers"]:
                    if TSDB.Ans[person].has_key(ansId):
                        printx("Validate TSDB:            ansId ", ansId, " OK")
                    else:
                        printx(
                            "Validate TSDB:            ansId ",
                            ansId,
                            " *** Not Found ***",
                        )

                if TSDB.Dlg[person][dlgId].has_key("NewDlg"):
                    ndlgId = TSDB.Dlg[person][dlgId]["NewDlg"]
                    if TSDB.Dlg[person].has_key(ndlgId) or ndlgId == None:
                        printx("Validate TSDB:            New dlgId ", ndlgId, " OK")
                    else:
                        printx(
                            "Validate TSDB:            New dlgId ", ndlgId, " Not Found"
                        )

            printx("Validate TSDB:    Ans Test")
            for ansId in TSDB.Ans[person].keys():
                if TSDB.Dlg[person].has_key(TSDB.Ans[person][ansId]["NextDlg"]):
                    printx("Validate TSDB:            AnsId ", ansId, " OK")
                else:
                    printx("Validate TSDB:            AnsId ", ansId, " Not Found")
                if TSDB.Ans[person][ansId].has_key("NewDlg"):
                    ndlgId = TSDB.Ans[person][ansId]["NewDlg"]
                    if TSDB.Dlg[person].has_key(ndlgId) or ndlgId == None:
                        printx("Validate TSDB:            New dlgId ", ndlgId, " OK")
                    else:
                        printx(
                            "Validate TSDB:            New dlgId ", ndlgId, " Not Found"
                        )

    def AddToJournal(self, jrlId, no_warning=0):
        Text = self.JrlTxt.get(jrlId)  # type: ignore
        if not Text:
            if Debug:
                printx("TS-DBG: AddToJournal : jrlId =", jrlId, " Not Found")
            return

        if Debug:
            printx("TS-DBG: AddToJournal : jrlId =", jrlId, " Text = ", Text)

        self.JrlIds.append(jrlId)
        if no_warning == 0:
            TSWidgets.SlidejNE(0)

    def RemoveFromJournal(self, jrlId):
        if Debug:
            printx("TS-DBG: RemoveFromJournal : jrlId =", jrlId)
        if jrlId in self.JrlIds:
            self.JrlIds.remove(jrlId)
            if Debug:
                printx("TS-DBG: RemoveFromJournal : Text =", self.JrlTxt[jrlId])


class ClsTS:
    CurrentPerson = None
    CallBackFuncs = {}

    def __init__(self):
        pass

    def Parse(self, text):
        for var in findall("%\w+", text):  # type: ignore
            text = string.replace(text, var, str(TSDB.GetVar(var[1:])))  # type: ignore
        return text

    def AnswerDisable(self, person, ansId):
        TSDB.Ans[person][ansId]["Enabled"] = 0

    def AnswerEnable(self, person, ansId):
        TSDB.Ans[person][ansId]["Enabled"] = 1

    def Say(self, person, dlgId=None):
        TSText.Reset()
        self.CurrentPerson = person
        tk = Bladex.GetEntity(person)
        if dlgId == None:
            dlgId = tk.Data.dlgId
        if dlgId == None:
            return
        CurrentDlg = TSDB.Dlg[person][dlgId]
        if Debug:
            printx("TS-DBG: Say ", person, " - ", dlgId)
        TSText.AddText(self.Parse("%" + person + ": " + CurrentDlg["Text"]))
        if CurrentDlg.has_key("ExtraDlg"):
            TSText.AddText(
                self.Parse(CurrentDlg["ExtraDlg"][0] + ": " + CurrentDlg["ExtraDlg"][1])
            )

        nAnswers = 0
        if len(CurrentDlg["Answers"]):
            for ansId in CurrentDlg["Answers"]:
                validAnsId = None
                if TSDB.Ans[person][ansId]["Enabled"]:
                    validAnsId = ansId
                elif CurrentDlg.has_key("ReplaceAns"):
                    if CurrentDlg["ReplaceAns"].has_key(ansId):
                        for nextAnsId in CurrentDlg["ReplaceAns"][ansId]:
                            if TSDB.Ans[person][nextAnsId]["Enabled"]:
                                validAnsId = nextAnsId
                                break
                if validAnsId:
                    TSText.AddText(
                        self.Parse(TSDB.Ans[person][validAnsId]["Text"]), validAnsId
                    )
                    nAnswers = nAnswers + 1
        if nAnswers == 0:
            if CurrentDlg.has_key("HideDelay"):
                hideDelay = CurrentDlg["HideDelay"]
            else:
                hideDelay = TSHideDelay
            Bladex.AddScheduledFunc(
                Bladex.GetTime() + hideDelay, TSWidgets.Disable, (), "TS_Disable"
            )
        else:
            TSText.TargetLInf = TSText.Answers[TSText.CurrentAns]["LineInf"]
            TSText.TargetLSup = TSText.Answers[TSText.CurrentAns]["LineSup"]
        if CurrentDlg.has_key("NewDlg"):
            tk.Data.dlgId = CurrentDlg["NewDlg"]
        TSText.ShowText()

        if CurrentDlg.has_key("CallBack"):
            callBackFunc = (
                CurrentDlg["CallBack"]
                + "('"
                + self.CurrentPerson
                + "','"
                + dlgId
                + "')"
            )
            try:
                if Debug:
                    printx("TS-DBG: Exec CallBack Func: ", callBackFunc)
                Func = self.CallBackFuncs[CurrentDlg["CallBack"]]
                Func(self.CurrentPerson, dlgId)
            except:
                printx("Talk System: Error executing function " + callBackFunc)
                import traceback

                traceback.print_exc()
                pass

        if CurrentDlg.has_key("Journal"):
            if Debug:
                printx("TS-DBG: Add Journal Entry: ", CurrentDlg["Journal"])
            TSDB.AddToJournal(CurrentDlg["Journal"])

    def SetAnswer(self, person, ansId, text, nextdlgId=None):
        TSDB.Ans[person][ansId]["Text"] = text
        if nextdlgId:
            TSDB.Ans[person][ansId]["NextDlg"] = nextdlgId
        TSDB.Ans[person][ansId]["Enabled"] = 1

    def SetDialog(self, person, dlgId, text, answers=None):
        TSDB.Dlg[person][dlgId]["Text"] = text
        if answers:
            TSDB.Dlg[person][dlgId]["Answers"] = answers

    def SeeFunc(self, EntityName):
        import Actions

        tk = Bladex.GetEntity(EntityName)
        if tk.Life < 0:
            return
        if B3DLib.GetXZDistance(EntityName, "Player1") < TSTalkRange:
            if tk.Data.TSoldSeeFunc or tk.Data.TSoldSeeFunc == None:
                tk.SeeFunc = tk.Data.TSoldSeeFunc
            Actions.TurnToFaceEntityNow("Player1", tk.Name)
            if tk.Data.dlgId and tk.Data.dlgId != None:
                TS.Say(tk.Name)
                TSWidgets.Enable()

    def AddCallBackFunc(self, FuncName, Func):
        self.CallBackFuncs[FuncName] = Func

    def ShowMessage(self, Text, HideDelay):
        TSText.Reset()
        if Debug:
            printx("TS-DBG: ShowMessage : Text = ", Text, "\nDelay = ", HideDelay)
        TSText.AddText(self.Parse(Text))
        TSText.ShowText()
        Bladex.AddScheduledFunc(Bladex.GetTime() + HideDelay, TSWidgets.Disable, ())


class ClsTSText:
    Line = {}
    NLines = 0
    LineInf = 1
    LineSup = 1
    Answers = {}
    NAns = 0
    CurrentAns = 1
    TargetLInf = 0
    TargetLSup = 0

    def __init__(self):
        self.MaxLines = MaxLines

    def Reset(self):
        self.Line = {}
        self.NLines = 0
        self.LineInf = 1
        self.LineSup = 1
        self.Answers = {}
        self.NAns = 0
        self.CurrentAns = 1
        self.TargetLInf = 0
        self.TargetLSup = 0

    def AddText(self, Text, ansId=None):
        # modified by sryml
        w = TSWidgets.DialogFrame.GetSize()[0]
        MaxWidth = int(w * (1 - TextMargin["left"] - TextMargin["right"]))
        Lines = UtilsWidget.WrapText(
            Text,
            MaxWidth,
            TSFontScale_,
            font_behaviour,
        )

        initNLines = self.NLines + 1
        for line in Lines:
            self.NLines = self.NLines + 1
            self.Line[self.NLines] = {"Text": line + "\n", "ansId": ansId}
            if Debug:
                printx("TS-DBG: AddText (", ansId, ") - ", line)
        if ansId:
            self.NAns = self.NAns + 1
            self.Answers[self.NAns] = {"LineInf": initNLines, "LineSup": self.NLines}
        else:
            self.NLines = self.NLines + 1
            self.Line[self.NLines] = {"Text": "\n", "ansId": ansId}
        self.LineInf = 1
        self.LineSup = min(self.MaxLines, self.NLines)

    def ShowText(self):
        for i in range(1, self.MaxLines + 1):
            currentLine = self.LineInf + i - 1
            if Debug:
                printx("TS-DBG: ShowText - Line: ", currentLine)
            try:
                ansId = self.Line[currentLine]["ansId"]
                if not ansId:
                    selectedMark = ""
                    TSWidgets.TextWidget[i].SetColor(
                        ColorDlg[0], ColorDlg[1], ColorDlg[2]
                    )
                elif currentLine >= self.TargetLInf and currentLine <= self.TargetLSup:
                    selectedMark = "> "
                    TSWidgets.TextWidget[i].SetColor(
                        ColorAnsSelected[0], ColorAnsSelected[1], ColorAnsSelected[2]
                    )
                else:
                    selectedMark = "  "
                    TSWidgets.TextWidget[i].SetColor(
                        ColorAns[0], ColorAns[1], ColorAns[2]
                    )
                Text = selectedMark + self.Line[currentLine]["Text"]
                if Debug:
                    printx("TS-DBG: ShowText - Text: ", Text)
                TSWidgets.TextWidget[i].SetText(Text)
            except:
                TSWidgets.TextWidget[i].SetText("")
        if currentLine < self.NLines:
            Text = string.replace(Text, "\n", "  >>>\n")  # type: ignore
            TSWidgets.TextWidget[i].SetText(Text)

    def MoveUp(self):
        self.LineInf = self.LineInf - 1
        if self.LineInf < 1:
            self.LineInf = 1
        self.LineSup = self.LineInf + self.MaxLines - 1
        self.ShowText()

    def MoveDown(self):
        self.LineInf = self.LineInf + 1
        if self.LineInf > self.NLines - self.MaxLines + 1:
            self.LineInf = self.LineInf - 1
        self.LineSup = self.LineInf + self.MaxLines - 1
        self.ShowText()

    def NextAnswer(self):
        if self.NAns == 0:
            return
        self.CurrentAns = self.CurrentAns + 1
        if self.CurrentAns > self.NAns:
            self.CurrentAns = 1
        self.TargetLInf = self.Answers[self.CurrentAns]["LineInf"]
        self.TargetLSup = self.Answers[self.CurrentAns]["LineSup"]

        if self.TargetLSup > self.LineSup:
            self.LineSup = self.TargetLSup
            self.LineInf = self.LineSup - self.MaxLines + 1
        elif self.TargetLInf < self.LineInf:
            self.LineInf = self.TargetLInf
            self.LineSup = self.LineInf + self.MaxLines
        self.ShowText()


class ClsTSjText:
    Line = {}
    NLines = 0
    LineInf = 1
    LineSup = 1
    JrlData = {}
    NJrl = 0
    TargetLInf = 0
    TargetLSup = 0

    def __init__(self):
        self.MaxLines = jMaxLines
        self.CurrentJrl = 0

    def Reset(self):
        self.Line = {}
        self.NLines = 0
        self.LineInf = 1
        self.LineSup = 1
        self.JrlData = {}
        self.NJrl = 0
        self.TargetLInf = 0
        self.TargetLSup = 0

    def AddText(self, Text, jrlN):
        # modified by sryml
        w = TSWidgets.JournalFrame.GetSize()[0]
        MaxWidth = int(w * (1 - jTextMargin["left"] - jTextMargin["right"]))
        Lines = UtilsWidget.WrapText(
            Text,
            MaxWidth,
            TSFontScale_,
            font_behaviour,
        )

        initNLines = self.NLines + 1
        for line in Lines:
            self.NLines = self.NLines + 1
            self.Line[self.NLines] = {"Text": line + "\n", "jrlN": jrlN}
            if Debug:
                printx("TS-DBG: AddText (", jrlN, ") - ", line)
        self.NLines = self.NLines + 1
        self.Line[self.NLines] = {"Text": "\n", "jrlN": jrlN}
        self.NJrl = self.NJrl + 1
        self.JrlData[self.NJrl] = {"LineInf": initNLines, "LineSup": self.NLines}
        self.LineInf = 1
        self.LineSup = min(self.MaxLines, self.NLines)

    def ShowText(self):
        if self.MaxLines < 1:
            return

        for i in range(1, self.MaxLines + 1):
            currentLine = self.LineInf + i - 1
            if Debug:
                printx("TS-DBG: ShowText - Line: ", currentLine)
            try:
                jrlN = self.Line[currentLine]["jrlN"]
                if currentLine >= self.TargetLInf and currentLine <= self.TargetLSup:
                    TSWidgets.jTextWidget[i].SetColor(
                        ColorjTextSelected[0],
                        ColorjTextSelected[1],
                        ColorjTextSelected[2],
                    )
                else:
                    TSWidgets.jTextWidget[i].SetColor(
                        ColorjText[0], ColorjText[1], ColorjText[2]
                    )
                Text = self.Line[currentLine]["Text"]
                if Debug:
                    printx("TS-DBG: ShowText - Text: ", Text)
                TSWidgets.jTextWidget[i].SetText(Text)
            except:
                TSWidgets.jTextWidget[i].SetText("")
        if currentLine < self.NLines:
            TSWidgets.jMoreWidget.SetVisible(1)  # type: ignore
            TSWidgets.jTextWidget[i].SetText(Text)
        else:
            TSWidgets.jMoreWidget.SetVisible(0)  # type: ignore

    def MoveUp(self):
        self.LineInf = self.LineInf - 1
        if self.LineInf < 1:
            self.LineInf = 1
        self.LineSup = self.LineInf + self.MaxLines - 1
        self.ShowText()

    def MoveDown(self):
        self.LineInf = self.LineInf + 1
        if self.LineInf > self.NLines - self.MaxLines + 1:
            self.LineInf = self.LineInf - 1
        self.LineSup = self.LineInf + self.MaxLines - 1
        self.ShowText()

    def SelectEntry(self, i):
        if self.NJrl == 0:
            return
        self.CurrentJrl = (self.CurrentJrl + i) % self.NJrl
        CurrentJrl = self.CurrentJrl + 1

        self.TargetLInf = self.JrlData[CurrentJrl]["LineInf"]
        self.TargetLSup = self.JrlData[CurrentJrl]["LineSup"]

        if self.TargetLSup > self.LineSup:
            self.LineSup = self.TargetLSup
            self.LineInf = self.LineSup - self.MaxLines + 1
        elif self.TargetLInf < self.LineInf:
            self.LineInf = self.TargetLInf
            self.LineSup = self.LineInf + self.MaxLines - 1
        self.ShowText()

    def PrevEntry(self):
        self.SelectEntry(-1)

    def NextEntry(self):
        self.SelectEntry(1)

    def LoadJournalText(self):
        self.Reset()
        jrlN = 0
        for jrlId in TSDB.JrlIds:
            text = TSDB.JrlTxt[jrlId]
            self.AddText(TS.Parse(text), jrlN)
            jrlN = jrlN + 1
        self.SelectEntry(0)  # Keep selected position
        self.ShowText()


class ClsTSWidgets:
    TextWidget = []
    jTextWidget = []
    LastIAS = "Default"
    jTitleWidget = 0
    jMoreWidget = 0
    BitMapIdx = 0
    inited = 0

    def __init__(self):
        # modified by sryml

        # Since the reissue version will change the size of Scorer.wFrame after loading the game, the scheduled function ensures that the widgets are added based on the final size.
        Bladex.AddScheduledFunc(
            Bladex.GetTime() + 0.2, self.InitWidgets, (), Lumenx.GetNSaveName()
        )

    def Reset(self):
        # added by sryml
        import Scorer

        Scorer.wFrame.RemoveWidget(self.MainFrame.Name())
        self.MainFrame = None
        self.DialogFrame = None
        self.TextWidget = []
        self.DialogIMG = None
        self.JournalFrame = None
        self.jTitleWidget = None
        self.jTextWidget = []
        self.jMoreWidget = None
        self.JournalIMG = None
        self.jNewEntry = None

    def InitWidgets(self):
        # added by sryml
        import Scorer

        global CurrentResolution
        UIScaleFactor = Bladex.GetUIScaleFactor()
        if UIScaleFactor != 0:
            scale = (1.2, 1.316)[UIScaleFactor - 1]
        else:
            scale = 1.0
        vw, vh = Scorer.wFrame.GetSize()
        auto_scale = 1
        if GameVersion != CLASSIC_VER:
            CurrentResolution = Bladex.GetResolution()
            auto_scale = 0

        MainFrame = self.MainFrame = BUIx.B_FrameWidget(
            Scorer.wFrame, "TS_MainFrame", vw, vh
        )
        MainFrame.SetAutoScale(1)
        Scorer.wFrame.AddWidget(MainFrame, 0, 0)

        w, h = UtilsWidget.AdaptResolution(
            (178 / 4.0 / 1.2, 256 / 4.0 / 1.2), (640, 480), keep_h=1
        )
        w, h = w * scale, h * scale
        self.jNewEntry = BUIx.B_BitmapWidget(
            MainFrame, "jNewEntry", w, h, "TSWarning", TSmmp
        )
        self.jNewEntry.SetColor(255, 255, 255)
        self.jNewEntry.SetAlpha(1.0)
        self.jNewEntry.SetVisible(0)

        # DialogFrame
        dialogframe_w, dialogframe_h = UtilsWidget.AdaptResolution(
            (1904 / 1.2, 540 / 1.2), (2560, 1440), keep_h=1
        )
        dialogframe_w, dialogframe_h = dialogframe_w * scale, dialogframe_h * scale
        DialogFrame = self.DialogFrame = BUIx.B_FrameWidget(
            MainFrame, "TS_DialogFrame", dialogframe_w, dialogframe_h
        )
        DialogFrame.SetAlpha(1.0)
        DialogFrame.SetAutoScale(auto_scale)
        DialogFrame.SetVisible(0)
        MainFrame.AddWidget(
            DialogFrame,
            0.5,
            0,
            BUIx.B_FrameWidget.B_FR_HRelative,
            BUIx.B_FrameWidget.B_FR_HCenter,
            BUIx.B_FrameWidget.B_FR_AbsoluteBottom,
            BUIx.B_FrameWidget.B_FR_Top,
        )

        text_ref = self.text_ref = BUIx.B_TextWidget(
            DialogFrame,
            "text_tmp",
            "T",
            ScorerWidgets.font_server,
            TSFont,
        )
        text_ref.SetCanvas((vw, vh))
        text_ref.SetScale(TSFontScale)

        h = text_ref.GetSize()[1]
        vsep = (h + h * float(TextVsep[:-2])) / dialogframe_h
        maxlines = int((1 - TextMargin["top"] - TextMargin["bottom"]) / vsep)
        if MaxLines == "auto" or MaxLines > maxlines:
            TSText.MaxLines = maxlines

        self.TextWidget.append(None)
        for i in range(1, TSText.MaxLines + 1):
            textWidget = BUIx.B_TextWidget(
                DialogFrame,
                "TextWidget" + str(i),
                "",
                ScorerWidgets.font_server,
                TSFont,
            )
            textWidget.SetCanvas((vw, vh))
            textWidget.SetScale(TSFontScale)
            textWidget.SetAlpha(1)
            textWidget.SetVisible(0)
            textWidget.SetAutoScale(auto_scale)

            DialogFrame.AddWidget(
                textWidget,
                TextMargin["left"],
                TextMargin["top"] + vsep * (i - 1),
                BUIx.B_FrameWidget.B_FR_HRelative,
                BUIx.B_FrameWidget.B_FR_Left,
                BUIx.B_FrameWidget.B_FR_VRelative,
                BUIx.B_FrameWidget.B_FR_Top,
            )
            self.TextWidget.append(textWidget)

        self.DialogIMG = BUIx.B_BitmapWidget(
            DialogFrame,
            "TS_DialogIMG",
            dialogframe_w,
            dialogframe_h,
            "TSDialogBox",
            TSmmp,
        )
        bri = int(255.0 * HUDBrightness)
        self.DialogIMG.SetColor(bri, bri, bri)
        self.DialogIMG.SetAlpha(1.0)
        self.DialogIMG.SetAutoScale(auto_scale)
        DialogFrame.AddWidget(self.DialogIMG, 0, 0)

        journalframe_w, journalframe_h = UtilsWidget.AdaptResolution(
            (918 * 1.1 / 1.2, 1190 * 1.1 / 1.2), (3840, 2160), keep_h=1
        )
        journalframe_w, journalframe_h = journalframe_w * scale, journalframe_h * scale
        # In the classic version, B_FrameWidget seems unable to display transparent image.
        JournalFrame = self.JournalFrame = BUIx.B_FrameWidget(
            MainFrame, "TS_JournalFrame", journalframe_w, journalframe_h
        )
        JournalFrame.SetAlpha(1.0)
        JournalFrame.SetAutoScale(auto_scale)
        JournalFrame.SetVisible(0)
        # bri = int(255.0 * jHUDBrightness)
        # JournalFrame.SetColor(bri, bri, bri)
        # JournalFrame.SetSolid(1)
        # JournalFrame.SetBitmap("TSJournal")
        MainFrame.AddWidget(
            JournalFrame,
            0,
            0.5,
            BUIx.B_FrameWidget.B_FR_AbsoluteRight,
            BUIx.B_FrameWidget.B_FR_Left,
            BUIx.B_FrameWidget.B_FR_VRelative,
            BUIx.B_FrameWidget.B_FR_VCenter,
        )

        h = text_ref.GetSize()[1]
        vsep = (h + h * float(jTextVsep[:-2])) / journalframe_h
        maxlines = int((1 - jTextMargin["top"] - jTextMargin["bottom"]) / vsep) - 2
        if jMaxLines == "auto" or jMaxLines > maxlines:
            TSjText.MaxLines = maxlines

        self.jTitleWidget = BUIx.B_TextWidget(
            JournalFrame, "jTitleWidget", "", ScorerWidgets.font_server, TSFont
        )
        self.jTitleWidget.SetCanvas((vw, vh))
        self.jTitleWidget.SetScale(TSFontScale * 1.1)
        self.jTitleWidget.SetAlpha(1.0)
        self.jTitleWidget.SetAutoScale(auto_scale)
        self.jTitleWidget.SetText(MenuText.GetMenuText(JournalTitle))
        self.jTitleWidget.SetColor(ColorjTitle[0], ColorjTitle[1], ColorjTitle[2])
        JournalFrame.AddWidget(
            self.jTitleWidget,
            0.5,
            jTextMargin["top"],
            BUIx.B_FrameWidget.B_FR_HRelative,
            BUIx.B_FrameWidget.B_FR_HCenter,
            BUIx.B_FrameWidget.B_FR_VRelative,
            BUIx.B_FrameWidget.B_FR_Top,
        )

        self.jTextWidget.append(None)
        for i in range(1, TSjText.MaxLines + 1):
            textWidget = BUIx.B_TextWidget(JournalFrame, "jTextWidget" + str(i), "", ScorerWidgets.font_server, TSFont)  # type: ignore
            textWidget.SetCanvas((vw, vh))
            textWidget.SetScale(TSFontScale)
            textWidget.SetAlpha(1)
            textWidget.SetVisible(0)
            textWidget.SetAutoScale(auto_scale)
            # textWidget.SetAutoSize(1)
            JournalFrame.AddWidget(
                textWidget,
                jTextMargin["left"],
                jTextMargin["top"] + vsep * (i + 1),
                BUIx.B_FrameWidget.B_FR_HRelative,
                BUIx.B_FrameWidget.B_FR_Left,
                BUIx.B_FrameWidget.B_FR_VRelative,
                BUIx.B_FrameWidget.B_FR_Top,
            )
            self.jTextWidget.append(textWidget)

        self.jMoreWidget = BUIx.B_TextWidget(
            JournalFrame, "jMoreWidget", ">>>", ScorerWidgets.font_server, TSFont
        )
        self.jMoreWidget.SetCanvas((vw, vh))
        self.jMoreWidget.SetScale(TSFontScale)
        self.jMoreWidget.SetAlpha(1.0)
        self.jMoreWidget.SetVisible(0)
        self.jMoreWidget.SetAutoScale(auto_scale)
        self.jMoreWidget.SetColor(ColorjText[0], ColorjText[1], ColorjText[2])
        JournalFrame.AddWidget(
            self.jMoreWidget,
            1 - jTextMargin["right"],
            1 - jTextMargin["bottom"],
            BUIx.B_FrameWidget.B_FR_HRelative,
            BUIx.B_FrameWidget.B_FR_Right,
            BUIx.B_FrameWidget.B_FR_VRelative,
            BUIx.B_FrameWidget.B_FR_Bottom,
        )

        self.JournalIMG = BUIx.B_BitmapWidget(
            JournalFrame,
            "TS_JournalIMG",
            journalframe_w,
            journalframe_h,
            "TSJournal",
            TSmmp,
        )
        bri = int(255.0 * jHUDBrightness)
        self.JournalIMG.SetColor(bri, bri, bri)
        self.JournalIMG.SetAlpha(1.0)
        self.JournalIMG.SetAutoScale(auto_scale)
        JournalFrame.AddWidget(self.JournalIMG, 0, 0)

        MainFrame.AddWidget(
            self.jNewEntry,
            0,
            0.5,
            BUIx.B_FrameWidget.B_FR_AbsoluteRight,
            BUIx.B_FrameWidget.B_FR_Left,
            BUIx.B_FrameWidget.B_FR_VRelative,
            BUIx.B_FrameWidget.B_FR_VCenter,
        )
        #
        ClsTSWidgets.inited = 1
        printx("Talk System Widgets initialized")

    def SlideFrame(self, OnOff, time=AnimFPS_T):
        # modified by sryml
        height = self.DialogFrame.GetSize()[1]

        f = time * AnimSpeed
        if f < 1.0:
            Bladex.AddScheduledFunc(
                Bladex.GetTime() + AnimFPS_T,  # 60 FPS
                self.SlideFrame,
                (OnOff, time + AnimFPS_T),
                "TS_SlideFrame",
            )
        else:
            f = 1.0

        if OnOff:
            y = height - height * f
        else:
            y = height * f

        self.MainFrame.MoveWidgetTo("TS_DialogFrame", 0.5, y)

    def SetBitMap(self, Name, File):
        self.BitMapIdx = self.BitMapIdx + 1
        BitMapName = "SBM_" + Name + "_" + str(self.BitMapIdx)
        Bladex.ReadAlphaBitMap(File, BitMapName)
        if Name == "TSDialogBox":
            self.DialogFrame.SetBitmap(BitMapName)
        elif Name == "TSJournal":
            self.JournalFrame.SetBitmap(BitMapName)
        elif Name == "TSWarning":
            self.jNewEntry.SetBitmap(BitMapName)

    def Enable(self):
        import Scorer
        import Actions

        IManager = BInput.GetInputManager()
        self.LastIAS = IManager.GetInputActionsSet()
        Bladex.RemoveBoundFunc("Attack", "Attack")
        IManager.SetInputActionsSet("TalkSystem")
        Bladex.RemoveBoundFunc("Attack", "Attack")
        Actions.FreeBothHands("Player1")
        Scorer.PowDefWidgets.Deactivate()
        Bladex.RemoveScheduledFunc("TS_Hide")
        Bladex.RemoveScheduledFunc("TS_Disable")
        Bladex.RemoveScheduledFunc("TS_SlideFrame")
        self.DialogFrame.SetVisible(1)
        self.SlideFrame(0)
        Bladex.AddScheduledFunc(
            Bladex.GetTime() + 1 / AnimSpeed, self.Show, (), "TS_Show"
        )

    def Show(self):
        for i in range(1, TSText.MaxLines + 1):
            self.TextWidget[i].SetVisible(1)
        TSText.ShowText()

    def Disable(self):
        for i in range(1, TSText.MaxLines + 1):
            self.TextWidget[i].SetVisible(0)
        Bladex.RemoveScheduledFunc("TS_Show")
        Bladex.RemoveScheduledFunc("TS_SlideFrame")
        self.SlideFrame(1)
        Bladex.AddScheduledFunc(
            Bladex.GetTime() + 1 / AnimSpeed, self.Hide, (), "TS_Hide"
        )
        IManager = BInput.GetInputManager()
        IManager.SetInputActionsSet(self.LastIAS)
        Bladex.AddBoundFunc("Attack", "Attack")

    def Hide(self):
        import Scorer

        self.DialogFrame.SetVisible(0)
        pj = Bladex.GetEntity("Player1")
        pj.SetActiveEnemy(None)  # type: ignore
        Scorer.PowDefWidgets.Activate()

    def jEnable(self):
        # Bladex.RemoveScheduledFunc("TS_Disable")
        Bladex.RemoveScheduledFunc("TS_HideNewEntry")
        Bladex.RemoveScheduledFunc("TS_ShowNewEntry")
        self.jNewEntry.SetVisible(0)

        TSJ.PlayStereo()
        TSjText.LoadJournalText()

        IManager = BInput.GetInputManager()
        device_obj = IManager.GetAttachedDevice("Keyboard")
        self.LastIAS = IManager.GetInputActionsSet()
        Bladex.RemoveBoundFunc("Attack", "Attack")

        IAction = IManager.GetInputActions().Find("TSEnableJournal")
        keys = list(map(lambda x: x[0], IAction.GetAssociatedKeys("Keyboard")))

        IManager.SetInputActionsSet("TSJournal")
        IAction = IManager.GetInputActions().Find("TSDisableJournal")
        keys2 = list(map(lambda x: x[0], IAction.GetAssociatedKeys("Keyboard")))

        keys.sort()
        keys2.sort()
        sync = 1
        if len(keys) != len(keys2):
            sync = 0
        else:
            for i in range(len(keys)):
                if keys[i] != keys2[i]:
                    sync = 0
                    break
        if not sync:
            IAction.RemoveAllDeviceEvents("Keyboard")
            for key in keys:
                if not device_obj.IsBinded(key):
                    Bladex.AssocKey("TSDisableJournal", "Keyboard", key)
        #
        Bladex.RemoveBoundFunc("Attack", "Attack")
        Bladex.RemoveScheduledFunc("TS_ShowJournal")
        self.JournalFrame.SetVisible(1)
        self.ShowJournal(0)
        self.jShow()

    def jShow(self):
        self.jTitleWidget.SetVisible(1)  # type: ignore
        self.jMoreWidget.SetVisible(1)  # type: ignore
        for i in range(1, TSjText.MaxLines + 1):
            self.jTextWidget[i].SetVisible(1)
        TSjText.ShowText()

    def jDisable(self):
        TSJ.PlayStereo()
        self.jTitleWidget.SetVisible(0)  # type: ignore
        self.jMoreWidget.SetVisible(0)  # type: ignore
        for i in range(1, TSjText.MaxLines + 1):
            self.jTextWidget[i].SetVisible(0)
        Bladex.RemoveScheduledFunc("TS_ShowJournal")
        self.ShowJournal(1)
        IManager = BInput.GetInputManager()
        IManager.SetInputActionsSet(self.LastIAS)
        Bladex.AddBoundFunc("Attack", "Attack")

    def ShowJournal(self, OnOff, increment=0):
        # modified by sryml
        width = self.JournalFrame.GetSize()[0]
        if increment == 0:
            total_time = 1 / AnimSpeed
            increment = width / (total_time / AnimFPS_T)

        x = self.MainFrame.GetWidgetPosition("TS_JournalFrame")[1]

        loop = 1
        if OnOff:
            x = x - increment
            if x < 0:
                x = 0
                loop = 0
                self.JournalFrame.SetVisible(0)
        else:
            x = x + increment
            if x > width:
                x = width
                loop = 0

        self.MainFrame.MoveWidgetTo("TS_JournalFrame", x, 0.5)
        if loop:
            Bladex.AddScheduledFunc(
                Bladex.GetTime() + AnimFPS_T,
                self.ShowJournal,
                (OnOff, increment),
                "TS_ShowJournal",
            )

    def SlidejNE(self, dir):
        TSJw.PlayStereo()
        Bladex.RemoveScheduledFunc("TS_HideNewEntry")
        Bladex.RemoveScheduledFunc("TS_ShowNewEntry")
        self.SlidejNE2(dir)
        self.jNewEntry.SetVisible(1)

    def SlidejNE2(self, dir, time=AnimFPS_T):
        # modified by sryml
        width = self.jNewEntry.GetSize()[0]

        f = time * AnimSpeed
        if f < 1.0:
            Bladex.AddScheduledFunc(
                Bladex.GetTime() + AnimFPS_T,  # 60 FPS
                self.SlidejNE2,
                (dir, time + AnimFPS_T),
                "TS_ShowNewEntry",
            )
        else:
            f = 1.0
            Bladex.AddScheduledFunc(
                Bladex.GetTime() + 7, self.HidejNE, (), "TS_HideNewEntry"
            )

        if dir:  # off
            x = width - width * f
        else:
            x = width * f

        self.MainFrame.MoveWidgetTo("jNewEntry", x, 0.5)

    def HidejNE(self):
        Bladex.RemoveScheduledFunc("TS_HideNewEntry")
        Bladex.RemoveScheduledFunc("TS_ShowNewEntry")
        self.jNewEntry.SetVisible(0)  # type: ignore


###########################################################################
# Initialization
###########################################################################
# try:
#     # Hay una forma más elegante de ver si existe la instancia TSDB?
#     dummy = TSDB.persistent_id()
# except:
#     TSDB = ClsTSDB()

"""
There is no need to check the TSDB instance, just restore the data to the global variable TSDB.
It is not recommended to set custom variables in the global scope of
DefFuncs.py as it will be overwritten after loading the archive.
This is because the ObjStore data is restored after DefFuncs.py
- Sryml
"""
TSDB = ClsTSDB()

TSWidgets = ClsTSWidgets()
TSText = ClsTSText()
TSjText = ClsTSjText()
TS = ClsTS()

###########################################################################
# User Interface
###########################################################################


def DBClear():
    TSDB.Clear()


def ClearVars():
    TSDB.ClearVars()


def ClearJournal():
    TSDB.ClearJournal()


def SetVar(name, value):
    TSDB.SetVar(name, value)


def GetVar(name):
    return TSDB.GetVar(name)


def Load(filename):
    TSDB.Load(filename)


def Assign(person, dlgId, event=None):
    TSDB.Assign(person, dlgId, event)


def Validate():
    TSDB.Validate()


def AnswerDisable(person, ansId):
    TS.AnswerDisable(person, ansId)


def AnswerEnable(person, ansId):
    TS.AnswerEnable(person, ansId)


def Say(person, dlgId=None):
    TS.Say(person, dlgId)
    TSWidgets.Enable()


def SetAnswer(person, ansId, text, nextdlgId=None):
    TS.SetAnswer(person, ansId, text, nextdlgId)


def SetDialog(person, dlgId, text, answers=None):
    TS.SetDialog(person, dlgId, text, answers)


def AddCallBackFunc(FuncName, Func):
    TS.AddCallBackFunc(FuncName, Func)


def ShowMessage(Text, HideDelay=TSHideDelay):
    TS.ShowMessage(Text, HideDelay)
    TSWidgets.Enable()


def Hide():
    TSWidgets.Disable()


def AddToJournal(jrlId, Warning=0):
    TSDB.AddToJournal(jrlId, Warning)


def RemoveFromJournal(jrlId):
    TSDB.RemoveFromJournal(jrlId)


def SetBitMap(Name, File):
    TSWidgets.SetBitMap(Name, File)
