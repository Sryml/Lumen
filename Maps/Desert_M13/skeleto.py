import darfuncs
import EnemyTypes
import PhantonFX


	

#skeketo magico

#1
espada=Bladex.CreateEntity("DESERTCimitarra2","Espadafilo",0,0,0)
espada.Weapon=1
escudo=Bladex.CreateEntity("DESERTEscudo2","Escudo7",0,0,0)
Sparks.MakeShield("DESERTEscudo2")
Breakings.SetBreakableWS("DESERTEscudo2")
Breakings.SetBreakableWS("DESERTCimitarra2")

pers=Bladex.CreateEntity("CaballeroLlave","Dark_Knight",-24896.780, -2017.02, 16121.63)
pers.Person=1
pers.Level=9
pers.Angle=3.14000499744
pers.Alpha = 0.0
Actions.TakeObject(pers.Name,"DESERTCimitarra2")
Actions.TakeObject(pers.Name,"DESERTEscudo2")

pers.ActionAreaMin=pow(2,14)
pers.ActionAreaMax=pow(2,15)

Actions.TakeObject("CaballeroLlave", "llave4")

EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

darfuncs.HideBadGuy("CaballeroLlave")

