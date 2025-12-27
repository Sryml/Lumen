


import Console
import sys



class ConsoleOutput:
  softspace=1

  def write(self,message):
    if message is None:
      Console.ConsoleOutput("None")
    else:
      Console.ConsoleOutput(message)

  def flush(self):
    pass


def InitConsole():
  ConsoleOut=ConsoleOutput()
  sys.stderr=sys.stdout=ConsoleOut
