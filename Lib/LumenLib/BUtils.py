#  _    _   _ __  __ _____ _   _
# | |  | | | |  \/  | ____| \ | |
# | |  | | | | |\/| |  _| |  \| |
# | |__| |_| | |  | | |___| |\  |
# |_____\___/|_|  |_|_____|_| \_|
#

import string
import types
import sys
import math

import ObjStore

from Lumenx import printx

#
import typing

if typing.TYPE_CHECKING:
    apply = lambda fn, args=(), kwds={}: None
    execfile = lambda filename, globals=None, locals=None: None
    cmp = lambda x, y: None


# -------------------------------
# 字典类
# -------------------------------
class Dictionary:
    def __init__(self, dict=None, persistent=0, **kwargs):
        """初始化字典"""
        if persistent:
            self.ObjId = ObjStore.GetNewId()
            ObjStore.ObjectsStore[self.ObjId] = self
        else:
            self.ObjId = None
        #
        self.update_callbacks = []
        self.data = {}
        apply(self.update, (dict,), kwargs)

    def persistent_id(self):
        return self.ObjId

    # -------------------------------
    def __getstate__(self):
        # type: () -> dict
        return {"Dictionary": (self.ObjId, self.data)}

    def __setstate__(self, state):
        self.update_callbacks = []
        state = state["Dictionary"]
        self.ObjId = state[0]
        if self.ObjId is not None:
            ObjStore.ObjectsStore[self.ObjId] = self
        #
        self.data = state[1]

    # -------------------------------
    def __repr__(self):
        """返回对象的字符串表示"""
        items = []
        for key, value in self.data.items():
            items.append("%s: %s" % (repr(key), repr(value)))
        return "Dictionary({" + string.join(items, ", ") + "})"

    def __cmp__(self, other):
        """比较两个字典 - Python 1.5 使用 __cmp__ 而非 __eq__"""
        if isinstance(other, Dictionary):
            return cmp(self.data, other.data)
        elif isinstance(other, types.DictType):
            return cmp(self.data, other)
        else:
            return -1  # 无法比较

    def __len__(self):
        """返回字典大小"""
        return len(self.data)

    def __getitem__(self, key):
        """通过 key 获取 value"""
        return self.data[key]

    def __setitem__(self, key, value):
        """设置 key-value 对"""
        self.data[key] = value
        self.CallUpdateCallbacks(key, value)

    def __delitem__(self, key):
        """删除 key"""
        del self.data[key]

    # -------------------------------
    def has_key(self, key):
        """检查 key 是否存在（Python 1.5 方法）"""
        return self.data.has_key(key)

    # def __contains__(self, key):
    #     return self.has_key(key)

    def items(self):
        """返回所有 key-value 对"""
        return self.data.items()

    def keys(self):
        """返回所有 key"""
        return self.data.keys()

    def values(self):
        """返回所有 value"""
        return self.data.values()

    def clear(self):
        """清空字典"""
        self.data.clear()

    def copy(self):
        """浅拷贝"""
        return Dictionary(self.data.copy())

    def get(self, key, default=None):
        """安全获取值"""
        if self.has_key(key):
            return self.data[key]
        return default

    def update(self, dict=None, **kwargs):
        """更新字典"""
        if dict:
            if hasattr(dict, "items"):
                items = dict.items()
            else:
                items = dict  # 假设是 (key, value) 列表
            for key, value in items:
                self[key] = value

        # 处理关键字参数
        for key, value in kwargs.items():
            self[key] = value

    def setdefault(self, key, default=None):
        """设置默认值（如果key不存在）"""
        if not self.has_key(key):
            self[key] = default
        return self[key]

    def pop(self, key, *args):
        """移除并返回值（Python 1.5 原版dict没有pop）"""
        if len(args) > 1:
            printx(TypeError, "pop expected at most 2 arguments")
            return None

        if self.has_key(key):
            value = self[key]
            del self[key]
            return value
        elif args:
            return args[0]
        else:
            printx(KeyError, key)

    # -------------------------------
    def AddUpdateCallback(self, callback):
        """添加更新回调"""
        self.update_callbacks.append(callback)

    def RemoveUpdateCallback(self, callback):
        """移除更新回调"""
        if callback in self.update_callbacks:
            self.update_callbacks.remove(callback)

    def CallUpdateCallbacks(self, key, value):
        """调用更新回调"""
        for callback in self.update_callbacks:
            callback(key, value)


class EntitiesSelectionDict(Dictionary):
    def __init__(self, dict=None, persistent=0, **kwargs):
        self.data_raw = {}
        apply(Dictionary.__init__, (self, dict, persistent), kwargs)

    # -------------------------------
    def __getstate__(self):
        state = {"Dictionary": (self.ObjId, {})}
        state.update({"EntitiesSelectionDict": self.data_raw})  # type: ignore
        return state

    def __setstate__(self, state):
        Dictionary.__setstate__(self, state)
        self.data_raw = state["EntitiesSelectionDict"]
        self.update(self.data_raw)

    # -------------------------------
    def __setitem__(self, key, value):
        import MenuText

        self.data_raw[key] = value
        new_value = value
        if type(value) in (types.TupleType, types.ListType) and len(value) == 3:
            new_value = (value[0], value[1], MenuText.GetMenuText(value[2]))
        Dictionary.__setitem__(self, key, new_value)

    def __delitem__(self, key):
        Dictionary.__delitem__(self, key)
        del self.data_raw[key]


# -------------------------------
# 解析UTF-8字符串
# -------------------------------
def is_continuation_byte(byte):
    """检查是不是 UTF-8 的后续字节（10xxxxxx）"""
    return (byte & 0xC0) == 0x80


def get_utf8_char_length(first_byte):
    """根据首字节判断 UTF-8 字符的字节长度"""
    if (first_byte & 0x80) == 0x00:  # ASCII（0xxxxxxx）
        return 1
    elif (first_byte & 0xE0) == 0xC0:  # 2字节（110xxxxx）
        return 2
    elif (first_byte & 0xF0) == 0xE0:  # 3字节（1110xxxx）
        return 3
    elif (first_byte & 0xF8) == 0xF0:  # 4字节（11110xxx）
        return 4
    else:
        return -1  # 非法UTF-8字符


def parse_utf8_string(s):
    """手动解析UTF-8字符串，返回字符列表（每个字符占用的字节当成一个整体）"""
    chars = []
    i = 0
    n = len(s)
    while i < n:
        first_byte = ord(s[i])
        length = get_utf8_char_length(first_byte)
        if length == -1 or i + length > n:
            break  # 无效UTF-8序列（Python 1.5无UnicodeError，直接截断）

        utf8_char = s[i : i + length]
        chars.append(utf8_char)
        i = i + length
    return chars


# -------------------------------
# 获取回溯命名空间
# -------------------------------
def get_tb_namespace(depth=1):
    """
    The function `get_tb_namespace` retrieves the global and local namespaces at a specified depth in
    the call stack when an exception occurs.

    :param depth: The `depth` parameter in the `get_tb_namespace` function determines how many levels up
    the call stack to go when retrieving the namespace. Positive values of `depth` indicate how many
    levels up to go, while a value of -1 indicates to go all the way to the top of the call, defaults to
    1 (optional)

    :return: The function `get_tb_namespace` returns the global and local namespaces of the frame at the
    specified depth in the call stack.
    """
    try:
        1 / 0
    except ZeroDivisionError:
        frame = sys.exc_info()[2].tb_frame.f_back
    #
    if depth > 0:
        for i in range(depth):
            if not frame.f_back:
                break
            frame = frame.f_back
    elif depth == -1:
        while frame.f_back:
            frame = frame.f_back

    return (frame.f_globals, frame.f_locals)


# -------------------------------
#
# -------------------------------


def ToQuat(axis, angle):
    angle = angle * 0.5
    w = math.cos(angle)
    x = axis[0] * math.sin(angle)
    y = axis[1] * math.sin(angle)
    z = axis[2] * math.sin(angle)
    return (w, x, y, z)


def QuatMul(q1, q2):
    w = q1[0] * q2[0] - q1[1] * q2[1] - q1[2] * q2[2] - q1[3] * q2[3]
    x = q1[0] * q2[1] + q1[1] * q2[0] + q1[2] * q2[3] - q1[3] * q2[2]
    y = q1[0] * q2[2] - q1[1] * q2[3] + q1[2] * q2[0] + q1[3] * q2[1]
    z = q1[0] * q2[3] + q1[1] * q2[2] - q1[2] * q2[1] + q1[3] * q2[0]
    return (w, x, y, z)


"""
if 1:
    from LumenLib import BUtils
    d=BUtils.Dictionary(a=1,b=2)
"""
