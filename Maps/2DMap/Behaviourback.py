import Bladex
import Scorer
import math
import Raster
import BUIx
import Gems
import GameText
import GotoMapVars
import lugaresback
import Language

CoolFlag = 1
thispos = 0,0,0

Gems.SetGemColor(Gems.RED_GEM)

Gems.MaximunAlpha =0.99

def EfectoCool():
	global thispos
	global CoolFlag
	Gems.EfectoConcentracion(	thispos,
								"achalay",
								80,#frames
								50.0,#scale
								60.0)

	if CoolFlag:
		Bladex.AddScheduledFunc(Bladex.GetTime() + 0.5,  EfectoCool,())

EfectoCool()

Frame = 0

font_server_behaviour=BUIx.B_FontServer()
font_behaviour=font_server_behaviour.CreateBFont(Language.FontTitle)


#------- LABEL SHOWING-------------
def LabelEntity(entity,text,dx,dy):
	if entity:
		scale = Language.FontScale["M"]
		Zcreen=Raster.GetSize()
		text_wh=(font_behaviour.GetTextWidth(text)*scale,font_behaviour.GetHeight("H")*scale)
		# FIXME: Due to some reason this is not working, re-enalbel next line later.
		Raster.SetFont(font_behaviour.GetPointer())
		text_pos=Bladex.GetScreenXY(entity.Rel2AbsPoint(0.0,0.0,0.0))
		text_x=(text_pos[0] * Zcreen[0]) + (Zcreen[0]/2) - (text_wh[0] / 2.0 + dx)
		text_y=(text_pos[1] * Zcreen[0]) + (Zcreen[1]/2) - (text_wh[1] / 2.0 + dy)
		#Raster.SetTextColor(200,180,180) #Por poner uno cualquiera
		Raster.SetPosition(text_x,text_y)
		Raster.SetTextScale(scale, scale)
		Raster.WriteText(text)

def ShowLabelEntity(Ent):
	Raster.SetTextAlpha(0.3)
	Raster.SetTextColor(255,255,255)
	LabelEntity(Ent, Ent.Name, 0, 0)

def ShowLabelEntity2(Ent):
	Raster.SetTextColor(255, 254, 125)
	Raster.SetTextAlpha(1)
	LabelEntity(Ent, Ent.Name, 0, 0)

vused = 0

def ContRot(Ent):
	Ent.RotateRel(0,0,0,  0,0,1,  0.1)
	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.05,  ContRot,(Ent,))

def SetShields():
	global GoodShield
	global BadShield
	global Cartelitos

	ca = 0
	for ThisGP in Cartelitos:
		# Visible Good shields and Complete Blade Sword
		if (ca < 6):
			if ((GotoMapVars.PlacedTablets[ca]) or (lugaresback.CarriedTablets[ca])):
				Bladex.GetEntity(GoodShield[ca]).PutToWorld()
			else:
				Bladex.GetEntity(BadShield[ca]).PutToWorld()
				ContRot(Bladex.GetEntity(BadShield[ca]))
		ca = ca + 1
	ContRot(Bladex.GetEntity(BadShield[6]))

def NameWrittingFuct(time):

	global thispos
	global Cartelitos
	global Frame
	global CurrentSelected
	global GoodShield
	global BadShield
	global Tablillas
	global vused

	if not vused:
		SetShields()
		vused = 1

	a = 0
	for ThisGP in Cartelitos:
		#if (lugaresback.MapStatus[a] or GotoMapVars.PlacedTablets[a]):
		# Visible Bad shields and Simple Blade Sword
		Ent = Bladex.GetEntity(ThisGP)
		if (a == CurrentSelected):
			thispos = Ent.Position
			Raster.SetTextAlpha(1)
			Raster.SetTextColor(255, 254, 125)
			Ent = Bladex.GetEntity(Cartelitas[a])
		elif (a < 6 and (GotoMapVars.PlacedTablets[a] == 0) and (CarriedTablets[a] != 1)) or (a == 6 and CarriedTablets.count(1)) or a == 7:
			Raster.SetTextAlpha(1)
			Raster.SetTextColor(200,200,200)
		else:
			Raster.SetTextAlpha(0.3)
			Raster.SetTextColor(255,255,255)
		LabelEntity(Ent, Ent.Name, 0, 0)
		a = a + 1

	cam = Bladex.GetEntity("Camera")
	cam.ETarget = "Player1"
	cam.TType = 0
	cam.SType = 0

	# GRAND MAP-------------
	cam.TPos = (-23400,1,-5000)
	cam.Position = -23400,-116000,-5001
	#-----------------------

Bladex.SetAfterFrameFunc("2dMap",NameWrittingFuct)
Bladex.GetEntity("Player1").SetOnFloor()

Scorer.SetVisible(0)

cam = Bladex.GetEntity("Camera")