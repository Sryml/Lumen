# for Lumen


import Console
import sys



class ConsoleOutput:
  softspace=1

  def write(self,message):
    if message is None:
      Console.ConsoleOutput("None")
      sys.__stdout__.write("None")
    else:
      Console.ConsoleOutput(message)
      sys.__stdout__.write(message)
    sys.__stdout__.flush()

  def flush(self):
    pass


def InitConsole():
  ConsoleOut=ConsoleOutput()
  sys.stderr=sys.stdout=ConsoleOut
