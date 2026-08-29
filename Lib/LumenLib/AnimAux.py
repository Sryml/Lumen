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
# LINEAR = "linear"
# EASE_OUT_SINE = "ease_out_sine"
# EASE_IN_SINE = "ease_in_sine"
# EASE_IN_QUAD = "ease_in_quad"
# EASE_OUT_QUAD = "ease_out_quad"
# EASE_IN_OUT = "ease_in_out"

# Destroy Methods
DESTROY_METHOD_BIN = 1
DESTROY_METHOD_REMOVE = 2


# ----------------------------------
def TrackEntity(
    self,
    track_name,
    track_loc=None,
    track_rot=None,
    track_dir=None,
    track_axis=None,
):
    track_ent = Bladex.GetEntity(track_name)  # type: Bladex._entity.B_PyEntity
    #
    if track_loc:
        mode, target, offset = track_loc
        x, y, z = offset
        if mode == "bone":
            if target == "":
                LocationBasis = track_ent.Rel2AbsPoint(x, y, z)
            else:
                LocationBasis = track_ent.Rel2AbsPoint(x, y, z, target)
        elif mode == "anchor":
            LocationBasis = track_ent.Rel2AbsPoint4Anchor(x, y, z, target)
        else:
            LocationBasis = (Vector(track_ent.Position) + Vector(offset)).to_tuple()

        self.LocationBasis = LocationBasis
    #
    if track_rot:
        mode, target, quat = track_rot
        if mode == "bone":
            if target == "":
                OrientationBasis = track_ent.Orientation
            else:
                x = track_ent.Rel2AbsVector(1, 0, 0, target)
                y = track_ent.Rel2AbsVector(0, 1, 0, target)
                z = track_ent.Rel2AbsVector(0, 0, 1, target)
                OrientationBasis = (
                    Matrix((x, y, z)).transposed().to_quaternion().to_tuple()
                )
        elif mode == "anchor":
            x = track_ent.GetDummyAxis(target, 1, 0, 0)
            y = track_ent.GetDummyAxis(target, 0, 1, 0)
            z = track_ent.GetDummyAxis(target, 0, 0, 1)
            OrientationBasis = Matrix((x, y, z)).transposed().to_quaternion().to_tuple()
        else:
            OrientationBasis = track_ent.Orientation
        OrientationBasis = QuatMul(OrientationBasis, quat)

        self.OrientationBasis = OrientationBasis
    #
    if track_dir and track_dir[0]:
        mode, target, offset = track_dir
        x, y, z = offset
        if mode == "bone":
            if target == "":
                Direction = track_ent.Rel2AbsVector(x, y, z)
            else:
                Direction = track_ent.Rel2AbsVector(x, y, z, target)
        elif mode == "anchor":
            Direction = track_ent.GetDummyAxis(target, x, y, z)

        self.Direction = Direction
    #
    if track_axis and track_axis[0]:
        mode, target, offset = track_axis
        x, y, z = offset
        if mode == "bone":
            if target == "":
                Axis = track_ent.Rel2AbsVector(x, y, z)
            else:
                Axis = track_ent.Rel2AbsVector(x, y, z, target)
        elif mode == "anchor":
            Axis = track_ent.GetDummyAxis(target, x, y, z)

        Axis = Vector(Axis).normalized().to_tuple()
        self.Axis = Axis


# ----------------------------------
class EASING:
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


class NODE_HANDLER:
    def __init__(self):
        self.TargetAttr = ""
        # 残影
        # self.Afterimage_Entities = []
        self.Afterimage_Target = ""
        self.Afterimage_LastTime = 0
        self.Afterimage_Interval = 0.1
        self.Afterimage_Time2Live = 0.7
        # self.Afterimage_HaloGradient = [] # TODO: Implement
        # 光环
        self.AuraParams = (0, 0, 1)

    # 位移
    def Displacement(self, time, me, value):
        # type: (Node, float, Bladex._entity.B_PyEntity, float) -> ...
        vx, vy, vz = Scale(self.Direction, value)  # type: ignore
        x, y, z = self.LocationBasis
        me.Position = (x + vx, y + vy, z + vz)

    # 角位移
    def AngularDisplacement(self, time, me, value):
        # type: (Node, float, Bladex._entity.B_PyEntity, float) -> ...
        q = Quaternion(self.Axis, value)
        loc = q * Vector(self.Direction)
        location = loc + Vector(self.LocationBasis)
        me.Position = location.to_tuple()

    # 旋转
    def Rotation(self, time, me, value):
        # type: (Node, float, Bladex._entity.B_PyEntity, float) -> ...
        q = ToQuat(self.Direction, value)
        me.Orientation = QuatMul(q, self.OrientationBasis)

    # 缩放
    def Scale(self, time, me, value):
        # type: (Node, float, Bladex._entity.B_PyEntity, float) -> ...
        me.Scale = value

    # 不透明度
    def Alpha(self, time, me, value):
        # type: (Node, float, Bladex._entity.B_PyEntity, float) -> ...
        me.Alpha = value

    # 自发光
    def SelfIlum(self, time, me, value):
        # type: (Node, float, Bladex._entity.B_PyEntity, float) -> ...
        me.SelfIlum = value

    # 亮度/强度
    def Intensity(self, time, me, value):
        # type: (Node, float, Bladex._entity.B_PyEntity, float) -> ...
        me.Intensity = value

    # 残影
    def AfterimageFX(self, time, me, value):
        # type: (Node, float, Bladex._entity.B_PyEntity, float) -> ...
        tar = Bladex.GetEntity(self.Afterimage_Target)
        if not tar:
            return
        if time - self.Afterimage_LastTime < self.Afterimage_Interval:
            return
        #
        self.Afterimage_LastTime = time
        x, y, z = tar.Position
        name = "%s%s" % (tar.Name, time)
        o = Bladex.CreateEntity(name, tar.Kind, x, y, z)
        o.ExclusionGroup = 1
        o.CastShadows = 0
        o.Orientation = tar.Orientation
        o.Alpha = 0.7
        o.SelfIlum = 0.5
        InitDataField.Initialise(o, Unselectable=1)
        # self.Afterimage_Entities.append(o)

        animation = Animation(o, Destroy=DESTROY_METHOD_BIN)

        channel = animation.AddChannel()
        node = channel.AddNode(
            o.Alpha, 0, self.Afterimage_Time2Live, Handler=NODE_HANDLER.Alpha
        )

        channel = animation.AddChannel()
        node = channel.AddNode(
            o.SelfIlum, 0, self.Afterimage_Time2Live, Handler=NODE_HANDLER.SelfIlum
        )

        animation.run()

    # 光环淡化缩放和亮度
    def FadeScaleIntensityAura(self, time, me, value):
        # type: (Node, float, Bladex._entity.B_PyEntity, ...) -> ...
        t = self.AuraParams
        me.SetAuraParams(value[0], value[1], value[2], t[0], t[1], t[2])

    # 任意属性
    def FromTargetAttr(self, time, me, value):
        # type: (Node, float, Bladex._entity.B_PyEntity, float) -> ...
        setattr(me, self.TargetAttr, value)


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

    def _update(self, time, elapsed):
        for event in self.Events:
            time, callback, pending = event
            if not pending:
                continue
            if time <= elapsed:
                apply(callback[0], (self,) + callback[1])
                event[2] = 0
                break

    def Reset(self):
        for event in self.Events:
            event[2] = 1


class Node(AnimEvent, EASING, NODE_HANDLER):
    def __init__(
        self,
        Name,
        Start,
        End,
        Duration,
        Direction=(1, 0, 0),
        LocationBasis=None,
        OrientationBasis=None,
        Handler=NODE_HANDLER.Displacement,
        BeforeFrame=(None, (), {}),
        AfterFrame=(None, (), {}),
        OnComplete=(None, ()),
        Easing=EASING.linear,
    ):
        AnimEvent.__init__(self)
        NODE_HANDLER.__init__(self)

        self.Name = Name
        me = Bladex.GetEntity(self.Name)
        if len(BeforeFrame) < 3:
            BeforeFrame = (BeforeFrame[0], BeforeFrame[1], {})
        if len(AfterFrame) < 3:
            AfterFrame = (AfterFrame[0], AfterFrame[1], {})
        #
        self.Start = Start
        self.End = End
        self.Duration = Duration
        self.Handler = Handler
        self.BeforeFrame = BeforeFrame
        self.AfterFrame = AfterFrame
        self.OnComplete = OnComplete
        self.Easing = Easing
        #
        if LocationBasis is None:
            LocationBasis = me.Position
        if OrientationBasis is None:
            OrientationBasis = getattr(me, "Orientation", (1, 0, 0, 0))

        self.Direction = Direction  # type: ...
        self.LocationBasis = LocationBasis  # type: ...
        self.OrientationBasis = OrientationBasis  # type: ...
        #
        self.elapsed = 0
        self.progress = 0
        self.eased_progress = 0
        if is_sequence(Start):
            self.Period = []
            for s, e in zip(Start, End):
                self.Period.append(e - s)
        else:
            self.Period = End - Start
        #
        self.Axis = (1, 0, 0)

    def _update(self, time, me, elapsed):
        progress = min(elapsed / self.Duration, 1.0)
        eased_progress = self.Easing(self, progress)
        if progress == 1.0:
            value = self.End
        else:
            if is_sequence(self.Start):
                value = []
                for idx in range(len(self.Start)):
                    value.append(self.Start[idx] + self.Period[idx] * eased_progress)
            else:
                value = self.Start + self.Period * eased_progress

        self.elapsed = elapsed
        self.progress = progress
        self.eased_progress = eased_progress

        if self.BeforeFrame[0]:
            apply(
                self.BeforeFrame[0], (self,) + self.BeforeFrame[1], self.BeforeFrame[2]
            )
        self.Handler(self, time, me, value)
        #
        AnimEvent._update(self, time, elapsed)
        #
        if self.AfterFrame[0]:
            apply(self.AfterFrame[0], (self,) + self.AfterFrame[1], self.AfterFrame[2])
        if progress == 1.0:
            if self.OnComplete[0]:
                apply(self.OnComplete[0], (self,) + self.OnComplete[1])

        return progress

    # def Handler(self, me, value):
    #     pass


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
        Start=0.0,  # type: float | tuple | list
        End=1.0,  # type: float | tuple | list
        Duration=1.0,
        Direction=(1, 0, 0),
        LocationBasis=None,
        OrientationBasis=None,
        Handler=NODE_HANDLER.Displacement,
        BeforeFrame=(None, (), {}),
        AfterFrame=(None, (), {}),
        OnComplete=(None, ()),
        Easing=EASING.linear,
    ):
        node = Node(
            self.Name,
            Start,
            End,
            Duration,
            Direction,
            LocationBasis,
            OrientationBasis,
            Handler,
            BeforeFrame,
            AfterFrame,
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
        Timer="Timer60",
        Destroy=0,
    ):
        AnimEvent.__init__(self)

        # self.ObjId = ObjStore.GetNewId()
        # ObjStore.ObjectsStore[self.ObjId] = self
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

    # def persistent_id(self):
    #     return self.ObjId

    # def persistent_check(self):
    #     me = Bladex.GetEntity(self.Name)
    #     if not me:
    #         return 0
    #     return 1

    # def __getstate__(self):
    #     return GameStateAux.SaveNewMembers(self)

    # def __setstate__(self, parm):
    #     GameStateAux.LoadNewMembers(self, parm)
    #     ObjStore.ObjectsStore[self.ObjId] = self

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
                apply(self.OnPause[0], (self,) + self.OnPause[1])

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
                apply(self.OnPlay[0], (self,) + self.OnPlay[1])

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
        AnimEvent._update(self, time, elapsed)
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
                    apply(channel.OnComplete[0], (channel,) + channel.OnComplete[1])
                continue
            #
            node = channel.Nodes[channel.CurrentNode]
            #
            elapsed = time - channel.InitTime
            AnimEvent._update(channel, time, elapsed)
            #
            elapsed = time - channel.StartTime
            progress = node._update(time, me, elapsed)
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
                            apply(
                                channel.OnComplete[0],
                                (channel,) + channel.OnComplete[1],
                            )
        #
        me = Bladex.GetEntity(self.Name)
        isDead = self.Time2Live > 0 and (time - self.InitTime) >= self.Time2Live
        if nDisabled == nChannels or isDead:
            self._running = False
            TimerAux.RemoveFromList(self.Timer, self._update)
            # if me:
            #     me.Data.LM_Animation = None
            if self.OnComplete[0]:
                apply(self.OnComplete[0], (self,) + self.OnComplete[1])
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


def _example():
    import InitDataField, GenFX
    from LumenLib import AnimAux

    # fmt: off
    for dir, kind, ptrl_type in [(1, "Gema", "GreenTrail"), (-1, "Gemaroja", "RedTrail")]:
        o = Bladex.CreateEntity(kind, kind, 0, 0, 0)
        InitDataField.Initialise(o, Unselectable=1)
        o.CastShadows = 0
        o.SelfIlum = 0.2
        o.Alpha = 0.9
        o.RasterMode = "AdditiveAlpha"
        prtlsys = GenFX.AddParticles(o.Name, ptrl_type, 400, 0, 0, 0.01, 19, 0)
        # Create Animation
        animation = AnimAux.Animation(o)
        TrackEntity = (AnimAux.TrackEntity, ("Player1", ("bone", "Chest", (0, 0, 0)), None, ("bone", "", (0, 600, 0)), ("bone", "", (-1, 0, 1 * dir))), {})
        #
        channel = animation.AddChannel(Loop=-1)
        node = channel.AddNode(0, AnimAux.two_pi, 1.3, Handler=AnimAux.NODE_HANDLER.AngularDisplacement, BeforeFrame=TrackEntity)
        animation.run()
    # fmt: on


"""
if 1:
    from LumenLib import AnimAux
    AnimAux._example()
"""
