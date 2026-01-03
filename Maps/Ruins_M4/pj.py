import AniSound
import Reference
import Basic_Funcs
import Breakings
import ItemTypes



def CreateMainChar():
	char=Bladex.CreateEntity("Player1","Amazon_N",0,0,0,"Person") #"Knight_N",0,0,0,"Person")
	char.Position=69600,-6950,14000
	char.Angle=3.14159/2.0
	char.SendTriggerSectorMsgs=1
	char.Data=Basic_Funcs.PlayerPerson(char)

def CreateInventory():
	char=Bladex.GetEntity("Player1")
	wo=Bladex.CreateEntity("WeaponInvPrb1","Bo",0,0,0,"Weapon") # "Lanza",0,0,0,"Weapon")
	inv=char.GetInventory()
	flag=Reference.GiveWeaponFlag("WeaponInvPrb1")
	inv.AddWeapon("WeaponInvPrb1", flag)
	#inv.LinkRightHand("WeaponInvPrb1")
	inv.LinkBack("WeaponInvPrb1")
	ItemTypes.ItemDefaultFuncs(wo)


def InitLevel():
	CreateMainChar()
	CreateInventory()


InitLevel()
