import Bladex
import Breakings
import Sparks
import Reference
import CharStats

PJ_DEF = [  2,  9,  14,  19 ]
PJ_ATT = [  2,  9,  14,  19 ]

PJ_CFG ={
	  "Knight_N":	[ ### C A B A L L E R O ###
	  			( ################## 1 ##################
	  				(### ESCUDOS ###
	  					"Escudo1",
	  					"Escudo2",
	  				),
	  				(### ESPADAS ###
	  					"Gladius",
	  					"Maza",
	  					"Espadaromana",
	  				),### Life ###
	  				300,
	  				# Energy
	  				540, 
	  			),
	  			( ################## 2 ##################
	  				(### ESCUDOS ###
	  					"Escudo1",
	  					"Escudo9",
	  				),
	  				(### ESPADAS ###
	  					"Espadaelfica",
	  					"Maza2",
	  					"HookSword",
	  				),### Life ###
	  				2200,
	  				# Energy
	  				1210, 
	  			),
	  			( ################## 3 ##################
	  				(### ESCUDOS ###
	  					"KingShield",
	  					"Escudo3",
	  				),
	  				(### ESPADAS ###
	  					"Espadacurva",
	  					"Dagesse",
	  					"Cimitarra",
	  				),### Life ###
	  				4200,
	  				# Energy
	  				3000, 
	  			),
	  			( ################## 4 ##################
	  				(### ESCUDOS ###
	  					"Escudo6",
	  				),
	  				(### ESPADAS ###
	  					"DoubleSword",
	  					"Espadafilo",
	  					"Espada",
	  				),### Life ###
	  				6200,
	  				# Energy
	  				8600, 
	  			),
	  		],
	  "Barbarian_N":	[ ### B A R B A R O ###
	  			( ################## 1 ##################
	  				(### ESCUDOS ###
	  					"Escudo1",
	  					"Escudo2",
	  				),
	  				(### ESPADAS ###
	  					"Chaosword",
	  					"Eclipse",
	  					"DeathSword",
	  					"Gladius",
	  				),### Life ###
	  				300,
	  				# Energy
	  				540, 
	  			),
	  			( ################## 2 ##################
	  				(### ESCUDOS ###
	  					"Escudo1",
	  					"Escudo9",
	  				),
	  				(### ESPADAS ###
	  					"Guadanya",
	  					"LongSword",
	  					"Alfanje",
	  					"Maza2",
	  				),### Life ###
	  				2200,
	  				# Energy
	  				1210, 
	  			),
	  			( ################## 3 ##################
	  				(### ESCUDOS ###
	  					"KingShield",
	  					"Escudo3",
	  				),
	  				(### ESPADAS ###
	  					"Hacha2hojas",
	  					"FlatSword",
	  					"BigSword",
	  					"Dagesse",
	  				),### Life ###
	  				4200,
	  				# Energy
	  				3000, 
	  			),
	  			( ################## 4 ##################
	  				(### ESCUDOS ###
	  					"Escudo6",
	  				),
	  				(### ESPADAS ###
	  					"RhinoClub",
	  					"Hacharrajada",
	  					"SawSword",
	  					"Espadafilo",
	  				),### Life ###
	  				6200,
	  				# Energy
	  				8600, 
	  			),
	  		],
	  "Dwarf_N":	[ ### E N A N O ###	  
	  			( ################## 1 ##################
	  				(### ESCUDOS ###
	  					"Escudo1",
	  					"Escudo2",
	  				),
	  				(### ESPADAS ###
	  					"Hacha",
	  					"Hacha5",
	  					"Garropin",
	  				),### Life ###
	  				300,
	  				# Energy
	  				540, 
	  			),
	  			( ################## 2 ##################
	  				(### ESCUDOS ###
	  					"Escudo1",
	  					"Escudo9",
	  				),
	  				(### ESPADAS ###
	  					"Hacha4",
	  					"Hacha3",
	  					"Martillo",
	  				),### Life ###
	  				2200,
	  				# Energy
	  				1210, 
	  			),
	  			( ################## 3 ##################
	  				(### ESCUDOS ###
	  					"KingShield",
	  					"Escudo3",
	  				),
	  				(### ESPADAS ###
	  					"Martillo2",
	  					"Garrote2",
	  					"MazaDoble",
	  				),### Life ###
	  				4200,
	  				# Energy
	  				3000, 
	  			),
	  			( ################## 4 ##################
	  				(### ESCUDOS ###
						"Escudo6",
	  				),
	  				(### ESPADAS ###
	  					"Hacha6",
	  					"Hacha2",
	  					"Martillo3",
	  				),### Life ###
	  				6200,
	  				# Energy
	  				8600, 
	  			),
	  		],
	  "Amazon_N":	[ ### A M A Z O N A ### 
	  			( ################## 1 ##################
	  				(### ESCUDOS ###
	  					"Escudo1",
	  					"Escudo2",
	  				),
	  				(### ESPADAS ###
	  					"Bo",
	  					"Bichero",
	  					"Lanza",
	  					"Gladius",
	  				),### Life ###
	  				300,
	  				# Energy
	  				540, 
	  			),
	  			( ################## 2 ##################
	  				(### ESCUDOS ###
	  					"Escudo1",
	  					"Escudo9",
	  				),
	  				(### ESPADAS ###
	  					"Naginata",
	  					"Tridente",
	  					"Axpear",
	  					"Maza2",
	  				),### Life ###
	  				2200,
	  				# Energy
	  				1210, 
	  			),
	  			( ################## 3 ##################
	  				(### ESCUDOS ###
	  					"KingShield",
	  					"Escudo3",
	  				),
	  				(### ESPADAS ###
	  					"DeathBo",
	  					"Crosspear",
	  					"Hachacuchilla",
	  					"Dagesse",
	  				),### Life ###
	  				4200,
	  				# Energy
	  				3000, 
	  			),
	  			( ################## 4 ##################
	  				(### ESCUDOS ###
	  					"Escudo6",
	  				),
	  				(### ESPADAS ###
	  					"Arpon",
	  					"Naginata2",
	  					"LanzaAncha",
	  					"Espadafilo",
	  				),### Life ###
	  				6200,
	  				# Energy
	  				8600, 
	  			),
	  		],
	}

	
def AddStandardWeapons2Char(EntityName,Typo="Knight",Handicap=4):

	ent = Bladex.GetEntity(EntityName)
	INV = ent.GetInventory()
	
	Weapons = PJ_CFG[Typo][Handicap-1][1]

	First = 1
	ent.Data.NetWeapons = []
	for arma in Weapons:
		sword=Bladex.CreateEntity("xxx"+Bladex.GenerateEntityName(),arma,0,0,0)
		print arma
		swordName = sword.Name
		sword.Weapon=1
		Breakings.SetBreakableWS(swordName)
		flag=Reference.GiveWeaponFlag(swordName)
		INV.AddWeapon(swordName,flag)
		ent.Data.NetWeapons.append(swordName)
		if First:
			INV.LinkRightHand(swordName)
			First = 0

	ent.Level         = 19
	ent.Life          = PJ_CFG[Typo][Handicap-1][2]
	ent.Data.NetLevel = Handicap
	ent.Data.NetLife  = ent.Life

def AddStandardShields2Char(EntityName,Typo="Knight",Handicap=4):

	ent = Bladex.GetEntity(EntityName)
	INV = ent.GetInventory()
	
	Shields = PJ_CFG[Typo][Handicap-1][0]
	Weapons = PJ_CFG[Typo][Handicap-1][1]

	First = 1
	for arma in Shields:
		# Escudo redondo
		shield=Bladex.CreateEntity("xxx"+Bladex.GenerateEntityName(),arma,0,0,0)
		print arma
		shieldname = shield.Name
		Sparks.MakeShield(shieldname)
		Breakings.SetBreakableWS(shieldname)
		INV.AddShield(shieldname)
		ent.Data.NetWeapons.append(shieldname)
		if First:
			First = 0
			if Reference.DefaultObjectData[Weapons[0]][5][0] == Reference.W_FLAG_1H:
				INV.LinkLeftHand(shieldname)
			
			

def GetDefense(Typo,Handicap):
	return CharStats.GetCharDefenseData(Typo,PJ_DEF[Handicap-1])

def GetDamage(Typo,Handicap):
	return CharStats.GetCharDamageData(Typo,PJ_ATT[Handicap-1])

def GetEnergy(pers):
	try:
		return PJ_CFG[pers.Kind][pers.Data.NetLevel-1][3]
		
	except:
		return 14
