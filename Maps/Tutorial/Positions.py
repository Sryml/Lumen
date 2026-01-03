import Bladex
import BInput

InputManager=BInput.GetInputManager()
InputManager.SetInputActionsSet("Default")

ON_RELEASE=0
ON_PRESS=1



def IrPosicion1():
	char=Bladex.GetEntity("Player1")
	char.Position=200148,-3000,45624

def IrPosicion2():
	char=Bladex.GetEntity("Player1")
	char.Position=253821.807167, -98.9134883089, 124066.1481		

def IrPosicion3():
	char=Bladex.GetEntity("Player1")
	char.Position=331280.311073, -6109.31555464, 114156.643	

def IrPosicion4():
	char=Bladex.GetEntity("Player1")
	char.Position=355109.461721, -369.336441421, 51080.9139		

def IrPosicion5():
	char=Bladex.GetEntity("Player1")
	char.Position=432969.210646, 4883.65153572, 42795.0658	

def IrPosicion6():
	char=Bladex.GetEntity("Player1")
	char.Position=501700, 7879, 31700


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
