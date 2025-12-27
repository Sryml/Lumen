import MemPersistence
ContinueLoad = 1

if not MemPersistence.Get("NetStuffChecked"):
	MemPersistence.Store("NetStuffChecked","peroporsupuestoqueclaroquesi")	
	import netgame
	
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
			
	#
	# usefull functions
	#
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
			SELMAPS = ["Arena1","Arena3","Arena4","Arena5","Arena7"]
	
		netgame.SetLocalOptions(PLAYERNAME,Caracteres[CHARTYPE][1],Caracteres[CHARTYPE][MODEL+2],`HANDICAP`,SELMAPS[ACTUALMAP])
	
		cfgfile.write('\n# God bless your way, little warrior.\n\n\n')
		cfgfile.close()
	
	
	
	
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
		
	
	############################
	# Dedicated server runtime.
	############################
	if netgame.IsDedicated():
		import Bladex
		import os
		
			
		ACTUALMAP = 0
		SaveConfiguration()
		
		
		# Reset the starting values
		
		# Start the networking stuff
		netgame.RestartNet()
		print "start server : ", netgame.StartServer("BD\n"+ARENANAME,PLAYERNAME,MAXPLAYERS+1,TCP)
		print "Loading ",SELMAPS[ACTUALMAP]
		netgame.SetPPS(NETPPS)
		
		# change to the server directory
		os.chdir("../"+SELMAPS[ACTUALMAP])
		
		# execute the server startup
		netgame.SetLocalOptions(PLAYERNAME,"Knight_N","Knight_N",`HANDICAP`,SELMAPS[ACTUALMAP])
		execfile("server.py")
		
		print " BLADE ARENA --- DEDICATED SERVER"
		
		ContinueLoad = 0
	else:
		import string
		import Bladex
		import os
			
		DoNet = "single"
		
		for params in string.splitfields(Bladex.GetCommandLine()):
			p = string.splitfields(string.lower(params),':')
			
			
			if p[0] == "-host":
				DoNet = "host"
				TCP   = 1
				
			elif p[0] == "-connect":
				DoNet = "client"
				IP    = p[1]
				TCP   = 1
			
			elif p[0] == "-player":
				PLAYERNAME = p[1]
				
			elif p[0] == "-arena":
				ARENANAME  = p[1]
		
			elif p[0] == "-knight":
				CHARTYPE  = "Knight"
		
			elif p[0] == "-amazon":
				CHARTYPE  = "Amazon"
		
			elif p[0] == "-barbarian":
				CHARTYPE  = "Barbarian"
		
			elif p[0] == "-dwarf":
				CHARTYPE  = "Dwarf"
				
			
			
		if DoNet == "host":
			ACTUALMAP = 0
			if len(SELMAPS)==0:
				SELMAPS = ["Arena1","Arena3","Arena4","Arena5","Arena7"]
			
			netgame.RestartNet()		
			print "start server : ", netgame.StartServer("BD\n"+ARENANAME,PLAYERNAME,MAXPLAYERS+1,TCP)
			SaveConfiguration()
			os.chdir("../"+SELMAPS[ACTUALMAP])
			print SELMAPS[ACTUALMAP]
			execfile("server.py")
			ContinueLoad = 0
	
		if DoNet == "client":
			netgame.BrowseSessions(IP)
			Srv = netgame.GetBrowseResult(0)
			if Srv != None:
				print "SERVIDOR : ",Srv
				netgame.SetPPS(0)
				SaveConfiguration()
				if netgame.JoinSession(0,PLAYERNAME):
					Bladex.LoadLevel("Arena1")
					ContinueLoad = 0
					print "UNIENDO"

	
