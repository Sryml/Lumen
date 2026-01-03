import EnemyTypes
import AniSound
import Sounds
import EnmGenRnd
import Scorer


pers=Bladex.CreateEntity("1lagarto","Salamander",-23000,-40000,9000)
pers.Person=1
pers.Angle=4.64

#pers.ActionAreaMin=pow(2,0)
#pers.ActionAreaMax=pow(2,0)
EnemyTypes.EnemyDefaultFuncs(pers)
#AniSound.AsignarSonidosSalamander('1lagarto')
pers.SetOnFloor()