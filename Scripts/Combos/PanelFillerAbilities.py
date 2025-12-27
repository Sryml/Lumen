import Bladex
import Language
import PanelFillerCommon
from PanelFillerCommon import relative, relativev, center, bottom, left, right, buttonOffset, buttonTextPosition

AbilitiesCombosAmz = ["${AttackIcon:Attack} ${PlusIcon} ${Left:ignore}${Right:ignore}${ignore:UseAndLeftRight}", "${Left:UseAndLeftRight}${Down}${Right:ignore}"]
AbilitiesCombosBarb = ["${AttackIcon:Attack}${Right} ${PlusIcon} ${AttackIcon:Attack}${Right}", "${JumpIcon:JumpAndSelectObj}${Right} ${PlusIcon} ${AttackIcon:Attack}", "${JumpIcon:JumpAndSelectObj}${Left} ${PlusIcon} ${AttackIcon:Attack}", "${Left:UseAndLeftRight}${Down}${Right:ignore}", "${AttackIcon:Attack}${Left} ${PlusIcon} ${AttackIcon:Attack}${Left}", "${AttackIcon:Attack}${Down} ${PlusIcon} ${AttackIcon:Attack}${Down}", "${AttackIcon:Attack}${Up} ${PlusIcon} ${AttackIcon:Attack}${Up}", "${AttackIcon:Attack} ${PlusIcon} ${Up}", "${AttackIcon:Attack}${Up} ${PlusIcon} ${Left:ignore}${Right:ignore}${ignore:UseAndLeftRight}", "${AttackIcon:Attack} ${PlusIcon} ${Up} ${PlusIcon} ${AttackIcon:Attack}"]
AbilitiesCombosDwarf = ["${JumpIcon:JumpAndSelectObj}${Right} ${PlusIcon} ${AttackIcon:Attack}", "${JumpIcon:JumpAndSelectObj}${Left} ${PlusIcon} ${AttackIcon:Attack}", "${Left:UseAndLeftRight}${Down}${Right:ignore}", "${AttackIcon:Attack} ${PlusIcon} ${Left:ignore}${Right:ignore}${ignore:UseAndLeftRight}"]
AbilitiesCombosKgt = ["${JumpIcon:JumpAndSelectObj}${Right} ${PlusIcon} ${AttackIcon:Attack}", "${JumpIcon:JumpAndSelectObj}${Left} ${PlusIcon} ${AttackIcon:Attack}", "${AttackIcon:Attack} ${PlusIcon} ${Down:ignore}${Up:ignore}${ignore:Turn Around}", "${Left:UseAndLeftRight}${Down}${Right:ignore}", "${AttackIcon:Attack}${Right} ${PlusIcon} ${AttackIcon:Attack}${Right}", "${AttackIcon:Attack}${Left} ${PlusIcon} ${AttackIcon:Attack}${Left}", "${AttackIcon:Attack}${Down} ${PlusIcon} ${AttackIcon:Attack}${Down}", "${AttackIcon:Attack}${Up} ${PlusIcon} ${AttackIcon:Attack}${Up}", "${AttackIcon:Attack} ${PlusIcon} ${Down:ignore}${Up:ignore}${ignore:Turn Around} ${PlusIcon} ${AttackIcon:Attack}"]

tilePosition = [
[0.31, 0.275], [0.31, 0.361], [0.31, 0.449], [0.31, 0.534], [0.31, 0.616], [0.31, 0.696],
[0.515, 0.275], [0.515, 0.361],  [0.515, 0.449], [0.515, 0.534], [0.515, 0.616], [0.515, 0.696]
]

titleOffset = [0,-0.008] # center
attackOffset = [0.027, -0.029] # left
comboOffset = [0.029, 0.011] # left
levelOffset = [0.173, 0.027] # right

abilities = PanelFillerCommon.GetEmptyData()
elemToDisplay = ["Title", "Attack", "Level", "Combo"]

def FillAbilitiesText(parent):
	global AbilitiesWidget
	charKind = Bladex.GetEntity("Player1").Kind
	PanelFillerCommon.SetParentScale(parent)

	widget = parent
	language = PanelFillerCommon.GetLanguageFallback()
	global abilities
	execfile("../../SCRIPTS/Combos/" + language + "/PanelAbilitiesLoca.py")
	for elem in elemToDisplay:
		index = 0
		if elem == "Combo":
			if charKind == "Amazon_N":
				texts = AbilitiesCombosAmz
			elif charKind == "Barbarian_N":
				texts = AbilitiesCombosBarb
			elif charKind == "Dwarf_N":
				texts = AbilitiesCombosDwarf
			else:
				texts = AbilitiesCombosKgt
		else:
			texts = abilities[language][charKind][elem]
		for text in texts:
			name = language + charKind + elem + str(index)
			font = PanelFillerCommon.CheckFontChineseFallback(elem)
			AbilitiesWidget=PanelFillerCommon.InitWidget(widget, name, text, font, elem)
			alignY = bottom
			alignX = left
			if elem == "Attack":
				AbilitiesWidget.SetColor(238,225,183)
				currOffset = attackOffset
			elif elem == "Level":
				AbilitiesWidget.SetColor(141,215,251)
				currOffset = levelOffset
				alignX = right
			elif elem == "Title":
				currOffset = titleOffset
				alignX = center
				alignY = center
				if language == "Russian":
					AbilitiesWidget.SetScale(0.40)
			elif elem == "Combo":
				currOffset = comboOffset
			posX = tilePosition[index][0] + currOffset[0]
			posY = tilePosition[index][1] + currOffset[1]
			if elem == "Level":
				posX = PanelFillerCommon.CheckBarbRightLevelOffset(index, posX)

			posX = PanelFillerCommon.CorrectPosX(posX)
			posY = PanelFillerCommon.CorrectPosY(posY)
			widget.AddWidget(AbilitiesWidget,posX,posY,relative,alignX,relativev,alignY)
			index = index + 1
