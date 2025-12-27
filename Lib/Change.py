import Bladex
import Actions

def ChangeObject(person,object,finish_func):
	char = Bladex.GetEntity (person)
	char.Data.obj_used = object
	char.Data.hand = 0
	char.Data.FinishAnm = finish_func	

	if char.InvRight == "":
		GetObject(person)
	else:
		if Actions.IsRightHandStandardObject(person):
			GetObject(person)
			if Actions.TryDropRight(person):	
				Actions.DropReleaseEventHandler(person, "DropRightEvent")
			#if not char.InvRight:
			
		else:
			char.AddAnmEventFunc("ChangeREvent",Actions.ToggleWEvent)			
			char.LaunchAnmType("Chg_r")	
			char.Data.o_hand = char.InvRight
			char.Data.hand = 1
			char.AnmEndedFunc=GetObject

def GetObject(entity):	
	char = Bladex.GetEntity(entity)
	#char.LaunchAnmType("bag")
	#char.AddAnmEventFunc("ChangeREvent",GetingFetiche)
	char.AddAnmEventFunc("ChangeREvent",GetingObject)
	if char.Kind[0] == "D":
		char.LaunchAnmType("Dwf_bag")
	else:
		char.LaunchAnmType("Kgt_bag")


def GetingObject(entity,event):
	char = Bladex.GetEntity(entity)
	inv = char.GetInventory()				
	inv.LinkRightHand(char.Data.obj_used)
	char.AnmEndedFunc=FinishAnm
	
def FinishAnm(entity):
	char = Bladex.GetEntity(entity)
	char.Data.FinishAnm(entity,char.Data.obj_used)

def Keep(ent,event):
	char = Bladex.GetEntity(ent)
	inv = char.GetInventory()
	inv.LinkRightHand("None")


def Toggle(ent,event):
	Actions.ToggleWEvent(ent,"ChangeREvent")
	#char = Bladex.GetEntity(ent)
	#inv = char.GetInventory()	
	#inv.LinkRightHand(char.Data.o_hand)

def RestoreHand(entity,launch):
	char = Bladex.GetEntity(entity)
	inv = char.GetInventory()

	if (launch):
		if (launch == 2):
			object = Bladex.GetEntity(char.InvRight)			
			impulse = char.Rel2AbsVector(-1000.0 * object.Mass, -1000.0 * object.Mass, 0.0)
			object.Impulse(impulse[0],impulse[1],impulse[2])

		if (char.Data.hand):
			char.LaunchAnmType("Chg_r")
			char.AddAnmEventFunc("ChangeREvent",Toggle)

		inv.RemoveObject(char.InvRight)
	else:
		if (char.Data.hand):
			char.LaunchAnmType("Chg_r")
			char.AddAnmEventFunc("ChangeREvent",Toggle)
		else:
			if char.Kind[0] == "D":
				char.LaunchAnmType("Dwf_bag")
			else:
				char.LaunchAnmType("Kgt_bag")
			char.AddAnmEventFunc("ChangeREvent",Keep)

	inv.LinkRightHand("None")