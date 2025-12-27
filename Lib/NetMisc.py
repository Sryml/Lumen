######################### Configuracion de red ##############################
try:
	execfile('../../Config/NetCfg.py')
except:
	TCP           = 1
	CHARTYPE      = "Knight"
	MODEL         = 0
	HANDICAP      = 4
	PLAYERNAME    = "BLADE"
	ARENANAME     = "ARENA"
	ARENAHANDICAP = 4
	POWERUPS      = 1
	MAXPLAYERS    = 5
	SELMAPS       = []
	ACTUALMAP     = 0
	IP            = ""
	FRAGLIMIT     = 6
	NETPPS        = 0
######################### Configuracion de red ##############################

import netwidgets
import MenuText
import MenuWidget
import netgame
import Bladex
import string
import os
import cheats
import BInput

Caracteres = {	 "Knight"     :[0,"Knight_N"
					,"Knight_N"
					,"KgtSkin1"
					,"KgtSkin2"
				
		],"Barbarian" :[1,"Barbarian_N"
					,"Barbarian_N"
					,"BarSkin1"
					,"BarSkin2"
				
		],"Dwarf"     :[2,"Dwarf_N"
					,"Dwarf_N"
					,"DwfSkin1"
					,"DwfSkin2"
		],"Amazon"    :[3,"Amazon_N"
			    		,"Amazon_N"
			    		,"AmzSkin1"
			    		,"AmzSkin2"
		]}

CharBitmaps = 	(
			("Knight_N"    , "../../Data/net/Knight_N.BMP"   ),
			("KgtSkin1"    , "../../Data/net/KgtSkin1.BMP"   ),
			("KgtSkin2"    , "../../Data/net/KgtSkin2.BMP"   ),
			("Barbarian_N" , "../../Data/net/Barbarian.BMP"  ),
			("BarSkin1"    , "../../Data/net/BarSkin1.BMP"   ),
			("BarSkin2"    , "../../Data/net/BarSkin2.BMP"   ),
			("Dwarf_N"     , "../../Data/net/Dwarf_N.BMP"    ),
			("DwfSkin1"    , "../../Data/net/DwfSkin1.BMP"   ),
			("DwfSkin2"    , "../../Data/net/DwfSkin2.BMP"   ),
			("Amazon_N"    , "../../Data/net/Amazon_L.BMP"   ),
			("AmzSkin1"    , "../../Data/net/AmzSkin1.BMP"   ),
			("AmzSkin2"    , "../../Data/net/AmzSkin2.BMP"   ),
		)

MapsBitmaps =   []

def ActualizeMapsBitmaps():
	global MapsBitmaps
	
	while len(MapsBitmaps)!=0:
		MapsBitmaps.remove(MapsBitmaps[0])
	
	dirlist = os.listdir("..")
	for dirname in dirlist:
		try:
			f = open("../"+dirname+"/Server.py")
		except:
			continue		
		print dirname
		cadena = f.readline()
		f.close()
		
		if cadena[0] == "#":
			cadena = string.strip(cadena[1:len(cadena)-1])
		else:
			cadena = dirname
		try:
			escrinchot = "../"+dirname+"/shoot.bmp"
			f = open(escrinchot)
			f.close()
			
		except:
			escrinchot = "../../Data/net/Logo.BMP"

		MapsBitmaps.append(escrinchot,cadena,dirname)
	return MapsBitmaps
		
		
			

def SetPPS(option):
	global NETPPS
	
	if option == "Variable":
		NETPPS = 0
	else:
		NETPPS = string.atoi(option)


def GetPPS():
	global NETPPS
	
	return int(NETPPS/10)
	

def SetProtocol(option):
	global TCP
	if option=="TCP/IP":
		TCP = 1
	else:
		TCP = 0

    
def GetProtocol():
	global TCP
	if TCP:
		return  1
	else:
		return  0

def SetCharType(option):
	global CHARTYPE
	global MODEL
	
	CHARTYPE = option
	MODEL    = 0
	netwidgets.ChangePlayer(Caracteres[CHARTYPE][MODEL+2])
	

def GetCharType():
	global CHARTYPE
	
	return Caracteres[CHARTYPE][0]

def SetHandicap(option):
	global HANDICAP
	
	HANDICAP = option
	
def GetHandicap():
	global HANDICAP
	
	return HANDICAP
	
def NextSkin(menu_class):
	global MODEL
	global CHARTYPE
	
	size = len(Caracteres[CHARTYPE])-2
	MODEL = MODEL + 1
	if MODEL>=size:
		MODEL = 0
	netwidgets.ChangePlayer(Caracteres[CHARTYPE][MODEL+2])

def PreviousSkin(menu_class):
	global MODEL
	global CHARTYPE
	
	size = len(Caracteres[CHARTYPE])-2
	MODEL = MODEL - 1
	if MODEL < 0:
		MODEL = size-1
	netwidgets.ChangePlayer(Caracteres[CHARTYPE][MODEL+2])


def SetPowerUp(option):
	global POWERUPS
	if option=="Yes":
		POWERUPS = 0
	else:
		POWERUPS = 1
		
def GetPowerUp():
	global POWERUPS
	return POWERUPS

def SetMaxPlayers(option):
	global MAXPLAYERS
	
	MAXPLAYERS = option
	
def GetMaxPlayers():
	global MAXPLAYERS
	
	return MAXPLAYERS

def SetArenaHandicap(option):
	global ARENAHANDICAP
	
	ARENAHANDICAP = option
	
def GetArenaHandicap():
	global ARENAHANDICAP
	
	return ARENAHANDICAP

def SetArenaMaps(option):	
	global SELMAPS
	SELMAPS = option
	
def GetArenaMaps():
	global SELMAPS
	return  SELMAPS

def GetCharStatus():
	global CHARTYPE
	global MODEL
	return Caracteres[CHARTYPE][MODEL+2]

def GetArenaName():
	global ARENANAME
	return  ARENANAME

def GetPlayerName():
	global PLAYERNAME
	return  PLAYERNAME

def GetIp():
	global IP
	global TCP
	
	if TCP:
		return IP
	else:
		return "LOCAL"
	

def SetArenaName(n):
	global ARENANAME
	ARENANAME = n

def SetPlayerName(n):
	global PLAYERNAME
	PLAYERNAME = n

def SetIp(n):
	global IP
	global TCP
	
	if TCP :
		IP = n

def IpLooked():
	global TCP
	return not TCP

def SetFragLimit(option):
	global FRAGLIMIT
	
	FRAGLIMIT = option
	
def GetFragLimit():
	global FRAGLIMIT
	
	return FRAGLIMIT


def JoinFunc(Name,NumPlayers,MaxPlayers,Idx):
	global PLAYERNAME

	netgame.SetPPS(0)
	print Name,NumPlayers,MaxPlayers,Idx,"Loading..."
	SaveConfiguration()
	if netgame.JoinSession(Idx,PLAYERNAME):
		Bladex.LoadLevel("Arena1")
	else:
		BrowseServers(0)

def RefreshFunc(Name,NumPlayers,MaxPlayers,Idx):
	BrowseServers(0)

def NullFunc(Name,NumPlayers,MaxPlayers,Idx):
	pass
	
def BrowseServers(menu_class):
	print "searching..."
	global TCP
	global IP
	
	lista = []
	netgame.RestartNet()
	if TCP:
		netgame.BrowseSessions(IP)
	else:
		netgame.BrowseSessions("[ipx]")
	i = 0
	Srv = netgame.GetBrowseResult(i)
	
	while Srv != None:
		if Srv[0][0:3]=="BS\n": # Standard Server
			lista.append({	"Name"		: Srv[0][3:],
					"NumPlayers"	: Srv[1],
					"MaxPlayers"	: Srv[2],
					"Idx"		: i,
					"Join"		: JoinFunc,
					"Kind"		: netwidgets.B_ServerLabel#MenuWidget.B_MenuItemTextNoFX#
					})
		if Srv[0][0:3]=="BD\n": # dedicated server
			lista.append({	"Name"		: Srv[0][3:],
					"NumPlayers"	: Srv[1]-1,
					"MaxPlayers"	: Srv[2]-1,
					"Idx"		: i,
					"Join"		: JoinFunc,
					"Kind"		: netwidgets.B_ServerLabel#MenuWidget.B_MenuItemTextNoFX#
					})
		i=i+1
		Srv = netgame.GetBrowseResult(i)

	if len(lista)>=1:
		lista.append({	"Name"		: MenuText.GetMenuText("< REFRESH >"),
				"NumPlayers"	: 0,
				"MaxPlayers"	: 0,
				"Idx"		: 0,
				"Join"		: RefreshFunc,
				"Kind"		: netwidgets.B_ServerLabel#MenuWidget.B_MenuItemTextNoFX#
				})
	else:
		lista.append({	"Name"		: MenuText.GetMenuText("< No server found >"),
				"NumPlayers"	: 0,
				"MaxPlayers"	: 0,
				"Idx"		: 0,
				"Join"		: NullFunc,
				"Kind"		: netwidgets.B_ServerLabel#MenuWidget.B_MenuItemTextNoFX#
				})
	
	
	netwidgets.LaListaDeServidores.SetList(lista)
	if len(lista)>=1:
		import Menu
		Menu._MainMenu.MenuNextItem()
	print "Ready!"

MainMenu = 0

def StartServer(menu_class):
	global ARENANAME
	global PLAYERNAME
	global MAXPLAYERS
	global TCP
	global SELMAPS
	global ACTUALMAP
	global MainMenu
	global NETPPS
	
	if len(SELMAPS)==0:
		return
		
	MainMenu.DeActivateMenuItem()
	netgame.RestartNet()
	print "start server : ", netgame.StartServer("BS\n"+ARENANAME,PLAYERNAME,MAXPLAYERS,TCP)
	ACTUALMAP = 0
	SaveConfiguration()
	print "Loading ",SELMAPS[ACTUALMAP]
	Bladex.LoadLevel(SELMAPS[ACTUALMAP])
	netgame.SetPPS(NETPPS)
	
	return

def ServerNextLevel():
	global ACTUALMAP
	global SELMAPS
	ACTUALMAP = (ACTUALMAP+1)%len(SELMAPS)
	SaveConfiguration()
	netgame.ServerChangeLevel(SELMAPS[ACTUALMAP])
	
	
def SavePlayerConfiguration(xx=0):
	MainMenu.DeActivateMenuItem()
	SaveConfiguration()
	
	if netgame.GetNetState() == 0:
		import GameText
		if GameText.MapList.has_key(string.upper(Bladex.GetCurrentMap())):
			InputManager=BInput.GetInputManager()
			oldIAS = InputManager.GetInputActionsSet()
			
			InputManager.SetInputActionsSet("Default")
			if   (CHARTYPE == "Knight")    and (PLAYERNAME=="SCAIGUOKER"):
				cheats.ActivateLaserEyes()
			elif (CHARTYPE == "Amazon")    and (PLAYERNAME=="PAMELA CHU"):
				cheats.ActivateMiscCheats()
			elif (CHARTYPE == "Barbarian") and (PLAYERNAME=="GUYAGAO"):
				cheats.ActivateWeaponGrow()
			elif (CHARTYPE == "Dwarf") and     (PLAYERNAME=="NO LEM KGB"):
				cheats.ActivateGoreCheatsCheats()
			elif (CHARTYPE == "Barbarian") and (PLAYERNAME=="IVALAOSTIA"):
				cheats.ActivateLevelCheats()
			
			InputManager.SetInputActionsSet(oldIAS)
			

def SaveConfiguration(xx=0):
	global TCP           
	global CHARTYPE      
	global MODEL         
	global HANDICAP      
	global PLAYERNAME    
	global ARENANAME     
	global ARENAHANDICAP 
	global POWERUPS      
	global MAXPLAYERS    
	global SELMAPS       
	global ACTUALMAP     
	global IP            
	global FRAGLIMIT     
	global NETPPS        
	
	cfgfile=open('../../Config/NetCfg.py','w')
	cfgfile.write('\n# The sacred file of blade is here!\n\n\n')
	cfgfile.write("TCP           = "+`TCP`+'\n')
	cfgfile.write("CHARTYPE      = "+'"'+CHARTYPE+'"'+'\n')
	cfgfile.write("MODEL         = "+`MODEL`+'\n')
	cfgfile.write("HANDICAP      = "+`HANDICAP`+'\n')
	cfgfile.write("PLAYERNAME    = "+'"'+PLAYERNAME+'"'+'\n')
	cfgfile.write("ARENANAME     = "+'"'+ARENANAME+'"'+'\n')
	cfgfile.write("ARENAHANDICAP = "+`ARENAHANDICAP`+'\n')
	cfgfile.write("POWERUPS      = "+`POWERUPS`+'\n')
	cfgfile.write("MAXPLAYERS    = "+`MAXPLAYERS`+'\n')
	cfgfile.write("SELMAPS       = "+`SELMAPS`+'\n')
	cfgfile.write("ACTUALMAP     = "+`ACTUALMAP`+'\n')
	cfgfile.write("IP            = "+'"'+IP+'"'+'\n')
	cfgfile.write("FRAGLIMIT     = "+`FRAGLIMIT`+'\n')
	cfgfile.write("NETPPS        = "+`NETPPS`+'\n')
	
	
	if len(SELMAPS)==0:
		SELMAPS = ["Arena1"]
		
	netgame.SetLocalOptions(PLAYERNAME,Caracteres[CHARTYPE][1],Caracteres[CHARTYPE][MODEL+2],`HANDICAP`,SELMAPS[ACTUALMAP])
	
	cfgfile.write('\n# God bless your way, little warrior.\n\n\n')
	cfgfile.close()
	
def Disconnect(xx=0):
	netgame.RestartNet()
	Bladex.LoadLevel("Casa")
	
	
LReadUserString = []

def ReadUserString(id,type,cad):
	
	print "Lee Cadena"
	
	global LReadUserString
	for f in LReadUserString:
		f(id,type,cad)


LOnStartRoundFunc = []

def OnStartRoundFunc():
	
	print "Inicia Round"
	
	global LOnStartRoundFunc
	for f in LOnStartRoundFunc:
		f()



LOnEndRoundFunc = []

def OnEndRoundFunc():
	print "Finaliza Round"
	
	global LOnEndRoundFunc
	for f in LOnEndRoundFunc:
		f()

LOnDamageFunc = []

def OnDamageFunc(entity):
	global LOnDamageFunc
	for f in LOnDamageFunc:
		if f(entity):
			return 1
	return 0
	

def SetMainMenu(_MainMenu_):
	global MainMenu
	
	MainMenu = _MainMenu_
	
	
	
def GetClientPlayerId(xx):
	if netgame.GetNetState() == 2:
		if(xx == "Player1"):
			return "PlayerX"
		elif(xx == netgame.GetClientId()):
			return "Player1"
		else:
			return xx
	else:
		return xx