# (-67210,-9916,-68408) # sector de deteccion
# (-63121,-9594,-69152) # eliminar flechas
import math
import whrandom
import Sounds

__X__ =  11750
__Z__ = -22000

InsideTrap=0

flechazo=Sounds.CreateEntitySound('../../Sounds/dart-shoot.wav', 'LaunchArrow')
flechazo.Volume=0.5; flechazo.MinDistance=7000; flechazo.MaxDistance=10000;



SActivaTFlecha = Bladex.GetSector(-67210+__X__,-9916,-68408+__Z__)
SActivaTFlecha.OnEnter = Entrampa
SActivaTFlecha.OnLeave = Saltrampa
