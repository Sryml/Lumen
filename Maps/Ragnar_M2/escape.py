import Bladex
import darfuncs



#######################
#     Preparacion     #
#######################

#derrumbemurocelda=Bladex.CreateSound("../../Sounds/derrumbamiento roca.wav", "DerrumbeMuroCelda")
#derrumbemurocelda.Volume=1
#derrumbemurocelda.MinDistance=10000
#derrumbemurocelda.MaxDistance=20000

derrumbemurocelda=Bladex.CreateSound("../../Sounds/Stone-floor-collapse.wav", "DerrumbeMuroCelda")
derrumbemurocelda.Volume=1
derrumbemurocelda.MinDistance=5000
derrumbemurocelda.MaxDistance=40000

derrumbemuroagua=Bladex.CreateSound("../../Sounds/impact-watersplash.wav", "DerrumbeMuroAgua")
derrumbemuroagua.Volume=1
derrumbemuroagua.MinDistance=5000
derrumbemuroagua.MaxDistance=40000

punteromuro=Bladex.CreateEntity("PunteroMuro","GhostPointer", -109440.0, 7396.0, 85450.0)
punteromuro.Static=1
punteromuro.Scale=1.000000
punteromuro.Orientation=0.707107,0.707107,0.000000,0.000000
darfuncs.SetHint(punteromuro,"Loose Brick")

muroceldasup=Bladex.GetSector(-109500.0, 7000.0, 86000.0)
muroceldasup.Active=0

muroceldainf=Bladex.GetSector(-109500.0, 8000.0, 86000.0)
muroceldainf.Active=0

muroceldasup.InitBreak((0.0, 0.0, 300.0), (1230.0, 0.0, 0.0), (0.0, 730.0, 0.0))#, "piedra pesada", 1000000.0)
muroceldainf.InitBreak((0.0, 0.0, 300.0), (1230.0, 0.0, 0.0), (0.0, 730.0, 0.0))#, "piedra pesada", 1000000.0)

Bladex.AddParticleGType("WallDust","SmokeParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	if i>30:
		traux=0.0
	else:
		traux=((30.0-i)/30.0)**0.5
	aux=((60.0-i)/60.0)**0.5
	r=255
	g=230
	b=210
	a=60.0*(1.0-traux)
	size=7.0+aux*1000.0
	Bladex.SetParticleGVal("WallDust",i,r,g,b,a,size)


punteromuro.UseFunc=DerribaMuro
