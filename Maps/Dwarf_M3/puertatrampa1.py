import Doors
import Levers
import Locks
import Objects
import Sounds
import Sparks
import AbreCam

############################################################
####------------------------------------------------------------------------------#####
####------PUERTA-PALANCA---SALA-SUBTERRANEOS----------------#####
############################################################
############################################################


sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/gate-madera-planchas111.wav", "SonidoRastrillo")
#sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
sonidorastrillo.MaxDistance=25000
sonidorastrillo.MinDistance=5000
sonidorastrillo.Volume=1.0

golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-pesado.wav", "GolpeMetalMediano")
golpemetalmediano.MaxDistance=25000
golpemetalmediano.MinDistance=5000
golpemetalmediano.Volume=1.0


o=Bladex.CreateEntity("barra1","BarroteAurelio",-154250,-1125,-65000)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000




o=Bladex.CreateEntity("barra2","BarroteAurelio",-154250,-2125,-65000)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000




o=Bladex.CreateEntity("barra3","BarroteAurelio",-154250,-3125,-65000)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



o=Bladex.CreateEntity("barra4","BarroteAurelio",-154250,-4125,-65000)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



###los otros		(1500,0,0)

o=Bladex.CreateEntity("barra5","BarroteAurelio",-154750,-625,-64800)
o.Scale=1.000000
o.Orientation=0.000000,0.000000,0.707107,-0.707107
barra5din=Objects.CreateDinamicObject("barra5")


o=Bladex.CreateEntity("barra6","BarroteAurelio",-154750,-1625,-64800)
o.Scale=1.000000
o.Orientation=0.000000,0.000000,0.707107,-0.707107




o=Bladex.CreateEntity("barra7","BarroteAurelio",-154750,-2625,-64800)
o.Scale=1.000000
o.Orientation=0.000000,0.000000,0.707107,-0.707107




o=Bladex.CreateEntity("barra8","BarroteAurelio",-154750,-3625,-64800)
o.Scale=1.000000
o.Orientation=0.000000,0.000000,0.707107,-0.707107




palancabarras=Levers.PlaceLever("Palancabarras", Levers.LeverType3, (-159856.5,-8318.7,-68120.2), (0.687569,0.687569,-0.165071,0.165071), 1.0)
palancabarras.mode=2

palancabarras.OnTurnOnFunc=Abrebarras
palancabarras.OnTurnOnArgs=()
