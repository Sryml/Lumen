ON_RELEASE=0
ON_PRESS=1	# default


import Bladex
import BInput

from LumenLib import Inventory

InputManager=BInput.GetInputManager()
InputManager.SetInputActionsSet("Default")  # Me aseguro de definir las acciones en el grupo correcto


Bladex.AssocKey("Forwards","Keyboard","W")
Bladex.AssocKey("FrwdUp","Keyboard","W",ON_RELEASE)
Bladex.AssocKey("FrwdDown","Keyboard","W")
Bladex.AssocKey("Backwards","Keyboard","S")
Bladex.AssocKey("BrwdUp","Keyboard","S",ON_RELEASE)
Bladex.AssocKey("BrwdDown","Keyboard","S")
Bladex.AssocKey("Turn Left","Keyboard","A")
Bladex.AssocKey("Turn Right","Keyboard","D")
Bladex.AssocKey("Jump","Mouse","RightButton")
Bladex.AssocKey("Attack","Mouse","LeftButton")
Bladex.AssocKey("Attack Release","Mouse","LeftButton",ON_RELEASE)
Bladex.AssocKey("Block","Keyboard","LCtrl")
Bladex.AssocKey("Block Release","Keyboard","LCtrl",ON_RELEASE)
Bladex.AssocKey("Throw","Keyboard","Q")
Bladex.AssocKey("Throw Release","Keyboard","Q",ON_RELEASE)
Bladex.AssocKey("Sneak","Keyboard","Shift")
Bladex.AssocKey("Use","Keyboard","E")
Bladex.AssocKey("Toggle Weapons","Keyboard","CapsLock")
Bladex.AssocKey("Cycle Weapons","Mouse","F") # "WheelUp"
Bladex.AssocKey("Cycle Shields","Mouse","R") # "WheelDown"
Bladex.AssocKey("Cycle Objects","Keyboard","C")
Bladex.AssocKey("Select Enemy","Keyboard","Tab")
Bladex.AssocKey("SelectObj","Keyboard","Space")
Bladex.AssocKey("Screen Shot","Keyboard","F2")
Bladex.AssocKey("Next View","Keyboard","Add")
Bladex.AssocKey("Last View","Keyboard","Subtract")

# Inventory
Bladex.AssocKey("Select Last Inventory","Mouse","WheelUp")
Bladex.AssocKey("Select Next Inventory","Mouse","WheelDown")
Bladex.AssocKey("Inventory 1","Keyboard","1")
Bladex.AssocKey("Inventory 2","Keyboard","2")
Bladex.AssocKey("Inventory 3","Keyboard","3")
Bladex.AssocKey("Inventory 4","Keyboard","4")
Bladex.AssocKey("Inventory 5","Keyboard","5")
Bladex.AssocKey("Inventory 6","Keyboard","6")
Bladex.AssocKey("Inventory 7","Keyboard","7")
Bladex.AssocKey("Inventory 8","Keyboard","8")


# Mouse stuff
Bladex.AssocKey("RotateX","Mouse","X_Axis")
Bladex.AssocKey("RotateY","Mouse","Y_Axis")
Bladex.SetMouseState(0,2.000000,2.000000)

# Have a nice day.


