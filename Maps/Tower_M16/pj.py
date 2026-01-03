import Actions
import AniSound
import Reference
import Basic_Funcs
import Sparks
import ItemTypes

char=Bladex.CreateEntity("Player1","Amazon_N",0,0,0,"Person")
#char=Bladex.CreateEntity("Player1","Knight_N",0,0,0,"Person")
#char=Bladex.CreateEntity("Player1","Barbarian_N",0,0,0,"Person")
#char=Bladex.CreateEntity("Player1","Dwarf_N",0,0,0,"Person")


char.Position=-41198,2142,-118553
char.Angle=4.6483
char.Level=18	

char.SendTriggerSectorMsgs=1
char.Data=Basic_Funcs.PlayerPerson(char)
inv=char.GetInventory()

o=Bladex.CreateEntity("WeaponInvPrb3","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddBow("WeaponInvPrb3")

o=Bladex.CreateEntity("QuiverInvPrb1","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv=char.GetInventory()
inv.AddQuiver("QuiverInvPrb1")



###AMAZONA

o=Bladex.CreateEntity("WeaponInvPrb1","Naginata2",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)
inv.AddWeapon(o.Name)

o=Bladex.CreateEntity("WeaponInvPrb1","SteelFeather",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddWeapon(o.Name)

o=Bladex.CreateEntity("WeaponInvPrb1","BladeSword2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddWeapon(o.Name)

###BARBARO

"""
o=Bladex.CreateEntity("WeaponInvPrb1","Hacharrajada",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)
inv.AddWeapon(o.Name)

o=Bladex.CreateEntity("WeaponInvPrb1","FireBigSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddWeapon(o.Name)

o=Bladex.CreateEntity("WeaponInvPrb1","BladeSwordBarbarian",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddWeapon(o.Name)

#o=Bladex.CreateEntity("WeaponInvPrb1","BladeSword2Barbarian",0,0,0,"Weapon")
#ItemTypes.ItemDefaultFuncs (o)
#inv.AddWeapon(o.Name)

"""
###CABALLERO

"""
o=Bladex.CreateEntity("WeaponInvPrb1","Espadafilo",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)
inv.AddWeapon(o.Name)

o=Bladex.CreateEntity("WeaponInvPrb1","IceSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddWeapon(o.Name)

o=Bladex.CreateEntity("WeaponInvPrb1","BladeSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddWeapon(o.Name)


o=Bladex.CreateEntity("EscudoInvPrb1","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddShield(o.Name)


o=Bladex.CreateEntity("EscudoInvPrb2","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddShield(o.Name)
"""


###ENANO

"""
o=Bladex.CreateEntity("WeaponInvPrb1","Hacha2",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)
inv.AddWeapon(o.Name)

o=Bladex.CreateEntity("WeaponInvPrb1","BladeSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddWeapon(o.Name)

o=Bladex.CreateEntity("WeaponInvPrb1","FireAxe",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddWeapon(o.Name)

o=Bladex.CreateEntity("EscudoInvPrb1","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddShield(o.Name)


o=Bladex.CreateEntity("EscudoInvPrb2","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddShield(o.Name)

"""
