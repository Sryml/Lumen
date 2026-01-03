import EnemyTypes
import AniSound
import Sounds
import EnmGenRnd
import Scorer
import ItemTypes
import Sparks



######################
#     Particulas     #
######################



CreateArenilla()


Bladex.AddParticleGType("Tierra3","GenericParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	aux=(60-i)/60
	r=40
	g=30
	b=0
	a=255*(1.0-aux/2.0)
	size=60.0*(1.0-aux)
	Bladex.SetParticleGVal("Tierra3",i,r,g,b,a,size)


###################################################
#     Funciones complementarias del generador     #
###################################################

DalPosition = ((-29500,-115000,9500),(-24500,-115000,12500),(-24500,-115000,5500))
NDalPositions = 3

generadorDlGk = EnmGenRnd.CreateEnemiesGenerator(6, 2)
#generadorDlGk.Level = 15

generadorDlGk.AddPoint((-18000,-110200,18000),("DlGk1", "Skeleton", "Espadacurva", 0, "VampShield", 1), "Skl_appears1",14)
generadorDlGk.AddPoint((-20000,-110200,20000),("DlGk2", "Skeleton", "EgyptSword", 0, "VampShield", 1), "Skl_appears1",15)
generadorDlGk.AddPoint((-23000,-110200,-1500),("DlGk3", "Skeleton", "Hacha6", 0, "VampShield", 1), "Skl_appears1",16)
generadorDlGk.AddPoint((-21000,-110200,-3000),("DlGk4", "Skeleton", "Maza3", 0, "VampShield", 1), "Skl_appears1",17)
generadorDlGk.AddPoint((-22500,-110200, 9000),("DlGk5", "Skeleton", "Espadafilo", 0, "VampShield", 1), "Skl_appears1",18)
generadorDlGk.AddPoint((-18000,-110200, 8000),("DlGk5", "Skeleton", "Espadafilo", 0, "VampShield", 1), "Skl_appears1",19)

generadorDlGk.InitGenFunc=SaltaTierraGen
generadorDlGk.DifTime = 3.0
generadorDlGk.VirGenPos = -32794,-118018,8916
generadorDlGk.FinishGenFunc = ReapearDalGurak3
generadorDlGk.Activate()
		
gen_DalGurak3 = EnmGenRnd.CreateEnemy((-25000, -116000, 9000),"GenDalGurak3", "DalGurak", "", 0, "", 0, 9)

GurakAparicion3Sec = Bladex.GetSector(4750,-113000,9250)
GurakAparicion3Sec.OnLeave = StartSceneGurak3

gen_DalGurak3.Data.VeryOldImDeadFunc = gen_DalGurak3.ImDeadFunc
gen_DalGurak3.ImDeadFunc = MuereDalGurak

gen_DalGurak3.Data.positionlist.append([-21967, -112384, 23536, 0])
gen_DalGurak3.Data.positionlist.append([-15479, -112407, 24079, 0])
gen_DalGurak3.Data.positionlist.append([-10118, -112392, 8941, 0])
gen_DalGurak3.Data.positionlist.append([-15377, -112387, -4779, 0])
gen_DalGurak3.Data.positionlist.append([-21813, -112388, -5216, 0])
gen_DalGurak3.Data.positionlist.append([-32521, -112919, 9144, 0])

dalinv= gen_DalGurak3.GetInventory()

gen_DalGurak3.Data.Dalweapon=Bladex.CreateEntity("DalWeapon", "DalWeapon", 0,0,0, "Weapon")
ItemTypes.ItemDefaultFuncs(gen_DalGurak3.Data.Dalweapon)
dalinv.AddWeapon(gen_DalGurak3.Data.Dalweapon.Name)

gen_DalGurak3.Data.Dalshield=Bladex.CreateEntity("DalShield","DalShield",0,0,0, "Weapon")
Sparks.MakeShield(gen_DalGurak3.Data.Dalshield.Name)
dalinv.AddShield(gen_DalGurak3.Data.Dalshield.Name)

dalmagicshield= ItemTypes.MakeMagicShield("DalMagicShield", gen_DalGurak3)
