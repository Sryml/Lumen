import BUIx
import Scorer
import ScorerWidgets
import string
import Bladex
import GameText
import BInput
import Language

WidgetName     = "TutoriaMessage"
LastText       = None
wTraveBookBmp1 = None
wTraveBookBmp2 = None

FadeTutorialScorer = 0

def LoopFadeTutorialScorer(FadeIdx):
	global FadeTutorialScorer
	global wTraveBookBmp1

	if FadeTutorialScorer:
		if FadeIdx>0:
			if FadeIdx>=1:
				wTraveBookBmp1.SetAlpha(FadeIdx-1)
			else:
				wTraveBookBmp1.SetAlpha(0)
		else:
			if FadeIdx<=-1:
				wTraveBookBmp1.SetAlpha(1)
			else:
				wTraveBookBmp1.SetAlpha(-FadeIdx)

		if FadeIdx<=-2.0:
			Bladex.AddScheduledFunc(Bladex.GetTime()+0.01,LoopFadeTutorialScorer,(2,))
		else:
			Bladex.AddScheduledFunc(Bladex.GetTime()+0.01,LoopFadeTutorialScorer,(FadeIdx-0.01,))
	else:
		wTraveBookBmp1.SetVisible(0)
		wTraveBookBmp2.SetVisible(0)
		Scorer.TBookSword.SetVisible(0)
		Scorer.Widget.SetVisible(0)


def LoadTBSamples():
	global wTraveBookBmp1
	global wTraveBookBmp2
	global FadeTutorialScorer

	if not wTraveBookBmp1:
		wTraveBookBmp1 = BUIx.B_BitmapWidget(Scorer.wFrame,"TravelZero",256 * 0.8,192 * 0.8,"TravelZero","../../Data/tb_0_hi.png")
		wTraveBookBmp1.SetColor(255,255,255)
		wTraveBookBmp1.SetAlpha(1.0)
		Scorer.wFrame.AddWidget(wTraveBookBmp1,0.5,0.5,
					BUIx.B_Widget.B_FR_HRelative, BUIx.B_Widget.B_FR_HCenter,
					BUIx.B_Widget.B_FR_VRelative, BUIx.B_Widget.B_FR_VCenter
					)
		wTraveBookBmp1.SetAutoScale(1)

	if not wTraveBookBmp2:
		wTraveBookBmp2 = BUIx.B_BitmapWidget(Scorer.wFrame,"TravelNone",256 * 0.8,192 * 0.8,"TravelNone","../../Data/tb_1_hi.png")
		wTraveBookBmp2.SetColor(255,255,255)
		wTraveBookBmp2.SetAlpha(1.0)
		Scorer.wFrame.AddWidget(
					wTraveBookBmp2,0.5,0.5,
					BUIx.B_Widget.B_FR_HRelative, BUIx.B_Widget.B_FR_HCenter,
					BUIx.B_Widget.B_FR_VRelative, BUIx.B_Widget.B_FR_VCenter
					)
		wTraveBookBmp2.SetAutoScale(1)

	wTraveBookBmp1.SetVisible(1)
	wTraveBookBmp2.SetVisible(1)

	FadeTutorialScorer = 1
	LoopFadeTutorialScorer(2)

def ActivateTutorialScorer(FontFile = Language.MapaDeLetras):
	global wMultiText


	wMultiText=BUIx.B_TextWidget(Scorer.wFrame,WidgetName,"\n\n\n\n\n",ScorerWidgets.font_server,FontFile)
	wMultiText.SetAlpha(1)
	wMultiText.SetColor(255,255,255)
	wMultiText.SetSolid(1)
	wMultiText.SetBackgroundAlpha(0.5)
	wMultiText.SetBackgroundColor(0,0,0)
	wMultiText.SetAutoScale(0)

FlashCicles = 2


def GetAction(ActionName):
	IAction = BInput.GetInputManager().GetInputActions().Find(ActionName)

	for idx in range(IAction.nInputEvents()):
		IEvent  = IAction.GetnInputEvent(idx)
		if(IEvent.GetDevice()=="Keyboard" or IEvent.GetDevice()=="Mouse"):
			return "["+IEvent.GetKey()+"]"
	return "???"


def ParseText(TextIdx):
	txt = GameText.Textos[TextIdx]
	res = []
	for ln in txt:
		start = 0
		while 1:
			start = string.find(ln,"%",start)
			if start == -1: break
			end = string.find(ln,"%",start+1)
			if end   == -1: break
			ln = string.replace(ln,ln[start:end+1],GetAction(ln[start+1:end]))
		res.append(ln)
	return res

#

#
## LIFE AND LEVEL
#######################
def ShowUL(texto,fs=1):
	global FlashCicles
	global LastText
	SPACES = 50
	FlashCicles = fs
	if LastText == texto:
		return
	LastText = texto

	texto = ParseText(texto)
	Scorer.wFrame.RemoveWidget(WidgetName,0)
	cad = "\n"
	for t in texto:
		cad = cad+string.rjust("",SPACES) +t+"  \n"

	wMultiText.SetText(cad+"  \n")
	wMultiText.SetJustification(BUIx.B_TextWidget.B_TEXT_Left)
	wMultiText.SetBackgroundAlpha(0.5)
	wMultiText.SetBackgroundColor(0,0,0)
	wMultiText.SetAlpha(0)
	Scorer.wFrame.AddWidget(wMultiText,0.0,0,
			BUIx.B_FrameWidget.B_FR_AbsoluteLeft,
			BUIx.B_FrameWidget.B_FR_AbsoluteTop,
			BUIx.B_FrameWidget.B_FR_Left,
			BUIx.B_FrameWidget.B_FR_Top)
	CiclicAppears(0)
	global FadeTutorialScorer
	FadeTutorialScorer = 0
	Scorer.wFrame.RecalcLayout()


#
## Center Down
#######################
def ShowBC(texto,fs=1):
	global FlashCicles
	SPACES = 50
	FlashCicles = fs
	global LastText

	if LastText == texto:
		return
	LastText = texto

	texto = ParseText(texto)
	Scorer.wFrame.RemoveWidget(WidgetName,0)
	cad = "\n"
	for t in texto:
		cad = cad+"  "+t+"  \n"

	wMultiText.SetText(cad)
	wMultiText.SetJustification(BUIx.B_TextWidget.B_TEXT_HCenter)
	wMultiText.SetBackgroundAlpha(0.5)
	wMultiText.SetBackgroundColor(0,0,0)
	wMultiText.SetAlpha(0)

	Scorer.wFrame.AddWidget(wMultiText,0.5,50,
				BUIx.B_FrameWidget.B_FR_HRelative,
				BUIx.B_FrameWidget.B_FR_HCenter,
				BUIx.B_FrameWidget.B_FR_AbsoluteBottom,
				BUIx.B_FrameWidget.B_FR_Bottom)
	CiclicAppears(0)
	global FadeTutorialScorer
	FadeTutorialScorer = 0
	Scorer.wFrame.RecalcLayout()


#
## Enemy icons
#######################
def ShowUR(texto,fs=1):
	global FlashCicles
	SPACES = 30
	FlashCicles = fs
	global LastText

	if LastText == texto:
		return
	LastText = texto

	texto = ParseText(texto)
	Scorer.wFrame.RemoveWidget(WidgetName,0)
	cad = "\n"
	for t in texto:
		cad = cad+"  "+t+string.rjust("",SPACES)+"\n"

	wMultiText.SetText(cad+"  \n")
	wMultiText.SetJustification(BUIx.B_TextWidget.B_TEXT_Left)
	wMultiText.SetBackgroundAlpha(0.5)
	wMultiText.SetBackgroundColor(0,0,0)
	wMultiText.SetAlpha(0)
	Scorer.wFrame.AddWidget(wMultiText,0.5,0,
				BUIx.B_FrameWidget.B_FR_AbsoluteRight,
				BUIx.B_FrameWidget.B_FR_Right,
				BUIx.B_FrameWidget.B_FR_AbsoluteTop,
				BUIx.B_FrameWidget.B_FR_Top)
	CiclicAppears(0)
	global FadeTutorialScorer
	FadeTutorialScorer = 0
	Scorer.wFrame.RecalcLayout()


#
## Inventory
#######################
def ShowUC(texto,fs=1):
	global FlashCicles
	SPACES = 30
	FlashCicles = fs
	global LastText

	if LastText == texto:
		return
	LastText = texto

	texto = ParseText(texto)
	Scorer.wFrame.RemoveWidget(WidgetName,0)
	cad = "\n"
	for t in texto:
		cad = cad+"  "+t+"  \n"

	wMultiText.SetText(cad)
	wMultiText.SetJustification(BUIx.B_TextWidget.B_TEXT_HCenter)
	wMultiText.SetBackgroundAlpha(0.5)
	wMultiText.SetBackgroundColor(0,0,0)
	wMultiText.SetAlpha(0)
	Scorer.wFrame.AddWidget(wMultiText,0.5,70,
				BUIx.B_FrameWidget.B_FR_HRelative,
				BUIx.B_FrameWidget.B_FR_HCenter,
				BUIx.B_FrameWidget.B_FR_AbsoluteTop,
				BUIx.B_FrameWidget.B_FR_Top)
	CiclicAppears(0)
	global FadeTutorialScorer
	FadeTutorialScorer = 0
	Scorer.wFrame.RecalcLayout()




def CiclicAppears(id):
	global FlashCicles
	if(id <= 1.0):
		wMultiText.SetAlpha(id)
	elif(id <= FlashCicles*2+1.0):
		c = (id -int(id))
		if int(id)%2==0:
			c = 1.0-c
		c = c*64
		wMultiText.SetBackgroundColor(c,c,c)
	else:
		wMultiText.SetBackgroundColor(0,0,0)
		wMultiText.SetBackgroundAlpha(0.5)
		return
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.01,CiclicAppears,(id+0.08,))

def SimpleDisappears(id):
	global LastText
	LastText = ""

	if(id <= 1.0):
		wMultiText.SetAlpha(1-id)
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.01,SimpleDisappears,(id+0.02,))
	else:
		Scorer.wFrame.RemoveWidget(WidgetName,0)

# "Select Enemy"

##
##GameText.Textos["Demo1"] = ["Four playable characters with individual skills.",
##                            "","",
##                            "An advanced combat system enabling characters to fight",
##                            "with weapons, surronding objects and even severed limbs.",
##                            "","",
##                            "A compelling mixture of fighting and adventuring.",
##                            "","",
##                            "A huge variety of awesome, intelligent monsters.",
##                            "","",
##                            "Thrilling multi-player arena combat.",
##                           ]
##
##GameText.Textos["Demo2"] = ["An ultra-powerfull 3D engine rendering superb",
##                            "animation and stunning environments.",
##                            "","",
##                            "An incredible physic system allowing objects to be thrown, ",
##                            "knocked and bounced off walls.",
##                            "","",
##                            "Destructible Objects which can be burnt or hacked to pieces.",
##                            "","",
##                            "Unique real-time shadow casting, flickering lights and flames.",
##                            "","",
##                            "Realistic reflecting and transparent surfaces.",
##                           ]
##TutorialScorer.wMultiText.SetColor(255,0,0)

# TutorialScorer.ActivateTutorialScorer("../../Data/Letras menu med.bmp")
# TutorialScorer.ShowBC("enemigos2",2)
# TutorialScorer.ShowUL("enemigos2",2)
# TutorialScorer.ShowUR("enemigos2")
# TutorialScorer.ShowUC("Demo1",0)
# TutorialScorer.ShowUC("Demo2",0)
# TutorialScorer.SimpleDisappears(0)


