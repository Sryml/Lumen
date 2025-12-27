##########################################################
#
#	SCRIPT	: sistema de paths simples para los persons
#
#	AUTH	: Yuio
#
#
##########################################################

import Bladex

PPathPos={}
PPathDictionary={}

def routeEnd(ent) :
	if ( PPathPos[ent] == PPathDictionary[ent][2] ) :
		#print"route end at point",PPathPos[ent]
		func = PPathDictionary[ent][1]
		if (func) :	func ( ent )
	else:
		#print"going to point:",PPathPos[ent]
		pers = Bladex.GetEntity(ent)
		pos = PPathDictionary[ent][3][PPathPos[ent]]
		pers.GoTo( pos[0],pos[1],pos[2] )
		pers.RouteEndedFunc = routeEnd
		PPathPos[ent]=PPathPos[ent]+1

def unlock(entName):
	del PPathPos[entName]
	del PPathDictionary[entName]

def lock( entName, endFunc, pathPointsN, pathPointsVecs ):
	if (PPathPos.has_key(entName)) : unlock(entName)
	PPathPos[entName] = 0
	PPathDictionary[entName] = entName, endFunc, pathPointsN, pathPointsVecs
	routeEnd(entName)


#persPath.lock("Player1",0,4,((-32484.9670546, 6953.2, -50721.8465672),(-39741.9550376, 6762.66279411, -44862.1058203),(-37973.714983, 5965.4, -29988.8561349),(-35688.677572, 6442.76323088, -42246.6595328)))
