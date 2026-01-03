



import AniSound
import Reference
import Basic_Funcs
import Sparks
import ItemTypes
import Breakings

class PersonData:
	pass

#char=Bladex.CreateEntity("Player1","Amazon_N",0,0,0,"Person")
char=Bladex.CreateEntity("Player1","Knight_N",0,0,0,"Person")
#char=Bladex.CreateEntity("Player1","Barbarian_N",0,0,0,"Person")
#char=Bladex.CreateEntity("Player1","Dwarf_N",0,0,0,"Person")

char.Position = (94000, -3000, 219000)
char.InitPos = 94000, -3000, 219000
	

char.SendTriggerSectorMsgs=1
char.Data=Basic_Funcs.PlayerPerson(char)
inv=char.GetInventory()


o=Bladex.CreateEntity("WeaponInvPrb3","Arco",0,0,0,"Weapon")
inv.AddBow("WeaponInvPrb3")
ItemTypes.ItemDefaultFuncs(Bladex.GetEntity("WeaponInvPrb3"))

o=Bladex.CreateEntity("QuiverInvPrb1","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv=char.GetInventory()
inv.AddQuiver("QuiverInvPrb1")



o=Bladex.CreateEntity("BladeSword","BladeSword",0,0,0,"Weapon")
inv=char.GetInventory()
inv.AddWeapon("BladeSword")
#inv.LinkRightHand("BladeSword")
inv.LinkBack("BladeSword")



o=Bladex.CreateEntity("EscudoInvPrb1","Escudo1",0,0,0)
Sparks.MakeShield("EscudoInvPrb1")
inv=char.GetInventory()
inv.AddShield("EscudoInvPrb1")
#inv.LinkLeftHand("EscudoInvPrb1")
inv.LinkBack("EscudoInvPrb1")
