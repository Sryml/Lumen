import Basic_Funcs

char=Bladex.CreateEntity("Player1","Spidersmall",0,0,0,"Person")
char.Data=Basic_Funcs.PlayerPerson(char)
char.Freeze()
char.RemoveFromWorld()
char.Alpha = 0



