import Bladex
import Reference
import Sounds
import stone
import heavyObjects

bola_activada = 0
puente_break = 1

SonidoDerrumbamiento = Sounds.CreateEntitySound('../../Sounds/Wooden-bridge-collapse.wav', 'SonidoDerrumbamiento')
SonidoDerrumbamiento.Volume=1.0
SonidoDerrumbamiento.MinDistance=15000
SonidoDerrumbamiento.MaxDistance=45000

#------bola1-------
p=5339.892785,-48577.644223,150222.464860
r=0.707107,0.707107,0.000000,0.000000
o=heavyObjects.CreateHeavyObject("bola1","BoladePiedra",p,r,1.0, heavyObjects.StoneHitEvent )
fuerza_bola1 = -8000 * o.Mass
stone.lock( "bola1", stone.DROPDARKDUST, 0, 1000, 0.0, 0.6, 20.0, stone.STONESOUND, 0.1 )

#------bola2-------
#p=27900.610000,-58293.155000,126374.981000
p=28037.319385,-58382.182330,124433.390732
r=0.707107,0.707107,0.000000,0.000000
o=heavyObjects.CreateHeavyObject("bola2","BoladePiedra",p,r,1.0, heavyObjects.StoneHitEvent )
fuerza_bola2 = 4000 * o.Mass
stone.lock( "bola2", stone.DROPDARKDUST, 0, 1000, 0.0, 0.6, 20.0, stone.STONESOUND, 0.1 )

# ---- inicializacion de la rotura del puente

sderp1=Bladex.GetSector(-28750,-30700,170000) ; sderp1.Active=0
sderp2=Bladex.GetSector(-26250,-30700,170000) ; sderp2.Active=0
sderp3=Bladex.GetSector(-27250,-30700,175000) ; sderp3.Active=0

sderp1.InitBreak((0.0, 300.0, 0.0), (3000.0, 0.0, 0.0), (0.0, 0.0, 8000.0)) #, "piedra pesada", 1000000.0)
sderp2.InitBreak((0.0, 300.0, 0.0), (3000.0, 0.0, 0.0), (0.0, 0.0, 8000.0)) #, "piedra pesada", 1000000.0)
sderp3.InitBreak((0.0, 300.0, 0.0), (3000.0, 0.0, 0.0), (0.0, 0.0, 8000.0)) #, "piedra pesada", 1000000.0)


# ---- sectores de activacion de la rotura del puente y del desprendimiento de las 2 bolas

puente=Bladex.GetSector(-27000,-32000,168500)  ; puente.OnEnter=RomperPuente
sbol1 =Bladex.GetSector(-14500,-45000,156500)  ; sbol1.OnEnter=ActivarBola1
sbol2 =Bladex.GetSector(25000,-48500,142000)   ; sbol2.OnEnter=ActivarBola2
