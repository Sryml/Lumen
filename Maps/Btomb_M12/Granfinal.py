import PhantonFX
import GameText
import AuxFuncs
import EnemyTypes
import ItemTypes
import darfuncs

hacha   = Bladex.CreateEntity(Bladex.GenerateEntityName(), "VampWeapon", 0, 0, 0,"Weapon")
escudo = Bladex.CreateEntity(Bladex.GenerateEntityName(), "VampShield", 0, 0, 0,"Weapon")

Drakula = Bladex.CreateEntity("Drakula", "Vamp", 475631.781, 46365.336, 61025.301,"Person")
EnemyTypes.EnemyDefaultFuncs(Drakula)
Drakula.Blind       = 1
Drakula.Deaf        = 1


Actions.TakeObject(Drakula.Name, hacha.Name)
Actions.TakeObject(Drakula.Name, escudo.Name)

ItemTypes.ItemDefaultFuncs(hacha)
ItemTypes.ItemDefaultFuncs(escudo)
darfuncs.HideBadGuy("Drakula")