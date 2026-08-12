#  _    _   _ __  __ _____ _   _
# | |  | | | |  \/  | ____| \ | |
# | |  | | | | |\/| |  _| |  \| |
# | |__| |_| | |  | | |___| |\  |
# |_____\___/|_|  |_|_____|_| \_|
#

import B3DLib
import math
import types
import re
import string

from Lumenx import printx
from math import pi

#
import typing

if typing.TYPE_CHECKING:
    apply = lambda fn, args=(), kwds={}: None
    execfile = lambda filename, globals=None, locals=None: None
    cmp = lambda x, y: None

# -------------------------------
two_pi = 2 * pi
epsilon = 1e-5
epsilon2 = 1 - epsilon
_component_pattern = re.compile(r'^[xyzw]+$')
_components = ["x", "y", "z", "w"]
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

def _is_sequence(value):
    return type(value) in (types.ListType, types.TupleType)


def _copy_sequence(value):
    result = []
    i = 0
    while i < len(value):
        v = value[i]
        # 统一零的符号，避免后续比较和序列化出现 -0.0。
        if v == 0:
            v = 0.0
        result.append(v)
        i = i + 1
    return result


class Vector:
    def __init__(self, values=(0, 0, 0)):
        if isinstance(values, Vector):
            values = values.values
        
        if not _is_sequence(values):
            raise TypeError, "Vector requires a tuple or list"  # type: ignore

        if len(values) == 0:
            raise ValueError, "Vector cannot be empty"  # type: ignore

        self.values = _copy_sequence(values)
        self.size = len(self.values)

    # def __getstate__(self):
    #     pass

    # def __setstate__(self, parm):
    #     pass

    def copy(self):
        return Vector(self.values)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        return self.values[index]

    def __setitem__(self, index, value):
        # -0.0 to 0.0
        if value == 0:
            value = 0.0
        self.values[index] = value

    def __getattr__(self, name):
        if len(name) <= 4 and _component_pattern.match(name):
            result = []
            for n in name:
                index = _components.index(n)
                if index >= self.size:
                    raise AttributeError, "Vector has no component '%s'" % n  # type: ignore
                result.append(self.values[index])
            if len(result) == 1:
                return result[0]
            else:
                return Vector(result)

        raise AttributeError, "Vector has no attribute '%s'" % name  # type: ignore

    def __setattr__(self, name, value):
        name_len = len(name)
        if name_len <= 4 and _component_pattern.match(name):
            if name_len == 1:
                index = _components.index(name[0])
                if index >= self.size:
                    raise AttributeError, "Vector has no component '%s'" % name  # type: ignore
                if value == 0:
                    value = 0.0
                self.values[index] = value
            else:
                for i in range(name_len):
                    index = _components.index(name[i])
                    if index >= self.size:
                        raise AttributeError, "Vector has no component '%s'" % name[i]  # type: ignore
                    component = value[i]
                    if component == 0:
                        component = 0.0
                    self.values[index] = component
        elif name == "values" or name == "size":
            self.__dict__[name] = value
        else:
            raise AttributeError, "Vector has no attribute '%s'" % name  # type: ignore

    def __cmp__(self, other):
        if isinstance(other, Vector):
            other = other.to_tuple()
        return cmp(self.to_tuple(), other)

    def __str__(self):
        return "<Vector %s>" % repr(self.to_tuple(1))

    def __repr__(self):
        return "Vector(%s)" % repr(tuple(self.values))

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError, "Vector can only be added to Vector"  # type: ignore

        if self.size != other.size:
            raise ValueError, "Vector sizes do not match"  # type: ignore

        result = []
        i = 0
        while i < self.size:
            result.append(self.values[i] + other.values[i])
            i = i + 1

        return Vector(result)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError, "Vector can only be subtracted from Vector"  # type: ignore

        if self.size != other.size:
            raise ValueError, "Vector sizes do not match"  # type: ignore

        result = []
        i = 0
        while i < self.size:
            result.append(self.values[i] - other.values[i])
            i = i + 1

        return Vector(result)

    def __neg__(self):
        result = []
        i = 0
        while i < self.size:
            result.append(-self.values[i])
            i = i + 1

        return Vector(result)

    def __mul__(self, other):
        if type(other) in (types.IntType, types.FloatType):
            result = []
            i = 0
            while i < self.size:
                result.append(self.values[i] * other)
                i = i + 1

            return Vector(result)

        if isinstance(other, Vector):
            if self.size != other.size:
                raise ValueError, "Vector sizes do not match"  # type: ignore

            result = []
            i = 0
            while i < self.size:
                result.append(self.values[i] * other.values[i])
                i = i + 1

            return Vector(result)

        raise TypeError, "Invalid Vector multiplication"  # type: ignore

    def __rmul__(self, other):
        return self * other

    def __div__(self, other):
        if other == 0:
            raise ZeroDivisionError, "division by zero"  # type: ignore

        result = []
        i = 0
        while i < self.size:
            result.append(self.values[i] / other)
            i = i + 1

        return Vector(result)

    def length_squared(self):
        return self.dot(self)

    def length(self):
        return math.sqrt(self.length_squared())

    def normalize(self):
        length = self.length()

        if length == 0:
            # 保持旧行为：零向量归一化后仍为零向量。
            return

        i = 0
        while i < self.size:
            self.values[i] = self.values[i] / length
            i = i + 1

    def normalized(self):
        result = self.copy()
        result.normalize()
        return result

    def dot(self, other):
        if isinstance(other, Vector):
            if self.size != other.size:
                raise ValueError, "Vector sizes do not match"  # type: ignore

            result = 0
            i = 0
            while i < self.size:
                result = result + self.values[i] * other.values[i]
                i = i + 1

            return result

        raise TypeError, "Invalid Vector dot product"  # type: ignore

    def cross(self, other):
        if not isinstance(other, Vector):
            raise TypeError, "Vector cross product requires a Vector"  # type: ignore

        if self.size != 3 or other.size != 3:
            raise ValueError, "Cross product requires 3D vectors"  # type: ignore

        return Vector((
            self.values[1] * other.values[2] -
            self.values[2] * other.values[1],

            self.values[2] * other.values[0] -
            self.values[0] * other.values[2],

            self.values[0] * other.values[1] -
            self.values[1] * other.values[0]
        ))

    def angle(self, other):
        value = self.dot(other)
        denominator = self.length() * other.length()

        if denominator == 0:
            raise ValueError, "Cannot calculate angle with zero vector"  # type: ignore

        value = value / denominator

        if value > 1:
            value = 1

        if value < -1:
            value = -1

        return math.acos(value)

    def to_tuple(self, precision=-1):
        if precision == -1:
            return tuple(self.values)
        return tuple(map(lambda x, precision=precision: round(x, precision), self.values))

    def _to_xd(self, size):
        result = []
        for i in range(size):
            if i < self.size:
                v = self.values[i]
            else:
                v = 1
            result.append(v)

        return Vector(result)

    def to_2d(self):
        return self._to_xd(2)

    def to_3d(self):
        return self._to_xd(3)

    def to_4d(self):
        return self._to_xd(4)

    def to_matrix(self):
        if self.size != 3:
            raise ValueError, "Matrix requires a 3D vector"  # type: ignore

        matrix = Matrix()
        matrix.SetTranslation(self)
        return matrix


class Quaternion:
    def __init__(self, values=(1,0,0,0), angle=None):
        if angle is None:
            if isinstance(values, Quaternion):
                self.w = values.w
                self.x = values.x
                self.y = values.y
                self.z = values.z
            else:
                if not _is_sequence(values) or len(values) != 4:
                    raise ValueError, "Quaternion requires four values"  # type: ignore

                self.w = values[0]
                self.x = values[1]
                self.y = values[2]
                self.z = values[3]
        else:
            if not _is_sequence(values) or len(values) != 3:  # type: ignore
                raise ValueError, "Axis-angle quaternion requires a 3D axis"  # type: ignore

            axis = Vector(values)
            if axis.length_squared() == 0:
                raise ValueError, "Axis-angle quaternion requires a non-zero axis"  # type: ignore
            axis.normalize()

            half_angle = angle * 0.5
            sine = math.sin(half_angle)

            self.w = math.cos(half_angle)
            self.x = axis[0] * sine
            self.y = axis[1] * sine
            self.z = axis[2] * sine

    def copy(self):
        return Quaternion((self.w, self.x, self.y, self.z))

    def __len__(self):
        return 4

    def __cmp__(self, other):
        if isinstance(other, Quaternion):
            other = other.to_tuple()
        return cmp(self.to_tuple(), other)

    def __repr__(self):
        return "Quaternion(%s)" % repr((
            self.w, self.x, self.y, self.z
        ))

    def __str__(self):
        return repr(self)

    def __getitem__(self, index):
        if index == 0:
            return self.w
        if index == 1:
            return self.x
        if index == 2:
            return self.y
        if index == 3:
            return self.z

        raise IndexError, "Quaternion index out of range"  # type: ignore

    def __setitem__(self, index, value):
        if index == 0:
            self.w = value
        elif index == 1:
            self.x = value
        elif index == 2:
            self.y = value
        elif index == 3:
            self.z = value
        else:
            raise IndexError, "Quaternion index out of range"  # type: ignore

    def __mul__(self, other):
        if isinstance(other, Matrix):
            return self.to_matrix(other.row_count) * other

        if isinstance(other, Quaternion):
            return Quaternion((
                self.w * other.w - self.x * other.x -
                self.y * other.y - self.z * other.z,

                self.w * other.x + self.x * other.w +
                self.y * other.z - self.z * other.y,

                self.w * other.y - self.x * other.z +
                self.y * other.w + self.z * other.x,

                self.w * other.z + self.x * other.y -
                self.y * other.x + self.z * other.w
            ))

        if isinstance(other, Vector):
            return self.rotate_vector(other)

        if type(other) in (types.IntType, types.FloatType):
            return Quaternion((
                self.w * other,
                self.x * other,
                self.y * other,
                self.z * other
            ))

        raise TypeError, "Invalid Quaternion multiplication"  # type: ignore

    def __rmul__(self, other):
        return self * other

    def conjugate(self):
        return Quaternion((self.w, -self.x, -self.y, -self.z))

    def length_squared(self):
        return (
            self.w * self.w +
            self.x * self.x +
            self.y * self.y +
            self.z * self.z
        )

    def length(self):
        return math.sqrt(self.length_squared())

    def normalize(self):
        length = self.length()

        if length == 0:
            raise ValueError, "Cannot normalize a zero quaternion"  # type: ignore

        self.w = self.w / length
        self.x = self.x / length
        self.y = self.y / length
        self.z = self.z / length

    def normalized(self):
        result = self.copy()
        result.normalize()
        return result

    def invert(self):
        length_squared = self.length_squared()

        if length_squared == 0:
            raise ValueError, "Cannot invert a zero quaternion"  # type: ignore

        self.w = self.w / length_squared
        self.x = -self.x / length_squared
        self.y = -self.y / length_squared
        self.z = -self.z / length_squared
    
    def inverted(self):
        length_squared = self.length_squared()

        if length_squared == 0:
            raise ValueError, "Cannot invert a zero quaternion"  # type: ignore

        return Quaternion((
            self.w / length_squared,
            -self.x / length_squared,
            -self.y / length_squared,
            -self.z / length_squared
        ))

    def rotate_vector(self, vector):
        if not isinstance(vector, Vector) or vector.size != 3:
            raise ValueError, "Quaternion rotation requires a 3D Vector"  # type: ignore

        # q * v * q^-1 可同时支持单位和非单位四元数，避免依赖调用方状态。
        qvector = Quaternion((0, vector[0], vector[1], vector[2]))
        result = self * qvector * self.inverted()

        return Vector((result.x, result.y, result.z))

    def to_matrix(self, size=3):
        if size != 3 and size != 4:
            raise ValueError, "Quaternion matrix size must be 3 or 4"  # type: ignore

        x = self.x
        y = self.y
        z = self.z
        w = self.w

        xx = x * x
        yy = y * y
        zz = z * z
        xy = x * y
        xz = x * z
        yz = y * z
        wx = w * x
        wy = w * y
        wz = w * z

        if size == 3:
            return Matrix(
                [(
                    1 - 2 * (yy + zz),
                    2 * (xy - wz),
                    2 * (xz + wy)
                ),
                (
                    2 * (xy + wz),
                    1 - 2 * (xx + zz),
                    2 * (yz - wx)
                ),
                (
                    2 * (xz - wy),
                    2 * (yz + wx),
                    1 - 2 * (xx + yy)
                )]
            )

        return Matrix(
            [(
                1 - 2 * (yy + zz),
                2 * (xy - wz),
                2 * (xz + wy),
                0
            ),
            (
                2 * (xy + wz),
                1 - 2 * (xx + zz),
                2 * (yz - wx),
                0
            ),
            (
                2 * (xz - wy),
                2 * (yz + wx),
                1 - 2 * (xx + yy),
                0
            ),
            (
                0, 0, 0, 1
            )]
        )

    def to_axis_angle(self):
        quaternion = self.normalized()

        if quaternion.w > 1:
            quaternion.w = 1

        if quaternion.w < -1:
            quaternion.w = -1

        angle = 2.0 * math.acos(quaternion.w)
        sine = math.sqrt(1.0 - quaternion.w * quaternion.w)

        if sine < 0.000001:
            axis = Vector((1.0, 0.0, 0.0))
        else:
            axis = Vector((
                quaternion.x / sine,
                quaternion.y / sine,
                quaternion.z / sine
            ))

        return axis, angle

    def to_tuple(self, precision=-1):
        values = (self.w, self.x, self.y, self.z)
        if precision == -1:
            return values
        return tuple(map(lambda x, precision=precision: round(x, precision), values))


class Matrix:
    def __init__(self, rows=[(1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,0,1)]):
        if len(rows) == 0:
            raise ValueError, "Matrix requires rows"  # type: ignore

        self.rows = []

        row_size = len(rows[0])

        if row_size == 0:
            raise ValueError, "Matrix rows cannot be empty"  # type: ignore

        i = 0
        while i < len(rows):
            if not _is_sequence(rows[i]):
                raise TypeError, "Matrix rows must be tuples or lists"  # type: ignore

            if len(rows[i]) != row_size:
                raise ValueError, "Matrix rows must have equal size"  # type: ignore

            self.rows.append(_copy_sequence(rows[i]))
            i = i + 1

        self.row_count = len(self.rows)
        self.column_count = row_size

    def copy(self):
        result = []
        i = 0
        while i < self.row_count:
            result.append(tuple(self.rows[i]))
            i = i + 1

        return Matrix(result)

    def __len__(self):
        return self.row_count

    def _to_square(self, size):
        # 缩小时截取左上角；放大时补齐齐次矩阵所需的单位元素。
        result = []
        i = 0
        while i < size:
            row = []
            j = 0
            while j < size:
                if i < self.row_count and j < self.column_count:
                    value = self.rows[i][j]
                elif i == j:
                    value = 1
                else:
                    value = 0

                row.append(value)
                j = j + 1

            result.append(tuple(row))
            i = i + 1

        return Matrix(result)

    def to_2x2(self):
        """返回矩阵的 2x2 方阵表示。"""
        return self._to_square(2)

    def to_3x3(self):
        """返回矩阵的 3x3 方阵表示。"""
        return self._to_square(3)

    def to_4x4(self):
        """返回矩阵的 4x4 方阵表示。"""
        return self._to_square(4)

    def __repr__(self):
        # values = []
        # i = 0
        # while i < self.row_count:
        #     values.append(tuple(self.rows[i]))
        #     i = i + 1

        return "Matrix(%s)" % repr(tuple(map(tuple, self.rows)))

    def __str__(self):
        s = "Matrix(("
        for i in range(self.row_count):
            sub = repr(tuple(self.rows[i]))
            if i == 0:
                s = "%s%s,\n" % (s, sub)
            elif i == self.row_count - 1:
                s = "%s        %s))" % (s, sub)
            else:
                s = "%s        %s,\n" % (s, sub)

        return s

    def __getitem__(self, index):
        return self.rows[index]

    def __setitem__(self, index, value):
        if len(value) != self.column_count:
            raise ValueError, "Invalid matrix row size"  # type: ignore

        self.rows[index] = _copy_sequence(value)

    # def __getattr__(self, name):
    #     if name == "translation":
    #         if self.row_count == 4:
    #             return Vector((self.rows[0][3], self.rows[1][3], self.rows[2][3]))
            
    #     raise AttributeError, "Matrix has no attribute '%s'" % name  # type: ignore

    # def __setattr__(self, name, value):
    #     if name == "translation":
    #         if self.row_count == 4:
    #             self.rows[0][3] = value[0]
    #             self.rows[1][3] = value[1]
    #             self.rows[2][3] = value[2]
    #     elif name in ("rows", "row_count", "column_count"):
    #         self.__dict__[name] = value
    #     else:
    #         raise AttributeError, "Matrix has no attribute '%s'" % name  # type: ignore

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError, "Matrix can only be added to Matrix"  # type: ignore

        if self.row_count != other.row_count:
            raise ValueError, "Matrix sizes do not match"  # type: ignore

        if self.column_count != other.column_count:
            raise ValueError, "Matrix sizes do not match"  # type: ignore

        result = []
        i = 0
        while i < self.row_count:
            row = []
            j = 0
            while j < self.column_count:
                row.append(self.rows[i][j] + other.rows[i][j])
                j = j + 1

            result.append(tuple(row))
            i = i + 1

        return Matrix(result)

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError, "Matrix can only be subtracted from Matrix"  # type: ignore

        if self.row_count != other.row_count:
            raise ValueError, "Matrix sizes do not match"  # type: ignore

        if self.column_count != other.column_count:
            raise ValueError, "Matrix sizes do not match"  # type: ignore

        result = []
        i = 0
        while i < self.row_count:
            row = []
            j = 0
            while j < self.column_count:
                row.append(self.rows[i][j] - other.rows[i][j])
                j = j + 1

            result.append(tuple(row))
            i = i + 1

        return Matrix(result)

    # def transform_point(self, vector):
    #     if self.row_count != 4 or self.column_count != 4:
    #         raise ValueError, "Point transform requires a 4x4 matrix"  # type: ignore

    #     result = self * Vector((vector[0], vector[1], vector[2], 1.0))
    #     return Vector((result[0], result[1], result[2]))


    # def transform_direction(self, vector):
    #     if self.row_count != 4 or self.column_count != 4:
    #         raise ValueError, "Direction transform requires a 4x4 matrix"  # type: ignore

    #     result = self * Vector((vector[0], vector[1], vector[2], 0.0))
    #     return Vector((result[0], result[1], result[2]))

    def __mul__(self, other):
        if isinstance(other, Vector):
            size = other.size
            other = other._to_xd(self.column_count)

            # if self.column_count != other.size:
            #     raise ValueError, "Matrix and Vector sizes do not match"  # type: ignore

            result = []
            i = 0
            while i < self.row_count:
                value = 0
                j = 0
                while j < self.column_count:
                    value = value + self.rows[i][j] * other[j]
                    j = j + 1

                result.append(value)
                i = i + 1

            return Vector(result)._to_xd(size)

        if isinstance(other, Matrix):
            if self.column_count != other.row_count:
                raise ValueError, "Matrix sizes do not match"  # type: ignore

            result = []
            i = 0
            while i < self.row_count:
                row = []
                j = 0
                while j < other.column_count:
                    value = 0
                    k = 0
                    while k < self.column_count:
                        value = value + (
                            self.rows[i][k] * other.rows[k][j]
                        )
                        k = k + 1

                    row.append(value)
                    j = j + 1

                result.append(tuple(row))
                i = i + 1

            return Matrix(result)

        if isinstance(other, Quaternion):
            if self.row_count < 3 or self.column_count < 3:
                raise ValueError, "Matrix must be at least 3x3"  # type: ignore

            rotation = self.to_quaternion()
            return rotation * other

        if type(other) in (types.IntType, types.FloatType):
            result = []
            i = 0
            while i < self.row_count:
                row = []
                j = 0
                while j < self.column_count:
                    row.append(self.rows[i][j] * other)
                    j = j + 1

                result.append(tuple(row))
                i = i + 1

            return Matrix(result)

        raise TypeError, "Invalid Matrix multiplication"  # type: ignore

    def __rmul__(self, other):
        return self * other

    def transpose(self):
        result = []
        i = 0
        while i < self.column_count:
            row = []
            j = 0
            while j < self.row_count:
                row.append(self.rows[j][i])
                j = j + 1

            result.append(tuple(row))
            i = i + 1

        self.rows = result

    def transposed(self):
        result = []
        i = 0
        while i < self.column_count:
            row = []
            j = 0
            while j < self.row_count:
                row.append(self.rows[j][i])
                j = j + 1

            result.append(tuple(row))
            i = i + 1

        return Matrix(result)

    def identity(self):
        if self.row_count != self.column_count:
            raise ValueError, "Identity requires a square matrix"  # type: ignore

        result = []
        i = 0
        while i < self.row_count:
            row = []
            j = 0
            while j < self.column_count:
                if i == j:
                    row.append(1)
                else:
                    row.append(0)

                j = j + 1

            result.append(tuple(row))
            i = i + 1

        return Matrix(result)

    def determinant(self):
        if self.row_count != self.column_count:
            raise ValueError, "Determinant requires a square matrix"  # type: ignore

        size = self.row_count

        if size == 1:
            return self.rows[0][0]

        if size == 2:
            return (
                self.rows[0][0] * self.rows[1][1] -
                self.rows[0][1] * self.rows[1][0]
            )

        if size == 3:
            a = self.rows
            return (
                a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1]) -
                a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0]) +
                a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
            )

        if size == 4:
            a = self.rows

            return (
                a[0][0] * (
                    a[1][1] * (a[2][2] * a[3][3] -
                               a[2][3] * a[3][2]) -
                    a[1][2] * (a[2][1] * a[3][3] -
                               a[2][3] * a[3][1]) +
                    a[1][3] * (a[2][1] * a[3][2] -
                               a[2][2] * a[3][1])
                ) -
                a[0][1] * (
                    a[1][0] * (a[2][2] * a[3][3] -
                               a[2][3] * a[3][2]) -
                    a[1][2] * (a[2][0] * a[3][3] -
                               a[2][3] * a[3][0]) +
                    a[1][3] * (a[2][0] * a[3][2] -
                               a[2][2] * a[3][0])
                ) +
                a[0][2] * (
                    a[1][0] * (a[2][1] * a[3][3] -
                               a[2][3] * a[3][1]) -
                    a[1][1] * (a[2][0] * a[3][3] -
                               a[2][3] * a[3][0]) +
                    a[1][3] * (a[2][0] * a[3][1] -
                               a[2][1] * a[3][0])
                ) -
                a[0][3] * (
                    a[1][0] * (a[2][1] * a[3][2] -
                               a[2][2] * a[3][1]) -
                    a[1][1] * (a[2][0] * a[3][2] -
                               a[2][2] * a[3][0]) +
                    a[1][2] * (a[2][0] * a[3][1] -
                               a[2][1] * a[3][0])
                )
            )

        raise ValueError, "Unsupported matrix size"  # type: ignore

    def invert(self):
        matrix = self.inverted()
        self.rows = matrix.rows

    def inverted(self):
        if self.row_count != self.column_count:
            raise ValueError, "Inverse requires a square matrix"  # type: ignore

        size = self.row_count
        if size != 2 and size != 3 and size != 4:
            raise ValueError, "Inverse supports 2x2, 3x3 and 4x4 matrices"  # type: ignore

        # 高斯-约旦消元：将 [A | I] 变换为 [I | A^-1]。
        augmented = []
        i = 0

        while i < size:
            row = []
            j = 0

            while j < size:
                row.append(float(self.rows[i][j]))
                j = j + 1

            j = 0
            while j < size:
                if i == j:
                    row.append(1.0)
                else:
                    row.append(0.0)

                j = j + 1

            augmented.append(row)
            i = i + 1

        i = 0
        while i < size:
            pivot = i

            while pivot < size and abs(augmented[pivot][i]) <= epsilon:
                pivot = pivot + 1

            if pivot == size:
                raise ValueError, "Matrix is singular"  # type: ignore

            if pivot != i:
                temporary = augmented[i]
                augmented[i] = augmented[pivot]
                augmented[pivot] = temporary

            divisor = augmented[i][i]
            j = 0

            while j < size * 2:
                augmented[i][j] = augmented[i][j] / divisor
                j = j + 1

            row_index = 0
            while row_index < size:
                if row_index != i:
                    factor = augmented[row_index][i]
                    j = 0

                    while j < size * 2:
                        augmented[row_index][j] = (
                            augmented[row_index][j] -
                            factor * augmented[i][j]
                        )
                        j = j + 1

                row_index = row_index + 1

            i = i + 1

        result = []
        i = 0

        while i < size:
            row = []
            j = size

            while j < size * 2:
                row.append(augmented[i][j])
                j = j + 1

            result.append(tuple(row))
            i = i + 1

        return Matrix(result)

    def decompose(self):
        if self.row_count != 4 or self.column_count != 4:
            raise ValueError, "TRS decomposition requires a 4x4 matrix"  # type: ignore

        # 当前矩阵约定为行向量存储旋转、最后一列存储平移。
        loc = Vector((
            self.rows[0][3],
            self.rows[1][3],
            self.rows[2][3]
        ))

        x_axis = Vector((
            self.rows[0][0],
            self.rows[1][0],
            self.rows[2][0]
        ))

        y_axis = Vector((
            self.rows[0][1],
            self.rows[1][1],
            self.rows[2][1]
        ))

        z_axis = Vector((
            self.rows[0][2],
            self.rows[1][2],
            self.rows[2][2]
        ))

        scale = Vector((
            x_axis.length(),
            y_axis.length(),
            z_axis.length()
        ))

        if scale[0] == 0 or scale[1] == 0 or scale[2] == 0:
            raise ValueError, "Cannot decompose zero-scale matrix"  # type: ignore

        rotation_rows = (
            (
                self.rows[0][0] / scale[0],
                self.rows[0][1] / scale[1],
                self.rows[0][2] / scale[2]
            ),
            (
                self.rows[1][0] / scale[0],
                self.rows[1][1] / scale[1],
                self.rows[1][2] / scale[2]
            ),
            (
                self.rows[2][0] / scale[0],
                self.rows[2][1] / scale[1],
                self.rows[2][2] / scale[2]
            )
        )

        rotation_matrix = Matrix(rotation_rows)

        if rotation_matrix.determinant() < 0:
            scale[0] = -scale[0]
            rotation_rows = (
                (
                    -rotation_rows[0][0],
                    rotation_rows[0][1],
                    rotation_rows[0][2]
                ),
                (
                    -rotation_rows[1][0],
                    rotation_rows[1][1],
                    rotation_rows[1][2]
                ),
                (
                    -rotation_rows[2][0],
                    rotation_rows[2][1],
                    rotation_rows[2][2]
                )
            )
            rotation_matrix = Matrix(rotation_rows)

        rot = rotation_matrix.to_quaternion()

        return loc, rot, scale

    def to_translation(self):
        if self.row_count != 4 or self.column_count != 4:
            raise ValueError, "Location requires a 4x4 matrix"  # type: ignore

        return Vector((
            self.rows[0][3],
            self.rows[1][3],
            self.rows[2][3]
        ))

    def to_quaternion(self):
        if self.row_count < 3 or self.column_count < 3:
            raise ValueError, "Matrix must be at least 3x3"  # type: ignore

        # 根据迹选择数值更稳定的分支，避免接近 180 度时精度恶化。
        trace = (
            self.rows[0][0] +
            self.rows[1][1] +
            self.rows[2][2]
        )

        if trace > 0:
            value = math.sqrt(trace + 1.0)
            w = value * 0.5
            value = 0.5 / value

            x = (self.rows[2][1] - self.rows[1][2]) * value
            y = (self.rows[0][2] - self.rows[2][0]) * value
            z = (self.rows[1][0] - self.rows[0][1]) * value

        elif (
            self.rows[0][0] > self.rows[1][1] and
            self.rows[0][0] > self.rows[2][2]
        ):
            value = math.sqrt(
                1.0 + self.rows[0][0] -
                self.rows[1][1] - self.rows[2][2]
            )
            x = value * 0.5
            value = 0.5 / value

            w = (self.rows[2][1] - self.rows[1][2]) * value
            y = (self.rows[0][1] + self.rows[1][0]) * value
            z = (self.rows[0][2] + self.rows[2][0]) * value

        elif self.rows[1][1] > self.rows[2][2]:
            value = math.sqrt(
                1.0 + self.rows[1][1] -
                self.rows[0][0] - self.rows[2][2]
            )
            y = value * 0.5
            value = 0.5 / value

            w = (self.rows[0][2] - self.rows[2][0]) * value
            x = (self.rows[0][1] + self.rows[1][0]) * value
            z = (self.rows[1][2] + self.rows[2][1]) * value

        else:
            value = math.sqrt(
                1.0 + self.rows[2][2] -
                self.rows[0][0] - self.rows[1][1]
            )
            z = value * 0.5
            value = 0.5 / value

            w = (self.rows[1][0] - self.rows[0][1]) * value
            x = (self.rows[0][2] + self.rows[2][0]) * value
            y = (self.rows[1][2] + self.rows[2][1]) * value

        return Quaternion((w, x, y, z)).normalized()

    def to_scale(self):
        if self.row_count != 4 or self.column_count != 4:
            raise ValueError, "Scale requires a 4x4 matrix"  # type: ignore

        return Vector((
            Vector((self.rows[0][0], self.rows[1]
                   [0], self.rows[2][0])).length(),
            Vector((self.rows[0][1], self.rows[1]
                   [1], self.rows[2][1])).length(),
            Vector((self.rows[0][2], self.rows[1]
                   [2], self.rows[2][2])).length()
        ))

    def SetTranslation(self, value):
        if self.row_count != 4:
            raise ValueError, "Matrix must be 4x4"  # type: ignore
        
        self.rows[0][3] = value[0]
        self.rows[1][3] = value[1]
        self.rows[2][3] = value[2]

def radians(degrees):
    return degrees * math.pi / 180.0


def degrees(radians_value):
    return radians_value * 180.0 / math.pi



# -------------------------------
def LocRotScale(loc, rot, scale):
    if isinstance(loc, Vector):
        if loc.size != 3:
            raise ValueError, "Location requires a 3D vector"  # type: ignore
        location = loc
    else:
        location = Vector(loc)

    if isinstance(scale, Vector):
        if scale.size != 3:
            raise ValueError, "Scale requires a 3D vector"  # type: ignore
        scaling = scale
    else:
        scaling = Vector(scale)

    if isinstance(rot, Quaternion):
        rotation = rot.normalized()
    else:
        rotation = Quaternion(rot).normalized()

    rotation_matrix = rotation.to_matrix(4)

    return Matrix((
        (
            rotation_matrix[0][0] * scaling[0],
            rotation_matrix[0][1] * scaling[1],
            rotation_matrix[0][2] * scaling[2],
            location[0]
        ),
        (
            rotation_matrix[1][0] * scaling[0],
            rotation_matrix[1][1] * scaling[1],
            rotation_matrix[1][2] * scaling[2],
            location[1]
        ),
        (
            rotation_matrix[2][0] * scaling[0],
            rotation_matrix[2][1] * scaling[1],
            rotation_matrix[2][2] * scaling[2],
            location[2]
        ),
        (0, 0, 0, 1)
    ))


def ToQuat(axis, angle):
    # type: (..., ...) -> tuple
    half_angle = angle * 0.5
    sine = math.sin(half_angle)

    w = math.cos(half_angle)
    x = axis[0] * sine
    y = axis[1] * sine
    z = axis[2] * sine

    return (w, x, y, z)


def QuatMul(q2, q1):
    # type: (..., ...) -> tuple
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
        raise ValueError # type: ignore


def Cross(v1, v2):
    # type: (..., ...) -> tuple
    if len(v1) == len(v2) == 3:
        return (
            v1[1] * v2[2] - v2[1] * v1[2],
            v1[2] * v2[0] - v2[2] * v1[0],
            v1[0] * v2[1] - v2[0] * v1[1],
        )
    printx(ValueError, "Input vectors must be of length 3.")
    raise ValueError # type: ignore


