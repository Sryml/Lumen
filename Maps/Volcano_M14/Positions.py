import Bladex
import BInput

InputManager=BInput.GetInputManager()
InputManager.SetInputActionsSet("Default")

ON_RELEASE=0
ON_PRESS=1


posicion1=IrPosicion1
posicion2=IrPosicion2
posicion3=IrPosicion3
posicion4=IrPosicion4
posicion5=IrPosicion5


Bladex.AddInputAction("GoToPos1", 0)
Bladex.AddInputAction("GoToPos2", 0)
Bladex.AddInputAction("GoToPos3", 0)
Bladex.AddInputAction("GoToPos4", 0)
Bladex.AddInputAction("GoToPos5", 0)


Bladex.AssocKey("GoToPos1", "Keyboard", "Numpad1", ON_PRESS)
Bladex.AssocKey("GoToPos2", "Keyboard", "Numpad2", ON_PRESS)
Bladex.AssocKey("GoToPos3", "Keyboard", "Numpad3", ON_PRESS)
Bladex.AssocKey("GoToPos4", "Keyboard", "Numpad4", ON_PRESS)
Bladex.AssocKey("GoToPos5", "Keyboard", "Numpad5", ON_PRESS)


Bladex.AddBoundFunc("GoToPos1", posicion1)
Bladex.AddBoundFunc("GoToPos2", posicion2)
Bladex.AddBoundFunc("GoToPos3", posicion3)
Bladex.AddBoundFunc("GoToPos4", posicion4)
Bladex.AddBoundFunc("GoToPos5", posicion5)
