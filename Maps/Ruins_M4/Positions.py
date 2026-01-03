import Bladex
import BInput

InputManager=BInput.GetInputManager()
InputManager.SetInputActionsSet("Default")

ON_RELEASE=0
ON_PRESS=1


######## Funcion: IrPosicion1()

######## Funcion: IrPosicion2()

######## Funcion: IrPosicion3()

######## Funcion: IrPosicion4()

######## Funcion: IrPosicion5()

######## Funcion: IrPosicion6()

######## Funcion: IrPosicion7()

######## Funcion: IrPosicion8()

######## Funcion: IrPosicion9()


Bladex.AddInputAction("GoToPos1", 0)
Bladex.AddInputAction("GoToPos2", 0)
Bladex.AddInputAction("GoToPos3", 0)
Bladex.AddInputAction("GoToPos4", 0)
Bladex.AddInputAction("GoToPos5", 0)
Bladex.AddInputAction("GoToPos6", 0)
Bladex.AddInputAction("GoToPos7", 0)
Bladex.AddInputAction("GoToPos8", 0)
Bladex.AddInputAction("GoToPos9", 0)

Bladex.AssocKey("GoToPos1", "Keyboard", "Numpad1", ON_PRESS)
Bladex.AssocKey("GoToPos2", "Keyboard", "Numpad2", ON_PRESS)
Bladex.AssocKey("GoToPos3", "Keyboard", "Numpad3", ON_PRESS)
Bladex.AssocKey("GoToPos4", "Keyboard", "Numpad4", ON_PRESS)
Bladex.AssocKey("GoToPos5", "Keyboard", "Numpad5", ON_PRESS)
Bladex.AssocKey("GoToPos6", "Keyboard", "Numpad6", ON_PRESS)
Bladex.AssocKey("GoToPos7", "Keyboard", "Numpad7", ON_PRESS)
Bladex.AssocKey("GoToPos8", "Keyboard", "Numpad8", ON_PRESS)
Bladex.AssocKey("GoToPos9", "Keyboard", "Numpad9", ON_PRESS)

Bladex.AddBoundFunc("GoToPos1", posicion1)
Bladex.AddBoundFunc("GoToPos2", posicion2)
Bladex.AddBoundFunc("GoToPos3", posicion3)
Bladex.AddBoundFunc("GoToPos4", posicion4)
Bladex.AddBoundFunc("GoToPos5", posicion5)
Bladex.AddBoundFunc("GoToPos6", posicion6)
Bladex.AddBoundFunc("GoToPos7", posicion7)
Bladex.AddBoundFunc("GoToPos8", posicion8)
Bladex.AddBoundFunc("GoToPos9", posicion9)
