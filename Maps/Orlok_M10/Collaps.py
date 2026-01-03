import Bladex
import AuxFuncs


MESSAGE_START_WEAPON=7
MESSAGE_STOP_WEAPON=8


###################
#     Sonidos     #
###################

derrumbesuelopiedra=Bladex.CreateSound("../../Sounds/Stone-floor-collapse.wav", "DerrumbeSueloPiedra")
derrumbesuelopiedra.Volume=1
derrumbesuelopiedra.MinDistance=5000
derrumbesuelopiedra.MaxDistance=40000


###################
#     Sonidos     #
###################

antsecr=Bladex.CreateEntity("AntSecreto","Antorchaenpared",-36193.664000,-38908.282000,87135.486000)
antsecr.Static=1
antsecr.Scale=1.000000
antsecr.Orientation=0.379928,0.379928,0.596368,-0.596368
antsecr.FiresIntensity=[ 3 ]
antsecr.Lights=[ (4.0,0.031250,(255,180,96)) ]

luzantsecr=AuxFuncs.GetSpot(antsecr)
luzantsecr.Intensity=0.0


####################################
#     Derrumbamiento del valle     #
####################################

dervalle=Bladex.GetSector(-65750.0, -34000.0, 3500.0)
dervalle.Active=0

dervalle.InitBreak((0.0, 500.0, 0.0), (1200.0, 0.0, 400.0), (300.0, 0.0, 900.0))

secdervalle2=Bladex.GetSector(-65750.0, -36000.0, 3500.0)
secdervalle1=Bladex.GetSector(-68750.0, -36000.0, 3500.0)

######## Funcion: ContDerValle()

######## Funcion: DerValle(sector_index, entity_name)

secdervalle2.OnWalkOn=DerValle
secdervalle1.OnWalkOn=DerValle



########################
#     Muros falsos     #
########################


### Sonidos

sonidoroturamurofalso=Bladex.CreateSound("../../Sounds/single-boulder-impact.wav", "SonidoRoturaMuroFalso")
sonidoroturamurofalso.Volume=1
sonidoroturamurofalso.MinDistance=4000
sonidoroturamurofalso.MaxDistance=20000


### Muro falso del laberinto

secmurofalsolab=Bladex.GetSector(-38625.0, -37000.0, 85220.0)
secmurofalsolab.Active=0

secmurofalsolab.InitBreak((180.0, 0.0, 180.0), (200.0, 700.0, -200.0), (500.0, 100.0, -500.0))

secrompemurofalsolab=Bladex.GetSector(-38500.0, -37000.0, 84906.0)
secrompemurofalsolab.ActiveSurface=-0.707107, 0.0, -0.707107

######## Funcion: RompeMuroFalsoLab(sector_index, entity_name, px, py, pz,ximpulse=0,yimpulse=0,zimpulse=0,x_norm=0,y_norm=0,z_norm=0,material="")

secrompemurofalsolab.OnHit=RompeMuroFalsoLab



##############################################
#     Derrumbamiento en la fortificacion     #
##############################################

derfort=Bladex.GetSector(41250.0, -41125.0, 73750.0)
derfort.Active=0

derfort.InitBreak((0.0, 125.0, 0.0), (0.0, 0.0, -1600.0), (300.0, 0.0, 0.0), "", 100.0, 0)

secderfort=Bladex.GetSector(41250.0, -42500.0, 73750.0)

######## Funcion: ContDerFort()

######## Funcion: DerFort(sector_index, entity_name)

secderfort.OnWalkOn=DerFort
