#########################################################
#														#
# Bolones a lo Indiana Jones			(en 2 sitios)	#
#														#
# (Yuio)												#
#														#
#########################################################

import Reference
import Select
import Change
import Actions
#import AniSound
import stone
import darfuncs
import ReadGSFile


######## pedruscos tochos
MESSAGE_START_WEAPON=7

"""
def x(v):
	o=Bladex.CreateEntity("Stone0","Roca2Aurelio",char.Position[0],char.Position[1],char.Position[2])
	o.Move(0,-v,0)
	o.Weapon = 1
	o.ExclusionMask = o.ExclusionMask | SolidMask.EX_PERSON
	o.MessageEvent(MESSAGE_START_WEAPON,0,0)
	o.Scale=1.000000
	o.Orientation=0.707107,0.707107,0.000000,0.000000
	o.Position = -6786.691000,-33639.532000,-48643.408000
	o.InflictHitFunc	= BedRockDie	
	o.Impulse(1,1,1)
	return o
o=x(5000)

	o.Weapon = 1
	o.ExclusionMask = o.ExclusionMask | SolidMask.EX_PERSON
	o.MessageEvent(MESSAGE_START_WEAPON,0,0)	

"""


o = heavyObjects.CreateHeavyObject("Stone0","Roca2Aurelio",(-6786.691000,-33639.532000,-48643.408000),r,1.0, BedRockDie )
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.Position = -6786.691000,-33639.532000,-48643.408000
o.InflictHitFunc	= BedRockDie

o = heavyObjects.CreateHeavyObject("Stone1","Roca1Aurelio",(-9417.124000,-33629.342000,-48660.696000),r,1.0, BedRockDie )
o.Scale=0.827740
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.InflictHitFunc	= BedRockDie


o = heavyObjects.CreateHeavyObject("Stone2","Roca1Aurelio",(-4586.740000,-33305.852000,-49065.785000),r,1.0, BedRockDie )
o.Scale=0.671653
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.InflictHitFunc	= BedRockDie
	

o = heavyObjects.CreateHeavyObject("Stone3","Roca1Aurelio",(-26069.327000,-32000.597000,-49074.655000),r,1.0, BedRockDie )
o.Scale=0.803396
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.InflictHitFunc	= BedRockDie
 
o = heavyObjects.CreateHeavyObject("Stone4","Roca1Aurelio",(-23836.285000,-31453.580000,-50062.393000),r,1.0, BedRockDie )
o.Scale=0.639055
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.InflictHitFunc	= BedRockDie


o = heavyObjects.CreateHeavyObject("Stone5","Roca1Aurelio",(-898.288000,-34311.873000,-46668.861000),r,1.0, BedRockDie )
o.Scale=0.671653
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.InflictHitFunc	= BedRockDie


#### desprendimiento

stone.lock( "Stone0", stone.DROPBROWNDUST, 0, 200, 0.0, 0.1, 9.0, stone.SOUNDNULL, 0.1 ) 
stone.lock( "Stone1", stone.DROPBROWNDUST, 0, 200, 0.0, 0.1, 9.0, stone.SOUNDNULL, 0.1 ) 
stone.lock( "Stone2", stone.DROPBROWNDUST, 0, 200, 0.0, 0.1, 9.0, stone.SOUNDNULL, 0.1 ) 
stone.lock( "Stone3", stone.DROPBROWNDUST, 0, 200, 0.0, 0.1, 9.0, stone.STONESOUND, 0.1 ) 
stone.lock( "Stone4", stone.DROPBROWNDUST, 0, 200, 0.0, 0.1, 9.0, stone.SOUNDNULL, 0.1 ) 
stone.lock( "Stone5", stone.DROPBROWNDUST, 0, 200, 0.0, 0.1, 9.0, stone.SOUNDNULL, 0.1 ) 


dropUsed=0

DSector=Bladex.GetSector(0, -20000, -58000)
DSector.OnEnter=dropAllStones
#DSector2=Bladex.GetSector(8000, -18000, -58000) 
#DSector2.OnEnter=dropAllStones

#### rotura del puente

bridgeBroken=0


######### puente

brokenBridge1=Bladex.GetSector(-7250, -15500, -58125)
brokenBridge2=Bladex.GetSector(-4750, -15500, -58125)
brokenBridge3=Bladex.GetSector(-1750, -15500, -58125)

brokenBridge1.Active=0
brokenBridge2.Active=0
brokenBridge3.Active=0

brokenBridge1.InitBreak((0.0, 100.0, 0.0), (2100.0, 0.0, -100.0), (170.0, 0.0, 1350.0) ,'madera pesada')
brokenBridge2.InitBreak((0.0, 100.0, 0.0), (24625.0, 0.0, -150.0), (200.0, 0.0, 1420.0) ,'madera pesada')
brokenBridge3.InitBreak((0.0, 100.0, 0.0), (2376.0, 0.0, -120.0), (230.0, 0.0, 1470.0) ,'madera pesada')

res=ReadGSFile.ReadGhostSectorFile("puente.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

char.SendTriggerSectorMsgs=1
#esp=Bladex.GetEntity("WeaponInvPrb1")
#esp.SendTriggerSectorMsgs=1

Bladex.SetTriggerSectorFunc("Tmp", "OnEnter", brokeBridge )
