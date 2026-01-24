import Bladex
import Lumenx
import sys
import os

import ConsoleOutput

ConsoleOutput.InitConsole()


def BladeRawInput(prompt=None):
    "Provides raw_input() for Blade"
    # flush stderr/out first.
    try:
        sys.stdout.flush()
        sys.stderr.flush()
    except:
        pass
    if prompt is None:
        prompt = ""
    ret = Bladex.Input(prompt)
    if ret == 0:
        exec(Lumenx.Raisex(KeyboardInterrupt, "operation cancelled"))
    return ret


sys.modules["__builtin__"].raw_input = BladeRawInput  # type: ignore
sys.modules["__builtin__"].input = BladeRawInput  # type: ignore
sys.setcheckinterval(100)  # type: ignore

Bladex.CloseDebugChannel("DefaultChannel")

if not os.path.exists("../../AnmPak"):
    os.mkdir("../../AnmPak")
#
import Menu
from LumenLib import BODLoader

BODLoader.Init()

Lumenx.printx("Executed sys_init.py")
