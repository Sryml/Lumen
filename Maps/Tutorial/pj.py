



import AniSound
import Reference
import Basic_Funcs
import Sparks
import Breakings


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

char = Bladex.CreateEntity("Player1",MainChar,0,0,0)

#char=Bladex.CreateEntity("Player1","Knight_N",0,0,0)
char.Position=200148,-3000,45624
char.Person=1
char.Angle=0.0
char=Bladex.GetEntity("Player1")
char.Data=Basic_Funcs.PlayerPerson(char)
char.SetOnFloor()
AniSound.AsignarSonidosCaballero('Player1')
