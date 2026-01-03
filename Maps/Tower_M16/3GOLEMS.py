import EnmGenRnd
import AuxFuncs
import PhantonFX
import darfuncs

SonidoWakeGolem1 = Sounds.CreateEntitySound('../../Sounds/golem-despierta.wav', 'SoundWakeGolem')
SonidoWakeGolem1.Volume=1.0
SonidoWakeGolem1.MinDistance=10000
SonidoWakeGolem1.MaxDistance=20000

SonidoWakeGolem2 = Sounds.CreateEntitySound('../../Sounds/golem-despierta.wav', 'SoundWakeGolem')
SonidoWakeGolem2.Volume=1.0
SonidoWakeGolem2.MinDistance=10000
SonidoWakeGolem2.MaxDistance=20000

METHALIKA = darfuncs.E_Grup()
METHALIKA.OnDeath = GolemDeath

EnmGlm1 = EnmGenRnd.CreateEnemy((-16250,-25797,15000),"EnmGlm1", "Golem_metal", "", 0, "", 0)
EnmGlm1.Position = EnmGlm1.Data.Position
EnmGlm1.Angle=4.64
EnmGlm1.Level = 6
EnmGlm1.Alpha = 0
EnmGlm1.SetOnFloor()
EnmGlm1.PutToWorld()
EnemyTypes.EnemyDefaultFuncs(EnmGlm1)
METHALIKA.AddGuy(EnmGlm1.Name)

darfuncs.HideBadGuy(EnmGlm1.Name)

EnmGlm2 = EnmGenRnd.CreateEnemy((-16250,-25797,5000),"EnmGlm2", "Golem_metal", "", 0, "", 0)
EnmGlm2.Position = EnmGlm2.Data.Position
EnmGlm2.Angle=4.64
EnmGlm2.Level = 6
EnmGlm2.SetOnFloor()
EnmGlm2.PutToWorld()
EnmGlm2.Alpha = 0
EnemyTypes.EnemyDefaultFuncs(EnmGlm2)
darfuncs.HideBadGuy(EnmGlm2.Name)
METHALIKA.AddGuy(EnmGlm2.Name)

SonidoWakeGolem1.Position = EnmGlm1.Position
SonidoWakeGolem2.Position = EnmGlm2.Position



#GolemSec = Bladex.GetSector(-11000,-26000,10000)
GolemSec = Bladex.GetSector(-3565.0, -25287.3, 8833.8)
GolemSec.OnEnter = StartGolem3

#char.Position = -7059, -25303, 10222
