import ScorerWidgets
import CharStats
import Reference
import Damage
import Bladex
import Scorer
import BUIx
import WidgetsExtra
import Language

DefTextWidget = 0
PowTextWidget = 0
Visible = 0
Color = 0
DefCounter = 0

def Draw():
	global Color
	global DefCounter

	DefCounter = DefCounter+1
	if DefCounter>=10:
		DefCounter = 1
		return

	try: # Cuando se carga una partida, char puede que no este inicializado
		if (Visible):
			char = Bladex.GetEntity("Player1")
			if not char:
				return

			shieldFPow = 0.0
			shieldFDef = 0.0
			weaponFPow = 0.0
			weaponFDef = 0.0

			charFPow= CharStats.GetCharDamageData(char.CharType,char.Level)
			charFPow= max(charFPow, 0)
			charFDef= 0

			charFDef= CharStats.GetCharDefenseData(char.CharType,char.Level) + char.Data.armour_prot_factor
			charFDef= max(charFDef, 0)

			#if (char.InvRight):
			#	WeaponName = char.InvRight
			#else:
			#	WeaponName = char.InvRightBack

			#if (char.InvLeft):
			#	ShieldName = char.InvLeft
			#else:
			#	ShieldName = char.InvLeftBack
			inv= char.GetInventory()
			if inv.HoldingBow:
				WeaponName = char.InvLeft
			else:
				WeaponName = inv.GetActiveWeapon()
			ShieldName = inv.GetActiveShield()

			if WeaponName:
				if Reference.EntitiesObjectData.has_key(WeaponName):
					if Reference.EntitiesObjectData[WeaponName][0] == Reference.OBJ_WEAPON or Reference.EntitiesObjectData[WeaponName][0] == Reference.OBJ_STANDARD or Reference.EntitiesObjectData[WeaponName][0] == Reference.OBJ_ARROW:
						weaponData = Reference.EntitiesObjectData[WeaponName]
						if len (weaponData) > 1:
							weaponFPow = weaponData[1]
							weaponFDef = weaponData[2]
				else:
					kind = Bladex.GetEntity(WeaponName).Kind
					if Reference.DefaultObjectData.has_key(kind):
						if Reference.DefaultObjectData[kind][0] == Reference.OBJ_WEAPON or Reference.DefaultObjectData[kind][0] == Reference.OBJ_STANDARD or Reference.DefaultObjectData[kind][0] == Reference.OBJ_ARROW or Reference.DefaultObjectData[kind][0] == Reference.OBJ_BOW:
							weaponData = Reference.DefaultObjectData[kind]
							if len (weaponData) > 1:
								weaponFPow = weaponData[1]
								weaponFDef = weaponData[2]
			if ShieldName:
				if Reference.EntitiesObjectData.has_key(ShieldName):
					if Reference.EntitiesObjectData[ShieldName][0] ==  Reference.OBJ_SHIELD:
						shieldFPow = Reference.EntitiesObjectData[ShieldName][1]

				else:
					kind = Bladex.GetEntity(ShieldName).Kind
					if Reference.DefaultObjectData.has_key(kind):
						if Reference.DefaultObjectData[kind][0] ==  Reference.OBJ_SHIELD:
							shieldFPow = Reference.DefaultObjectData[kind][1]

			FDefense = char.Data.FDefense
			FAttack = char.Data.FAttack

			if (char.Data.PowerPotion):
				if (Color == 0):
					DefTextWidget.SetColor(255,0,0)
					PowTextWidget.SetColor(255,0,0)
					Color = 1
			else:
				if (Color):
					DefTextWidget.SetColor(0,128,255)
					PowTextWidget.SetColor(0,128,255)
					Color = 0

			damage = int((charFPow * FAttack) + (weaponFPow + shieldFPow))
			defense = int((charFDef * FDefense) + weaponFDef)
			
			import MenuText
			POW = MenuText.GetMenuText("POW")
			DEF = MenuText.GetMenuText("DEF")
			PowTextWidget.SetText(POW + " " + `damage`)
			DefTextWidget.SetText(DEF + " " + `defense`)

			wPowFrame.RecalcLayout()
			wDefFrame.RecalcLayout()

	except Exception,exc:
		print "PowDefWidgets.Draw()",exc


def Deactivate():
	global Visible

	if Visible and PowTextWidget and DefTextWidget:
		PowTextWidget.SetVisible(0)
		DefTextWidget.SetVisible(0)
		PowBmpWidget.SetVisible(0)
		DefBmpWidget.SetVisible(0)

		Visible = 0

def Activate():
	global Visible

	if not Visible and PowTextWidget and DefTextWidget:
		PowTextWidget.SetVisible(1)
		DefTextWidget.SetVisible(1)
		PowBmpWidget.SetVisible(1)
		DefBmpWidget.SetVisible(1)
		Visible = 1


def CreateWidgest():
	global DefTextWidget
	global PowTextWidget

	global DefBmpWidget
	global PowBmpWidget

	global wDefFrame
	global wPowFrame

	wDefFrame=BUIx.B_FrameWidget(Scorer.wFrame,"DefFrame",80,40)
	Scorer.wFrame.AddWidget(wDefFrame,0.09,15,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)

	wPowFrame=BUIx.B_FrameWidget(Scorer.wFrame,"PowFrame",80,40)
	Scorer.wFrame.AddWidget(wPowFrame,0.91,15,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)


	DefTextWidget=WidgetsExtra.B_FlashTextWidget(wDefFrame,"DefText","0",ScorerWidgets.font_server,Language.MapaDeLetrasHi)


	DefTextWidget.SetAlpha(1)
	DefTextWidget.SetColor(0,128,255)
	DefTextWidget.SetText("Def")
	DefTextWidget.SetScale(0.25)
	wDefFrame.AddWidget(DefTextWidget,0.5,0.5,BUIx.B_FrameWidget.B_FR_HRelative,      BUIx.B_FrameWidget.B_FR_HCenter,
	                                          BUIx.B_FrameWidget.B_FR_VRelative,      BUIx.B_FrameWidget.B_FR_VCenter)

	PowTextWidget=WidgetsExtra.B_FlashTextWidget(wPowFrame,"PowText","0",ScorerWidgets.font_server,Language.MapaDeLetrasHi)
	PowTextWidget.SetAlpha(1)
	PowTextWidget.SetColor(0,128,255)
	PowTextWidget.SetText("Pow")
	PowTextWidget.SetScale(0.25)
	wPowFrame.AddWidget(PowTextWidget,0.5,0.5,BUIx.B_FrameWidget.B_FR_HRelative,      BUIx.B_FrameWidget.B_FR_HCenter,
	                                          BUIx.B_FrameWidget.B_FR_VRelative,      BUIx.B_FrameWidget.B_FR_VCenter)



	DefBmpWidget = BUIx.B_BitmapWidget(wDefFrame,"DefBmpWidget",80,40,"MARCADORDEFENSA","../../Data/marcadordefensa.mmp")
	DefBmpWidget.SetColor(255,255,255)
	DefBmpWidget.SetAlpha(1.0)
	wDefFrame.AddWidget(DefBmpWidget,0.5,0.55,BUIx.B_FrameWidget.B_FR_HRelative,      BUIx.B_FrameWidget.B_FR_HCenter,
	                                         BUIx.B_FrameWidget.B_FR_VRelative,      BUIx.B_FrameWidget.B_FR_VCenter)

	PowBmpWidget = BUIx.B_BitmapWidget(wPowFrame,"PowBmpWidget",80,40,"MARCADORATAQUE","../../Data/marcadorataque.mmp")
	PowBmpWidget.SetColor(255,255,255)
	PowBmpWidget.SetAlpha(1.0)
	wPowFrame.AddWidget(PowBmpWidget,0.5,0.55,BUIx.B_FrameWidget.B_FR_HRelative,      BUIx.B_FrameWidget.B_FR_HCenter,
	                                         BUIx.B_FrameWidget.B_FR_VRelative,      BUIx.B_FrameWidget.B_FR_VCenter)

	Deactivate()


def FlashWidgest():
	global DefTextWidget
	global PowTextWidget

	DefTextWidget.SetFlash(22)
	PowTextWidget.SetFlash(22)

	Bladex.AddScheduledFunc (Bladex.GetTime() + 2.0,DefTextWidget.SetFlash,(0,))
	Bladex.AddScheduledFunc (Bladex.GetTime() + 2.0,PowTextWidget.SetFlash,(0,))





