

import Bladex
import sys
# import Reference

sys.path.append("../../Scripts")
sys.path.append("../../Scripts/Combos")
sys.path.append("../../Scripts/Biped")
sys.path.append("../../Lib")
sys.path.append("../../Lib/AnmSets")
sys.path.append("../../Lib/Widgets")
sys.path.append("../../Lib/PythonLib")
sys.path.append("../../Lib/PythonLib/Idle")
sys.path.append("../../Lib/PythonLib/lib-tk")
sys.path.append("../../Lib/PythonLib/DLLs")



import ConsoleOutput

ConsoleOutput.InitConsole()

# execfile("../../SCRIPTS/import_loca.py")

def BladeRawInput(prompt=None):
  "Provides raw_input() for Blade"
  # flush stderr/out first.
  try:
    sys.stdout.flush()
    sys.stderr.flush()
  except:
    pass
  if prompt is None: prompt = ""
  ret=Bladex.Input(prompt)
  if ret==0:
    raise KeyboardInterrupt, "operation cancelled"
  return ret


def BladeInput(prompt=None):
  "Provides input() for Blade apps"
  return eval(raw_input(prompt))



sys.modules['__builtin__'].raw_input=BladeRawInput
sys.modules['__builtin__'].input=BladeInput
sys.setcheckinterval(100)


Bladex.CloseDebugChannel("DefaultChannel")

# if Reference.PYTHON_DEBUG:
    # execfile("../../SCRIPTS/generate_loca.py")

try:
	os.mkdir("../../AnmPak")
except:
	pass

print "Executed sys_init.py"

