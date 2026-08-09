import math

from LumenLib import BTest

from LumenLib.mathutils import *


def _assert_close(value, expected, tolerance=1e-5):
    assert abs(value - expected) <= tolerance


def test_Vector_init():
    v = Vector((1.0, 2.0, 3.0))
    assert v.to_tuple() == (1.0, 2.0, 3.0)


def test_Vector_copy():
    v = Vector((1.0, 2.0, 3.0))
    copy = v.copy()
    assert copy.to_tuple() == v.to_tuple()
    assert copy is not v


def test_Vector_len_getitem_setitem():
    v = Vector((1.0, 2.0, 3.0))
    assert len(v) == 3
    assert v[1] == 2.0
    v[1] = -0.0
    assert v[1] == 0.0


def test_Vector_component_attributes():
    v = Vector((1.0, 2.0, 3.0))
    assert v.x == 1.0
    assert v.xy.to_tuple() == (1.0, 2.0)
    v.xy = (4.0, 5.0)
    assert v.to_tuple() == (4.0, 5.0, 3.0)
    v.z = 0
    assert v.z == 0.0


def test_Vector_cmp():
    assert Vector((1, 2)).__cmp__(Vector((1, 3))) == -1
    assert Vector((1, 2)).__cmp__(Vector((1, 2))) == 0
    assert Vector((1, 3)).__cmp__(Vector((1, 2))) == 1


def test_Vector_str_repr():
    v = Vector((1.0, 2.0, 3.0))
    assert str(v) == "<Vector (1.0, 2.0, 3.0)>"
    assert repr(v) == "Vector((1.0, 2.0, 3.0))"


def test_Vector_add_sub_neg():
    first = Vector((1.0, 2.0, 3.0))
    second = Vector((3.0, 2.0, 1.0))
    assert (first + second).to_tuple() == (4.0, 4.0, 4.0)
    assert (first - second).to_tuple() == (-2.0, 0.0, 2.0)
    assert (-first).to_tuple() == (-1.0, -2.0, -3.0)


def test_Vector_mul_rmul_div():
    v = Vector((2.0, 4.0, 6.0))
    assert (v * 2).to_tuple() == (4.0, 8.0, 12.0)
    assert (2 * v).to_tuple() == (4.0, 8.0, 12.0)
    assert (v * Vector((1.0, 2.0, 3.0))).to_tuple() == (2.0, 8.0, 18.0)
    assert v.__div__(2).to_tuple() == (1.0, 2.0, 3.0)


def test_Vector_lengths():
    v = Vector((3.0, 4.0, 0.0))
    assert v.length_squared() == 25.0
    assert v.length() == 5.0


def test_Vector_normalize_normalized():
    v = Vector((3.0, 4.0, 0.0))
    normalized = v.normalized()
    assert v.to_tuple() == (3.0, 4.0, 0.0)
    _assert_close(normalized.length(), 1.0)
    v.normalize()
    assert v.to_tuple() == normalized.to_tuple()


def test_Vector_dot_cross_angle():
    x_axis = Vector((1.0, 0.0, 0.0))
    y_axis = Vector((0.0, 1.0, 0.0))
    assert x_axis.dot(y_axis) == 0.0
    assert x_axis.cross(y_axis).to_tuple() == (0.0, 0.0, 1.0)
    assert x_axis.angle(y_axis) == math.pi * 0.5


def test_Vector_to_tuple_and_dimensions():
    v = Vector((1.23456, 2.34567))
    assert v.to_tuple(2) == (1.23, 2.35)
    assert v.to_2d().to_tuple() == (1.23456, 2.34567)
    assert v.to_3d().to_tuple() == (1.23456, 2.34567, 1)
    assert v.to_4d().to_tuple() == (1.23456, 2.34567, 1, 1)


def test_Quaternion_init():
    q = Quaternion((1.0, 2.0, 3.0, 4.0))
    assert q.to_tuple() == (1.0, 2.0, 3.0, 4.0)
    identity = Quaternion()
    assert identity.to_tuple() == (1, 0, 0, 0)


def test_Quaternion_axis_angle_init():
    q = Quaternion((0.0, 0.0, 1.0), math.pi)
    _assert_close(q.w, 0.0)
    _assert_close(q.z, 1.0)


def test_Quaternion_copy_cmp_repr_str():
    q = Quaternion((1.0, 2.0, 3.0, 4.0))
    assert q.copy().to_tuple() == q.to_tuple()
    assert q.__cmp__(Quaternion((1.0, 2.0, 3.0, 4.0))) == 0
    assert repr(q) == "Quaternion((1.0, 2.0, 3.0, 4.0))"
    assert str(q) == repr(q)


def test_Quaternion_getitem_setitem():
    q = Quaternion((1.0, 2.0, 3.0, 4.0))
    assert q[0] == 1.0
    q[0] = 5.0
    assert q.w == 5.0


def test_Quaternion_mul_rmul():
    q = Quaternion((1.0, 2.0, 3.0, 4.0))
    assert (q * 2).to_tuple() == (2.0, 4.0, 6.0, 8.0)
    assert (2 * q).to_tuple() == (2.0, 4.0, 6.0, 8.0)
    assert (Quaternion() * q).to_tuple() == q.to_tuple()


def test_Quaternion_conjugate_lengths():
    q = Quaternion((1.0, 2.0, 3.0, 4.0))
    assert q.conjugate().to_tuple() == (1.0, -2.0, -3.0, -4.0)
    assert q.length_squared() == 30.0
    _assert_close(q.length(), math.sqrt(30.0))


def test_Quaternion_normalize_normalized_inverse():
    q = Quaternion((1.0, 2.0, 3.0, 4.0))
    normalized = q.normalized()
    assert q.to_tuple() == (1.0, 2.0, 3.0, 4.0)
    _assert_close(normalized.length(), 1.0)
    inverse = q.inverse()
    product = q * inverse
    _assert_close(product.w, 1.0)
    _assert_close(product.x, 0.0)
    _assert_close(product.y, 0.0)
    _assert_close(product.z, 0.0)


def test_Quaternion_rotate_vector():
    q = Quaternion((0.0, 0.0, 1.0), math.pi * 0.5)
    rotated = q.rotate_vector(Vector((1.0, 0.0, 0.0)))
    _assert_close(rotated.x, 0.0)
    _assert_close(rotated.y, 1.0)
    _assert_close(rotated.z, 0.0)


def test_Quaternion_to_matrix():
    q = Quaternion()
    assert q.to_matrix(3).rows == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert q.to_matrix(4).rows == [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]


def test_Quaternion_to_axis_angle_tuple():
    q = Quaternion((0.0, 0.0, 1.0), math.pi)
    axis, angle = q.to_axis_angle()
    assert axis.to_tuple() == (0.0, 0.0, 1.0)
    _assert_close(angle, math.pi)
    assert q.to_tuple(1) == (0.0, 0.0, 0.0, 1.0)


def test_Matrix_init():
    m = Matrix(
        [(1.0, 2.0, 3.0),
        (4.0, 5.0, 6.0),
        (7.0, 8.0, 9.0)]
    )
    assert m.row_count == 3
    assert m.column_count == 3
    assert m[0] == [1.0, 2.0, 3.0]
    assert m[2] == [7.0, 8.0, 9.0]


def test_Matrix_copy_repr_str():
    m = Matrix([(1.0, 2.0), (3.0, 4.0)])
    copy = m.copy()
    assert copy.rows == m.rows
    assert copy is not m
    assert repr(m) == "Matrix(((1.0, 2.0), (3.0, 4.0)))"
    assert str(m) == "Matrix(((1.0, 2.0),\n        (3.0, 4.0)))"


def test_Matrix_getitem_setitem():
    m = Matrix([(1.0, 2.0), (3.0, 4.0)])
    assert m[1][0] == 3.0
    m[1] = (5.0, 6.0)
    assert m[1] == [5.0, 6.0]


def test_Matrix_add_sub():
    first = Matrix([(1.0, 2.0), (3.0, 4.0)])
    second = Matrix([(4.0, 3.0), (2.0, 1.0)])
    assert (first + second).rows == [[5.0, 5.0], [5.0, 5.0]]
    assert (first - second).rows == [[-3.0, -1.0], [1.0, 3.0]]


def test_Matrix_mul_vector_matrix_scalar():
    matrix = Matrix([(1.0, 2.0), (3.0, 4.0)])
    assert (matrix * Vector((2.0, 3.0))).to_tuple() == (8.0, 18.0)
    assert (matrix * matrix).rows == [[7.0, 10.0], [15.0, 22.0]]
    assert (matrix * 2).rows == [[2.0, 4.0], [6.0, 8.0]]
    assert (2 * matrix).rows == [[2.0, 4.0], [6.0, 8.0]]


def test_Matrix_mul_quaternion():
    matrix = Matrix([(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)])
    q = Quaternion((1.0, 2.0, 3.0, 4.0))
    assert (matrix * q).to_tuple(3) == q.to_tuple(3)


def test_Matrix_transposed_identity():
    matrix = Matrix([(1.0, 2.0, 3.0), (4.0, 5.0, 6.0)])
    assert matrix.transposed().rows == [
        [1.0, 4.0],
        [2.0, 5.0],
        [3.0, 6.0]
    ]
    square = Matrix([(1.0, 2.0), (3.0, 4.0)])
    assert square.identity().rows == [[1, 0], [0, 1]]


def test_Matrix_determinant():
    assert Matrix([(4.0, 7.0), (2.0, 6.0)]).determinant() == 10.0
    assert Matrix(
        [(1.0, 2.0, 3.0),
        (0.0, 1.0, 4.0),
        (5.0, 6.0, 0.0)]
    ).determinant() == 1.0


def test_Matrix_inverse():
    matrix = Matrix([(4.0, 7.0), (2.0, 6.0)])
    inverse = matrix.inverse()
    _assert_close(inverse[0][0], 0.6)
    _assert_close(inverse[0][1], -0.7)
    _assert_close(inverse[1][0], -0.2)
    _assert_close(inverse[1][1], 0.4)
    product = matrix * inverse
    _assert_close(product[0][0], 1.0)
    _assert_close(product[0][1], 0.0)
    _assert_close(product[1][0], 0.0)
    _assert_close(product[1][1], 1.0)


def test_Matrix_decompose_translation_quaternion_scale():
    matrix = Matrix(
        [(2.0, 0.0, 0.0, 10.0),
        (0.0, 3.0, 0.0, 20.0),
        (0.0, 0.0, 4.0, 30.0),
        (0.0, 0.0, 0.0, 1.0)]
    )
    location, rotation, scale = matrix.decompose()
    assert location.to_tuple() == (10.0, 20.0, 30.0)
    assert rotation.to_tuple() == (1.0, 0.0, 0.0, 0.0)
    assert scale.to_tuple() == (2.0, 3.0, 4.0)
    assert matrix.to_translation().to_tuple() == (10.0, 20.0, 30.0)
    assert matrix.to_quaternion().to_tuple() == (1.0, 0.0, 0.0, 0.0)
    assert matrix.to_scale().to_tuple() == (2.0, 3.0, 4.0)


def test_Matrix_to_square():
    matrix = Matrix([(1.0, 2.0), (3.0, 4.0)])
    assert matrix.to_2x2().rows == [[1.0, 2.0], [3.0, 4.0]]
    assert matrix.to_3x3().rows == [
        [1.0, 2.0, 0.0],
        [3.0, 4.0, 0.0],
        [0.0, 0.0, 1.0]
    ]
    assert matrix.to_4x4().rows == [
        [1.0, 2.0, 0.0, 0.0],
        [3.0, 4.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ]

def test_Matrix_loc_rot_scale_roundtrip():
    original = Matrix(
        [(2.0, 0.0, 0.0, 10.0),
         (0.0, 3.0, 0.0, 20.0),
         (0.0, 0.0, 4.0, 30.0),
         (0.0, 0.0, 0.0, 1.0)]
    )

    loc, rot, scale = original.decompose()
    restored = LocRotScale(loc, rot, scale)

    for i in range(4):
        for j in range(4):
            _assert_close(restored[i][j], original[i][j])

#
BTest.Run()
