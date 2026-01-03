import Bladex
import BInput

InputManager=BInput.GetInputManager()
InputManager.SetInputActionsSet("Default")

ON_RELEASE=0
ON_PRESS=1

def IrPosicion1():
	char=Bladex.GetEntity("Player1")
	char.Position=7066.49313608, -149.024699022, -4854.107342	

def IrPosicion2():
	char=Bladex.GetEntity("Player1")
	char.Position=24304.2086494, -168.115240304, -5435.95090848		

def IrPosicion3():
	char=Bladex.GetEntity("Player1")
	char.Position=7801.07397769, -159.019837883, 14624.9608164		


def IrPosicion4():
	char=Bladex.GetEntity("Player1")
	char.Position=23815.5211544, -159.313915256, 16299.6980865


def IrPosicion5():
	char=Bladex.GetEntity("Player1")
	char.Position=15759.4413188, -157.543156353, -14584.3707067


def IrPosicion6():
	char=Bladex.GetEntity("Player1")
	char.Position=15338.8777075, -408.226884675, 31143.9235769





posicion1=IrPosicion1
posicion2=IrPosicion2
posicion3=IrPosicion3
posicion4=IrPosicion4
posicion5=IrPosicion5
posicion6=IrPosicion6


Bladex.AddInputAction("GoToPos1", 0)
Bladex.AddInputAction("GoToPos2", 0)
Bladex.AddInputAction("GoToPos3", 0)
Bladex.AddInputAction("GoToPos4", 0)
Bladex.AddInputAction("GoToPos5", 0)
Bladex.AddInputAction("GoToPos6", 0)



Bladex.AssocKey("GoToPos1", "Keyboard", "Numpad1", ON_PRESS)
Bladex.AssocKey("GoToPos2", "Keyboard", "Numpad2", ON_PRESS)
Bladex.AssocKey("GoToPos3", "Keyboard", "Numpad3", ON_PRESS)
Bladex.AssocKey("GoToPos4", "Keyboard", "Numpad4", ON_PRESS)
Bladex.AssocKey("GoToPos5", "Keyboard", "Numpad5", ON_PRESS)
Bladex.AssocKey("GoToPos6", "Keyboard", "Numpad6", ON_PRESS)


Bladex.AddBoundFunc("GoToPos1", posicion1)
Bladex.AddBoundFunc("GoToPos2", posicion2)
Bladex.AddBoundFunc("GoToPos3", posicion3)
Bladex.AddBoundFunc("GoToPos4", posicion4)
Bladex.AddBoundFunc("GoToPos5", posicion5)
Bladex.AddBoundFunc("GoToPos6", posicion6)


