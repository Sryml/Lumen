import Bladex
import darfuncs
import Basic_Funcs


import GotoMapVars


print "executing pj.py  2dMap"


GotoMapVars.Get2DMapValues()

char = Bladex.CreateEntity("Player1","Spidersmall",0,0,0,"Person")
darfuncs.HideBadGuy("Player1")


char=Bladex.GetEntity("Player1")
char.Data=Basic_Funcs.PlayerPerson(char)
