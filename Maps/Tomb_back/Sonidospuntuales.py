

import Sounds
import Bladex


"""

cuervo1=Sounds.CreatePeriodicSound("../../Sounds/torch-burn.wav", "cuervo1",10,5,(-35000, 4500, -3100))
cuervo1.MinDistance=1000
cuervo1.MaxDistance=20000
cuervo1.Volume=1
cuervo1.BaseVolume=1.0
cuervo1.Scale=1.0
cuervo1.SendNotify=0

cuervo1.PlayPeriodic()

###EJEMPLO DE SONIDO PUNTUAL CONTINUO###
v8=Bladex.CreateSound("../../Sounds/whistlingwind-thruconduit.wav","v8")
v8.MaxDistance=20000
v8.MinDistance=2000
v8.Volume=1.0
v8.BaseVolume=1.0
v8.Scale=1.0
v8.SendNotify=0
v8.Play(-34250, -31000, 26500,-1)


antorcha1=Bladex.CreateSound("../../Sounds/torch-burn.wav","antorcha1")
antorcha1.MaxDistance=20000
antorcha1.MinDistance=2000
antorcha1.Volume=1.0
antorcha1.BaseVolume=1.0
antorcha1.Scale=1.0
antorcha1.SendNotify=0
antorcha1.Play(-35000, 4500, -3100,-1)
"""
sp1=Bladex.CreateSound("../../Sounds/frog-bg.wav","cricri")
sp1.MaxDistance=20000
sp1.MinDistance=400
sp1.Volume=0.7
sp1.BaseVolume=1.0
sp1.Scale=1.0
sp1.SendNotify=0

sp1.Play(-35000, 4500, -3100,-1)
