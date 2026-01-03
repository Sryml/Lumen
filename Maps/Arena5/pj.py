



import AniSound
import Reference
import Basic_Funcs
import Sparks
import Breakings
import netgame
import ItemTypes

netdata = netgame.GetLocalOptions()
print netdata

class PersonData:
	pass
kind = netdata[1]
char=Bladex.CreateEntity("Player1",netdata[1],-24367, -11239, 28623)
char.Person   = 1
char.Angle    = 0.0
char.Position = netgame.GetNextPosition()

	
char=Bladex.GetEntity("Player1")
char.Data=Basic_Funcs.PlayerPerson(char)

if kind == "Knight_N":
	AsignarSonidosCaballero("Player1")
elif kind == "Amazon_L":
	AsignarSonidosAmazona("Player1")
elif kind == "Barbarian":
	AsignarSonidosBarbaro("Player1")
elif kind == "Dwarf_N":
	AsignarSonidosEnano("Player1")		
else:
	print "Sonidos para "+kind+"no implementado"
