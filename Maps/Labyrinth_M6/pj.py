import AniSound
import Reference
import Basic_Funcs
import Sparks
import Breakings
import ItemTypes


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

#char=Bladex.CreateEntity("Player1","Amazon_N",0,0,0,"Person")
#char=Bladex.CreateEntity("Player1","Knight_N",0,0,0,"Person")
#char=Bladex.CreateEntity("Player1","Barbarian_N",0,0,0,"Person")
#char=Bladex.CreateEntity("Player1","Dwarf_N",0,0,0,"Person")
char.Position=23000,9000,-25000
char.Angle=3.14

char.SendTriggerSectorMsgs=1
#char.Level=3
char.Data=Basic_Funcs.PlayerPerson(char)

o=Bladex.CreateEntity("WeaponInvPrb1","Gladius",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv=char.GetInventory()
inv.AddWeapon("WeaponInvPrb1")
inv.LinkBack("WeaponInvPrb1")

o=Bladex.CreateEntity("EscudoInvPrb1","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv.AddShield("EscudoInvPrb1")
inv.LinkBack("EscudoInvPrb1")

o=Bladex.CreateEntity("EscudoInvPrb2","Escudo2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv.AddShield("EscudoInvPrb2")

o=Bladex.CreateEntity("WeaponInvPrb3","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
inv.AddBow("WeaponInvPrb3")

o=Bladex.CreateEntity("QuiverInvPrb1","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs(o)
inv=char.GetInventory()
inv.AddQuiver("QuiverInvPrb1")

