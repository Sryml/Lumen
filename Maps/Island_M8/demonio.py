import Bladex
import EnemyTypes
import AniSound
import PhantonFX


RugidoDemonio=Sounds.CreateEntitySound("../../Sounds/M-rugido-demon.wav", "RugidoDemonio")
RugidoDemonio.Volume=1
RugidoDemonio.MinDistance=10000
RugidoDemonio.MaxDistance=90000

FireBallCool=Sounds.CreateEntitySound("../../Sounds/fireball-swing.wav","Fireball")
FireBallCool.Volume=1
FireBallCool.MinDistance=10000
FireBallCool.MaxDistance=90000

Bladex.AddParticleGType("Energia3","GenericParticle",B_PARTICLE_GTYPE_ADD,80)

for i in range(80):
	if i>60:
		traux=1-((i-60.0)/20.0) #va de 0 a 1
	elif i<20:
		traux=i/20.0 #va de 1 a 0
	else:
		traux=1.0
	r=255
	g=80
	b=100
	a=255.0*traux
	size=20.0
	Bladex.SetParticleGVal("Energia3",i,r,g,b,a,size)


Bladex.AddParticleGType("Energia2","GenericParticle",B_PARTICLE_GTYPE_ADD,120)

for i in range(120):
	if i>90:
		traux=1-((i-90.0)/30.0) #va de 0 a 1
	elif i<20:
		traux=i/20.0 #va de 1 a 0
	else:
		traux=1.0
	r=100
	g=100
	b=255
	a=255.0*traux
	size=20.0
	Bladex.SetParticleGVal("Energia2",i,r,g,b,a,size)


Bladex.AddParticleGType("FuegoInvocacion","FireParticle",B_PARTICLE_GTYPE_ADD,120)


demoniox=Bladex.CreateEntity("demoniox","Little_Demon",0,0,0,"Person")
demoniox.Angle=3
demoniox.Level=5
AniSound.AsignarSonidosLittleDemon(demoniox.Name)
demoniox.Blind = 1
demoniox.Deaf  = 1
demoniox.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(demoniox)

demoniox.Freeze()
demoniox.Alpha = 0.0
demoniox.RemoveFromWorld()



ELDEMOSEC=Bladex.GetSector(-38413.9893755, -49119.1878554, 20782.3193118)
ELDEMOSEC.OnEnter = ElDemonio

# CoolDemon("demoniox")
# demoniox.SubscribeToList("Pin")
# char.Position = (-48749.3754276, -49118.6347739, 29820.3305089)
