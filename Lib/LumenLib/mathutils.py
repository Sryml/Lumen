#  _    _   _ __  __ _____ _   _
# | |  | | | |  \/  | ____| \ | |
# | |  | | | | |\/| |  _| |  \| |
# | |__| |_| | |  | | |___| |\  |
# |_____\___/|_|  |_|_____|_| \_|
#

import B3DLib
import math

from Lumenx import printx

#
import typing

if typing.TYPE_CHECKING:
    apply = lambda fn, args=(), kwds={}: None
    execfile = lambda filename, globals=None, locals=None: None
    cmp = lambda x, y: None


# -------------------------------
epsilon = 1e-5
epsilon2 = 1 - epsilon


# -------------------------------
def DiffAngle(*args):
    return apply(B3DLib.DiffAngle, args)


def GetEntity2EntityAngle(*args):
    return apply(B3DLib.GetEntity2EntityAngle, args)


def GetXZAngle(*args):
    return apply(B3DLib.GetXZAngle, args)


def GetXZDistance(*args):
    return apply(B3DLib.GetXZDistance, args)


def GetYAngle(*args):
    return apply(B3DLib.GetYAngle, args)


def Modulo(*args):
    return apply(B3DLib.Modulo, args)


def Normalize(*args):
    return apply(B3DLib.Normalize, args)


def Pos2PosXZAngle(*args):
    return apply(B3DLib.Pos2PosXZAngle, args)


def Pos2PosYAngle(*args):
    return apply(B3DLib.Pos2PosYAngle, args)


def Scale(*args):
    return apply(B3DLib.Scale, args)


# -------------------------------


def ToQuat(axis, angle):
    angle = angle * 0.5
    w = math.cos(angle)
    x = axis[0] * math.sin(angle)
    y = axis[1] * math.sin(angle)
    z = axis[2] * math.sin(angle)
    return (w, x, y, z)


def QuatMul(q2, q1):
    w = q2[0] * q1[0] - q2[1] * q1[1] - q2[2] * q1[2] - q2[3] * q1[3]
    x = q2[0] * q1[1] + q2[1] * q1[0] + q2[2] * q1[3] - q2[3] * q1[2]
    y = q2[0] * q1[2] - q2[1] * q1[3] + q2[2] * q1[0] + q2[3] * q1[1]
    z = q2[0] * q1[3] + q2[1] * q1[2] - q2[2] * q1[1] + q2[3] * q1[0]
    return (w, x, y, z)


def Dot(v1, v2):
    if len(v1) == len(v2) == 3:
        return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]
    elif len(v1) == len(v2) == 4:
        return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2] + v1[3] * v2[3]
    else:
        printx(ValueError, "Input vectors or quaternions must be of length 3 or 4.")
        raise ValueError


def Cross(v1, v2):
    if len(v1) == len(v2) == 3:
        return (
            v1[1] * v2[2] - v2[1] * v1[2],
            v1[2] * v2[0] - v2[2] * v1[0],
            v1[0] * v2[1] - v2[0] * v1[1],
        )
    printx(ValueError, "Input vectors must be of length 3.")
    raise ValueError


def Degrees(x):
    """Convert angle x from radians to degrees."""
    return x / math.pi * 180.0


def Radians(x):
    """Convert angle x from degrees to radians."""
    return x / 180.0 * math.pi
