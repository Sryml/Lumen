import Bladex
import Traps_C

Traps_C.InitSector()

last_room = 0

rooms = [0,0]

class ROOM:
	def __init__(self,enter,leave,sld):
		self.n_entrances = 0
		self.room = 0
		self.entrance = 0
		self.inside = 0
		self.enter_func = enter
		self.leave_func = leave
		self.sld = sld
		self.sld_doors = [0,0]

	def IsInside(self):
		return self.inside

	def AddDoor(self,sector_x,sector_y,sector_z):
		sector = Bladex.GetSector(sector_x,sector_y,sector_z)
		i = Traps_C.AddSector(sector,self)
		rooms[i:i] = [self]
		self.sld_doors[self.n_entrances:self.n_entrances] = [sector.Index]
		sector.OnEnter = EnterEntrance
		sector.OnLeave = LeaveEntrance
		self.n_entrances = self.n_entrances + 1

	def AddEntity(self,name):
		Traps_C.AddName(self.sld,name)

		for i in range(self.n_entrances):
			Traps_C.AddName(self.sld_doors[i],name)

	def AddAllObjects(self,v):
		Traps_C.AddAllObjects(self.sld,v)
	
		for i in range(self.n_entrances):
			Traps_C.AddAllObjects(self.sld_doors[i],v)


	def AddAllPersons(self,v):
		Traps_C.AddAllPersons(self.sld,v)	
			
		for i in range(self.n_entrances):
			Traps_C.AddAllPersons(self.sld_doors[i],v)

def CreateRoom(sector_x,sector_y,sector_z,enter_func,leave_func):	
	sector = Bladex.GetSector(sector_x,sector_y,sector_z)
	room = ROOM(enter_func,leave_func,sector.Index)	
	i = Traps_C.AddSector(sector,room)
	rooms[i:i] = [room]
	sector.OnEnter = EnterRoom
	sector.OnLeave = LeaveRoom

	return room

def EnterEntrance(sld,entity):
	i = Traps_C.IsValidEntity(sld,entity)		
	if (i >= 0):
		p = rooms[i]
		p.entrance = 1
		p.room = 0

def EnterRoom(sld,entity):
	i = Traps_C.IsValidEntity(sld,entity)
	if (i >= 0):
		p = rooms[i]
		p.room = 1

def LeaveRoom(sld,entity):
	i = Traps_C.IsValidEntity(sld,entity)
	if (i >= 0):
		p = rooms[i]
		p.room = 0

		if (p.inside):
			p.inside = 0
			if (p.entrance):
				apply(p.leave_func, (sld,entity))

def LeaveEntrance(sld,entity):
	i = Traps_C.IsValidEntity(sld,entity)
	if (i >= 0):
		p = rooms[i]
		p.entrance = 0

		if (p.room):
			p.inside = 1		
			apply(p.enter_func, (sld,entity))