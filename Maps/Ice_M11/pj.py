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

char.Position=-61936.6384469, 22902.952862, 85541.6398723
char.Angle=3.14149612446
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

if char.Kind=="Knight_N":
	o=Bladex.CreateEntity("WeaponInvPrb1","Cimitarra",0,0,0,"Weapon")
	Actions.TakeObject(char.Name,o.Name)
	ItemTypes.ItemDefaultFuncs (o)
	
	o=Bladex.CreateEntity("WeaponInvPrb1","Escudo2",0,0,0,"Weapon")
	Actions.TakeObject(char.Name,o.Name)
	ItemTypes.ItemDefaultFuncs (o)

elif char.Kind=="Amazon_N":
	###AMAZONA
	
	o=Bladex.CreateEntity("WeaponInvPrb1","Crosspear",0,0,0,"Weapon")
	Actions.TakeObject(char.Name,o.Name)
	ItemTypes.ItemDefaultFuncs (o)
	
	o=Bladex.CreateEntity("WeaponInvPrb2","FireBo",0,0,0,"Weapon")
	Actions.TakeObject(char.Name,o.Name)
	ItemTypes.ItemDefaultFuncs (o)

elif char.Kind=="Barbarian_N":
	###BARBARO
	
	o=Bladex.CreateEntity("WeaponInvPrb1","FlatSword",0,0,0,"Weapon")
	Actions.TakeObject(char.Name,o.Name)
	ItemTypes.ItemDefaultFuncs (o)
	
elif char.Kind=="Dwarf_N":
	###ENANO
	o=Bladex.CreateEntity("WeaponInvPrb1","Garrote2",0,0,0,"Weapon")
	Actions.TakeObject(char.Name,o.Name)
	ItemTypes.ItemDefaultFuncs (o)
	
	o=Bladex.CreateEntity("EscudoInvPrb1","Escudo2",0,0,0,"Weapon")
	Actions.TakeObject(char.Name,o.Name)
	ItemTypes.ItemDefaultFuncs (o)

	o=Bladex.CreateEntity("EscudoInvPrb2","Escudo2",0,0,0,"Weapon")
	Actions.TakeObject(char.Name,o.Name)
	ItemTypes.ItemDefaultFuncs (o)