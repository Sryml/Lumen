#  _    _   _ __  __ _____ _   _
# | |  | | | |  \/  | ____| \ | |
# | |  | | | | |\/| |  _| |  \| |
# | |__| |_| | |  | | |___| |\  |
# |_____\___/|_|  |_|_____|_| \_|
#

import Bladex
import Lumenx
import BInput

import math

from Lumenx import printx, debugprint
from LumenLib import TimerAux, AnimAux
from LumenLib.mathutils import *

#
InputManager = BInput.GetInputManager()

DEBUG_IAS = "Lumen Debug"
CAMERA_ROAMING_IAS = "Lumen Debug - Camera Roaming"
LAST_IAS = []
LM_DEBUG_KEEP = 0

# uuid.uuid5(uuid.NAMESPACE_OID,"Lumen:MataEnemigo")
WP_NAME = "b0665d50-c59c-5dfd-82b7-115cf93b9633"


# ----------------------------------
# LM_Debug
# ----------------------------------
def ToggleInputSet():
    global LAST_IAS, LM_DEBUG_KEEP

    if LM_DEBUG_KEEP:
        LM_DEBUG_KEEP = 0
        Bladex.RestartTime()
        return

    CurrentIAS = InputManager.GetInputActionsSet()
    if BInput.CurrentlyActivated("Sneak") or BInput.CurrentlyActivated(
        "LMD_Shift"
    ):  # XXX 需要优化，利用LPC让Lumen服务返回按键状态
        IASet = CAMERA_ROAMING_IAS
    else:
        IASet = DEBUG_IAS
    if CurrentIAS != IASet:
        InputManager.SetInputActionsSet(IASet)
        LAST_IAS.append(CurrentIAS)
        #
        if IASet == DEBUG_IAS:
            Bladex.StopTime()
        elif IASet == CAMERA_ROAMING_IAS:
            CAMERA_ROAMING.LMD_CR_OnEnter()
    elif LAST_IAS:
        InputManager.SetInputActionsSet(LAST_IAS[-1])
        LAST_IAS.remove(LAST_IAS[-1])
        Bladex.RestartTime()

    debugprint("Input set changed to: " + InputManager.GetInputActionsSet())


def LMD_Keep():
    global LM_DEBUG_KEEP
    LM_DEBUG_KEEP = 1


def MataEnemigoEncarado():
    import Reference, InitDataField

    char = Lumenx.GetControlCharacter()
    victim_name = (
        char.ActiveEnemy or char.Data.selected_enemy and char.Data.selected_enemy[0]
    )
    if victim_name:
        victim = Bladex.GetEntity(victim_name)
        if victim.Life <= 0:
            return
        if getattr(victim.Data, "MataEnemigoEncarado", 0):
            damage = victim.Life + 100
        else:
            damage = int(victim.Life * 0.5)
        Reference.EntitiesObjectData[WP_NAME] = [
            Reference.OBJ_WEAPON,
            damage,
            0,
            2.2,
            Reference.THR_SPINNING,
            [
                Reference.W_FLAG_1H,
            ],
        ]
        DamageType = "Debug"  # "Slash"
        DamageZone = 1
        DamageNode = -1
        Shielded = 0
        if victim.DamageFunc:
            InitDataField.Initialise(victim, MataEnemigoEncarado=1)
            victim.DamageFunc(
                victim_name,
                "",  # char.Name,
                WP_NAME,
                DamageType,
                DamageZone,
                DamageNode,
                0,
                -1,
                0,
                Shielded,
            )
        elif victim.Life < 2:
            victim.Life = 0
        else:
            victim.Life = 1


def LMD_NextLevel():
    import GotoMapVars

    char = Bladex.GetEntity("Player1")
    if char.Life > 0.0:
        Bladex.AddScheduledFunc(
            Bladex.GetTime() + 0.0, GotoMapVars.EndOfLevel, (), "ChangingLevel"
        )


def LMD_ToggleInvincibility():
    import Actions

    Actions.ToggleInvincibility()


def LMD_SimulateHit():
    import Actions, Reference

    me = Lumenx.GetControlCharacter()
    DamageType = "Debug"  # "Slash"
    DamageZone = 1
    DamageNode = 1
    Shielded = 0
    if me.DamageFunc:
        Reference.EntitiesObjectData[WP_NAME] = [
            Reference.OBJ_WEAPON,
            1,
            0,
            2.2,
            Reference.THR_SPINNING,
            [
                Reference.W_FLAG_1H,
            ],
        ]
        me.DamageFunc(
            me.Name,
            "",
            WP_NAME,
            DamageType,
            DamageZone,
            DamageNode,
            0,
            -1,
            0,
            Shielded,
        )
    Actions.ReportMsg("Simulate Hit")


def LMD_Freeze():
    me = Lumenx.GetControlCharacter()
    me.Frozen = not me.Frozen


# ----------------------------------
# LM_Debug_Camera_Roaming
# ----------------------------------
class CameraRoaming:
    def __init__(self):
        self.Listener = BInput.B_InputListener("LMD_CR_Listener")
        self.Listener.SetPythonFunc(self.ListenDevice)
        self.Distance = 1000
        self.TPosOffset = Vector()
        #
        self.SpeedDefault = 90
        self.Speed = self.SpeedDefault
        self.SpeedUp = 3.0
        self.SpeedDown = 1 / 3.0
        self.TurnSpeed = 0.008

        self.SyncChar = 0
        self.Front = 0
        self.Back = 0
        self.Left = 0
        self.Right = 0
        self.Up = 0
        self.Down = 0
        self.Shift = 0
        self.LAlt = 0
        #
        self.KeyMap = {
            "W": "Front",
            "A": "Left",
            "S": "Back",
            "D": "Right",
            "R": "Up",
            "F": "Down",
            "F": "Down",
            "Shift": "Shift",
            "LAlt": "LAlt",
        }
        #
        dummy = Bladex.GetEntity("CameraRoamingTest")
        if not dummy:
            dummy = Bladex.CreateEntity(
                "CameraRoamingTest", "Trajectory", 0, 0, 0, "Physic"
            )
        dummy.SendSectorMsgs = 0
        dummy.CastShadows = 0
        dummy.Alpha = 0.0
        dummy.RemoveFromWorld()
        self.dummy = dummy
        #
        cam = Bladex.GetEntity("Camera")
        self.Animation = AnimAux.Animation(cam)

    def ResetKey(self):
        for v in self.KeyMap.values():
            self.__dict__[v] = 0

    def LMD_CR_OnEnter(self):
        self.ResetKey()

        o = Bladex.GetEntity("Player1")
        o.Freeze()
        cam = Bladex.GetEntity("Camera")
        cam.TType = 0
        cam.SType = 0
        Position = Vector(cam.Position)
        TPos = Vector(cam.TPos)
        self.Distance = (TPos - Position).length()
        self.TPosOffset = Vector(o.Position) - TPos
        self.SyncChar = 0
        Bladex.SetListenerPosition(2)
        #
        keyb = InputManager.GetAttachedDevice("Keyboard")
        keyb.AddListener(self.Listener)
        keyb = InputManager.GetAttachedDevice("Mouse")
        keyb.AddListener(self.Listener)
        #
        TimerAux.SubscribeToList("Timer60", self.LMD_CR_Timer)

    def LMD_CR_OnExit(self):
        if self.Animation.isRunning():
            return
        global LAST_IAS

        TimerAux.RemoveFromList("Timer60", self.LMD_CR_Timer)

        keyb = InputManager.GetAttachedDevice("Keyboard")
        keyb.RemoveListener(self.Listener.Name)
        keyb = InputManager.GetAttachedDevice("Mouse")
        keyb.RemoveListener(self.Listener.Name)
        #
        o = Bladex.GetEntity("Player1")
        o.UnFreeze()
        cam = Bladex.GetEntity("Camera")
        cam.SetPersonView("Player1")
        cam.Cut()
        Bladex.SetListenerPosition(1)
        #
        InputManager.SetInputActionsSet(LAST_IAS[-1])
        LAST_IAS.remove(LAST_IAS[-1])
        debugprint("Input set changed to: " + InputManager.GetInputActionsSet())

    def LMD_CR_SpeedUp(self):
        self.Speed = self.Speed + 30

    def LMD_CR_SpeedDown(self):
        self.Speed = max(8, self.Speed - 30)

    def LMD_CR_SpeedReset(self):
        self.Speed = self.SpeedDefault

    def LMD_CR_Confirm(self):
        if self.Animation.isRunning():
            return
        if not self.SyncChar:
            cam = Bladex.GetEntity("Camera")
            o = Bladex.GetEntity("Player1")
            o.Position = (Vector(cam.TPos) + self.TPosOffset).to_tuple()
        self.LMD_CR_OnExit()

    def LMD_CR_SyncChar(self):
        self.SyncChar = not self.SyncChar
        if self.SyncChar:
            o = Bladex.GetEntity("Player1")
            cam = Bladex.GetEntity("Camera")
            o.Position = (Vector(cam.TPos) + self.TPosOffset).to_tuple()

    def LMD_CR_Teleport(self):
        if self.Animation.isRunning():
            return
        #
        dummy = self.dummy
        cam = Bladex.GetEntity("Camera")
        Position = Vector(cam.Position)
        TPos = Vector(cam.TPos)
        direction = (TPos - Position).normalized()
        x_axis = Vector((1, 0, 0))
        axis = x_axis.cross(direction).normalized()
        angle = math.acos(x_axis.dot(direction))
        dummy.Orientation = ToQuat(axis, angle)
        dummy.Position = (TPos + direction * 1000.0).to_tuple()
        vx, vy, vz = (direction * 900).to_tuple()

        if not dummy.TestHit:
            while not dummy.TestHit:
                dummy.Move(vx, vy, vz)

            Duration = 0.5
            distance = (Vector(dummy.Position) - TPos).length()
            self.Animation.ClearChannels()
            pos_node = self.Animation.AddChannel().AddNode(
                0, distance, Duration, direction.to_tuple()
            )
            tpos_node = self.Animation.AddChannel().AddNode(
                0, distance, Duration, direction.to_tuple(), TPos.to_tuple()
            )
            tpos_node.TargetAttr = "TPos"
            self.Animation.run()
            if self.SyncChar:
                o = Bladex.GetEntity("Player1")
                anim = AnimAux.Animation(o)
                pos_node = anim.AddChannel().AddNode(
                    0, distance, Duration, direction.to_tuple()
                )
                anim.run()
            #
            dummy.RemoveFromWorld()

    def ListenDevice(self, x, y, z):
        if self.Animation.isRunning():
            return
        key = self.KeyMap.get(x)
        if key:
            self.__dict__[key] = z
        elif x in ("X_Axis", "Y_Axis"):
            cam = Bladex.GetEntity("Camera")
            Position = Vector(cam.Position)
            TPos = Vector(cam.TPos)
            direction = (TPos - Position).normalized()
            angle = z * self.TurnSpeed

            dot = direction.dot((0, 1, 0))
            if dot > epsilon2:
                direction = Vector((0.0174, 0.9998, 0.0)).normalized()
            elif dot < -epsilon2:
                direction = Vector((0.0174, -0.9998, 0.0)).normalized()

            if x == "X_Axis":
                direction = Quaternion((0, 1, 0), angle) * direction
            else:
                if angle < 0:
                    min_angle = -math.acos(direction.dot((0, -1, 0))) + 0.0174
                    angle = max(min_angle, angle)
                elif angle > 0:
                    max_angle = math.acos(direction.dot((0, 1, 0))) - 0.0174
                    angle = min(max_angle, angle)
                if abs(angle) > epsilon:
                    axis = direction.cross(Vector((0, 1, 0))).normalized()
                    direction = Quaternion(axis, angle) * direction

            TPos = Position + direction * self.Distance
            cam.TPos = TPos.to_tuple()
            if self.SyncChar:
                o = Bladex.GetEntity("Player1")
                o.Position = (TPos + self.TPosOffset).to_tuple()
                o.Angle = GetXZAngle(direction.x, 0, direction.z)

    def LMD_CR_Timer(self, time):
        if self.Animation.isRunning():
            return
        cam = Bladex.GetEntity("Camera")
        Position = Vector(cam.Position)
        TPos = Vector(cam.TPos)
        z_axis = (TPos - Position).normalized()
        x_axis = z_axis.cross(Vector((0, -1, 0))).normalized()
        y_axis = x_axis.cross(z_axis).normalized()
        if self.Shift:
            Speed = self.Speed * self.SpeedUp
        elif self.LAlt:
            Speed = self.Speed * self.SpeedDown
        else:
            Speed = self.Speed
        #
        direction = Vector((0, 0, 0))
        if self.Front:
            direction = z_axis
        elif self.Back:
            direction = -z_axis
        if self.Left:
            direction = direction - x_axis
        elif self.Right:
            direction = direction + x_axis
        if self.Up:
            direction = direction + y_axis
        elif self.Down:
            direction = direction - y_axis

        if direction != (0, 0, 0):  # type: ignore
            direction = direction.normalized()
            offset = direction * Speed
            cam.Position = (Position + offset).to_tuple()
            TPos = TPos + offset
            cam.TPos = TPos.to_tuple()
            if self.SyncChar:
                o = Bladex.GetEntity("Player1")
                o.Position = (TPos + self.TPosOffset).to_tuple()


# ----------------------------------
def AddInputSet():
    OldIASet = InputManager.GetInputActionsSet()
    if not InputManager.AddInputActionsSet(DEBUG_IAS):
        return

    global CAMERA_ROAMING
    CAMERA_ROAMING = CameraRoaming()

    wp = Bladex.GetEntity(WP_NAME)
    if not wp:
        wp = Bladex.CreateEntity(WP_NAME, "Gladius", 0, 0, 0, "Weapon")
        wp.SendSectorMsgs = 0
        wp.Alpha = 0
        wp.RemoveFromWorld()

    # DEBUG_IAS
    InputManager.SetInputActionsSet(DEBUG_IAS)

    Bladex.AddInputAction("LMD_Toggle", 0)
    Bladex.AssocKey("LMD_Toggle", "Keyboard", "Grave", 0)
    Bladex.AddBoundFunc("LMD_Toggle", ToggleInputSet)

    Bladex.AddInputAction("LMD_Keep", 0)
    Bladex.AssocKey("LMD_Keep", "Keyboard", "Tab")
    Bladex.AddBoundFunc("LMD_Keep", LMD_Keep)

    Bladex.AddInputAction("LMD_Shift", 0)
    Bladex.AssocKey("LMD_Shift", "Keyboard", "Shift")

    Bladex.AddInputAction("LMD_Mata", 0)
    Bladex.AssocKey("LMD_Mata", "Keyboard", "K")
    Bladex.AddBoundFunc("LMD_Mata", MataEnemigoEncarado)

    Bladex.AddInputAction("LMD_Toggle_BB", 0)
    Bladex.AssocKey("LMD_Toggle_BB", "Keyboard", "F4")
    Bladex.AddBoundFunc("LMD_Toggle_BB", "Toggle BB")

    Bladex.AddInputAction("LMD_Camera_Left", 1)
    Bladex.AssocKey("LMD_Camera_Left", "Keyboard", "F5")
    Bladex.AddBoundFunc("LMD_Camera_Left", "Camera Left")

    Bladex.AddInputAction("LMD_Camera_Right", 1)
    Bladex.AssocKey("LMD_Camera_Right", "Keyboard", "F6")
    Bladex.AddBoundFunc("LMD_Camera_Right", "Camera Right")

    # Bladex.AddInputAction("LMD_Camera Dist", 0)
    # Bladex.AssocKey("LMD_Camera Dist", "Keyboard", "F7")
    # Bladex.AddBoundFunc("LMD_Camera Dist", "Change Camera")

    # Bladex.AddInputAction("LMD_Fixed Camera", 0)
    # Bladex.AssocKey("LMD_Fixed Camera", "Keyboard", "F8")
    # Bladex.AddBoundFunc("LMD_Fixed Camera", "Fixed Camera")

    # Bladex.AddInputAction("LMD_Camera Dist", 0)
    # Bladex.AssocKey("LMD_Camera Dist", "Keyboard", "F9")
    # Bladex.AddBoundFunc("LMD_Camera Dist", "Camera Dist")

    Bladex.AddInputAction("LMD_NextLevel", 0)
    Bladex.AssocKey("LMD_NextLevel", "Keyboard", "F9", 1)
    Bladex.AddBoundFunc("LMD_NextLevel", LMD_NextLevel)

    Bladex.AddInputAction("LMD_ToggleInvincibility", 0)
    Bladex.AssocKey("LMD_ToggleInvincibility", "Keyboard", "F10")
    Bladex.AddBoundFunc("LMD_ToggleInvincibility", LMD_ToggleInvincibility)

    Bladex.AddInputAction("LMD_Bigger FOV", 0)
    Bladex.AssocKey("LMD_Bigger FOV", "Keyboard", "F11")
    Bladex.AddBoundFunc("LMD_Bigger FOV", "Bigger FOV")

    Bladex.AddInputAction("LMD_Smaller FOV", 0)
    Bladex.AssocKey("LMD_Smaller FOV", "Keyboard", "F12")
    Bladex.AddBoundFunc("LMD_Smaller FOV", "Smaller FOV")

    Bladex.AddInputAction("LMD_SimulateHit", 0)
    Bladex.AssocKey("LMD_SimulateHit", "Keyboard", "Numpad1")
    Bladex.AddBoundFunc("LMD_SimulateHit", LMD_SimulateHit)

    Bladex.AddInputAction("LMD_Freeze", 0)
    Bladex.AssocKey("LMD_Freeze", "Keyboard", "Numpad2")
    Bladex.AddBoundFunc("LMD_Freeze", LMD_Freeze)

    # CAMERA_ROAMING_IAS
    InputManager.AddInputActionsSet(CAMERA_ROAMING_IAS)
    InputManager.SetInputActionsSet(CAMERA_ROAMING_IAS)

    Bladex.AddInputAction("LMD_CR_SpeedUp", 0)
    Bladex.AssocKey("LMD_CR_SpeedUp", "Mouse", "WheelUp")
    Bladex.AddBoundFunc("LMD_CR_SpeedUp", CAMERA_ROAMING.LMD_CR_SpeedUp)

    Bladex.AddInputAction("LMD_CR_SpeedDown", 0)
    Bladex.AssocKey("LMD_CR_SpeedDown", "Mouse", "WheelDown")
    Bladex.AddBoundFunc("LMD_CR_SpeedDown", CAMERA_ROAMING.LMD_CR_SpeedDown)

    Bladex.AddInputAction("LMD_CR_SpeedReset", 0)
    Bladex.AssocKey("LMD_CR_SpeedReset", "Mouse", "MiddleButton")
    Bladex.AddBoundFunc("LMD_CR_SpeedReset", CAMERA_ROAMING.LMD_CR_SpeedReset)

    # Bladex.AddInputAction("LMD_CR_Confirm", 0)
    # Bladex.AssocKey("LMD_CR_Confirm", "Mouse", "LeftButton")
    # Bladex.AddBoundFunc("LMD_CR_Confirm", CAMERA_ROAMING.LMD_CR_Confirm)

    Bladex.AddInputAction("LMD_CR_OnExit", 0)
    Bladex.AssocKey("LMD_CR_OnExit", "Mouse", "RightButton")
    Bladex.AddBoundFunc("LMD_CR_OnExit", CAMERA_ROAMING.LMD_CR_OnExit)

    Bladex.AddInputAction("LMD_CR_SyncChar", 0)
    Bladex.AssocKey("LMD_CR_SyncChar", "Keyboard", "Q")
    Bladex.AddBoundFunc("LMD_CR_SyncChar", CAMERA_ROAMING.LMD_CR_SyncChar)

    Bladex.AddInputAction("LMD_CR_Teleport", 0)
    Bladex.AssocKey("LMD_CR_Teleport", "Keyboard", "Space")
    Bladex.AddBoundFunc("LMD_CR_Teleport", CAMERA_ROAMING.LMD_CR_Teleport)

    # Default
    InputManager.SetInputActionsSet("Default")

    Bladex.AddInputAction("Toggle_LM_Debug", 0)
    Bladex.AssocKey("Toggle_LM_Debug", "Keyboard", "Grave")
    Bladex.AddBoundFunc("Toggle_LM_Debug", ToggleInputSet)
    #
    InputManager.SetInputActionsSet(OldIASet)


# ----------------------------------
Bladex.AddScheduledFunc(-1, AddInputSet, (), Lumenx.GetNSaveName())
