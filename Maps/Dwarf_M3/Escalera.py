import Doors
import Bladex
import Sounds
import Button
import Scorer


Escalera_sound=Sounds.CreateEntitySound('../../Sounds/block-sliding.wav', 'SonidoEscalera')
Escalera_sound.Volume=0.5
Escalera_sound.MinDistance=5000
Escalera_sound.MaxDistance=30000

SonidoClackEsc = Sounds.CreateEntitySound('../../Sounds/metal-lever2.wav', 'SonidoClackEscalera')
SonidoClackEsc.Volume=1.0
SonidoClackEsc.MinDistance=10000
SonidoClackEsc.MaxDistance=30000


#escalon 1
escalon1=Doors.CreateDoor("Escalon1", (-201000,-20000,69000), (0,-1,0), 0, 4000, Doors.OPENED)

escalon1.opentype=Doors.UNIF
escalon1.o_med_vel=-900
escalon1.o_med_displ=250

escalon1.closetype=Doors.UNIF
escalon1.c_med_vel=900
escalon1.c_med_displ=250

#escalon 2
escalon2=Doors.CreateDoor("Escalon2", (-201000,-20000,69500), (0,-1,0), 0, 4000, Doors.OPENED)

escalon2.opentype=Doors.UNIF
escalon2.o_med_vel=-900
escalon2.o_med_displ=500

escalon2.closetype=Doors.UNIF
escalon2.c_med_vel=900
escalon2.c_med_displ=500

#escalon 3
escalon3=Doors.CreateDoor("Escalon3", (-201000,-20000,70000), (0,-1,0), 0, 4000, Doors.OPENED)

escalon3.opentype=Doors.UNIF
escalon3.o_med_vel=-900
escalon3.o_med_displ=750

escalon3.closetype=Doors.UNIF
escalon3.c_med_vel=900
escalon3.c_med_displ=750

#escalon 4
escalon4=Doors.CreateDoor("Escalon4", (-201000,-20000,70500), (0,-1,0), 0, 4000, Doors.OPENED)

escalon4.opentype=Doors.UNIF
escalon4.o_med_vel=-900
escalon4.o_med_displ=1000

escalon4.closetype=Doors.UNIF
escalon4.c_med_vel=900
escalon4.c_med_displ=1000

#escalon 5
escalon5=Doors.CreateDoor("Escalon5", (-201000,-20000,71000), (0,-1,0), 0, 4000, Doors.OPENED)

escalon5.opentype=Doors.UNIF
escalon5.o_med_vel=-900
escalon5.o_med_displ=1250

escalon5.closetype=Doors.UNIF
escalon5.c_med_vel=900
escalon5.c_med_displ=1250

#escalon 6
escalon6=Doors.CreateDoor("Escalon6", (-201000,-20000,71500), (0,-1,0), 0, 4000, Doors.OPENED)

escalon6.opentype=Doors.UNIF
escalon6.o_med_vel=-900
escalon6.o_med_displ=1500

escalon6.closetype=Doors.UNIF
escalon6.c_med_vel=900
escalon6.c_med_displ=1500

#escalon 7
escalon7=Doors.CreateDoor("Escalon7", (-201000,-20000,72000), (0,-1,0), 0, 4000, Doors.OPENED)

escalon7.opentype=Doors.UNIF
escalon7.o_med_vel=-900
escalon7.o_med_displ=1750

escalon7.closetype=Doors.UNIF
escalon7.c_med_vel=900
escalon7.c_med_displ=1750

#escalon 8
escalon8=Doors.CreateDoor("Escalon8", (-201000,-20000,72500), (0,-1,0), 0, 4000, Doors.OPENED)

escalon8.opentype=Doors.UNIF
escalon8.o_med_vel=-900
escalon8.o_med_displ=2000

escalon8.closetype=Doors.UNIF
escalon8.c_med_vel=900
escalon8.c_med_displ=2000

#escalon 9
escalon9=Doors.CreateDoor("Escalon9", (-201000,-20000,73000), (0,-1,0), 0, 4000, Doors.OPENED)

escalon9.opentype=Doors.UNIF
escalon9.o_med_vel=-900
escalon9.o_med_displ=2250

escalon9.closetype=Doors.UNIF
escalon9.c_med_vel=900
escalon9.c_med_displ=2250

#escalon 10
escalon10=Doors.CreateDoor("Escalon10", (-201000,-20000,73500), (0,-1,0), 0, 4000, Doors.OPENED)

escalon10.opentype=Doors.UNIF
escalon10.o_med_vel=-900
escalon10.o_med_displ=2500

escalon10.closetype=Doors.UNIF
escalon10.c_med_vel=900
escalon10.c_med_displ=2500

#escalon 11
escalon11=Doors.CreateDoor("Escalon11", (-201000,-20000,74000), (0,-1,0), 0, 4000, Doors.OPENED)

escalon11.opentype=Doors.UNIF
escalon11.o_med_vel=-900
escalon11.o_med_displ=2750

escalon11.closetype=Doors.UNIF
escalon11.c_med_vel=900
escalon11.c_med_displ=2750

#escalon 12
escalon12=Doors.CreateDoor("Escalon12", (-201000,-20000,74500), (0,-1,0), 0, 4000, Doors.OPENED)

escalon12.opentype=Doors.UNIF
escalon12.o_med_vel=-900
escalon12.o_med_displ=3000

escalon12.closetype=Doors.UNIF
escalon12.c_med_vel=900
escalon12.c_med_displ=3000

#escalon 13
escalon13=Doors.CreateDoor("Escalon13", (-201000,-20000,75000), (0,-1,0), 0, 4000, Doors.OPENED)

escalon13.opentype=Doors.UNIF
escalon13.o_med_vel=-900
escalon13.o_med_displ=3250

escalon13.closetype=Doors.UNIF
escalon13.c_med_vel=900
escalon13.c_med_displ=3250

#escalon 14
escalon14=Doors.CreateDoor("Escalon14", (-201000,-20000,75500), (0,-1,0), 0, 4000, Doors.OPENED)

escalon14.opentype=Doors.UNIF
escalon14.o_med_vel=-900
escalon14.o_med_displ=3500

escalon14.closetype=Doors.UNIF
escalon14.c_med_vel=900
escalon14.c_med_displ=3500

#escalon 15
escalon15=Doors.CreateDoor("Escalon15", (-201000,-20000,76000), (0,-1,0), 0, 4000, Doors.OPENED)

escalon15.opentype=Doors.UNIF
escalon15.o_med_vel=-900
escalon15.o_med_displ=3750

escalon15.closetype=Doors.UNIF
escalon15.c_med_vel=900
escalon15.c_med_displ=3750


escalon15.SetWhileOpenSound(Escalera_sound)
escalon15.SetEndOpenSound(SonidoClackEsc)



o=Bladex.CreateEntity("PuEscalera","Bloque",-222250,-19950,75500)
o.Orientation=0.5,0.5,-0.5,0.5
darfuncs.SetHint(o,"Trigger")


ButEsc = Button.CreateButtonCombination(0,Descubrelo,0)
bp1 = ButEsc.AddButton("PuEscalera",2,(0,0,-1),800,0,0,0)