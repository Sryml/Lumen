import Bladex
import BInput

InputManager=BInput.GetInputManager()
InputManager.SetInputActionsSet("Default")

ON_RELEASE=0
ON_PRESS=1

def IrPosicion1():
	char=Bladex.GetEntity("Player1")
	char.Position= -150500,2000,16750			# inicio

def IrPosicion2():
	char=Bladex.GetEntity("Player1")
	char.Position=-37750,-7000,27000			# sala trono

def IrPosicion3():
	char=Bladex.GetEntity("Player1")
	char.Position=-11000,-12000,30750			# pasarela 2ª planta

def IrPosicion4():
	char=Bladex.GetEntity("Player1")
	char.Position=-38000,-24000,30750			# escalera doble

def IrPosicion5():
	char=Bladex.GetEntity("Player1")
	char.Position=-18500, -1000, 3500			# subterraneos

def IrPosicion6():
	char=Bladex.GetEntity("Player1")
	char.Position=-36000, -8000, 42500			# patio bajo

def IrPosicion7():
	char=Bladex.GetEntity("Player1")
	char.Position=-66000, -1000, 30000			# final

def IrPosicion8():
	char=Bladex.GetEntity("Player1")
	char.Position=-27500, -58000, 29000			# final

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

