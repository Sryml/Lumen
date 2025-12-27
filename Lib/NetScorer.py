import netgame
import BUIx
import CharStats
import Netval
import Bladex
import ScorerWidgets
import WidgetsExtra
import MenuText
import Language
from Reference import ENERGY_LOW_LEVEL
import BInput

wants_auto_scale = 1

VISIBLE=1

CURRENT_STRENGTH_R=251
CURRENT_STRENGTH_G=241
CURRENT_STRENGTH_B=2


__wNULL=BUIx.CreateNULLWidget()
wFrame=BUIx.B_FrameWidget(__wNULL,"MainFrame",640,480)

# Game Information
wPlayerFrame=BUIx.B_FrameWidget(wFrame,"PlayerFrame",640,480)


# life and level
wLeftFrame=BUIx.B_FrameWidget(wPlayerFrame,"BarsFrame",195,65)

wDownFrame=BUIx.B_FrameWidget(wPlayerFrame,"DownFrame",195,73)
wChatFrame=BUIx.B_FrameWidget(wPlayerFrame,"ChatFrame",320,65)

wFragFrame=BUIx.B_FrameWidget(wFrame,"FragFrame",200,200)


Bladex.ReadBitMap("../../Data/Bar.bmp","BitmapBarra")
Bladex.ReadBitMap("../../Data/Vida.bmp","Vida")

wLifeMarker = BUIx.B_BitmapWidget(wLeftFrame,"ObjNameBg",205,51,"MARCADORVIDARED","../../Data/marcadorvidared.mmp");
wLifeMarker.SetColor(255,255,255)
wLifeMarker.SetAlpha(1.0)

BAR_DELTA = 26

wLifeBar=WidgetsExtra.B_FlashBarWidget(wLeftFrame,"LifeBar",116+BAR_DELTA,10)
wLifeBar.SetColor(255,0,0)
wLifeBar.SetFlashColor(53, 141, 36)
wLifeBar.SetFlash(0)
wLifeBar.Continuous= 1
wLifeBar.SetBackgroundAlpha(0.0)
wLifeBar.SetAlpha(1.0)
wLifeBar.SetBitmap("Vida")


##def wLifeBarSizeChanged(x,y):
##  print "wLifeBarSizeChanged",x,y
##
##wLifeBar.SetSizeChangedFunc(wLifeBarSizeChanged)

wLifeLabel=BUIx.B_TextWidget(wLifeBar,"LifeLabel","100/100",ScorerWidgets.font_server,Language.MapaDeLetras)
wLifeLabel.SetColor(255,0,0)
wLifeLabel.SetAlpha(1.0)
wLifeBar.AddLabel(wLifeLabel,4-BAR_DELTA,-2,
                  BUIx.B_Widget.B_LAB_Right,BUIx.B_Widget.B_LAB_VCenter,
                  BUIx.B_Widget.B_FR_AbsoluteLeft,BUIx.B_Widget.B_FR_Left,
                  BUIx.B_Widget.B_FR_AbsoluteTop,BUIx.B_Widget.B_FR_Top
                  )


wPoisonLabel=BUIx.B_TextWidget(wLifeBar,"PoisonLabel",MenuText.GetMenuText("POISONED"),ScorerWidgets.font_server,Language.MapaDeLetras)
wPoisonLabel.SetColor(85,105,60)
wPoisonLabel.SetAlpha(1.0)
wLifeBar.AddLabel(wPoisonLabel,0.4,0.5,
                  BUIx.B_Widget.B_LAB_HCenter,BUIx.B_Widget.B_LAB_VCenter,
                  BUIx.B_Widget.B_FR_HRelative, BUIx.B_Widget.B_FR_HCenter,
                  BUIx.B_Widget.B_FR_VRelative, BUIx.B_Widget.B_FR_VCenter
                  )
wPoisonLabel.SetVisible(0)


wCurrentLevelLabel=BUIx.B_TextWidget(wLifeBar,"CurrentLevelLabel","Level 5",ScorerWidgets.font_server,Language.MapaDeLetras)
wCurrentLevelLabel.SetColor(0,159,220)
wCurrentLevelLabel.SetAlpha(0.5)
wLifeBar.AddLabel(wCurrentLevelLabel,0,5,
                  BUIx.B_Widget.B_LAB_HCenter,BUIx.B_Widget.B_LAB_Bottom,
                  BUIx.B_Widget.B_FR_AbsoluteLeft,BUIx.B_Widget.B_FR_Left,
                  BUIx.B_Widget.B_FR_AbsoluteTop,BUIx.B_Widget.B_FR_Top
                  )

# Frags
wPlayersFrags=BUIx.B_TextWidget(wLifeBar,"FragsLabel","",ScorerWidgets.font_server,Language.LetrasMenu)
wPlayersFrags.SetColor(207,144,49)
wPlayersFrags.SetAlpha(0.8)
wLifeBar.AddLabel(wPlayersFrags,10,5,
                  BUIx.B_Widget.B_LAB_HCenter,BUIx.B_Widget.B_LAB_Bottom,
                  BUIx.B_Widget.B_FR_AbsoluteLeft,BUIx.B_Widget.B_FR_Left,
                  BUIx.B_Widget.B_FR_AbsoluteTop,BUIx.B_Widget.B_FR_Top
                  )


# versus value
wPlayersVS=BUIx.B_TextWidget(wLifeBar,"VersusLabel",MenuText.GetMenuText("Waiting for combat..."),ScorerWidgets.font_server,Language.MapaDeLetras)
wPlayersVS.SetColor(220,220,220)
wPlayersVS.SetAlpha(0.7)
wDownFrame.AddWidget(wPlayersVS,0,0)

# Status of the client
wStatusGame=BUIx.B_TextWidget(wLifeBar,"VersusLabel","",ScorerWidgets.font_server,Language.LetrasMenuSmall)
wStatusGame.SetColor(0,128,255)
wStatusGame.SetAlpha(0.8)
wDownFrame.AddWidget(wStatusGame,0,16)


# Barra de un bar    -------------------------------------------------------------------------------------------
wLowBarFrame=BUIx.B_FrameWidget(wPlayerFrame,"LowBarFrame",176, 22)
wLowBarFrame.SetVisible(1)


wEnergyBmp=BUIx.B_BitmapWidget(wLowBarFrame,"EnergyBmp",176, 22,"MARCADORLANZAMAGOTAM","../../Data/marcadorlanzamagotam.mmp")
wEnergyBmp.SetColor(255,255,255)
wEnergyBmp.SetAlpha(1.0)
wEnergyBmp.SetVisible(1)

# Barra de strength  -------------------------------------------------------------------------------------------
wStrengthBar=ScorerWidgets.B_SmoothBarWidget(wLowBarFrame,"StrengthBar",112*(8.0/6.5),8)
wStrengthBar.SetColor(CURRENT_STRENGTH_R,CURRENT_STRENGTH_G,CURRENT_STRENGTH_B)
wStrengthBar.SetAlpha(0.75)
wStrengthBar.SetBackgroundAlpha(0.0)
wStrengthBar.SetBackgroundColor(CURRENT_STRENGTH_R,CURRENT_STRENGTH_G,CURRENT_STRENGTH_B)
wStrengthBar.SetVisible(0)
wStrengthBar.SetBitmap("Vida")

wMaxPowerLabel=WidgetsExtra.B_FlashTextWidget(wStrengthBar,"MaxPowerLabel",MenuText.GetMenuText("Maximun power"),ScorerWidgets.font_server,Language.MapaDeLetras)
wMaxPowerLabel.SetColor(255,255,255)
wMaxPowerLabel.SetAlpha(1.0)
wMaxPowerLabel.SetVisible(0)
wStrengthBar.AddLabel(wMaxPowerLabel,0.4,0.5,
                  BUIx.B_Widget.B_LAB_HCenter,BUIx.B_Widget.B_LAB_VCenter,
                  BUIx.B_Widget.B_FR_HRelative, BUIx.B_Widget.B_FR_HCenter,
                  BUIx.B_Widget.B_FR_VRelative, BUIx.B_Widget.B_FR_VCenter
                  )

wStrengthLabel=WidgetsExtra.B_FlashTextWidget(wStrengthBar,"StrengthLabel",MenuText.GetMenuText("Launch"),ScorerWidgets.font_server,Language.MapaDeLetras)
wStrengthLabel.SetColor(251,210,99)
wStrengthLabel.SetAlpha(1.0)
wStrengthLabel.SetFlash(0.0)
wStrengthBar.AddLabel(wStrengthLabel,9,0.5,
                  BUIx.B_Widget.B_LAB_Left,BUIx.B_Widget.B_LAB_VCenter,
                  BUIx.B_Widget.B_FR_AbsoluteRight,BUIx.B_Widget.B_FR_Right,
                  BUIx.B_Widget.B_FR_VRelative, BUIx.B_Widget.B_FR_VCenter
                  )

#wStrengthBar.SetBitmap("BitmapBarra")

# Barra de energy  -------------------------------------------------------------------------------------------
wEnergyBar=ScorerWidgets.B_SmoothBarWidget(wLowBarFrame,"EnergyBar",112*(8.0/6.5),8)
wEnergyBar.SetColor(0,255,128)
wEnergyBar.SetAlpha(0.75)
wEnergyBar.SetBackgroundAlpha(0.0)
wEnergyBar.SetBackgroundColor(64,64,64)
wEnergyBar.SetVisible(0)
wEnergyBar.SetBitmap("Vida")

wDangerLabel=WidgetsExtra.B_FlashTextWidget(wEnergyBar,"DangerLabel",MenuText.GetMenuText("Low energy"),ScorerWidgets.font_server,Language.MapaDeLetras)
wDangerLabel.SetColor(238,191,0)
wDangerLabel.SetAlpha(1.0)
wDangerLabel.SetVisible(0)
wEnergyBar.AddLabel(wDangerLabel,0.4,0.5,
                  BUIx.B_Widget.B_LAB_HCenter,BUIx.B_Widget.B_LAB_VCenter,
                  BUIx.B_Widget.B_FR_HRelative, BUIx.B_Widget.B_FR_HCenter,
                  BUIx.B_Widget.B_FR_VRelative, BUIx.B_Widget.B_FR_VCenter
                  )

wEnergyMaxLabel=WidgetsExtra.B_FlashTextWidget(wEnergyBar,"EnergyMaxLabel","100",ScorerWidgets.font_server,Language.MapaDeLetras)
wEnergyMaxLabel.SetColor(0,255,128)
wEnergyMaxLabel.SetAlpha(1)
wEnergyMaxLabel.SetVisible(1)
wEnergyBar.AddLabel(wEnergyMaxLabel,7,0.5,
                  BUIx.B_Widget.B_LAB_Left,BUIx.B_Widget.B_LAB_VCenter,
                  BUIx.B_Widget.B_FR_AbsoluteRight, BUIx.B_Widget.B_FR_Right,
                  BUIx.B_Widget.B_FR_VRelative, BUIx.B_Widget.B_FR_VCenter
                  )


wLowBarFrame.AddWidget(wStrengthBar,56,6)

wLowBarFrame.AddWidget(wEnergyBar,56,6)

wLowBarFrame.AddWidget(wEnergyBmp,0,0)

wChatLines = ["","","",""]

for i in range(len(wChatLines)):
	wChatLines[i]=BUIx.B_TextWidget(wLifeBar,"VersusLabel","",ScorerWidgets.font_server,Language.MapaDeLetras)
	wChatLines[i].SetColor(220,220,220)
	wChatLines[i].SetAlpha((i+1.0)/(len(wChatLines)))
	wChatFrame.AddWidget(wChatLines[i],0,i*14)

wChatInput=BUIx.B_TextWidget(wLifeBar,"Chatinput","",ScorerWidgets.font_server,Language.MapaDeLetras)
wChatInput.SetColor(255,255,255)
wChatInput.SetAlpha(1.0)
wChatFrame.AddWidget(wChatInput,0,5*14)

# FragLimit
wFragLimit=BUIx.B_TextWidget(wFragFrame,"FragLimimit",MenuText.GetMenuText("THE CARNAGE IS OVER"),ScorerWidgets.font_server,Language.LetrasMenuBig)
wFragLimit.SetColor(255,0,0)
wFragLimit.SetAlpha(0.8)
wFragFrame.AddWidget(wFragLimit,0.5,4,
				BUIx.B_FrameWidget.B_FR_HRelative,
				BUIx.B_FrameWidget.B_FR_HCenter,
				BUIx.B_FrameWidget.B_FR_AbsoluteTop,
				BUIx.B_FrameWidget.B_FR_Top)

wFragList=BUIx.B_TextWidget(wFragFrame,"FragLimimit","",ScorerWidgets.font_server,Language.LetrasMenuBig)
wFragList.SetColor(207,144,49)
wFragList.SetAlpha(0.8)
wFragFrame.AddWidget(wFragList,0.5,40,
				BUIx.B_FrameWidget.B_FR_HRelative,
				BUIx.B_FrameWidget.B_FR_HCenter,
				BUIx.B_FrameWidget.B_FR_AbsoluteTop,
				BUIx.B_FrameWidget.B_FR_Top)


##############################################################################################
wFrame.SetVisible(1)
wLeftFrame.SetVisible(1)
wDownFrame.SetVisible(1)
wPlayerFrame.SetVisible(1)
wFragFrame.SetVisible(0)

# muestra la lista grande de frags
def ShowFragLimit(val):
	wPlayerFrame.SetVisible(val)
	wFragFrame.SetVisible(val==0)
	wFragFrame.RecalcLayout()


wPlayerFrame.AddWidget(wLeftFrame,0,0)

wLeftFrame.AddWidget(wLifeBar,14,6)
wLeftFrame.AddWidget(wLifeMarker,1,1)

wPlayerFrame.AddWidget(wDownFrame,0.5,20,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,
                              BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_VCenter)

wPlayerFrame.AddWidget(wChatFrame,20,20,BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_Right,
                              BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)

wFrame.AddWidget(wFragFrame,0.5,0.0,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,
                              BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)

wFrame.AddWidget(wPlayerFrame,0,0)

wPlayerFrame.AddWidget(wLowBarFrame,0.5,2,
                           BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,
                           BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)


Bladex.SetRootWidget(wFrame.GetPointer())

ScrollLimit = 0

def SetStrengthBarValue(v):
  wEnergyBar.SetVisible(0)
  if VISIBLE:
  	wStrengthBar.SetVisible(1)
  old_pos= wStrengthBar.GetPositionPercentage()
  wStrengthBar.SetPositionPercentage(v*(6.5/8.0))

  if v>=1.0:
  	if old_pos<1.0:
	  	wMaxPowerLabel.SetFlash(14)
	  	wStrengthLabel.SetFlash(14)
	  	wMaxPowerLabel.SetVisible(1)
  else:
  	wMaxPowerLabel.SetVisible(0)
  	wStrengthLabel.SetFlash(0.0)

def SetEnergyBarValue(v, max_v):
  wStrengthBar.SetVisible(0)
  if VISIBLE:
  	wEnergyBar.SetVisible(1)
  pos= min(max(v/max_v, 0),1.0)
  wEnergyMaxLabel.SetText(`int(max_v)`)
  wEnergyBar.SetPositionPercentage(pos*(6.5/8.0))
  wEnergyBar.RecalcLabelLayout(BUIx.B_Widget.B_LAB_Left,BUIx.B_Widget.B_LAB_VCenter)
  if pos<=ENERGY_LOW_LEVEL:
  	wDangerLabel.SetFlash(14)
  	wDangerLabel.SetVisible(1)
  else:
  	wDangerLabel.SetVisible(0)

def ScrollChatConsole():
	global ScrollLimit
	for i in range(len(wChatLines)-1):
		wChatLines[i].SetText(wChatLines[i+1].GetTextData())
	wChatLines[len(wChatLines)-1].SetText("")
	ScrollLimit = Bladex.GetTime()+3.0


def ChatClientString(cad):
	ScrollChatConsole()
	wChatLines[len(wChatLines)-1].SetText(cad)


def AddChatString(cad):
	if netgame.GetNetState() != 2:
		ScrollChatConsole()
		wChatLines[len(wChatLines)-1].SetText(cad)
	netgame.SendUserString(Netval.NET_GAME_CHAT_STRING,cad)

NetPlayer = "Player1"

def SetNetPlayerScorer(s):
	global NetPlayer
	NetPlayer = s

LastFragViewerTime = 0

def SwitchFragViewer():
	global LastFragViewerTime

	LastFragViewerTime = Bladex.GetTime()+4.0
	wPlayersFrags.SetVisible(1)

ViewStats          = 0
last_lifeValue     = -100

def NetScorerAfterFrameFunc(time):
	import Actions
	global ScrollLimit
	global NetPlayer
	global LastFragViewerTime
	global last_lifeValue
	global FlickInput

	pj=Bladex.GetEntity(NetPlayer)

	if FlickInput:
		if (time%1)<0.25:
			wChatInput.SetText(InputString+"-")
		elif (time%1)<0.5:
			wChatInput.SetText(InputString+">")
		elif (time%1)<0.75:
			wChatInput.SetText(InputString+"|")
		else:
			wChatInput.SetText(InputString+"<")

	if "NetLife" in dir(pj.Data):
		if "NetLevel" in dir(pj.Data):
			info = netgame.GetPlayerData(NetPlayer)


			if (NetPlayer=="Player1"):
				throw_pressed = Bladex.GetTimeActionHeld ("Throw")
			else:
				throw_pressed = 0
			if throw_pressed:
				SetStrengthBarValue(Actions.ThrowTime2ThrowForce(throw_pressed))
				wLowBarFrame.SetVisible(1)
			else:
				import NetWeapon
				max_energy= NetWeapon.GetEnergy(pj)
				wStrengthBar.SetVisible(0)
				if info[0] < max_energy:
					SetEnergyBarValue(info[0]*1.0, max_energy*1.0)
					wLowBarFrame.SetVisible(1)
				else:
					wStrengthBar.SetVisible(0)
					wLowBarFrame.SetVisible(0)
					wEnergyBar.SetVisible(0)

			if last_lifeValue != info[1]:
				wLifeBar.SetPositionPercentage(info[1]/(pj.Data.NetLife/6.5*8.0))
				wLifeLabel.SetText(str(info[1])+"/"+str(int(pj.Data.NetLife)))
				wLeftFrame.RecalcLayout()
				last_lifeValue = info[1]

			wCurrentLevelLabel.SetText(MenuText.GetMenuText("Level")+" "+str(int(pj.Data.NetLevel)))
			if ScrollLimit<time :
				ScrollChatConsole()
			if LastFragViewerTime<time:
				wPlayersFrags.SetVisible(0)
			if ViewStats:
				wStatusGame.SetText(netgame.ServerInfoBlock())

Bladex.SetAfterFrameFunc("DefaultSelectionData",NetScorerAfterFrameFunc)

def ActivateScorer():
	Bladex.SetRootWidget(wFrame.GetPointer())


wFrame.SetAutoScale(1)
wFragFrame.SetAutoScale(1)
wPlayerFrame.SetAutoScale(1)

if wants_auto_scale:
	wLeftFrame.SetAutoScale(1)

	wDownFrame.SetAutoScale(1)
	wChatFrame.SetAutoScale(1)

	wLifeMarker.SetAutoScale(1)

	wLifeLabel.SetAutoScale(1)
	wLifeBar.SetAutoScale(1)
	wLifeLabel.SetAutoScale(1)
	wPoisonLabel.SetAutoScale(1)
	wCurrentLevelLabel.SetAutoScale(1)
	wPlayersFrags.SetAutoScale(1)
	wPlayersVS.SetAutoScale(1)
	wStatusGame.SetAutoScale(1)
	wLowBarFrame.SetAutoScale(1)
	wEnergyBmp.SetAutoScale(1)
	wStrengthBar.SetAutoScale(1)
	wMaxPowerLabel.SetAutoScale(1)
	wStrengthLabel.SetAutoScale(1)
	wEnergyBar.SetAutoScale(1)
	wDangerLabel.SetAutoScale(1)
	wEnergyMaxLabel.SetAutoScale(1)
	wFragLimit.SetAutoScale(1)
	wFragList.SetAutoScale(1)
	for i in range(len(wChatLines)):
		wChatLines[i].SetAutoScale(1)





def ListenDevice(x,y,z):
	import NetMisc
	global InputString
	if z==1.0:
		if x=="Enter":
			AddChatString("["+NetMisc.PLAYERNAME+"] "+InputString)
			EndInput()
		elif x=="Esc":
			EndInput()
		elif x=="Backspace":
			largo = len(InputString)
			if(largo!=0):
				InputString = InputString[0:largo-1]
		elif x=="Delete":
			InputString = ""
		elif len(x)==1:
			InputString = InputString+x
		elif x=="Decimal":
			InputString = InputString+"."
		elif x=="Period":
			InputString = InputString+"."
		elif x[0:6]=="Numpad":
			InputString = InputString+x[6]
		elif x[0:6]=="Space":
			InputString = InputString+" "

		if len(InputString) > 22:
			InputString = InputString[0:22]

		wChatInput.SetText(InputString)


def StartInput():
	global InputString
	global FlickInput
	if not FlickInput:
		BInput.GetInputManager().GetAttachedDevice("Keyboard").AddListener(Listener)
		InputString = ""
		wChatInput.SetText(InputString)
		FlickInput = 1

def EndInput():
	global InputString
	global FlickInput

	BInput.GetInputManager().GetAttachedDevice("Keyboard").RemoveListener("ChatInput")
	InputString = ""
	wChatInput.SetText(InputString)
	FlickInput = 0

InputString = ""
FlickInput  = 0

Listener=BInput.B_InputListener("ChatInput")
Listener.SetPythonFunc(ListenDevice)
