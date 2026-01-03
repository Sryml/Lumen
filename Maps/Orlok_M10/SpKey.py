import Bladex
import AuxFuncs
import OnInitTake
import Objects
import Actions
import Doors
import Sounds
import math
import darfuncs




##################################
###     Sistemas de particulas
##################################

Bladex.ReadAlphaBitMap("../../Data/Estrellita.bmp","Estrellita")
Bladex.ReadBitMap("../../Data/KeyGlow.bmp","GlowKey")


Bladex.AddParticleGType("ChispaLlave","Estrellita",B_PARTICLE_GTYPE_ADD,60)

for i in range(60):
	if i>40:
		traux=(i-40.0)/20.0
	elif i>30:
		traux=0.0
	else:
		traux=(30.0-i)/30.0
	r=100.0
	g=100.0
	b=255.0
	a=200.0*(1.0-traux)
	size=40.0*(1.0-traux)
	Bladex.SetParticleGVal("ChispaLlave",i,r,g,b,a,size)



##########################################
###     Objetos, particulas, luces...
##########################################

col=Bladex.CreateEntity("ColumnaLlave","Columna",25000.0, -32363.0, 68975.0)
col.Static=1
col.Scale=0.9
col.Orientation=0.707107,0.707107,0.000000,0.000000

coldin=Objects.CreateDinamicObject("ColumnaLlave")

llaveazul=Bladex.CreateEntity("SHELL","LlaveAzul",25000.0, -32950.0, 69000.0, "Physic")
llaveazul.Scale=1.00000
llaveazul.Orientation=0.707107,0.707107,0.000000,0.000000
llaveazul.Solid=0
darfuncs.SetHint(llaveazul,"Aquamarine Key")

luzllave=Bladex.CreateEntity("LuzLlaveAzul", "Entity Spot", 0.0, 0.0, 0.0)
luzllave.Position=llaveazul.Position
luzllave.Color=160, 128, 255
luzllave.Intensity=0.4
luzllave.Precission=0.06
luzllave.CastShadows=0
luzllave.GlowTexture="GlowKey"
luzllave.AngVel=0.2
luzllave.SizeFactor=1.0

llaveazuldin=Objects.CreateDinamicObject("SHELL")

chllave=Bladex.CreateEntity("ChispasLlave", "Entity Particle System D1", 0.0, 0.0, 0.0)
chllave.Position=llaveazul.Position
chllave.ParticleType="ChispaLlave"
chllave.YGravity=0.0
chllave.Friction=0.0
chllave.PPS=50
chllave.Velocity=0.0, 0.0, 0.0
chllave.RandomVelocity=-4.0
chllave.Time2Live=60



####################
###     Puertas
####################

deslizhoja1=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizHoja1")
golpehoja1=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "GolpeHoja1")
deslizhoja2=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "DeslizHoja2")
golpehoja2=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "GolpeHoja2")
clickagujero=Sounds.CreateEntitySound("../../Sounds/trap-clicked.wav", "ClickAgujero")

hoja1=Doors.CreateDoor("Hoja1", (24500, -34000, 76500), (1, 0, 0), 250, 2125, Doors.CLOSED)
hoja2=Doors.CreateDoor("Hoja2", (25500, -34000, 76500), (-1, 0, 0), 250, 2125, Doors.CLOSED)
agujero=Doors.CreateDoor("Agujero", (25000, -31500, 69000), (0, -1, 0), 705, 1495, Doors.CLOSED)

hoja1.opentype=Doors.AC_UNIF
hoja1.o_init_vel=0
hoja1.o_init_displ=250
hoja1.o_med_vel=-300
hoja1.o_med_displ=1625
hoja1.closetype=Doors.AC_UNIF
hoja1.c_init_vel=0
hoja1.c_init_displ=250
hoja1.c_med_vel=600
hoja1.c_med_displ=1625
hoja2.opentype=Doors.AC_UNIF
hoja2.o_init_vel=0
hoja2.o_init_displ=250
hoja2.o_med_vel=-300
hoja2.o_med_displ=1625
hoja2.closetype=Doors.AC_UNIF
hoja2.c_init_vel=0
hoja2.c_init_displ=250
hoja2.c_med_vel=600
hoja2.c_med_displ=1625
agujero.opentype=Doors.AC_UNIF
agujero.o_init_vel=0
agujero.o_init_displ=140
agujero.o_med_vel=-131.3
agujero.o_med_displ=650
agujero.closetype=Doors.AC_UNIF
agujero.c_init_vel=0
agujero.c_init_displ=140
agujero.c_med_vel=131.3
agujero.c_med_displ=650

hoja1.SetWhileOpenSound(deslizhoja1)
hoja1.SetEndOpenSound(golpehoja1)
hoja1.SetWhileCloseSound(deslizhoja1)
hoja1.SetEndCloseSound(golpehoja1)
hoja2.SetWhileOpenSound(deslizhoja2)
hoja2.SetEndOpenSound(golpehoja2)
hoja2.SetWhileCloseSound(deslizhoja2)
hoja2.SetEndCloseSound(golpehoja2)
agujero.SetInitOpenSound(clickagujero)


#################################
###     Funcionamiento llave
#################################

ejey=(0.0, 1.0, 0.0)
ejeyn=(0.0, -1.0, 0.0)

KEYTRVAR=1.0/90.0
KEYSCLVAR=1.0/90.0
KEYINTVAR=0.4/90.0
KEYSIZEVAR=1.0/90.0
KEYESTTIME=2.0

######## Funcion: ReseteaCamaraLlave()

######## Funcion: MueveChispasLlave()

######## Funcion: AbrePuertaFort()

######## Funcion: DesapareceLlaveGradual(ent_name, time)

######## Funcion: LanzaEstelaChispasLlave(ent_name, time)

######## Funcion: DesapareceLlave()

######## Funcion: ElevaLlave()

######## Funcion: CogeLlave()

######## Funcion: SituaPersonajeLlave()

OnInitTake.AddOnInitTakeEvent("SHELL", SituaPersonajeLlave)


######## Funcion: repite()
