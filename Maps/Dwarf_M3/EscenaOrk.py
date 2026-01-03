import def_class
import Bladex
import Actions
import EnemyTypes
import Enm_Def
import copy
import Combat
import AuxTran
import Scorer
import Breakings



##################### Creando Orco 1 Escena de Lucha ##################################

Ork1 = Bladex.CreateEntity("OrkFight1","Ork",-72750,-12000,-11250,"Person")
Ork1.SetOnFloor()
weapon=Bladex.CreateEntity("WeaponOrk1","Hacha" , 0.0, 0.0, 0.0,"Weapon")
Actions.TakeObject(Ork1.Name, weapon.Name)
EnemyTypes.EnemyDefaultFuncs(Ork1)
#Ork1.Life = 3200



##################### Creando Enano 1 Escena de Lucha ##################################

Dwf1 = Bladex.CreateEntity("DwfFight1","Enano1",-67000,-12000,-14000,"Person")
Dwf1.SetOnFloor()
weapon=Bladex.CreateEntity("WeaponDwf1","Hacha" , 0.0, 0.0, 0.0,"Physic")
Breakings.SetBreakable("WeaponDwf1")
Actions.TakeObject(Dwf1.Name, weapon.Name)
Dwf1.Data = def_class.Enano(Dwf1)
Dwf1.Life = 200
Dwf1.ImDeadFunc = DwarfMuerto1


##################### Creando Orco 1 Escena 2 de Lucha ##################################

Ork3 = Bladex.CreateEntity("OrkFight3","Ork",-55500,-12000,-11500,"Person")
Ork3.SetOnFloor()
weapon=Bladex.CreateEntity("WeaponOrk3","Hacha" , 0.0, 0.0, 0.0,"Weapon")
Actions.TakeObject(Ork3.Name, weapon.Name)
EnemyTypes.EnemyDefaultFuncs(Ork3)
#Ork3.Life = 3200



##################### Creando Enano 1 Escena 2 de Lucha ##################################

Dwf2 = Bladex.CreateEntity("DwfFight2","Enano2",-52000,-12000,-8700,"Person")
Dwf2.SetOnFloor()
weapon=Bladex.CreateEntity("WeaponDwf2","Hacha" , 0.0, 0.0, 0.0,"Physic")
Breakings.SetBreakable("WeaponDwf2")
Actions.TakeObject(Dwf2.Name, weapon.Name)
Dwf2.Data = def_class.Enano(Dwf2)
Dwf2.Life = 600
Dwf2.ImDeadFunc = DwarfMuerto2


EscenaFight = 0


FightSector = Bladex.GetSector(-48004, -9934, -39162)
FightSector.OnEnter = StartAtack

EraseSec1 = Bladex.GetSector(-54354, -8834, -72805)
EraseSec1.OnEnter = EraseFightOrk
EraseSec2 = Bladex.GetSector(-55930, -9288, -59316)
EraseSec2.OnEnter = EraseFightOrk


