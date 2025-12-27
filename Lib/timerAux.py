##########################################################
#
#	SCRIPT	: simplificacion de los timers
#
#	AUTH	: Yuio
#
#
##########################################################

import Bladex

TimerDictionary={} # dictionary of functions

def unhandledTimer( entName, startTime, totalTime, val, data ) :
	print "unhandledTimer(",entName,",",startTime,",",totalTime,",",val,",",data,")"

def unhandledTimerEnd( entName ) :
	print "unhandledTimerEnd(",entName,")"

def lock( entName, data, totalTime, handler=0, endhandler=0 ):
	if (not handler) : handler = unhandledTimer
	if (not endhandler) : endhandler = unhandledTimerEnd
	TimerDictionary[entName]= Bladex.GetTime(), totalTime, entName, data, handler, endhandler

def unlock(entName):
	del TimerDictionary[entName]

Bladex.CreateTimer("TimerAuxT",0.20)
def run(entName):
	ent = Bladex.GetEntity(entName)
	TimerDictionary[entName] = Bladex.GetTime(), TimerDictionary[entName][1], TimerDictionary[entName][2], TimerDictionary[entName][3], TimerDictionary[entName][4], TimerDictionary[entName][5]
	ent.SubscribeToList("TimerAuxT")
	ent.TimerFunc = timerAuxHandler

def manualTermination(entName):
	ent = Bladex.GetEntity(entName)
	ent.RemoveFromList("TimerAuxT")
	ent.TimerFunc = ""

	endhandler	= TimerDictionary[entName][5]
	endhandler(entName)

def timerAuxHandler(ent, time):
	end			= 0
	time		= Bladex.GetTime()
	startTime	= TimerDictionary[ent][0]
	totalTime	= TimerDictionary[ent][1]
	if (time>(startTime+totalTime)) :
		time=startTime+totalTime
		end = 1
	handler		= TimerDictionary[ent][4]
	val			= (time-startTime)/totalTime
	handler( TimerDictionary[ent][2], startTime , totalTime, val, TimerDictionary[ent][3] )
	if (end) : manualTermination(ent)

