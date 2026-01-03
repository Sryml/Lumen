import Actions
import Sounds
import Scorer
import OnOff
import ItemTypes

vamp_sha = Bladex.CreateEntity("vampshadow","Vamp",-33000,-65000,-33000,"Person")

weaponvampsha=Bladex.CreateEntity("WeaponVampShadow", "VampWeapon", -33000,-80000,-33000,"Weapon")
ItemTypes.ItemDefaultFuncs(weaponvampsha)

shieldvampsha=Bladex.CreateEntity("ShieldVampShadow", "VampShield", -33000,-80000,-33000,"Weapon")
ItemTypes.ItemDefaultFuncs(shieldvampsha)

Actions.TakeObject("vampshadow", "WeaponVampShadow")
Actions.TakeObject("vampshadow", "ShieldVampShadow")



Ang1 = 1.69
Ang2 = 3.6

	

VSha = Bladex.GetSector(-27000,-25000,31000)
VSha.OnEnter = VampiroShadow
