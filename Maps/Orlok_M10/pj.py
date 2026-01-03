import AniSound
import Reference
import Basic_Funcs
import Sparks
import Breakings
import ItemTypes


class PersonData:
	pass

MainCharS = "AM"

try:
	File = open("../2dmap/2dMapData.txt")
	MainCharS = File.read(2)
	File.close()
except:
	pass

if MainCharS == "KN":
	MainChar = "Knight_N"
if MainCharS == "BR":
	MainChar = "Barbarian_N"
if MainCharS == "DW":
	MainChar = "Dwarf_N"
if MainCharS == "AM":
	MainChar = "Amazon_N"

char = Bladex.CreateEntity("Player1",MainChar,0,0,0,"Person")

#char=Bladex.CreateEntity("Player1","Amazon_N",0,0,0, "Person")
#char=Bladex.CreateEntity("Player1","Knight_N",0,0,0, "Person")
#char=Bladex.CreateEntity("Player1","Barbarian_N",0,0,0, "Person")
#char=Bladex.CreateEntity("Player1","Dwarf_N",0,0,0, "Person")
char.Position=-47000.0, -31500.0, -73000.0
char.Angle=0.0

char.SendTriggerSectorMsgs=1
char.Data=Basic_Funcs.PlayerPerson(char)
char.Level=11

o=Bladex.CreateEntity("WeaponInvPrb1","Gladius",0,0,0,"Weapon")
inv=char.GetInventory()
inv.AddWeapon("WeaponInvPrb1")
inv.LinkBack("WeaponInvPrb1")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("EscudoInvPrb1","Escudo1",0,0,0,"Weapon")
inv=char.GetInventory()
inv.AddShield("EscudoInvPrb1")
ItemTypes.ItemDefaultFuncs(o)
inv.LinkBack("EscudoInvPrb1")

o=Bladex.CreateEntity("EscudoInvPrb2","Escudo2",0,0,0,"Weapon")
inv.AddShield("EscudoInvPrb2")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("WeaponInvPrb3","Arco",0,0,0,"Weapon")
inv.AddBow("WeaponInvPrb3")
ItemTypes.ItemDefaultFuncs(o)

o=Bladex.CreateEntity("QuiverInvPrb1","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs(o)
inv=char.GetInventory()
inv.AddQuiver("QuiverInvPrb1")

