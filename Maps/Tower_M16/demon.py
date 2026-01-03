import EnmGenRnd
import GameText
import Bladex
import Scorer
import Levers
import Sounds
import Damage
import Doors
import Reference
import dust



SoundScreamDemon = Sounds.CreateEntitySound('../../Sounds/M-rugido-demon.wav', 'SoundScreamDemon')
SoundScreamDemon.Volume=1.0
SoundScreamDemon.MinDistance=30000
SoundScreamDemon.MaxDistance=80000


######################################
###	TRAMPILLA GRAN DEMONIO	######
######################################

Dpta1d=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DaderaDesliz")
Dpta1d.MaxDistance=70000
Dpta1d.MinDistance=20000
Dpta1d.Volume=1.0


Dpta1g=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "DaderaGolpe")
Dpta1g.MaxDistance=70000
Dpta1g.MinDistance=20000
Dpta1g.Volume=1.0

#lado trampilla1
escalon1a=Doors.CreateDoor("TrampillaElevador1a", (0,-88800,11000), (0,0,-1), 0, 3250, Doors.CLOSED)

escalon1a.opentype=Doors.UNIF
escalon1a.o_med_vel=-1500
escalon1a.o_med_displ=3250

escalon1a.closetype=Doors.UNIF
escalon1a.c_med_vel=10000
escalon1a.c_med_displ=3250

escalon1a.SetWhileOpenSound(Dpta1d)
escalon1a.SetEndOpenSound(Dpta1g)

#lado trampilla2
escalon2a=Doors.CreateDoor("TrampillaElevador2a", (0,-88800,8000), (0,0,1), 0, 3250, Doors.CLOSED)

escalon2a.opentype=Doors.UNIF
escalon2a.o_med_vel=-1500
escalon2a.o_med_displ=3250

escalon2a.closetype=Doors.UNIF
escalon2a.c_med_vel=10000
escalon2a.c_med_displ=3250


#plataforma sube

Fpta1d=Sounds.CreateEntitySound("../../Sounds/lava-flow.wav", "FaderaDesliz")
Fpta1d.MaxDistance=80000
Fpta1d.MinDistance=20000
Fpta1d.Volume=1.0


Fpta1g=Sounds.CreateEntitySound("../../Sounds/fireball-impact.wav", "FaderaGolpe")
Fpta1g.MaxDistance=80000
Fpta1g.MinDistance=20000
Fpta1g.Volume=1.0

escalon3a=Doors.CreateDoor("ElevadorDemonio", (0,-80000,9000), (0,-1,0), 0, 10500, Doors.OPENED)

escalon3a.opentype=Doors.UNIF
escalon3a.o_med_vel=-700
escalon3a.o_med_displ=10500

escalon3a.closetype=Doors.UNIF
escalon3a.c_med_vel=2100
escalon3a.c_med_displ=10500


escalon3a.SetWhileCloseSound(Fpta1d)
escalon3a.SetEndCloseSound(Fpta1g)

#funci�n que abre la trampilla y sube la plataforma


######################################
### PUERTAS SALA GRAN DEMONIO
######################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


#pta 1D
pta1D=Doors.CreateDoor("Escalon1D", (-20650,-92000,13000), (0,1,0), 500, 5500, Doors.OPENED)

pta1D.opentype=Doors.UNIF
pta1D.o_med_vel=-1000
pta1D.o_med_displ=5000

pta1D.closetype=Doors.UNIF
pta1D.c_med_vel=5000
pta1D.c_med_displ=5000


#pta 2D
pta2D=Doors.CreateDoor("Escalon2D", (-20650,-92000,5000), (0,1,0), 500, 5500, Doors.OPENED)

pta2D.opentype=Doors.UNIF
pta2D.o_med_vel=-1000
pta2D.o_med_displ=5000

pta2D.closetype=Doors.UNIF
pta2D.c_med_vel=5000
pta2D.c_med_displ=5000

pta1D.SetWhileOpenSound(maderadesliz)
pta1D.SetEndOpenSound(maderagolpe)

pta1D.SetWhileCloseSound(maderadesliz)
pta1D.SetEndCloseSound(maderagolpe)




gen_DalGurakGDM = Bladex.CreateEntity("GenDalGurakGDM", "DalGurak",3629, -90539, 9113,"Person")
gen_GDM = EnmGenRnd.CreateEnemy((1300, -78412, 9128),"GenGDM", "Great_Demon", "", 0, "", 0)
demondetector =  darfuncs.E_Grup()
demondetector.AddGuy(gen_GDM.Name)
demondetector.OnDeath = AbrePuerta2OnDie

#ActDemonSec = Bladex.GetSector(-25053,-88000,15642)
ActDemonSec = Bladex.GetSector(-23232, -88050,16564 )
ActDemonSec.OnEnter = StartSceneDemonio

demonlight=Bladex.CreateEntity("demonlight","Entity Spot",-2200.0, -85500.0, 9100.0)
demonlight.Color=230,74,0
demonlight.Intensity=60
demonlight.Precission=0.3
demonlight.Visible=0
demonlight.CastShadows=1
demonlight.Flick=0
