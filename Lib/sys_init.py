import Bladex
import Lumenx
import os
import sys


def init():
    paths = [
        "Bin",
        "Scripts",
        "Scripts/Combos",
        "Scripts/Biped",
        "Lib",
        "Lib/AnmSets",
        "Lib/Widgets",
        "Lib/PythonLib",
        "Lib/PythonLib/Idle')",
        "Lib/PythonLib/lib-tk')",
        "Lib/PythonLib/DLLs')",
        "Lib/PythonLib/Pmw')",
        "Lib/PythonLib/Pmw/Pmw_0_8')",
        "Lib/PythonLib/Pmw/Pmw_0_8/lib')",
    ]

    sys.path = ["."]

    if Lumenx.GetCurrentMod():
        ModRelpath = os.path.join("..", os.path.relpath(".", Lumenx.GetMapListPath()))
        RootRelpath = os.path.join(
            ModRelpath, "..", os.path.relpath(".", Lumenx.ModListPath)
        )
    else:
        ModRelpath = ""
        RootRelpath = "../.."
    OriginalRootRelpath = os.path.join(RootRelpath, "..")

    for root in (
        ModRelpath,
        RootRelpath,
        OriginalRootRelpath,
    ):
        if not ModRelpath:
            continue
        for p in paths:
            sys.path.append(os.path.join(root, p))

    Lumenx.SetCurrentMap(os.path.basename(os.getcwd()))

    # Loaded from original
    # if not globals().get("Lumen"):
    #     pass


init()
del init

####
import ConsoleOutput

ConsoleOutput.InitConsole()


# execfile("SCRIPTS/import_loca.py")


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
        # raise KeyboardInterrupt, "operation cancelled"
        print("KeyboardInterrupt: operation cancelled")
    return ret


def BladeInput(prompt=None):
    "Provides input() for Blade apps"
    return eval(raw_input(prompt))


sys.modules["__builtin__"].raw_input = BladeRawInput
sys.modules["__builtin__"].input = BladeInput
sys.setcheckinterval(100)


Bladex.CloseDebugChannel("DefaultChannel")

# if Reference.PYTHON_DEBUG:
# execfile("SCRIPTS/generate_loca.py")

try:
    os.mkdir("../../AnmPak")
except:
    pass

import BODLoader

BODLoader.init()

print("Executed sys_init.py")
