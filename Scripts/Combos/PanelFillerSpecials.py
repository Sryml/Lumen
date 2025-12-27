import Bladex
import Language
import PanelFillerCommon
from PanelFillerCommon import relative, relativev, center, bottom, left, right, buttonOffset, buttonTextPosition

SpecialsCombosAmz = ["${AttackIcon:Attack}${Left} ${PlusIcon} ${Down}${Right}", "${AttackIcon:Attack} ${PlusIcon} ${Left}${Up}", "${AttackIcon:Attack}${Up} ${PlusIcon} ${Down:ignore}${Up:ignore}${ignore:Turn Around}", "${AttackIcon:Attack} ${PlusIcon} ${Up}${Right}", "${AttackIcon:Attack} ${PlusIcon} ${Down}"]
SpecialsCombos2Amz = [-1, -1, -1, -1, "${AttackIcon:Attack} ${PlusIcon} ${AttackIcon:Attack}${Up}"]
SpecialsCombosBarb = ["${AttackIcon:Attack}${Left} ${PlusIcon} ${Down}${Right}", "${AttackIcon:Attack} ${PlusIcon} ${Up} ${PlusIcon} ${Down}", "${AttackIcon:Attack} ${PlusIcon} ${Left}${Down}", "${AttackIcon:Attack} ${PlusIcon} ${Down}"]
SpecialsCombos2Barb = [-1, "${AttackIcon:Attack} ${PlusIcon} ${Up} ${PlusIcon} ${AttackIcon:Attack} ${PlusIcon} ${Left:ignore}${Right:ignore}${ignore:UseAndLeftRight}", -1, "${AttackIcon:Attack} ${PlusIcon} ${AttackIcon:Attack}${Up}"]
SpecialsCombosDwarf = ["${AttackIcon:Attack}${Left} ${PlusIcon} ${Down}${Right}", "${AttackIcon:Attack} ${PlusIcon} ${Down}${Right}", "${AttackIcon:Attack}${Down} ${PlusIcon} ${Down:ignore}${Up:ignore}${ignore:Turn Around}", "${AttackIcon:Attack} ${PlusIcon} ${Left:ignore}${Right:ignore}${ignore:UseAndLeftRight} ${PlusIcon} ${Down:ignore}${Up:ignore}${ignore:Turn Around}", "${AttackIcon:Attack} ${PlusIcon} ${Down}"]
SpecialsCombos2Dwarf = [-1, -1, -1, -1, "${AttackIcon:Attack} ${PlusIcon} ${AttackIcon:Attack}${Up}"]
SpecialsCombosKgt = ["${AttackIcon:Attack}${Left} ${PlusIcon} ${Down}${Right}", "${AttackIcon:Attack} ${PlusIcon} ${Down:ignore}${Up:ignore}${ignore:Turn Around} ${PlusIcon} ${Down}", "${AttackIcon:Attack} ${PlusIcon} ${Down:ignore}${Up:ignore}${ignore:Turn Around} ${PlusIcon} ${Left:ignore}${Right:ignore}${ignore:UseAndLeftRight}", "${AttackIcon:Attack} ${PlusIcon} ${Down}"]
SpecialsCombos2Kgt = [-1, -1, -1, "${AttackIcon:Attack} ${PlusIcon} ${AttackIcon:Attack}${Up}"]

tilePosition = [
[0.39, 0.247],
[0.29, 0.417], [0.29, 0.59],
[0.5, 0.417], [0.5, 0.59]
]

tileBarbPosition = [
[0.29, 0.247], [0.29, 0.507],
[0.5, 0.247], [0.5, 0.507]
]

titleOffset = [0.051,0] # left
attackOffset = [0,0] # left
defenseOffset = [0.044, 0.059] # right
descrOffset = [0.051, 0.023] # left
descr2Offset = [0.051, 0.083] # left
descrBarb2Offset = [0.051, 0.125] # left
comboOffset = [0.053, 0.055] # left
combo2Offset = [0.053, 0.118] # left
comboBarb2Offset = [0.053, 0.16] # left
levelOffset = [0.21, 0.136] # right
level2Offset = [0.21, 0.058] # right
levelBarbOffset = [0.201, 0.226] # right
levelBarb2Offset = [0.201, 0.106] # right
doesHaveSecondAttackKgt = [0, 0, 0, 1]
doesHaveSecondAttackBarb = [0, 1, 0, 1]
doesHaveSecondAttack = [0, 0, 0, 0, 1]

specials = PanelFillerCommon.GetEmptyData()
elemToDisplay = ["Title", "Attack", "Defense", "Descr", "Descr2", "Level", "Level2", "Combo", "Combo2"]

def CheckBarbRightLevelOffset(index, position):
	if index > 1:
		return position + 0.01
	return position

def CheckBarbBottomLevelOffset(index, position):
	if index % 2 == 1:
		return position - 0.01
	return position

def CheckLeftLevelOffset(index, position):
	if index < 3 and index > 0:
		return position - 0.01
	return position

def FillSpecialsText(parent):
	global SpecialsWidget
	charKind = Bladex.GetEntity("Player1").Kind
	PanelFillerCommon.SetParentScale(parent)

	widget = parent
	language = PanelFillerCommon.GetLanguageFallback()
	global specials
	execfile("../../SCRIPTS/Combos/" + language + "/PanelSpecialsLoca.py")
	for elem in elemToDisplay:
		index = 0
		if elem == "Combo":
			if charKind == "Amazon_N":
				texts = SpecialsCombosAmz
			elif charKind == "Barbarian_N":
				texts = SpecialsCombosBarb
			elif charKind == "Dwarf_N":
				texts = SpecialsCombosDwarf
			else:
				texts = SpecialsCombosKgt
		elif elem == "Combo2":
			if charKind == "Amazon_N":
				texts = SpecialsCombos2Amz
			elif charKind == "Barbarian_N":
				texts = SpecialsCombos2Barb
			elif charKind == "Dwarf_N":
				texts = SpecialsCombos2Dwarf
			else:
				texts = SpecialsCombos2Kgt
		else:
			texts = specials[language][charKind][elem]
		for text in texts:
			if text == -1:
				index = index + 1
				continue
			name = language + charKind + elem + str(index)
			font = PanelFillerCommon.CheckFontChineseFallback(elem)
			SpecialsWidget=PanelFillerCommon.InitWidget(widget, name, text, font, elem)
			alignX = left
			alignY = bottom
			if elem == "Title":
				currOffset = titleOffset
			elif elem == "Descr":
				SpecialsWidget.SetColor(238,225,183)
				currOffset = descrOffset
			elif elem == "Descr2":
				SpecialsWidget.SetColor(238,225,183)
				if charKind == "Barbarian_N" or charKind == "Knight_N":
					currOffset = descrBarb2Offset
				else:
					currOffset = descr2Offset
			elif elem == "Defense":
				SpecialsWidget.SetColor(255,17,13)
				alignX = right
				currOffset = defenseOffset
			elif elem == "Attack":
				SpecialsWidget.SetColor(202,216,16)
				currOffset = attackOffset
			elif elem == "Level":
				SpecialsWidget.SetColor(141,215,251)
				if charKind == "Barbarian_N":
					if doesHaveSecondAttackBarb[index] == 0:
						currOffset = levelBarbOffset
					else:
						currOffset = levelBarb2Offset
				elif charKind == "Knight_N":
					if doesHaveSecondAttackKgt[index] == 0:
						currOffset = levelBarbOffset
					else:
						currOffset = levelBarb2Offset
				else:
					if doesHaveSecondAttack[index] == 0:
						currOffset = levelOffset
					else:
						currOffset = level2Offset
				alignX = right
			elif elem == "Level2":
				SpecialsWidget.SetColor(141,215,251)
				if charKind == "Barbarian_N" or charKind == "Knight_N":
					currOffset = levelBarbOffset
				else:
					currOffset = levelOffset
				alignX = right
			elif elem == "Combo":
				currOffset = comboOffset
			elif elem == "Combo2":
				if charKind == "Barbarian_N":
					if doesHaveSecondAttackBarb[index] != 0:
						currOffset = comboBarb2Offset
				elif charKind == "Knight_N":
					if doesHaveSecondAttackKgt[index] != 0:
						currOffset = comboBarb2Offset
				else:
					if doesHaveSecondAttack[index] != 0:
						currOffset = combo2Offset
			currTile = tilePosition
			if charKind == "Barbarian_N" or charKind == "Knight_N":
				currTile = tileBarbPosition
			posX = currTile[index][0] + currOffset[0]
			posY = currTile[index][1] + currOffset[1]
			if elem == "Level" or elem == "Level2":
				if charKind == "Barbarian_N" or charKind == "Knight_N":
					posX = CheckBarbRightLevelOffset(index, posX)
					posY = CheckBarbBottomLevelOffset(index, posY)
				else:
					posX = CheckLeftLevelOffset(index, posX)

			posX = PanelFillerCommon.CorrectPosX(posX)
			posY = PanelFillerCommon.CorrectPosY(posY)
			widget.AddWidget(SpecialsWidget,posX,posY,relative,alignX,relativev,alignY)
			index = index + 1
