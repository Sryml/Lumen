

import AniSound
import Actions
import AniSound
import Reference
import Basic_Funcs
import Sparks
import ItemTypes

#char=Bladex.CreateEntity("Player1","Amazon_N",0,0,0,"Person")
char=Bladex.CreateEntity("Player1","Knight_N",0,0,0,"Person")
#char=Bladex.CreateEntity("Player1","Barbarian_N",0,0,0,"Person")
#char=Bladex.CreateEntity("Player1","Dwarf_N",0,0,0,"Person")

char.Position=19874.124738, 36425.24621, 25814.8194569
char.Angle=3.14159/2.0
char.Level=8
	

char.SendTriggerSectorMsgs=1
char.Data=Basic_Funcs.PlayerPerson(char)
inv=char.GetInventory()

o=Bladex.CreateEntity("WeaponInvPrb3","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddBow(o.Name)

o=Bladex.CreateEntity("QuiverInvPrb1","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver(o.Name)


###AMAZONA
"""
o=Bladex.CreateEntity("WeaponInvPrb1","Axpear",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)
inv.AddWeapon(o.Name)

"""


###BARBARO
"""
o=Bladex.CreateEntity("WeaponInvPrb1","LongSword",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)
inv.AddWeapon(o.Name)

"""

###CABALLERO

#"""
o=Bladex.CreateEntity("WeaponInvPrb1","HookSword",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)
inv.AddWeapon(o.Name)

o=Bladex.CreateEntity("QueenSword","QueenSword",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)
inv.AddWeapon(o.Name)

o=Bladex.CreateEntity("KingShield","KingShield",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)
inv.AddShield(o.Name)

o=Bladex.CreateEntity("EscudoInvPrb1","Escudo1",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)
inv.AddShield(o.Name)
#"""

###ENANO

"""
o=Bladex.CreateEntity("WeaponInvPrb1","Martillo",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)
inv.AddWeapon(o.Name)


o=Bladex.CreateEntity("EscudoInvPrb1","Escudo1",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)
inv.AddShield(o.Name)

"""