#######################################################################
#
# Nam: heavyObjects.py
#
# Com: objetos que aplastan
#
# Ath: Yui0
#
#######################################################################

import Bladex
import math
import SolidMask
import Blood
import Reference
import Actions
import Breakings

MESSAGE_START_WEAPON=7								
MESSAGE_STOP_WEAPON=8								

def levanteseHombre():
	char=Bladex.GetEntity("Player1")
	char.LaunchAnmType("Rlx")
	Bladex.GetEntity("Camera").SetPersonView("Player1")
	cam = Bladex.GetEntity("Camera")	
	cam.SetPersonView("Player1")
	cam.Cut()

def StoneStopFuncHitEvent(ent):
	#print("quita la mascara")
	ent = Bladex.GetEntity(ent)
	ent.ExclusionMask = ent.ExclusionMask & (~SolidMask.EX_PERSON)

def StoneHitEvent(EntityName, VictimName, ImpX, ImpY, ImpZ):
	#print("nos hundimos!!: entname:%s victimname:%s x:%f y:%f z:%f"%(EntityName, VictimName, ImpX, ImpY, ImpZ))

	ent = Bladex.GetEntity ( VictimName )
	if (ent.Person):
		dir = ImpX, ImpY, ImpZ

		size = math.sqrt(ImpX*ImpX + ImpY*ImpY + ImpZ*ImpZ)	
		if (size>0.1) :
			#print("lleva suficiente fuerza como para matar a alguien")
			dirn = dir[0]/size , dir[1]/size , dir[2]/size
			ang = math.asin(dirn[0])
			if (dirn[2]<0.0) : ang=ang+3.1415

			char = Bladex.GetEntity("Player1")
			difang = ang - char.Angle
			difang = abs( difang - int(difang/6.28)*6.28 )

			#print("b:%f c:%f d:%f"%(ang, char.Angle, difang))
			
			ent.Life=-1
			
			if (difang<(3.14*0.5) or difang>(3.14*1.5)):
				#print("se cae pa lante")
				ent.SetTmpAnmFlags(1,1,1,0,5,1,0)
				ent.Wuea=Reference.WUEA_ENDED
				ent.LaunchAnmType("dth_rock")
			else:
				#print("se cae pa atras")
				ent.SetTmpAnmFlags(1,1,1,0,5,1,0)
				ent.Wuea=Reference.WUEA_ENDED				
				ent.LaunchAnmType("dth_rockfront")

			#if VictimName=="Player1":
			#	Bladex.GetEntity("Camera").TType=0
			#	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, levanteseHombre, ())
			#
			
			if VictimName!="Player1":
				oname = ent.InvLeft
				Actions.RemoveFromInventory(ent,Bladex.GetEntity(ent.InvLeft),0)
				try:
					if oname and Bladex.GetEntity(oname) and Bladex.GetEntity(oname).Data.brkobjdata:
						Breakings.ExplodeSpecialObject(oname,10000)
				except: pass
	
				oname = ent.InvRight
				Actions.RemoveFromInventory(ent,Bladex.GetEntity(ent.InvRight),0)
				try:
					if oname and Bladex.GetEntity(oname) and Bladex.GetEntity(oname).Data.brkobjdata:
						Breakings.ExplodeSpecialObject(oname,10000)
				except: pass

			#print("sangre")
			charPos = ent.Position			
			Blood.BleedingImpact(ent , charPos[0], charPos[1], charPos[2],9999,0,0,None,0,0,0,0,0,0)
			Blood.BleedingImpact(ent , charPos[0], charPos[1], charPos[2],9999,0,9999,None,0,0,0,0,0,0)
			Blood.BleedingImpact(ent , charPos[0], charPos[1], charPos[2],3333,0,0,None,0,0,0,0,0,0)
			Blood.BleedingImpact(ent , charPos[0], charPos[1], charPos[2],9999,0,3333,None,0,0,0,0,0,0)
			Blood.BleedingImpact(ent , charPos[0], charPos[1], charPos[2],0,0,3333,None,0,0,0,0,0,0)
			Blood.BleedingImpact(ent , charPos[0], charPos[1], charPos[2],0,0,9999,None,0,0,0,0,0,0)
			Blood.BleedingImpact(ent , charPos[0], charPos[1], charPos[2],0,0,0,None,0,0,0,0,0,0)

			#print("impulso")
			pedrolo = Bladex.GetEntity(EntityName)
			x = -pedrolo.Mass*0.000001*ImpX
			y = -3500.0*pedrolo.Mass
			z = -pedrolo.Mass*0.000001*ImpZ
			#print(pedrolo.Mass)
			#print((x,y,z))
			pedrolo.Impulse(x,y,z)

			##print("borra")
			#stone.unlock(EntityName) 
			#bolon.SubscribeToList("Pin")

			##print("ok")
			Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, RestoreInflictHitFunc,(pedrolo,))

def RestoreInflictHitFunc(o):
	o.ExclusionMask = o.ExclusionMask | SolidMask.EX_PERSON
	o.MessageEvent(MESSAGE_START_WEAPON,0,0)	
	o.InflictHitFunc	= StoneHitEvent			

def CreateHeavyObject(name,objtype,positionVec,orientationQuat,fScale, hitfunc ):
	o=Bladex.CreateEntity(name,objtype,positionVec[0],positionVec[1],positionVec[2])
	o.Scale=fScale
	o.Orientation=orientationQuat
	o.Weapon = 1
	o.ExclusionMask = o.ExclusionMask | SolidMask.EX_PERSON
	o.MessageEvent(MESSAGE_START_WEAPON,0,0)	
	o.InflictHitFunc	= hitfunc
	o.OnStopFunc		= StoneStopFuncHitEvent	

	return o
