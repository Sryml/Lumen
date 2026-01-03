import Sounds

FPS = 30.0

wyv2 = Bladex.CreateEntity("Wyv2","Wyvern",-6012.023,-15213.682,-69911.445)
wyv2.RotateRel(0,0,0,1,0,0,1.57)
wyv2.Static = 1

soundwyvscream2=Sounds.CreateEntitySound('../../Sounds/Wyvern.wav', 'SoundWyvernScream')
soundwyvscream2.Volume=0.75
soundwyvscream2.MinDistance=1000
soundwyvscream2.MaxDistance=50000


SecWyvCiclica = Bladex.GetSector(-134000,-5000,38500)
SecWyvCiclica.OnEnter = WyvCiclica


SecWyvSeVaATPC = Bladex.GetSector(-20000,-13000,30000)
SecWyvSeVaATPC.OnEnter = WyvSeVaATPC