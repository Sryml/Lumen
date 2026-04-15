#  _    _   _ __  __ _____ _   _
# | |  | | | |  \/  | ____| \ | |
# | |  | | | | |\/| |  _| |  \| |
# | |__| |_| | |  | | |___| |\  |
# |_____\___/|_|  |_|_____|_| \_|
#
import AuxFuncs
import Bladex
import Lumenx
import math
import sys
import GameState
import GameStateAux

from LumenLib.BUtils import ToQuat, QuatMul

# ----------------------------------
TRAJECTORY_UID = "69DE623E"
TRAJECTORYS = []  # type: list[Bladex._entity.B_PyEntity]
DUMMY_T = None  # type: Bladex._entity.B_PyEntity # type: ignore

# GRAVITY = 9800  # Gravity acceleration
# C = 0.5  # # Constant for mass influence coefficient
# MASS = 0.503  # Mass of the arrow ( unit: kg )

# SECTOR_LENGTH = 900  # Length of each section
# INTERVAL = 900
# MAX_SECTIONS = 200
# START_DISTANCE = 2000
# ----------------------------------


def init():
    global DUMMY_T
    name = "%s_d" % TRAJECTORY_UID
    dummy = Bladex.GetEntity(name)
    if not dummy:
        dummy = Bladex.CreateEntity(name, "Trajectory", 0, 0, 0, "Physic")
        dummy.SendSectorMsgs = 0
        dummy.ExclusionMask = 0
        dummy.CastShadows = 0
        dummy.Alpha = 0.0
    DUMMY_T = dummy  # type: ignore
    #
    for i in TRAJECTORYS:
        i.RemoveFromWorld()


class ClsTrajectory:
    arrow = None  # type: Bladex._entity.B_PyEntity # type: ignore
    vector = None  # type: tuple # type: ignore
    g = 9800  # Gravity acceleration
    C = 0.5  # # Constant for mass influence coefficient
    m = 0.503  # Mass of the arrow ( unit: kg )

    sector_length = 900  # Length of each section
    interval = 900
    max_sections = 200
    start_distance = 2000

    def __init__(self):
        self.AfterFrameFuncName = Lumenx.GetNSaveName()
        self.active = 0

    # 获取子轨迹
    def GetSubTrajectory(
        self, InitPos, v0_x, v0_y, v0_z, g_prime, h_speed, time, length
    ):
        x = v0_x * time
        z = v0_z * time
        y = v0_y * time + 0.5 * g_prime * time**2

        v0_y_prime = v0_y + g_prime * time
        v = AuxFuncs.Normalize((v0_x, v0_y_prime, v0_z))
        v = AuxFuncs.Scale(v, length)
        pitch = math.atan2(v0_y_prime, h_speed)  # 俯仰角

        pos = InitPos[0] + x, InitPos[1] + y, InitPos[2] + z
        tpos = pos[0] + v[0], pos[1] + v[1], pos[2] + v[2]

        return pos, tpos, pitch

    # 碰撞检测并隐藏剩余弹道
    def TestHit(self, pos, q, i):
        dummy = DUMMY_T
        dummy.Position = pos[0], pos[1], pos[2]
        dummy.Orientation = q
        dummy.RemoveFromWorld()
        if dummy.TestHit:
            # 隐藏剩余弹道
            for j in range(i + 1, len(TRAJECTORYS)):
                TRAJECTORYS[j].RemoveFromWorld()
            return 1
        return 0

    # 反激活
    def Deactivate(self):
        self.active = 0

    # 激活
    def Activate(self, arrow, vector, m=0.501):
        if self.active or Lumenx.GetConfig("ArcheryTrajectory") == "Disabled":
            return

        self.active = 1

        self.arrow = arrow
        self.vector = vector
        self.m = m
        Bladex.SetAfterFrameFunc(self.AfterFrameFuncName, self.Update)

    # 更新箭的轨迹
    def Update(self, t):
        arrow = self.arrow
        vector = self.vector
        m = self.m

        if arrow.Parent and Bladex.GetEntity(arrow.Parent).AnimName != "b3":
            self.active = 0
        if not self.active:
            Bladex.RemoveAfterFrameFunc(self.AfterFrameFuncName)
            for i in TRAJECTORYS:
                i.RemoveFromWorld()
            return

        k = self.C / m  # Mass influence coefficient
        g_prime = self.g * k  # Correction for gravity acceleration

        vx, vy, vz = arrow.Rel2AbsVector(vector[0], vector[1], vector[2])
        InitPos = arrow.Position
        # 重复的计算
        # v0 = AuxFuncs.Module((vx, vy, vz))
        # theta = math.atan2(vy, (vx**2 + vz**2) ** 0.5)
        # alpha = math.atan2(vz, vx)

        # v0_x = v0 * math.cos(theta) * math.cos(alpha)
        # v0_z = v0 * math.cos(theta) * math.sin(alpha)
        # v0_y = v0 * math.sin(theta)
        #
        v0_x = vx
        v0_z = vz
        v0_y = vy

        yaw = math.atan2(v0_z, v0_x)  # 航向角

        # horizontal speed
        h_speed = AuxFuncs.Module((v0_x, 0, v0_z))
        time = self.start_distance / h_speed

        alpha = 0.65
        t_num = len(TRAJECTORYS)
        for i in range(self.max_sections):
            pos, tpos, pitch = self.GetSubTrajectory(
                InitPos, v0_x, v0_y, v0_z, g_prime, h_speed, time, self.sector_length
            )

            # Rotate pitch first and then rotate yaw
            q1 = ToQuat((0, 0, 1), pitch)
            q2 = ToQuat((0, -1, 0), yaw)
            q = QuatMul(q2, q1)
            if i >= t_num:
                o = Bladex.CreateEntity(
                    "%s_%s" % (TRAJECTORY_UID, i), "Trajectory", 0, 0, 0
                )
                o.SendSectorMsgs = 0
                o.CastShadows = 0
                o.SelfIlum = 0.4
                o.Alpha = alpha
                o.ExclusionGroup = 1
                TRAJECTORYS.append(o)  # type: ignore
                if i < 10:
                    o.Alpha = min(i * 0.05 + 0.15, alpha)

            o = TRAJECTORYS[i]
            o.Position = pos[0], pos[1], pos[2]
            o.Orientation = q
            o.PutToWorld()

            # 碰撞检测
            if self.TestHit(pos, q, i):
                break

            time = (
                AuxFuncs.Module((tpos[0] - InitPos[0], 0, tpos[2] - InitPos[2]))
                / h_speed
            )
            pos, tpos, pitch = self.GetSubTrajectory(
                InitPos, v0_x, v0_y, v0_z, g_prime, h_speed, time, self.interval
            )
            q1 = ToQuat((0, 0, 1), pitch)
            q = QuatMul(q2, q1)
            # 碰撞检测
            if self.TestHit(pos, q, i):
                break

            time = (
                AuxFuncs.Module((tpos[0] - InitPos[0], 0, tpos[2] - InitPos[2]))
                / h_speed
            )


# ----------------------------------

Trajectory = ClsTrajectory()


####
#### For testing
####
TrackArrowCount = 0


# 克隆轨迹
def CloneTrajectory(trajectory):
    global TrackArrowCount
    if TrackArrowCount > 6:
        return
    for i in trajectory.trajectory:
        if not i.InWorld:
            break
        o = Bladex.CreateEntity(i.Name + "C", "Trajectory", 0, 0, 0)
        o.CastShadows = 0
        o.SelfIlum = 0.4
        o.Alpha = 0.9
        o.ExclusionGroup = 1
        o.Position = i.Position
        o.Orientation = i.Orientation


def ResetCam():
    cam = Bladex.GetEntity("Camera")
    cam.SetPersonView("Player1")
    cam.Cut()


# 跟踪箭头
def TrackArrow(o):
    global TVector, Vector, Arrow, TrackArrowCount
    TrackArrowCount = TrackArrowCount + 1
    if TrackArrowCount > 6:
        return
    Bladex.SetTimeSpeed(0.2)
    global TVector, Vector, Arrow
    Arrow = o
    cam = Bladex.GetEntity("Camera")
    cam.TType = cam.SType = 0
    TVector = (
        cam.TPos[0] - cam.Position[0],
        cam.TPos[1] - cam.Position[1],
        cam.TPos[2] - cam.Position[2],
    )
    Vector = (
        cam.Position[0] - Arrow.Position[0],
        cam.Position[1] - Arrow.Position[1],
        cam.Position[2] - Arrow.Position[2],
    )
    Bladex.SetAfterFrameFunc("TrackArrow", TrackArrowFunc)


def TrackArrowFunc(t):
    global TVector, Vector, Arrow
    cam = Bladex.GetEntity("Camera")
    x, y, z = Arrow.Position
    x, y, z = x + Vector[0], y + Vector[1], z + Vector[2]
    cam.Position = x, y, z
    cam.TPos = x + TVector[0], y + TVector[1], z + TVector[2]
    if Arrow.Velocity == (0.0, 0.0, 0.0):
        Bladex.SetTimeSpeed(1.0)
        Bladex.RemoveAfterFrameFunc("TrackArrow")
        Bladex.AddScheduledFunc(Bladex.GetTime() + 1.6, ResetCam, ())


# ----------------------------------
def SaveData(filename):
    GameStateAux.SaveData(filename, TRAJECTORYS)


def LoadData(filename):
    global TRAJECTORYS
    TRAJECTORYS = GameStateAux.LoadData(filename)


GameState.ModulesToBeSaved.append(sys.modules[__name__])

Bladex.AddScheduledFunc(-1, init, ())

"""
import Trajectory
trajectory = Trajectory.Trajectory()

def EndDrawBowEventHandler(EntityName, EventName):
    ...

    trajectory.active=0
    Trajectory.CloneTrajectory(trajectory)
    arrow.Fly(vx,vy,vz)
    Trajectory.TrackArrow(arrow)

    ...

    me.LaunchAnmType ("b3")
    if not trajectory.active:
        arrow= Bladex.GetEntity(me.InvRight)
        trajectory.Activate(arrow, (0,0,-40000))
"""

"""
a1 = Bladex.CreateEntity("a1", "Trajectory", 0, -8389, -93554.0, "Physic")
a2 = Bladex.CreateEntity("a2", "Manzana", 0, -8389 - 400, -93554.0, "Physic")
a2.ExclusionMask = 0
a2.Impulse(0, 100, 0)
if 1:

    a1 = Bladex.CreateEntity("a1", "Trajectory", 0, -8389, -93554.0, "Physic")
    a2 = Bladex.CreateEntity("a1", "Flecha", 0, -8389, -93554.0, "Physic")

    o = Bladex.CreateEntity(
        "arrow", "Flecha", 34355.7757963, -11276.8357746, -34287, "Weapon"
    )
    o.Rotate(-1, 0, 0, math.pi - 0.4)
    t = Trajectory()
    t.Activate(o, (0, 0, -20000))

    t.trajectory[0].SimpleSections

    vx, vy, vz = o.Rel2AbsVector(0, 0, -40000)
    o.Fly(vx, vy, vz)

if 1:
    import BBLib

    # BBLib.ReadMMP("../../3dobjs/Trajectory.mmp")
    Bladex.ReadBitMap("../../3dobjs/Trajectory.bmp", "Trajectory")
    BBLib.ReadBOD("../../3dobjs/Trajectory.bod")
    BBLib.LoadBOD("Trajectory")
if 1:
    x, y, z = char.Position
    t = Bladex.CreateEntity("Trajectory", "Trajectory", x - 100, y, z, "Physic")
    t.ExclusionMask = 0
    t.ExclusionGroup = 1
    t1.Impulse(0, 200, 0)
    x, y, z = char.Position
    o = Bladex.CreateEntity("Trajectory", "Eclipse", x, y, z, "Weapon")
    o.Rotate(1, 0, 0, math.pi / 2)
    # TestHit

    t.Scale
    # t.ExclusionMask
    # t.SelfIlum = 1

# 初始参数
# x, y = 0, 0
# v0 = 50  # 初速度
# theta = 45  # 射角（角度制）
g = 9800  # 重力加速度
m = 0.5  # 箭的质量（单位：kg）
C = 0.5  # 质量影响系数的常数（可调）
t = 0  # 时间
dt = 0.1  # 时间步长

# 计算质量影响系数
k = C / m
g_prime = g * k  # 修正重力加速度

vx, vy, vz = 1, 1, 1  # XXX
v0 = AuxFuncs.Module((vx, vy, vz))
theta = math.atan2(vy, (vx**2 + vz**2) ** 0.5)
alpha = math.atan2(vz, vx)

vx1 = v0 * math.cos(theta) * math.cos(alpha)
vz1 = v0 * math.cos(theta) * math.sin(alpha)
vy1 = v0 * math.sin(theta)

x = vx1 * t
z = vz1 * t
y = vy1 * t - 0.5 * g * t**2


def fly(o, pos_init, t, v0_x, v0_y, v0_z, start_time):
    g = 9800
    C = 0.5
    m = 0.503
    k = C / m
    g_prime = g * k  # 修正重力加速度
    dt = 1 / 30.0
    t = Bladex.GetTime() - start_time

    x = v0_x * t
    z = v0_z * t
    y = v0_y * t + 0.5 * g_prime * t**2

    v0_y_prime = v0_y + g_prime * t

    v1 = (0, 0, -1)
    v2 = AuxFuncs.Normalize((v0_x, v0_y_prime, v0_z))
    axis = AuxFuncs.Normalize(
        (
            v1[1] * v2[2] - v2[1] * v1[2],
            v1[2] * v2[0] - v2[2] * v1[0],
            v1[0] * v2[1] - v2[0] * v1[1],
        )
    )
    angle = math.acos(v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2])

    # q1 = (0, 0, 0, -1)
    q = toquat(axis, angle)
    # q = quat_mult(q2,q1)

    # q1 = 0,0, v0_x,v0_y_prime,v0_z
    # theta = math.atan2(v0_y_prime , (v0_x**2 + v0_z**2)**0.5)
    # alpha = math.atan2(z , x)

    # q1 = toquat((0,-1,0), 90)
    # q2 = toquat((0,0,1), theta / math.pi * 180.0)
    # q3 = toquat((0,-1,0), alpha / math.pi * 180.0)
    # q = quat_mult(q2,q1)
    # q = quat_mult(q3,q)

    if t != 0:
        o.Orientation = q
    # if t < 0.2:
    #     print axis, angle / math.pi * 180.0
    #     print q2
    pos = pos_init[0] + x, pos_init[1] + y, pos_init[2] + z
    test_pos = o.Rel2AbsPoint(0, 0, -2000)
    s = Bladex.GetSector(test_pos[0], test_pos[1], test_pos[2])
    if s:
        o.Position = pos
        Bladex.AddScheduledFunc(
            Bladex.GetTime() + 1 / 60.0,
            fly,
            (o, pos_init, t + dt, v0_x, v0_y, v0_z, start_time),
        )
    else:
        arrow.Stop()


def Reset(o, pos, q):
    char.Unlink(o)
    o.Orientation = q
    o.Position = pos


if 1:
    # create_arrow(-10000)
    # o = Bladex.CreateEntity("arrow", "Flecha", 34355.7757963, -11276.8357746, -34287,"Arrow")
    o.Stop()
    o.Position = 34355.7757963, -11276.8357746, -34287
    o.Orientation = 1, 0, 0, 0
    o.Rotate(-1, 0, 0, math.pi - 0.4)
    vx, vy, vz = o.Rel2AbsVector(0, 0, -40000)
    o.Fly(vx, vy, vz)


def start_fly(o1, pos, t, v0_x, v0_y, v0_z, F):
    global arrow
    fly(o1, pos, t, v0_x, v0_y, v0_z, Bladex.GetTime())
    arrow.Stop()
    arrow.Position = 34355.7757963, -11276.8357746, -34287
    arrow.Orientation = 1, 0, 0, 0
    arrow.Rotate(-1, 0, 0, math.pi - 0.4)
    vx, vy, vz = arrow.Rel2AbsVector(0, 0, F)
    arrow.Fly(vx, vy, vz)


def create_arrow(F):
    import math
    import AuxFuncs
    import Bladex
    import Actions

    o = Bladex.CreateEntity(
        "arrow", "Flecha", 34355.7757963, -11276.8357746, -34287, "Weapon"
    )
    o.Rotate(-1, 0, 0, math.pi - 0.4)

    vx, vy, vz = o.Rel2AbsVector(0, 0, F)  # -40000
    v0 = AuxFuncs.Module((vx, vy, vz))
    theta = math.atan2(vy, (vx**2 + vz**2) ** 0.5)
    alpha = math.atan2(vz, vx)

    v0_x = v0 * math.cos(theta) * math.cos(alpha)
    v0_z = v0 * math.cos(theta) * math.sin(alpha)
    v0_y = v0 * math.sin(theta)
    pos = o.Position
    q = o.Orientation

    trail = Bladex.GetTrailType("Default")
    trail.Time2Live = 60.0
    trail.Color = 200, 0, 0
    trail.Transparency = 0.1
    trail.ShrinkFactor = 0.0

    inv = char.GetInventory()
    inv.LinkRightHand(o.Name)
    o.MessageEvent(Actions.MESSAGE_START_TRAIL, 0, 0)
    Bladex.AddScheduledFunc(Bladex.GetTime() + 0.03, Reset, (o, pos, q))
    Bladex.AddScheduledFunc(
        Bladex.GetTime() + 0.1, start_fly, (o, pos, 0, v0_x, v0_y, v0_z, F)
    )

    # fly(o,pos,0,vx1,vy1,vz1)


if 1:
    trail = Bladex.GetTrailType("Default")
    trail.Time2Live = 30.0
    trail.Color = 200, 0, 0
    trail.Transparency = 0.7
    trail.ShrinkFactor = 0.0


"""

"""
# 角度转换为弧度
theta_rad = radians(theta)

# 初始速度分量
v_x = v0 * cos(theta_rad)
v_y = v0 * sin(theta_rad)

# 计算质量影响系数
k = C / m
g_prime = g * k  # 修正重力加速度

# 模拟箭的运动
while y >= 0:
    # 更新位置
    x = v_x * t
    y = v_y * t - 0.5 * g_prime * t**2
    
    # 递增时间
    t += dt
    
    # 渲染箭的位置
    render_arrow(x, y)

if 1:
    pitch = AuxFuncs.Normalize((1,-1, 0.0))
    q = (0.0,) + pitch
    mod = (q[0]**2 + q[1]**2 + q[2]**2 + q[3]**2) ** 0.5
    q = (q[0]/mod, q[1]/mod, q[2]/mod, q[3]/mod)
if 1:
    pitch = math.atan2(-1, 1)
    q2 = ToQuat((0,0,1), pitch)
    yaw = math.atan2(1, 1)
    q1 = ToQuat((0, -1, 0), yaw)
    w = q1[0] * q2[0] - q1[1] * q2[1] - q1[2] * q2[2] - q1[3] * q2[3]
    x = q1[0] * q2[1] + q1[1] * q2[0] + q1[2] * q2[3] - q1[3] * q2[2]
    y = q1[0] * q2[2] - q1[1] * q2[3] + q1[2] * q2[0] + q1[3] * q2[1]
    z = q1[0] * q2[3] + q1[1] * q2[2] - q1[2] * q2[1] + q1[3] * q2[0]
    t.Orientation=w,x,y,z
"""
