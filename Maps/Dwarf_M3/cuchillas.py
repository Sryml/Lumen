import Sounds
import InitDataField

MESSAGE_START_WEAPON         =7
MESSAGE_STOP_WEAPON          =8

Sonido_TrampaCuchilla_Activada = Bladex.CreateSound('../../Sounds/trap-clicked.wav', 'TrampaCuchillaActivacion')
Sonido_TrampaCuchilla_Activada.Volume=1
Sonido_TrampaCuchilla_Activada.MinDistance=25000
Sonido_TrampaCuchilla_Activada.MaxDistance=40000



Sonido_Cuchilla_Inicio=Sounds.CreateEntitySound('../../Sounds/disco-empiez.wav', 'CuchillaActivacion')
Sonido_Cuchilla_Inicio.Volume=1.0
Sonido_Cuchilla_Inicio.MinDistance=4000
Sonido_Cuchilla_Inicio.MaxDistance=400000

Sonido_Cuchilla_Bucle=Sounds.CreateEntitySound('../../Sounds/disco-empiez1.wav', 'CuchillaCorta')
Sonido_Cuchilla_Bucle.Volume=1.0
Sonido_Cuchilla_Bucle.MinDistance=4000
Sonido_Cuchilla_Bucle.MaxDistance=400000

Sonido_Cuchilla_Fin=Sounds.CreateEntitySound('../../Sounds/disco-parada.wav', 'CuchillaSeLaCome')
Sonido_Cuchilla_Fin.Volume=1.0
Sonido_Cuchilla_Fin.MinDistance=4000
Sonido_Cuchilla_Fin.MaxDistance=400000

###########################################################################################################

Sonido_Cuchilla_Inicio1=Sounds.CreateEntitySound('../../Sounds/disco-empiez.wav', 'CuchillaActivacion')
Sonido_Cuchilla_Inicio1.Volume=1.0
Sonido_Cuchilla_Inicio1.MinDistance=4000
Sonido_Cuchilla_Inicio1.MaxDistance=400000

Sonido_Cuchilla_Bucle1=Sounds.CreateEntitySound('../../Sounds/disco-empiez1.wav', 'CuchillaCorta')
Sonido_Cuchilla_Bucle1.Volume=1.0
Sonido_Cuchilla_Bucle1.MinDistance=4000
Sonido_Cuchilla_Bucle1.MaxDistance=400000

Sonido_Cuchilla_Fin1=Sounds.CreateEntitySound('../../Sounds/disco-parada.wav', 'CuchillaSeLaCome')
Sonido_Cuchilla_Fin1.Volume=1.0
Sonido_Cuchilla_Fin1.MinDistance=4000
Sonido_Cuchilla_Fin1.MaxDistance=400000

###########################################################################################################

Sonido_Cuchilla_Inicio2=Sounds.CreateEntitySound('../../Sounds/disco-empiez.wav', 'CuchillaActivacion')
Sonido_Cuchilla_Inicio2.Volume=1.0
Sonido_Cuchilla_Inicio2.MinDistance=4000
Sonido_Cuchilla_Inicio2.MaxDistance=400000

Sonido_Cuchilla_Bucle2=Sounds.CreateEntitySound('../../Sounds/disco-empiez1.wav', 'CuchillaCorta')
Sonido_Cuchilla_Bucle2.Volume=1.0
Sonido_Cuchilla_Bucle2.MinDistance=4000
Sonido_Cuchilla_Bucle2.MaxDistance=400000

Sonido_Cuchilla_Fin2=Sounds.CreateEntitySound('../../Sounds/disco-parada.wav', 'CuchillaSeLaCome')
Sonido_Cuchilla_Fin2.Volume=1.0
Sonido_Cuchilla_Fin2.MinDistance=4000
Sonido_Cuchilla_Fin2.MaxDistance=400000

o=Bladex.CreateEntity("Blade0","CuchillaFernando",-231922,-23572 + 2250,90102.453506)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.Weapon = 1
InitDataField.Initialise(o)
o.Data.NoFXOnHit=1


o=Bladex.CreateEntity("Blade1","CuchillaFernando",-231920,-25101,86997 - 2250)
o.Scale=1.000000
o.Orientation=0.008727,-0.999962,0.000000,0.000000
o.Weapon = 1
InitDataField.Initialise(o)
o.Data.NoFXOnHit=1

o=Bladex.CreateEntity("Blade2","CuchillaFernando",-231920,-25101,93154 + 2250)
o.Scale=1.000000
o.Orientation=0.008727,-0.999962,0.000000,0.000000
o.Weapon = 1
InitDataField.Initialise(o)
o.Data.NoFXOnHit=1

stop_blades = 0
blades_ready = 1
playerstate = 0

Bladex.CreateTimer("Timer60",1.0/60.0)

WAIT_TIME = 6.0
CounterXCU = 0
CounterXCU1 = 0
CounterXCU2 = 0


Entrada = Bladex.GetSector(-215000,-25000,90000)
#Salida = Bladex.GetSector(-237000,-26000,90000)

Entrada.OnEnter = ActivateBlades
Entrada.OnLeave = DeactivateBlades

#Salida.OnLeave = DeactivateBlades
#Salida.OnEnter = ActivateBlades

#char.Position = -203549.867423, -24034.5999881, 90141
#Bladex.SetCallCheck(1)