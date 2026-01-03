import Doors
import Levers
import Locks
import Objects
import Sounds
import Sparks
import ReadGSFile
import Button
import Stars
import darfuncs



sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")


granpiedradeslizando=Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav", "Granpiedradeslizando")
cierrepiedra=Sounds.CreateEntitySound("../../Sounds/Stone-door-shut.wav", "Cierrepiedra")

granpiedradeslizando2=Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav", "Granpiedradeslizando2")
cierrepiedra2=Sounds.CreateEntitySound("../../Sounds/Stone-door-shut.wav", "Cierrepiedra2")


mecanismo1=Sounds.CreateEntitySound("../../Sounds/mechanism3.wav", "Mecanismo1")
madera=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "Madera")


rastrini=Bladex.CreateEntity("Rastrini","Rastrillo",325911.547685, -1800, -227201.584969)
rastrini.Static=1
rastrini.Scale=1.000000
rastrini.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Rastrini")



###
###
###


###rastrillo zona escaleras 1

rastresc=Bladex.CreateEntity("Rastresc","Rastrillo",309611.030000,-4949.704000,-191350.111000)
rastresc.Static=1
rastresc.Scale=1.149474
rastresc.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Rastresc")

palanca0=Levers.PlaceLever("Palanca0",Levers.LeverType3,(311419.673794,-46.768847,-190355.429637),(0.006171,0.006171,0.707080,-0.707080),1.0)



# rastrillo nuevo en zona golem

rastgol=Bladex.CreateEntity("Rastgol","Rastrillo",347255.513000,-5043.179000,-193149.572000)
rastgol.Static=1
rastgol.Scale=1.000000
rastgol.Orientation=0.707080,0.707080,-0.006171,0.006171
Sparks.SetMetalSparkling("Rastgol")

palanca00=Levers.PlaceLever("Palanca00",Levers.LeverType3,(345148.487067,129.883513,-192364.935130),(0.006171,0.006171,0.707080,-0.707080),1.0)


#palanca00.OnTurnOffFunc=Cierragol
#palanca00.OnTurnOffArgs=()

#rastrillo nuevo exterior golem

rastgol2=Bladex.CreateEntity("Rastgol2","Rastrillo",343606.947257,-4785.484341,-179308.875334)
rastgol2.Static=1
rastgol2.Scale=1.000000
rastgol2.Orientation=0.500000,0.500000,0.500000,-0.500000
Sparks.SetMetalSparkling("Rastgol2")

palanca000=Levers.PlaceLever("Palanca000",Levers.LeverType3,(340392.513127,486.789792,-181502.291583),(0.326506,0.326506,0.627211,-0.627211),1.0)


##rastrillo ultima hora

rastgol3=Bladex.CreateEntity("Rastgol3","Rastrillo",368791.030693,-4900.221084,-175110.743523)
rastgol3.Static=1
rastgol3.Scale=1.000000
rastgol3.Orientation=0.500000,0.500000,0.500000,-0.500000
Sparks.SetMetalSparkling("Rastgol3")

palanca0000=Levers.PlaceLever("Palanca0000",Levers.LeverType3,(368004.908654,338.709443,-177176.845861),(0.500000,0.500000,0.500000,-0.500000),1.0)


##rastrillo zona inferior

rastinf=Bladex.CreateEntity("Rastinf","Rastrillo",389273.281862,4933.843693,-212298.040711)
rastinf.Static=1
rastinf.Scale=0.678370
rastinf.Orientation=0.500000,0.500000,0.500000,-0.500000
Sparks.SetMetalSparkling("Rastinf")


#cerradura y llave del rastrillo anterior


cerradurainf=Locks.PlaceLock("cerradurainf","Cerraduracutre",(388374.799825,8890.771300,-210891.396565),(0.012341,0.012341,-0.706999,0.706999),1.596263)
darfuncs.SetHint(cerradurainf.obj,"Golem Lock")


###Rastrillo llave cobre oxidada

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")


rastrillox=Bladex.CreateEntity("Rastrillox","Rastrillo",347015.276666,14272.233194,-229847.248729)
rastrillox.Static=1
rastrillox.Scale=1.061520
rastrillox.Orientation=0.500000,0.500000,-0.500000,0.500000
Sparks.SetMetalSparkling("Rastrillox")

rastrilloxdin=Objects.CreateDinamicObject("Rastrillox")



sectx1=Bladex.GetSector(355000, 16000, -226000)
sectx1.OnEnter=x1



sectx2=Bladex.GetSector(345000, 15000, -245000)
sectx2.OnEnter=x2






###palanca abre rastrillo

palanca5=Levers.PlaceLever("Palanca5",Levers.LeverType3,(344888.845567,15715.993092,-233124.594451),(0.500000,0.500000,0.500000,-0.500000),1.0)


palanca5.mode=1

palanca5.OnTurnOnFunc=Abrex
palanca5.OnTurnOnArgs=()











###GRAN PUERTA RASTRILLO QUE DA PASO A LA ZONA 2 DEL MAPA




granrast=Bladex.CreateEntity("Granrast","Rastrillo",325489.215146,-5895.024781,-178185.296849)
granrast.Static=1
granrast.Scale=1.0
granrast.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Granrast")


cerradura1=Locks.PlaceLock("cerradura1","Cerraduracobox",(328139.975804,-51.642598,-179740.367855),(0.495618,0.495618,0.504344,-0.504344),1.445076)
darfuncs.SetHint(cerradura1.obj,"Atysi Lock")







########
#######
#######
##### PUERTA GORDA Y RASTRILLOS

###rastrillo 1


sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")


rastgor=Bladex.CreateEntity("Rastgor","Rastrillo",336373.094200,-7393.188150,-156559.764259)
rastgor.Static=1
rastgor.Scale=0.844377
rastgor.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Rastgor")


rastgordin=Objects.CreateDinamicObject("Rastgor")


#2

rastgor2=Bladex.CreateEntity("Rastgor2","Rastrillo",313145.065897,-6855.368366,-156702.166247)
rastgor2.Static=1
rastgor2.Scale=0.712973
rastgor2.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Rastgor2")


rastgor2din=Objects.CreateDinamicObject("Rastgor2")







gordai=Doors.CreateDoor("Gordai", (324000,0,-137000), (1,0,0), 0, 2500, Doors.CLOSED)


gordai.opentype=Doors.UNIF
gordai.o_med_vel=-500
gordai.o_med_displ=2500


gordai.closetype=Doors.UNIF
gordai.c_med_vel=500
gordai.c_med_displ=2500


gordai.SetWhileOpenSound(granpiedradeslizando)
gordai.SetEndOpenSound(cierrepiedra)

gordai.SetWhileCloseSound(granpiedradeslizando)
gordai.SetEndCloseSound(cierrepiedra)


##hoja derecha

#granpiedradeslizando2=Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav", "Granpiedradeslizando2")
#cierrepiedra2=Sounds.CreateEntitySound("../../Sounds/Stone-door-shut.wav", "Cierrepiedra2")


gordad=Doors.CreateDoor("Gordad", (327000,0,-137000), (-1,0,0), 0, 2500, Doors.CLOSED)



gordad.opentype=Doors.UNIF
gordad.o_med_vel=-500
gordad.o_med_displ=2500


gordad.closetype=Doors.UNIF
gordad.c_med_vel=500
gordad.c_med_displ=2500


gordad.SetWhileOpenSound(granpiedradeslizando2)
gordad.SetEndOpenSound(cierrepiedra2)

gordad.SetWhileCloseSound(granpiedradeslizando2)
gordad.SetEndCloseSound(cierrepiedra2)

##palanca que abre la puerta gorda

palancag=Levers.PlaceLever("Palancag",Levers.LeverType3,(338899.005195,-6181.522109,-144201.812931),(0.707107,0.707107,0.000000,0.000000),1.0)


palancag.mode=2


palancag.OnTurnOnFunc=Abreg
palancag.OnTurnOnArgs=()








########
########

###elevador tablilla


#mecanismo1=Sounds.CreateEntitySound("../../Sounds/mechanism3.wav", "Mecanismo1")
#madera=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "Madera")


elevador1=Doors.CreateDoor("Elevador1", (340000,-4000,-135000), (0,-1,0), 0, 22000, Doors.OPENED)


elevador1.opentype=Doors.UNIF
elevador1.o_med_vel=-1500
elevador1.o_med_displ=22000


elevador1.closetype=Doors.UNIF
elevador1.c_med_vel=1500
elevador1.c_med_displ=22000


elevador1.SetWhileCloseSound(madera)
elevador1.SetWhileOpenSound(madera)
elevador1.SetEndCloseSound(mecanismo1)
elevador1.SetEndOpenSound(mecanismo1)


res=ReadGSFile.ReadGhostSectorFile("ascensor.sf")
for igs in res:
   Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

Bladex.SetTriggerSectorFunc("ascensor", "OnEnter", Pisa )

char = Bladex.GetEntity("Player1")
char.SendTriggerSectorMsgs = 1


elevador1.OnEndCloseFunc=Vuelve0
elevador1.OnEndOpenFunc=Vuelve01

###elevador columna puente


elevador2=Doors.CreateDoor("Elevador2", (325000,16000,-125000), (0,-1,0), 0, 30000, Doors.OPENED)


elevador2.opentype=Doors.UNIF
elevador2.o_med_vel=-1500
elevador2.o_med_displ=30000


elevador2.closetype=Doors.UNIF
elevador2.c_med_vel=1500
elevador2.c_med_displ=30000

elevador2.SetWhileCloseSound(granpiedradeslizando)
elevador2.SetWhileOpenSound(granpiedradeslizando)
elevador2.SetEndCloseSound(cierrepiedra)
elevador2.SetEndOpenSound(cierrepiedra)

##palanca que activa el elevador

palanca1=Levers.PlaceLever("Palanca1",Levers.LeverType3,(325015.491000,43952.359000,-127722.653000),(0.000000,0.000000,0.707107,-0.707107),1.0)


palanca1.mode=1


palanca1.OnTurnOnFunc=Sube2
palanca1.OnTurnOnArgs=()


elevador2.OnEndCloseFunc=Vuelve



###elevador columna 2 puente

elevador3=Doors.CreateDoor("Elevador3", (325000,31000,-97000), (0,-1,0), 0, 14500, Doors.OPENED)


elevador3.opentype=Doors.UNIF
elevador3.o_med_vel=-1500
elevador3.o_med_displ=14500


elevador3.closetype=Doors.UNIF
elevador3.c_med_vel=2500
elevador3.c_med_displ=14500

elevador3.SetWhileCloseSound(granpiedradeslizando)
elevador3.SetWhileOpenSound(granpiedradeslizando)
elevador3.SetEndCloseSound(cierrepiedra)
elevador3.SetEndOpenSound(cierrepiedra)

##palancas que activan el elevador

palanca2a=Levers.PlaceLever("Palanca2a",Levers.LeverType3,(322155.262780,44034.295658,-97221.179717),(0.495618,0.495618,-0.504344,0.504344),1.0)


palanca2a.mode=1
palanca2a.OnTurnOnFunc=Sube3
palanca2a.OnTurnOnArgs=()




palanca2b=Levers.PlaceLever("Palanca2b",Levers.LeverType3,(323140.935611,29530.660508,-94642.503798),(0.500000,0.500000,-0.500000,0.500000),1.0)


palanca2b.mode=1

palanca2b.OnTurnOnFunc=Baja3
palanca2b.OnTurnOnArgs=()


palanca2b.OnTurnOffFunc=Sube3
palanca2b.OnTurnOffArgs=()

###rastrillo en puente inferior


rastpuen=Bladex.CreateEntity("Rastpuen","Rastrillo",324982.290000,39320.000000,-99503.384000)
rastpuen.Static=1
rastpuen.Scale=0.861349
rastpuen.Orientation=0.725374,0.688355,0.000000,0.000000
#Sparks.SetMetalSparkling("rastpuen")



###elevador previo a zona tablilla


elevador4=Doors.CreateDoor("Elevador4", (325000,16000,-80000), (0,-1,0), 0, 14000, Doors.OPENED)


elevador4.opentype=Doors.UNIF
elevador4.o_med_vel=-1500
elevador4.o_med_displ=14000


elevador4.closetype=Doors.UNIF
elevador4.c_med_vel=2000
elevador4.c_med_displ=14000

elevador4.SetWhileCloseSound(granpiedradeslizando)
elevador4.SetWhileOpenSound(granpiedradeslizando)
elevador4.SetEndCloseSound(cierrepiedra)
elevador4.SetEndOpenSound(cierrepiedra)


##palancas que activan el elevador

palanca3a=Levers.PlaceLever("Palanca3a",Levers.LeverType3,(324990.554037,28349.442410,-77124.207296),(0.707107,0.707107,0.000000,0.000000),1.0)


palanca3a.mode=1




palanca3a.OnTurnOnFunc=Sube4
palanca3a.OnTurnOnArgs=()


palanca3b=Levers.PlaceLever("Palanca3b",Levers.LeverType3,(321881.425347,14004.262495,-77902.257316),(0.500000,0.500000,-0.500000,0.500000),1.0)

palanca3b.mode=1


palanca3b.OnTurnOnFunc=Baja4
palanca3b.OnTurnOnArgs=()


palanca3b.OnTurnOffFunc=Sube4
palanca3b.OnTurnOffArgs=()


###2 rastrillos laterales antes de zona tablilla

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")



rastla=Bladex.CreateEntity("Rastla","Rastrillo",354408.833526,8259.796229,-43689.273799,"Physic")
rastla.Scale=1.000000
rastla.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Rastla")

rastladin=Objects.CreateDinamicObject("Rastla")








sectrast1=Bladex.GetSector(350000, 10000, -40000)


sectrast1.OnEnter=bb




###palanca abre rastrillo

palanca6a=Levers.PlaceLever("Palanca6a",Levers.LeverType3,(352138.064255,8750.243785,-46950.882391),(0.500000,0.500000,-0.500000,0.500000),1.0)


palanca6a.mode=1

palanca6a.OnTurnOnFunc=Abrela
palanca6a.OnTurnOnArgs=()


#palanca6a.OnTurnOffFunc=Cierrala
#palanca6a.OnTurnOffArgs=()



sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")


rastlb=Bladex.CreateEntity("Rastlb","Rastrillo",295489.350891,8381.893569,-43781.660792,"Physic")
rastlb.Scale=1.000000
rastlb.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Rastlb")


rastlbdin=Objects.CreateDinamicObject("Rastlb")





sectrast2=Bladex.GetSector(300000, 10000, -40000)


sectrast2.OnEnter=bbb






###palanca abre rastrillo


palanca6b=Levers.PlaceLever("Palanca6b",Levers.LeverType3,(297832.884152,8406.745351,-47547.995169),(0.500000,0.500000,0.500000,-0.500000),1.0)

palanca6b.mode=1


palanca6b.OnTurnOnFunc=Abrelb
palanca6b.OnTurnOnArgs=()


###
###
###Gran puerta tablilla


tabi=Doors.CreateDoor("Tabi", (324000,3000,-31500), (1,0,0), 0, 2750, Doors.CLOSED)


tabi.opentype=Doors.UNIF
tabi.o_med_vel=-500
tabi.o_med_displ=2750


tabi.closetype=Doors.UNIF
tabi.c_med_vel=500
tabi.c_med_displ=2750

tabi.SetWhileOpenSound(granpiedradeslizando)
tabi.SetEndOpenSound(cierrepiedra)


##hoja derecha

tabd=Doors.CreateDoor("Tabd", (326000,3000,-31500), (-1,0,0), 0, 2750, Doors.CLOSED)



tabd.opentype=Doors.UNIF
tabd.o_med_vel=-500
tabd.o_med_displ=2750


tabd.closetype=Doors.UNIF
tabd.c_med_vel=500
tabd.c_med_displ=2750

tabd.SetWhileOpenSound(granpiedradeslizando2)
tabd.SetEndOpenSound(cierrepiedra2)



o=Bladex.CreateEntity("ArchButton1","AdoquinRuna",324981.544183,-4981.804583,-32147.686259)
o.Static=0
o.Scale=1.580459
o.Orientation=0.500000,0.500000,-0.500000,0.500000
archbutton1=Button.CreateButtonCombination(0,Abrexx,"")
archbutton1.AddButton("ArchButton1",3,(0,0,1),400,0,0,1)


##rastrillo gas

rastrillomovil=Bladex.CreateEntity("RastrilloMovil","Rastrillo",325902.027381, 4000, -210965.412381)
rastrillomovil.Static=1
rastrillomovil.Scale=1
rastrillomovil.Orientation=0.707107,0.707107,0.000000,0.000000

CerraduraGas=Locks.PlaceLock("CerraduraGas","Cerraduracobox",(323043.904114,8800.149830,-210244.081568),(0.500000,0.500000,-0.500000,0.500000),1.518790)
darfuncs.SetHint(CerraduraGas.obj,"Jara Lock")


palanca7=Levers.PlaceLever("Palanca7",Levers.LeverType3,(326655.360536,6809.978360,20251.592565),(0.495618,0.495618,0.504344,-0.504344),1.0)