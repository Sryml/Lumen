import Bladex
import Sounds

desprendimiento=Sounds.CreateEntitySound("../../Sounds/drawbridge-door-close.wav", "GolpeDesprendimiento")
desprendimiento.Volume=1
desprendimiento.MinDistance=10000
desprendimiento.MaxDistance=90000

Bladex.CreateTimer("Timer10",1.0/10.0)

number = 0
n_pilares = 0
n_fragments = 0
pilar = [0]
fragment = [0]
fragment_position = [0]
fragment_radio = [0]
fragment_state = [0]

last_pilar = 0



suelo = Bladex.GetSector(-64000,0,141500)
suelo.OnEnter = ActivateDesprendimientoSuelo
suelo.OnLeave = DeactivateDesprendimientoSuelo


AddDesprendimiento((-56000,3800,136937),1000,1000)
AddDesprendimiento((-58000,3800,141937),3000,4000)
AddDesprendimiento((-57000,3800,146937),2000,1000)
AddDesprendimiento((-61000,3800,136937),2000,1000)
AddDesprendimiento((-62000,3800,141937),1000,2000)
AddDesprendimiento((-64000,3800,146937),3000,1000)
AddDesprendimiento((-65000,3800,140937),2000,5000)
AddDesprendimiento((-68000,3800,137937),1000,2000)
AddDesprendimiento((-70000,3800,143937),3000,2000)
AddDesprendimiento((-72000,3800,138937),3000,3000)
AddDesprendimiento((-72000,3800,145937),3000,2000)

AddPilar((-58000,3800,136937))
AddPilar((-60000,3800,146937))
AddPilar((-62000,3800,138937))
AddPilar((-62000,3800,144937))
AddPilar((-68000,3800,140937))
AddPilar((-68000,3800,146937))
AddPilar((-74000,3800,142937))