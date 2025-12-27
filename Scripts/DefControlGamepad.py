ON_RELEASE=0
ON_PRESS=1  # default



import BInput
InputManager=BInput.GetInputManager()
InputManager.SetInputActionsSet("Default")  # Me aseguro de definir las acciones en el grupo correcto


Bladex.AssocKey("Forwards","Gamepad","JoyUp")
Bladex.AssocKey("FrwdUp","Gamepad","JoyUp",ON_RELEASE)
Bladex.AssocKey("FrwdDown","Gamepad","JoyUp")
Bladex.AssocKey("Backwards","Gamepad","JoyDown")
Bladex.AssocKey("BrwdUp","Gamepad","JoyDown",ON_RELEASE)
Bladex.AssocKey("BrwdDown","Gamepad","JoyDown")
Bladex.AssocKey("Turn Left","Gamepad","JoyLeft")
Bladex.AssocKey("Turn Right","Gamepad","JoyRight")
Bladex.AssocKey("Attack","Gamepad","ButtonSouth")
Bladex.AssocKey("Attack Release","Gamepad","ButtonSouth",ON_RELEASE)
Bladex.AssocKey("Block","Gamepad","ButtonLeftShoulder")
Bladex.AssocKey("Block Release","Gamepad","ButtonLeftShoulder",ON_RELEASE)
Bladex.AssocKey("Throw","Gamepad","ButtonRightShoulder")
Bladex.AssocKey("Throw Release","Gamepad","ButtonRightShoulder",ON_RELEASE)
Bladex.AssocKey("Toggle Weapons","Gamepad","ButtonUp")
Bladex.AssocKey("Cycle Weapons","Gamepad","ButtonDown")
Bladex.AssocKey("Cycle Shields","Gamepad","ButtonLeft")
Bladex.AssocKey("Cycle Objects","Gamepad","ButtonRight")
Bladex.AssocKey("Select Enemy","Gamepad","ButtonRightTrigger")
Bladex.AssocKey("Turn Around","Gamepad","ButtonNorth")
Bladex.AssocKey("UseAndLeftRight","Gamepad","ButtonWest")
Bladex.AssocKey("SneakOrSelectPreviousEnemy","Gamepad","ButtonLeftTrigger")
Bladex.AssocKey("SneakOrSelectPreviousEnemyRelease","Gamepad","ButtonLeftTrigger",ON_RELEASE)
Bladex.AssocKey("JumpAndSelectObj","Gamepad","ButtonEast")
Bladex.AssocKey("Screen Shot","Gamepad","ButtonLeftStick")
Bladex.AssocKey("Last View","Gamepad","ButtonRightStick")

# Have a nice day.


