import Actions
import Sounds
import Scorer
import B3DLib
import darfuncs

#char.Position = -97065.856439,-27037.893892,155774.699829

soundtotemhit=Sounds.CreateEntitySound('../../Sounds/golpe-madera-pesada.wav', 'SoundTotemHit')
soundtotemhit.Volume=0.5
soundtotemhit.MinDistance=10000
soundtotemhit.MaxDistance=20000

soundesfuerzo1=Sounds.CreateEntitySound('../../Sounds/esfuerzo-barb-corto.wav', 'SoundEsfuerzo1')
soundesfuerzo1.Volume=0.5
soundesfuerzo1.MinDistance=10000
soundesfuerzo1.MaxDistance=20000

soundesfuerzo2=Sounds.CreateEntitySound('../../Sounds/esfuerzo-barb-mediano.wav', 'SoundEsfuerzo2')
soundesfuerzo2.Volume=0.5
soundesfuerzo2.MinDistance=10000
soundesfuerzo2.MaxDistance=20000

soundesfuerzo3=Sounds.CreateEntitySound('../../Sounds/esfuerzo-barb-largo.wav', 'SoundEsfuerzo3')
soundesfuerzo3.Volume=0.5
soundesfuerzo3.MinDistance=10000
soundesfuerzo3.MaxDistance=20000

soundcrujido1=Sounds.CreateEntitySound('../../Sounds/wood-bridge-creak.wav', 'SoundCrujido1')
soundcrujido1.Volume=1
soundcrujido1.MinDistance=10000
soundcrujido1.MaxDistance=20000

soundcrujido2=Sounds.CreateEntitySound('../../Sounds/wood-bridge-creak2.wav', 'SoundCrujido2')
soundcrujido2.Volume=1
soundcrujido2.MinDistance=10000
soundcrujido2.MaxDistance=20000


boingtotem=Bladex.CreateEntity("Totem","Boingtotem2",-95065.856439,-27037.893892,155774.699829)
boingtotem.RotateRel(0,0,0,1,0,0,1.57)
boingtotem.Alpha = 0.0

totem=Bladex.CreateEntity("Totem","Totem2",-95065.856439,-27037.893892,155774.699829)
totem.Orientation = (0.631790161133, 0.604139924049, -0.350825279951, -0.335824012756)
totem.Static=1

punterototem=Bladex.CreateEntity("Puntero Totem","GhostPointer",-95065.856439,-28527.893892,155774.699829)
punterototem.Static = 0
punterototem.Scale = 0.1
punterototem.UseFunc = ThrowTotem
darfuncs.SetHint(punterototem,"Totem Pole")