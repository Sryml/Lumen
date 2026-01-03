import Bladex
import EnemyTypes

o=Bladex.CreateEntity("OrcGladius3Achalay","Orksword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)
o=Bladex.CreateEntity("OrcEscudo3Achalay","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(o)

pers=Bladex.CreateEntity("3ORCAchalay","Great_Ork",19684, 48932, -9439,"Person")
Actions.TakeObject(pers.Name,"OrcGladius3Achalay")
Actions.TakeObject(pers.Name,"OrcEscudo3Achalay")
EnemyTypes.EnemyDefaultFuncs(pers)
pers.Angle = 1
pers.Blind = 1
pers.Deaf  = 1
pers.SetOnFloor()


s1=Bladex.GetSector(-2905, 48158, -1234)
s1.OnEnter=OrcHuye