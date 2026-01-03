import Levers
import InitDataField

MESSAGE_START_WEAPON         =7
MESSAGE_STOP_WEAPON          =8

Sonido_TrampaCuchilla_Activada = Bladex.CreateSound('../../Sounds/trap-clicked.wav', 'TrampaCuchillaActivacion')
Sonido_TrampaCuchilla_Activada.Volume=1
Sonido_TrampaCuchilla_Activada.MinDistance=10000
Sonido_TrampaCuchilla_Activada.MaxDistance=20000

Sonido_Cuchilla1_Activada = Bladex.CreateSound('../../Sounds/spike-trap1.wav', 'CuchillaActivacion')
Sonido_Cuchilla1_Activada.Volume=1
Sonido_Cuchilla1_Activada.MinDistance=10000
Sonido_Cuchilla1_Activada.MaxDistance=20000

Sonido_Cuchilla2_Activada = Bladex.CreateSound('../../Sounds/spike-trap1.wav', 'CuchillaActivacion')
Sonido_Cuchilla2_Activada.Volume=1
Sonido_Cuchilla2_Activada.MinDistance=10000
Sonido_Cuchilla2_Activada.MaxDistance=20000

Sonido_Cuchilla1_Recogida = Bladex.CreateSound('../../Sounds/mechanism-operated.wav', 'SonidoRecogida')
Sonido_Cuchilla1_Recogida.Volume=1
Sonido_Cuchilla1_Recogida.MinDistance=10000
Sonido_Cuchilla1_Recogida.MaxDistance=20000

Sonido_Cuchilla2_Recogida = Bladex.CreateSound('../../Sounds/mechanism-operated.wav', 'SonidoRecogida')
Sonido_Cuchilla2_Recogida.Volume=1
Sonido_Cuchilla2_Recogida.MinDistance=10000
Sonido_Cuchilla2_Recogida.MaxDistance=20000

Sonido_TrampaCuchilla_Reactivada = Bladex.CreateSound('../../Sounds/metal-lever1.wav', 'TrampaCuchillaReactivacion')
Sonido_TrampaCuchilla_Reactivada.Volume=1
Sonido_TrampaCuchilla_Reactivada.MinDistance=10000
Sonido_TrampaCuchilla_Reactivada.MaxDistance=20000


lever=Levers.PlaceLever("Lever1",Levers.LeverType3,(-141827,-23140,-113373),(0,0,0.707,-0.707),1.0)

o=Bladex.CreateEntity("Blade1","CuchillaFernando",-138250,-23598,-105000)
o.Orientation=1.000000,0.000000,0.000000,0.000000
o.Scale=0.8
o.Weapon=1
InitDataField.Initialise(o)
o.Data.NoFXOnHit=1


o=Bladex.CreateEntity("Blade2","CuchillaFernando",-145250,-23124,-105000)
o.Orientation=1.000000,0.000000,0.000000,0.000000
o.Scale=0.8
o.Weapon=1
InitDataField.Initialise(o)
o.Data.NoFXOnHit=1



#char=Bladex.GetEntity("Player1")
#char.Position=-141500,-23500,-92500

blades_ready=1

Bladex.CreateTimer("Timer60",1.0/60.0)

b1_time=0.0



Bladex.AddParticleGType("Spark","GenericParticle",B_PARTICLE_GTYPE_BLEND,8)

for i in range(8):
	if (i>4):
		aux=0.0
	else:
		aux=(4.0-i)/4.0
	r=255
	g=140
	b=0
	a=255*(1.0-aux)
	size=3.0*(1.0-aux)
	Bladex.SetParticleGVal("Spark",i,r,g,b,a,size)



b2_time=0.0



lever.OnTurnOnFunc=RBlades
lever.OnTurnOnArgs=()

#######################################################################
#######################################################################
##########
##########

slab=Bladex.CreateEntity("Slab","Entity Sliding Area",-141750,-23000,-99000)
slab.SlidingSurface=0,-1,0
slab.Displacement=100

slab_s=Bladex.GetSector(-141750,-23000,-99000)
slab_s.OnEnter=ActivateBlades
slab.SlideTo(0,-200,0)
