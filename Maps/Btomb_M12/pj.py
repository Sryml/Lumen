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

char.Position=325982, -105, -221910
char.Angle=0.0
char.Level=10


char.SendTriggerSectorMsgs=1
char.Data=Basic_Funcs.PlayerPerson(char)
inv=char.GetInventory()

o=Bladex.CreateEntity("WeaponInvPrb3","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddBow(o.Name)

o=Bladex.CreateEntity("QuiverInvPrb1","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver(o.Name)
"""
o=Bladex.CreateEntity("WeaponInvPrb1","QueenSword",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)

o=Bladex.CreateEntity("WeaponInvPrb1","KingShield",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)
"""
###AMAZONA

o=Bladex.CreateEntity("WeaponInvPrb1","Axpear",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
Actions.TakeObject(char.Name,o.Name)



###BARBARO
"""
o=Bladex.CreateEntity("WeaponInvPrb1","Alfanje",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)

o=Bladex.CreateEntity("WeaponInvPrb1","Hacha2hojas",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)
"""


###ENANO
"""
o=Bladex.CreateEntity("WeaponInvPrb1","Martillo2",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)

o=Bladex.CreateEntity("EscudoInvPrb1","KingShield",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)


o=Bladex.CreateEntity("EscudoInvPrb2","Escudo2",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)


"""



#o=Bladex.CreateEntity("Tablilla3","Tablilla3",0,0,0)
#Actions.TakeObject("Player1","Tablilla3")

