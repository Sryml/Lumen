import netgame
import Damage
import Actions
import Netval
import NetWeapon
import NetScorer
import Reference
import Breakings
import string
import NetMisc
import acts
import Language
import MenuText
import AuxFuncs
import darfuncs

#    Estructura de mensajes:
#  0     (Frags)
#  1     (Ordenes)
#  2..10 (Jugador activo)
#
PJ = []

OnStartRoundFunc = ""
OnJoinFunc       = ""
END_OF_ARENA = 0

CameraName = ""
CameraChar = ""
def CameraBreak(Camera,frame):
	global CameraChar
	cam = Bladex.GetEntity("Camera")
	netgame.SetPersonView(CameraChar)
	if netgame.GetNetState() == 1:
		Bladex.GetEntity(CameraChar).UnFreeze()
	cam.Cut()
	if CameraChar == "Player1":
		Bladex.SetListenerPosition(1)
	SetObserverMessage(0)
	if Reference.PYTHON_DEBUG >= 1:
		print "Camera breaks to ",CameraChar
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, FastChapuzaSolution,())


GRANCHAPUZA = 1
def FastChapuzaSolution():
	global GRANCHAPUZA
	if GRANCHAPUZA:
		print "F.CH.S run!"
		netgame.SetPersonView(CameraChar)
		cam = Bladex.GetEntity("Camera")
		cam.Cut()
#		GRANCHAPUZA = 0

def SetCameraData(i,c):
	global CameraName
	global CameraChar

	CameraName = "Player"+`i`+".cam"
	CameraChar = c
	NetScorer.SetNetPlayerScorer(c)


def StartCamera():
	global CameraName
	global CameraChar
	global CameraFrames

	darfuncs.StopMatrixFX()
	cam = Bladex.GetEntity("Camera")

	cam.SetMaxCamera(CameraName,0,CameraFrames)
	cam.AddCameraEvent( -1,CameraBreak)
	Bladex.SetListenerPosition(2)
	AuxFuncs.FadeFrom(1.0,0.1)
	if Reference.PYTHON_DEBUG >= 1:
		print "Camera goes to ",CameraChar

def SetObserverMessage(v):
	if END_OF_ARENA:
		NetScorer.wFragLimit.SetText(MenuText.GetMenuText("THE CARNAGE IS OVER"))
	else:
		NetScorer.wFragLimit.SetText(MenuText.GetMenuText("Waiting for combat..."))
	NetScorer.ShowFragLimit(not v)

language = Language.CheckFallback()

sonido_fight                = Bladex.CreateSound("../../Sounds/"+language+"/NetFight.wav","NetFight")
sonido_fight.MaxDistance = 1000000.0
sonido_fight.MinDistance = 1000000.0
sonido_excelent             = Bladex.CreateSound("../../Sounds/"+language+"/NetPerfect.wav","NetPerfect")
sonido_excelent.MaxDistance = 1000000.0
sonido_excelent.MinDistance = 1000000.0


sonido_cool                 = Bladex.CreateSound("../../Sounds/"+language+"/NetImpressive.wav","NetImpressive")
sonido_cool.MaxDistance = 1000000.0
sonido_cool.MinDistance = 1000000.0
sonido_notcool              = Bladex.CreateSound("../../Sounds/"+language+"/NetThatsHurt.wav","NetThatsHurt")
sonido_notcool.MaxDistance = 1000000.0
sonido_notcool.MinDistance = 1000000.0

sonido_mutilator            = Bladex.CreateSound("../../Sounds/"+language+"/NetMutilator.wav","NetMutilator")
sonido_mutilator.MaxDistance = 1000000.0
sonido_mutilator.MinDistance = 1000000.0
sonido_notmutilator         = Bladex.CreateSound("../../Sounds/"+language+"/NetVeryImpressive.wav","NetVeryImpressive")
sonido_notmutilator.MaxDistance = 1000000.0
sonido_notmutilator.MinDistance = 1000000.0

sonido_win                  = Bladex.CreateSound("../../Sounds/"+language+"/NetWin.wav","NetWin")
sonido_win.MaxDistance = 1000000.0
sonido_win.MinDistance = 1000000.0
sonido_loose                = Bladex.CreateSound("../../Sounds/"+language+"/NetLooser.wav","NetLooser")
sonido_loose.MaxDistance = 1000000.0
sonido_loose.MinDistance = 1000000.0

sonido_care                 = Bladex.CreateSound("../../Sounds/"+language+"/NetBeCarefull.wav","NetBeCarefull")
sonido_care.MaxDistance = 1000000.0
sonido_care.MinDistance = 1000000.0





FRAG_LIMIT = 6 # should be modificable

HIT_COUNTER = {}


def HitCounter(PjName):
	global HIT_COUNTER

	t       = Bladex.GetTime()
	pj      = Bladex.GetEntity(PjName)
	Life    = netgame.GetPlayerData(PjName)[1]
	MaxLife = pj.Data.NetLife

	PreviousLife = Life
	if not HIT_COUNTER.has_key(PjName): # check if exist
		HIT_COUNTER[PjName] = [(t,Life)]
	else:
		if HIT_COUNTER[PjName][0][1] < Life: # check if new round
			HIT_COUNTER[PjName] = []
		else:
			PreviousLife = HIT_COUNTER[PjName][0][1]

		HIT_COUNTER[PjName].insert(0,(t,Life))



	if ((Life<=0) and (PreviousLife>0)):
		if PjName=="Player1":
			print "You are death"
			sonido_loose.PlayStereo()
		else:
			print "You kill him!"
			sonido_win.PlayStereo()
		return

	# be carefull
	LifeLimit = MaxLife*0.35

	if (Life <= LifeLimit) and (PreviousLife > LifeLimit):
		if PjName=="Player1":
			print "You will die!"
			sonido_care.PlayStereo()
		else:
			print "Almost death"
		return

	# Acurancy

	TimeLimit    = t-2.0
	LifeCounter  = 0
	DeathCounter = 0

	for ps in HIT_COUNTER[PjName]:
		if ps[0]<TimeLimit:
			break
		else:
			if ps[1] > 0:
				LifeCounter  = LifeCounter+1
			else:
				DeathCounter = DeathCounter+1

	if (LifeCounter >= 3) and (DeathCounter==0):
		HIT_COUNTER[PjName][0] = (TimeLimit,HIT_COUNTER[PjName][0][1])
		if PjName=="Player1":
			print "Fast Attack!"
			sonido_notcool.PlayStereo()
		else:
			print "too many hits"
			sonido_cool.PlayStereo()

	elif (DeathCounter==3):
		HIT_COUNTER[PjName][0] = (TimeLimit,HIT_COUNTER[PjName][0][1])
		if PjName=="Player1":
			print "3 hits afther deadh!"
			sonido_notmutilator.PlayStereo()
		else:
			print "the serverance hit!"
			sonido_mutilator.PlayStereo()



def DestroyWeaponAndParts(name):
	o = Bladex.GetEntity(name)
	if o:
		o.SubscribeToList("Pin")
	for i in range(50):
		o = Bladex.GetEntity(name+"Pieza"+`i+1`)
		if o:
			o.SubscribeToList("Pin")
		else:
			break

def FreeInventory(EntityName):
	CHAR = Bladex.GetEntity(EntityName)
	INV = CHAR.GetInventory()
	INV.LinkBack("None")
	INV.LinkLeftHand("None")
	INV.LinkRightHand("None")
	INV.CycleShields()
	while INV.GetSelectedShield():
		o = Bladex.GetEntity(INV.GetSelectedShield())
		Actions.RemoveFromInventory(CHAR,o,"")
		DestroyWeaponAndParts(o.Name)
		INV.CycleShields()

	INV.CycleWeapons()
	while INV.GetSelectedWeapon():
		o = Bladex.GetEntity(INV.GetSelectedWeapon())
		Actions.RemoveFromInventory(CHAR,o,"")
		DestroyWeaponAndParts(o.Name)
		INV.CycleWeapons()

	l = []
	for i in range(CHAR.GetNChildren()):
		l.append(CHAR.GetChild(i))

	CHAR.UnlinkChildren()
	for i in l:
		DestroyWeaponAndParts(i)


	try:
		for wn in CHAR.Data.NetWeapons:
			w = Bladex.GetEntity(wn)
			if not w:
				DestroyWeaponAndParts(wn)
			elif not w.Parent:
				DestroyWeaponAndParts(wn)
	except AttributeError:
		print AttributeError

def RunOutCamera():
	Bladex.GetEntity("Camera").SetMaxCamera("movie.cam",0,-1)

def StartWatchMode():
	#Bladex.DeactivateInput() # en modo espera
	i = 0

	NetScorer.wStatusGame.SetText(MenuText.GetMenuText("OBSERVER MODE"))
	SetObserverMessage(0)
	if PJ[0]=="" and PJ[1]=="":
		SetObserverMessage(1)
		RunOutCamera()
	elif netgame.GetNetState() == 1:
		for xx in PJ:
			i=i+1
			if xx!="":
				SetCameraData(i,xx)
				StartCamera()
				return
		print "_-=[StartWatchMode]=-_"
		print "CRITICAL ERROR! SOMEONE MUST BE IN THE ARENA"
	else:
		for xx in PJ:
			i=i+1
			if xx!="":
				if(xx == "Player1"):
					SetCameraData(i,"PlayerX")
					StartCamera()
					return
				elif(xx == netgame.GetClientId()):
					SetCameraData(i,"Player1")
					StartCamera()
					return
				else:
					SetCameraData(i,xx)
					StartCamera()
					return

def EndWatchMode():
	NetScorer.wStatusGame.SetText("")
	#Bladex.ActivateInput()
	if netgame.GetNetState() == 1:
		xx = "Player1"
	else:
		xx = netgame.GetClientId()

	for i in range(len(PJ)):
		if PJ[i] == xx:
			SetCameraData(i+1,"Player1")
			StartCamera()
			return

	print "_-=[EndWatchMode]=-_"
	print "CRITICAL ERROR! SOMEONE MUST BE IN THE ARENA"

def isOnGame(name):
	for i in PJ:
		if i==name:
			return 1
	return 0

def GetPlayerId(Name):
	if netgame.GetNetState() == 1:
		return Name
	else:
		if(Name == "Player1"):
			return "PlayerX"
		elif(Name == netgame.GetClientId()):
			return "Player1"
		else:
			return Name
def StartMatrixFX():
	if PJ[0] != "":
		Name = GetPlayerId(PJ[0])
		cam = Bladex.GetEntity("Camera")
		if netgame.GetPlayerData(Name)[1] >=0:
			netgame.SetPersonView(PJ[0])
			cam.Cut()
			darfuncs.StartMatrixFX(Name)
			print Name
			return

	if PJ[1] != "":
		Name = GetPlayerId(PJ[1])
		if netgame.GetPlayerData(Name)[1] >=0:
			netgame.SetPersonView(PJ[0])
			cam.Cut()
			darfuncs.StartMatrixFX(Name)
			print Name
			return

CameraState = -1
def SwitchCamerasView():
	global CameraState

	# Salir si meto la pata
	if netgame.GetNetState() == 1:
		if isOnGame("Player1"):
			return
	else:
		if isOnGame(netgame.GetClientId()):
			return

	# primero ver si hay alguien jugando
	if PJ[0]=="" or PJ[0]=="":
		return

	# switch entre jugadores
	if CameraState==1:
		CameraState = -1
		RunOutCamera()
		SetObserverMessage(1)
	elif CameraState==-1:
		CameraState = 0
		SetObserverMessage(0)
		pn = GetPlayerId(PJ[0])
		NetScorer.SetNetPlayerScorer(pn)
		netgame.SetPersonView(pn)
		Bladex.GetEntity("Camera").Cut()
	else: # CameraState == 1
		CameraState = 1
		SetObserverMessage(0)
		pn = GetPlayerId(PJ[1])
		NetScorer.SetNetPlayerScorer(pn)
		netgame.SetPersonView(pn)
		Bladex.GetEntity("Camera").Cut()



Bladex.AddBoundFunc("Attack Release",SwitchCamerasView)


if netgame.GetNetState() == 1:
	#--------------------[ \/ Server Kombat module \/ ]--------------------------#
	del Damage.SpecialDamageFuncs['Venom'] # no venom damage here... sorry Enrik

	P_KB = 0 # players in kombat
	Combat = 0
	DarBola = 1
	FRAG_LIMIT = NetMisc.FRAGLIMIT

	def ServerChapuza(EntityName):
		me = Bladex.GetEntity(EntityName)
		if me:
			if me.Data:
				if me.Life <=0:
					me.Data.ReSpawn(EntityName)
					me.SetOnFloor()
					me.Wuea = Reference.WUEA_ENDED
					me.LaunchAnmType("Rlx")
					me.AnmEndedFunc = None
					print me.AnimName


	#----------------------------
	def Calculate_P_KB():
		global P_KB
		P_KB = 0 # players in kombat
		for i in PJ:
			if i!="":
				P_KB = P_KB + 1



	def RestartCarnage():
		NetScorer.ShowFragLimit(1)
		for a in PlayersList:
			a[6] = 0

		for i in range(len(PJ)):
			CheckFreeSlot(PlayersList[0][1])
		FillFrags()

	def ActivateRequest(EntityName):
		for i in range(len(PlayersNotRequestedYet)):
			if PlayersNotRequestedYet[i][1]==EntityName:
				print EntityName+" Ready to fight!"
				PlayersList.insert(len(PlayersList)-1,PlayersNotRequestedYet[i])
				SendGameInformation(PlayersNotRequestedYet[i][0])
				del PlayersNotRequestedYet[i]
				return


	def ReadUserString(id,type,cad):
		if(type==Netval.NET_GAME_CHAT_STRING):
			NetScorer.AddChatString(cad)
			print "chat : "+cad
		elif(type==Netval.NET_GAME_STATUS): # on join!
			ActivateRequest(cad)
			if len(PlayersList)==2:
				Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, RestartCarnage,())
				Bladex.AddScheduledFunc(Bladex.GetTime()+6.0,FillFrags,())
				print "Ready! for join : "+cad
			elif len(PlayersList)>2:
				Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, CheckFreeSlot,(cad,))
				Bladex.AddScheduledFunc(Bladex.GetTime()+6.0,FillFrags,())
				print "Request for join : "+cad
			else:
				print "Not enough for join : "+cad
				netgame.SendUserString(Netval.NET_GAME_STATUS,'O') # Observer Mode
				global Combat
				Combat = 0
		else:
			Actions.ServerCallBack(id,type,cad)
			NetMisc.ReadUserString(id,type,cad)

	PlayersNotRequestedYet = []

	if netgame.IsDedicated():
		PlayersList=[] # Lista de jugadores
		char.Freeze()
		char.RemoveFromWorld()
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, Bladex.SetBloodLevel,(0,))
	else:
		PlayersList=[[-1,char.Name,netdata[0],netdata[1],netdata[2],netdata[3],0]] # Lista de jugadores
	#                    0:netid    1:object   2:Name    3:Race       4:Kind      5:Handicap     6:Frags

	def qSort(l, r):
		i = l
		j = r
		x = PlayersList[(l+r)/2]
		while(i <= j):
			while (PlayersList[i][6]  >  x[6]   ):
				i=i+1
			while (x[6]     >  PlayersList[j][6]):
				j=j-1

			if (i <= j):
				y = PlayersList[i]
				PlayersList[i] = PlayersList[j]
				PlayersList[j] = y
				i = i + 1
				j = i - 1

		if (l < j):
			qSort(l, j)
		if (i < r):
			qSort(i, r)


	def SearchPlayerDescriptor(entity):
		global PlayersList
		for i in range(len(PlayersList)):
			if PlayersList[i][1] == entity:
				return i
		return -1

	def GetPlayerDescriptor(entity):
		global PlayersList
		for i in range(len(PlayersList)):
			if PlayersList[i][1] == entity:
				return PlayersList[i][2]
		return ""

	def SearchPlayerId(id):
		global PlayersList
		for i in range(len(PlayersList)):
			if PlayersList[i][0] == id:
				return i
		return -1


	def ReSpawnPlayer(EntityName):
		ent = Bladex.GetEntity(EntityName)
		ent.Data.ReSpawn(EntityName)
		ent.Level        = 19
		ent.PartialLevel = 0
		ent.UnFreeze()
		ent.Alpha    = 1.0
		ent.SelfIlum = 0.0
		FreeInventory(EntityName)
		INV = ent.GetInventory()
		i = SearchPlayerDescriptor(EntityName)

		handicap = int(PlayersList[i][5])
		if(NetMisc.ARENAHANDICAP < handicap):
			handicap = NetMisc.ARENAHANDICAP
		NetWeapon.AddStandardWeapons2Char(EntityName,PlayersList[i][3],handicap)
		ent.Wuea = Reference.WUEA_ENDED
		ent.AnmEndedFunc = None
		ent.LaunchAnmType("Rlx")
		ent.Energy = NetWeapon.GetEnergy(ent)





	def FillFrags():
		global END_OF_ARENA

		if END_OF_ARENA:
			return
		s=""
		for x in PlayersList:
			s = s+"\n"+x[2]+": "+`x[6]`
		NetScorer.wPlayersFrags.SetText(s)
		NetScorer.wFragList.SetText(s)
		netgame.SendUserString(Netval.NET_GAME_FRAGS,s)
		NetScorer.wFragFrame.RecalcLayout()
		NetScorer.wLeftFrame.RecalcLayout()

	for i in range(len(PJInit)):
		PJ.append("")


	#inicia el combate
	def StartKombat():
		global Combat
		# update the VS label
		s = ""
		for i in PJ:
			idx = SearchPlayerDescriptor(i)
			if(idx != -1):
				s = s +  PlayersList[idx][2] + " VS "
		s = s[0:len(s)-4]
		NetScorer.wPlayersVS.SetText(s)
		netgame.SendUserString(Netval.NET_GAME_IN_COMBAT,s)

		if isOnGame("Player1"):
			EndWatchMode()
		netgame.ClearPools()
		sonido_fight.PlayStereo()
		Combat = 1
		for i in range(len(PJ)):
			if PJ[i]!="":
				pl = Bladex.GetEntity(PJ[i])
				netgame.SendUserString(Netval.NET_GAME_KOMBATERS+i,PJ[i]+"*"+str(int(pl.Data.NetLevel))+"?"+str(int(pl.Data.NetLife)))

		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, netgame.SendUserString,(Netval.NET_GAME_STATUS,'F',))


		for i in range(len(PJ)):
			ent          = Bladex.GetEntity(PJ[i])
			ent.Position = PJInit[i][0], PJInit[i][1], PJInit[i][2]
			ent.Angle    = PJInit[i][3]
			ent.Wuea = Reference.WUEA_ENDED
			ent.LaunchAnmType("Rlx")
			ent.AnmEndedFunc = None
			ent.SetOnFloor()
			ent.UnFreeze()


		Actions.QuickTurnToFaceEntity(PJ[1],PJ[0])
		Bladex.GetEntity(PJ[1]).SetActiveEnemy(Bladex.GetEntity(PJ[0]))
		Actions.QuickTurnToFaceEntity(PJ[0],PJ[1])
		Bladex.GetEntity(PJ[0]).SetActiveEnemy(Bladex.GetEntity(PJ[1]))


		if(OnStartRoundFunc != ""):
			OnStartRoundFunc()
		NetMisc.OnStartRoundFunc()
		Reference.LavaInmune = []
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, StartCamera,())

		p1          = Bladex.GetEntity(PJ[0])
		p2          = Bladex.GetEntity(PJ[1])
		i1          = SearchPlayerDescriptor(PJ[0])
		i2          = SearchPlayerDescriptor(PJ[1])

		if p1.GetInventory().nShields == 0:
			NetWeapon.AddStandardShields2Char(p1.Name,PlayersList[i1][3],p2.Data.NetLevel)

		if p2.GetInventory().nShields == 0:
			NetWeapon.AddStandardShields2Char(p2.Name,PlayersList[i2][3],p1.Data.NetLevel)
		SetObserverMessage(0)

	def SetAtEndOfQueue(EntityName):

		i = SearchPlayerDescriptor(EntityName)
		aux = PlayersList[i]
		PlayersList.remove(PlayersList[i])
		PlayersList.append(aux)


	# se fija si hay algun lugar libre para ponerlo en modo combate
	def CheckFreeSlot(EntityName):
		global P_KB
		global Combat
		global PJ

		print "CheckFreeSlot("+EntityName+")"

		Calculate_P_KB()

		if Combat == 1:
			return

		if isOnGame(EntityName):
			SetAtEndOfQueue(EntityName)
			print "Aperation failed : "+EntityName+" is fighting"
			return

		ent = Bladex.GetEntity(EntityName)

		if ent == None:
			return

		for i in range(len(PJ)):
			if PJ[i] == "": # Slot libre!
				PJ[i] = EntityName
				ReSpawnPlayer(EntityName)
				Bladex.AddScheduledFunc(Bladex.GetTime()+0.25, ServerChapuza,(EntityName,))
				netgame.SetObjectState(EntityName,1)
				ent.Position = PJInit[i][0], PJInit[i][1], PJInit[i][2]
				ent.Angle    = PJInit[i][3]
				ent.Wuea = Reference.WUEA_ENDED
				ent.LaunchAnmType("Rlx")
				ent.AnmEndedFunc = None
				ent.SetOnFloor()
				P_KB = P_KB+1
				SetAtEndOfQueue(EntityName)
				if P_KB == len(PJ): # Start the Kombat?
					StartKombat()
				return

	# just one will survive... Hilander, the inmortal.
	def EndOfKombat():
		global Combat
		global PJ
		global FRAG_LIMIT
		global DarBola
		global P_KB

		print "End Of Kombat"
		NetMisc.OnEndRoundFunc()

		# assign a round to the player x
		Combat = 0
		xPlayer = ""
		frags = 0
		quecagada = 0

		for name in PJ:
			if name!="":
				if(quecagada==0):
					quecagada = 1
					x = SearchPlayerDescriptor(name)
					#if(DarBola == 1):
					#	PlayersList[x][6] = PlayersList[x][6]+1
					frags = PlayersList[x][6]

					DarBola = 0
					FillFrags()
					xPlayer = name
					NetScorer.AddChatString(GetPlayerDescriptor(xPlayer)+" "+MenuText.GetMenuText("wins the battle!"))
					FreePlayerSlot(name,0)
				else:
					name = ""
					print "Something is wrong..."
		P_KB = 0

		CheckFreeSlot(xPlayer)
		if(FRAG_LIMIT<=frags):
			global END_OF_ARENA
			qSort(0,len(PlayersList)-1)
			FillFrags()
			netgame.SendUserString(Netval.NET_GAME_STATUS,'E') # End Of Carnage
			sonido_excelent.PlayStereo()
			SetObserverMessage(1)
			Bladex.AddScheduledFunc(Bladex.GetTime()+7.0, NetMisc.ServerNextLevel,())
			END_OF_ARENA = 1
			for name in PJ:
				if name!="":
					FreePlayerSlot(name,0)
			RunOutCamera()
		else:
			NetScorer.ShowFragLimit(1)
			if(len(PlayersList)<len(PJ)):
				return

			while Combat == 0:
				CheckFreeSlot(PlayersList[0][1])



	def DeactivateIfNotInGame(EntityName):
		global PJ

		if EntityName in PJ:
			netgame.SetObjectState(EntityName,1)
		else:
			netgame.SetObjectState(EntityName,0)

	# Some player dies...
	def FreePlayerSlot(EntityName,nactual=1):
		global P_KB

		Calculate_P_KB()

		print "FreePlayerSlot("+EntityName+", "+`nactual`+")"
		if (EntityName == ""):
			print "Something is wrong"
			return

		for i in range(len(PJ)):
			if(PJ[i] == EntityName):
				ent = Bladex.GetEntity(EntityName)
				ent.Position = netgame.GetNextPosition()
				ent.Freeze()
				ent.RemoveFromWorld()
				PJ[i] = ""

				Bladex.AddScheduledFunc(Bladex.GetTime()+4.0, DeactivateIfNotInGame,(EntityName,))

				# hey! is me!
				if(EntityName == "Player1"):
					StartWatchMode()

				P_KB = P_KB - 1
				FreeInventory(EntityName)
				if nactual:
					if len(PlayersList) < 2:
						print "Not enough players to start"
						if P_KB == 1:
							for i in PJ:
								if i != "":
									FreePlayerSlot(i)
						else:
							global Combat
							StartWatchMode()
							netgame.SendUserString(Netval.NET_GAME_STATUS,'O') # Observer Mode
							Combat = 0
					elif P_KB == 1:
						EndOfKombat()
					elif P_KB == 0:
						CheckFreeSlot(EntityName)







	if not netgame.IsDedicated():
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, CheckFreeSlot,("Player1",))  # siempre al inicio el servidor...
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, FreePlayerSlot,("Player1",))  # siempre saco del inicio el servidor...
	NetScorer.wStatusGame.SetText(MenuText.GetMenuText("OBSERVER MODE"))


	def SendGameInformation(id):
		if (PJ[0]!="") and (PJ[1]!=""):

			idxpl = 0
			npl = Bladex.GetEntity(PJ[idxpl])
			netgame.SendUserString(Netval.NET_GAME_KOMBATERS+idxpl,PJ[idxpl]+"*"+str(int(npl.Data.NetLevel))+"?"+str(int(npl.Data.NetLife)),`id`)

			idxpl = 1
			npl = Bladex.GetEntity(PJ[idxpl])
			netgame.SendUserString(Netval.NET_GAME_KOMBATERS+idxpl,PJ[idxpl]+"*"+str(int(npl.Data.NetLevel))+"?"+str(int(npl.Data.NetLife)),`id`)

	def JoinFunc(id,objname,name,race,weapon,shield):
		import Basic_Funcs

		PlayersNotRequestedYet.insert(0,[ id, objname, name, race, weapon, shield, 0])     # Lo agrega a la lista de jugadores con frags = 0
		NetScorer.AddChatString(name+" "+MenuText.GetMenuText("gets into the slaughter"))

		CHAR = Bladex.GetEntity(objname)
		CHAR.Position = netgame.GetNextPosition()
		CHAR.Wuea = Reference.WUEA_ENDED
		CHAR.LaunchAnmType("Rlx")
		CHAR.AnmEndedFunc = None
		CHAR.SetOnFloor()
		CHAR.Level=19
		CHAR.PartialLevel=0
		CHAR.SendTriggerSectorMsgs=1
		CHAR.Data=Basic_Funcs.PlayerPerson(CHAR)
		CHAR.Life = 1000

		CHAR.OnStepFunc = SendStepData

		netgame.SetObjectState(objname,0)

		if(OnJoinFunc != ""):
			OnJoinFunc(id,objname,name,race,weapon,shield)

		#Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, CheckFreeSlot,(objname,))
		#Bladex.AddScheduledFunc(Bladex.GetTime()+6.0,FillFrags,())





	def ByeFunc(i,s):
		global PlayersList
		global DarBola

		id = SearchPlayerId(i)
		if id != -1:
			NetScorer.AddChatString(GetPlayerDescriptor(s)+" "+MenuText.GetMenuText("flees like a chicken!"))
			PlayersList.remove(PlayersList[id])
			DarBola = 1
			FreePlayerSlot(s)
			pj = Bladex.GetEntity(s)
			pj.Life = -1
			Bladex.AddScheduledFunc(Bladex.GetTime()+10.0, pj.SubscribeToList,("Pin",))
			Bladex.AddScheduledFunc(Bladex.GetTime()+11.0, FillFrags,         ())
			print "Bye Bye "+s
			if PJ[0]!="" or PJ[1]!="":
				darfuncs.StopMatrixFX()
			else:
				Bladex.SetTimeSpeed(1)
			netgame.SendUserString(Netval.NET_GAME_STATUS,'m') # Observer Mode

	netgame.SetJoinPlayerFunc(JoinFunc)
	netgame.SetByePlayerFunc(ByeFunc)
	netgame.SetStringUserFunc(ReadUserString)



	def FreezeTheHit(AttackerName):
		an = Bladex.GetEntity(AttackerName)
		an.Freeze()
		an.AnmEndedFunc = None
		darfuncs.StopMatrixFX()
		netgame.SendUserString(Netval.NET_GAME_STATUS,'m') # Observer Mode


	def PlayerHurt( VictimName, AttackerName, Life, prevLife):
		global PlayersList
		global DarBola

		print VictimName+" <- "+AttackerName+" Life:"+`Life`+" Previous life:"+`prevLife`
		HitCounter(VictimName)
		if Life <= 0:
			if prevLife > 0:
				x = SearchPlayerDescriptor(AttackerName)
				if x != -1:
					if VictimName==AttackerName:
						PlayersList[x][6]=PlayersList[x][6]-1
					else:
						PlayersList[x][6]=PlayersList[x][6]+1
					NetScorer.AddChatString(GetPlayerDescriptor(VictimName)+" "+MenuText.GetMenuText("was massacred by")+" "+GetPlayerDescriptor(AttackerName))
					DarBola = 1
					Bladex.RemoveScheduledFunc("FreePlayerSlot")
					Bladex.AddScheduledFunc(Bladex.GetTime()+5.0,FreePlayerSlot,(VictimName,),"FreePlayerSlot")
					Bladex.GetEntity(VictimName).ImDeadFunc(VictimName)
					Bladex.GetEntity(AttackerName).AnmEndedFunc = FreezeTheHit
					StartMatrixFX()
					netgame.SendUserString(Netval.NET_GAME_STATUS,'M') # Observer Mode
				else:
					vi = SearchPlayerDescriptor(VictimName)
					PlayersList[vi][6]=PlayersList[vi][6]-1
					if AttackerName == "BigFall":
						NetScorer.AddChatString(GetPlayerDescriptor(VictimName)+" "+MenuText.GetMenuText("falls into limbo"))
						DarBola = 1
						Bladex.RemoveScheduledFunc("FreePlayerSlot")
						Bladex.AddScheduledFunc(Bladex.GetTime()+5.0,FreePlayerSlot,(VictimName,),"FreePlayerSlot")
					elif AttackerName == "Fall":
						NetScorer.AddChatString(GetPlayerDescriptor(VictimName)+" "+MenuText.GetMenuText("flies too high"))
						Bladex.RemoveScheduledFunc("FreePlayerSlot")
						Bladex.AddScheduledFunc(Bladex.GetTime()+5.0,FreePlayerSlot,(VictimName,),"FreePlayerSlot")
						Bladex.GetEntity(VictimName).ImDeadFunc(VictimName)
					elif AttackerName == "Lava":
						NetScorer.AddChatString(GetPlayerDescriptor(VictimName)+" "+MenuText.GetMenuText("dives into the lava"))
						Bladex.RemoveScheduledFunc("FreePlayerSlot")
						Bladex.AddScheduledFunc(Bladex.GetTime()+5.0,FreePlayerSlot,(VictimName,),"FreePlayerSlot")
						Bladex.GetEntity(VictimName).ImDeadFunc(VictimName)
				Reference.LavaInmune = ["Knight_N","Barbarian_N","Amazon_N","Dwarf_N"]

	Damage.PlayerHitFunc = PlayerHurt

	FillFrags()
	char.SendTriggerSectorMsgs=1

	def SendStepData(personaje):
		netgame.CallEventSound(personaje,4)

	char.OnStepFunc = SendStepData


	print "Server:Kombat Mode"
	#--------------------[ /\ Server Kombat module /\ ]--------------------------#
else:
	#--------------------[ \/ Client Kombat module \/ ]--------------------------#

	################################### Pa' todos lo cliente ###################################
	TajoMutilacion=Bladex.CreateSound('../../Sounds/golpe-arma-escudo.wav', 'TajoMutilacion_Red')
	TajoCortante=Bladex.CreateSound('../../Sounds/corte-carne-2.wav', 'TajoCortante')

	import Blood
	def ClientDamage(EntityName):

		en = Bladex.GetEntity(EntityName)
		if NetMisc.OnDamageFunc(en):
			return

		Blood.BleedingImpact(en, en.Position[0], en.Position[1], en.Position[2], 0,10000,0,  0,   0,0,0,   0,0,0  )
		TajoCortante.Play(       en.Position[0], en.Position[1], en.Position[2], 0)

		HitCounter(EntityName)


	netgame.SetClientDamageFunc(ClientDamage)

	def Mutilate(pj_name,obj_name,x,y,z,nx,ny,nz,node):

		en = Bladex.GetEntity(pj_name)
		TajoMutilacion.Play(en.Position[0], en.Position[1], en.Position[2], 0)
		Blood.Mutilate(pj_name,obj_name,x,y,z,nx,ny,nz,node)


	netgame.SetMutilaFunc(Mutilate)

	def ClientSoundEvent(s,i):
		if i == 4:
			hit_ent = Bladex.GetEntity(s)
			if hit_ent.Name[0:6]=="Player":
				PlayNetStepSound(hit_ent)
			else:
				Reference.DefaultObjectData[hit_ent.Kind][3].Play(hit_ent.Position[0], hit_ent.Position[1], hit_ent.Position[2], 0)
		elif i == 5:
			Breakings.PlayBreakSound(s)
		else:
			print "Error Sound event ",s,i


	netgame.SetSoundFunc(ClientSoundEvent)

	def ByeFunc(i,s):
		NetMisc.Disconnect()

	netgame.SetByePlayerFunc(ByeFunc)

	################################### Pa' todos lo cliente ###################################


	PJ=["","","","","","","","","",""]

	class ClientData:
		pass
	def ReadUserString(id,type,cad):
		print `type`+" : "+cad
		if  (type==Netval.NET_GAME_FRAGS):
			NetScorer.wPlayersFrags.SetText(cad)
			NetScorer.wFragList.SetText(cad)
			NetScorer.wFragFrame.RecalcLayout()
		elif(type==Netval.NET_GAME_STATUS):
			if   cad[0] == "E":  # End of game.
				global END_OF_ARENA
				END_OF_ARENA = 1
				SetObserverMessage(1)
				sonido_excelent.PlayStereo()
				RunOutCamera()
			elif cad[0] == "F":  # Start round
				SetObserverMessage(0)
				netgame.ClearPools()
				sonido_fight.PlayStereo()
				if isOnGame(netgame.GetClientId()):
					EndWatchMode()
				else:
					StartWatchMode()
				StartCamera()
			elif cad[0] == "O":  # Not enough players
				global PJ
				PJ=["","","","","","","","","",""]
				StartWatchMode()
			elif cad[0] == "M":  # Matrix FX start
				StartMatrixFX()
			elif cad[0] == "m":  # Matrix FX stop
				if PJ[0]!="" or PJ[1]!="":
					darfuncs.StopMatrixFX()
				else:
					Bladex.SetTimeSpeed(1)

		elif(type<=10):
			PJ[type-Netval.NET_GAME_KOMBATERS] = 	cad[0:string.find(cad,"*")]
			pl = Bladex.GetEntity(NetMisc.GetClientPlayerId(cad[0:string.find(cad,"*")]))
			pl.Data = ClientData()
			pl.Data.last_frwdup = 0
			pl.Data.last_brwdup = 0
			pl.Data.NetLevel = string.atoi(cad[string.find(cad,"*")+1:string.find(cad,"?")])
			pl.Data.NetLife  = string.atoi(cad[string.find(cad,"?")+1:])


			if isOnGame(netgame.GetClientId()):
				EndWatchMode()
			else:
				StartWatchMode()
		elif(type==Netval.NET_GAME_IN_COMBAT):
			NetScorer.wPlayersVS.SetText(cad)
		elif(type==Netval.NET_GAME_CHAT_STRING):
			NetScorer.ChatClientString(cad)
		else:
			Actions.ClientCallBack(id,type,cad)
			NetMisc.ReadUserString(id,type,cad)



	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0,netgame.SendUserString,(Netval.NET_GAME_STATUS,netgame.GetClientId()),"SendUserString")

	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0,StartWatchMode,(),"StartWatchMode")

	netgame.SetStringUserFunc(ReadUserString)
	cam = Bladex.GetEntity("Camera")
	cam.PViewType = 1
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, RunOutCamera,())
	print "Client:Kombat Mode"
	#--------------------[ /\ Client Kombat module /\ ]--------------------------#


# solo para dos jugadores modo Kombat
def AhoraSiEncarate(EntityName):
	CHAR = Bladex.GetEntity(EntityName)
	if PJ[0] != EntityName :
		CHAR.SetActiveEnemy(Bladex.GetEntity(PJ[0]))
	else:
		CHAR.SetActiveEnemy(Bladex.GetEntity(PJ[1]))

def Encarate(EntityName="Player1"):
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.125, AhoraSiEncarate,(EntityName,))

def xxxSwitchFragViewer(xx=0,xxx=0,xxxxx=0):
	NetScorer.SwitchFragViewer()

def xxxStartChatString(xx=0,xxx=0,xxxxx=0):
	NetScorer.StartInput()

def NetBinds(PlayerName):
	Bladex.AddBoundFunc("Select Enemy",acts.DefArgWrapper (PlayerName, Encarate))
	Bladex.AddBoundFunc("Show Scorer", acts.DefArgWrapper (PlayerName, xxxSwitchFragViewer))
	Bladex.AddBoundFunc("Send Message", acts.DefArgWrapper (PlayerName, xxxStartChatString))

acts.NetBinds = NetBinds

netgame.Bind("Select Enemy",   Encarate,0)