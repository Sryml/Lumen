import BBLib
import BUIx
import Raster
import Language
import ScorerWidgets
import MenuText
import Bladex
import Menu
import MenuWidget
import BInput
import acts

class B_GamepadWidget(BUIx.B_FrameWidget):

	def __init__(self,Parent,MenuDesc,menuStack):
		self.controller = Bladex.GetLastUsedController()
		if self.controller == 0:
			self.controller = 2
		self.commands = ["command 1", "command 2", "command 3", "command 4", "command 5", "command 6", "command 7", "command 8", "command 9", "command 10", "command 11", "command 12", "command 13", "command 14", "command 15", "command 16", "command 17", "command 18"]
		self.FillCommands()
		self.positionU = [[-390, 83], [-390, 146], [-390, 191], [-390, 307], [-390, 356], [-390, 405], [-390, 453], [-110, 522], [-110, 562], [110, 562], [110, 522], [360, 354], [360, 327], [360, 299], [360, 271], [380, 191], [380, 146], [380, 83]]

		self.positionX = [[-360, 83], [-380, 156], [-380, 198], [-380, 410], [-380, 449], [-380, 490], [-380, 532], [-380, 280], [-380, 330], [110, 563], [110, 523], [360, 349], [360, 322], [360, 295], [360, 267], [380, 198], [380, 156], [360, 83]]

		self.positionP = [[-370, 87], [-380, 146], [-380, 185], [-380, 283], [-380, 332], [-380, 381], [-380, 430], [-110, 522], [-110, 562], [110, 562], [110, 522], [360, 352], [360, 323], [360, 296], [360, 269], [380, 185], [380, 146], [370, 87]]

		self.positionS = [[-400, 289], [-420, 197], [-420, 228], [-400, 353], [-400, 395], [-400, 437], [-400, 482], [-270, 150], [-270, 108], [270, 108], [270, 150], [380, 451], [380, 420], [380, 351], [380, 386], [420, 228], [420, 197], [400, 289]]
		self.PanelWidgets = []
		self.PanelWidgetsName = []
		self.vidw = 1
		self.vidh = 1
		self.controllerScale = 0.8
		BUIx.B_FrameWidget.__init__(self,Parent,MenuDesc["Name"],self.vidw,self.vidh)
		Size_X, Size_Y = Raster.GetUnscaledSize()
		Parent.SetSize(Size_X, Size_Y)
		self.DisplayController()
		self.gamepad = Raster.BmpHandle(self.gamepadName)
		Raster.SetPenColor(255,255,255);
		self.SetCommandTexts()
		self.SetDrawFunc(self.Draw)

		def MyGamepadChange(controllerType,widget=self):
			widget.OnGamepadChange(controllerType)
	
		Bladex.SetGamepadChangeFunc(MyGamepadChange)

	def OnGamepadChange(self,controllerType):
		self.controller = int(controllerType)
		self.DisplayController()
		self.SetCommandTexts()
		self.gamepad = Raster.BmpHandle(self.gamepadName)
		
	def DisplayController(self):
		if self.controller == 1:
			controllerStr = "Universal"
			self.positions = self.positionU
		elif self.controller == 3:
			controllerStr = "Playstation"
			self.positions = self.positionP
		elif self.controller == 4:
			controllerStr = "Steamdeck"
			self.positions = self.positionS
		else:
			controllerStr = "Xbox"
			self.positions = self.positionX
		self.gamepadName = "gamepad" + str(self.controller)
		Bladex.ReadBitMap("../../DATA/LayoutController_" + controllerStr + ".png", self.gamepadName)

	def Draw(self,x,y,time):
		Size_X, Size_Y = Raster.GetSize()
		scale = (1.0 * Size_Y) / 1080.0
		image_height = Size_Y * self.controllerScale
		image_width = 1920.0 / (1080.0 / image_height)
		Raster.SetPenColor(255,255,255);
		Raster.SetPosition(Size_X/2 - image_width/2, Size_Y/2 - image_height/2 - image_height * 0.2)
		Raster.DrawBitmap(self.gamepad, image_width, image_height)
		self.DefDraw(x,y,time)

	def ResetTexts(self):
		for elem in self.PanelWidgetsName:
			self.RemoveWidget_Idx(0)

		self.PanelWidgets = []
		self.PanelWidgetsName = []
	def SetCommandTexts(self):
		self.ResetTexts()
		Size_X, Size_Y = Raster.GetSize()
		scale = 1
		if Size_Y < 800:
			scale = Size_Y / 800.0
		index = 0
		for pos in self.positions:
			textAlign = BUIx.B_FrameWidget.B_FR_Right
			if index >= (len(self.positions)/2):
				textAlign = BUIx.B_FrameWidget.B_FR_Left
			name = "command " + str(index)
			Widget=BUIx.B_TextWidget(self, name,"",ScorerWidgets.font_server,Language.LetrasMenu)
			Widget.SetAlpha(1)
			Widget.SetColor(207,144,49)
			Widget.SetText(MenuText.GetMenuText(self.commands[index]))
			self.PanelWidgets.append(Widget)
			self.PanelWidgetsName.append(name)
			self.AddWidget(
					Widget,
					pos[0] * scale,
					pos[1] * scale,
					BUIx.B_FrameWidget.B_FR_HRelative,
					textAlign,
					BUIx.B_FrameWidget.B_FR_VRelative,
					BUIx.B_FrameWidget.B_FR_HCenter
					)
			index = index + 1

	def FillCommands(self):
		IManager = BInput.GetInputManager()
		oldInputActionsSet = IManager.GetInputActionsSet()
		IManager.SetInputActionsSet("Default")
		IActions=IManager.GetInputActions()
		for i in acts.ConfigurableActions:
			IAction=IActions.Find(i[1])
			for j in range(IAction.nInputEvents()):
				IEvent=IAction.GetnInputEvent(j)
				IDevice=IEvent.GetDevice()
				IAction=IActions.Find(i[1])
				if IDevice == "Gamepad" :
					if self.GetCommandIndex(IEvent.GetKey()):
						self.commands[self.GetCommandIndex(IEvent.GetKey())] = MenuText.GetMenuText(i[0])

		self.commands[0] = MenuText.GetMenuText("Travel Book")
		self.commands[17] = MenuText.GetMenuText("Menu")
		self.commands[8] = MenuText.GetMenuText("Move")
		self.commands[9] = MenuText.GetMenuText("Camera")

		IManager.SetInputActionsSet(oldInputActionsSet)

	def GetCommandIndex(self, key):
		if key == "ButtonLeftTrigger":
			return 1
		elif key == "ButtonLeftShoulder":
			return 2
		elif key == "ButtonUp":
			return 3
		elif key == "ButtonDown":
			return 4
		elif key == "ButtonLeft":
			return 5
		elif key == "ButtonRight":
			return 6
		elif key == "ButtonLeftStick":
			return 7
		elif key == "ButtonRightStick":
			return 10
		elif key == "ButtonEast":
			return 11
		elif key == "ButtonSouth":
			return 12
		elif key == "ButtonNorth":
			return 13
		elif key == "ButtonWest":
			return 14
		elif key == "ButtonRightShoulder":
			return 15
		elif key == "ButtonRightTrigger":
			return 16

	def AcceptsFocus(self):
		return 0
