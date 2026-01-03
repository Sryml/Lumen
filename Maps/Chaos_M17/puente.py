from math import pow
import Bladex
import Ontake
import AniSound
import Sparks
import Actions
import pocimac
import Breakings
import Sounds
import Locks
import Objects
import Stars
import darfuncs
import EnemyTypes
import Actions
import PhantonFX






##########################################################
#                     Golen' de verda'                  �#
##########################################################


Inicio1 = darfuncs.E_Grup()
Inicio1.OnDeath = AbrePuertagolem

Sisepasa= darfuncs.E_Grup()

#darfuncs.EnterSecEvent(320781, 41777, -70862,Suenaotra)

#1

pers=Bladex.CreateEntity("Golem1","Golem_metal",370335.687481,30426.025422,-42695.944976,"Person")
pers.Level=10
pers.Angle=6.20514607103
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

Inicio1.AddGuy(pers.Name)
#Sisepasa.AddGuy(pers.Name)


pers=Bladex.CreateEntity("Golem2","Golem_metal",370262.041632,30420.641208,-37602.686308,"Person")
pers.Level=2
pers.Angle=3.10955538774
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

Inicio1.AddGuy(pers.Name)

#Sisepasa.AddGuy(pers.Name)

Inicio1.HideBadGuys()




##Rastrillo secreto

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GoLpeMetalMediano")


rastsec=Bladex.CreateEntity("Rastsec","Rastrillo",378741.652902,45419.186689,-78391.814458,"Physic")
rastsec.Scale=1.138093
rastsec.Orientation=0.500000,0.500000,0.500000,-0.500000
rastsec.CastShadows=0
Sparks.SetMetalSparkling("Rastsec")


rastsecdin=Objects.CreateDinamicObject("Rastsec")



###cerradura y llave del rastrillo anterior


cerraduraz=Locks.PlaceLock("cerraduraz","Cerraduracutre",(377779.070584,47441.952223,-80489.016839),(0.504344,0.504344,-0.495618,0.495618),2.573538)
cerraduraz.key="Llavez"
darfuncs.SetHint(cerraduraz.obj,"Golems Lock")

cerraduraz.OnUnLockFunc=Abrerastsec
cerraduraz.OnUnLockArgs=()


llavez=Bladex.CreateEntity("Llavez","Llavecutre",370067.482989,31087.943364,-40175.646477,"Physic")
llavez.Scale=1.374941
llavez.Solid=0
llavez.Orientation=0.016803,-0.993765,0.008489,0.109891
darfuncs.SetHint(llavez,"Golems Key")
Stars.Twinkle("Llavez")


Ontake.AddOnTakeEvent("Llavez", CreaGolemsPuente)

obpega()
