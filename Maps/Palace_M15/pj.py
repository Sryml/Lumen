



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
char.Position=46600,-2950,75000
char.Angle=3.14159/2.0

char.Level=20	

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



o=Bladex.CreateEntity("WeaponInvPrb1","Espadaromana",0,0,0,"Weapon")
inv=char.GetInventory()
inv.AddWeapon("WeaponInvPrb1")
#inv.LinkRightHand("WeaponInvPrb1")
inv.LinkBack("WeaponInvPrb1")



o=Bladex.CreateEntity("EscudoInvPrb1","Escudo1",0,0,0)
Sparks.MakeShield("EscudoInvPrb1")
inv=char.GetInventory()
inv.AddShield("EscudoInvPrb1")
#inv.LinkLeftHand("EscudoInvPrb1")
inv.LinkBack("EscudoInvPrb1")

"""
key1=Bladex.CreateEntity("STAR","LlaveBlanca",0,0,0)
key1.Orientation = 0.7,0.0,0.0,-0.7
key1.Scale = 0.1
key2=Bladex.CreateEntity("BEETLE","LlaveAmarilla",0,0,0)
key2.Orientation = 0.0,-0.7,0.7,0.0
key2.Scale = 0.1
key3=Bladex.CreateEntity("SHELL","LlaveAzul",0,0,0)
key3.Orientation = 0.5,0.5,0.5,-0.5
key3.Scale = 0.1
key4=Bladex.CreateEntity("SPIDER","LlaveNegra",0,0,0)
key4.Orientation = 0.7,0.0,0.0,-0.7
key4.Scale = 0.1

inv=char.GetInventory()
inv.AddSpecialKey("STAR")
inv.AddSpecialKey("BEETLE")
inv.AddSpecialKey("SHELL")
inv.AddSpecialKey("SPIDER")
"""
