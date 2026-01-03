



import AniSound
import Reference
import Basic_Funcs
import Sparks
import Breakings

char=Bladex.CreateEntity("Player1","Knight_N",-111000,7500,80000,"Person")
char.Angle=0.0	
char=Bladex.GetEntity("Player1")
char.Data=Basic_Funcs.PlayerPerson(char)
AniSound.AsignarSonidosCaballero('Player1')

char.SendTriggerSectorMsgs=1
