import EnemyTypes
import AniSound
import Sounds
import EnmGenRnd
import Scorer



#SonidoWakeGolem.Position = -7500,-6000,9500


OldImDeadFunc = 0

Bladex.AddParticleGType("DustGolem","SmokeParticle",B_PARTICLE_GTYPE_BLEND,64)

for i in range(64):
	if i>32:
		traux=0.0
	else:
		traux=(32.0-i)/32.0
	aux=(64.0-i)/64.0
	r=190
	g=150
	b=160
	a=100.0*(1.0-traux)**0.5
	size=1.0+aux*450.0
	Bladex.SetParticleGVal("DustGolem",i,r,g,b,a,size)



pers=Bladex.CreateEntity("1GLM","Golem_stone",-3400,-6594,500,"Person")
pers.Angle=0
pers.Level=9
#pers.ActionAreaMin=pow(2,0)
#pers.ActionAreaMax=pow(2,0)
EnemyTypes.EnemyDefaultFuncs(pers)
#AniSound.AsignarSonidosTroll('1GLM')
pers.SetOnFloor()
OldImDeadFunc = pers.ImDeadFunc 
pers.ImDeadFunc = AbrirPuertaGlm1
pers.Blind = 1
pers.Deaf = 1
pers.Freeze()



gen_DalGurak=Bladex.CreateEntity("GenDalGurak", "DalGurak",-23000,-13291,7716,"Person")
gen_DalGurak.RemoveFromWorld()

Glm11ActSec = Bladex.GetSector(-19500,-9000,9500)
Glm11ActSec.OnEnter = WakeUpGlm11

DalGurakActSec = Bladex.GetSector(-3400,-7000,18875)
