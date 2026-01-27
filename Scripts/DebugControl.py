# This script is written automatically in the config controls
# and is really for defining key asociations with Actions

#pdb.set_trace()
ON_RELEASE=0
ON_PRESS=1	# default

import Bladex
import Lumenx
import Reference
import BInput

InputManager=BInput.GetInputManager()
OldIASet = InputManager.GetInputActionsSet()
InputManager.SetInputActionsSet("Default")  # Me aseguro de definir las acciones en el grupo correcto


ON_RELEASE=0
ON_PRESS=1	# default




Bladex.AssocKey("Swim Up","Keyboard","4")
Bladex.AssocKey("Swim Down","Keyboard","5")
Bladex.AssocKey("ToggleStats","Keyboard","T")
Bladex.AssocKey("ToggleSampling","Keyboard","V")
Bladex.AssocKey("ToggleProfiling","Keyboard","F3")
Bladex.AssocKey("Toggle BB","Keyboard","F4")
Bladex.AssocKey("Camera Left","Keyboard","F5")
Bladex.AssocKey("Camera Right","Keyboard","F6")
Bladex.AssocKey("Change Camera","Keyboard","F7")
Bladex.AssocKey("Fixed Camera","Keyboard","F8")
Bladex.AssocKey("Camera Dist","Keyboard","F9")
Bladex.AssocKey("ToggleInvincibility","Keyboard","F10")
# Bladex.AssocKey("Bigger FOV","Keyboard","F11")
Bladex.AssocKey("Smaller FOV","Keyboard","F12")
Bladex.AssocKey("Change Mov","Keyboard","P")

print "Executed DebugControl.py"

# uuid.uuid5(uuid.NAMESPACE_OID,"Lumen:MataEnemigo")
MataEnemigoWP = Bladex.GetEntity("b0665d50-c59c-5dfd-82b7-115cf93b9633")
if not MataEnemigoWP:
	MataEnemigoWP = Bladex.CreateEntity("b0665d50-c59c-5dfd-82b7-115cf93b9633", "Gladius", 0, 0, 0, "Weapon")
	MataEnemigoWP.Alpha = 0
	MataEnemigoWP.RemoveFromWorld()
Reference.EntitiesObjectData[MataEnemigoWP.Name] = [Reference.OBJ_WEAPON,  5000, 0, 2.2,  Reference.THR_SPINNING, [Reference.W_FLAG_1H,]]
def MataEnemigoEncarado():
	char = Lumenx.GetControlCharacter()
	victim_name = char.ActiveEnemy or char.Data.selected_enemy and char.Data.selected_enemy[0]
	if victim_name:
		victim = Bladex.GetEntity(victim_name)
		if victim.DamageFunc:
			victim.DamageFunc(victim_name, char.Name, MataEnemigoWP.Name, "Debug", 1, -1, 0,-1,0, 0)
		elif victim.Life<2:
			victim.Life=0
		else:
			victim.Life=1


Bladex.AddInputAction("Mata", 0)
Bladex.AssocKey("Mata", "Keyboard", "K")
Bladex.AddBoundFunc("Mata", MataEnemigoEncarado)

import cPickle
import ObjStore
import os
from stat import *

def TestSave():
	print "TestSave"
	filename="test.dat"

	print "Checkstore"
	ObjStore.CheckStore()

	funcfile=open(filename,"wt")
	print "Pickler"
	p=cPickle.Pickler(funcfile)
	print "Dump"
	p.dump(ObjStore.ObjectsStore)
	funcfile.close()
	size = os.stat("/tmp/test.dat")[ST_SIZE]
	print "File size = "
	print size

	if size < 40000:
		print "===================================== CHECK !!!! ======================"

# Bladex.AddInputAction("Test", 0)
# Bladex.AssocKey("Test", "Keyboard", "Q")
# Bladex.AddBoundFunc("Test", TestSave)

InputManager.SetInputActionsSet(OldIASet)
