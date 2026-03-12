#  _    _   _ __  __ _____ _   _
# | |  | | | |  \/  | ____| \ | |
# | |  | | | | |\/| |  _| |  \| |
# | |__| |_| | |  | | |___| |\  |
# |_____\___/|_|  |_|_____|_| \_|
#

import string

from Lumenx import printx

#
import typing

if typing.TYPE_CHECKING:
    apply = lambda fn, args=(), kwds={}: None
    execfile = lambda filename, globals=None, locals=None: None


# -------------------------------
# 字典类
# -------------------------------
class Dictionary:
    def __init__(self, dict=None, **kwargs):
        """初始化字典"""
        self.data = {}
        apply(self.update, (dict,), kwargs)

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
        elif isinstance(other, dict):
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

    def __delitem__(self, key):
        """删除 key"""
        del self.data[key]

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
        """移除并返回值（Python 1.5 原版dict没有pop，但我们可以实现）"""
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


"""
if 1:
    from LumenLib import BUtils
    d=BUtils.Dictionary(a=1,b=2)
"""
