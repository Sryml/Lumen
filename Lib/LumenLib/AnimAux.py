#  _    _   _ __  __ _____ _   _
# | |  | | | |  \/  | ____| \ | |
# | |  | | | | |\/| |  _| |  \| |
# | |__| |_| | |  | | |___| |\  |
# |_____\___/|_|  |_|_____|_| \_|
#

import Bladex
import Lumenx
import InitDataField
import ObjStore
import GameStateAux

# import GameState
# import Reference

import math
import sys
import traceback

from Lumenx import printx
from LumenLib import TimerAux
from LumenLib.mathutils import *

#
import typing

if typing.TYPE_CHECKING:
    apply = lambda fn, args=(), kwds={}: None
    execfile = lambda filename, globals=None, locals=None: None
    cmp = lambda x, y: None


# ----------------------------------
LINEAR = "linear"
EASE_OUT_SINE = "ease_out_sine"
EASE_IN_SINE = "ease_in_sine"
EASE_IN_QUAD = "ease_in_quad"
EASE_OUT_QUAD = "ease_out_quad"
EASE_IN_OUT = "ease_in_out"

# Destroy Methods
DESTROY_METHOD_BIN = 1
DESTROY_METHOD_REMOVE = 2


# ----------------------------------
def TrackEntity(
    self,
    track_name,
    bone_loc=None,
    anchor_loc="",
    local_vector=(0, 0, 0),
    anchor_dir="",
    local_dir=(0, 0, 0),
):
    track_ent = Bladex.GetEntity(track_name)  # type: Bladex._entity.B_PyEntity
    #
    x, y, z = local_vector
    if bone_loc is not None:
        if bone_loc == "":
            LocationBasis = track_ent.Rel2AbsPoint(x, y, z)
        else:
            LocationBasis = track_ent.Rel2AbsPoint(x, y, z, bone_loc)
    elif anchor_loc:
        LocationBasis = track_ent.Rel2AbsPoint4Anchor(x, y, z, anchor_loc)
    else:
        LocationBasis = (Vector(track_ent.Position) + Vector(local_vector)).to_tuple()

    self.LocationBasis = LocationBasis
    #
    x, y, z = local_dir
    if anchor_dir:
        Direction = track_ent.GetDummyAxis(anchor_dir, x, y, z)
        self.Direction = Direction
    #
    self.OrientationBasis = track_ent.Orientation


# ----------------------------------
class EasingFunctions:
    def linear(self, t):
        return t

    def ease_out_sine(self, t):
        return math.sin(t * math.pi / 2)

    def ease_in_sine(self, t):
        return 1 - math.cos(t * math.pi / 2)

    def ease_in_quad(self, t):
        return t * t

    def ease_out_quad(self, t):
        return 1 - (1 - t) * (1 - t)

    def ease_in_out(self, t):
        if t < 0.5:
            return 2 * t * t
        return 1 - math.pow((-2 * t + 2), 2) / 2


class AnimEvent:
    def __init__(self):
        self.Events = []

    def AddEvent(self, time, callback):
        self.Events.append([time, callback, 1])
        self.Events.sort(lambda x, y: x > y)  # type: ignore

    def RemoveEvent(self, time, callback):
        for event in self.Events:
            if event[0] == time and event[1] == callback:
                self.Events.remove(event)
                break

    def _update(self, elapsed):
        for event in self.Events:
            time, callback, pending = event
            if not pending:
                continue
            if time <= elapsed:
                apply(callback[0], callback[1])
                event[2] = 0
                break

    def Reset(self):
        for event in self.Events:
            event[2] = 1


class Node(AnimEvent, EasingFunctions):
    def __init__(
        self,
        Name,
        Start,
        End,
        Duration,
        Direction=(1, 0, 0),
        LocationBasis=None,
        OrientationBasis=None,
        Execute="Translation",
        BeforeFrame=(None, (), {}),
        OnComplete=(None, ()),
        Easing=LINEAR,
    ):
        AnimEvent.__init__(self)

        self.Name = Name
        me = Bladex.GetEntity(self.Name)
        #
        self.Start = Start
        self.End = End
        self.Duration = Duration
        self.Execute = getattr(self, Execute, self.Translation)
        self.BeforeFrame = BeforeFrame
        self.OnComplete = OnComplete
        self.Easing = getattr(self, Easing)
        #
        if LocationBasis is None:
            LocationBasis = me.Position
        if OrientationBasis is None:
            OrientationBasis = me.Orientation

        self.Direction = Direction  # type: ...
        self.LocationBasis = LocationBasis  # type: ...
        self.OrientationBasis = OrientationBasis  # type: ...
        #
        self.Period = End - Start
        self.elapsed = 0
        self.progress = 0
        #
        self.Axis = (1, 0, 0)

    def _update(self, me, elapsed):
        progress = min(elapsed / self.Duration, 1.0)
        eased_progress = self.Easing(progress)
        value = self.Start + self.Period * eased_progress

        self.elapsed = elapsed
        self.progress = progress

        if self.BeforeFrame[0]:
            apply(
                self.BeforeFrame[0], (self,) + self.BeforeFrame[1], self.BeforeFrame[2]
            )
        self.Execute(me, value)
        #
        AnimEvent._update(self, elapsed)
        #
        if progress == 1.0:
            if self.OnComplete[0]:
                apply(self.OnComplete[0], self.OnComplete[1])

        return progress

    # def Execute(self, me, value):
    #     pass

    # def EndExecute(self):
    #     pass

    # 平移
    def Translation(self, me, value):
        # type: (Bladex._entity.B_PyEntity, float) -> ...
        vx, vy, vz = Scale(self.Direction, value)  # type: ignore
        x, y, z = self.LocationBasis
        me.Position = (x + vx, y + vy, z + vz)

    # 轴角平移
    def TranslationByAxis(self, me, value):
        # type: (Bladex._entity.B_PyEntity, float) -> ...
        q = Quaternion(self.Axis, value)
        loc = q * Vector(self.Direction)
        location = loc + Vector(self.LocationBasis)
        me.Position = location.to_tuple()

    # 旋转
    def Rotation(self, me, value):
        # type: (Bladex._entity.B_PyEntity, float) -> ...
        q = ToQuat(self.Direction, value)
        me.Orientation = QuatMul(q, self.OrientationBasis)

    # 缩放
    def Scale(self, me, value):
        # type: (Bladex._entity.B_PyEntity, float) -> ...
        me.Scale = value

    # 不透明度
    def Opacity(self, me, value):
        # type: (Bladex._entity.B_PyEntity, float) -> ...
        me.Alpha = value

    # 自发光
    def Emission(self, me, value):
        # type: (Bladex._entity.B_PyEntity, float) -> ...
        me.SelfIlum = value


class Channel(AnimEvent):
    def __init__(self, Name, Loop=0, Time2Live=0.0, OnComplete=(None, ())):
        AnimEvent.__init__(self)

        self.Name = Name
        self.Time2Live = Time2Live
        self.Loop = Loop
        self.OnComplete = OnComplete
        #
        self.Enabled = 1
        self.InitTime = 0
        self.StartTime = 0
        self.LoopCount = 0
        self.CurrentNode = 0
        self.Nodes = []  # type: list[Node]

    def AddNode(
        self,
        Start,
        End,
        Duration,
        Direction=(1, 0, 0),
        LocationBasis=None,
        OrientationBasis=None,
        Execute="Translation",
        BeforeFrame=(None, (), {}),
        OnComplete=(None, ()),
        Easing=LINEAR,
    ):
        node = Node(
            self.Name,
            Start,
            End,
            Duration,
            Direction,
            LocationBasis,
            OrientationBasis,
            Execute,
            BeforeFrame,
            OnComplete,
            Easing,
        )
        self.Nodes.append(node)
        return node

    def RemoveNode(self, node):
        if node in self.Nodes:
            self.Nodes.remove(node)

    def Reset(self):
        self.Enabled = 1
        self.LoopCount = 0
        AnimEvent.Reset(self)
        for node in self.Nodes:
            node.Reset()


class Animation(AnimEvent):
    def __init__(
        self,
        me,
        Time2Live=0.0,
        OnPlay=(None, ()),
        OnPause=(None, ()),
        OnComplete=(None, ()),
        Destroy=0,
        Timer="Timer60",
    ):
        AnimEvent.__init__(self)

        self.ObjId = ObjStore.GetNewId()
        ObjStore.ObjectsStore[self.ObjId] = self
        self.Name = me.Name  # type: str

        self.InitTime = 0
        self.PauseTime = 0
        self.Channels = []  # type: list[Channel]

        self.Time2Live = Time2Live
        # self.OnStart = OnStart
        self.OnPlay = OnPlay
        self.OnPause = OnPause
        self.OnComplete = OnComplete
        self.DestroyOnEnd = Destroy
        self.Timer = Timer

        self._running = False
        self._cancelled = False
        self._paused = False
        #
        InitDataField.Initialise(me, LM_Animation=self)

    def persistent_id(self):
        return self.ObjId

    def persistent_check(self):
        me = Bladex.GetEntity(self.Name)
        if not me:
            return 0
        return 1

    def __getstate__(self):
        return GameStateAux.SaveNewMembers(self)

    def __setstate__(self, parm):
        GameStateAux.LoadNewMembers(self, parm)
        ObjStore.ObjectsStore[self.ObjId] = self

    # ----------------------------------
    def Cancel(self):
        if not self._running:
            return
        
        # self._cancelled = True
        TimerAux.RemoveFromList(self.Timer, self._update)
        self.Reset()

    def Pause(self):
        if not self._paused:
            self._paused = True
            self.PauseTime = Bladex.GetTime()
            #
            if self.OnPause[0]:
                apply(self.OnPause[0], self.OnPause[1])

    def Resume(self):
        if self._paused:
            self._paused = False
            PauseTime = Bladex.GetTime() - self.PauseTime
            self.InitTime = self.InitTime + PauseTime
            for channel in self.Channels:
                channel.InitTime = channel.InitTime + PauseTime
                channel.StartTime = channel.StartTime + PauseTime
            #
            if self.OnPlay[0]:
                apply(self.OnPlay[0], self.OnPlay[1])

    def AddChannel(self, Loop=0, Time2Live=0.0, OnComplete=(None, ())):
        channel = Channel(self.Name, Loop, Time2Live, OnComplete)
        self.Channels.append(channel)
        return channel

    def RemoveChannel(self, channel):
        if channel in self.Channels:
            self.Channels.remove(channel)

    def Reset(self):
        self._running = False
        self._cancelled = False
        self._paused = False
        #
        AnimEvent.Reset(self)
        for channel in self.Channels:
            channel.Reset()

    # ----------------------------------
    def _update(self, time):
        if self._cancelled:
            return
        if self._paused:
            return
        me = Bladex.GetEntity(self.Name)
        if not me:
            TimerAux.RemoveFromList(self.Timer, self._update)
            return

        #
        elapsed = time - self.InitTime
        AnimEvent._update(self, elapsed)
        #
        nChannels = len(self.Channels)
        nDisabled = 0
        for idx in range(nChannels - 1, -1, -1):
            channel = self.Channels[idx]
            if not channel.Enabled:
                nDisabled = nDisabled + 1
                continue
            if channel.Time2Live > 0 and (time - channel.InitTime) >= channel.Time2Live:
                channel.Enabled = 0
                nDisabled = nDisabled + 1
                if channel.OnComplete[0]:
                    apply(channel.OnComplete[0], channel.OnComplete[1])
                continue
            #
            node = channel.Nodes[channel.CurrentNode]
            #
            elapsed = time - channel.InitTime
            AnimEvent._update(channel, elapsed)
            #
            elapsed = time - channel.StartTime
            progress = node._update(me, elapsed)
            if progress == 1.0:
                channel.CurrentNode = (channel.CurrentNode + 1) % len(channel.Nodes)
                channel.StartTime = time
                if channel.CurrentNode == 0:
                    if channel.Loop == -1 or channel.LoopCount < channel.Loop:
                        if channel.Loop > 0:
                            channel.LoopCount = channel.LoopCount + 1
                        for node in channel.Nodes:
                            node.Reset()
                    else:
                        # self.Channels.remove(channel)
                        channel.Enabled = 0
                        if channel.OnComplete[0]:
                            apply(channel.OnComplete[0], channel.OnComplete[1])
        #
        me = Bladex.GetEntity(self.Name)
        isDead = self.Time2Live > 0 and (time - self.InitTime) >= self.Time2Live
        if nDisabled == nChannels or isDead:
            self._running = False
            TimerAux.RemoveFromList(self.Timer, self._update)
            # if me:
            #     me.Data.LM_Animation = None
            if self.OnComplete[0]:
                apply(self.OnComplete[0], self.OnComplete[1])
            if self.DestroyOnEnd:
                if self.DestroyOnEnd == DESTROY_METHOD_BIN:
                    me.SubscribeToList("Pin")
                elif self.DestroyOnEnd == DESTROY_METHOD_REMOVE:
                    me.RemoveFromWorld()

    def run(self):
        me = Bladex.GetEntity(self.Name)
        if not me:
            return
        if self._running:
            return

        time = Bladex.GetTime()
        self.InitTime = time
        for channel in self.Channels:
            channel.InitTime = time
            channel.StartTime = time
        TimerAux.SubscribeToList(self.Timer, self._update)

        self._running = True


# ----------------------------------
