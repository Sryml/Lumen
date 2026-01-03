import Bladex
import Basic_Funcs
import ItemTypes
import Actions
import Breakings
import Sparks

char=Bladex.CreateEntity("Player1","Barbarian_N",-83243,8785,-127941,"Person")
char.InitPos = -83243,8785,-127941
char.Angle=0.0
char.Data=Basic_Funcs.PlayerPerson(char)
inv=char.GetInventory()


o=Bladex.CreateEntity("FirstBarbarianSword","Chaosword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
Actions.TakeObject("Player1","FirstBarbarianSword")