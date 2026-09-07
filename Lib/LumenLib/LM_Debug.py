#  _    _   _ __  __ _____ _   _
# | |  | | | |  \/  | ____| \ | |
# | |  | | | | |\/| |  _| |  \| |
# | |__| |_| | |  | | |___| |\  |
# |_____\___/|_|  |_|_____|_| \_|
#

import Bladex
import Lumenx
import BInput

from Lumenx import printx, debugprint

#
InputManager = BInput.GetInputManager()

DEBUG_INPUT_SET = "LM_Debug"
LAST_INPUT_SET = None
LM_DEBUG_KEEP = 0

# ----------------------------------


def ToggleInputSet():
    global LAST_INPUT_SET, LM_DEBUG_KEEP

    if LM_DEBUG_KEEP:
        LM_DEBUG_KEEP = 0
        return

    CurrentIAS = InputManager.GetInputActionsSet()
    if CurrentIAS != DEBUG_INPUT_SET:
        InputManager.SetInputActionsSet(DEBUG_INPUT_SET)
        LAST_INPUT_SET = CurrentIAS
    elif LAST_INPUT_SET:
        InputManager.SetInputActionsSet(LAST_INPUT_SET)
        LAST_INPUT_SET = None

    debugprint("Input set changed to: " + InputManager.GetInputActionsSet())


def LM_Debug_keep():
    global LM_DEBUG_KEEP
    LM_DEBUG_KEEP = 1


def AddInputSet():
    OldIASet = InputManager.GetInputActionsSet()
    if not InputManager.AddInputActionsSet(DEBUG_INPUT_SET):
        return
    InputManager.SetInputActionsSet(DEBUG_INPUT_SET)
    #
    Bladex.AddInputAction("LM_Debug_Toggle", 0)
    Bladex.AssocKey("LM_Debug_Toggle", "Keyboard", "Grave", 0)
    Bladex.AddBoundFunc("LM_Debug_Toggle", ToggleInputSet)

    Bladex.AddInputAction("LM_Debug_keep", 0)
    Bladex.AssocKey("LM_Debug_keep", "Keyboard", "1")
    Bladex.AddBoundFunc("LM_Debug_keep", LM_Debug_keep)
    #
    InputManager.SetInputActionsSet("Default")
    Bladex.AddInputAction("Toggle_LM_Debug", 0)
    Bladex.AssocKey("Toggle_LM_Debug", "Keyboard", "Grave")
    Bladex.AddBoundFunc("Toggle_LM_Debug", ToggleInputSet)
    #
    InputManager.SetInputActionsSet(OldIASet)


# ----------------------------------
Bladex.AddScheduledFunc(-1, AddInputSet, (), Lumenx.GetNSaveName())
