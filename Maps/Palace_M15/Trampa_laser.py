import darfuncs
import Bladex
import AbreCam
import dust
import Doors
import AuxFuncs

_SndTunderRay=Bladex.CreateSound("../../Sounds/M-IMPACTO-FUEGO.wav","SndTunderRay")
_SndTunderRay.MinDistance=100000.0
_SndTunderRay.MaxDistance=1000000.0

_SoundClank=Bladex.CreateSound("../../Sounds/metal-lever3.wav","SoundClank")
_SoundClank.MinDistance=10000
_SoundClank.MaxDistance=100000


_Soundbrum=Bladex.CreateSound("../../Sounds/M-GENERADOR-ENTIERRA3.wav","Soundbrum")
_Soundbrum.MinDistance=10000
_Soundbrum.MaxDistance=100000

_SoundMaderazo=Bladex.CreateSound("../../Sounds/golpe-madera-mediana.wav","SoundMaderazo")
_SoundMaderazo.MinDistance=2000
_SoundMaderazo.MaxDistance=10000

_SoundTemblorFatidico=Bladex.CreateSound("../../Sounds/piedra-rodando-1.wav","SoundTemblorFatidico")
_SoundTemblorFatidico.MinDistance=20000
_SoundTemblorFatidico.MaxDistance=10000
_SoundTemblorFatidico.Volume = 1

_SoundGolpeFatidico=Bladex.CreateSound("../../Sounds/golpe-piedra-pesada.wav","SoundGolpeFatidico")
_SoundGolpeFatidico.MinDistance=20000
_SoundGolpeFatidico.MaxDistance=10000
_SoundGolpeFatidico.Volume = 1





DerruP=Bladex.CreateEntity("DerruP","AdoquinRuna",-62362.797000,907.151000,171557.770000)
DerruP.Scale=3.538461
DerruP.Orientation=0.707107,0.707107,0.000000,0.000000


AbreP=Bladex.CreateEntity("AbreP","AdoquinRuna",-62390.398000,858.545000,178348.235000)
AbreP.Scale=3.366725
AbreP.Orientation=0.707107,0.707107,0.000000,0.000000

Rocas = [1,2,3,4]

Rocas[0]=Bladex.CreateEntity("Rocuna","Roca1Aurelio",-62064.615798,-7542.295549,171722.342797,"Physic")
Rocas[0].Scale=0.555954
Rocas[0].Orientation=0.444997,0.444997,0.549525,-0.549525


Rocas[1]=Bladex.CreateEntity("Rocola","Roca1Aurelio",-62072.942870,-7945.133762,173004.682252,"Physic")
Rocas[1].Scale=0.578528
Rocas[1].Orientation=0.579228,0.579228,0.405580,-0.405580

Rocas[2]=Bladex.CreateEntity("Rocallosa","Roca1Aurelio",-62503.122739,-6318.306086,173231.534831,"Physic")
Rocas[2].Scale=0.608039
Rocas[2].Orientation=0.564721,0.564721,0.425547,-0.425547


Rocas[3]=Bladex.CreateEntity("Rocoleta","Roca1Aurelio",-62502.348633,-6176.136741,171741.937986,"Physic")
Rocas[3].Scale=0.567129
Rocas[3].Orientation=0.632814,0.632814,0.315509,-0.315509

SexRock = Bladex.GetSector(-62502.348633,-6176.136741,171741.937986)
SexRock.Active = 0





vigas = [0,0,0,0]
vigas[0]=Bladex.CreateEntity("vigero","Vigaro1",-62474.185711,-807.715643,173008.876018,"Physic")
vigas[0].Scale=0.705914
vigas[0].Orientation=0.017452,0.999848,0.000000,0.000000


vigas[1]=Bladex.CreateEntity("viagra","Vigaro1",-62407.200051,-4618.740368,170922.262399,"Physic")
vigas[1].Scale=0.602019
vigas[1].Orientation=0.725374,0.688355,0.000000,0.000000


vigas[2]=Bladex.CreateEntity("vigar","Vigaro1",-62454.795150,-4670.367568,173038.706556,"Physic")
vigas[2].Scale=0.734577
vigas[2].Orientation=0.000000,0.000000,0.743145,-0.669131



vigas[3]=Bladex.CreateEntity("virga","Vigaro1",-62461.738035,-2883.471261,173169.234042,"Physic")
vigas[3].Scale=0.645445
vigas[3].Orientation=1,0.02,0,0


vigacaida = [0,1,2,3]

vigacaida[0]=Bladex.CreateEntity("vigacaida0","Vigaro1",-62464.186000,-157.716000,173428.876000)
vigacaida[0].Scale=0.705914
vigacaida[0].Orientation=0.061048,0.998135,0.000000,0.000000


vigacaida[1]=Bladex.CreateEntity("vigacaida1","Vigaro1",-62407.200000,-4618.740000,170422.262000)
vigacaida[1].Scale=0.602019
vigacaida[1].Orientation=0.981627,0.190810,0.000000,0.000000


vigacaida[2]=Bladex.CreateEntity("vigacaida2","Vigaro1",-62454.795000,-4670.368000,173948.707000)
vigacaida[2].Scale=0.734577
vigacaida[2].Orientation=0.000000,0.000000,0.970296,-0.241922



vigacaida[3]=Bladex.CreateEntity("vigacaida3","Vigaro1",-62418.245604,-340.800705,171670.859414)
vigacaida[3].Scale=0.584313
vigacaida[3].Orientation=0.704955,0.704602,-0.066385,0.046559

for v in vigacaida:
	v.RemoveFromWorld()



GemaUno=Bladex.CreateEntity("GemaUno","Gemaazul",-81470.779899,-10010.026057,174901.350868)
GemaUno.Scale=3.609585
GemaUno.Orientation=0.706999,0.012341,-0.012341,-0.706999
GemaUno.SelfIlum = -2



GemaDos=Bladex.CreateEntity("GemaDos","Gemaazul",-64087.309902,-6545.078031,174660.613283)
GemaDos.Scale=3.645680
GemaDos.Orientation=0.706999,0.012341,-0.012341,-0.706999
GemaDos.SelfIlum = -2

rayo = [0,1,2,3]

GEMAPOS = -64587.309902, -6545.078031, 174660.613283

rayo[0]=Bladex.CreateEntity("Rayo1", "Entity ElectricBolt",-64686.690098, -7444.921969, 173859.386717)
rayo[0].MaxAmplitude=400.0
rayo[0].MinSectorLength=250000.0
rayo[0].Active=0
rayo[0].Damage=0
rayo[0].Position =-64686.690098, -7444.921969, 173859.386717


rayo[1]=Bladex.CreateEntity("Rayo2", "Entity ElectricBolt",-64686.690098, -5844.921969, 173859.386717)
rayo[1].MaxAmplitude=400.0
rayo[1].MinSectorLength=250000.0
rayo[1].Active=0
rayo[1].Damage=0
rayo[1].Position = -64686.690098, -5844.921969, 173859.386717


rayo[2]=Bladex.CreateEntity("Rayo2", "Entity ElectricBolt",-64686.690098, -5844.921969, 175559.386717)
rayo[2].MaxAmplitude=400.0
rayo[2].MinSectorLength=250000.0
rayo[2].Active=0
rayo[2].Damage=0
rayo[2].Position = -64686.690098, -5844.921969, 175559.386717


rayo[3]=Bladex.CreateEntity("Rayo2", "Entity ElectricBolt",-64686.690098, -7444.921969, 175559.386717)
rayo[3].MaxAmplitude=400.0
rayo[3].MinSectorLength=250000.0
rayo[3].Active=0
rayo[3].Damage=0
rayo[3].Position = -64686.690098, -7444.921969, 175559.386717


rayo[0].Target  = GEMAPOS
rayo[1].Target  = GEMAPOS
rayo[2].Target  = GEMAPOS
rayo[3].Target  = GEMAPOS


rayoMalo=Bladex.CreateEntity("Rayo1", "Entity ElectricBolt",GEMAPOS[0],GEMAPOS[1],GEMAPOS[2])
rayoMalo.MaxAmplitude=400.0
rayoMalo.MinSectorLength=250000.0
rayoMalo.Active=0
rayoMalo.Damage=0
rayoMalo.Position =GEMAPOS


#######################PUERTA DE LA GEMA


puertaGEMA=Doors.CreateDoor("PuertaGEMA", (-81300,-10000,175000), (0,1,0), 0, 1750, Doors.CLOSED)

puertaGEMA.opentype=Doors.UNIF
puertaGEMA.o_med_vel=-1000
puertaGEMA.o_med_displ=1750

puertaGEMA.closetype=Doors.UNIF
puertaGEMA.c_med_vel=1000
puertaGEMA.c_med_displ=1750


#######################PUERTA DE LA cabeza


puertaCABEZA=Doors.CreateDoor("PuertaCABEZA", (-86400,-7000,175000), (0,1,0), 0, 3500, Doors.CLOSED)

puertaCABEZA.opentype=Doors.UNIF
puertaCABEZA.o_med_vel=-1000
puertaCABEZA.o_med_displ=3500

puertaCABEZA.closetype=Doors.UNIF
puertaCABEZA.c_med_vel=1000
puertaCABEZA.c_med_displ=3500

darfuncs.EnterSecEvent(-63124.1005114, -814.604598102, 178061.441262,AbrepuertaCABEZA)

EstadoPuertaGema = Doors.CLOSED



puertaGEMA.OnEndOpenFunc  = PuertaAbierta
puertaGEMA.OnEndCloseFunc = PuertaCerrada


GemoSec         = Bladex.GetSector(-61962.4560859, -793.892317899, 171923.63627)
GemoSec.OnEnter = PisaBotonGema
GemoSec.OnLeave = SueltaBotonGema


PartesRayuela = ("L_Hand","R_Hand","L_Foot","R_Foot","Head")


import whrandom


RayoMaloSec = Bladex.GetSector(-84644.7975458, -5555.057629, 175605.587055)
RayoMaloSec.OnEnter = RayoMaloMataAlIdiota

HitsLeft = 6

vigas[0].HitFunc = GolpeAlPilar