import Bladex
import BInput

InputManager=BInput.GetInputManager()
InputManager.SetInputActionsSet("Default")

ON_RELEASE=0
ON_PRESS=1

def IrPosicion1():
	char=Bladex.GetEntity("Player1")
	char.Position= -58160.91, 14102.74, -21261.14		# KASHGAR

def IrPosicion2():
	char=Bladex.GetEntity("Player1")
	char.Position=-80310.316, 14071.37, 3083.33		# TABRIZ

def IrPosicion3():
	char=Bladex.GetEntity("Player1")
	char.Position=-99901.29, 14110.95, -2993.093		# KAZEL-ZALAM

def IrPosicion4():
	char=Bladex.GetEntity("Player1")
	char.Position=-54700.32, 14072.62, -8432.73		# MARACAMDA

def IrPosicion5():
	char=Bladex.GetEntity("Player1")
	char.Position=-89089.77, 14117.513, 740.89		# KELBEGEN

def IrPosicion6():
	char=Bladex.GetEntity("Player1")
	char.Position=-78169.42, 14111.099, -4046.469		# TELL-HALAF

def IrPosicion7():
	char=Bladex.GetEntity("Player1")
	char.Position=-70303.92, 14110.45, 10525.97		# EPHIRA

def IrPosicion8():
	char=Bladex.GetEntity("Player1")
	char.Position=-57384.55, 14111.59, 21971.50		# KARUM
	

posicion1=IrPosicion1
posicion2=IrPosicion2
posicion3=IrPosicion3
posicion4=IrPosicion4
posicion5=IrPosicion5
posicion6=IrPosicion6
posicion7=IrPosicion7
posicion8=IrPosicion8


Bladex.AddInputAction("GoToPos1", 0)
Bladex.AddInputAction("GoToPos2", 0)
Bladex.AddInputAction("GoToPos3", 0)
Bladex.AddInputAction("GoToPos4", 0)
Bladex.AddInputAction("GoToPos5", 0)
Bladex.AddInputAction("GoToPos6", 0)
Bladex.AddInputAction("GoToPos7", 0)
Bladex.AddInputAction("GoToPos8", 0)


Bladex.AssocKey("GoToPos1", "Keyboard", "Numpad1", ON_PRESS)
Bladex.AssocKey("GoToPos2", "Keyboard", "Numpad2", ON_PRESS)
Bladex.AssocKey("GoToPos3", "Keyboard", "Numpad3", ON_PRESS)
Bladex.AssocKey("GoToPos4", "Keyboard", "Numpad4", ON_PRESS)
Bladex.AssocKey("GoToPos5", "Keyboard", "Numpad5", ON_PRESS)
Bladex.AssocKey("GoToPos6", "Keyboard", "Numpad6", ON_PRESS)
Bladex.AssocKey("GoToPos7", "Keyboard", "Numpad7", ON_PRESS)
Bladex.AssocKey("GoToPos8", "Keyboard", "Numpad8", ON_PRESS)


Bladex.AddBoundFunc("GoToPos1", posicion1)
Bladex.AddBoundFunc("GoToPos2", posicion2)
Bladex.AddBoundFunc("GoToPos3", posicion3)
Bladex.AddBoundFunc("GoToPos4", posicion4)
Bladex.AddBoundFunc("GoToPos5", posicion5)
Bladex.AddBoundFunc("GoToPos6", posicion6)
Bladex.AddBoundFunc("GoToPos7", posicion7)
Bladex.AddBoundFunc("GoToPos8", posicion8)

