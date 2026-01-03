import Sounds
import Bladex




### sonidos derrumbamientos lejanos y movimientos de rocas en zona inicial

quake1=Sounds.CreatePeriodicSound("../../Sounds/Rock-floor-collapse.wav", "quake1",30,5,(299695.803001, 3000, -2909.96369149))
quake1.Volume=1
quake1.MinDistance=100
quake1.MaxDistance=50000
quake1.BaseVolume=1.0
quake1.Scale=1.0
quake1.SendNotify=0
quake1.PlayPeriodic()




quake2=Sounds.CreatePeriodicSound("../../Sounds/Rockfall3x.wav", "quake2",15,5,(307975.838193, 23192.4900305, -25795.014228))
quake2.Volume=0.7
quake2.MinDistance=100
quake2.MaxDistance=50000
quake2.BaseVolume=1.0
quake2.Scale=1.0
quake2.SendNotify=0
quake2.PlayPeriodic()





quake3=Sounds.CreatePeriodicSound("../../Sounds/Rockfall1rev.wav", "quake3",10,1,(307859.168481, 31170.1351563, 3272.1996447))
quake3.Volume=0.3
quake3.MinDistance=100
quake3.MaxDistance=50000
quake3.BaseVolume=1.0
quake3.Scale=1.0
quake3.SendNotify=0
quake3.PlayPeriodic()



quake4=Sounds.CreatePeriodicSound("../../Sounds/rocas-eco.wav", "quake4",20,10,(278811.759709, 36974.5785156, -803.557792635))
quake4.Volume=0.7
quake4.MinDistance=100
quake4.MaxDistance=50000
quake4.BaseVolume=1.0
quake4.Scale=1.0
quake4.SendNotify=0
quake4.PlayPeriodic()



quake5=Sounds.CreatePeriodicSound("../../Sounds/M-rafaga-viento.wav", "quake5",15,3,(288648.095546, 29938.8416251, 21656.1675826))
quake5.Volume=0.7
quake5.MinDistance=100
quake5.MaxDistance=50000
quake5.BaseVolume=1.0
quake5.Scale=1.0
quake5.SendNotify=0
quake5.PlayPeriodic()









###sonidos demoniacos por aqu� y por all�.

##en catedral esqueletos

cat1=Sounds.CreatePeriodicSound("../../Sounds/spirits.wav", "cat1",10,5,(422500, 65000, -41500))
cat1.Volume=1
cat1.MinDistance=100
cat1.MaxDistance=50000
cat1.BaseVolume=1.0
cat1.Scale=1.0
cat1.SendNotify=0
cat1.PlayPeriodic()

cat2=Sounds.CreatePeriodicSound("../../Sounds/spirits2.wav", "cat2",10,5,(421720, 66881, -52838))
cat2.Volume=1
cat2.MinDistance=100
cat2.MaxDistance=50000
cat2.BaseVolume=1.0
cat2.Scale=1.0
cat2.SendNotify=0
cat2.PlayPeriodic()


##en vampiro's house

vamp1=Sounds.CreatePeriodicSound("../../Sounds/spirits2.wav", "vamp1",20,5,(410000, 72000, 0))
vamp1.Volume=1
vamp1.MinDistance=100
vamp1.MaxDistance=50000
vamp1.BaseVolume=1.0
vamp1.Scale=1.0
vamp1.SendNotify=0
vamp1.PlayPeriodic()

vamp2=Sounds.CreatePeriodicSound("../../Sounds/spirits.wav", "vamp2",20,5,(430000, 72000, 0))
vamp2.Volume=1
vamp2.MinDistance=100
vamp2.MaxDistance=50000
vamp2.BaseVolume=1.0
vamp2.Scale=1.0
vamp2.SendNotify=0
vamp2.PlayPeriodic()

#####sonidos demoniacos en bucle#####

buclea=Sounds.CreatePeriodicSound("../../Sounds/spirits.wav", "buuu",10,4,(404500, 85000, 26000))
buclea.Volume=1
buclea.MinDistance=100
buclea.MaxDistance=50000
buclea.Volume=1
buclea.BaseVolume=1.0
buclea.Scale=1.0
buclea.SendNotify=0

buclea.PlayPeriodic()



bucleb=Sounds.CreatePeriodicSound("../../Sounds/spirits2.wav", "buuu2",15,8,(407500, 87000, 35000))
bucleb.Volume=1
bucleb.MinDistance=100
bucleb.MaxDistance=50000
bucleb.Volume=1
bucleb.BaseVolume=1.0
bucleb.Scale=1.0
bucleb.SendNotify=0

bucleb.PlayPeriodic()

#EN ZONA DEMONIOS


dem1=Sounds.CreatePeriodicSound("../../Sounds/spirits.wav", "dem1",10,4,(461241, 80000, 24415))
dem1.Volume=1
dem1.MinDistance=100
dem1.MaxDistance=50000
dem1.Volume=1
dem1.BaseVolume=1.0
dem1.Scale=1.0
dem1.SendNotify=0

dem1.PlayPeriodic()



dem2=Sounds.CreatePeriodicSound("../../Sounds/spirits2.wav", "dem2",15,8,(508027, 80000, -11751))
dem2.Volume=1
dem2.MinDistance=100
dem2.MaxDistance=50000
dem2.Volume=1
dem2.BaseVolume=1.0
dem2.Scale=1.0
dem2.SendNotify=0

dem2.PlayPeriodic()




##en escalera previa a elevador

prev=Sounds.CreatePeriodicSound("../../Sounds/spirits.wav", "prev",15,5,(528250, 86000, 58000))
prev.Volume=1
prev.MinDistance=100
prev.MaxDistance=50000
prev.BaseVolume=1.0
prev.Scale=1.0
prev.SendNotify=0
prev.PlayPeriodic()


##tras escalera previa a elevador


tras=Sounds.CreatePeriodicSound("../../Sounds/spirits2.wav", "tras",15,5,(528500, 293000, 148000))
tras.Volume=1
tras.MinDistance=100
tras.MaxDistance=50000
tras.BaseVolume=1.0
tras.Scale=1.0
tras.SendNotify=0
tras.PlayPeriodic()


##en EndOfFirstArena


end1=Sounds.CreatePeriodicSound("../../Sounds/spirits.wav", "end1",10,5,(529228, 297000, 147262))
end1.Volume=1
end1.MinDistance=100
end1.MaxDistance=50000
end1.BaseVolume=1.0
end1.Scale=1.0
end1.SendNotify=0
end1.PlayPeriodic()


end2=Sounds.CreatePeriodicSound("../../Sounds/spirits.wav", "end2",10,5,(542185, 294215, 182855))
end2.Volume=1
end2.MinDistance=100
end2.MaxDistance=50000
end2.BaseVolume=1.0
end2.Scale=1.0
end2.SendNotify=0
end2.PlayPeriodic()



end3=Sounds.CreatePeriodicSound("../../Sounds/spirits.wav", "end3",10,5,(620011, 292285, 183426))
end3.Volume=1
end3.MinDistance=100
end3.MaxDistance=50000
end3.BaseVolume=1.0
end3.Scale=1.0
end3.SendNotify=0
end3.PlayPeriodic()




##entrada palacio BUUUUU

bu=Sounds.CreatePeriodicSound("../../Sounds/spirits2.wav", "bu",10,3,(697086, 310478, 169765))
bu.Volume=1
bu.MinDistance=100
bu.MaxDistance=50000
bu.BaseVolume=1.0
bu.Scale=1.0
bu.SendNotify=0
bu.PlayPeriodic()




bu0=Sounds.CreatePeriodicSound("../../Sounds/spirits2.wav", "bu0",10,4,(740000, 325000, 170000))
bu0.Volume=1
bu0.MinDistance=100
bu0.MaxDistance=50000
bu0.BaseVolume=1.0
bu0.Scale=1.0
bu0.SendNotify=0
bu0.PlayPeriodic()


###En el palacio BU

bu1=Sounds.CreatePeriodicSound("../../Sounds/spirits.wav", "bu1",7,3,(808000, 330000, 170000))
bu1.Volume=1
bu1.MinDistance=100
bu1.MaxDistance=50000
bu1.BaseVolume=1.0
bu1.Scale=1.0
bu1.SendNotify=0
bu1.PlayPeriodic()

bu2=Sounds.CreatePeriodicSound("../../Sounds/spirits2.wav", "bu2",7,4,(828000, 330000, 170000))
bu2.Volume=1
bu2.MinDistance=100
bu2.MaxDistance=50000
bu2.BaseVolume=1.0
bu2.Scale=1.0
bu2.SendNotify=0
bu2.PlayPeriodic()


bu3=Sounds.CreatePeriodicSound("../../Sounds/spirits2.wav", "bu3",7,5,(866000, 330000, 170000))
bu3.Volume=1
bu3.MinDistance=100
bu3.MaxDistance=50000
bu3.BaseVolume=1.0
bu3.Scale=1.0
bu3.SendNotify=0
bu3.PlayPeriodic()
