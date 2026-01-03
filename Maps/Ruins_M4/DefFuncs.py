import ScriptSkip
import whrandom
import Reference
import NetSounds




#################################################################################################
## Positions.py



def IrPosicion1():
	char=Bladex.GetEntity("Player1")
	char.Position=46139.666, 751.5, 738.593	# interior piramide inicio

def IrPosicion2():
	char=Bladex.GetEntity("Player1")
	char.Position=48000, 6250, 25700		# derrumbamiento subt. cerca de inicio

def IrPosicion3():
	char=Bladex.GetEntity("Player1")
	char.Position=-76800, 4750, -3200		# derrumbamiento subt. opuesto a inicio

def IrPosicion4():
	char=Bladex.GetEntity("Player1")
	char.Position=-49000, -2850, -57000		# mausoleo

def IrPosicion5():
	char=Bladex.GetEntity("Player1")
	char.Position=51925, -1248, 46055		# lago laberinto

def IrPosicion6():
	char=Bladex.GetEntity("Player1")
	char.Position=-16000, -1500.0, 40000.0	# frente piramide norte

def IrPosicion7():
	char=Bladex.GetEntity("Player1")
	char.Position=46000, -4000.0, 28500.0	# puente laberinto

def IrPosicion8():
	char=Bladex.GetEntity("Player1")
	char.Position=8000.0, 825.0, 12450.0	# final

def IrPosicion9():
	char=Bladex.GetEntity("Player1")
	char.Position=32400, -3350, -33360		# fuentes

posicion1=IrPosicion1
posicion2=IrPosicion2
posicion3=IrPosicion3
posicion4=IrPosicion4
posicion5=IrPosicion5
posicion6=IrPosicion6
posicion7=IrPosicion7
posicion8=IrPosicion8
posicion9=IrPosicion9



#################################################################################################



#################################################################################################
## Enemigos.py


def DescongelaEnemigos(lista_enemigos):
	for ene_name in lista_enemigos:
		ene=Bladex.GetEntity(ene_name)
		if ene and ene.Life>0:
			ene.UnFreeze()

def ActivaOrco5(SectorIndex,EntityName):
	if EntityName=='Player1':
		pers=Bladex.GetEntity("5orc")
		if pers and pers.Life>0:
			pers.Blind=pers.Deaf=0

def DesactivaOrco5(SectorIndex,EntityName):
	if EntityName=='Player1':
		pers=Bladex.GetEntity("5orc")
		if pers and pers.Life>0:
			pers.Blind=pers.Deaf=1

def AmazonDefeatsOrc(person):
	Bladex.GetEntity(person).Data.ImDeadFuncX(person)
	Bladex.TriggerEvent(2)



#################################################################################################


#################################################################################################
## Generadores.py



###################################################
#     Funciones complementarias del generador     #
###################################################

def RemueveTierraGen(pos, v1, v2, v3):
	tierra=Bladex.CreateEntity("TierraRemoviendose", "Entity Particle System D3", pos[0]+v1[0], pos[1]-1100.0, pos[2]+v1[2])
	tierra.D1=v2[0]-v1[0], 0.0, v2[2]-v1[2]
	tierra.D2=v3[0]-v1[0], 0.0, v3[2]-v1[2]
	if pos[1]>3000.0:
		tierra.ParticleType="Tierra2sub"
	else:
		tierra.ParticleType="Tierra2"
	tierra.PPS=64
	tierra.YGravity=200.0
	tierra.Friction=0.1
	tierra.Velocity=0.0, -400.0, 0.0
	tierra.RandomVelocity=15.0
	tierra.Time2Live=64
	tierra.DeathTime=Bladex.GetTime()+2.0

def SaltaTierraGen(enmgen):
	char=Bladex.GetEntity("Player1")
	pos=enmgen.Position
	v=char.Position[0]-pos[0], 0.0, char.Position[2]-pos[2]
	v=B3DLib.Normalize(v)
	v1=v[0]*500.0, 0.0, v[2]*500.0
	v2=v1[0]*math.cos(1.7453)-v1[2]*math.sin(1.7453), 0.0, v1[0]*math.sin(1.7453)+v1[2]*math.cos(1.7453)
	v3=v2[0]*math.cos(2.7925)-v2[2]*math.sin(2.7925), 0.0, v2[0]*math.sin(2.7925)+v2[2]*math.cos(2.7925)
	saltatie=Bladex.CreateEntity("TierraSaltando", "Entity Particle System D1", pos[0], pos[1]-1100.0, pos[2])
	saltatie.ParticleType="Tierra3"
	saltatie.PPS=1024
	saltatie.YGravity=4900.0
	saltatie.Friction=0.05
	saltatie.Velocity=0.0, -600.0, 0.0
	saltatie.RandomVelocity=50.0
	saltatie.Time2Live=60
	saltatie.DeathTime=Bladex.GetTime()+10.0/60.0
	saltati2=Bladex.CreateEntity("TierraSaltando2", "Entity Particle System D1", pos[0], pos[1]-1100.0, pos[2])
	if pos[1]>3000.0:
		saltati2.ParticleType="Tierra2sub"
	else:
		saltati2.ParticleType="Tierra2"
	saltati2.PPS=128
	saltati2.YGravity=200.0
	saltati2.Friction=0.1
	saltati2.Velocity=0.0, -300.0, 0.0
	saltati2.RandomVelocity=15.0
	saltati2.Time2Live=32
	saltati2.DeathTime=Bladex.GetTime()+10.0/60.0
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, RemueveTierraGen, (pos, v1, v2, v3))



### Generadores de las catacumbas

def SetAreas2728(enm):
	enm.ActionAreaMin=pow(2,26)
	enm.ActionAreaMax=pow(2,27)

def SetAreas2930(enm):
	enm.ActionAreaMin=pow(2,28)
	enm.ActionAreaMax=pow(2,29)



#################################################################################################




#################################################################################################
## Puertas.py

def ParaArenillaPuertaSecretaSub():
	global arenillapuertasecretasub
	arenillapuertasecretasub.DeathTime=Bladex.GetTime()+1.0/60.0

def AbrePuertaSecretaSub():
	global arenillapuertasecretasub
	arenillapuertasecretasub=Bladex.CreateEntity("ArenillaPuertaSecretaSub", "Entity Particle System D2", -56260.0, 3010.0, 4990.0)
	arenillapuertasecretasub.D=-1980.0, 0.0, 0.0
	arenillapuertasecretasub.ParticleType="Sand"
	arenillapuertasecretasub.YGravity=4900.0
	arenillapuertasecretasub.Friction=0.2
	arenillapuertasecretasub.RandomVelocity=10.0
	arenillapuertasecretasub.PPS=512
	arenillapuertasecretasub.Time2Live=32
	puertasecretasub.OpenDoor()

def CierraPuertaSecretaSub2():
	ParaArenillaPuertaSecretaSub()
	polvareda=Bladex.CreateEntity("PolvoPuertaSecretaSub", "Entity Particle System D2", -56260.0, 5990.0, 4990.0)
	polvareda.D=-1980.0, 0.0, 0.0
	polvareda.ParticleType="MediumDust"
	polvareda.YGravity=0.0
	polvareda.Friction=0.2
	polvareda.PPS=512
	polvareda.Velocity=0.0, -1000.0, -1000.0
	polvareda.RandomVelocity=30.0
	polvareda.Time2Live=30
	polvareda.DeathTime=Bladex.GetTime()+3.0/60.0

def CierraPuertaSecretaSub():
	global arenillapuertasecretasub
	arenillapuertasecretasub=Bladex.CreateEntity("ArenillaPuertaSecretaSub", "Entity Particle System D2", -56260.0, 3010.0, 4990.0)
	arenillapuertasecretasub.D=-1980.0, 0.0, 0.0
	arenillapuertasecretasub.ParticleType="Sand"
	arenillapuertasecretasub.YGravity=4900.0
	arenillapuertasecretasub.Friction=0.2
	arenillapuertasecretasub.RandomVelocity=10.0
	arenillapuertasecretasub.PPS=512
	arenillapuertasecretasub.Time2Live=32
	puertasecretasub.CloseDoor()


def AbrePuertaPozo():
	puertapozogolpe.Volume=0.6
	puertapozo1.OpenDoor()
	puertapozo2.OpenDoor()

def CierraPuertaPozo2():
	polvareda=Bladex.CreateEntity("PolvoPuertaPozo", "Entity Particle System D2", 31937.5, 8990.0, -53750.0)
	polvareda.D=0.0, -4480.0, 0.0
	polvareda.ParticleType="MediumDust"
	polvareda.YGravity=0.0
	polvareda.Friction=0.2
	polvareda.PPS=512
	polvareda.Velocity=750.0, 0.0, 0.0
	polvareda.RandomVelocity=20.0
	polvareda.Time2Live=30
	polvareda.DeathTime=Bladex.GetTime()+6.0/60.0

def CierraPuertaPozo():
	puertapozogolpe.Volume=1.0
	puertapozo1.CloseDoor()
	puertapozo2.CloseDoor()



def AbreRastrilloCementerio():
	desplazamientos=(2000.0, 750.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(500.0, 2000)
	vel_finales=(2000.0, 500)
	son_durante=(sonidodeslizamientorastrillo, sonidodeslizamientorastrillo)
	son_finales=("", sonidogolperastrillo)
	Objects.NDisplaceObject(rastrillocementeriodin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)



def AbrePuertaFinal():
	puertapozogolpe.Volume=0.6
	puertafinal.OpenDoor()

def CierraPuertaFinal():
	puertapozogolpe.Volume=1.0
	puertafinal.CloseDoor()

def CierraPuertaFinal2():
	polvareda=Bladex.CreateEntity("PolvoPuertaFinal", "Entity Particle System D2", -22525.0, 6990.0, 11525.0)
	polvareda.D=0.0, -5230.0, 0.0
	polvareda.ParticleType="MediumDust"
	polvareda.YGravity=0.0
	polvareda.Friction=0.2
	polvareda.PPS=512
	polvareda.Velocity=-750.0, 0.0, 0.0
	polvareda.RandomVelocity=20.0
	polvareda.Time2Live=30
	polvareda.DeathTime=Bladex.GetTime()+6.0/60.0


def ReiniciaCamaraPinchosMaus():
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Bladex.SetListenerPosition(1)
	Scorer.SetVisible(1)
	Bladex.ActivateInput()


def ContAbrePinchosMausoleo():
	DescongelaEnemigos(("10orc", "11orc", "Beej7", "Beej7", "Beej8", "Beej9", "Beej10", "Beej11", "Beej12", "Beej13", "Beej14"))
	Bladex.SetListenerPosition(2)
	Scorer.SetVisible(0)
	AuxFuncs.MoveCamFromTo(-61250.0, -4850.0, -46800.0, -58000.0, -2100.0, -46980.0, -57000.0, -1225.0, -38500.0, -61430.0, -4900.0, -38025.0, 3.5, ReiniciaCamaraPinchosMaus)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, Objects.DisplaceObject, (pinchopue1din, 1900.0, (-1.0, 0.0, 0.0), 0.0, 12000.0, "", pinchosdeslizando1, pinchosgolpeando1))
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, Objects.DisplaceObject, (pinchopue2din, 2250.0, (-1.0, 0.0, 0.0), 0.0, 12000.0, "", pinchosdeslizando1, pinchosgolpeando1))
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, Objects.DisplaceObject, (pinchopue3din, 1900.0, (-1.0, 0.0, 0.0), 0.0, 12000.0, "", pinchosdeslizando1, pinchosgolpeando1))


def AbrePinchosMausoleo():
	global pinchosmausyaabiertos
	sonidopalanca.Play(-49518.923,-1500.0,-39771.62,0)
	Bladex.DeactivateInput()
	if not pinchosmausyaabiertos:
		pinchosmausyaabiertos=1
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, ContAbrePinchosMausoleo, ())
	else:
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, Objects.DisplaceObject, (pinchopue1din, 1900.0, (-1.0, 0.0, 0.0), 0.0, 12000.0, "", pinchosdeslizando1, pinchosgolpeando1))
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, Objects.DisplaceObject, (pinchopue2din, 2250.0, (-1.0, 0.0, 0.0), 0.0, 12000.0, "", pinchosdeslizando1, pinchosgolpeando1))
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, Objects.DisplaceObject, (pinchopue3din, 1900.0, (-1.0, 0.0, 0.0), 0.0, 12000.0, "", pinchosdeslizando1, pinchosgolpeando1))
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, Bladex.ActivateInput, ())


def CierraPinchosMausoleo():
	sonidopalanca.Play(-49518.923,-1500.0,-39771.62,0)
	Bladex.DeactivateInput()
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, Objects.DisplaceObject, (pinchopue1din, 1900.0, (1.0, 0.0, 0.0), 0.0, 12000.0, "", pinchosdeslizando1, pinchosgolpeando1))
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, Objects.DisplaceObject, (pinchopue2din, 2250.0, (1.0, 0.0, 0.0), 0.0, 12000.0, "", pinchosdeslizando1, pinchosgolpeando1))
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, Objects.DisplaceObject, (pinchopue3din, 1900.0, (1.0, 0.0, 0.0), 0.0, 12000.0, "", pinchosdeslizando1, pinchosgolpeando1))
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, Bladex.ActivateInput, ())


############################################
#     Puertas de estacas del laberinto     #
############################################


def MueveEstacasA():
	global yest3a
	despl=est3a.Position[1]-yest3a
	est1a.Move(0,despl,0)
	est2a.Move(0,despl,0)
	est4a.Move(0,despl,0)
	est5a.Move(0,despl,0)
	est6a.Move(0,despl,0)
	yest3a=est3a.Position[1]

def AbreEstacasA():
	sec1actenelab.OnEnter=""
	sec2actenelab.OnEnter=""
	secdesenelab.OnEnter=""
	Objects.DisplaceObject(est3adin, 4100.0, (0.0, 1.0, 0.0), 600.0, 600.0, "", estacasdesliz, clickbarra, MueveEstacasA)


def MueveEstacasB():
	global yest3b
	despl=est3b.Position[1]-yest3b
	est1b.Move(0,despl,0)
	est2b.Move(0,despl,0)
	est4b.Move(0,despl,0)
	est5b.Move(0,despl,0)
	yest3b=est3b.Position[1]

def AbreEstacasB():
	Objects.DisplaceObject(est3bdin, 4100.0, (0.0, 1.0, 0.0), 600.0, 600.0, "", estacasdesliz, clickbarra, MueveEstacasB)


#################################################################################################








#################################################################################################
## Collaps.py



def ReposicionaPlayer(x, y, z):
	char=Bladex.GetEntity("Player1")
	char.Position=x, y, z
	Bladex.SetTriggerSectorFunc("TSPinchos", "OnEnter", MuertePinchos)

def MuertePinchos(trsector_name, entity_name):
	pers=Bladex.GetEntity(entity_name)
	if pers and pers.Person:
		pers.Life=0
		if entity_name=="Player1":
			Bladex.RemoveTriggerSectorFunc("TSPinchos", "OnEnter")
			AuxFuncs.FadeTo(2.0, 6.0, 50, 0, 0)
			#Bladex.AddScheduledFunc(Bladex.GetTime()+4.8, ReposicionaPlayer, (47500, 6363, 25000))




def Cont2DerSubCerInic():
	derrumbesueloagua.Play(47000.0, 11500.0, 21000.0)

def Cont2DerSubOpInic():
	derrumbesueloagua.Play(-73000.0, 11200.0, 1000.0)

def ContDerSubCerInic():
	dersubcerinic.DoBreak((0.0, 0.0, 0.0), (47000.0, 7600.0, 21000.0), (0.0, 0.0, 0.0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, Cont2DerSubCerInic, ())

def ContDerSubOpInic():
	dersubopinic.DoBreak((0.0, 0.0, 0.0), (-73000.0, 6100.0, 1000.0), (0.0, 0.0, 0.0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, Cont2DerSubOpInic, ())

def DerSubCerInic(sector_index, entity_name):
	if entity_name=="Player1":
		derrumbesuelopiedra.Play(47000.0, 7600.0, 21000.0)
		sectordersubcerinic.OnEnter=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, ContDerSubCerInic, ())

def DerSubOpInic(sector_index, entity_name):
	if entity_name=="Player1":
		derrumbesuelopiedra.Play(-73000.0, 6100.0, 1000.0)
		sectordersubopinic.OnEnter=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, ContDerSubOpInic, ())




def Cont2DerPasarela():
	derrumbesueloagua.Play(58000.0, 4000.0, 52000.0)

def ContDerPasarela():
	derpasarela1.DoBreak((0.0, 0.0, 0.0), (58250.0, 500.0, 51500.0), (0.0, 0.0, 0.0))
	derpasarela2.DoBreak((0.0, 0.0, 0.0), (57750.0, 500.0, 52500.0), (0.0, 0.0, 0.0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.7, Cont2DerPasarela, ())

def DerrumbaPasarela(sector_index, entity_name):
	if entity_name=="Player1":
		derrumbesuelopiedra.Play(58000.0, 500.0, 52000.0)
		sectorderpasarela.OnWalkOn=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, ContDerPasarela, ())


def Cont2DerPasarelaSub():
	derrumbesueloagua.Play(-5000.0, 13000.0, -54500.0)

def ContDerPasarelaSub():
	derpasarelasub1.DoBreak((0.0, 0.0, 0.0), (-5000.0, 9500.0, -54000.0), (0.0, 0.0, 0.0))
	derpasarelasub2.DoBreak((0.0, 0.0, 0.0), (-5000.0, 9500.0, -55000.0), (0.0, 0.0, 0.0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.7, Cont2DerPasarelaSub, ())

def DerrumbaPasarelaSub(sector_index, entity_name):
	if entity_name=="Player1":
		derrumbesuelopiedra.Play(-5000.0, 9500.0, -54500.0)
		sectorderpasarelasub.OnWalkOn=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, ContDerPasarelaSub, ())



### Vapores del lago de acido

def VaporesAcido(ps, positions, snd_number):
	variation=whrandom.uniform(0.1, 0.7)
	new_pos=positions[whrandom.randint(0, 20)]
	ps.Position=x, y, z=new_pos
	new_pitch=whrandom.uniform(0.3, 3.0)
	if snd_number==5:
		snd_number=1
	surtgas=Bladex.GetSound("SurtidorGas"+`snd_number`)
	surtgas.Pitch=new_pitch
	surtgas.Play(x, y, z, 0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+variation, VaporesAcido, (ps, positions, snd_number+1))

def LanzaVaporesAcido(sector_index, entity_name):
	if entity_name=="Player1":
		sectorlanzavapores.OnEnter=""
		ps=Bladex.CreateEntity("VaporesLagoAcido", "Entity Particle System D1", 0, 0, 0)
		ps.ParticleType="GasVenenoso2"
		ps.YGravity=-600.0
		ps.Friction=0.05
		ps.PPS=20
		ps.Velocity=0.0, 0.0, 0.0
		ps.RandomVelocity=20.0
		ps.Time2Live=60
		positions=[ (-6000, 13480, -44500), (-1500, 13480, -46000), (-4500, 13480, -47000), (-7000, 13480, -48000), (-500, 13480, -49000), (-5500, 13480, -50500),
				(-2500, 13480, -50500), (1000, 13480, -52000), (-5000, 13480, -53000), (-2000, 13480, -53000), (0, 13480, -54500), (-7000, 13480, -54000),
				(-3500, 13480, -55500), (-10000, 13480, -54500), (-12500, 13480, -56500), (-11000, 13480, -59000), (-8500, 13480, -57000), (-7500, 13480, -60000),
				(-5500, 13480, -62000), (-4000, 13480, -59000), (-3000, 13480, -61000) ]
		VaporesAcido(ps, positions, 1)



def FuegoVerdePlayer(obj_name, time):
	global fuegoverde
	char=Bladex.GetEntity("Player1")
	fuegoverde.Position=char.Position[0], 14000, char.Position[2]

def ContRevive():
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")

def ReviveEnLagoSub(entity_name):
	global fuegoverde
	print "hola caracola!"
	fuegoverde.DeathTime=Bladex.GetTime()+1.0/60.0
	fuegoverde.RemoveFromList("Frame")
	fuegoverde.FrameFunc=""
	char=Bladex.GetEntity("Player1")
	char.Position=3397.0, 7749.0, -59890.0
	char.Life=200
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, ContRevive, ())

def MuerteEnLagoSub(sector_index, entity_name):
	global fuegoverde
	if entity_name=="Player1":
		char=Bladex.GetEntity("Player1")
		char.Life=0
		#char.AnmEndedFunc=ReviveEnLagoSub
		siseoacido.Play(char.Position[0], 13500, char.Position[2])
		fuegoverde=Bladex.CreateEntity("FuegoVerde", "Entity Particle System D1", char.Position[0], 14000, char.Position[2])
		fuegoverde.ParticleType="GreenFire"
		fuegoverde.YGravity=0.0
		fuegoverde.Friction=0.05
		fuegoverde.PPS=512
		fuegoverde.Velocity=0.0, -2000.0, 0.0
		fuegoverde.RandomVelocity=25.0
		fuegoverde.Time2Live=32
		fuegoverde.FrameFunc=FuegoVerdePlayer
		fuegoverde.SubscribeToList("Frame")
		cam=Bladex.GetEntity("Camera")
		cam.SType=0
		cam.TType=0



def Cont2DerPirAbajo():
	derpirabajo1.DoBreak((0.0, 0.0, 0.0), (-2000.0, -10000.0, -40000.0), (0.0, 0.0, 0.0))
	derpirabajo2.DoBreak((0.0, 0.0, 0.0), (0.0, -10000.0, -38000.0), (0.0, 0.0, 0.0))

def ContDerPirAbajo():
	derrumbesuelopiedra.Play(-1000.0, -10000.0, -38000.0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, Cont2DerPirAbajo, ())

def DerrumbaPirAbajo(sector_index, entity_name):
	if entity_name=="Player1":
		sectorderpirabajo.OnWalkOn=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, ContDerPirAbajo, ())



def Cont2DerPirIzq():
	derpirizq1.DoBreak((0.0, 0.0, 0.0), (-42000.0, -10000.0, 2000.0), (0.0, 0.0, 0.0))

def ContDerPirIzq():
	derrumbesuelopiedra.Play(-42000.0, -10000.0, 2000.0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, Cont2DerPirIzq, ())

def DerrumbaPirIzq(sector_index, entity_name):
	if entity_name=="Player1":
		sectorderpirizq.OnWalkOn=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, ContDerPirIzq, ())


def RompeMuroFalso(sector_index, entity_name, px, py, pz, ximpulse, yimpulse, zimpulse, x_norm, y_norm, z_norm,ximpulse=0,yimpulse=0,zimpulse=0,x_norm=0,y_norm=0,z_norm=0,material=""):
	if (pz<=-50750+125) and (pz>=-50750-125):#pz==-50750.0:
		sonidoroturamurofalso.Play(-28000.0, -1500.0, -50875.0, 0)
		sectormurofalsoext.DoBreak((0.0, 0.0, -2.5), (px, py, pz), (0.0, 0.0, 0.0))
		sectorrompemurofalsoext.OnHit=""
	if (pz<=-37500+125) and (pz>=-37500-125):#pz==-37500.0:
		sonidoroturamurofalso.Play(-55000.0, -1500.0, -37625.0, 0)
		sectormurofalsoint.DoBreak((0.0, 0.0, -2.5), (px, py, pz), (0.0, 0.0, 0.0))
		sectorrompemurofalsoint.OnHit=""
	if (px<=-29500+125) and (px>=-29500-125):#px==-29500.0:
		sonidoroturamurofalso.Play(-29250.0, -1500.0, 23500.0, 0)
		sectormurofalsotes.DoBreak((-2.5, 0.0, 0.0), (px, py, pz), (0.0, 0.0, 0.0))
		sectorrompemurofalsotes.OnHit=""


#################################################################################################







#################################################################################################
## Pivotes.py

def InicializaFlecha(entity_name):
	pivote=Bladex.GetEntity(entity_name)
	flecha=Flechas.FlechaController(pivote, sonidopiv)
	return flecha

def FuncPivotelab(SectorIndex,EntityName):
	global pivstop
	if EntityName=='Player1':
		lanzapivtimer.SubscribeToList("Timer025")
		pivstop=0

def FuncPivotelabStop(SectorIndex,EntityName):
	global pivstop
	if EntityName=='Player1':
		pivstop=1

def TimerFuncPivotelab(entname,time):
	global pivstop
	global ntimepiv
	ntimepiv=ntimepiv+1
	
	if ntimepiv==1:
		flechalab1.RestartArrow((0.500000,0.500000,-0.500000,-0.500000), (21436.0,-1410.0,32305.0), (30000,0,0))
	elif ntimepiv==2:
		flechalab2.RestartArrow ((0.500000,0.500000,-0.500000,-0.500000), (21436.0,-1403.0,34086.0), (30000,0,0))
	elif ntimepiv==3:
		flechalab3.RestartArrow ((0.500000,0.500000,-0.500000,-0.500000), (21436.0,-1410.0,35872.0), (30000,0,0))
	elif ntimepiv==4:
		flechalab4.RestartArrow ((0.500000,0.500000,-0.500000,-0.500000), (21436.0,-1400.0,37676.0), (30000,0,0))
	elif ntimepiv==5:
		if pivstop==1:
			flechalab1.StopArrow ((0.500000,0.500000,-0.500000,-0.500000), (20974.0,-1410.0,32305.0))
			flechalab2.StopArrow ((0.500000,0.500000,-0.500000,-0.500000), (20974.0,-1403.0,34086.0))
			flechalab3.StopArrow ((0.500000,0.500000,-0.500000,-0.500000), (20974.0,-1410.0,35872.0))
			flechalab4.StopArrow ((0.500000,0.500000,-0.500000,-0.500000), (20974.0,-1400.0,37676.0))
			
			ntimepiv=0
			pivstop=0
			lanzapivtimer.RemoveFromList("Timer025")
		else:
			flechalab1.RestartArrow ((0.500000,0.500000,-0.500000,-0.500000), (21436.0,-1410.0,32305.0), (30000,0,0))
			ntimepiv=1

def FuncPivoteint(SectorIndex,EntityName):
	if EntityName=='Player1':
		flechaint2.RestartArrow ((0.707107,-0.000000,0.707107,0.000000), (58059.863,5991.060,-61329.302), (-40000,0,0))
		flechaint4.RestartArrow ((0.707107,-0.000000,0.707107,0.000000), (58055.662,6890.940,-61325.458), (-40000,0,0))
		
		lanzapivtimer1.SubscribeToList("Timer025")

def TimerFuncPivoteint(entname,time):
	global ntimepivint
	ntimepivint=ntimepivint+1
	if ntimepivint==5:
		flechaint1.RestartArrow ((0.707107,-0.000000,0.707107,0.000000), (58052.537,6461.237,-62019.761), (-40000,0,0))
		flechaint3.RestartArrow ((0.707107,-0.000000,0.707107,0.000000), (58051.044,6457.474,-60646.428), (-40000,0,0))
	elif ntimepivint==10:
		ntimepivint=0
		flechaint1.StopArrow ((0.707107,-0.000000,0.707107,0.000000), (58500.537,6461.237,-62019.761))
		flechaint2.StopArrow ((0.707107,-0.000000,0.707107,0.000000), (58500.863,5991.060,-61329.302))
		flechaint3.StopArrow ((0.707107,-0.000000,0.707107,0.000000), (58500.044,6457.474,-60646.428))
		flechaint4.StopArrow ((0.707107,-0.000000,0.707107,0.000000), (58500.562,6890.940,-61325.458))
		
		lanzapivtimer1.RemoveFromList("Timer025")



def FuncPivotext(SectorIndex,EntityName):
	global pivextstop
	if EntityName=='Player1':
		flechaext1.RestartArrow ((0.500000,0.500000,0.500000,0.500000), (-15426.598,-1412.396,-17696.588), (-40000, 0, 0))
		flechaext2.RestartArrow ((0.707107,-0.000000,-0.000000,-0.707107), (-18382.010,-967.265,-15450.499), (0, 0, -40000))
		pivextstop=0
		lanzapivtimer2.SubscribeToList("Timer025")

def FuncPivotextStop(SectorIndex,EntityName):
	global pivextstop
	if EntityName=='Player1':
		pivextstop=1

def TimerFuncPivotext(entname,time):
	global ntimepivext
	global pivextstop
	ntimepivext=ntimepivext+1
	if ntimepivext==3:
		ntimepivext=0
		if pivextstop==1:
			flechaext1.StopArrow ((0.500000,0.500000,0.500000,0.500000), (-15000.598,-1412.396,-17696.588))
			flechaext2.StopArrow ((0.707107,-0.000000,-0.000000,-0.707107), (-18382.010,-967.265,-15000.499))
			
			pivextstop=0
			lanzapivtimer2.RemoveFromList("Timer025")
		else:
			flechaext1.RestartArrow ((0.500000,0.500000,0.500000,0.500000), (-15426.598,-1412.396,-17696.588), (-40000, 0, 0))
			flechaext2.RestartArrow ((0.707107,-0.000000,-0.000000,-0.707107), (-18382.010,-967.265,-15450.499), (0, 0, -40000))



def FuncPivotetes():
	global pivtesstop
	if pivtesstop:
		pivtesstop=0
		return
	flechates1.RestartArrow ((0.500000,0.500000,0.500000,0.500000), (-41200.0,-2100.0,45250.0), (-40000, 0, 0))
	flechates2.RestartArrow ((0.000000,0.707107,-0.707107,0.000000), (-45250.0,-1800.0,41200.0), (0, 0, 40000))
	
	lanzapivtimer3.SubscribeToList("Timer025")

def LanzaFuncPivotetes(SectorIndex,EntityName):
	if EntityName=='Player1':
		sonidoactivacionflechas.Play(-40844.0,-2100.0,45250.0,0)
		sonidoactivacionflechas.Play(-45250.0,-1800.0,40844.0,0)
		Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, FuncPivotetes, ())

def FuncPivotetesStop(SectorIndex,EntityName):
	global pivtesstop
	if EntityName=='Player1':
		pivtesstop=1

def TimerFuncPivotetes(entname,time):
	global ntimepivtes
	global pivtesstop
	ntimepivtes=ntimepivtes+1
	if ntimepivtes==3:
		ntimepivtes=0
		if pivtesstop:
			flechates1.StopArrow ((0.500000,0.500000,0.500000,0.500000), (-40750.0,-2100.0,45250.0))
			flechates2.StopArrow ((0.000000,0.707107,-0.707107,0.000000), (-45250.0,-1800.0,40750.0))
			
			pivtesstop=0
			lanzapivtimer3.RemoveFromList("Timer025")
			
		else:
			flechates1.RestartArrow ((0.500000,0.500000,0.500000,0.500000), (-41200.0,-2100.0,45250.0), (-40000, 0, 0))
			flechates2.RestartArrow ((0.000000,0.707107,-0.707107,0.000000), (-45250.0,-1800.0,41200.0), (0, 0, 40000))

#################################################################################################









#################################################################################################
## BladeTraps.py



def GiraCuchillas():
	Objects.RotateObject(cuchilla1piramidenortedin, VUELTASDURANTE, VELGIRO, VELGIRO, (0.0, 0.0, 0.0), (0, 1, 0), Objects.REL, "", "", "", "", (), GiraCuchillas, ())
	Objects.RotateObject(cuchilla2piramidenortedin, VUELTASDURANTE, VELGIRO, VELGIRO, (0.0, 0.0, 0.0), (0, 1, 0))
	Objects.RotateObject(cuchilla3piramidenortedin, VUELTASDURANTE, VELGIRO, VELGIRO, (0.0, 0.0, 0.0), (0, 1, 0))
	Objects.RotateObject(cuchilla4piramidenortedin, VUELTASDURANTE, VELGIRO, VELGIRO, (0.0, 0.0, 0.0), (0, 1, 0))

def IniciaGiraCuchillas():
	Objects.RotateObject(cuchilla1piramidenortedin, VUELTASINICIO, 0.0, VELGIRO, (0.0, 0.0, 0.0), (0, 1, 0), Objects.REL, "", "", "", "", (), GiraCuchillas, ())
	Objects.RotateObject(cuchilla2piramidenortedin, VUELTASINICIO, 0.0, VELGIRO, (0.0, 0.0, 0.0), (0, 1, 0))
	Objects.RotateObject(cuchilla3piramidenortedin, VUELTASINICIO, 0.0, VELGIRO, (0.0, 0.0, 0.0), (0, 1, 0))
	Objects.RotateObject(cuchilla4piramidenortedin, VUELTASINICIO, 0.0, VELGIRO, (0.0, 0.0, 0.0), (0, 1, 0))

def TerminaGiraCuchillas():
	Objects.RotateObject(cuchilla1piramidenortedin, VUELTASFIN, VELGIRO, 0.0, (0.0, 0.0, 0.0), (0, 1, 0))
	Objects.RotateObject(cuchilla2piramidenortedin, VUELTASFIN, VELGIRO, 0.0, (0.0, 0.0, 0.0), (0, 1, 0))
	Objects.RotateObject(cuchilla3piramidenortedin, VUELTASFIN, VELGIRO, 0.0, (0.0, 0.0, 0.0), (0, 1, 0))
	Objects.RotateObject(cuchilla4piramidenortedin, VUELTASFIN, VELGIRO, 0.0, (0.0, 0.0, 0.0), (0, 1, 0))

def LanzaCuchilla(ncuchilla):

	global tr_cuch_nor_act
	global cuchillasfuera
	if tr_cuch_nor_act==0:
		if cuchillasfuera==0:
			cuchillasfuera=-1
			cuchilla1piramidenorte.MessageEvent(MESSAGE_STOP_WEAPON,0,0)
			cuchilla2piramidenorte.MessageEvent(MESSAGE_STOP_WEAPON,0,0)
			cuchilla3piramidenorte.MessageEvent(MESSAGE_STOP_WEAPON,0,0)
			cuchilla4piramidenorte.MessageEvent(MESSAGE_STOP_WEAPON,0,0)
			sonidoactivacioncuchillas.Play(5500.0, 700.0, 40000.0, 0)
			sonidoactivacioncuchillas.Play(-5500.0, 700.0, 40000.0, 0)
			TerminaGiraCuchillas()
		return
	if ncuchilla==1:
		cuchilla1piramidenorte.MessageEvent(MESSAGE_START_WEAPON,0,0)
		Objects.DisplaceObject(cuchilla1piramidenortedin, 1850.0, (0.0, 0.0, 1.0), 6000.0, 10000.0, sonidosalidacuchilla)
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.2, RecogeCuchilla, (1,))
	elif ncuchilla==2:
		cuchilla2piramidenorte.MessageEvent(MESSAGE_START_WEAPON,0,0)
		Objects.DisplaceObject(cuchilla2piramidenortedin, 1850.0, (0.0, 0.0, -1.0), 6000.0, 10000.0, sonidosalidacuchilla)
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.6, RecogeCuchilla, (2,))
	elif ncuchilla==3:
		cuchilla3piramidenorte.MessageEvent(MESSAGE_START_WEAPON,0,0)
		Objects.DisplaceObject(cuchilla3piramidenortedin, 1850.0, (0.0, 0.0, -1.0), 6000.0, 10000.0, sonidosalidacuchilla)
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.2, RecogeCuchilla, (3,))
	else:
		cuchilla4piramidenorte.MessageEvent(MESSAGE_START_WEAPON,0,0)
		Objects.DisplaceObject(cuchilla4piramidenortedin, 1850.0, (0.0, 0.0, 1.0), 6000.0, 10000.0, sonidosalidacuchilla)
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.6, RecogeCuchilla, (4,))
	cuchillasfuera=cuchillasfuera+1

def RecogeCuchilla(ncuchilla):
	global cuchillasfuera
	if ncuchilla==1:
		Objects.DisplaceObject(cuchilla1piramidenortedin, 1850.0, (0.0, 0.0, -1.0), 10000.0, 6000.0)
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.8, LanzaCuchilla, (1,)) #1.4
	elif ncuchilla==2:
		Objects.DisplaceObject(cuchilla2piramidenortedin, 1850.0, (0.0, 0.0, 1.0), 10000.0, 6000.0)
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.2, LanzaCuchilla, (2,)) #1.7
	elif ncuchilla==3:
		Objects.DisplaceObject(cuchilla3piramidenortedin, 1850.0, (0.0, 0.0, 1.0), 10000.0, 6000.0)
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.8, LanzaCuchilla, (3,)) #1.4
	else:
		Objects.DisplaceObject(cuchilla4piramidenortedin, 1850.0, (0.0, 0.0, -1.0), 10000.0, 6000.0)
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.2, LanzaCuchilla, (4,)) #1.7
	cuchillasfuera=cuchillasfuera-1

def LanzaTrampaCuchillas():

	global tr_cuch_nor_act
	global cuchillasfuera
	tr_cuch_nor_act=1
	cuchillasfuera=0
	sector1paracuchillas.OnEnter=ParaTrampaCuchillas
	sector2paracuchillas.OnEnter=ParaTrampaCuchillas
	sonidoactivacioncuchillas.Play(5500.0, 700.0, 40000.0, 0)
	sonidoactivacioncuchillas.Play(-5500.0, 700.0, 40000.0, 0)
	IniciaGiraCuchillas()
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, LanzaCuchilla, (1,))
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, LanzaCuchilla, (2,))
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, LanzaCuchilla, (3,))
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, LanzaCuchilla, (4,))

def ParaTrampaCuchillas(sector_index, entity_name):

	global tr_cuch_nor_act
	if entity_name=="Player1":
		tr_cuch_nor_act=0
		sector1paracuchillas.OnEnter=""
		sector2paracuchillas.OnEnter=""



#################################################################################################







#################################################################################################
## Pinchos.py



def PinchoSolido(pinchos, n):
	for pincho in pinchos:
		pincho.Solid=n


def LanzaPinchos12():
	despl1=(1800.0, 250.0)
	vect1=((-1.0, 0.0, 0.0), (1.0, 0.0, 0.0))
	vel_inic1=(0.0, 7000.0)
	vel_fin1=(14000.0, 0.0)
	son_inic1=(pinchosdeslizando1, pinchosgolpeando1)
	despl2=(1800.0, 250.0)
	vect2=((1.0, 0.0, 0.0), (-1.0, 0.0, 0.0))
	vel_inic2=(0.0, 7000.0)
	vel_fin2=(14000.0, 0.0)
	son_inic2=(pinchosdeslizando2, pinchosgolpeando2)
	pinchos=(pinchopiramide1, pinchopiramide2)
	Objects.NDisplaceObject(pinchopiramide1movil, despl1, vect1, vel_inic1, vel_fin1, son_inic1, (), (), "", (), PinchoSolido, (pinchos, 1))
	Objects.NDisplaceObject(pinchopiramide2movil, despl2, vect2, vel_inic2, vel_fin2, son_inic2)
	polvopincho1=Bladex.CreateEntity("PolvoPincho1", "Entity Particle System D1", 41510.0, 1190.0, 7150.0)
	polvopincho1.ParticleType="MediumDust"
	polvopincho1.YGravity=0.0
	polvopincho1.Friction=0.2
	polvopincho1.PPS=60
	polvopincho1.Velocity=-2000.0, 0.0, 0.0
	polvopincho1.RandomVelocity=40.0
	polvopincho1.Time2Live=64
	polvopincho1.DeathTime=Bladex.GetTime()+4.0/60.0
	polvopincho2=Bladex.CreateEntity("PolvoPincho2", "Entity Particle System D1", 38470.0, 300.0, 7150.0)
	polvopincho2.ParticleType="MediumDust"
	polvopincho2.YGravity=0.0
	polvopincho2.Friction=0.2
	polvopincho2.PPS=60
	polvopincho2.Velocity=2000.0, 0.0, 0.0
	polvopincho2.RandomVelocity=40.0
	polvopincho2.Time2Live=64
	polvopincho2.DeathTime=Bladex.GetTime()+4.0/60.0


def LanzaPinchos34():
	despl3=(1000.0, 350.0)
	vect3=((-1.0, 0.0, 0.0), (1.0, 0.0, 0.0))
	vel_inic3=(0.0, 5500.0)
	vel_fin3=(11000.0, 0.0)
	son_inic3=(pinchosdeslizando1, pinchosgolpeando1)
	despl4=(1000.0, 350.0)
	vect4=((1.0, 0.0, 0.0), (-1.0, 0.0, 0.0))
	vel_inic4=(0.0, 5500.0)
	vel_fin4=(11000.0, 0.0)
	son_inic4=(pinchosdeslizando2, pinchosgolpeando2)
	pinchos=(pinchopiramide3, pinchopiramide4)
	Objects.NDisplaceObject(pinchopiramide3movil, despl3, vect3, vel_inic3, vel_fin3, son_inic3, (), (), "", (), PinchoSolido, (pinchos, 1))
	Objects.NDisplaceObject(pinchopiramide4movil, despl4, vect4, vel_inic4, vel_fin4, son_inic4)
	polvopincho1=Bladex.CreateEntity("PolvoPincho1", "Entity Particle System D1", 41510.0, 1190.0, -7150.0)
	polvopincho1.ParticleType="MediumDust"
	polvopincho1.YGravity=0.0
	polvopincho1.Friction=0.2
	polvopincho1.PPS=60
	polvopincho1.Velocity=-2000.0, 0.0, 0.0
	polvopincho1.RandomVelocity=40.0
	polvopincho1.Time2Live=64
	polvopincho1.DeathTime=Bladex.GetTime()+4.0/60.0
	polvopincho2=Bladex.CreateEntity("PolvoPincho2", "Entity Particle System D1", 38470.0, 300.0, -7150.0)
	polvopincho2.ParticleType="MediumDust"
	polvopincho2.YGravity=0.0
	polvopincho2.Friction=0.2
	polvopincho2.PPS=60
	polvopincho2.Velocity=2000.0, 0.0, 0.0
	polvopincho2.RandomVelocity=40.0
	polvopincho2.Time2Live=64
	polvopincho2.DeathTime=Bladex.GetTime()+4.0/60.0



def LanzaTrampaPinchos12(sector, entity_name):
	if pinchopiramide1movil.Activado:
		clicktrampa.Play(39990.0, 745.0, 7150.0, 0)
		pinchos=(pinchopiramide1, pinchopiramide2)
		PinchoSolido(pinchos, 0)
		pinchopiramide1.MessageEvent(MESSAGE_START_WEAPON,0,0)
		pinchopiramide2.MessageEvent(MESSAGE_START_WEAPON,0,0)
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.35, LanzaPinchos12, ())
		sectorpinchos12.OnEnter=""


def LanzaTrampaPinchos34(sector, entity_name):
	if pinchopiramide1movil.Activado:
		clicktrampa.Play(39990.0, 745.0, -7150.0, 0)
		pinchos=(pinchopiramide3, pinchopiramide4)
		PinchoSolido(pinchos, 0)
		pinchopiramide3.MessageEvent(MESSAGE_START_WEAPON,0,0)
		pinchopiramide4.MessageEvent(MESSAGE_START_WEAPON,0,0)
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.35, LanzaPinchos34, ())
		sectorpinchos34.OnEnter=""


def otra():
	global LanzaTrampaPinchos12
	global LanzaTrampaPinchos34
	char.Position=46139.666, 751.5, 738.593
	pinchopiramide1.Position=42510.0, 1190.0, 7150.0
	pinchopiramide2.Position=37470.0, 300.0, 7150.0
	pinchopiramide3.Position=42510.0, 1190.0, -7150.0
	pinchopiramide4.Position=37470.0, 300.0, -7150.0
	sectorpinchos12.OnEnter=LanzaTrampaPinchos12
	sectorpinchos34.OnEnter=LanzaTrampaPinchos34
	pinchopiramide1movil.Activado=1




def ParaArenillaPuertaPiramide():

	global arenillapuertapiramide
	arenillapuertapiramide.DeathTime=Bladex.GetTime()+1.0/60.0
	if (puertapiramide.status==Doors.CLOSED):
		polvareda2=Bladex.CreateEntity("PolvoPuertaPiramide2", "Entity Particle System D2", 44500.0, 2000.0, -1250.0)
		polvareda2.D=0.0, 0.0, 2500.0
		polvareda2.ParticleType="Dust"
		polvareda2.YGravity=0.0
		polvareda2.Friction=0.2
		polvareda2.PPS=512
		polvareda2.Velocity=750.0, -700.0, 0.0
		polvareda2.RandomVelocity=10.0
		polvareda2.Time2Live=30
		polvareda2.DeathTime=Bladex.GetTime()+3.0/60.0


def AbrePuertaPiramide():

	global arenillapuertapiramide
	puertapiramide.opentype=Doors.AC_UNIF_DEC
	puertapiramide.o_init_vel=0
	puertapiramide.o_init_displ=250
	puertapiramide.o_med_vel=-1250
	puertapiramide.o_med_displ=2900
	puertapiramide.o_end_vel=0
	puertapiramide.o_end_displ=100
	puertapiramide.opened_displ=350
	arenillapuertapiramide=Bladex.CreateEntity("ArenillaPuertaPiramide", "Entity Particle System D2", 44500.0, -1500.0, -435.0)
	arenillapuertapiramide.D=0.0, 0.0, 870.0
	arenillapuertapiramide.ParticleType="Sand"
	arenillapuertapiramide.YGravity=4900.0
	arenillapuertapiramide.Friction=0.2
	arenillapuertapiramide.RandomVelocity=10.0
	arenillapuertapiramide.PPS=512
	arenillapuertapiramide.Time2Live=32
	puertapiramide.OnEndOpenFunc=ParaArenillaPuertaPiramide
	puertapiramide.SetInitOpenSound(puertapiabr)
	puertapiramide.OpenDoor()
	pinchopiramide1movil.Activado=1


def CierraPuertaPiramide3():

	puertapiramide.c_init_vel=0
	puertapiramide.c_init_displ=250
	puertapiramide.c_med_vel=1500
	puertapiramide.OnEndCloseFunc=ParaArenillaPuertaPiramide
	puertapiramide.InitCloseSound=""
	puertapiramide.CloseDoor()


def CierraPuertaPiramide2():

	puertapiramide.opentype=Doors.DEC
	puertapiramide.o_med_vel=-2000
	puertapiramide.o_end_displ=250
	puertapiramide.o_end_vel=0
	puertapiramide.opened_displ=puertapiramide.closed_displ-puertapiramide.o_end_displ
	puertapiramide.OnEndOpenFunc=CierraPuertaPiramide3
	polvareda1=Bladex.CreateEntity("PolvoPuertaPiramide1", "Entity Particle System D2", 44500.0, 2000.0, -1250.0)
	polvareda1.D=0.0, 0.0, 2500.0
	polvareda1.ParticleType="MediumDust"
	polvareda1.YGravity=0.0
	polvareda1.Friction=0.2
	polvareda1.PPS=512
	polvareda1.Velocity=1000.0, -1000.0, 0.0
	polvareda1.RandomVelocity=30.0
	polvareda1.Time2Live=30
	polvareda1.DeathTime=Bladex.GetTime()+3.0/60.0
	puertapiramide.InitOpenSound=""
	puertapiramide.OpenDoor()


def CierraPuertaPiramide():

	global arenillapuertapiramide
	puertapiramide.c_init_vel=0
	puertapiramide.c_init_displ=3250
	puertapiramide.c_med_vel=4100
	arenillapuertapiramide=Bladex.CreateEntity("ArenillaPuertaPiramide", "Entity Particle System D2", 44500.0, -1500.0, -435.0)
	arenillapuertapiramide.D=0.0, 0.0, 870.0
	arenillapuertapiramide.ParticleType="Sand"
	arenillapuertapiramide.YGravity=4900.0
	arenillapuertapiramide.Friction=0.2
	arenillapuertapiramide.RandomVelocity=10.0
	arenillapuertapiramide.PPS=512
	arenillapuertapiramide.Time2Live=32
	puertapiramide.OnEndCloseFunc=CierraPuertaPiramide2
	puertapiramide.SetInitCloseSound(puertapicerr)
	puertapiramide.CloseDoor()


def SaltaTierra(x, y, z):
	tierra=Bladex.CreateEntity("TierraSaltando", "Entity Particle System D1", x, y, z)
	tierra.ParticleType="Tierra"
	tierra.PPS=512
	tierra.YGravity=9800.0
	tierra.Friction=0.05
	tierra.Velocity=0.0, -750.0, 0.0
	tierra.RandomVelocity=100.0
	tierra.Time2Live=120
	tierra.DeathTime=Bladex.GetTime()+15.0/60.0

def RompeHuecoIzq():
	sonidoroturahueco.Play(65875.0, 0.0, 20375.0,0)
	sector1borpinizq.Active=1
	sector2borpinizq.Active=1
	sector3borpinizq.Active=1
	sector4borpinizq.Active=1
	sector5borpinizq.Active=1
	sector1pinizq.DoBreak((0.5, -1.0, 0.5), (65875.0, 0.0, 20375.0), (0.0, 0.0, 0.0))
	sector2pinizq.DoBreak((-0.75, -1.0, 0.0), (65875.0, 0.0, 20375.0), (0.0, 0.0, 0.0))
	sector3pinizq.DoBreak((0.25, -1.0, -0.75), (65875.0, 0.0, 20375.0), (0.0, 0.0, 0.0))
	SaltaTierra(65875.0, 0.0, 20375.0)

def RompeHuecoDer():
	sonidoroturahueco.Play(67000.0, 0.0, 20375.0,0)
	sector1borpinder.Active=1
	sector2borpinder.Active=1
	sector3borpinder.Active=1
	sector4borpinder.Active=1
	sector5borpinder.Active=1
	sector1pinder.DoBreak((0.0, -1.0, 0.75), (67000.0, 0.0, 20375.0), (0.0, 0.0, 0.0))
	sector2pinder.DoBreak((-0.5, -1.0, -0.5), (67000.0, 0.0, 20375.0), (0.0, 0.0, 0.0))
	sector3pinder.DoBreak((0.75, -1.0, -0.25), (67000.0, 0.0, 20375.0), (0.0, 0.0, 0.0))
	SaltaTierra(67000.0, 0.0, 20375.0)

def Solidifica(pincho):
	pincho.Solid=1

def RecogePinchoIzq():
	Objects.DisplaceObject(pincholabizqdin, 2750.0, (0.0, 1.0, 0.0), 10000.0, 20000.0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, LanzaPinchoIzq, ())

def LanzaPinchoIzq():
	global pinchoslabactivados
	if pinchoslabactivados:
		pincholabizq.Solid=0
		pincholabizq.MessageEvent(MESSAGE_START_WEAPON,0,0)
		Objects.DisplaceObject(pincholabizqdin, 2750.0, (0.0, -1.0, 0.0), 10000.0, 20000.0, sonidopinchosaliendo, "", pinchosgolpeando1, "", (), Solidifica, (pincholabizq,))
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, RecogePinchoIzq, ())

def RecogePinchoDer():
	Objects.DisplaceObject(pincholabderdin, 2750.0, (0.0, 1.0, 0.0), 10000.0, 20000.0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, LanzaPinchoDer, ())

def LanzaPinchoDer():
	global pinchoslabactivados
	if pinchoslabactivados:
		pincholabder.Solid=0
		pincholabder.MessageEvent(MESSAGE_START_WEAPON,0,0)
		Objects.DisplaceObject(pincholabderdin, 2750.0, (0.0, -1.0, 0.0), 10000.0, 20000.0, sonidopinchosaliendo, "", pinchosgolpeando1, "", (), Solidifica, (pincholabder,))
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, RecogePinchoDer, ())

def ParaPinchosLab(sector_index, entity_name):
	global pinchoslabactivados
	if entity_name=="Player1":
		sectorlanzapinchoslab.OnWalkOn=LanzaPinchosLab
		sector1guardapinchoslab.OnEnter=""
		sector2guardapinchoslab.OnEnter=""
		pinchoslabactivados=0

def LanzaPinchosLab(sector_index, entity_name):
	global pinchoslabactivados
	global huecopinchoslabcerrado
	if entity_name=="Player1":
		sectorlanzapinchoslab.OnWalkOn=""
		sector1guardapinchoslab.OnEnter=ParaPinchosLab
		sector2guardapinchoslab.OnEnter=ParaPinchosLab
		pinchoslabactivados=1
		if huecopinchoslabcerrado:
			RompeHuecoIzq()
			Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, RompeHuecoDer, ())
			huecopinchoslabcerrado=0
		LanzaPinchoIzq()
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, LanzaPinchoDer, ())




#################################################################################################







#################################################################################################
## Flame.py



def EnciendeLuzLlamGrad(ent_name, time):
	luzllamarada=Bladex.GetEntity(ent_name)
	luzllamarada.Intensity=luzllamarada.Intensity+0.2
	if luzllamarada.Intensity>=4.0:
		luzllamarada.RemoveFromList("Timer60")
		luzllamarada.TimerFunc=""

def EnciendeLuzLlamarada(flame_n):
	luzllamarada=Bladex.GetEntity("LuzLlamarada"+`flame_n`)
	luzllamarada.Intensity=0.0
	luzllamarada.TimerFunc=EnciendeLuzLlamGrad
	luzllamarada.SubscribeToList("Timer60")

def ApagaLuzLlamGrad(ent_name, time):
	luzllamarada=Bladex.GetEntity(ent_name)
	luzllamarada.Intensity=luzllamarada.Intensity-0.2
	if luzllamarada.Intensity<=0.0:
		luzllamarada.RemoveFromList("Timer60")

def ApagaLuzLlamarada(flame_n):
	luzllamarada=Bladex.GetEntity("LuzLlamarada"+`flame_n`)
	luzllamarada.Intensity=4.0
	luzllamarada.TimerFunc=ApagaLuzLlamGrad
	luzllamarada.SubscribeToList("Timer60")

def LanzaSurtidor(flame_n):
	global llamaradasactivadas
	global des
	global chllama1
	global chllama2
	if des>0:
		des=des-1
		return
	if llamaradasactivadas:
		llamarada=Bladex.CreateEntity("Llamarada"+`flame_n`, "Entity Particle System D1", 46000.0+(flame_n-1)*5000.0, -4250.0, -36450.0)
		llamarada.ParticleType="Flame"
		llamarada.YGravity=-4900.0
		llamarada.Friction=0.12
		llamarada.PPS=512
		llamarada.Velocity=0.0, 5000.0, 16000.0
		llamarada.RandomVelocity=40.0
		llamarada.Time2Live=21
		llamarada.DeathTime=Bladex.GetTime()+0.75
		sonidollamarada.Play(46000.0+(flame_n-1)*5000.0, -3500.0, -33000.0,0)
		EnciendeLuzLlamarada(flame_n)
		if flame_n==1:
			chllama1.startCheck(llamarada, 0.72)
		else:
			chllama2.startCheck(llamarada, 0.72)
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.75, ApagaLuzLlamarada, (flame_n,))
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, LanzaSurtidor, (flame_n,))

def LanzaTrampaLlamas(sec_index, ent_name):
	global llamaradasactivadas
	if ent_name=="Player1":
		llamaradasactivadas=1
		sonidoactivacionllamaradas.Play(46000.0, -4250.0, -36450.0,0)
		sonidoactivacionllamaradas.Play(51000.0, -4250.0, -36450.0,0)
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.25, LanzaSurtidor, (1,))
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, LanzaSurtidor, (2,))

def ParaTrampaLlamas(sec_index, ent_name):
	global llamaradasactivadas
	global des
	if ent_name=="Player1":
		llamaradasactivadas=0
		des=des+2


def FlameDamage(prtl_name,hit_entity,x,y,z,vx,vy,vz,wcx,wcy,wcz,wdx,wdy,wdz):
	ent=Bladex.GetEntity(hit_entity)
	if ent and ent.Person:
		if ent.Life>0:
			Reference.EntitiesObjectData[prtl_name]= [Reference.OBJ_WEAPON, 0, 0,  1.0,  Reference.THR_STRAIGHT, Reference.W_FLAG_1H, ["Fire", +5.0]]
			ent.DamageFunc(hit_entity, "", prtl_name, "Fire", 1, -1, x, y, z, 0)
			if Reference.EntitiesObjectData.has_key(prtl_name):
				del Reference.EntitiesObjectData[prtl_name]
			ent.Wuea=Reference.WUEA_ENDED
			ent.InterruptCombat()
			ent.LaunchAnmType("hurt_f_big")



#################################################################################################






#################################################################################################
## Pozo.py



def AbrePuertaF3():
	puertaf3golpe.Volume=0.4
	puertaf3.OpenDoor()

def CierraPuertaF3():
	puertaf3golpe.Volume=0.6
	puertaf3.CloseDoor()



def LucesRayos(): #OJO!! Las luces son Rayo1Luz1, Rayo1Luz2, Rayo3Luz1, Rayo3Luz2, Rayo5Luz1, Rayo5Luz2, Rayo7Luz1, Rayo7Luz2
	for i in range(4):
		rayo=Bladex.GetEntity("Rayo"+`2*i+1`)
		if i==0 or i==2:
			xvar=0.0
			zvar=1500.0
		else:
			xvar=1500.0
			zvar=0.0
		for j in range(2):
			if j==0:
				luzrayo=Bladex.CreateEntity(rayo.Name+"Luz"+`j+1`, "Entity Spot", rayo.Position[0]+xvar, -1500.0, rayo.Position[2]-zvar)
			else:
				luzrayo=Bladex.CreateEntity(rayo.Name+"Luz"+`j+1`, "Entity Spot", rayo.Target[0]-xvar, -1500.0, rayo.Target[2]+zvar)
			luzrayo.Color=100, 100, 220
			luzrayo.Intensity=3
			luzrayo.Precission=0.2 #0.03125
			luzrayo.Visible=0
			luzrayo.CastShadows=0

def PartLimber(PersonName,idx):
	char = Bladex.GetEntity(PersonName)
	if char:
		if idx == 1:
		        o = char.SeverLimb(1)
		        if o: o.Impulse(0,-10000,0)
		if idx == 2:
		        o = char.SeverLimb(2)
		        if o: o.Impulse(-10000*math.cos(char.Angle),-10000,-10000*math.sin(char.Angle))
		if idx == 4:
		        o = char.SeverLimb(4)
		        if o: o.Impulse(10000*math.cos(char.Angle),-10000,10000*math.sin(char.Angle))
		if idx == 6:
		        o = char.SeverLimb(6)
		        if o: o.Impulse(-10000*math.cos(char.Angle),-10000,-10000*math.sin(char.Angle))
		if idx == 8:
		        o = char.SeverLimb(8)
		        if o: o.Impulse(10000*math.cos(char.Angle),-10000,10000*math.sin(char.Angle))


def MuerteBarreraMagica(trsector_name, entity_name):
	pers=Bladex.GetEntity(entity_name)
	if pers and pers.Person:
		x, y, z=pers.Position
		rayo=Bladex.CreateEntity("RayoMuerte", "Entity ElectricBolt", x, y-700.0, z)
		rayo.Position=x, y-700.0, z
		rayo.Target=x, y+1100.0, z
		rayo.MaxAmplitude=500.0
		rayo.MinSectorLength=10000.0
		rayo.Damage=0
		rayo.Active=1
		chispas=Bladex.CreateEntity("ChispasMuerte", "Entity Particle System D2", x, y-700.0, z)
		chispas.D=0.0, 1800.0, 0.0
		chispas.ParticleType="ChispasM"
		chispas.PPS=3000
		chispas.YGravity=4900.0
		chispas.Friction=0.01
		chispas.RandomVelocity=50.0
		chispas.Time2Live=20
		chispas.DeathTime=Bladex.GetTime()+8.0/60.0
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, rayo.SubscribeToList, ("Pin",))
		pers.Life=0
		#pers.Wuea=Reference.WUEA_ENDED
		#pers.SetTmpAnmFlags(1,1,1,0,5,1)
		#pers.LaunchAnmType("dth_n02")
		#Bladex.AddScheduledFunc(Bladex.GetTime()+0.25, PartLimber, (entity_name,1))
		#Bladex.AddScheduledFunc(Bladex.GetTime()+0.50, PartLimber, (entity_name,2))
		#Bladex.AddScheduledFunc(Bladex.GetTime()+0.75, PartLimber, (entity_name,4))
		#Bladex.AddScheduledFunc(Bladex.GetTime()+1.00, PartLimber, (entity_name,6))
		#Bladex.AddScheduledFunc(Bladex.GetTime()+1.25, PartLimber, (entity_name,8))


def ReiniciaCamaraInfPozo():
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Bladex.SetListenerPosition(1)
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)

def LanzaCamaraInfPozo(sector_index, entity_name):
	if entity_name=="Player1":
		DescongelaEnemigos(("OrkF3", "Beej1", "Beej2", "Beej3", "Beej4", "Beej5", "Beej6"))
		secdesactcamara.OnEnter=""
		secactcamara.OnEnter=""
		ScriptSkip.SkipScriptStart("EscenaCamaraInfPozo")
		#Bladex.DeactivateInput()
		Scorer.SetVisible(0)
		Bladex.SetListenerPosition(2)
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("puerta_laberinto_y_pozo"))
		AuxFuncs.MoveCamFromTo(48000.0, 8000.0, -50000.0, 52000.0, -16000.0, -53500.0, 49000.0, 7000.0, -40500.0, 47000.0, 14000.0, -46000.0, 12.0)
		Bladex.AddScheduledFunc(Bladex.GetTime()+13.0, ReiniciaCamaraInfPozo, ())
		Bladex.GetEntity("OrkF3").Angle=3.0*3.14159/4.0

def DesactivaCamaraInfPozo(sector_index, entity_name):
	if entity_name=="Player1":
		secdesactcamara.OnEnter=""
		secactcamara.OnEnter=""


def ReiniciaCamara():
	global despiertaorcos
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Bladex.SetListenerPosition(1)
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)
	if despiertaorcos:
		despiertaorcos=0
		orc1=Bladex.GetEntity("Ork1F12")
		orc2=Bladex.GetEntity("Ork2F12")
		orc1.PutToWorld()
		orc1.UnFreeze()
		orc1.Angle=3.14159
		orc2.PutToWorld()
		orc2.UnFreeze()
		orc2.Angle=-3.14159/2.0
		desplazamientos=(2250.0, 750.0)
		vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
		vel_iniciales=(500.0, 2000)
		vel_finales=(2000.0, 500)
		son_durante=(snddeslizrastrpozo, snddeslizrastrpozo)
		son_finales=("", sndgolperastrpozo)
		Objects.NDisplaceObject(rastrpozodin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


def ActivaPalancaPozo(n):
	if n==1:
		palancapozo12.TurnOn()
		sonidopalanca.Play(46150.0,2500.0,-48980.0,0)
	else:
		palancapozo3.TurnOn()
		sonidopalanca.Play(50850.0,2500.0,-48980.0,0)

def EspumaCascada(n):
	if n==1:
		espuma=Bladex.CreateEntity("EspumaCascada12", "Entity Particle System D2", 46800.0, 10990.0, -48400.0)
		salpique=Bladex.CreateEntity("SalpiqueCascada12", "Entity Particle System D2", 46800.0, 10990.0, -48400.0)
	else:
		espuma=Bladex.CreateEntity("EspumaCascada3", "Entity Particle System D2", 50200.0, 10990.0, -48400.0)
		salpique=Bladex.CreateEntity("SalpiqueCascada3", "Entity Particle System D2", 50200.0, 10990.0, -48400.0)
	espuma.D=0.0, 0.0, -1200.0
	espuma.ParticleType="Espuma"
	espuma.PPS=256
	espuma.YGravity=0.0
	espuma.Friction=0.07
	espuma.Velocity=0.0, -1000.0, 0.0
	espuma.RandomVelocity=30.0
	espuma.RandomVelocity_V=30.0
	espuma.Time2Live=10
	salpique.D=0.0, 0.0, -1200.0
	salpique.ParticleType="Salpique"
	salpique.PPS=512
	salpique.YGravity=4900.0
	salpique.Friction=0.07
	salpique.Velocity=0.0, -3000.0, 0.0
	salpique.RandomVelocity=30.0
	salpique.RandomVelocity_V=30.0
	salpique.Time2Live=25

def SalpiquePalanca(n):
	if n==1:
		salpique=Bladex.CreateEntity("SalpiquePalanca12", "Entity Particle System D1", 46450.0,2700.0,-48980.0)
		salpique.Velocity=2000.0, -2000.0, 0.0
	else:
		salpique=Bladex.CreateEntity("SalpiquePalanca3", "Entity Particle System D1", 50550.0,2700.0,-48980.0)
		salpique.Velocity=-2000.0, -2000.0, 0.0
	salpique.ParticleType="Salpique"
	salpique.PPS=128
	salpique.YGravity=4900.0
	salpique.Friction=0.07
	salpique.RandomVelocity=20.0
	salpique.Time2Live=30


def SaltaChispas(n):
	rayo=Bladex.GetEntity("Rayo"+`n`)
	if n==1 or n==2 or n==5 or n==6:
		xvar=0.0
		zvar=4000.0
	else:
		xvar=4000.0
		zvar=0.0
	for j in range(2):
		if j==0:
			chispas=Bladex.CreateEntity(rayo.Name+"Chispas1", "Entity Particle System D1", rayo.Position[0], rayo.Position[1], rayo.Position[2])
			chispas.Velocity=xvar, 0.0, -zvar
		else:
			chispas=Bladex.CreateEntity(rayo.Name+"Chispas2", "Entity Particle System D1", rayo.Target[0], rayo.Target[1], rayo.Target[2])
			chispas.Velocity=-xvar, 0.0, zvar
		chispas.ParticleType="Chispas"
		chispas.PPS=1024
		chispas.YGravity=4900.0
		chispas.Friction=0.01
		chispas.RandomVelocity=60.0
		chispas.Time2Live=20
		chispas.DeathTime=Bladex.GetTime()+4.0/60.0

def QuitaLuzGradual(ent_name, time):
	luzrayo=Bladex.GetEntity(ent_name)
	luzrayo.Intensity=luzrayo.Intensity-0.05
	if luzrayo.Intensity<=0.0:
		luzrayo.RemoveFromList("Timer60")
		luzrayo.TimerFunc=""
		luzrayo.SubscribeToList("Pin")

def QuitaRayo(n):
	rayo=Bladex.GetEntity("Rayo"+`n`)
	rayo.Active=0
	SaltaChispas(n)
	if n==2 or n==3 or n==5 or n==8:
		if n%2==0:
			n=n-1
		luzrayo1=Bladex.GetEntity("Rayo"+`n`+"Luz1")
		luzrayo1.TimerFunc=QuitaLuzGradual
		luzrayo1.SubscribeToList("Timer60")
		luzrayo2=Bladex.GetEntity("Rayo"+`n`+"Luz2")
		luzrayo2.TimerFunc=QuitaLuzGradual
		luzrayo2.SubscribeToList("Timer60")
	sonidoringpozo.Volume=max(0.0, sonidoringpozo.Volume-0.1) #0.8/8.0
	rayo.SubscribeToList("Pin")

def QuitaBarreraMagica():
	secdesactcamara.OnEnter=""
	secactcamara.OnEnter=""
	Bladex.RemoveTriggerSectorFunc("BarreraMagica", "OnEnter")
	cam=Bladex.GetEntity("Camera")
	cam.SType=0
	cam.TType=0
	cam.Position=37300.0, -6150.0, -44200.0
	cam.TPos=45000.0, -1500.0, -48400.0
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, ReiniciaCamara, ())
	orden=[1,6,4,7,2,5,3,8]
	for i in range(8):
		Bladex.AddScheduledFunc(Bladex.GetTime()+i/2.0, QuitaRayo, (orden[i],))


def ArranqueFuentes12():
	surtidoraguaa1=Bladex.CreateEntity("SurtidorAguaa1", "Entity Particle System D2", 23750.0, -2575.0, -43100.0)
	surtidoraguaa1.D=0.0, 0.0, 200.0
	surtidoraguaa1.ParticleType="Agua"
	surtidoraguaa1.PPS=512
	surtidoraguaa1.YGravity=0.0
	surtidoraguaa1.Friction=0.0
	surtidoraguaa1.Velocity=2000.0, 1000.0, 0.0
	surtidoraguaa1.Time2Live=12
	surtidoraguaa2=Bladex.CreateEntity("SurtidorAguaa2", "Entity Particle System D2", 23750.0, -2575.0, -55100.0)
	surtidoraguaa2.D=0.0, 0.0, 200.0
	surtidoraguaa2.ParticleType="Agua"
	surtidoraguaa2.PPS=512
	surtidoraguaa2.YGravity=0.0
	surtidoraguaa2.Friction=0.0
	surtidoraguaa2.Velocity=2000.0, 1000.0, 0.0
	surtidoraguaa2.Time2Live=12

def CaidaFuentes12():
	surtidoraguab1=Bladex.CreateEntity("SurtidorAguab1", "Entity Particle System D2", 24450.0, -2200.0, -43100.0)
	surtidoraguab1.D=0.0, 0.0, 200.0
	surtidoraguab1.ParticleType="Agua"
	surtidoraguab1.PPS=512
	surtidoraguab1.YGravity=9800.0
	surtidoraguab1.Friction=0.2
	surtidoraguab1.Velocity=2000.0, 1000.0, 0.0
	surtidoraguab1.Time2Live=23
	surtidoraguab2=Bladex.CreateEntity("SurtidorAguab2", "Entity Particle System D2", 24450.0, -2200.0, -55100.0)
	surtidoraguab2.D=0.0, 0.0, 200.0
	surtidoraguab2.ParticleType="Agua"
	surtidoraguab2.PPS=512
	surtidoraguab2.YGravity=9800.0
	surtidoraguab2.Friction=0.2
	surtidoraguab2.Velocity=2000.0, 1000.0, 0.0
	surtidoraguab2.Time2Live=23


def SubeAguaFuentes12(ent_name, time):
	global nivelagua12
	agua12=Bladex.GetEntity("Agua12")
	nivelagua12=nivelagua12-1.0
	agua12.Position=24875.0, nivelagua12, -49000.0
	if nivelagua12<=-801.0:
		agua12.RemoveFromList("Timer60")
		agua12.TimerFunc=""

def AguaFuentes12():
	agua12=Bladex.CreateEntity("Agua12","Entity Water",24875.0,-401.0,-49000.0)
	agua12.Reflection=-1.5
	agua12.Color=0,10,15
	agua12.TimerFunc=SubeAguaFuentes12
	agua12.SubscribeToList("Timer60")

def IniciaCamara12():
	ScriptSkip.SkipScriptStart("EscenaFuentes12")
	#Bladex.DeactivateInput()
	Scorer.SetVisible(0)
	Bladex.SetListenerPosition(2)
	cam=Bladex.GetEntity("Camera")
	cam.SType=0
	cam.TType=0
	cam.Position=28725.0, -5250.0, -40135.0
	cam.TPos=25120.0, -70.0, -47890.0

def TravellingCamara12():
	AuxFuncs.MoveCamFromTo(43000.0, -5000.0, -44000.0, 49500.0, -2000.0, -51000.0, 37500.0, 0.0, -49000.0, 46000.0, 1000.0, -49000.0, 5.0)

def CaidaCascada12():
	cascada12=Bladex.CreateEntity("Cascada12", "Entity Particle System D2", 45900.0, 170.0, -48550.0)
	cascada12.D=0.0, 0.0, -900.0
	cascada12.ParticleType="AguaC"
	cascada12.PPS=512
	cascada12.YGravity=9800.0
	cascada12.Friction=0.07
	cascada12.Velocity=1800.0, 0.0, 0.0
	cascada12.Time2Live=51

def SubeSonidoCascada12Gradual(ent_name, time):
	sonidocascada12.Volume=sonidocascada12.Volume+0.01
	if sonidocascada12.Volume>=0.99:
		palancapozo12.obj.RemoveFromList("Timer60")
		palancapozo12.obj.TimerFunc=""


def SubeAguaCanal12(ent_name, time):
	global palancasactivadas
	global nivelaguacanal12
	aguacanal12=Bladex.GetEntity("AguaCanal12")
	espumacanal12=Bladex.GetEntity("EspumaCanal12")
	nivelaguacanal12=nivelaguacanal12-0.5
	aguacanal12.Position=35250.0, nivelaguacanal12, -49000.0
	posesp=espumacanal12.Position
	espumacanal12.Position=posesp[0]+36.5, posesp[1]-0.5, posesp[2]
	espumacanal12.D=0.0, 0.0, -900.0
	if sonidocanal12.Volume<0.6:
		sonidocanal12.Volume=sonidocanal12.Volume+0.0025
	if nivelaguacanal12<=251.0:
		aguacanal12.RemoveFromList("Timer60")
		aguacanal12.TimerFunc=""
		espumacanal12.DeathTime=Bladex.GetTime()+1.0/60.0
		CaidaCascada12()
		EspumaCascada(1)
		palancapozo12.obj.TimerFunc=SubeSonidoCascada12Gradual
		palancapozo12.obj.SubscribeToList("Timer60")
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, ActivaPalancaPozo, (1,))
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, SalpiquePalanca, (1,))
		palancasactivadas=palancasactivadas+1
		if palancasactivadas==2:
			Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, QuitaBarreraMagica, ())
		else:
			Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, ReiniciaCamara, ())

def AguaCanal12():
	aguacanal12=Bladex.CreateEntity("AguaCanal12","Entity Water",35250.0,380.0,-49000.0)
	aguacanal12.Reflection=-1.5
	aguacanal12.Color=0,10,15
	espumacanal12=Bladex.CreateEntity("EspumaCanal12", "Entity Particle System D2", 36550.0, 300.0, -48550.0)
	espumacanal12.D=0.0, 0.0, -900.0
	espumacanal12.ParticleType="AguaC"
	espumacanal12.PPS=512
	espumacanal12.YGravity=9800.0
	espumacanal12.Friction=0.07
	espumacanal12.Velocity=0.0, -1000.0, 0.0
	espumacanal12.RandomVelocity=20.0
	espumacanal12.Time2Live=10
	aguacanal12.TimerFunc=SubeAguaCanal12
	aguacanal12.SubscribeToList("Timer60")
	TravellingCamara12()

def LanzaFuentes12():
	global despiertaorcos
	despiertaorcos=1
	sonidopalanca.Play(24020.0,-2250.0,-49000.0,0)
	IniciaCamara12()
	ArranqueFuentes12()
	aguafuente1.Play(24450.0, -2200.0, -43000.0, -1)
	aguafuente2.Play(24450.0, -2200.0, -55000.0, -1)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.35, CaidaFuentes12, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.85, AguaFuentes12, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+7.0, AguaCanal12, ())


def ArranqueFuente3():
	surtidoraguaa3=Bladex.CreateEntity("SurtidorAguaa3", "Entity Particle System D2", 67500.0, -3775.0, -48900.0)
	surtidoraguaa3.D=0.0, 0.0, -200.0
	surtidoraguaa3.ParticleType="Agua"
	surtidoraguaa3.PPS=512
	surtidoraguaa3.YGravity=0.0
	surtidoraguaa3.Friction=0.0
	surtidoraguaa3.Velocity=-1800.0, 1200.0, 0.0
	surtidoraguaa3.Time2Live=17

def CaidaFuente3():
	surtidoraguab3=Bladex.CreateEntity("SurtidorAguab3", "Entity Particle System D2", 66525.0, -3125.0, -48900.0)
	surtidoraguab3.D=0.0, 0.0, -200.0
	surtidoraguab3.ParticleType="Agua"
	surtidoraguab3.PPS=512
	surtidoraguab3.YGravity=9800.0
	surtidoraguab3.Friction=0.2
	surtidoraguab3.Velocity=-1800.0, 1200.0, 0.0
	surtidoraguab3.Time2Live=23




def SubeAguaFuente3(ent_name, time):
	global nivelagua3
	agua3=Bladex.GetEntity("Agua3")
	nivelagua3=nivelagua3-1.0
	agua3.Position=65500.0, nivelagua3, -49000.0
	if nivelagua3<=-1951.0:
		agua3.RemoveFromList("Timer60")
		agua3.TimerFunc=""

def AguaFuente3():
	agua3=Bladex.CreateEntity("Agua3","Entity Water",65500.0,-1651.0,-49000.0)
	agua3.Reflection=-1.5
	agua3.Color=0,10,15
	agua3.TimerFunc=SubeAguaFuente3
	agua3.SubscribeToList("Timer60")

def IniciaCamara3():
	ScriptSkip.SkipScriptStart("EscenaFuente3")
	#Bladex.DeactivateInput()
	Scorer.SetVisible(0)
	Bladex.SetListenerPosition(2)
	cam=Bladex.GetEntity("Camera")
	cam.SType=0
	cam.TType=0
	cam.Position=61665.0, -6110.0, -45020.0
	cam.TPos=64890.0, -2745.0, -53870.0

def TravellingCamara3():
	AuxFuncs.MoveCamFromTo(54000.0, -5000.0, -54000.0, 47500.0, -2000.0, -47000.0, 59500.0, 0.0, -49000.0, 51000.0, 1000.0, -49000.0, 5.0)

def CaidaCascada3():
	cascada3=Bladex.CreateEntity("Cascada3", "Entity Particle System D2", 51100.0, 170.0, -48550.0)
	cascada3.D=0.0, 0.0, -900.0
	cascada3.ParticleType="AguaC"
	cascada3.PPS=512
	cascada3.YGravity=9800.0
	cascada3.Friction=0.07
	cascada3.Velocity=-1800.0, 0.0, 0.0
	cascada3.Time2Live=51

def SubeSonidoCascada3Gradual(ent_name, time):
	sonidocascada3.Volume=sonidocascada3.Volume+0.01
	if sonidocascada3.Volume>=0.99:
		palancapozo3.obj.RemoveFromList("Timer60")
		palancapozo3.obj.TimerFunc=""




def SubeAguaCanal3(ent_name, time):
	global palancasactivadas
	global nivelaguacanal3
	aguacanal3=Bladex.GetEntity("AguaCanal3")
	espumacanal3=Bladex.GetEntity("EspumaCanal3")
	nivelaguacanal3=nivelaguacanal3-0.5
	aguacanal3.Position=61750.0, nivelaguacanal3, -49000.0
	posesp=espumacanal3.Position
	espumacanal3.Position=posesp[0]-36.5, posesp[1]-0.5, posesp[2]
	espumacanal3.D=0.0, 0.0, -900.0
	if sonidocanal3.Volume<0.6:
		sonidocanal3.Volume=sonidocanal3.Volume+0.0025
	if nivelaguacanal3<=251.0:
		aguacanal3.RemoveFromList("Timer60")
		aguacanal3.TimerFunc=""
		espumacanal3.DeathTime=Bladex.GetTime()+1.0/60.0
		CaidaCascada3()
		EspumaCascada(3)
		palancapozo3.obj.TimerFunc=SubeSonidoCascada3Gradual
		palancapozo3.obj.SubscribeToList("Timer60")
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, ActivaPalancaPozo, (3,))
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, SalpiquePalanca, (3,))
		palancasactivadas=palancasactivadas+1
		if palancasactivadas==2:
			Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, QuitaBarreraMagica, ())
		else:
			Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, ReiniciaCamara, ())

def AguaCanal3():
	aguacanal3=Bladex.CreateEntity("AguaCanal3","Entity Water",61750.0,380.0,-49000.0)
	aguacanal3.Reflection=-1.5
	aguacanal3.Color=0,10,15
	espumacanal3=Bladex.CreateEntity("EspumaCanal3", "Entity Particle System D2", 60450.0, 300.0, -48550.0)
	espumacanal3.D=0.0, 0.0, -900.0
	espumacanal3.ParticleType="AguaC"
	espumacanal3.PPS=512
	espumacanal3.YGravity=9800.0
	espumacanal3.Friction=0.07
	espumacanal3.Velocity=0.0, -1000.0, 0.0
	espumacanal3.RandomVelocity=20.0
	espumacanal3.Time2Live=10
	aguacanal3.TimerFunc=SubeAguaCanal3
	aguacanal3.SubscribeToList("Timer60")
	TravellingCamara3()

def LanzaFuente3():
	sonidopalanca.Play(64007.415,-3250.0,-54963.836,0)
	IniciaCamara3()
	ArranqueFuente3()
	aguafuente3.Play(66525.0, -3125.0, -49000.0, -1)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, CaidaFuente3, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, AguaFuente3, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+4.0, AguaCanal3, ())






#################################################################################################






#################################################################################################
## Mausoleo.py





def RompePuertaMaus():
	sonidoroturamurofalso1.Play(-45500.0, -2750.0, -43500.0, 0)
	puertamau1.DoBreak((0.6, 0.0, 0.6), (-46375.0, -3500.0, -42625.0), (0.0, 0.0, 0.0))
	puertamau2.DoBreak((0.8, 0.0, 0.8), (-46125.0, -3500.0, -42875.0), (0.0, 0.0, 0.0))
	puertamau3.DoBreak((1.0, 0.0, 1.0), (-45937.5, -3500.0, -43062.5), (0.0, 0.0, 0.0))
	puertamau4.DoBreak((1.0, 0.0, 1.0), (-45562.5, -3500.0, -43437.5), (0.0, 0.0, 0.0))
	puertamau5.DoBreak((0.8, 0.0, 0.8), (-45000.0, -3500.0, -44000.0), (0.0, 0.0, 0.0))
	puertamau6.DoBreak((0.6, 0.0, 0.6), (-44625.0, -3500.0, -44375.0), (0.0, 0.0, 0.0))
	puertamau7.DoBreak((0.6, 0.0, 0.6), (-44625.0, -2000.0, -44375.0), (0.0, 0.0, 0.0))
	#puertamau1.DoBreak((1.5, 0.0, 1.5), (-46375.0, -3500.0, -42625.0), (0.0, 0.0, 0.0))
	#puertamau2.DoBreak((2.0, 0.0, 2.0), (-46125.0, -3500.0, -42875.0), (0.0, 0.0, 0.0))
	#puertamau3.DoBreak((2.5, 0.0, 2.5), (-45937.5, -3500.0, -43062.5), (0.0, 0.0, 0.0))
	#puertamau4.DoBreak((2.5, 0.0, 2.5), (-45562.5, -3500.0, -43437.5), (0.0, 0.0, 0.0))
	#puertamau5.DoBreak((2.0, 0.0, 2.0), (-45000.0, -3500.0, -44000.0), (0.0, 0.0, 0.0))
	#puertamau6.DoBreak((1.5, 0.0, 1.5), (-44625.0, -3500.0, -44375.0), (0.0, 0.0, 0.0))
	#puertamau7.DoBreak((1.5, 0.0, 1.5), (-44625.0, -2000.0, -44375.0), (0.0, 0.0, 0.0))
	#puertamau1.Active=1
	#puertamau2.Active=1
	#puertamau3.Active=1
	#puertamau4.Active=1
	#puertamau5.Active=1
	#puertamau6.Active=1
	#puertamau7.Active=1

def RompeLosa():
	sonidoroturamurofalso2.Play(-49875.0, -2750.0, -47875.0, 0)
	tumba1.DoBreak((-0.1, -0.65, 0.1), (-50000.0, -2750.0, -47750.0), (0.0, 0.0, 0.0))
	tumba2.DoBreak((0.2, -0.65, 0.1), (-49250.0, -2750.0, -47500.0), (0.0, 0.0, 0.0))
	tumba3.DoBreak((0.1, -0.65, -0.1), (-49750.0, -2750.0, -48125.0), (0.0, 0.0, 0.0))
	tumba4.DoBreak((-0.2, -0.65, -0.1), (-50500.0, -2750.0, -48375.0), (0.0, 0.0, 0.0))
	#tumba1.Active=1
	#tumba2.Active=1
	#tumba3.Active=1
	#tumba4.Active=1

def ReiniciaCamaraMaus():
	luzfarolmaus.Precission=0.03125
	cam=Bladex.GetEntity("Camera")
	Bladex.SetListenerPosition(1)
	cam.SetPersonView("Player1")
	cam.Cut()
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)
	Bladex.SetTriggerSectorFunc("enc1_entrada_princ_lab", "OnEnter", EnciendeMusicaExteriorDespues)
	Bladex.SetTriggerSectorFunc("enc1_puerta_piramide", "OnEnter", EnciendeMusicaExteriorDespues)
	Bladex.SetTriggerSectorFunc("enc1_entrada_fuentes", "OnEnter", EnciendeMusicaExteriorDespues)
	Bladex.SetTriggerSectorFunc("enc1_puerta_mausoleo", "OnEnter", EnciendeMusicaExteriorDespues)

def MueveEstela():
	estela.Position=spirit1.Position
	spirit2.Position=spirit1.Position

def MueveEstelaYTarget():
	cam=Bladex.GetEntity("Camera")
	estela.Position=spirit1.Position
	spirit2.Position=spirit1.Position
	cam.TPos=spirit1.Position

def BajaVolEspiritu(ent_name, time):
	sndespiritu=Bladex.GetEntity(ent_name)
	if sndespiritu.Volume>0.0:
		sndespiritu.Volume=max(0.0, sndespiritu.Volume-0.125) # 1.0/8.0
	else:
		sndespiritu.RemoveFromList("Timer8")
		sndespiritu.TimerFunc=""
		sndespiritu.StopSound()

def OcultaEspiritu():
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, spirit1.RemoveFromWorld, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, spirit2.RemoveFromWorld, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, estela.RemoveFromWorld, ())
	sndespiritu.TimerFunc=BajaVolEspiritu
	sndespiritu.SubscribeToList("Timer8")
	generador1.Activate()
	generador2.Activate()
	generador3.Activate()
	generador4.Activate()
	generador5.Activate()
	generador6.Activate()

def LanzaEspirituTemplo2():
	init_pos=spirit1.Position
	end_pos=1702.08343227, -13106.3289632, 951.876042692
	Objects.DisplaceObjectFromTo(spirit1din, init_pos, end_pos, 12000.0, 0.0, "", "", "", MueveEstelaYTarget, (), OcultaEspiritu)

def LanzaEspirituTemplo():
	init_pos=spirit1.Position
	end_pos=0, -13500, 0
	Objects.DisplaceObjectFromTo(spirit1din, init_pos, end_pos, 0.0, 12000.0, "", "", "", MueveEstelaYTarget, (), LanzaEspirituTemplo2)

def CamaraExtTemplo():
	cam=Bladex.GetEntity("Camera")
	init_pos=spirit1.Position
	end_pos=-21100, -19000, -11800
	AuxFuncs.MoveCamFromTo(-31240.0, -1680.0, -17850.0, -21775.0, -19570.0, 5840.0, init_pos[0], init_pos[1], init_pos[2], -6280.0, -10770.0, -19650.0, 8.0)
	cam.TType=0
	Objects.DisplaceObjectFromTo(spirit1din, init_pos, end_pos, 8000.0, 0.0, "", "", "", MueveEstelaYTarget, (), LanzaEspirituTemplo)
	Bladex.AddScheduledFunc(Bladex.GetTime()+11.0, ReiniciaCamaraMaus, ())

def ImpactoLengua(lengua):
	x, y, z = lengua.Position
	sndimplengua.Play(x, y, z, 0)
	lengua.DeathTime=Bladex.GetTime()+0.5
	conc=Bladex.CreateEntity("Concentracion"+lengua.Name[len(lengua.Name)-1:], "Entity Particle System D1", 0.0, 0.0, 0.0)
	conc.Position=x, y, z
	conc.ParticleType="Energia"
	conc.YGravity=0.0
	conc.Friction=0.0
	conc.PPS=256
	conc.Velocity=0.0, 0.0, 0.0
	conc.RandomVelocity=-30.0
	conc.Time2Live=30
	conc.DeathTime=Bladex.GetTime()+0.5



def LanzaLenguaEspiritu(lapida):
	global n_lengua
	sndlengua.PlaySound(0)
	lengua=Bladex.CreateEntity("Lengua"+`n_lengua`, "Entity Particle System D1", 0.0, 0.0, 0.0)
	lengua.ParticleType="Volutilla"
	lengua.YGravity=500.0
	lengua.Friction=0.2
	lengua.PPS=512
	lengua.Velocity=0.0, 0.0, 0.0
	lengua.RandomVelocity=30.0
	lengua.Time2Live=32
	lenguadin=Objects.CreateDinamicObject(lengua.Name)
	lenguadin.Timer="Timer30"
	Objects.DisplaceObjectFromTo(lenguadin, spirit1.Position, lapida.Position, 8000.0, 8000.0, "", "", "", "", (), ImpactoLengua, (lengua,))

def EspirituPatio():
	AuxFuncs.MoveCamFromTo(-25400.0, -8900.0, -41100.0, -35000.0, -4300.0, -48700.0, -32000.0, -3800.0, -40000.0, -35300.0, -2100.0, -38900.0, 8.0)
	RompePuertaMaus()
	estela.PPS=128
	estela.RandomVelocity=70.0
	Objects.DisplaceObject(spirit1din, 38000.0, (1.25, 0.1, 1.125), 4000.0, 4000.0, (), (), (), MueveEstela, (), CamaraExtTemplo)
	orden=[3,7,5,1,10,2,8,4,6,9]
	ntime=1.0
	for n in orden:
		lapida=Bladex.GetEntity("Lapida"+`n`)
		Bladex.AddScheduledFunc(Bladex.GetTime()+ntime, LanzaLenguaEspiritu, (lapida,))
		ntime=ntime+0.5

def LanzaEspirituPuerta():
	Objects.DisplaceObject(spirit1din, 6000.0, (1.0, 0.25, 1.0), 0.0, 5000.0, (), (), (), MueveEstela, (), EspirituPatio)

def EspirituLibre():
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, GameText.WriteText, ("M4T5",))
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("espiritu_libre")) # lanza MP3

def ElevaEspiritu():
	desplazamientos=(1500.0, 500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(500.0, 500.0)
	vel_finales=(500.0, 0.0)
	Objects.NDisplaceObject(spirit1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), (), (), MueveEstela)

def SubeVolEspiritu(ent_name, time):
	sndespiritu=Bladex.GetEntity(ent_name)
	if sndespiritu.Volume<1.0:
		sndespiritu.Volume=min(sndespiritu.Volume+0.0625, 1.0) # 1.0/16.0
	else:
		sndespiritu.RemoveFromList("Timer8")
		sndespiritu.TimerFunc=""

def ApareceEspiritu():
	spirit1.Intensity=1.0
	spirit2.Intensity=0.01
	RompeLosa()
	sndespiritu.Volume=0
	sndespiritu.PlaySound(-1)
	sndespiritu.TimerFunc=SubeVolEspiritu
	sndespiritu.SubscribeToList("Timer8")
	Bladex.AddScheduledFunc(Bladex.GetTime()+6.0, LanzaEspirituPuerta, ())
	EspirituLibre()

def ComienzaCamaraMaus():
	AuxFuncs.MoveCamFromTo(-50000.0, -5000.0, -51000.0, -54000.0, -2000.0, -48000.0, -49000.0, -2750.0, -48000.0, -49875.0, -4000.0, -47875.0, 10.0) #8.0

def BajaIntLuzMausGrad(ent_name, time):
	if luzantmaus1.Intensity<=0.1:
		luzantmaus1.Intensity=0.0
		luzantmaus2.Intensity=0.0
		luzantmaus3.Intensity=0.0
		luzantmaus4.Intensity=0.0
		fuegoantmaus1.Intensity=20.0
		fuegoantmaus2.Intensity=20.0
		fuegoantmaus3.Intensity=20.0
		fuegoantmaus4.Intensity=20.0
		antmaus1.Move(0.0,0.0,0.0)
		antmaus2.Move(0.0,0.0,0.0)
		antmaus3.Move(0.0,0.0,0.0)
		antmaus4.Move(0.0,0.0,0.0)
		luzantmaus1.RemoveFromList("Timer8")
		luzantmaus1.TimerFunc=""
		return
	luzantmaus1.Intensity=luzantmaus1.Intensity-0.1
	luzantmaus2.Intensity=luzantmaus2.Intensity-0.1
	luzantmaus3.Intensity=luzantmaus3.Intensity-0.1
	luzantmaus4.Intensity=luzantmaus4.Intensity-0.1
	luzantmaus1.SizeFactor=luzantmaus1.SizeFactor-0.05
	luzantmaus2.SizeFactor=luzantmaus2.SizeFactor-0.05
	luzantmaus3.SizeFactor=luzantmaus3.SizeFactor-0.05
	luzantmaus4.SizeFactor=luzantmaus4.SizeFactor-0.05
	fuegoantmaus1.Intensity=fuegoantmaus1.Intensity+1.0
	fuegoantmaus2.Intensity=fuegoantmaus2.Intensity+1.0
	fuegoantmaus3.Intensity=fuegoantmaus3.Intensity+1.0
	fuegoantmaus4.Intensity=fuegoantmaus4.Intensity+1.0
	antmaus1.Move(0.0,0.0,0.0)
	antmaus2.Move(0.0,0.0,0.0)
	antmaus3.Move(0.0,0.0,0.0)
	antmaus4.Move(0.0,0.0,0.0)

def ApagaLucesMaus():
	luzantmaus1.TimerFunc=BajaIntLuzMausGrad
	luzantmaus1.SubscribeToList("Timer8")

def EmpujaLosa2():
	ComienzaCamaraMaus()
	ApagaLucesMaus()
	Bladex.AddScheduledFunc(Bladex.GetTime()+4.0, ApareceEspiritu, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, ElevaEspiritu, ())

def EmpujaLosa():
	char=Bladex.GetEntity("Player1")
	NetSounds.AddAnimSound(char,'Amz_push_sarcofa', ruinspasopie1amz, 0.0625)
	NetSounds.AddAnimSound(char,'Amz_push_sarcofa', ruinspasopie2amz, 0.1250)
	NetSounds.AddAnimSound(char,'Amz_push_sarcofa', ruinspasopie3amz, 0.3958)
	NetSounds.AddAnimSound(char,'Amz_push_sarcofa', ruinsesfcorto2amz, 0.4070)
	NetSounds.AddAnimSound(char,'Amz_push_sarcofa', ruinsesflargoamz, 0.5000)
	NetSounds.AddAnimSound(char,'Amz_push_sarcofa', ruinspasopie2amz, 0.6416)
	NetSounds.AddAnimSound(char,'Amz_push_sarcofa', ruinspasopie1amz, 0.6708)
	cam=Bladex.GetEntity("Camera")
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.LaunchAnimation("Amz_push_sarcofa")
	char.Position=-48025.0, -2610.0, -49100.0
	char.Angle=3.14159/4.0
	punterotumba.RemoveFromWorld()
	cam.SType=0
	cam.TType=0
	cam.Position=-47700.0, -1660.0, -46875.0
	cam.TPos=-51700.0, -5875.0, -55000.0
	Bladex.SetListenerPosition(2)
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.8, EmpujaLosa2, ())

def EnfilaYEmpuja(entity_name):
	char=Bladex.GetEntity("Player1")
	char.QuickFace(3.14159/4.0)
	Actions.FreeBothHands("Player1")
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, EmpujaLosa, ())

def Colocacion(obj_name, use_from):
	ScriptSkip.SkipScriptStart("EscenaMausoleo")
	#Bladex.DeactivateInput()
	Scorer.SetVisible(0)
	EnfilaYEmpuja("Player1")


#################################################################################################











#################################################################################################
## Cementerio.py








def RemueveTierra(pos, v1, v2, v3):
	tierra=Bladex.CreateEntity("TierraRemoviendose", "Entity Particle System D3", pos[0]+v1[0], pos[1]-1200.0, pos[2]+v1[2])
	tierra.D1=v2[0]-v1[0], 0.0, v2[2]-v1[2]
	tierra.D2=v3[0]-v1[0], 0.0, v3[2]-v1[2]
	tierra.ParticleType="Tierra2"
	tierra.PPS=64
	tierra.YGravity=200.0
	tierra.Friction=0.1
	tierra.Velocity=0.0, -400.0, 0.0
	tierra.RandomVelocity=15.0
	tierra.Time2Live=64
	tierra.DeathTime=Bladex.GetTime()+2.0

def Despierta(ent_name):
	o = Bladex.GetEntity(ent_name + "quad")
	if o:
		o.SubscribeToList("Pin")
	enemigo=Bladex.GetEntity(ent_name)
	enemigo.InitPos=enemigo.Position
	alfa=B3DLib.GetEntity2EntityAngle(ent_name, "Player1")
	enemigo.Face(alfa)
	enemigo.Blind=0
	enemigo.Deaf=0

def GeneraEnemigo(enemigo):
	char=Bladex.GetEntity("Player1")
	enemigo.UnFreeze()
	pos=enemigo.Position
	v=char.Position[0]-pos[0], 0.0, char.Position[2]-pos[2]
	v=B3DLib.Normalize(v)
	v1=v[0]*500.0, 0.0, v[2]*500.0
	v2=v1[0]*math.cos(1.7453)-v1[2]*math.sin(1.7453), 0.0, v1[0]*math.sin(1.7453)+v1[2]*math.cos(1.7453)
	v3=v2[0]*math.cos(2.7925)-v2[2]*math.sin(2.7925), 0.0, v2[0]*math.sin(2.7925)+v2[2]*math.cos(2.7925)
	saltatie=Bladex.CreateEntity("TierraSaltando", "Entity Particle System D1", pos[0], pos[1]-1200.0, pos[2])
	saltatie.ParticleType="Tierra3"
	saltatie.PPS=1024
	saltatie.YGravity=4900.0
	saltatie.Friction=0.05
	saltatie.Velocity=0.0, -600.0, 0.0
	saltatie.RandomVelocity=50.0
	saltatie.Time2Live=60
	saltatie.DeathTime=Bladex.GetTime()+10.0/60.0
	saltati2=Bladex.CreateEntity("TierraSaltando2", "Entity Particle System D1", pos[0], pos[1]-1200.0, pos[2])
	saltati2.ParticleType="Tierra2"
	saltati2.PPS=128
	saltati2.YGravity=200.0
	saltati2.Friction=0.1
	saltati2.Velocity=0.0, -300.0, 0.0
	saltati2.RandomVelocity=15.0
	saltati2.Time2Live=32
	saltati2.DeathTime=Bladex.GetTime()+10.0/60.0
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, RemueveTierra, (pos, v1, v2, v3))
	enemigo.SetTmpAnmFlags(1,1,1,0,5,1,0)
	enemigo.LaunchAnimation("Skl_appears1")
	enemigo.Position=pos
	alfa=B3DLib.GetEntity2EntityAngle(enemigo.Name, "Player1")
	enemigo.Angle=alfa
	enemigo.AnmEndedFunc=Despierta
	darfuncs.CreateFalseCube(enemigo.Position,-1.0,enemigo.Name)

def GeneraEnemigoEnEspera(ent_name, time):	
	enemigo=Bladex.GetEntity(ent_name)
	if B3DLib.GetXZDistance(ent_name, "Player1")>5000.0:
		enemigo.RemoveFromList("Timer1")
		enemigo.TimerFunc=""
		GeneraEnemigo(enemigo)

def LevantaOtroEsqueleto(ent_name):
	char=Bladex.GetEntity("Player1")
	oldesq=Bladex.GetEntity(ent_name)
	oldesq.Data.OldImDeadFunc(ent_name)	
	newesq=Bladex.GetEntity(ent_name[:len(ent_name)-1]+`(int(ent_name[len(ent_name)-1:])+2)`) # +3)`)
	if B3DLib.GetXZDistance(newesq.Name, "Player1")>5000.0:
		GeneraEnemigo(newesq)
	else:
		newesq.TimerFunc=GeneraEnemigoEnEspera
		newesq.SubscribeToList("Timer1")

def EmpiezaLevantamientoEsqueletos(sec_idx, ent_name):
	if ent_name=="Player1":
		salidamaus.OnEnter=""
		GeneraEnemigo(esq1)
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, GeneraEnemigo, (esq2,))
		#Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, GeneraEnemigo, (esq3,))




def CreaEsqueleto(n, x, y, z, level, arma="Gladius", escudo=""):
	esq=Bladex.CreateEntity("Esq"+`n`, "Skeleton", x, y, z, "Person")
	esq.Angle=0.0
	esq.Level=level
	hacha=Bladex.CreateEntity("RuinsHachaEsq"+`n`, arma, 0, 0, 0, "Weapon")
	ItemTypes.ItemDefaultFuncs(hacha)
	Actions.TakeObject(esq.Name, hacha.Name)
	if escudo:
		esc=Bladex.CreateEntity("RuinsEscEsq"+`n`, escudo, 0, 0, 0, "Weapon")
		ItemTypes.ItemDefaultFuncs(esc)
		Actions.TakeObject(esq.Name, esc.Name)
	esq.ActionAreaMin=pow(2,12)
	esq.ActionAreaMax=pow(2,13)
	EnemyTypes.EnemyDefaultFuncs(esq)
	esq.Blind=1
	esq.Deaf=1
	if n<9: # n<8:
		esq.Data.OldImDeadFunc=esq.ImDeadFunc
		esq.ImDeadFunc=LevantaOtroEsqueleto
	esq.Freeze()
	esq.RemoveFromWorldWithChilds()
	return esq





#################################################################################################











#################################################################################################
## Inicio.py




def ReiniciaCamaraInicio(ent_name):
	cam=Bladex.GetEntity("Camera")
	Bladex.SetListenerPosition(1)
	cam.SetPersonView("Player1")
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("exterior_antes"))

def UltimoTravelling():
	AuxFuncs.MoveCamFromTo(63500.0, -5000.0, 3000.0, 62000.0, -100.0, 2000, 65000.0, -7000.0, 6000.0, 65000.0, -3000.0, 4000.0, 1.5)

def LanzaAnimacionInicio():
	char=Bladex.GetEntity("Player1")
	NetSounds.AddAnimSound(char,'Amz_start', ruinsesfcorto1amz, 0.2421)
	NetSounds.AddAnimSound(char,'Amz_start', ruinspasopie1amz, 0.3438)
	NetSounds.AddAnimSound(char,'Amz_start', ruinspasopie2amz, 0.4067)
	NetSounds.AddAnimSound(char,'Amz_start', ruinspasopie1amz, 0.4891)
	NetSounds.AddAnimSound(char,'Amz_start', ruinspasopie3amz, 0.5399)
	NetSounds.AddAnimSound(char,'Amz_start', ruinspasopie2amz, 0.5410)
	NetSounds.AddAnimSound(char,'Amz_start', ruinsesfcorto2amz, 0.5423)
	NetSounds.AddAnimSound(char,'Amz_start', ruinspasopie1amz, 0.6368)
	NetSounds.AddAnimSound(char,'Amz_start', ruinspasopie3amz, 0.6585)
	NetSounds.AddAnimSound(char,'Amz_start', ruinspasopie1amz, 0.6755)
	NetSounds.AddAnimSound(char,'Amz_start', ruinspasopie2amz, 0.6973)
	NetSounds.AddAnimSound(char,'Amz_start', ruinspasopie3amz, 0.7167)
	NetSounds.AddAnimSound(char,'Amz_start', ruinspasopie1amz, 0.7384)
	NetSounds.AddAnimSound(char,'Amz_start', ruinspasopie3amz, 0.7506)
	NetSounds.AddAnimSound(char,'Amz_start', ruinspasopie1amz, 0.8571)
	NetSounds.AddAnimSound(char,'Amz_start', ruinspasopie2amz, 0.8580)
	NetSounds.AddAnimSound(char,'Amz_start', ruinsesfcorto2amz, 0.8595)
	#char.SetTmpAnmFlags(1,1,1,0,3,1)	valores por defecto
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.LaunchAnimation("Amz_start")
	char.Position=69850,-6725.0,14000
	char.Angle=3.14159
	char.AnmEndedFunc=ReiniciaCamaraInicio
	AuxFuncs.MoveCamFromTo(60625.0, -8750.0, 8100.0, 63100.0, -6450.0, 14750, 68000.0, -8500.0, 13000.0, 68000.0, -8500.0, 13000.0, 11.5)
	Bladex.AddScheduledFunc(Bladex.GetTime()+12.5, AuxFuncs.MoveCamFromTo, (65000.0, -8500.0, 4000.0, 63500.0, -5000.0, 3000.0, 64000.0, -7500.0, 8000.0, 65000.0, -7000.0, 6000.0, 4.0, UltimoTravelling))

def MusicayTexto():
	GameText.WriteText("M4T2")
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musica_inicio")) # lanza MP3
	if Reference.DEMO_MODE==0:
		GotoMapVars.MapText(4,"D_M4_T1")

def Comienza():
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, MusicayTexto, ())
	AuxFuncs.FadeFrom(2.0)
	ScriptSkip.SkipScriptStart("EscenaInicio")
	#Bladex.DeactivateInput()
	Scorer.SetVisible(0)
	cam=Bladex.GetEntity("Camera")
	cam.SType=0
	cam.TType=0
	cam.Position=46000.0, -13000.0, -6600.0
	cam.TPos=40000.0, -11000.0, -6600.0
	Bladex.SetListenerPosition(2)
	AuxFuncs.MoveCamFromTo(46000.0, -13000.0, -6600.0, 52000.0, -8000.0, 3600.0, 40000.0, -11000.0, -6600.0, 40000.0, -14000.0, 1100.0, 8.0, LanzaAnimacionInicio)





#################################################################################################









#################################################################################################
## Final.py







def FundidoFin():
	char=Bladex.GetEntity("Player1")
	char.LaunchAnimation("Amz_darkbook")
	Bladex.DeactivateInput()
	AuxFuncs.FadeTo(2.5, 2.0)
	Scorer.SetVisible(0)

	time = 4
	if Reference.DEMO_MODE==0:
		Bladex.AddScheduledFunc(Bladex.GetTime() + time, GotoMapVars.EndOfLevel, ())
		GotoMapVars.MapText(4,"D_M4_T2")
	else:
		AuxFuncs.setDemoBg(time)


def ReseteaCamaraFinal2():
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Bladex.SetListenerPosition(1)

def SubeIntLuzTemploGrad(ent_name, time):
	global curr_fire_int
	curr_fire_int=curr_fire_int-0.5
	light_int=lanttempl1.Intensity+0.4
	lanttempl1.Intensity=light_int
	lanttempl2.Intensity=light_int
	lanttempl3.Intensity=light_int
	lanttempl4.Intensity=light_int
	fanttempl1.Intensity=curr_fire_int
	fanttempl2.Intensity=curr_fire_int
	fanttempl3.Intensity=curr_fire_int
	fanttempl4.Intensity=curr_fire_int
	libromag.Move(0.0, 0.0, 0.0)
	if lanttempl1.Intensity>=6.0:
		lanttempl1.RemoveFromList("Timer8")
		lanttempl1.TimerFunc=""
		ReseteaCamaraFinal2()

def ApagaLuzBolaFuego(ent_name, time):
	luzexpldemonio.Intensity=luzexpldemonio.Intensity-0.15
	libromag.Move(0.0, 0.0, 0.0)
	if luzexpldemonio.Intensity<=0.0:
		luzexpldemonio.Intensity=0.0
		librocer.RemoveFromList("Timer60")
		librocer.TimerFunc=""
		lanttempl1.CastShadows=1
		lanttempl2.CastShadows=1
		lanttempl3.CastShadows=1
		lanttempl4.CastShadows=1
		lanttempl1.TimerFunc=SubeIntLuzTemploGrad
		lanttempl1.SubscribeToList("Timer8")

def ReapareceLibro():
	global bf
	bf.PPS=1200
	bf.YGravity=4000.0
	bf.Friction=0.1
	bf.Velocity=0.0, -6000.0, 0.0
	bf.RandomVelocity=60.0
	bf.RandomVelocity_V=40.0
	bf.DeathTime=Bladex.GetTime()+0.1
	luzexpldemonio.Position=0.0, -2000.0, 0.0
	luzexpldemonio.Intensity=12.0
	librocer.TimerFunc=ApagaLuzBolaFuego
	librocer.SubscribeToList("Timer60")
	luzlibro.PutToWorld()
	luzlibro.Color=80, 40, 255
	luzlibro.Position=0.0, -2000.0, 0.0
	luzlibro.Intensity=1.0
	libromag.PutToWorld()
	libromag.Move(0.0, 0.0, 0.0)
	dat_pos=[263.0, -1351.0, 389.0, 263.0, -1351.0, 389.0, -263.0, -1351.0, -389.0, -263.0, -1351.0, -389.0]
	dat_D=[0.0, 0.0, -778.0, -526.0, 0.0, 0.0, 0.0, 0.0, 778.0, 526.0, 0.0, 0.0]
	for n in range(4):
		cl=Bladex.CreateEntity("ChispasLibro"+`n+1`, "Entity Particle System D2", dat_pos[0+n*3], dat_pos[1+n*3], dat_pos[2+n*3])
		cl.D=dat_D[0+n*3], dat_D[1+n*3], dat_D[2+n*3]
		cl.ParticleType="Energia2"
		cl.YGravity=-150.0
		cl.Friction=0.0
		cl.PPS=16
		cl.Velocity=0.0, 0.0, 0.0
		cl.Time2Live=80
	sndfuegodemon.TimerFunc=BajaVolEspiritu
	sndfuegodemon.SubscribeToList("Timer8")
	sndchispaslibro.Position=libromag.Position
	sndchispaslibro.Volume=0
	sndchispaslibro.PlaySound(-1)
	sndchispaslibro.TimerFunc=SubeVolEspiritu
	sndchispaslibro.SubscribeToList("Timer8")
	cam=Bladex.GetEntity("Camera")
	cam.RemoveFromList("Timer60")
	cam.TimerFunc=""

def BolaSigueLuz():
	global bf
	bf.Position=luzexpldemonio.Position

def BolaPicado():
	init_pos=luzexpldemonio.Position
	end_pos=libromag.Position
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, Objects.DisplaceObjectFromTo, (luzexpldemoniodin, init_pos, end_pos, 0.0, 10000.0, "", "", sndimpdemonsello, BolaSigueLuz, (), ReapareceLibro, ()))

def BolaArriba():
	init_pos=luzexpldemonio.Position
	end_pos=0.0, -10000.0, 0.0
	Objects.DisplaceObjectFromTo(luzexpldemoniodin, init_pos, end_pos, 4000.0, 0.0, "", "", "", BolaSigueLuz, (), BolaPicado, ())

def CamaraSigueBolaFuego(ent_name, time):
	cam=Bladex.GetEntity("Camera")
	cam.TPos=luzexpldemonio.Position

def CamaraMuerteDemonio():
	cam=Bladex.GetEntity("Camera")
	cam.SType=0
	cam.TType=0
	p=luzexpldemonio.Position
	cam.Position=-(p[0]/abs(p[0]))*5000.0, -6500.0, -(p[2]/abs(p[2]))*5000.0
	cam.TPos=p
	Bladex.SetListenerPosition(2)
	cam.TimerFunc=CamaraSigueBolaFuego
	cam.SubscribeToList("Timer60")

def DesmaterializaDemonio(ent_name, time):
	global bf
	demonio.Alpha=demonio.Alpha-0.005
	if demonio.Alpha<=0.0:
		demonio.Alpha=0.0
		demonio.RemoveFromList("Timer60")
		demonio.TimerFunc=""
		demonio.RemoveFromWorld()
		bf.RandomVelocity=40.0
		CamaraMuerteDemonio()
		init_pos=luzexpldemonio.Position
		end_pos=luzexpldemonio.Position[0]/2.0, (luzexpldemonio.Position[1]-10000.0)/2.0, luzexpldemonio.Position[2]/2.0
		Objects.DisplaceObjectFromTo(luzexpldemoniodin, init_pos, end_pos, 0.0, 4000.0, "", "", "", BolaSigueLuz, (), BolaArriba, ())

def BajaIntLuzLampara(ent_name, time):
	luzlamptemplo.Intensity=luzlamptemplo.Intensity-1.0
	if luzlamptemplo.Intensity<=6.0:
		fuelamptemplo.Intensity=3
		luzlamptemplo.RemoveFromList("Timer8")
		luzlamptemplo.TimerFunc=""

def SubeLuzBolaFuego(ent_name, time):
	luzexpldemonio.Intensity=luzexpldemonio.Intensity+0.07
	if luzexpldemonio.Intensity>=4.0:
		luzexpldemonio.Intensity=4.0
		luzexpldemonio.RemoveFromList("Timer60")
		luzexpldemonio.TimerFunc=""

def BolaFuegoMagico():
	global bf
	alfa=demonio.Angle+3.14159/2.0
	x=demonio.Position[0]+500.0*math.cos(alfa)
	y=demonio.Position[1]+250.0
	z=demonio.Position[2]+500.0*math.sin(alfa)
	demonio.RasterMode="Read"
	bf=Bladex.CreateEntity("BolaFuego", "Entity Particle System D1", x, y, z)
	bf.ParticleType="FuegoInvocacion"
	bf.PPS=250
	bf.YGravity=0.0
	bf.Friction=0.1
	bf.Velocity=0.0, 0.0, 0.0
	bf.RandomVelocity=50.0
	bf.Time2Live=40
	luzexpldemonio.Position=x, y, z
	luzexpldemonio.TimerFunc=SubeLuzBolaFuego
	luzexpldemonio.SubscribeToList("Timer60")
	demonio.TimerFunc=DesmaterializaDemonio
	demonio.SubscribeToList("Timer60")
	sndfuegodemon.Position=0,0,0
	luzexpldemonio.Link(sndfuegodemon)
	sndfuegodemon.Volume=0
	sndfuegodemon.PlaySound(-1)
	sndfuegodemon.TimerFunc=SubeVolEspiritu
	sndfuegodemon.SubscribeToList("Timer8")

def ImplosionDemonio():
	impl=Bladex.CreateEntity("ImplosionDemonio", "Entity Particle System D1", demonio.Position[0], demonio.Position[1], demonio.Position[2])
	impl.ParticleType="Energia3"
	impl.YGravity=0.0
	impl.Friction=0.0
	impl.PPS=300
	impl.Velocity=0.0, 0.0, 0.0
	impl.RandomVelocity=-30.0
	impl.Time2Live=70
	impl.DeathTime=Bladex.GetTime()+1.0

def MuerteDemonio(ent_name):
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.25, Bladex.TriggerEvent, (26,))
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("emptyloquesea"))
	luzlamptemplo.TimerFunc=BajaIntLuzLampara
	luzlamptemplo.SubscribeToList("Timer8")
	demonio.Wuea=Reference.WUEA_ENDED
	demonio.SetTmpAnmFlags(1,1,1,0,5,1)
	demonio.LaunchAnimation("Ldm_dth_disap")
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.25, ImplosionDemonio, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, BolaFuegoMagico, ())


def m2():
	demonio.Life=-10

def m():
	demonio.Position=-1000, -2730, -4000
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, m2, ())


def ReseteaCamaraFinal():
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Bladex.SetListenerPosition(1)
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("combate_final"))

def SubeIntLuzLampara(ent_name, time):
	luzlamptemplo.Intensity=luzlamptemplo.Intensity+1.0
	if luzlamptemplo.Intensity>=40.0:
		fuelamptemplo.Intensity=1
		luzlamptemplo.RemoveFromList("Timer8")
		luzlamptemplo.TimerFunc=""

def DespiertaDemonio2():
	demonio.Blind=0
	demonio.Deaf=0

def DespiertaDemonio(ent_name):
	sndfuegodemon.TimerFunc=BajaVolEspiritu
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, sndfuegodemon.SubscribeToList, ("Timer8",))
	luzlamptemplo.TimerFunc=SubeIntLuzLampara
	luzlamptemplo.SubscribeToList("Timer8")
	Bladex.AddScheduledFunc(Bladex.GetTime()+4.0, DespiertaDemonio2, ())

def ApagaLuzDemonio(ent_name, time):
	luzdemonio.Intensity=luzdemonio.Intensity-0.05
	if luzdemonio.Intensity<=0.0:
		luzdemonio.Intensity=0.0
		luzdemonio.RemoveFromList("Timer60")
		luzdemonio.TimerFunc=""

def MaterializaDemonio(ent_name, time):
	demonio.Alpha=demonio.Alpha+0.001
	if demonio.Alpha>=1.0:
		demonio.Alpha=1.0
		demonio.RemoveFromList("Timer60")
		demonio.TimerFunc=""

def EnciendeLuzDemonio(ent_name, time):
	luzdemonio.Intensity=luzdemonio.Intensity+0.1
	if luzdemonio.Intensity>=6.0:
		luzdemonio.RemoveFromList("Timer60")
		luzdemonio.TimerFunc=""

def ReduceMegaSurtidor():
	global ms
	ms.PPS=80
	ms.Time2Live=60

def LanzaMegaSurtidor2(v1, v2, v3):
	global ms
	ms=Bladex.CreateEntity("MegaSurtidor", "Entity Particle System D3", v1[0]-250.0, -1501.0, v1[2])
	ms.D1=v2[0]-v1[0], 0.0, v2[2]-v1[2]
	ms.D2=v3[0]-v1[0], 0.0, v3[2]-v1[2]
	ms.ParticleType="FuegoInvocacion"
	ms.PPS=140
	ms.YGravity=0.0
	ms.Friction=0.0
	ms.Velocity=0.0, -50.0, 0.0
	ms.RandomVelocity=3.0
	ms.Time2Live=120
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, ReduceMegaSurtidor, ())

def LanzaMegaSurtidor(v1, v2, v3):
	explms=Bladex.CreateEntity("ExplMegaSurtidor", "Entity Particle System D1", 0.0, -1400.0, 0.0)
	explms.ParticleType="FuegoInvocacion"
	explms.PPS=1200
	explms.YGravity=4000.0
	explms.Friction=0.1
	explms.Velocity=0.0, -4000.0, 0.0
	explms.RandomVelocity=60.0
	explms.RandomVelocity_V=40.0
	explms.Time2Live=40
	explms.DeathTime=Bladex.GetTime()+0.25
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, LanzaMegaSurtidor2, (v1, v2, v3))

def CortinaMagica2():
	dat_pos=[0.0, -1355.0, 2350.0, 0.0, -1355.0, 2350.0, 2080.0, -1355.0, -1140.0, 2080.0, -1355.0, -1140.0, -2080.0, -1355.0, -1140.0, -2080.0, -1355.0, -1140.0]
	dat_D=[-2080.0, 0.0, -1200.0, 2080.0, 0.0, -1200.0, 0.0, 0.0, 2290.0, -2080.0, 0.0, -1200.0, 2080.0, 0.0, -1200.0, 0.0, 0.0, 2290.0]
	for n in range(6):
		cortina2=Bladex.CreateEntity("Cortina2"+`n+1`, "Entity Particle System D2", dat_pos[0+n*3], dat_pos[1+n*3], dat_pos[2+n*3])
		cortina2.D=dat_D[0+n*3], dat_D[1+n*3], dat_D[2+n*3]
		cortina2.ParticleType="Energia3"
		cortina2.YGravity=-500.0
		cortina2.Friction=0.0
		cortina2.PPS=16
		cortina2.Velocity=0.0, 0.0, 0.0
		cortina2.Time2Live=70
		cortina2.DeathTime=Bladex.GetTime()+6.0

def ApagaExplosionLuzDemonio(ent_name, time):
	luzexpldemonio.Intensity=luzexpldemonio.Intensity-0.2
	if luzexpldemonio.Intensity<=0.0:
		luzexpldemonio.Intensity=0.0
		luzexpldemonio.RemoveFromList("Timer60")
		luzexpldemonio.TimerFunc=""

def ExplosionLuzDemonio(ent_name, time):
	luzexpldemonio.Intensity=luzexpldemonio.Intensity+0.5
	if luzexpldemonio.Intensity>=20.0:
		luzexpldemonio.Intensity=20.0
		luzexpldemonio.TimerFunc=ApagaExplosionLuzDemonio

def ExplosionDemonio():
	global ms
	ms.PPS=60
	x, y, z = demonio.Position
	expldemonruins.Position = x, y, z
	expldemonruins.PlaySound(0)
	ondaexpdm=Bladex.CreateEntity("OndaExpDm", "Entity Particle System D1", x, y, z)
	ondaexpdm.ParticleType="Energia3"
	ondaexpdm.YGravity=0.0
	ondaexpdm.Friction=0.1
	ondaexpdm.PPS=4000
	ondaexpdm.Velocity=0.0, 0.0, 0.0
	ondaexpdm.RandomVelocity=90.0
	ondaexpdm.Time2Live=40
	ondaexpdm.DeathTime=Bladex.GetTime()+0.2
	luzexpldemonio.TimerFunc=ExplosionLuzDemonio
	luzexpldemonio.SubscribeToList("Timer60")

def AparicionDemonio():
	sndimpdemonsello.Position=sndfuegodemon.Position=libromag.Position
	sndimpdemonsello.PlaySound(0)
	sndfuegodemon.Volume=0
	sndfuegodemon.PlaySound(-1)
	sndfuegodemon.TimerFunc=SubeVolEspiritu
	sndfuegodemon.SubscribeToList("Timer8")
	char=Bladex.GetEntity("Player1")
	v=char.Position[0], 0.0, char.Position[2]
	v=B3DLib.Normalize(v)
	v1=v[0]*1250.0, 0.0, v[2]*1250.0
	v2=v1[0]*math.cos(2.0944)-v1[2]*math.sin(2.0944), 0.0, v1[0]*math.sin(2.0944)+v1[2]*math.cos(2.0944)
	v3=v2[0]*math.cos(2.0944)-v2[2]*math.sin(2.0944), 0.0, v2[0]*math.sin(2.0944)+v2[2]*math.cos(2.0944)
	LanzaMegaSurtidor(v1, v2, v3)
	CortinaMagica2()
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.4, ExplosionDemonio, ())
	luzdemonio.Position=-250.0, -1900.0, 0.0
	luzdemonio.TimerFunc=EnciendeLuzDemonio
	luzdemonio.SubscribeToList("Timer60")
	libromag.RemoveFromWorld()
	spirit1.RemoveFromWorld()
	demonio.UnFreeze()
	demonio.TimerFunc=MaterializaDemonio
	demonio.SubscribeToList("Timer60")
	alfa=-(3.14159/2.0)*(v[0]/abs(v[0]))+math.atan(v[2]/v[0])
	demonio.SetTmpAnmFlags(1,1,1,0,5,1,0)
	demonio.LaunchAnimation("Ldm_appears")
	demonio.Position=-100.0, -2730.0, -125.0
	demonio.Angle=alfa
	demonio.SetOnFloor()
	demonio.AnmEndedFunc=DespiertaDemonio

def CamaraEspiralDemonio(ent_name, time):
	global ms
	global initdmcampos
	global dmcam_step
	cam=Bladex.GetEntity("Camera")
	dmcam_step=dmcam_step+1
	if dmcam_step>TOTAL_DMCAM_STEPS:
		curr_time=(dmcam_step-TOTAL_DMCAM_STEPS)/60.0
		v_ang=DMCAM_ANGLE+curr_time*(ANG_VEL+curr_time*ANG_DEC/2)
		v_alt=DMCAM_HEIGHT+curr_time*(HGT_VEL+curr_time*HGT_DEC/2)
		v_alt_trg=DMTRG_HEIGHT+curr_time*(TRG_VEL+curr_time*TRG_DEC/2)
		v_rad=DMCAM_RADIUS+curr_time*(RAD_VEL+curr_time*RAD_DEC/2)
	else:
		v_ang=dmcam_step*DMCAM_ANGLE_VARIATION
		v_alt=dmcam_step*DMCAM_HEIGHT_VARIATION
		v_alt_trg=dmcam_step*DMTRG_HEIGHT_VARIATION
		v_rad=dmcam_step*DMCAM_RADIUS_VARIATION
	initdmcampos=vposplcamnorm[0]*(DMCAM_INIT_RADIUS+v_rad), -5000.0, vposplcamnorm[2]*(DMCAM_INIT_RADIUS+v_rad)
	cam.Position=initdmcampos[0]*math.cos(v_ang)-initdmcampos[2]*math.sin(v_ang), initdmcampos[1]+v_alt, initdmcampos[0]*math.sin(v_ang)+initdmcampos[2]*math.cos(v_ang)
	cam.TPos=0.0, -2500.0+v_alt_trg, 0.0
	if dmcam_step==TOTAL_DMCAM_STEPS+DEC_STEPS:
		cam.RemoveFromList("Timer60")
		cam.TimerFunc=""
		ms.DeathTime=Bladex.GetTime()+0.25
		luzdemonio.TimerFunc=ApagaLuzDemonio
		luzdemonio.SubscribeToList("Timer60")
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, ReseteaCamaraFinal, ())

def CamaraAparicionDemonio():
	global initdmcampos
	cam=Bladex.GetEntity("Camera")
	cam.Position=initdmcampos
	cam.TPos=0.0, -2500.0, 0.0
	cam.TimerFunc=CamaraEspiralDemonio
	cam.SubscribeToList("Timer60")


def CaeLibroSello():
	Objects.DisplaceObject(libromagdin, 1000.0, (0.0, 1.0, 0.0), 0.0, 2500.0, (), (), (), "", (), AparicionDemonio)

def ApagaLuzLibroGrad(ent_name, time):
	luzlibro.Intensity=luzlibro.Intensity-0.2
	libromag.Move(0.0, 0.0, 0.0)
	if luzlibro.Intensity<=0:
		librocer.RemoveFromList("Timer60")
		librocer.TimerFunc=""
		luzlibro.RemoveFromWorld()
		#luzlibro.SubscribeToList("Pin")

def ApagaLuzLibro():
	librocer.TimerFunc=ApagaLuzLibroGrad
	librocer.SubscribeToList("Timer60")

def TornaLuzLibroRojaGrad(ent_name, time):
	global lcol80_255
	global lcol40_20
	global lcol255_10
	global lcol80_255_var
	global lcol40_20_var
	global lcol255_10_var
	lcol80_255=lcol80_255+lcol80_255_var
	lcol40_20=lcol40_20-lcol40_20_var
	lcol255_10=lcol255_10-lcol255_10_var
	luzlibro.Color=min(255,int(lcol80_255)), int(lcol40_20), int(lcol255_10)
	libromag.Move(0.0, 0.0, 0.0)
	if luzlibro.Color[0]>=255:
		luzlibro.Color=255, 20, 10
		luzlibro.RemoveFromList("Timer60")
		luzlibro.TimerFunc=""

def TornaLuzLibroRoja():
	luzlibro.TimerFunc=TornaLuzLibroRojaGrad
	luzlibro.SubscribeToList("Timer60")
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, ApagaLuzLibro, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, CaeLibroSello, ())

def ExplosionLibro():
	spirit1.Intensity=0.0
	spirit2.RemoveFromWorld()
	estela.DeathTime=Bladex.GetTime()+1.0
	ondaexp=Bladex.CreateEntity("OndaExp", "Entity Particle System D1", libromag.Position[0], libromag.Position[1], libromag.Position[2])
	ondaexp.ParticleType="Energia2"
	ondaexp.YGravity=0.0
	ondaexp.Friction=0.1
	ondaexp.PPS=4000
	ondaexp.Velocity=0.0, 0.0, 0.0
	ondaexp.RandomVelocity=75.0
	ondaexp.Time2Live=30
	ondaexp.DeathTime=Bladex.GetTime()+0.1
	despl=(200.0, 200.0, 150.0, 150.0, 100.0, 100.0, 75.0, 75.0, 50.0, 25.0, 25.0)
	vect=(ejey, ejeyn, ejeyn, ejey, ejey, ejeyn, ejeyn, ejey, ejey, ejeyn, ejeyn)
	vel_inic=(4000.0, 0.0, 3000.0, 0.0, 2000.0, 0.0, 1250.0, 0.0, 750.0, 0.0, 500.0)
	vel_fin=(0.0, 3000.0, 0.0, 2000.0, 0.0, 1250.0, 0.0, 750.0, 0.0, 500.0, 0.0)
	Objects.NDisplaceObject(libromagdin, despl, vect, vel_inic, vel_fin, (), (), (), "", (), TornaLuzLibroRoja)

def ArrojaEspirituLibro():
	sndespiritu.TimerFunc=BajaVolEspiritu
	sndespiritu.SubscribeToList("Timer8")
	Objects.DisplaceObject(spirit1din, 2455, (0.0, 1.0, 0.0), 0.0, 6000.0, "", "", sndimplibro, MueveEstela, (), ExplosionLibro)

def ElevaLibroSello():
	despl=(750.0, 250.0)
	vect=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_inic=(0.0, 500.0)
	vel_fin=(500.0, 0.0)
	Objects.NDisplaceObject(libromagdin, despl, vect, vel_inic, vel_fin)
	angulos=(-_4PI, -_4PI)
	vel_ang_inic=(0.0, _2PI+_2PI/5.0) #(0.0, _2PI)
	vel_ang_fin=(_2PI+_2PI/5.0, 0.0) #(_2PI, 0.0)
	centros=(orig, orig)
	ejes=((0.0, 0.0, 1.0), (0.0, 0.0, 1.0))
	Objects.NRotateObject(libromagdin, angulos, vel_ang_inic, vel_ang_fin, centros, ejes, Objects.REL, (), (), (), "", (), ArrojaEspirituLibro)

def ElevaEspirituEspiral(ent_name, time):
	global initsppos
	global sp_step
	sp_step=sp_step+1
	v_ang=sp_step*SP_ANGLE_VARIATION
	v_alt=sp_step*SP_HEIGHT_VARIATION
	v_rad=sp_step*SP_RADIUS_VARIATION
	initsppos=vposplspnorm[0]*(SP_RADIUS+v_rad), -1350.0, vposplspnorm[2]*(SP_RADIUS+v_rad)
	spirit1.Position=initsppos[0]*math.cos(v_ang)-initsppos[2]*math.sin(v_ang), initsppos[1]+v_alt, initsppos[0]*math.sin(v_ang)+initsppos[2]*math.cos(v_ang)
	spirit2.Position=estela.Position=spirit1.Position
	if sp_step==TOTAL_SP_STEPS:
		spirit1.RemoveFromList("Timer60")
		spirit1.TimerFunc=""



def TranspEspiritu(ent_name, time):
	global spcol0_128
	global spcol0_180
	global spcol0_200
	global spcol0_255
	global spcol0_128_var
	global spcol0_180_var
	global spcol0_200_var
	global spcol0_255_var
	spcol0_128=spcol0_128+spcol0_128_var
	spcol0_180=spcol0_180+spcol0_180_var
	spcol0_200=spcol0_200+spcol0_200_var
	spcol0_255=spcol0_255+spcol0_255_var
	spirit1.Color=min(180,int(spcol0_180)), min(255,int(spcol0_255)), min(128,int(spcol0_128))
	spirit2.Color=min(180,int(spcol0_180)), min(255,int(spcol0_255)), min(200,int(spcol0_200))
	if spirit1.Color[1]>=255:
		spirit1.Color=180, 255, 128
		spirit2.Color=180, 255, 200
		spirit2.RemoveFromList("Timer60")
		spirit2.TimerFunc=""

def ReapareceEspiritu():
	global initsppos
	spirit1.Intensity=0.01
	spirit2.Intensity=0.01
	spirit1.Color=0, 0, 0
	spirit2.Color=0, 0, 0
	spirit2.TimerFunc=TranspEspiritu
	spirit2.SubscribeToList("Timer60")
	spirit1.Position=spirit2.Position=estela.Position=initsppos
	estela.PPS=32
	estela.RandomVelocity=50.0
	spirit1.TimerFunc=ElevaEspirituEspiral
	spirit1.SubscribeToList("Timer60")
	sndespiritu.Volume=0
	sndespiritu.PlaySound(-1)
	sndespiritu.TimerFunc=SubeVolEspiritu
	sndespiritu.SubscribeToList("Timer8")
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, ElevaLibroSello, ())

def SubeIntLuzLibroGrad(ent_name, time):
	luzlibro.Intensity=luzlibro.Intensity+0.25
	libromag.Move(0.0, 0.0, 0.0)
	if luzlibro.Intensity>=8.0:
		luzlibro.RemoveFromList("Timer8")
		luzlibro.TimerFunc=""

def EnciendeLuzLibro():
	luzlibro.TimerFunc=SubeIntLuzLibroGrad
	luzlibro.SubscribeToList("Timer8")

def DesciendeCamaraEspiral(ent_name, time):
	global initspcampos
	global spcam_step
	spcam_step=spcam_step+1
	v_ang=spcam_step*SPCAM_ANGLE_VARIATION
	v_alt=spcam_step*SPCAM_HEIGHT_VARIATION
	cam=Bladex.GetEntity("Camera")
	cam.Position=initspcampos[0]*math.cos(v_ang)-initspcampos[2]*math.sin(v_ang), initspcampos[1]+v_alt, initspcampos[0]*math.sin(v_ang)+initspcampos[2]*math.cos(v_ang)
	cam.TPos=0.0, libromag.Position[1]+(spirit1.Position[1]-libromag.Position[1])/2.0, 0.0
	if spcam_step==TOTAL_SPCAM_STEPS:
		cam.RemoveFromList("Timer60")
		cam.TimerFunc=""
		CamaraAparicionDemonio()

def CortinaMagica():
	global initspcampos
	spirit1.Intensity=0.0
	spirit1.Position=initsppos
	cam=Bladex.GetEntity("Camera")
	cam.SType=0
	cam.TType=0
	cam.Position=initspcampos
	cam.TPos=0.0, spirit1.Position[1], 0.0
	cam.TimerFunc=DesciendeCamaraEspiral
	cam.SubscribeToList("Timer60")
	dat_pos=[0.0, -1355.0, 2350.0, 0.0, -1355.0, 2350.0, 2080.0, -1355.0, -1140.0, 2080.0, -1355.0, -1140.0, -2080.0, -1355.0, -1140.0, -2080.0, -1355.0, -1140.0]
	dat_D=[-2080.0, 0.0, -1200.0, 2080.0, 0.0, -1200.0, 0.0, 0.0, 2290.0, -2080.0, 0.0, -1200.0, 2080.0, 0.0, -1200.0, 0.0, 0.0, 2290.0]
	for n in range(6):
		cortina=Bladex.CreateEntity("Cortina"+`n+1`, "Entity Particle System D2", dat_pos[0+n*3], dat_pos[1+n*3], dat_pos[2+n*3])
		cortina.D=dat_D[0+n*3], dat_D[1+n*3], dat_D[2+n*3]
		cortina.ParticleType="Energia2"
		cortina.YGravity=-250.0
		cortina.Friction=0.0
		cortina.PPS=16
		cortina.Velocity=0.0, 0.0, 0.0
		cortina.Time2Live=120
		cortina.DeathTime=Bladex.GetTime()+11.0
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, EnciendeLuzLibro, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, ReapareceEspiritu, ())

def BajaIntLuzTemploGrad(ent_name, time):
	global curr_fire_int
	curr_fire_int=curr_fire_int+0.5
	light_int=lanttempl1.Intensity-0.4
	lanttempl1.Intensity=light_int
	lanttempl2.Intensity=light_int
	lanttempl3.Intensity=light_int
	lanttempl4.Intensity=light_int
	fanttempl1.Intensity=curr_fire_int
	fanttempl2.Intensity=curr_fire_int
	fanttempl3.Intensity=curr_fire_int
	fanttempl4.Intensity=curr_fire_int
	lanttempl1.Move(0.0, 0.0, 0.0)
	lanttempl2.Move(0.0, 0.0, 0.0)
	lanttempl3.Move(0.0, 0.0, 0.0)
	lanttempl4.Move(0.0, 0.0, 0.0)
	if lanttempl1.Intensity<=1.0:
		lanttempl1.RemoveFromList("Timer8")
		lanttempl1.TimerFunc=""

def BajaLucesTemplo():
	lanttempl1.TimerFunc=BajaIntLuzTemploGrad
	lanttempl1.SubscribeToList("Timer8")

def FinPosaLibroSello():
	librocer.RemoveFromList("Timer60")
	librocer.TimerFunc=""
	dat_pos=[263.0, -1351.0, 389.0, 263.0, -1351.0, 389.0, -263.0, -1351.0, -389.0, -263.0, -1351.0, -389.0]
	dat_D=[0.0, 0.0, -778.0, -526.0, 0.0, 0.0, 0.0, 0.0, 778.0, 526.0, 0.0, 0.0]
	dat_vel=[800.0, -250.0, 0.0, 0.0, -250.0, 800.0, -800.0, -250.0, 0.0, 0.0, -250.0, -800.0]
	for n in range(4):
		polvo=Bladex.CreateEntity("PolvoLibro"+`n+1`, "Entity Particle System D2", dat_pos[0+n*3], dat_pos[1+n*3], dat_pos[2+n*3])
		polvo.D=dat_D[0+n*3], dat_D[1+n*3], dat_D[2+n*3]
		polvo.ParticleType="Polvillo"
		polvo.YGravity=0.0
		polvo.Friction=0.15
		polvo.PPS=512
		polvo.Velocity=dat_vel[0+n*3], dat_vel[1+n*3], dat_vel[2+n*3]
		polvo.RandomVelocity=4.0
		polvo.Time2Live=60
		polvo.DeathTime=Bladex.GetTime()+2.0/60.0
	BajaLucesTemplo()
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, CortinaMagica, ())

def PosaLibroSello(ent_name, time):
	yvar=2400.0*((6000.0-libromag.Position[0])/6000.0)**3
	libromag.Position=libromag.Position[0], -3795.0+yvar, libromag.Position[2]

def LlevaLibroSello():
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, GameText.WriteText, ("M4T3",))
	AuxFuncs.MoveCamFromTo(2650.0, -5000.0, 2400.0, -2000.0, -2525.0, -3175.0, 6000.0, -3295.0, 0.0, 0.0, -1850.0, 0.0, 9.0)
	despl=(3000.0, 3000.0)
	vect=((-1.0, 0.0, 0.0), (-1.0, 0.0, 0.0))
	vel_inic=(0.0, 1500.0)
	vel_fin=(1500.0, 0.0)
	Objects.NDisplaceObject(libromagdin, despl, vect, vel_inic, vel_fin, (), (), (), "", (), FinPosaLibroSello)
	angulos=(_2PI, _2PI)
	vel_ang_inic=(0.0, 3.25)
	vel_ang_fin=(3.25, 0.0)
	centros=(orig, orig)
	ejes=(ejexyz, ejexyz)
	Objects.NRotateObject(libromagdin, angulos, vel_ang_inic, vel_ang_fin, centros, ejes)
	librocer.TimerFunc=PosaLibroSello
	librocer.SubscribeToList("Timer60")

def ElevaLibroAltar():
	AuxFuncs.MoveCamFromTo(5500.0, -5150.0, -3800.0, 5500.0, -5150.0, -3800.0, 9850.0, 1100.0, 2700.0, 6250.0, -3000.0, 0.0, 3.8)
	despl=(600.0, 400.0)
	vect=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_inic=(0.0, 500.0)
	vel_fin=(500.0, 0.0)
	Objects.NDisplaceObject(libromagdin, despl, vect, vel_inic, vel_fin, (), (), (), "", (), LlevaLibroSello)
	angulos=(PI24, PI24, -PI24, -PI12, -PI24, PI24, PI24)
	vel_ang_inic=(0, 0.48, 0, 0.48, 0.48, 0, 0.48)
	vel_ang_fin=(0.48, 0, 0.48, 0.48, 0, 0.48, 0)
	centros=(orig, orig, orig, orig, orig, orig, orig)
	ejes=(ejeyz, ejeyz, ejeyz, ejeyz, ejeyz, ejeyz, ejeyz)
	Objects.NRotateObject(libromagdin, angulos, vel_ang_inic, vel_ang_fin, centros, ejes)

def SubeEscalon(sld_name):
	Bladex.GetEntity(sld_name).OnStopFunc=""
	nesc=int(sld_name[7:])
	if nesc==12:
		golpeescalonfinal.Play(8000.0, 1650.0-250.0*nesc, 5500.0-500.0*nesc, 0)
		polvareda1=Bladex.CreateEntity("Polvo1EscalerasFinal", "Entity Particle System D2", 7550.0, -1255.0, 3700.0)
		polvareda1.D=0.0, 0.0, -4400.0
		polvareda1.ParticleType="PolvoMedio"
		polvareda1.YGravity=0.0
		polvareda1.Friction=0.2
		polvareda1.PPS=500
		polvareda1.Velocity=750.0, -750.0, 0.0
		polvareda1.RandomVelocity=20.0
		polvareda1.Time2Live=30
		polvareda1.DeathTime=Bladex.GetTime()+6.0/60.0
		polvareda2=Bladex.CreateEntity("Polvo2EscalerasFinal", "Entity Particle System D2", 7550.0, -1255.0, 3700.0)
		polvareda2.D=1650.0, 0.0, 0.0
		polvareda2.ParticleType="PolvoMedio"
		polvareda2.YGravity=0.0
		polvareda2.Friction=0.2
		polvareda2.PPS=500
		polvareda2.Velocity=0.0, -750.0, -750.0
		polvareda2.RandomVelocity=20.0
		polvareda2.Time2Live=30
		polvareda2.DeathTime=Bladex.GetTime()+6.0/60.0
		polvareda3=Bladex.CreateEntity("Polvo3EscalerasFinal", "Entity Particle System D2", 9200.0, -1255.0, -700.0)
		polvareda3.D=0.0, 0.0, 4400.0
		polvareda3.ParticleType="PolvoMedio"
		polvareda3.YGravity=0.0
		polvareda3.Friction=0.2
		polvareda3.PPS=500
		polvareda3.Velocity=-750.0, -750.0, 0.0
		polvareda3.RandomVelocity=20.0
		polvareda3.Time2Live=30
		polvareda3.DeathTime=Bladex.GetTime()+6.0/60.0
		polvareda4=Bladex.CreateEntity("Polvo4EscalerasFinal", "Entity Particle System D2", 9200.0, -1255.0, -700.0)
		polvareda4.D=-1650.0, 0.0, 0.0
		polvareda4.ParticleType="PolvoLigero"
		polvareda4.YGravity=0.0
		polvareda4.Friction=0.2
		polvareda4.PPS=500
		polvareda4.Velocity=0.0, -750.0, 750.0
		polvareda4.RandomVelocity=20.0
		polvareda4.Time2Live=30
		polvareda4.DeathTime=Bladex.GetTime()+6.0/60.0
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musica_invocacion")) # lanza MP3
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, ElevaLibroAltar, ())
		return
	if nesc%2:
		golpeescalon1.Play(8000.0, 1650.0-250.0*nesc, 5500.0-500.0*nesc, 0)
	else:
		golpeescalon2.Play(8000.0, 1650.0-250.0*nesc, 5500.0-500.0*nesc, 0)
	polvareda=Bladex.CreateEntity("PolvoEscalon"+`nesc`, "Entity Particle System D2", 7550.0, 1600.0-250.0*nesc, 5250.0-500.0*nesc)
	polvareda.D=1650.0, 0.0, 0.0
	polvareda.ParticleType="PolvoLigero"
	polvareda.YGravity=0.0
	polvareda.Friction=0.2
	polvareda.PPS=400
	polvareda.Velocity=0.0, -750.0, 0.0
	polvareda.RandomVelocity=20.0
	polvareda.Time2Live=30
	polvareda.DeathTime=Bladex.GetTime()+6.0/60.0
	Bladex.GetEntity("Escalon"+`nesc+1`).OnStopFunc=SubeEscalon
	for n in range(1, nesc+2):
		if (nesc<11) or (nesc==11 and n>3):
			esc_n=Bladex.GetEntity("Escalon"+`n`)
			esc_n.SlideTo(esc_n.Displacement+250, 1000, 0)

def SubeEscaleras():
	Bladex.SetActionCameraMovement("ruinas_final",-3.14159/2.0,0.1,0.5)
	char=Bladex.GetEntity("Player1")
	pasos=[18, 28, 37, 47, 56, 65, 75, 85, 94, 104, 113, 123, 133, 141, 160, 172]
	for n in pasos:
		np=whrandom.randint(1, 3)
		if np==1:
			sndpaso=ruinspasopie1amz
		elif np==2:
			sndpaso=ruinspasopie2amz
		else:
			sndpaso=ruinspasopie3amz
		NetSounds.AddAnimSound(char,'Amz_ruinas_final', sndpaso, n/180.0)
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.LaunchAnmType("ruinas_final")
	char.Position=8200.0, 1131.0, 5850.0
	char.Angle=3.14159
	AuxFuncs.MoveCamFromTo(8200.0, -3200.0, -450.0, 5500.0, -5150.0, -3800.0, 8550.0, 3250.0, 7200.0, 9850.0, 1100.0, 2700.0, 8.0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+6.5, escalon1.SlideTo, (250, 1000, 0))
	espiritu1.sound.Volume=0.6
	espiritu2.sound.Volume=0.6

def EncaraEscaleras(ent_name):
	char=Bladex.GetEntity("Player1")
	char.QuickFace(3.14159)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, SubeEscaleras, ())

def EntrandoAlTemplo(sector_index, entity_name):
	if entity_name=="Player1":
		sectoresctemplo.OnEnter=""
		ScriptSkip.SkipScriptStart("EscenaFinal")
		#Bladex.DeactivateInput()
		Scorer.SetVisible(0)
		Bladex.SetListenerPosition(2)
		char=Bladex.GetEntity("Player1")
		char.GoTo(8200.0, 800.0, 5850.0)
		char.RouteEndedFunc=EncaraEscaleras





############################################################################################
## Sonidos.py


def ActivaDerrumbe(sectorindex,entityname):
	if entityname=='Player1':
		aderrumbe1.Play(-68000,0,-33000,0)
		s1.OnEnter=""

def ActivaRocaseco1(sectorindex,entityname):
	if entityname=='Player1':
		rocaseco1.Play(-77500,15000,-11750,0)
		s2.OnEnter=""

def ActivaEcoagua1(sectorindex,entityname):
	if entityname=='Player1':
		ecoagua1.Play(-69250,18000,750,0)
		s3.OnEnter=""

def ActivaAcido(sectorindex,entityname):
	if entityname=='Player1':
		acido.Play(-3000,18000,-56000,0)
		s4.OnEnter=""

def SuenaPozo(sectorindex,entityname):
	if entityname=='Player1':
		pozo1.Play(43560,7835,-47871,0)
		s5.OnEnter=""



############################################################################################
## pulsadores.py


def MueveEstaca5():
	x5, y5, z5 = est5.Position
	est5.Position = x5, est1.Position[1], z5

def MueveEstacas34():
	x3, y3, z3 = est3.Position
	x4, y4, z4 = est4.Position
	est3.Position = x3, est2.Position[1], z3
	est4.Position = x4, est2.Position[1], z4

def AbreEstacasLaberinto():
	ScriptSkip.SkipScriptStart("EscenaEntradaLaberinto")
	#Bladex.DeactivateInput()
	Scorer.SetVisible(0)
	Bladex.SetListenerPosition(2)
	AuxFuncs.MoveCamFromTo(15000, -211, 21106, 22904, -3616, 18988, 23659, -4204, 24118, 25825, -1704, 28358, 8, ReiniciaCamaraInfPozo)
	Objects.DisplaceObject(est1din, 3400.0, (0.0, 1.0, 0.0), 600.0, 600.0, "", "", "", MueveEstaca5)
	Objects.DisplaceObject(est2din, 4300.0, (0.0, 1.0, 0.0), 600.0, 600.0, "", estacasdesliz, "", MueveEstacas34)

def AbreLaberinto():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("puerta_laberinto_y_pozo"))
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, AbreEstacasLaberinto, ())
	DescongelaEnemigos(("4orc", "5orc", "6orc"))

def ActivaBajaBarra(button_name,type,x=0,y=0,z=0,xc=0,yc=0,zc=0,wcx=0,wcy=0,wcz=0,wdx=0,wdy=0,wdz=0):
	Bladex.DeactivateInput()
	puls=Bladex.GetEntity(button_name)
	puls.UseFunc=puls.HitFunc=""
	print button_name
	if button_name=="puls1":
		barra_name="barracareto"
	elif button_name=="puls2":
		barra_name="barraelefante"
	elif button_name=="puls3":
		barra_name="barrapajaro"
	else:
		barra_name="barranarizon"
	if not puls1.UseFunc and not puls2.UseFunc and not puls3.UseFunc and not puls4.UseFunc:
		Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, Objects.DisplaceObject, (Bladex.GetEntity(barra_name).Data.dinobjdata, 800.0, (0.0, 1.0, 0.0), 160.0, 160.0, clickbarra, barradesliz, clickbarra))
	else:
		Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, BajaBarra, (barra_name,))
	if x==0 and y==0 and z==0:
		Button.UseButton(button_name, 0)
		if barra_name=="barranarizon":
			Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, LanzaTrampaCuchillas, ())
	else:
		Button.HitFunc(button_name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

def BajaBarra(barra_name):
	ScriptSkip.SkipScriptStart("EscenaBaja"+barra_name)
	Scorer.SetVisible(0)
	Bladex.SetListenerPosition(2)
	AuxFuncs.MoveCamFromTo(20450, -550, 23750, 21450, -550, 22850, 29850, -2600, 26450, 29850, -1800, 28150, 6, ReiniciaCamaraInfPozo)
	Objects.DisplaceObject(Bladex.GetEntity(barra_name).Data.dinobjdata, 800.0, (0.0, 1.0, 0.0), 160.0, 160.0, clickbarra, barradesliz, clickbarra)





##############################################################################
#	Musicas.py


def ApagaMusicaAlEntrar(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("emptyloquesea"))

def EnciendeMusicaExteriorAntes(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("exterior_antes"))

def EnciendeMusicaExteriorDespues(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("exterior_despues"))

def EnciendeMusicaLabInt(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("laberinto_e_interiores"))

def EnciendeMusicaSubterraneos(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("catacumbas"))

def EnciendeMusicaMausoleo(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("mausoleo"))

def EnciendeMusicaTemploFinal(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("templo_final"))
