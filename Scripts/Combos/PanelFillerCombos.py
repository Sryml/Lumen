import Bladex
import Language
import PanelFillerCommon
from PanelFillerCommon import relative, relativev, center, bottom, left, right, buttonOffset, buttonTextPosition

WeaponsCombosAmz = ["${AttackIcon:Attack}${Down} ${PlusIcon} ${Up}","${AttackIcon:Attack}${Up} ${PlusIcon} ${Down}","${AttackIcon:Attack} ${PlusIcon} ${Down}${Right}","${AttackIcon:Attack}${Right} ${PlusIcon} ${Left}","${AttackIcon:Attack} ${PlusIcon} ${Left}${Down}","${AttackIcon:Attack}${Left} ${PlusIcon} ${Left}","${AttackIcon:Attack}${Up} ${PlusIcon} ${Up}${Right}","${AttackIcon:Attack}${Left} ${PlusIcon} ${Left}${Up}","${AttackIcon:Attack}${Right} ${PlusIcon} ${Left:ignore}${Right:ignore}${ignore:UseAndLeftRight}","${AttackIcon:Attack}${Up} ${PlusIcon} ${AttackIcon:Attack}${Up}","${AttackIcon:Attack} ${PlusIcon} ${Up:ignore}${Down:ignore}${ignore:Turn Around}","${AttackIcon:Attack} ${PlusIcon} ${Left:ignore}${Right:ignore}${ignore:UseAndLeftRight} ${PlusIcon} ${Up:ignore}${Down:ignore}${ignore:Turn Around}","${AttackIcon:Attack}${Down} ${PlusIcon} ${AttackIcon:Attack}${Down}"]
WeaponsCombosBarb = ["${AttackIcon:Attack}${Up} ${PlusIcon} ${Down}", "${AttackIcon:Attack}${Down} ${PlusIcon} ${AttackIcon:Attack}${Down}", "${AttackIcon:Attack}${Up} ${PlusIcon} ${Down:ignore}${Up:ignore}${ignore:Turn Around}", "${AttackIcon:Attack}${Right} ${PlusIcon} ${AttackIcon:Attack}${Right}", "${AttackIcon:Attack}${Left} ${PlusIcon} ${Right}", "${AttackIcon:Attack}${Down} ${PlusIcon} ${AttackIcon:Attack}${Down} ${PlusIcon} ${Up}", "${AttackIcon:Attack}${Left} ${PlusIcon} ${Up}${Right}", "${AttackIcon:Attack} ${PlusIcon} ${Left:ignore}${Right:ignore}${ignore:UseAndLeftRight}", "${AttackIcon:Attack}${Up} ${PlusIcon} ${Down}", "${AttackIcon:Attack}${Left} ${PlusIcon} ${AttackIcon:Attack}${Left}", "${AttackIcon:Attack}${Right} ${PlusIcon} ${Down}${Left}", "${AttackIcon:Attack}${Up} ${PlusIcon} ${Left:ignore}${Right:ignore}${ignore:UseAndLeftRight}"]
WeaponsCombosDwarf = ["${AttackIcon:Attack}${Down} ${PlusIcon} ${Up}", "${AttackIcon:Attack}${Up} ${PlusIcon} ${Down}", "${AttackIcon:Attack}${Right} ${PlusIcon} ${Left}${Down}", "${AttackIcon:Attack}${Up} ${PlusIcon} ${Left}${Down}", "${AttackIcon:Attack}${Right} ${PlusIcon} ${Left}", "${AttackIcon:Attack}${Right} ${PlusIcon} ${Left}${Up}", "${AttackIcon:Attack} ${PlusIcon} ${Down}", "${AttackIcon:Attack}${Down} ${PlusIcon} ${Down}", "${AttackIcon:Attack}${Up} ${PlusIcon} ${Up}", "${AttackIcon:Attack}${Up} ${PlusIcon} ${Up:ignore}${Down:ignore}${ignore:Turn Around}", "${AttackIcon:Attack} ${PlusIcon} ${Up}", "${AttackIcon:Attack}${Left} ${PlusIcon} ${Right}", "${AttackIcon:Attack}${Up} ${PlusIcon} ${Down}${Right}"]
WeaponsCombosKgt = ["${AttackIcon:Attack} ${PlusIcon} ${Left}${Up}", "${AttackIcon:Attack} ${PlusIcon} ${Down}${Right}", "${AttackIcon:Attack}${Left} ${PlusIcon} ${Up}", "${AttackIcon:Attack} ${PlusIcon} ${Up}${Right}", "${AttackIcon:Attack}${Down} ${PlusIcon} ${Up}", "${AttackIcon:Attack}${Up} ${PlusIcon} ${Down}", "${AttackIcon:Attack}${Right} ${PlusIcon} ${Left}", "${AttackIcon:Attack} ${PlusIcon} ${Down}", "${AttackIcon:Attack} ${PlusIcon} ${Up:ignore}${Down:ignore}${ignore:Turn Around} ${PlusIcon} ${Up}", "${AttackIcon:Attack}${Down} ${PlusIcon} ${Up}${Right}", "${AttackIcon:Attack}${Right} ${PlusIcon} ${AttackIcon:Attack}${Right} ${PlusIcon} ${Left}", "${AttackIcon:Attack} ${PlusIcon} ${Left}${Down}", "${AttackIcon:Attack}${Up} ${PlusIcon} ${Left:ignore}${Right:ignore}${ignore:UseAndLeftRight}"]

tilePosition = [
[0.389,0.242], [0.289,0.316], [0.289,0.389], [0.289,0.461], [0.289, 0.534], [0.289, 0.607], [0.289, 0.68],
[0.496, 0.316], [0.496, 0.389], [0.496, 0.461], [0.496, 0.534], [0.496, 0.607], [0.496, 0.68]
]
barbTilePosition = [
[0.289,0.244], [0.289,0.333], [0.289,0.42], [0.289, 0.503], [0.289, 0.589], [0.289, 0.67],
[0.493, 0.244], [0.493, 0.333], [0.493, 0.42], [0.493, 0.503], [0.493, 0.589], [0.493, 0.67]
]
titleOffset = [0.044,0]
barbTitleOffset = [0.049,0]
descOffset = [0.044,0.015]
barbDescOffset = [0.049,0.018]
comboOffset = [0.044,0.045]
barbComboOffset = [0.052,0.052]
attackOffset = [0,0]
levelOffset = [0.213, 0.048] # right
barbLevelOffset = [0.197, 0.064] # right
defenseOffset = [0.036, 0.05] # right
barbDefenseOffset = [0.043, 0.066] # right

combos = PanelFillerCommon.GetEmptyData()

elemToDisplay = ["Title", "Attack", "Defense", "Descr", "Level", "Combo"]

def CheckBarbRightTitleOffset(index, position):
	if index > 5:
		return position + 0.002
	return position

def CheckBarbBottomOffset(index, position):
	return position - ((index%6)*0.0025)

def CheckLeftTitleOffset(index, position):
	if index < 7 and index > 0:
		return position - 0.003
	return position

def RemoveNewLine(line):
	line = string.replace(line, "\r", "")
	line = string.replace(line, "\n", "")
	return line

def CheckLeftLevelOffset(index, position):
	if index < 7 and index > 0:
		return position - 0.015
	return position

def CheckLeftDefenseOffset(index, position):
	if index < 7 and index > 0:
		return position - 0.002
	return position

def CheckBottomTileOffset(index, position):
	if index%6 == 0:
		return position - 0.004
	return position

def CheckButtonOffset(index, position):
	if index > 3:
		return position + 0.007
	return position

def FillCombosText(parent):
	global CombosWidget
	charKind = Bladex.GetEntity("Player1").Kind
	PanelFillerCommon.SetParentScale(parent)

	widget = parent

	language = PanelFillerCommon.GetLanguageFallback()
	global combos
	execfile("../../SCRIPTS/Combos/" + language + "/PanelCombosLoca.py")
	for elem in elemToDisplay:
		index = 0
		if elem == "Combo":
			if charKind == "Amazon_N":
				texts = WeaponsCombosAmz
			elif charKind == "Barbarian_N":
				texts = WeaponsCombosBarb
			elif charKind == "Dwarf_N":
				texts = WeaponsCombosDwarf
			else:
				texts = WeaponsCombosKgt
		else:
			texts = combos[language][charKind][elem]
		for text in texts:
			if text == -1:
				index = index + 1
				continue
			name = language + charKind + elem + str(index)
			currTilePos = tilePosition
			if charKind == "Barbarian_N":
				currTilePos = barbTilePosition
			font = PanelFillerCommon.CheckFontChineseFallback(elem)
			CombosWidget=PanelFillerCommon.InitWidget(widget, name, text, font, elem)
			alignX = left
			alignY = bottom
			if elem == "Title":
				currOffset = titleOffset
				posX = CheckLeftTitleOffset(index, currTilePos[index][0] + currOffset[0])
				posY = currTilePos[index][1] + currOffset[1]
				if charKind == "Barbarian_N":
					currOffset = barbTitleOffset
					posX = CheckBarbRightTitleOffset(index, currTilePos[index][0] + currOffset[0])
					posY = currTilePos[index][1] + currOffset[1]
			elif elem == "Descr":
				currOffset = descOffset
				CombosWidget.SetColor(238,225,183)
				posX = CheckLeftTitleOffset(index, currTilePos[index][0] + currOffset[0])
				if charKind == "Barbarian_N":
					currOffset = barbDescOffset
					posX = CheckBarbRightTitleOffset(index, currTilePos[index][0] + currOffset[0])
				posY = currTilePos[index][1] + currOffset[1]
			elif elem == "Defense":
				alignX = right
				currOffset = defenseOffset
				CombosWidget.SetColor(255,17,13)
				posX = CheckLeftDefenseOffset(index, currTilePos[index][0] + currOffset[0])
				posY = CheckBottomTileOffset(index, currTilePos[index][1] + currOffset[1])
				if charKind == "Barbarian_N":
					currOffset = barbDefenseOffset
					posX = currTilePos[index][0] + currOffset[0]
					posY = CheckBarbBottomOffset(index, currTilePos[index][1] + currOffset[1])
			elif elem == "Attack":
				CombosWidget.SetColor(202,216,16)
				posX = currTilePos[index][0]
				posY = currTilePos[index][1]
			elif elem == "Level":
				alignX = right
				currOffset = levelOffset
				CombosWidget.SetColor(141,215,251)
				posX = CheckLeftLevelOffset(index, currTilePos[index][0] + currOffset[0])
				posY = CheckBottomTileOffset(index, currTilePos[index][1] + currOffset[1])
				if charKind == "Barbarian_N":
					currOffset = barbLevelOffset
					posX = PanelFillerCommon.CheckBarbRightLevelOffset(index, currTilePos[index][0] + currOffset[0])
					posY = CheckBarbBottomOffset(index, currTilePos[index][1] + currOffset[1])
			elif elem == "Combo":
				currOffset = comboOffset
				if charKind == "Barbarian_N":
					currOffset = barbComboOffset
				posX = currTilePos[index][0] + currOffset[0]
				posY = currTilePos[index][1] + currOffset[1]
			posX = PanelFillerCommon.CorrectPosX(posX)
			posY = PanelFillerCommon.CorrectPosY(posY)
			widget.AddWidget(CombosWidget,posX,posY,relative,alignX,relativev,alignY)
			index = index + 1
