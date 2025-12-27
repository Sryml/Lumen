import netgame
if netgame.GetNetState() == 1:
	#--------------------[ \/ Server Deathmatch module \/ ]--------------------------#
	import Basic_Funcs
	import Damage
	
	def TimeRespawnAlive(e_name, time):
		pj = Bladex.GetEntity(e_name)
		pj.Alpha = pj.Alpha+0.005
		if pj.Alpha>=1.0:
			pj.Alpha=1.0;
			pj.TimerFunc  = ""
			pj.RemoveFromList("Timer30")
		if pj.InvRight <> '':
			Der          = Bladex.GetEntity(pj.InvRight)
			Der.Alpha=pj.Alpha		
		else:
			INV  = pj.GetInventory()
			i=SearchPlayerDescriptor(e_name)
			sword=Bladex.CreateEntity("WeaponINVPrb1",PlayersList[i][4],0,0,0)
			swordName = sword.Name
			sword.Weapon=1
			Breakings.SetBreakableWS(swordName)
			INV.AddWeapon(swordName)
			INV.LinkRightHand(swordName)
			
			
		if pj.InvLeft <> '':
			Izq          = Bladex.GetEntity(pj.InvLeft)
			Izq.Alpha=pj.Alpha
		else:
			INV  = pj.GetInventory()
			i=SearchPlayerDescriptor(e_name)
			Shield = Bladex.CreateEntity("escudo",PlayersList[i][5],0,0,0)
			shieldname = Shield.Name
			Sparks.MakeShield(shieldname)
			Breakings.SetBreakableWS(shieldname)
			
			Sparks.MakeShield(shieldname)
			INV.AddShield(shieldname)
			INV.LinkLeftHand(shieldname)
	
	def TimeRespawnDisolve(e_name, time):
		pj = Bladex.GetEntity(e_name)
		pj.Alpha = pj.Alpha-0.0025
		if pj.Alpha<=0.0 :
			pj.Alpha = 0.01
			pj.TimerFunc  = TimeRespawnAlive
			pj.Data.ReSpawn(e_name)
			pj.Position = netgame.GetNextPosition()		
			
	
		if pj.InvRight <> '':
			Der          = Bladex.GetEntity(pj.InvRight)
			Der.Alpha=pj.Alpha
		if pj.InvLeft <> '':
			Izq          = Bladex.GetEntity(pj.InvLeft)
			Izq.Alpha=pj.Alpha
	
	def ReSpawPlayer(name):
		pj = Bladex.GetEntity(name)
		pj.SubscribeToList("Timer30")
		pj.TimerFunc  = TimeRespawnDisolve
	
	
	def ReadUserString(id,type,cad):
	  print `type`+" : "+cad
	
	PlayersList=[[-1,char.Name,netdata[0],netdata[1],netdata[2],netdata[3],0]] # Lista de jugadores
	#                    0:netid    1:object   2:Name    3:Race       4:Weapon      5:Shield     6:Frags
	
	def FillFrags():
		s=""
		for x in PlayersList:
			s = s+"\n"+x[2]+": "+`x[6]`
		wPlayersFrags.SetText(s)
		netgame.SendUserString(0,s)
	
	def JoinFunc(id,objname,name,race,weapon,shield):
	
		print name," has join to the arena:"	
		
		PlayersList.append([ id, objname, name, race, weapon, shield, 0])     # Lo agrega a la lista de jugadores con frags = 0
		
		CHAR = Bladex.GetEntity(objname)
		CHAR.Level=0
		CHAR.PartialLevel=0
		CHAR.SendTriggerSectorMsgs=1
		CHAR.Data=Basic_Funcs.PlayerPerson(CHAR)
		
		INV  = CHAR.GetInventory()
		
		sword=Bladex.CreateEntity("WeaponINVPrb1",weapon,0,0,0)
		swordName = sword.Name
		sword.Weapon=1
		Breakings.SetBreakableWS(swordName)
		INV.AddWeapon(swordName)
		INV.LinkRightHand(swordName)
		print "  weapon :",weapon
		
		# Crea el escudo
		Shield = Bladex.CreateEntity("escudo",shield,0,0,0)
		shieldname = Shield.Name
		Sparks.MakeShield(shieldname)
		Breakings.SetBreakableWS(shieldname)
		
		Sparks.MakeShield(shieldname)
		INV.AddShield(shieldname)
		INV.LinkLeftHand(shieldname)
		print "  weapon :",shield
		FillFrags()
	
		#### Probando arco y flecha ####
		
		o=Bladex.CreateEntity("WeaponInvPrb3","Arco",0,0,0)
		o.Weapon=1
		INV.AddBow(o.Name)	
		
		o=Bladex.CreateEntity("QuiverInvPrb1","Carcaj",0,0,0)
		ItemTypes.ItemDefaultFuncs (o)
		INV=CHAR.GetInventory()
		INV.AddQuiver(o.Name)
	
		#### Probando arco y flecha ####
		
		o=Bladex.CreateEntity("WeaponInvPrb1","Hacha",0,0,0)
		name = o.Name
		o.Weapon=1
		INV=CHAR.GetInventory()
		INV.AddWeapon(name)	
		
		o=Bladex.CreateEntity("EscudoInvPrb3","Escudo3",0,0,0)
		name = o.Name
		o.Weapon=1
		INV.AddShield(name)	
	
	def ByeFunc(i,s):
		global PlayersList
		print "Bye Bye "+s
		id = SearchPlayerId(i)
		if id != -1:
			PlayersList.remove(PlayersList[id])
			FillFrags()
			pj = Bladex.GetEntity(s)
			pj.SubscribeToList("Pin")
		
	
	def SearchPlayerDescriptor(entity):
		global PlayersList
		for i in range(len(PlayersList)):
			if PlayersList[i][1] == entity:
				return i
		return -1
	
	def SearchPlayerId(id):
		global PlayersList
		for i in range(len(PlayersList)):
			if PlayersList[i][0] == id:
				return i
		return -1
			
	netgame.SetJoinPlayerFunc(JoinFunc)
	netgame.SetByePlayerFunc(ByeFunc)
	netgame.SetStringUserFunc(ReadUserString)
	
	def PlayerHurt( VictimName, AttackerName, Life, prevLife):
		global PlayersList
		print VictimName+" <- "+AttackerName+" Life:"+`Life`+" Previous life:"+`prevLife`
		if Life <= 0:
			if prevLife >= 0:
				x = SearchPlayerDescriptor(AttackerName)
				if x != -1:
					PlayersList[x][6] = PlayersList[x][6]+1
					print VictimName+" killed by "+AttackerName
					print AttackerName+" "+`PlayersList[x][6]`+" frags"
					FillFrags()								
					ReSpawPlayer(VictimName)
					#Bladex.AddScheduledFunc(Bladex.GetTime()+15.0,ReSpawPlayer,(VictimName,))
				else:
					print "Error, "+AttackerName+"Not found"
	
	Damage.PlayerHitFunc = PlayerHurt
	
	FillFrags()
	
	print "Server:DeathMatch Mode"
	#--------------------[ /\ Server Deathmatch module /\ ]--------------------------#
else:
	#--------------------[ \/ Client deathmatch module \/ ]--------------------------#
	def ReadUserString(id,type,cad):
		print `type`+" : "+cad
		if(type==0):
			wPlayersFrags.SetText(cad)
			
	
	netgame.SetStringUserFunc(ReadUserString)
	cam = Bladex.GetEntity("Camera")
	cam.PViewType = 3
	print "Client:DeathMatch Mode"
	#--------------------[ /\ Client deathmatch module /\ ]--------------------------#