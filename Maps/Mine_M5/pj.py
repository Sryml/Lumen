import Actions
import AniSound
import Reference
import Basic_Funcs
import Sparks
import ItemTypes

#char=Bladex.CreateEntity("Player1","Amazon_N",0,0,0,"Person")
#char=Bladex.CreateEntity("Player1","Knight_N",0,0,0,"Person")
char=Bladex.CreateEntity("Player1","Barbarian_N",0,0,0,"Person")
#char=Bladex.CreateEntity("Player1","Dwarf_N",0,0,0,"Person")

char.Position=52207.2086495, -1149.3599481, -13424.7579349
char.Angle=5.27893307842
char.Level=6


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
o=Bladex.CreateEntity("WeaponInvPrb1","Naginata",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)

o=Bladex.CreateEntity("WeaponInvPrb1","Tridente",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)
"""

###BARBARO

o=Bladex.CreateEntity("WeaponInvPrb1","DeathSword",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)

o=Bladex.CreateEntity("WeaponInvPrb1","Guadanya",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)


###CABALLERO
"""

o=Bladex.CreateEntity("WeaponInvPrb1","ElfSword",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)


o=Bladex.CreateEntity("WeaponInvPrb1","Maza2",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)


o=Bladex.CreateEntity("EscudoInvPrb1","Escudo2",0,0,0)
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)

"""


###ENANO
"""
o=Bladex.CreateEntity("WeaponInvPrb1","Hacha4",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)


o=Bladex.CreateEntity("WeaponInvPrb1","Hacha3",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)


o=Bladex.CreateEntity("EscudoInvPrb1","Escudo2",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)

"""