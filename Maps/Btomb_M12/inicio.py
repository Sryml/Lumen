import Sounds
import GameText
import Sparks
import Scorer
import AuxFuncs

char = Bladex.GetEntity("Player1")

AuxFuncs.SingleFrameFade()
Scorer.SetVisible(0)


rastrini=Bladex.CreateEntity("Rastrini","Rastrillo",325911.547685,-5833.950796,-227201.584969)
rastrini.Static=1
rastrini.Scale=1.000000
rastrini.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Rastrini")

rastrinidin=Objects.CreateDinamicObject("Rastrini")


sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

Bladex.AddScheduledFunc(Bladex.GetTime(),IniciaJuego,())
#Bladex.AddScheduledFunc(Bladex.GetTime()+2,IniciaJuego,())