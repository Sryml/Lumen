



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
char=Bladex.CreateEntity("Player1",netdata[1],-1060.49388999, -3200, 2567.27016586,"Person",netdata[2])
char.Angle    = 0.0
char.Position = netgame.GetNextPosition()

	
char=Bladex.GetEntity("Player1")
char.Data=Basic_Funcs.PlayerPerson(char)
