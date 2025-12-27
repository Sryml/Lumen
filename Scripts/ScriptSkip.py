# Created 3/7/2000 by Wolfson
# Script handling data and procs needed to perform scripted animation skipping
# cenerates .py files in the ./pak directory

import pickle
import Bladex
import AuxFuncs
import Reference
import copy

TempTime	= 0
TempName	= ""
SkipTimes	= {}

# To be Called at the deactivateinput() call level
def SkipScriptStart(name):
	global TempName
	global TempTime
	global SkipTimes

	#print("oka, started")

	AuxFuncs.DeactivateKeyboard()

	# Open File w data
	opened = 1

	try:
		SkippingDataFile = open("./pak/SDF.txt","r")
	except:
		opened	= 0

	# Place Data in phython object
	if opened:
		skiptimes = pickle.load(SkippingDataFile)
		SkippingDataFile.close()
		SkipTimes = copy.copy(skiptimes)

	TempName = copy.copy(name)
	TempTime = Bladex.GetTime()

# To be Called at the activateinput() call level
# In script end, we always save time data, but, since we alter the clock in the enter/esc call
# the saved value still holds the correct timming data

def SkipScriptEnd2():
	global TempTime
	global SkipTimes
	global TempName

	print("SkipScript Ended")
	AuxFuncs.ActivateKeyboard()
	Bladex.ResumeSoundSystem()

	TempTime = Bladex.GetTime() - TempTime # Elapsed time from script-begin to script-end
	SkipTimes[TempName] = TempTime
	TempName = "NonValidName" # Security lock, in case we call SkipCalled out-of-the-nest

	opened = 1

	try:
		SkippingDataFile = open("./pak/SDF.txt","w")
	except:
		opened	= 0

	# Place data in file
	if opened:
		skiptimes= copy.copy(SkipTimes)
		pickle.dump(skiptimes, SkippingDataFile, 0)

		SkippingDataFile.close()

# To be Called on ESC event while input is deactivated
def SkipCalled():
	import GameText
	global TempName
	global SkipTimes
	global TempTime

	if SkipTimes.has_key(TempName):
		TimeToSkip = SkipTimes[TempName] - (Bladex.GetTime() - TempTime)
		if TimeToSkip > 0: # Safety check
			GameText.AbortText()
			Bladex.PauseSoundSystemButMusic()
			Bladex.ShutDownSoundChannels()
			Bladex.GoToTime(Bladex.GetTime() + TimeToSkip)
			GameText.AbortText()
		else:
			print("Wolfson's Error: Negative index for script skipping, timing may be wrong")
	else:
		print("Wolfson's Error: SkipCalled called outta nest")

def SkipScriptEnd():
	Bladex.AddScheduledFunc(Bladex.GetTime(), SkipScriptEnd2, (), "SkipScriptEnd2")
