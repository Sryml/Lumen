import Doors
import Levers
import Locks
import Objects
import Sounds
import Button





#########
#########


###trampa cripta

###tramo A. La escalera baja

escalond=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
escalond.MaxDistance=30000
escalond.MinDistance=5000
escalond.Volume=1.0

escalong=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
escalong.MaxDistance=30000
escalong.MinDistance=5000
escalong.Volume=1.0

#escalon 1a
escalon1a=Doors.CreateDoor("Escalon1a", (-42250,11300,-22000), (0,-1,0), 0, 200, Doors.CLOSED)

escalon1a.opentype=Doors.UNIF
escalon1a.o_med_vel=-900
escalon1a.o_med_displ=200

escalon1a.closetype=Doors.UNIF
escalon1a.c_med_vel=900
escalon1a.c_med_displ=200


#escalon 1b
escalon1b=Doors.CreateDoor("Escalon1b", (-42250,11300,-23000), (0,-1,0), 0, 200, Doors.CLOSED)

escalon1b.opentype=Doors.UNIF
escalon1b.o_med_vel=-900
escalon1b.o_med_displ=200

escalon1b.closetype=Doors.UNIF
escalon1b.c_med_vel=900
escalon1b.c_med_displ=200


#escalon 2a
escalon2a=Doors.CreateDoor("Escalon2a", (-43250,11300,-22000), (0,-1,0), 0, 700, Doors.CLOSED)

escalon2a.opentype=Doors.UNIF
escalon2a.o_med_vel=-900
escalon2a.o_med_displ=700

escalon2a.closetype=Doors.UNIF
escalon2a.c_med_vel=800
escalon2a.c_med_displ=700


#escalon 2b
escalon2b=Doors.CreateDoor("Escalon2b", (-43250,11300,-23000), (0,-1,0), 0, 700, Doors.CLOSED)

escalon2b.opentype=Doors.UNIF
escalon2b.o_med_vel=-900
escalon2b.o_med_displ=700

escalon2b.closetype=Doors.UNIF
escalon2b.c_med_vel=800
escalon2b.c_med_displ=700

#escalon 3a
escalon3a=Doors.CreateDoor("Escalon3a", (-44250,11300,-22000), (0,-1,0), 0, 1200, Doors.CLOSED)

escalon3a.opentype=Doors.UNIF
escalon3a.o_med_vel=-900
escalon3a.o_med_displ=1200

escalon3a.closetype=Doors.UNIF
escalon3a.c_med_vel=900
escalon3a.c_med_displ=1200

#escalon 3b
escalon3b=Doors.CreateDoor("Escalon3b", (-44250,11300,-23000), (0,-1,0), 0, 1200, Doors.CLOSED)

escalon3b.opentype=Doors.UNIF
escalon3b.o_med_vel=-900
escalon3b.o_med_displ=1200

escalon3b.closetype=Doors.UNIF
escalon3b.c_med_vel=900
escalon3b.c_med_displ=1200



#escalon 4a
escalon4a=Doors.CreateDoor("Escalon4a", (-45250,11300,-22000), (0,-1,0), 0, 1700, Doors.CLOSED)

escalon4a.opentype=Doors.UNIF
escalon4a.o_med_vel=-900
escalon4a.o_med_displ=1700

escalon4a.closetype=Doors.UNIF
escalon4a.c_med_vel=900
escalon4a.c_med_displ=1700


#escalon 4b
escalon4b=Doors.CreateDoor("Escalon4b", (-45250,11300,-23000), (0,-1,0), 0, 1700, Doors.CLOSED)

escalon4b.opentype=Doors.UNIF
escalon4b.o_med_vel=-900
escalon4b.o_med_displ=1700

escalon4b.closetype=Doors.UNIF
escalon4b.c_med_vel=900
escalon4b.c_med_displ=1700


#escalon 5a
escalon5a=Doors.CreateDoor("Escalon5a", (-46250,11300,-22000), (0,-1,0), 0, 2200, Doors.CLOSED)

escalon5a.opentype=Doors.UNIF
escalon5a.o_med_vel=-900
escalon5a.o_med_displ=2200

escalon5a.closetype=Doors.UNIF
escalon5a.c_med_vel=900
escalon5a.c_med_displ=2200



#escalon 5b
escalon5b=Doors.CreateDoor("Escalon5b", (-46250,11300,-23000), (0,-1,0), 0, 2200, Doors.CLOSED)

escalon5b.opentype=Doors.UNIF
escalon5b.o_med_vel=-900
escalon5b.o_med_displ=2200

escalon5b.closetype=Doors.UNIF
escalon5b.c_med_vel=900
escalon5b.c_med_displ=2200


#escalon 6a
escalon6a=Doors.CreateDoor("Escalon6a", (-47250,11300,-22000), (0,-1,0), 0, 2700, Doors.CLOSED)

escalon6a.opentype=Doors.UNIF
escalon6a.o_med_vel=-900
escalon6a.o_med_displ=2700

escalon6a.closetype=Doors.UNIF
escalon6a.c_med_vel=900
escalon6a.c_med_displ=2700


#escalon 6b
escalon6b=Doors.CreateDoor("Escalon6b", (-47250,11300,-23000), (0,-1,0), 0, 2700, Doors.CLOSED)

escalon6b.opentype=Doors.UNIF
escalon6b.o_med_vel=-900
escalon6b.o_med_displ=2700

escalon6b.closetype=Doors.UNIF
escalon6b.c_med_vel=900
escalon6b.c_med_displ=2700


#escalon 7a
escalon7a=Doors.CreateDoor("Escalon7a", (-48250,11300,-22000), (0,-1,0), 0, 3200, Doors.CLOSED)

escalon7a.opentype=Doors.UNIF
escalon7a.o_med_vel=-900
escalon7a.o_med_displ=3200

escalon7a.closetype=Doors.UNIF
escalon7a.c_med_vel=900
escalon7a.c_med_displ=3200


#escalon 7b
escalon7b=Doors.CreateDoor("Escalon7b", (-48250,11300,-23000), (0,-1,0), 0, 3200, Doors.CLOSED)

escalon7b.opentype=Doors.UNIF
escalon7b.o_med_vel=-900
escalon7b.o_med_displ=3200

escalon7b.closetype=Doors.UNIF
escalon7b.c_med_vel=900
escalon7b.c_med_displ=3200


#escalon 8a
escalon8a=Doors.CreateDoor("Escalon8a", (-49250,11300,-22000), (0,-1,0), 0, 3700, Doors.CLOSED)

escalon8a.opentype=Doors.UNIF
escalon8a.o_med_vel=-900
escalon8a.o_med_displ=3700

escalon8a.closetype=Doors.UNIF
escalon8a.c_med_vel=900
escalon8a.c_med_displ=3700


#escalon 8b
escalon8b=Doors.CreateDoor("Escalon8b", (-49250,11300,-23000), (0,-1,0), 0, 3700, Doors.CLOSED)

escalon8b.opentype=Doors.UNIF
escalon8b.o_med_vel=-900
escalon8b.o_med_displ=3700

escalon8b.closetype=Doors.UNIF
escalon8b.c_med_vel=900
escalon8b.c_med_displ=3700


#escalon 9a
escalon9a=Doors.CreateDoor("Escalon9a", (-50250,11300,-22000), (0,-1,0), 0, 4200, Doors.CLOSED)

escalon9a.opentype=Doors.UNIF
escalon9a.o_med_vel=-900
escalon9a.o_med_displ=4200

escalon9a.closetype=Doors.UNIF
escalon9a.c_med_vel=900
escalon9a.c_med_displ=4200


#escalon 9b
escalon9b=Doors.CreateDoor("Escalon9b", (-50250,11300,-23000), (0,-1,0), 0, 4200, Doors.CLOSED)

escalon9b.opentype=Doors.UNIF
escalon9b.o_med_vel=-900
escalon9b.o_med_displ=4200

escalon9b.closetype=Doors.UNIF
escalon9b.c_med_vel=900
escalon9b.c_med_displ=4200


#escalon 10a
escalon10a=Doors.CreateDoor("Escalon10a", (-51250,11300,-22000), (0,-1,0), 0, 4700, Doors.CLOSED)

escalon10a.opentype=Doors.UNIF
escalon10a.o_med_vel=-900
escalon10a.o_med_displ=4700

escalon10a.closetype=Doors.UNIF
escalon10a.c_med_vel=500
escalon10a.c_med_displ=4700

#escalon 10b
escalon10b=Doors.CreateDoor("Escalon10b", (-51250,11300,-23000), (0,-1,0), 0, 4700, Doors.CLOSED)

escalon10b.opentype=Doors.UNIF
escalon10b.o_med_vel=-900
escalon10b.o_med_displ=4700

escalon10b.closetype=Doors.UNIF
escalon10b.c_med_vel=500
escalon10b.c_med_displ=4700


#escalon 11a
escalon11a=Doors.CreateDoor("Escalon11a", (-52250,11300,-22000), (0,-1,0), 0, 5200, Doors.CLOSED)

escalon11a.opentype=Doors.UNIF
escalon11a.o_med_vel=-900
escalon11a.o_med_displ=5200

escalon11a.closetype=Doors.UNIF
escalon11a.c_med_vel=900
escalon11a.c_med_displ=5200

#escalon 11b
escalon11b=Doors.CreateDoor("Escalon11b", (-52250,11300,-23000), (0,-1,0), 0, 5200, Doors.CLOSED)

escalon11b.opentype=Doors.UNIF
escalon11b.o_med_vel=-900
escalon11b.o_med_displ=5200

escalon11b.closetype=Doors.UNIF
escalon11b.c_med_vel=900
escalon11b.c_med_displ=5200


#escalon 12a
escalon12a=Doors.CreateDoor("Escalon12a", (-53250,11300,-22000), (0,-1,0), 0, 5700, Doors.CLOSED)

escalon12a.opentype=Doors.UNIF
escalon12a.o_med_vel=-900
escalon12a.o_med_displ=5700

escalon12a.closetype=Doors.UNIF
escalon12a.c_med_vel=900
escalon12a.c_med_displ=5700

#escalon 12b
escalon12b=Doors.CreateDoor("Escalon12b", (-53250,11300,-23000), (0,-1,0), 0, 5700, Doors.CLOSED)

escalon12b.opentype=Doors.UNIF
escalon12b.o_med_vel=-900
escalon12b.o_med_displ=5700

escalon12b.closetype=Doors.UNIF
escalon12b.c_med_vel=900
escalon12b.c_med_displ=5700


#escalon 13a
escalon13a=Doors.CreateDoor("Escalon13a", (-54250,11300,-22000), (0,-1,0), 0, 6200, Doors.CLOSED)

escalon13a.opentype=Doors.UNIF
escalon13a.o_med_vel=-900
escalon13a.o_med_displ=6200

escalon13a.closetype=Doors.UNIF
escalon13a.c_med_vel=900
escalon13a.c_med_displ=6200

#escalon 13b
escalon13b=Doors.CreateDoor("Escalon13b", (-54250,11300,-23000), (0,-1,0), 0, 6200, Doors.CLOSED)

escalon13b.opentype=Doors.UNIF
escalon13b.o_med_vel=-900
escalon13b.o_med_displ=6200

escalon13b.closetype=Doors.UNIF
escalon13b.c_med_vel=900
escalon13b.c_med_displ=6200


#escalon 14a
escalon14a=Doors.CreateDoor("Escalon14a", (-55250,11300,-22000), (0,-1,0), 0, 6700, Doors.CLOSED)

escalon14a.opentype=Doors.UNIF
escalon14a.o_med_vel=-900
escalon14a.o_med_displ=6700

escalon14a.closetype=Doors.UNIF
escalon14a.c_med_vel=900
escalon14a.c_med_displ=6700


#escalon 14b
escalon14b=Doors.CreateDoor("Escalon14b", (-55250,11300,-23000), (0,-1,0), 0, 6700, Doors.CLOSED)

escalon14b.opentype=Doors.UNIF
escalon14b.o_med_vel=-900
escalon14b.o_med_displ=6700

escalon14b.closetype=Doors.UNIF
escalon14b.c_med_vel=900
escalon14b.c_med_displ=6700


#funci�n que sube y baja los escalones de ambos tramos al unisono


escalon14a.SetWhileOpenSound(escalond)
escalon14a.SetEndOpenSound(escalong)

escalon14a.SetWhileCloseSound(escalond)
escalon14a.SetEndCloseSound(escalong)

o=Bladex.CreateEntity("bloque","Bloque",-31380.429626,9469.027132,-22557.734373)
o.Static=0
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
darfuncs.SetHint(o,"Trigger")

button=Button.CreateButtonCombination(0,Descubre,"")
button.AddButton("bloque",3,(1,0,0),400,0,0,1)











##############################################
#########trampa aplastamiento  ###############
##############################################



res=ReadGSFile.ReadGhostSectorFile("trampas.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])



ladodesliz=Sounds.CreateEntitySound("../../Sounds/M-MECAN.wav", "MaderaDesliz")
ladodesliz.Volume=1
ladodesliz.MinDistance = 4000
ladodesliz.MaxDistance = 40000

ladogolpe=Sounds.CreateEntitySound("../../Sounds/close-gate-1.wav", "MaderaGolpe")
ladogolpe.Volume=1
ladogolpe.MinDistance = 4000
ladogolpe.MaxDistance = 40000


lado1=Doors.CreateDoor("lado1", (-44000,8000,-20000), (0,0,-1), 0, 4500, Doors.OPENED)


lado1.opentype=Doors.UNIF
lado1.o_med_vel=-800
lado1.o_med_displ=4500


lado1.closetype=Doors.AC
lado1.c_init_displ=4500
lado1.c_med_vel=500


lado1.SetWhileOpenSound(ladodesliz)
lado1.SetEndOpenSound(ladogolpe)

lado1.SetWhileCloseSound(ladodesliz)
lado1.SetEndCloseSound(ladogolpe)
lado1.Squezze=1

######################################3

lado2=Doors.CreateDoor("lado2", (-44000,8000,-24000), (0,0,1), 0, 4500, Doors.OPENED)


lado2.opentype=Doors.UNIF
lado2.o_med_vel=-800
lado2.o_med_displ=4500


lado2.closetype=Doors.AC
lado2.c_init_displ=4500
lado2.c_med_vel=500
lado2.Squezze=1
lado2.OnEndCloseFunc = Abrelados
lado2.OnEndCloseArgs = ()

#lado2.SetWhileOpenSound(maderadesliz)
#lado2.SetEndOpenSound(maderagolpe)

#lado2.SetWhileCloseSound(maderadesliz)
#lado2.SetEndCloseSound(maderagolpe)

#####################################
piedradesliz=Sounds.CreateEntitySound("../../Sounds/M-MECAN.wav", "MaderaDesliz")
piedradesliz.Volume=1
piedradesliz.MinDistance = 3000
piedradesliz.MaxDistance = 40000

piedragolpe=Sounds.CreateEntitySound("../../Sounds/close-gate-1.wav", "MaderaGolpe")
piedragolpe.Volume=1
piedragolpe.MinDistance = 3000
piedragolpe.MaxDistance = 40000

ptatrampa=Doors.CreateDoor("ptatrampa", (-30500,5000,-19500), (0,1,0), 0, 6250, Doors.OPENED)


ptatrampa.opentype=Doors.UNIF
ptatrampa.o_med_vel=-1000
ptatrampa.o_med_displ=6250


ptatrampa.closetype=Doors.AC
ptatrampa.c_init_displ=6250
ptatrampa.c_med_vel=5000


ptatrampa.SetWhileOpenSound(piedradesliz)
ptatrampa.SetEndOpenSound(piedragolpe)

ptatrampa.SetWhileCloseSound(piedradesliz)
ptatrampa.SetEndCloseSound(piedragolpe)

cam = Bladex.GetEntity("Camera")

ladosCerrados = 0

TrapClack = Sounds.CreateEntitySound("../../Sounds/mechanism_operated_2.wav", "trapclackgfh")

print("poniendo el trigger sector")
Bladex.SetTriggerSectorFunc("sectortr1", "OnEnter", EntroEnTriggerSector)
