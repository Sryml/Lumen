#
#
#	Path_test.py
#
#
#
#	File to test the path planning
#
#	Put it in any map directory and load it from the cfg.py ( at the end of the file) (or import it)
#
#
#	KEYS :
#
#	1 -> Puts a traitor_knight two meters from you ( be careful to select a open area , it could crash otherwise )
#
#   2 -> Adds a new point to the patrol
#		 Use it as many times as desired
#
#	3 -> End the route ( that given point included ) , and launch the patrol
#
#	4 -> kill him!
#
#   Enjoy ! ;)
#



import Bladex
import EnemyTypes
import Breakings 


last_person_name=""


def AddBay():
	global last_person_name
	print "AddBay In"
	new_person=Bladex.GetEntity(last_person_name)
	player1=Bladex.GetEntity("Player1")
	pos=player1.Position
	new_person.AddBayPoint=pos[0],pos[1],pos[2]
	print "AddBay Out"


def PutPerson():		
	global last_person_name
		
	player1=Bladex.GetEntity("Player1")
	last_person_name=Bladex.GenerateEntityName()	

	pos=player1.Position	
	new_person=Bladex.CreateEntity(last_person_name, "Knight_Traitor",pos[0]+1750,pos[1],pos[2])
	new_person.Person=1
	new_person.Angle=player1.Angle
	EnemyTypes.EnemyDefaultFuncs(new_person)

	o=Bladex.CreateEntity(Bladex.GenerateEntityName(),"Espadaromana",0,0,0)
	o.Weapon=1
	inv=new_person.GetInventory()
	inv.AddWeapon(o.Name)
	inv.LinkRightHand(o.Name)

	new_person.Blind=1
	new_person.Deaf=1		



def EndBay():
	global last_person_name
	print "EndBay In"
	AddBay()
	new_person=Bladex.GetEntity(last_person_name)
	en_pos=new_person.Position
	new_person.AddBayPoint=en_pos[0],en_pos[1],en_pos[2]
	new_person.LaunchBayRoute()
	print "EndBay Out"

def ResetMe():
	global last_person_name
	print "Reseting..."	
	new_person=Bladex.GetEntity(last_person_name)
	en_pos=new_person.InitPos
	new_person.Position=en_pos[0],en_pos[1],en_pos[2]	
	new_person.LaunchBayRoute()
	print "ResetMe Out"


def KillMe():
	global last_person_name
	new_person=Bladex.GetEntity(last_person_name)
	new_person.Life=0


def PutBox():
	print "PutBox In" 
	player1=Bladex.GetEntity("Player1")
	box_name=Bladex.GenerateEntityName()

	pos=player1.Position
	new_box=Bladex.CreateEntity(box_name, "Cajon2",pos[0]+1750,pos[1],pos[2])
	new_box.Static=1

	Breakings.SetBreakable(box_name, 2)

	print "PutBox Out"

Bladex.AddInputAction("PutPerson",0)
Bladex.AssocKey("PutPerson","Keyboard","1", 1 )
Bladex.AddBoundFunc("PutPerson",PutPerson)


Bladex.AddInputAction("AddBay",0)
Bladex.AssocKey("AddBay","Keyboard","2",1 )
Bladex.AddBoundFunc("AddBay",AddBay)


Bladex.AddInputAction("EndBay",0)
Bladex.AssocKey("EndBay","Keyboard","3",1 )
Bladex.AddBoundFunc("EndBay",EndBay)


Bladex.AddInputAction("KillMe",0)
Bladex.AssocKey("KillMe","Keyboard","4",1 )
Bladex.AddBoundFunc("KillMe",KillMe)

Bladex.AddInputAction("ResetMe",0)
Bladex.AssocKey("ResetMe","Keyboard","9",1 )
Bladex.AddBoundFunc("ResetMe",ResetMe)


Bladex.AddInputAction("PutBox",0)
Bladex.AssocKey("PutBox","Keyboard","0",1 )
Bladex.AddBoundFunc("PutBox",PutBox)

