# type: ignore

# Author: Sryml
# Email: sryml@hotmail.com
# Python Version: 1.5.2
# License: MIT
# Date: 2024-04-22

import sys

""" 
"AssertionError",
"AttributeError",
"EOFError",
"FloatingPointError",
"IOError",
"ImportError",
"IndexError",
"KeyError",
"KeyboardInterrupt",
"MemoryError",
"NameError",
"OverflowError",
"RuntimeError",
"SyntaxError",
"SystemError",
"SystemExit",
"TypeError",
"ValueError",
"ZeroDivisionError",
"""


class AssertionError:
    def __init__(self, msg=""):
        self.msg = msg

    def __repr__(self):
        return self.msg


class AttributeError:
    def __init__(self, msg=""):
        self.msg = msg

    def __repr__(self):
        return self.msg


class EOFError:
    def __init__(self, msg=""):
        self.msg = msg

    def __repr__(self):
        return self.msg


class FloatingPointError:
    def __init__(self, msg=""):
        self.msg = msg

    def __repr__(self):
        return self.msg


class IOError:
    def __init__(self, msg=""):
        self.msg = msg

    def __repr__(self):
        return self.msg


class ImportError:
    def __init__(self, msg=""):
        self.msg = msg

    def __repr__(self):
        return self.msg


class IndexError:
    def __init__(self, msg=""):
        self.msg = msg

    def __repr__(self):
        return self.msg


class KeyError:
    def __init__(self, msg=""):
        self.msg = msg

    def __repr__(self):
        return self.msg


class KeyboardInterrupt:
    def __init__(self, msg=""):
        self.msg = msg

    def __repr__(self):
        return self.msg


class MemoryError:
    def __init__(self, msg=""):
        self.msg = msg

    def __repr__(self):
        return self.msg


class NameError:
    def __init__(self, msg=""):
        self.msg = msg

    def __repr__(self):
        return self.msg


class OverflowError:
    def __init__(self, msg=""):
        self.msg = msg

    def __repr__(self):
        return self.msg


class RuntimeError:
    def __init__(self, msg=""):
        self.msg = msg

    def __repr__(self):
        return self.msg


class SyntaxError:
    def __init__(self, msg=""):
        self.msg = msg

    def __repr__(self):
        return self.msg


class SystemError:
    def __init__(self, msg=""):
        self.msg = msg

    def __repr__(self):
        return self.msg


class SystemExit:
    def __init__(self, msg=""):
        self.msg = msg

    def __repr__(self):
        return self.msg


class TypeError:
    def __init__(self, msg=""):
        self.msg = msg

    def __repr__(self):
        return self.msg


class ValueError:
    def __init__(self, msg=""):
        self.msg = msg

    def __repr__(self):
        return self.msg


class ZeroDivisionError:
    def __init__(self, msg=""):
        self.msg = msg

    def __repr__(self):
        return self.msg


sys.modules["__builtin__"].AssertionError = AssertionError
sys.modules["__builtin__"].AttributeError = AttributeError
sys.modules["__builtin__"].EOFError = EOFError
sys.modules["__builtin__"].FloatingPointError = FloatingPointError
sys.modules["__builtin__"].IOError = IOError
sys.modules["__builtin__"].ImportError = ImportError
sys.modules["__builtin__"].IndexError = IndexError
sys.modules["__builtin__"].KeyError = KeyError
sys.modules["__builtin__"].KeyboardInterrupt = KeyboardInterrupt
sys.modules["__builtin__"].MemoryError = MemoryError
sys.modules["__builtin__"].NameError = NameError
sys.modules["__builtin__"].OverflowError = OverflowError
sys.modules["__builtin__"].RuntimeError = RuntimeError
sys.modules["__builtin__"].SyntaxError = SyntaxError
sys.modules["__builtin__"].SystemError = SystemError
sys.modules["__builtin__"].SystemExit = SystemExit
sys.modules["__builtin__"].TypeError = TypeError
sys.modules["__builtin__"].ValueError = ValueError
sys.modules["__builtin__"].ZeroDivisionError = ZeroDivisionError
