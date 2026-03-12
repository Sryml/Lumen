#  _    _   _ __  __ _____ _   _
# | |  | | | |  \/  | ____| \ | |
# | |  | | | | |\/| |  _| |  \| |
# | |__| |_| | |  | | |___| |\  |
# |_____\___/|_|  |_|_____|_| \_|
#


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
