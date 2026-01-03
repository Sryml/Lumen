import netgame
if netgame.GetNetState() == 0:
	import AniSound
	import Reference
	import Basic_Funcs
	import Sparks
	
	
	class PersonData:
		pass
	
	#char=Bladex.CreateEntity("Player1","Amazon_L",0,0,0)
	char=Bladex.CreateEntity("Player1","Knight_N",0,0,0)
	#char=Bladex.CreateEntity("Player1","Barbarian",0,0,0)
	#char=Bladex.CreateEntity("Player1","Dwarf_N",0,0,0)
	#char=Bladex.CreateEntity("Player1","Cos",0,0,0)
	char.Person=1
	char.Position=0.0,-3000,0.0
	char.Angle=3.14159/2.0
	
	
	
	
	
	
	
		
	
	char.SendTriggerSectorMsgs=1
	char.Data=Basic_Funcs.PlayerPerson(char)
	
	o=Bladex.CreateEntity("EscudoInvPrb1","Escudo1",0,0,0)
	Sparks.MakeShield("EscudoInvPrb1")
	inv=char.GetInventory()
	inv.AddShield("EscudoInvPrb1")
	inv.LinkLeftHand("EscudoInvPrb1")
	#inv.LinkBack("EscudoInvPrb1")
	
	
	o=Bladex.CreateEntity("EscudoInvPrb2","Escudo2",0,0,0)
	Sparks.MakeShield("EscudoInvPrb2")
	inv.AddShield("EscudoInvPrb2")
	
	
	#o=Bladex.CreateEntity("EscudoInvPrb3","Escudo3",0,0,0)
	#o.Weapon=1
	#inv.AddShield("EscudoInvPrb3")
	
	
	
	o=Bladex.CreateEntity("WeaponInvPrb1","Espadaromana",0,0,0)
	o.Weapon=1
	inv=char.GetInventory()
	inv.AddWeapon("WeaponInvPrb1")
	inv.LinkRightHand("WeaponInvPrb1")
	#inv.LinkBack("WeaponInvPrb1")
	
	#o=Bladex.CreateEntity("WeaponInvPrb2","Espadacurva",0,0,0)
	#o.Weapon=1
	#inv.AddWeapon("WeaponInvPrb2")
	
	#o=Bladex.CreateEntity("WeaponInvPrb3","Arco",0,0,0)
	#o.Weapon=1
	#inv.AddWeapon("WeaponInvPrb3")
	
	
	
	#o=Bladex.CreateEntity("QuiverInvPrb1","Carcaj",0,0,0)
	#o.Weapon=1
	#inv=char.GetInventory()
	#inv.AddQuiver("QuiverInvPrb1")
	
	#o=Bladex.CreateEntity("QuiverInvPrb2","CarcajFuego",0,0,0)
	#o.Weapon=1
	#inv.AddQuiver("QuiverInvPrb2")
	
	#o=Bladex.CreateEntity("QuiverInvPrb3","CarcajEnvenenado",0,0,0)
	#o.Weapon=1
	#inv.AddQuiver("QuiverInvPrb3")
	
	
	
	#AniSound.AsignarSonidosBarbaro('Player1')
	#AniSound.AsignarSonidosCaballero('Player1')
	#AniSound.AsignarSonidosAmazona('Player1')
	AniSound.AsignarSonidosEnano('Player1')
else:
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
	char=Bladex.CreateEntity("Player1",netdata[1],0,-1200,0)
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
