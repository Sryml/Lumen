from math import pow
import EnemyTypes
import AniSound
import Sparks
import Actions



#11-----------------MINOTAUROS DEFENDIENDO LA PALANCA-----------



#1
#espada=Bladex.CreateEntity("garroteM1","Hachacarnicero",0,0,0,"Weapon")

#pers=Bladex.CreateEntity("1MINOT","Minotaur",62134.1, -794.6, 21441.4,"Person")
#pers.Level=8
#pers.Angle=0
#Actions.TakeObject(pers.Name,"garroteM1")

#pers.ActionAreaMin=pow(2,6)
#pers.ActionAreaMax=pow(2,7)
#EnemyTypes.EnemyDefaultFuncs(pers)
#pers.SetOnFloor()

#darfuncs.HideBadGuy("1MINOT")
#minopuen.AddGuy("1MINOT")




#2
espada=Bladex.CreateEntity("garroteM2","Mazapiedra",0,0,0,"Weapon")

pers=Bladex.CreateEntity("2MINOT","Minotaur",93488.2, -65.6, 25556.7,"Person")
pers.Level=9
pers.Angle=1.5
Actions.TakeObject(pers.Name,"garroteM2")

pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

darfuncs.HideBadGuy("2MINOT")


#3
espada=Bladex.CreateEntity("garroteM3","Mazapiedra",0,0,0,"Weapon")

pers=Bladex.CreateEntity("3MINOT","Minotaur",105031.909766, 1286.14872485, 22922.2,"Person")
pers.Level=10
pers.Angle=1.5
Actions.TakeObject(pers.Name,"garroteM3")

pers.ActionAreaMin=pow(2,6)
pers.ActionAreaMax=pow(2,7)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Deaf  = 1
pers.Blind = 1
pers.SetOnFloor()



#darfuncs.HideBadGuy("3MINOT")
#pers.AddBayPoint=105031.909766, 1286.14872485, 22922.2
#pers.AddBayPoint=117644.506581, 3510.77882759, 25430.09
#pers.AddBayPoint=118675.763957, 3933.1493805, 28807.6
#pers.AddBayPoint=110154.610648, 2667.88024547, 29037.58


minopuen=darfuncs.E_Grup()
minopuen.OnDeath =finGrupominorxo
minopuen.AddGuy("3MINOT")
minopuen.AddGuy("2MINOT")
minopuen.AddGuy("5DKGT")
minopuen.AddGuy("6DKGT")



GrupoMin1=darfuncs.E_Grup()
GrupoMin1.OnDeath =finGrupoMin1
GrupoMin1.AddGuy("2MINOT")
GrupoMin1.AddGuy("3MINOT")

	
	
darfuncs. EnterSecEvent(83189.2, -62.7, 20344.8,MINORXO)

darfuncs. EnterSecEvent(71087.6, -64.6, 23361.9,CierraPuerta11)