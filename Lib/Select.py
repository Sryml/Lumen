import Bladex
import Reference
import netgame



TRUE=(1==1)
FALSE=(1!=1)

if netgame.GetNetState() == 2:
	MAX_VISIBLE_ENEMIES_DISTANCE = 80000
	MAX_SELECTION_DISTANCE=8000.0	
else:
##	me=Bladex.GetEntity("Player1")
##	chartype = Bladex.GetCharType(me.CharType,me.CharTypeExt)
##	MAX_VISIBLE_ENEMIES_DISTANCE=chartype.MaxCombatDist
	MAX_SELECTION_DISTANCE=8000.0




AUTOSELECT_PERIOD=0.2
Gpj=None

def SqDistanceToGpj(entity):
	global Gpj
	return(Gpj.SQDistance2(entity))

def GetSelectionData(entity_name):
	entity=Bladex.GetEntity(entity_name)
	if(Reference.EntitiesSelectionData.has_key(entity_name)):
		return(Reference.EntitiesSelectionData[entity_name])
	elif(Reference.DefaultSelectionData.has_key(entity.Kind)):
		return(Reference.DefaultSelectionData[entity.Kind])
	else: return(None)

def IsValidForSelection(entity_entry):
	if(entity_entry[1]):
		entity_name=entity_entry[0]
		entity=Bladex.GetEntity(entity_name)
		if(entity):
			try:
				if entity.Data.Estado == 0:
					return(FALSE)
			except:
				pass
			parent_name=entity.Parent;
			if(parent_name!=None):
				if(parent_name!=""):
					parent=Bladex.GetEntity(parent_name)
					if(parent.Person):
						return(FALSE)
		else:
			return(FALSE)
		if(SqDistanceToGpj(entity)>entity_entry[1][1]*entity_entry[1][1]):
			return(FALSE)
	else:
		return(FALSE)
	return(TRUE)

def GetMoreInterestingEntity(pj,list):
	target=None
	priority=0.0
	sqdistance=MAX_SELECTION_DISTANCE*MAX_SELECTION_DISTANCE
	for x in list:
		if(priority<x[1][0] or (priority==x[1][0] and sqdistance>SqDistanceToGpj(Bladex.GetEntity(x[0])))):
			target=x
			priority=x[1][0]
			sqdistance=SqDistanceToGpj(Bladex.GetEntity(x[0]))
	return(target)


def GetNextMoreInterestingEntity(pj,list,sentry):
	target=None
	priority=0.0
	sqdistance=MAX_SELECTION_DISTANCE*MAX_SELECTION_DISTANCE

	spriority=sentry[1][0]
	ssqdistance=SqDistanceToGpj(Bladex.GetEntity(sentry[0]))
	
	for x in list:
		if(priority<x[1][0] or (priority==x[1][0] and sqdistance>SqDistanceToGpj(Bladex.GetEntity(x[0])))):
			if(spriority>x[1][0] or (spriority==x[1][0] and ssqdistance<SqDistanceToGpj(Bladex.GetEntity(x[0])))):
				target=x
				priority=x[1][0]
				sqdistance=SqDistanceToGpj(Bladex.GetEntity(x[0]))
	return(target)

def GetFromList(entity_entry,list):
	for x in list:
		if(x[0]==entity_entry[0]):
			return(entity_entry)
	return(None)

def GetNextFromList(entity_entry,list):
	for x in range(1,len(list)+1):
		if(list[x-1][0]==entity_entry[0]):
			if(x==len(list)):
				return list[0]
			else:
				return(list[x])
	return(None)

def GetPreviousFromList(entity_entry,list):
	for x in range(-1,len(list) - 1):
		if(list[x+1][0]==entity_entry[0]):
			if(x==-1):
				return list[len(list) - 1]
			else:
				return(list[x])	
	return(None)

def SelectNext(pj):
	global Gpj
	Gpj=pj
	head_pos=pj.Rel2AbsPoint(0.0,0.0,0.0,"Head")
	pj_dir=pj.Rel2AbsVector(0.0,-1.0,0.0)
	list=Bladex.GetObjectEntitiesVisibleFrom(head_pos,MAX_SELECTION_DISTANCE,pj_dir,0.0)
	list=map(None,list,map(GetSelectionData,list))
	list=filter(IsValidForSelection,list)

	if(pj.Data.selection_locked and pj.Data.selected_entity):
		target=GetFromList(pj.Data.selected_entity,list)
		if(not target):
			pj.Data.selection_locked=FALSE
			target=GetMoreInterestingEntity(pj,list)
		else:
			target=GetNextMoreInterestingEntity(pj,list,pj.Data.selected_entity)
			if(not target):
				target=GetMoreInterestingEntity(pj,list)
	else:
		pj.Data.selection_locked=FALSE
		target=GetMoreInterestingEntity(pj,list)
	
	pj.Data.selected_entity=target

	if(target):
		pj.LookAtEntity(target[0])
	else:
		pj.LookAtEntity("")
		pj.StopLooking()


def AutoSelect(pj):
	global Gpj
	Gpj=pj
	head_pos=pj.Rel2AbsPoint(0.0,0.0,0.0,"Head")
	pj_dir=pj.Rel2AbsVector(0.0,-1.0,0.0)
	list=Bladex.GetObjectEntitiesVisibleFrom(head_pos,MAX_SELECTION_DISTANCE,pj_dir,0.0)
	list=map(None,list,map(GetSelectionData,list))
	list=filter(IsValidForSelection,list)

	if(pj.Data.selection_locked and pj.Data.selected_entity):
		target=GetFromList(pj.Data.selected_entity,list)
		if(not target):
			pj.Data.selection_locked=FALSE
			target=GetMoreInterestingEntity(pj,list)
	else:
		pj.Data.selection_locked=FALSE
		target=GetMoreInterestingEntity(pj,list)
	
	pj.Data.selected_entity=target


def GetEnemiesScorerData(entity_name):
	entity=Bladex.GetEntity(entity_name)
	if(Reference.EnemiesScorerData.has_key(entity_name)):
		return(Reference.EnemiesScorerData[entity_name])
	elif(Reference.EnemiesDefaultScorerData.has_key(entity.MeshName)):
		return(Reference.EnemiesDefaultScorerData[entity.MeshName])
	else:
		if(Reference.EnemiesDefaultScorerData.has_key(entity.Kind)):
			return(Reference.EnemiesDefaultScorerData[entity.Kind])
		else:
			return(None)

def Distance2Pj(enemy_entry):
	global Gpj
	enemy=Bladex.GetEntity(enemy_entry[0])
	return(Gpj.SQDistance2(enemy))


def ShortEnemiesList(pj):
	global Gpj
	Gpj=pj	
	list=pj.Data.visible_enemies
	if(len(list)):
		distances=map(Distance2Pj,list)
		for i in range(len(list)-1):
			for j in range(len(list)-1):
				if(distances[j]>distances[j+1]):
					tmp=distances[j]
					distances[j]=distances[j+1]
					distances[j+1]=tmp
					tmp=list[j]
					list[j]=list[j+1]
					list[j+1]=tmp
				


def SelectNextEnemy(pj, backward=0):
	chartype = Bladex.GetCharType(pj.CharType,pj.CharTypeExt)
	MAX_VISIBLE_ENEMIES_DISTANCE=chartype.MaxCombatDist
	head_pos=pj.Rel2AbsPoint(0.0,0.0,0.0) #,"Head")
	pj_dir=pj.Rel2AbsVector(0.0,-1.0,0.0)
	list=Bladex.GetEnemiesVisibleFrom(head_pos,MAX_VISIBLE_ENEMIES_DISTANCE,pj_dir,0.0)
	list=map(None,list,map(GetEnemiesScorerData,list))
	pj.Data.visible_enemies=list
	if(len(pj.Data.visible_enemies)):
		ShortEnemiesList(pj)
		if(pj.Data.enemy_locked and pj.Data.selected_enemy):
			if not backward:
				target=GetNextFromList(pj.Data.selected_enemy,list)
			else:
				target=GetPreviousFromList(pj.Data.selected_enemy,list)

			if(not target):
				pj.Data.enemy_locked=FALSE
			else:
				pj.Data.selected_enemy=target
		else:
			pj.Data.selected_enemy=pj.Data.visible_enemies[0]
	else:
		pj.Data.enemy_locked=FALSE
		pj.Data.selected_enemy=None


import pdb

def GetVisibleEnemies(pj):
	head_pos=pj.Rel2AbsPoint(0.0,0.0,0.0) #,"Head")
	
	if ( pj.AnimName=="g_back" or pj.AnimName=="g2h_back") and pj.AnmPos>0.6:	
		dir_y=1.0		
	else:
		dir_y=-1.0
	chartype = Bladex.GetCharType(pj.CharType,pj.CharTypeExt)
	MAX_VISIBLE_ENEMIES_DISTANCE=chartype.MaxCombatDist
	pj_dir=pj.Rel2AbsVector(0.0,dir_y,0.0)
	list=Bladex.GetEnemiesVisibleFrom(head_pos,MAX_VISIBLE_ENEMIES_DISTANCE,pj_dir,0.0)
	list=map(None,list,map(GetEnemiesScorerData,list))
	pj.Data.visible_enemies=list
	if(len(pj.Data.visible_enemies)):
		ShortEnemiesList(pj)
		if(pj.Data.enemy_locked and pj.Data.selected_enemy):
			target=GetFromList(pj.Data.selected_enemy,list)
			if(not target):
				pj.Data.enemy_locked=FALSE
				pj.Data.selected_enemy=pj.Data.visible_enemies[0]
		else:
			pj.Data.selected_enemy=pj.Data.visible_enemies[0]
	else:
		pj.Data.enemy_locked=FALSE
		pj.Data.selected_enemy=None





def PeriodicAutoSelect(pj_name, look_for_enemies=1, autoselect_period=AUTOSELECT_PERIOD):
	import DefaultSelectionData

	pj=Bladex.GetEntity(pj_name) # Puede ser None
	
	if pj and pj.Data.auto_select:
		AutoSelect(pj)
		GetVisibleEnemies(pj)
	
		if(pj.Data.selected_enemy):
			pj.LookAtEntity(pj.Data.selected_enemy[0])
		else:
			if(pj.Data.selected_entity):
				pj.LookAtEntity(pj.Data.selected_entity[0])
				if(pj.Data.selected_entity and (not pj.Data.selection_locked) and (pj.Data.selected_entity[1][0]>6)):
					DefaultSelectionData.SelectObject()
			else:
				pj.LookAtEntity("")
				pj.StopLooking()




		Bladex.AddScheduledFunc(Bladex.GetTime()+autoselect_period,PeriodicAutoSelect,(pj_name,look_for_enemies,autoselect_period),"PeriodicAutoSelect"+pj_name)


def AutoSelectInAttack(EntityName):
	import DefaultSelectionData

	pj=Bladex.GetEntity(EntityName)
	
	if pj and not pj.Data.NPC and Bladex.GetAutoEngageCombat():
		if not pj.InCombat:
			DefaultSelectionData.SelectEnemy()





def TurnOnAutoSelect(pj_name, look_for_enemies=1, autoselect_period=AUTOSELECT_PERIOD):
	pj=Bladex.GetEntity(pj_name)
	if pj.Data:
		pj.Data.selected_entity=None
		pj.Data.selection_locked=FALSE
		pj.Data.visible_enemies=()
		pj.Data.selected_enemy=None
		pj.Data.enemy_locked=FALSE
		pj.Data.auto_select=TRUE
	else:
		Bladex.AddScheduledFunc(Bladex.GetTime(), TurnOnAutoSelect, (pj_name, look_for_enemies, autoselect_period), "DeferredTurnOnAutoSelect"+pj_name)
		return
	# Make sure that we don't have multiple  versions running at the same time
	Bladex.RemoveScheduledFunc("TurnOnAutoSelect"+pj_name)
	Bladex.RemoveScheduledFunc("PeriodicAutoSelect"+pj_name)

	Bladex.AddScheduledFunc(Bladex.GetTime()+autoselect_period,PeriodicAutoSelect,(pj_name,look_for_enemies,autoselect_period),"TurnOnAutoSelect"+pj_name)

def TurnOffAutoSelect(pj_name):
	pj=Bladex.GetEntity(pj_name)
	pj.Data.auto_select=FALSE
