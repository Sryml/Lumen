#  _    _   _ __  __ _____ _   _
# | |  | | | |  \/  | ____| \ | |
# | |  | | | | |\/| |  _| |  \| |
# | |__| |_| | |  | | |___| |\  |
# |_____\___/|_|  |_|_____|_| \_|
#

# Refactored by Sryml
# Date: 2024-04-27

# This file was created automatically by SWIG.

import Bladex
import Lumenx
import BInputc
import BCopy
import types

from Lumenx import printx

__CurrentInputActions = "Default"
__InputActionsSet = {}  # type: dict[str,B_InputActionsPtr]
__InputActionsNum = 0
# __AutoUniqueization = 0  # Enabling it will cause some button functions to fail, such as the attack function.


def Wrapper(func):
    def wrapped(func=func):
        Bladex.AddScheduledFunc(-1, func, (), "[NSAVE]")

    return wrapped


def GetInternalName(ID, action_name):
    return action_name
    # global __AutoUniqueization
    # if not __AutoUniqueization:
    #     return action_name
    # else:
    #     return str(ID) + "_" + action_name


class B_InputListenerPtr:
    def __init__(self, this):
        self.this = this
        self.thisown = 0

    def SetPythonFunc(self, arg0):
        val = BInputc.B_InputListener_SetPythonFunc(self.this, arg0)
        return val

    def EventCallback(self, arg0, arg1, arg2):
        val = BInputc.B_InputListener_EventCallback(self.this, arg0, arg1, arg2)
        return val

    def __str__(self):
        val = BInputc.B_InputListener___str__(self.this)
        return val

    def __repr__(self):
        return "<C B_InputListener instance>"


class B_InputListener(B_InputListenerPtr):
    def __init__(self, arg0):
        self.this = BInputc.new_B_InputListener(arg0)
        self.thisown = 1
        self.Name = arg0  #


class B_InputDevicePtr:
    def __init__(self, this, device):
        self.this = this
        self.thisown = 0
        self.__name = device

    def AddListener(self, arg0):
        val = BInputc.B_InputDevice_AddListener(self.this, arg0.this)
        return val

    def Name(self):
        """Newly added function to get the name of the device."""
        return self.__name

    def RemoveListener(self, arg0):
        val = BInputc.B_InputDevice_RemoveListener(self.this, arg0)
        return val

    def nListeners(self):
        val = BInputc.B_InputDevice_nListeners(self.this)
        return val

    def IsBinded(self, arg0, *args):
        val = apply(
            BInputc.B_InputDevice_IsBinded,
            (
                self.this,
                arg0,
            )
            + args,
        )
        return val

    def UnBinded(self, key):
        """Newly added function to unbind a key."""
        count = 0
        IActions = InputManager.GetInputActions()
        for action_name in IActions.names:
            for k, on_press in IActions.actions[action_name]["Devices"][self.Name()]:
                if k == key:
                    IAction = IActions.Find(action_name)
                    IAction.RemoveEvent(self, key, on_press)
                    count = count + 1
                    if count == 2:
                        break
        return 1

    def __str__(self):
        val = BInputc.B_InputDevice___str__(self.this)
        return val

    def __repr__(self):
        return "<C B_InputDevice instance>"


class B_InputDevice(B_InputDevicePtr):
    def __init__(self, this):
        self.this = this


class B_nInputEventPtr:
    def __init__(self, this):
        self.this = this
        self.thisown = 0

    def GetPress(self):
        val = BInputc.B_nInputEvent_GetPress(self.this)
        return val

    def GetDevice(self):
        val = BInputc.B_nInputEvent_GetDevice(self.this)
        return val

    def GetKey(self):
        val = BInputc.B_nInputEvent_GetKey(self.this)
        return val

    def __repr__(self):
        return "<C B_nInputEvent instance>"


class B_nInputEvent(B_nInputEventPtr):
    def __init__(self, this):
        self.this = this


class B_InputActionPtr:
    def __init__(self, this, name, action):
        self.this = this
        self.thisown = 0
        self.name = name
        self.action = action

    def __getstate__(self):
        pass

    def __setstate__(self, parms):
        pass

    def __str__(self):
        val = BInputc.B_InputAction___str__(self.this)
        return val

    def Name(self):
        return self.name
        # val = BInputc.B_InputAction_Name(self.this)
        # return val

    def IsConst(self):
        val = BInputc.B_InputAction_IsConst(self.this)
        return val

    def nInputEvents(self):
        val = BInputc.B_InputAction_nInputEvents(self.this)
        return val

    def nProcs(self):
        val = BInputc.B_InputAction_nProcs(self.this)
        return val

    def AddEvent(self, device_obj, key, on_press, toggle=0):
        device = device_obj.Name()
        key_tuple = (key, on_press)
        if key_tuple in self.action["Devices"][device] and (not toggle):
            return 0

        if not toggle:
            IActions = InputManager.GetInputActions()
            # If already bound, unbind and overwrite
            if device_obj.IsBinded(key):
                for name in IActions.names:
                    # Actions with IsConst set to 1 will not be overridden, skipped
                    if IActions.actions[name]["IsConst"] or name == self.name:
                        continue
                    if key_tuple in IActions.actions[name]["Devices"][device]:
                        IAction = IActions.Find(name)
                        IAction.RemoveEvent(device_obj, key, on_press)
                        break
            #
            self.action["Devices"][device].append(key_tuple)
        val = BInputc.B_InputAction_AddEvent(self.this, device_obj.this, key, on_press)
        return val

    def GetnInputEvent(self, *args):
        val = apply(BInputc.B_InputAction_GetnInputEvent, (self.this,) + args)
        val = B_nInputEventPtr(val)
        return val

    def GetTimeActivated(self):
        val = BInputc.B_InputAction_GetTimeActivated(self.this)
        return val

    def GetAssociatedKeys(self, device):
        """[LUMEN] Added\n
        device: [Keyboard, Mouse, Gamepad]\n
        returns: List of tuples (key, on_press)
        """
        if self.name == "NULL":
            return []
        return BCopy.deepcopy(self.action["Devices"].get(device, []))

    def CurrentlyActivated(self):
        val = BInputc.B_InputAction_CurrentlyActivated(self.this)
        return val

    def RemoveEvent(self, device_obj, key, on_press):
        device = device_obj.Name()
        key_tuple = (key, on_press)
        if key_tuple not in self.action["Devices"][device]:
            return 0

        val = BInputc.B_InputAction_RemoveEvent(
            self.this, device_obj.this, key, on_press
        )
        self.action["Devices"][device].remove(key_tuple)
        return val

    def RemoveAllEvents(self, toggle=0):
        if not toggle:
            for device in self.action["Devices"].keys():
                self.action["Devices"][device] = []
        val = BInputc.B_InputAction_RemoveAllEvents(self.this)
        return val

    def RemoveAllDeviceEvents(self, device):
        """New to the reissue, it now also applies to the Classic Edition."""
        if not hasattr(BInputc, "B_InputAction_RemoveAllDeviceEvents"):
            # printx("RemoveAllDeviceEvents: Not available in current version.")
            device_obj = GetInputManager().GetAttachedDevice(device)
            for key, on_press in self.action["Devices"][device]:
                self.RemoveEvent(device_obj, key, on_press)
            return 1

        val = BInputc.B_InputAction_RemoveAllDeviceEvents(self.this, device)  # type: ignore
        self.action["Devices"][device] = []
        return val

    def RemoveAllProcs(self, toggle=0):
        if not toggle:
            self.action["BoundFunc"] = []
            self.action["BoundFuncMap"] = {}
        val = BInputc.B_InputAction_RemoveAllProcs(self.this)
        return val

    def __repr__(self):
        return "<C B_InputAction instance>"


class B_InputAction(B_InputActionPtr):
    def __init__(self, this):
        self.this = this


class B_InputActionsPtr:
    def __init__(self, this, ID):
        self.this = this
        self.thisown = 0
        self.ID = ID
        self.names = []
        self.actions = {
            # "action_name": {
            #     "IsConst": 0,
            #     "Devices": {
            #         "Keyboard": [("A", 1),("A", 0)],
            #         "Mouse": [],
            #         "Gamepad": [],
            #     },
            #     "BoundFunc": [],
            # },
        }

    def __getstate__(self):
        pass

    def __setstate__(self, parms):
        pass

    def nElements(self):
        return len(self.names)
        # val = BInputc.B_InputActions_nElements(self.this)
        # return val

    def GetAction(self, idx):
        return self.Find(self.names[idx])
        # val = BInputc.B_InputActions_GetAction(self.this, arg0)
        # val = B_InputActionPtr(val)
        # return val

    def Find(self, action_name):
        if action_name not in self.names:
            action_name = "NULL"
        val = BInputc.B_InputActions_Find(
            self.this, GetInternalName(self.ID, action_name)
        )
        val = B_InputActionPtr(val, action_name, self.actions.get(action_name, None))
        return val

    def RemoveAction(self, action_name, dict_only=0, toggle=0):
        """dict_only: If set to 1, only the dictionary is updated"""
        if action_name not in self.names:
            return 0

        if not toggle:
            self.names.remove(action_name)
            self.actions[action_name]["BoundFunc"] = []
            self.actions[action_name]["BoundFuncMap"] = {}
            del self.actions[action_name]
        if not dict_only:
            val = BInputc.B_InputActions_RemoveAction(
                self.this, GetInternalName(self.ID, action_name)
            )
        return 1

    def __str__(self):
        val = BInputc.B_InputActions___str__(self.this)
        return val

    def __repr__(self):
        return "<C B_InputActions instance>"


class B_InputActions(B_InputActionsPtr):
    def __init__(self, this):
        self.this = this


class B_InputManagerPtr:
    def __init__(self, this):
        self.this = this
        self.thisown = 0
        self.InputActionsSet = globals()[
            "__InputActionsSet"
        ]  # type: dict[str,B_InputActionsPtr]

    def __del__(self):
        if self.thisown == 1:
            BInputc.delete_B_InputManager(self.this)

    def GetTimeActionHeld(self, action_name, time):
        action_name = GetInternalName(self.GetInputActions().ID, action_name)
        val = BInputc.B_InputManager_GetTimeActionHeld(self.this, action_name, time)
        return val

    def GetTimeActionActivated(self, action_name):
        action_name = GetInternalName(self.GetInputActions().ID, action_name)
        val = BInputc.B_InputManager_GetTimeActionActivated(self.this, action_name)
        return val

    def AddInputAction(self, action_name, IsConst, dict_only=0, toggle=0):
        """dict_only: If set to 1, only the dictionary is updated"""
        IActions = self.GetInputActions()
        if not toggle:
            if action_name in IActions.names:
                return 0

            IActions.names.append(action_name)
            IActions.actions[action_name] = {
                "IsConst": IsConst,
                "Devices": {
                    "Keyboard": [],
                    "Mouse": [],
                    "Gamepad": [],
                },
                "BoundFunc": [],
                "BoundFuncMap": {},
            }
        if not dict_only:
            action_name = GetInternalName(IActions.ID, action_name)
            val = BInputc.B_InputManager_AddInputAction(self.this, action_name, IsConst)
        return 1

    def AssocKey(self, action_name, device, key, on_press, dict_only=0, toggle=0):
        """dict_only: If set to 1, only the dictionary is updated"""
        IActions = self.GetInputActions()
        if not toggle:
            if action_name not in IActions.names:
                return 0

            key_tuple = (key, on_press)
            if key_tuple in IActions.actions[action_name]["Devices"][device]:
                return 0
            # If already bound, unbind and overwrite
            device_obj = GetInputManager().GetAttachedDevice(device)
            if device_obj.IsBinded(key):
                for name in IActions.names:
                    # Actions with IsConst set to 1 will not be overridden, skipped
                    if IActions.actions[name]["IsConst"] or name == action_name:
                        continue
                    if key_tuple in IActions.actions[name]["Devices"][device]:
                        IAction = IActions.Find(name)
                        IAction.RemoveEvent(device_obj, key, on_press)
                        break
            #
            IActions.actions[action_name]["Devices"][device].append(key_tuple)

        if not dict_only:
            action_name = GetInternalName(IActions.ID, action_name)
            val = BInputc.B_InputManager_AssocKey(
                self.this, action_name, device, key, on_press
            )
        return 1

    def DisassocKey(self, device, key):
        # if not hasattr(BInputc, "B_InputManager_DisassocKey"):
        #     printx("DisassocKey: Not available in current version.")
        #     return
        # val = BInputc.B_InputManager_DisassocKey(self.this, device, key)  # type: ignore
        return self.GetAttachedDevice(device).UnBinded(key)

    def AddBoundFunc(self, action_name, proc, toggle=0):
        """[LUMEN] Added"""
        IActions = self.GetInputActions()
        val = 0
        if toggle:
            val = 1
        else:
            if action_name in IActions.names:
                action = IActions.actions[action_name]
                raw_proc = proc
                if not action["BoundFuncMap"].has_key(raw_proc):
                    if type(raw_proc) == types.StringType:
                        action["BoundFuncMap"][raw_proc] = proc
                    else:
                        action["BoundFuncMap"][raw_proc] = Wrapper(proc)

                proc = action["BoundFuncMap"][raw_proc]
                action["BoundFunc"].append(proc)
                val = 1
        if val:
            Lumenx.Bladex_raw.AddBoundFunc(action_name, proc)
        return val

    def RemoveBoundFunc(self, action_name, proc, toggle=0):
        """[LUMEN] Added"""
        IActions = self.GetInputActions()
        val = 0
        if toggle:
            val = 1
        else:
            if action_name in IActions.names:
                action = IActions.actions[action_name]
                raw_proc = proc
                proc = action["BoundFuncMap"].get(raw_proc)
                if proc:
                    action["BoundFunc"].remove(proc)
                    if proc not in action["BoundFunc"]:
                        del action["BoundFuncMap"][raw_proc]
                    val = 1
        if val:
            Lumenx.Bladex_raw.RemoveBoundFunc(action_name, proc)
        return val

    def Bind2(self, arg0, arg1, arg2, arg3):
        val = BInputc.B_InputManager_Bind2(self.this, arg0, arg1, arg2, arg3)
        return val

    def GetInputActions(self):
        # type: () -> B_InputActionsPtr
        return self.InputActionsSet[self.GetInputActionsSet()]
        # val = BInputc.B_InputManager_GetInputActions(self.this)
        # val = B_InputActionsPtr(val)
        # return val

    def GetAttachedDevice(self, device):
        val = BInputc.B_InputManager_GetAttachedDevice(self.this, device)
        val = B_InputDevicePtr(val, device)
        return val

    def AddInputActionsSet(self, set_name):
        if self.InputActionsSet.get(set_name, None):
            return 0

        InputActionsNum = globals()["__InputActionsNum"] + 1
        globals()["__InputActionsNum"] = InputActionsNum
        val = BInputc.B_InputManager_GetInputActions(self.this)
        self.InputActionsSet[set_name] = B_InputActionsPtr(val, InputActionsNum)
        return 1
        # val = BInputc.B_InputManager_AddInputActionsSet(self.this,arg0)
        # return val

    def ClearInputActionsSet(self, set_name):
        """New to the reissue, it now also applies to the Classic Edition."""
        if not self.InputActionsSet.get(set_name, None):
            return 0
        if set_name == self.GetInputActionsSet():
            self.SetInputActionsSet("Default")

        IActions = self.InputActionsSet[set_name]
        for action_name in IActions.names:
            IAction = IActions.Find(action_name)
            IAction.RemoveAllProcs()
            IAction.RemoveAllEvents()
            IActions.RemoveAction(action_name)

        del self.InputActionsSet[set_name]
        return 1
        # val = BInputc.B_InputManager_ClearInputActionsSet(self.this,arg0)
        # return val

    def SetInputActionsSet(self, set_name):
        if not self.InputActionsSet.get(set_name, None):
            return 0

        if set_name == self.GetInputActionsSet():
            return 1

        IActions = self.GetInputActions()
        for action_name in IActions.names:
            # IAction = IActions.Find(action_name)
            # IAction.RemoveAllEvents(toggle=1)
            # IAction.RemoveAllProcs(toggle=1)
            # if IAction.IsConst():
            Bladex.RemoveInputAction(action_name, toggle=1)  # type: ignore

        IActions = self.InputActionsSet[set_name]
        for action_name in IActions.names:
            actions = IActions.actions[action_name]
            # if actions["IsConst"]:
            Bladex.AddInputAction(action_name, actions["IsConst"], toggle=1)  # type: ignore
            for device, keys in actions["Devices"].items():
                for key, on_press in keys:
                    Bladex.AssocKey(action_name, device, key, on_press, toggle=1)  # type: ignore
            for proc in actions["BoundFunc"]:
                InputManager.AddBoundFunc(action_name, proc, toggle=1)
            # IAction = IActions.Find(action_name)
            # for device, keys in IActions.actions[action_name]["Devices"].items():
            #     device_obj = self.GetAttachedDevice(device)
            #     for key, on_press in keys:
            #         IAction.AddEvent(device_obj, key, on_press, toggle=1)

        globals()["__CurrentInputActions"] = set_name
        return 1
        # val = BInputc.B_InputManager_SetInputActionsSet(self.this,arg0)
        # return val

    def GetInputActionsSet(self):
        return globals()["__CurrentInputActions"]
        # val = BInputc.B_InputManager_GetInputActionsSet(self.this)
        # return val

    def GetAllInputActionsSet(self):
        """[LUMEN] Added"""
        return self.InputActionsSet.keys()

    def __repr__(self):
        return "<C B_InputManager instance>"


class B_InputManager(B_InputManagerPtr):
    def __init__(self):
        self.this = BInputc.new_B_InputManager()
        self.thisown = 1


# -------------- FUNCTION WRAPPERS ------------------

InputManager = None


def GetInputManager():
    global InputManager
    if not InputManager:
        InputManager = BInputc.GetInputManager()
        InputManager = B_InputManagerPtr(InputManager)
    return InputManager


def CurrentlyActivated(action_name):
    action = InputManager.GetInputActions().Find(action_name)
    if action.this != "NULL" and action.CurrentlyActivated():
        return 1
    return 0


# -------------- VARIABLE WRAPPERS ------------------

# -------------- INITIALIZATION ------------------

GetInputManager().AddInputActionsSet("EmptySet")
GetInputManager().AddInputActionsSet("Default")
