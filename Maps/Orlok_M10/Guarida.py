import Bladex
import AuxFuncs
import EnemyTypes
import Actions
import math
import ItemTypes
import Reference
import LevelFuncs

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 12
expected_player_lvl_max= 16

lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)



##################################################
##	Definicion de sistemas de particulas
##################################################

Bladex.AddParticleGType("PolvoRoca","SmokeParticle",B_PARTICLE_GTYPE_BLEND,120)

for i in range(120):
	if i>100:
		traux=1.0-(120.0-i)/20.0
	else:
		traux=(100.0-i)/100.0
	aux=(120.0-i)/120.0
	r=255
	g=230
	b=210
	a=80.0*(1.0-traux)**2.0
	size=800.0+aux*400.0
	Bladex.SetParticleGVal("PolvoRoca",i,r,g,b,a,size)


####################
##	Enemigos
####################

# Troll en la guarida del laberinto. Areas 19 y 20

arma=Bladex.CreateEntity("OrlokArmaTrollLab", "Hachacarnicero", 0.0, 0.0, 0.0, "Weapon")
ItemTypes.ItemDefaultFuncs(arma)
trolllab=Bladex.CreateEntity("OrlokTrollLab", "Troll_Dark", -23500.0, -34500.0, 90000.0, "Person")
trolllab.Angle=3.14159
trolllab.Level=lvl_control.GiveLevel(7,9)
Actions.TakeObject(trolllab.Name, arma.Name)
trolllab.ActionAreaMin=math.pow(2,18)
trolllab.ActionAreaMax=math.pow(2,19)
EnemyTypes.EnemyDefaultFuncs(trolllab)
trolllab.Blind=1
trolllab.Deaf=1
trolllab.SetOnFloor()


##################
##	Sonidos
##################

sonidoroturamurotroll=Bladex.CreateSound("../../Sounds/single-boulder-impact.wav", "SonidoRoturaMuroTroll")
sonidoroturamurotroll.Volume=1
sonidoroturamurotroll.MinDistance=6000
sonidoroturamurotroll.MaxDistance=25000

rugidoroturamurotroll=Bladex.CreateSound("../../Sounds/herida-troll1.wav", "RugidoRoturaMuroTroll")
rugidoroturamurotroll.Volume=1
rugidoroturamurotroll.MinDistance=8000
rugidoroturamurotroll.MaxDistance=30000


#####################
##	Sectores
#####################

murotroll=Bladex.GetSector(-23875.0, -34500.0, 87000.0)
murotroll.Active=0

murotrolli1=Bladex.GetSector(-25000.0, -34000.0, 87000.0)
murotrolli1.Active=0

murotrolli2=Bladex.GetSector(-25000.0, -36000.0, 87000.0)
murotrolli2.Active=0

murotrolld=Bladex.GetSector(-22750.0, -34500.0, 87000.0)
murotrolld.Active=0

murotroll.InitBreak((0.0, 0.0, 250.0), (-800.0, 200.0, 0.0), (300.0, 1000.0, 0.0), "", 100.0, 0)
murotrolli1.InitBreak((0.0, 0.0, 250.0), (-800.0, 0.0, 0.0), (0.0, 1000.0, 0.0), "", 100.0, 0)
murotrolli2.InitBreak((0.0, 0.0, 250.0), (-800.0, 0.0, 0.0), (0.0, 1000.0, 0.0), "", 100.0, 0)
murotrolld.InitBreak((0.0, 0.0, 250.0), (-800.0, 0.0, 0.0), (0.0, 1000.0, 0.0), "", 100.0, 0)

slanzatroll=Bladex.GetSector(-23750.0, -36000.0, 79000.0)


#####################
##	Objetos
#####################

cubotroll=Bladex.CreateEntity("CuboTroll","Bloque",-23728.000000,-34414.000000,85424.000000)
cubotroll.Scale=4.108044
cubotroll.Orientation=0.707107,-0.000000,-0.000000,0.707107
cubotroll.CastShadows=0
cubotroll.Alpha = 0.0
cubotroll.ExclusionMask=2|4
Reference.EntitiesSelectionData[cubotroll.Name]=(0,0,"")


###########################
##	Funcionamiento
###########################

######## Funcion: rep()

######## Funcion: DespiertaTroll(person)

######## Funcion: LanzaTroll(sec_idx, ent_name)

slanzatroll.OnEnter=LanzaTroll
