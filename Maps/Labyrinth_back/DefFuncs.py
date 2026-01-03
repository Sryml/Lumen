import Bladex
import Ontake
import EnemyTypes
import ReadGSFile
import Enm_Gen
import B3DLib
import Traps_C
import GameText
import AuxFuncs
import Scorer
import Sounds
import EnmGenRnd
import ReadGSFile
import Actions
import Reference
import Sounds
import stone
import heavyObjects
import Room
import Button
import GotoMapVars
import ScriptSkip
import GenFX
import BackMisc
import MusicTool





#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para positions.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def IrPosicion1():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=0, -3000, -8000			# sala del trono

def IrPosicion2():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=0, 0, 45000			# Puerta castillo

def IrPosicion3():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=0, 0, -48000			# estanque

def IrPosicion4():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=0, 4000, -17000			# pasadizo de escape

def IrPosicion5():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=0, -2000, 31000			# Puerta torre central

def IrPosicion6():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=0, -27500, -15000		# habitacion duque

def IrPosicion7():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=46000, -4000.0, 28500.0	# puente laberinto

def IrPosicion8():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=8000.0, 825.0, 12450.0	# final

def IrPosicion9():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=32400, -3350, -33360		# fuentes




#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								********************
#*******************************   Definiciones para labyr_back.py            ********************
#*******************************								********************
#*************************************************************************************************
#*************************************************************************************************

### Surtidores ###

def Fuentes():
	fuente1=Bladex.CreateEntity("Fuente1", "Entity Particle System D1", 2615.878000,-75.000000,38543.549000)
	fuente1.ParticleType="Agua"
	fuente1.PPS=128
	fuente1.YGravity=7000.0
	fuente1.Friction=0.08
	fuente1.Velocity=0.0, 0.0, 1400.0
	fuente1.RandomVelocity=5.0
	fuente1.Time2Live=20
	fuente2=Bladex.CreateEntity("Fuente2", "Entity Particle System D1", -2627.899000,-75.000000,38540.703000)
	fuente2.ParticleType="Agua"
	fuente2.PPS=128
	fuente2.YGravity=7000.0
	fuente2.Friction=0.08
	fuente2.Velocity=0.0, 0.0, 1400.0
	fuente2.RandomVelocity=5.0
	fuente2.Time2Live=20

def Cascadas():
	cascadaestanque=Bladex.CreateEntity("CascadaEstanque", "Entity Particle System D2",-750,2450,-54000) #2100,-54000)
	cascadaestanque.D=1500.0, 0.0, 0.0
	cascadaestanque.ParticleType="AguaC"
	cascadaestanque.PPS=800
	cascadaestanque.Time2Live=20
	cascadaestanque.Velocity=0.0, 0.0, -2500.0
	cascadaestanque.RandomVelocity=10.0
	cascadaestanque.Friction=0.07
	cascadaestanque.YGravity=9800
	cascadapozo=Bladex.CreateEntity("CascadaPozo", "Entity Particle System D2", 12900.0,4950.0,-26450.0)
	cascadapozo.D=0.0, 0.0, 900.0
	cascadapozo.ParticleType="AguaC"
	cascadapozo.PPS=400
	cascadapozo.Time2Live=40
	cascadapozo.Friction=0.1
	cascadapozo.RandomVelocity=5.0
	cascadapozo.Velocity=2000.0, 0.0, 0.0
	cascadapozo.YGravity=9800
	espest=Bladex.CreateEntity("EspumaEstanque", "Entity Particle System D2", -700,5000,-54900)
	espest.D=1400.0, 0.0, 0.0
	espest.ParticleType="Espuma"
	espest.PPS=200
	espest.YGravity=0.0
	espest.Friction=0.07
	espest.Velocity=0.0, -1000.0, 0.0
	espest.RandomVelocity=30.0
	espest.RandomVelocity_V=30.0
	espest.Time2Live=10
	salpest=Bladex.CreateEntity("SalpiqueEstanque", "Entity Particle System D2", -700,5000,-54900)
	salpest.D=1400.0, 0.0, 0.0
	salpest.ParticleType="Salpique"
	salpest.PPS=250
	salpest.YGravity=4000.0
	salpest.Friction=0.07
	salpest.Velocity=0.0, -3000.0, 0.0
	salpest.RandomVelocity=30.0
	salpest.RandomVelocity_V=30.0
	salpest.Time2Live=25
	esppozo=Bladex.CreateEntity("EspumaPozo", "Entity Particle System D2", 13650.0,11250.0,-26250.0)
	esppozo.D=0.0, 0.0, 800.0
	esppozo.ParticleType="Espuma"
	esppozo.PPS=160
	esppozo.YGravity=0.0
	esppozo.Friction=0.07
	esppozo.Velocity=0.0, -1000.0, 0.0
	esppozo.RandomVelocity=30.0
	esppozo.RandomVelocity_V=30.0
	esppozo.Time2Live=10
	salppozo=Bladex.CreateEntity("SalpiquePozo", "Entity Particle System D2", 13650.0,11250.0,-26250.0)
	salppozo.D=0.0, 0.0, 800.0
	salppozo.ParticleType="Salpique"
	salppozo.PPS=250
	salppozo.YGravity=4000.0
	salppozo.Friction=0.07
	salppozo.Velocity=0.0, -3000.0, 0.0
	salppozo.RandomVelocity=30.0
	salppozo.RandomVelocity_V=30.0
	salppozo.Time2Live=25





#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para puertas.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

#def RompePuertaInfTorreEN():
#	puitoen.DoBreak((3.0, 0.0, 3.0), (51375, 0, 12375), (0.0, 0.0, 0.0))

def AbrePuertaSupTorreEN():
	pustoen.OpenDoor()
	pers=Bladex.GetEntity("7ORC")
	if pers and pers.Life>0 and pers.Deaf:
		pers.Deaf=0
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("susto"))

#def RompePuertaSupTorreES():
#	pustoes.DoBreak((0.0, 0.0, -4.0), (57750, -8000, -9375), (0.0, 0.0, 0.0))

#def RompePuertaInfTorreOS():
#	puitoos.DoBreak((-3.0, 0.0, -3.0), (-51375, 0, -12375), (0.0, 0.0, 0.0))

#def RompePuertaSupTorreON():
#	pustoon.DoBreak((0.0, 0.0, 4.0), (-57750, -8000, 9375), (0.0, 0.0, 0.0))

def AbreRasanexo():
	desplazamientos=(2000.0, 600.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(500.0, 4000)
	vel_finales=(4000.0, 500)
	son_durante=(deslizrasanexo, deslizrasanexo)
	son_finales=("", golperasanexo)
	Objects.NDisplaceObject(rasanexodin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def CierraRasanexo():
	desplazamientos=(2000.0, 600.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(500.0, 4000)
	vel_finales=(4000.0, 500)
	son_durante=(deslizrasanexo, deslizrasanexo)
	son_finales=("", golperasanexo)
	Objects.NDisplaceObject(rasanexodin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def AbreRasanexe():
	desplazamientos=(2000.0, 600.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(500.0, 4000)
	vel_finales=(4000.0, 500)
	son_durante=(deslizrasanexe, deslizrasanexe)
	son_finales=("", golperasanexe)
	Objects.NDisplaceObject(rasanexedin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def CierraRasanexe():
	desplazamientos=(2000.0, 600.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(500.0, 4000)
	vel_finales=(4000.0, 500)
	son_durante=(deslizrasanexe, deslizrasanexe)
	son_finales=("", golperasanexe)
	Objects.NDisplaceObject(rasanexedin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

#def RompePuertaTorreCen():
#	putocen.DoBreak((0.0, 0.0, -9.0), (0, -3000, 24750), (0.0, 0.0, 0.0))


def AbreRasalc():
	desplazamientos=(2500.0, 750.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(500.0, 4000)
	vel_finales=(4000.0, 500)
	son_durante=(deslizrasalc, deslizrasalc)
	son_finales=("", golperasalc)
	Objects.NDisplaceObject(rasalcdin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def CierraRasalc():
	desplazamientos=(2500.0, 750.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(500.0, 4000)
	vel_finales=(4000.0, 500)
	son_durante=(deslizrasalc, deslizrasalc)
	son_finales=("", golperasalc)
	Objects.NDisplaceObject(rasalcdin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)




#def RompePuertas():
#	RompePuertaInfTorreEN()
#	RompePuertaSupTorreES()
#	RompePuertaInfTorreOS()
#	RompePuertaSupTorreON()
#	RompePuertaTorreCen()




#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para tablilla.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def CaidaMuroAgua():
	espmuroagua=Bladex.CreateEntity("EspumaMuroAgua", "Entity Particle System D3", 3250.0, 5250.0, -26500.0)
	espmuroagua.D1=0.0, 0.0, -2000.0
	espmuroagua.D2=4000.0, 0.0, -1000.0
	espmuroagua.ParticleType="Espuma2"
	espmuroagua.PPS=80
	espmuroagua.YGravity=800.0
	espmuroagua.Friction=0.05
	espmuroagua.Velocity=0.0, -2000.0, 0.0
	espmuroagua.RandomVelocity=30.0
	espmuroagua.Time2Live=60
	espmuroagua.DeathTime=Bladex.GetTime()+1.0
	salpmuroagua=Bladex.CreateEntity("SalpiqueMuroAgua", "Entity Particle System D3", 3250.0, 5250.0, -26500.0)
	salpmuroagua.D1=0.0, 0.0, -2000.0
	salpmuroagua.D2=4000.0, 0.0, -1000.0
	salpmuroagua.ParticleType="Salpique"
	salpmuroagua.PPS=512
	salpmuroagua.YGravity=3000.0
	salpmuroagua.Friction=0.07
	salpmuroagua.Velocity=0.0, -4000.0, 0.0
	salpmuroagua.RandomVelocity=50.0
	salpmuroagua.RandomVelocity_V=30.0
	salpmuroagua.Time2Live=30
	salpmuroagua.DeathTime=Bladex.GetTime()+1.5
	golpemuroagua.PlaySound(0)

def DisipaTemblor(ent_name, time):
	cam=Bladex.GetEntity("Camera")
	if cam.EarthQuakeFactor>8:
		cam.EarthQuakeFactor=cam.EarthQuakeFactor-8
	else:
		cam.RemoveFromList("Timer10")
		cam.TimerFunc=""
		cam.EarthQuake=0

def RompeMuroSecreto():
	cam=Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor=100
	cam.EarthQuake=1
	cam.TimerFunc=DisipaTemblor
	cam.SubscribeToList("Timer10")
	muroruna1.DoBreak((1.1, -0.9, 0.0), (3000, 4500, -26375), (0.0, 0.0, 0.0))
	muroruna2.DoBreak((1.0, -0.9, 0.0), (3000, 3750, -26375), (0.0, 0.0, 0.0))
	muroruna3.DoBreak((0.9, -0.9, 0.0), (3000, 3000, -26375), (0.0, 0.0, 0.0))
	muroruna4.DoBreak((1.2, -0.9, 0.0), (3000, 4500, -27500), (0.0, 0.0, 0.0))
	muroruna5.DoBreak((1.1, -0.9, 0.0), (3000, 4500, -28375), (0.0, 0.0, 0.0))
	muroruna6.DoBreak((1.0, -0.9, 0.0), (3000, 3500, -28375), (0.0, 0.0, 0.0))
	muroruna7.DoBreak((0.9, -0.9, 0.0), (3000, 2750, -28375), (0.0, 0.0, 0.0))
	muroruna8.DoBreak((0.9, -0.9, 0.0), (3000, 2250, -27000), (0.0, 0.0, 0.0))
	muroruna9.DoBreak((1.0, -0.9, 0.0), (3000, 2000, -27500), (0.0, 0.0, 0.0))
	muroruna10.DoBreak((0.9, -0.9, 0.0), (3000, 2400, -28000), (0.0, 0.0, 0.0))
	roturamuroruna.PlaySound(0)
	pruna=Bladex.GetEntity("PulsadorRuna")
	pcaido=Bladex.GetEntity("PulsadorRunaCaido")
	pcaido.Position=pruna.Position
	pruna.RemoveFromWorld()
	pcaido.PutToWorld()
	pcaido.Impulse(10000,-1000,0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.2, CaidaMuroAgua, ())

def EmpujaPulsadorRuna(ent_name, event):
	char=Bladex.GetEntity("Player1")
	Objects.DisplaceObject(pulrunadin, 325.0, (1.0, 0.0, 0.0), 200.0, 200.0, "", deslizpulruna, "", "", (), RompeMuroSecreto, ())
	char.DelAnmEventFunc("Activate")
	char.Data.obj_used=None
	import MenuText
	Reference.EntitiesSelectionData["PulsadorRuna"]=(9.0,10.0, MenuText.GetMenuText("Rune"))

def LanzaEmpujaPulsadorRuna(obj_name, use_from):
	pulruna.UseFunc=""
	char=Bladex.GetEntity("Player1")
	Actions.QuickTurnToFaceEntity ("Player1","PulsadorRuna")
	char.LaunchAnmType("pulsador")
	char.Data.obj_used=pulruna
	char.AddAnmEventFunc("Activate",EmpujaPulsadorRuna)

### Chequeadores

def FlameDamage(prtl_name,hit_entity,x,y,z,vx,vy,vz,wcx,wcy,wcz,wdx,wdy,wdz):
	if hit_entity=="Player1":
		char=Bladex.GetEntity("Player1")
		if char.Life>0:
			char.Life=char.Life-5

def EnciendeLuzLlamGrad(ent_name, time):
	luzllamarada=Bladex.GetEntity(ent_name)
	luzllamarada.Intensity=luzllamarada.Intensity+0.2
	if luzllamarada.Intensity>=4.0:
		luzllamarada.RemoveFromList("Timer60")
		luzllamarada.TimerFunc=""

def EnciendeLuzLlamarada(flame_n):
	luzllamarada=Bladex.GetEntity("Luz"+`flame_n`)
	luzllamarada.Intensity=0.0
	luzllamarada.TimerFunc=EnciendeLuzLlamGrad
	luzllamarada.SubscribeToList("Timer60")

def ApagaLuzLlamGrad(ent_name, time):
	luzllamarada=Bladex.GetEntity(ent_name)
	luzllamarada.Intensity=luzllamarada.Intensity-0.2
	if luzllamarada.Intensity<=0.0:
		luzllamarada.RemoveFromList("Timer60")

def ApagaLuzLlamarada(flame_n):
	luzllamarada=Bladex.GetEntity("Luz"+`flame_n`)
	luzllamarada.Intensity=4.0
	luzllamarada.TimerFunc=ApagaLuzLlamGrad
	luzllamarada.SubscribeToList("Timer60")

def LanzaSurtidor(flame_n):
	global tractivada
	if tractivada:
		pos=Bladex.GetEntity("LP"+`flame_n`).Position
		if flame_n==2:
			s=-1
		else:
			s=1
		llamarada=Bladex.CreateEntity("Llamarada"+`flame_n`, "Entity Particle System D1", pos[0], 12000, pos[2])
		llamarada.ParticleType="Flame"
		llamarada.YGravity=-4900.0
		llamarada.Friction=0.12
		llamarada.PPS=260
		llamarada.Velocity=s*12000.0, 0.0, 0.0
		llamarada.RandomVelocity=30.0
		llamarada.Time2Live=21
		llamarada.DeathTime=Bladex.GetTime()+0.75
		sonidollamarada.Play(pos[0]+s*1000.0, 12500.0, pos[2], 0)
		EnciendeLuzLlamarada(flame_n)
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.75, ApagaLuzLlamarada, (flame_n,))
		if flame_n==1:
			chllama1.startCheck(llamarada, 0.72)
			flame_n=flame_n+1
		elif flame_n==2:
			chllama2.startCheck(llamarada, 0.72)
			flame_n=flame_n+1
		else:
			chllama3.startCheck(llamarada, 0.72)
			flame_n=1
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, LanzaSurtidor, (flame_n,))

def GiraCuchillas():
	Objects.RotateObject(cuchizqdin, VUELTASDURANTE, VELGIRO, VELGIRO, (0.0, 0.0, 0.0), (0, 1, 0), Objects.REL, "", "", "", "", (), GiraCuchillas, ())
	Objects.RotateObject(cuchderdin, VUELTASDURANTE, VELGIRO, VELGIRO, (0.0, 0.0, 0.0), (0, -1, 0))

def IniciaGiraCuchillas():
	Objects.RotateObject(cuchizqdin, VUELTASINICIO, 0.0, VELGIRO, (0.0, 0.0, 0.0), (0, 1, 0), Objects.REL, "", "", "", "", (), GiraCuchillas, ())
	Objects.RotateObject(cuchderdin, VUELTASINICIO, 0.0, VELGIRO, (0.0, 0.0, 0.0), (0, -1, 0))

def TerminaGiraCuchillas():
	Objects.RotateObject(cuchizqdin, VUELTASFIN, VELGIRO, 0.0, (0.0, 0.0, 0.0), (0, 1, 0))
	Objects.RotateObject(cuchderdin, VUELTASFIN, VELGIRO, 0.0, (0.0, 0.0, 0.0), (0, -1, 0))

def RecolocaCuchilla(ncuchilla):
	despl=(1000.0, 7000.0, 1000.0)
	vect=((0.0, 0.0, -1.0), (0.0, 0.0, -1.0), (0.0, 0.0, -1.0))
	vel_inic=(0.0, 6000.0, 6000.0)
	vel_fin=(6000.0, 6000.0, 0.0)
	if ncuchilla==1:
		son_durante=(sonido2cuchilla1, sonido2cuchilla1, sonido2cuchilla1)
		Objects.NDisplaceObject(cuchizqdin, despl, vect, vel_inic, vel_fin, (), son_durante, (), "", (), LanzaCuchilla, (1,))
	else:
		son_durante=(sonido2cuchilla2, sonido2cuchilla2, sonido2cuchilla2)
		Objects.NDisplaceObject(cuchderdin, despl, vect, vel_inic, vel_fin, (), son_durante, (), "", (), LanzaCuchilla, (2,))

def RecogeCuchilla(ncuchilla):
	if ncuchilla==1:
		Objects.DisplaceObject(cuchizqdin, 2200.0, (-1.0, 0.0, 0.0), 10000.0, 6000.0, sonido1cuchilla1, "", "", "", (), RecolocaCuchilla, (1,))
	else:
		Objects.DisplaceObject(cuchderdin, 2200.0, (1.0, 0.0, 0.0), 10000.0, 6000.0, sonido1cuchilla2, "", "", "", (), RecolocaCuchilla, (2,))

def DesplazaCuchilla(ncuchilla):
	despl=(1000.0, 7000.0, 1000.0)
	vect=((0.0, 0.0, 1.0), (0.0, 0.0, 1.0), (0.0, 0.0, 1.0))
	vel_inic=(0.0, 6000.0, 6000.0)
	vel_fin=(6000.0, 6000.0, 0.0)
	if ncuchilla==1:
		son_durante=(sonido2cuchilla1, sonido2cuchilla1, sonido2cuchilla1)
		Objects.NDisplaceObject(cuchizqdin, despl, vect, vel_inic, vel_fin, (), son_durante, (), "", (), RecogeCuchilla, (1,))
	else:
		son_durante=(sonido2cuchilla2, sonido2cuchilla2, sonido2cuchilla2)
		Objects.NDisplaceObject(cuchderdin, despl, vect, vel_inic, vel_fin, (), son_durante, (), "", (), RecogeCuchilla, (2,))

def LanzaCuchilla(ncuchilla):
	global tractivada
	if tractivada:
		if ncuchilla==1:
			cuchizq.MessageEvent(MESSAGE_START_WEAPON,0,0)
			Objects.DisplaceObject(cuchizqdin, 2200.0, (1.0, 0.0, 0.0), 6000.0, 10000.0, sonido1cuchilla1, "", "", "", (), DesplazaCuchilla, (1,))
		else:
			cuchder.MessageEvent(MESSAGE_START_WEAPON,0,0)
			Objects.DisplaceObject(cuchderdin, 2200.0, (-1.0, 0.0, 0.0), 6000.0, 10000.0, sonido1cuchilla2, "", "", "", (), DesplazaCuchilla, (2,))
	else:
		cuchizq.MessageEvent(MESSAGE_STOP_WEAPON,0,0)
		cuchder.MessageEvent(MESSAGE_STOP_WEAPON,0,0)
		TerminaGiraCuchillas()

def ParaTrampa(sec_index, ent_name):
	global tractivada
	if ent_name=="Player1":
		sectorparatrampa.OnEnter=""
		sonidoactdes.Play(22875.0, 11000.0, -9750.0, 0)
		tractivada=0
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("alcantytabvue"))

def LanzaTrampa(sec_index, ent_name):
	global tractivada
	if ent_name=="Player1":
		sectorlanzatrampa.OnEnter=""
		sonidoactdes.Play(22875.0, 11000.0, -9750.0, 0)
		tractivada=1
		LanzaSurtidor(1)
		IniciaGiraCuchillas()
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, LanzaCuchilla, (1,))
		Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, LanzaCuchilla, (2,))

def AbreTrampa():
	sectorlanzatrampa.OnEnter=LanzaTrampa
	sectorparatrampa.OnEnter=ParaTrampa
	despl=(600.0, 1800.0)
	vectizq=((-1.0, 0.0, 0.0), (-1.0, 0.0, 0.0))
	vectder=((1.0, 0.0, 0.0), (1.0, 0.0, 0.0))
	vel_inic=(200.0, 1000)
	vel_fin=(1000.0, 200)
	son_durizq=(deslizpasizq, deslizpasizq)
	son_finizq=("", golpepasizq)
	son_durder=(deslizpasder, deslizpasder)
	son_finder=("", golpepasder)
	Objects.NDisplaceObject(pasarelaizqdin, despl, vectizq, vel_inic, vel_fin, (), son_durizq, son_finizq)
	Objects.NDisplaceObject(pasareladerdin, despl, vectder, vel_inic, vel_fin, (), son_durder, son_finder)

def CierraTrampa():
	despl=(600.0, 1800.0)
	vectizq=((1.0, 0.0, 0.0), (1.0, 0.0, 0.0))
	vectder=((-1.0, 0.0, 0.0), (-1.0, 0.0, 0.0))
	vel_inic=(200.0, 1000)
	vel_fin=(1000.0, 200)
	son_durizq=(deslizpasizq, deslizpasizq)
	son_finizq=("", golpepasizq)
	son_durder=(deslizpasder, deslizpasder)
	son_finder=("", golpepasder)
	Objects.NDisplaceObject(pasarelaizqdin, despl, vectizq, vel_inic, vel_fin, (), son_durizq, son_finizq)
	Objects.NDisplaceObject(pasareladerdin, despl, vectder, vel_inic, vel_fin, (), son_durder, son_finder)

def RecolocaTablilla():
	global var1
	global var2
	global var3
	char=Bladex.GetEntity("Player1")
	if char.CharType[:2]=="Dw":
		var1=151
		var2=108
		var3=139
	elif char.CharType[:2]=="Ba":
		var1=-239
		var2=-300
		var3=-312
	elif char.CharType[:2]=="Am":
		var1=-86
		var2=-88
		var3=74
	else:
		var1=0
		var2=0
		var3=0
	tab.Move(0,var1,0)
	luztab.Move(0,var1,0)

def ParticulasTablilla():
	RecolocaTablilla()
	luzsolida=Bladex.CreateEntity("LuzSolidaTablilla", "Entity Particle System D2", 33000.0, 10950.0, 1000.0)
	luzsolida.D=0.0, -3500.0, 0.0
	luzsolida.ParticleType="LuzSolida"
	luzsolida.YGravity=0.0
	luzsolida.Friction=0.01
	luzsolida.PPS=5
	luzsolida.Velocity=-100.0, 0.0, 0.0
	luzsolida.RandomVelocity=5.0
	luzsolida.Time2Live=240
	luzmagica=Bladex.CreateEntity("LuzMagicaTablilla", "Entity Particle System D1", 33000.0, 5750.0, 1000.0)
	luzmagica.ParticleType="LuzMagica"
	luzmagica.YGravity=0.0
	luzmagica.Friction=0.01
	luzmagica.PPS=35
	luzmagica.Velocity=0.0, 100.0, 0.0
	luzmagica.RandomVelocity=6.0
	luzmagica.Time2Live=120
	dat_pos=[33252.816, 9704.169, 636.788, 33265.5, 9722.301, 1276.408, 33008.684, 10127.771, 1270.006, 32996.004, 10109.638, 630.386]
	dat_D=[12.684, 18.132, 639.62, -256.816, 405.47, -6.402, -12.68, -18.133, -639.62, 256.812, -405.469, 6.402]
	for n in range(4):
		for l in ("u", "d"):
			cl=Bladex.CreateEntity("EnergiaTablilla"+`n+1`+l, "Entity Particle System D2", dat_pos[0+n*3], dat_pos[1+n*3]+var1, dat_pos[2+n*3])
			cl.D=dat_D[0+n*3], dat_D[1+n*3], dat_D[2+n*3]
			cl.ParticleType="Energia"
			if l=="u":
				cl.YGravity=-75.0
			else:
				cl.YGravity=75.0
			cl.Friction=0.0
			cl.PPS=20
			cl.Velocity=0.0, 0.0, 0.0
			cl.Time2Live=70

def Repite():
	luztab.Intensity=0.8
	tab.Alpha=1.0
	char.Position=20995.498, 9959.623, 977.119
	tab.Position=33137.0674797, 9898.73625443+var1, 910.410864308
	tab.Orientation=0.61795938015, 0.329014241695, 0.620333433151, -0.353641480207
	luztab.Position=32797.7392561, 9892.42437652+var1, 910.410864308
	dat_pos=[33252.816, 9704.169, 636.788, 33265.5, 9722.301, 1276.408, 33008.684, 10127.771, 1270.006, 32996.004, 10109.638, 630.386]
	dat_D=[12.684, 18.132, 639.62, -256.816, 405.47, -6.402, -12.68, -18.133, -639.62, 256.812, -405.469, 6.402]
	for n in range(4):
		for l in ("u", "d"):
			cl=Bladex.CreateEntity("EnergiaTablilla"+`n+1`+l, "Entity Particle System D2", dat_pos[0+n*3], dat_pos[1+n*3]+var1, dat_pos[2+n*3])
			cl.D=dat_D[0+n*3], dat_D[1+n*3], dat_D[2+n*3]
			cl.ParticleType="Energia"
			if l=="u":
				cl.YGravity=-75.0
			else:
				cl.YGravity=75.0
			cl.Friction=0.0
			cl.PPS=20
			cl.Velocity=0.0, 0.0, 0.0
			cl.Time2Live=70

def AbrePuertaTablilla():
	golpehojader.Volume=0.6
	#golpehojaizq.Volume=0.6
	hojaizq.OpenDoor()
	hojader.OpenDoor()

def CierraPuertaTablilla2():
	polvareda=Bladex.CreateEntity("PolvoPuertaTablilla", "Entity Particle System D2", 26625.5, 10950.0, 1000.0)
	polvareda.D=0.0, -4650.0, 0.0
	polvareda.ParticleType="MediumDust"
	polvareda.YGravity=0.0
	polvareda.Friction=0.2
	polvareda.PPS=512
	polvareda.Velocity=-750.0, 0.0, 0.0
	polvareda.RandomVelocity=20.0
	polvareda.Time2Live=30
	polvareda.DeathTime=Bladex.GetTime()+6.0/60.0

def CierraPuertaTablilla():
	golpehojader.Volume=1.0
	#golpehojaizq.Volume=1.0
	hojaizq.CloseDoor()
	hojader.CloseDoor()

def EnciendeLuzGrad(ent_name, time):
	global fireint
	fireint=fireint-0.3
	lantpaltab.Intensity=lantpaltab.Intensity+0.2
	lantpaltab.SizeFactor=lantpaltab.SizeFactor+0.016
	fantpaltab.Intensity=fireint
	if lantpaltab.Intensity>=6.0:
		fireint=0.0
		lantpaltab.Intensity=6.0
		lantpaltab.SizeFactor=1.0
		fantpaltab.Intensity=0.0
		lantpaltab.RemoveFromList("Timer10")
		lantpaltab.TimerFunc=""
	pasarelaizq.Move(0,0,0)
	pasarelader.Move(0,0,0)

def EnciendeLuz():
	lantpaltab.Precission=0.1
	lantpaltab.TimerFunc=EnciendeLuzGrad
	lantpaltab.SubscribeToList("Timer10")

def ReduceLuzGrad(ent_name, time):
	global fireint
	fireint=fireint+0.3
	lantpaltab.Intensity=lantpaltab.Intensity-0.2
	lantpaltab.SizeFactor=lantpaltab.SizeFactor-0.016
	fantpaltab.Intensity=fireint
	if lantpaltab.Intensity<=0.4:
		fireint=8.3
		lantpaltab.Intensity=0.4
		lantpaltab.SizeFactor=0.534
		fantpaltab.Intensity=8.3
		lantpaltab.RemoveFromList("Timer10")
	pasarelaizq.Move(0,0,0)
	pasarelader.Move(0,0,0)

def ReduceLuz():
	lantpaltab.Precission=0.0625
	lantpaltab.TimerFunc=ReduceLuzGrad
	lantpaltab.SubscribeToList("Timer10")

def FinalEscenaTablilla(camera, frame):
	global tablillacogida
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Bladex.SetListenerPosition(1)
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)
	tablillacogida=1
	EnciendeLuz()
	AbreTrampa()
	GenFX.CreateMagicTransport("transp9", (20500, 850, -35000))
	GenFX.CreateMagicTransport("transp10", (-10000, 850, -40500))
	GenFX.CreateMagicTransport("transp11", (24000, 9350, -29000))
	GenFX.CreateMagicTransport("transp12", (-1500, 4850, -30000))

def MueveLuz(ent_name, time):
	luztab.Position=(tab.Position[0]+char.Position[0])/2.0, (5.0*tab.Position[1]+char.Position[1])/6.0, tab.Position[2]

def CogeTablilla(camera, frame):
	GameText.WriteText("M6T4")
	#Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musica_tablilla"))
	GotoMapVars.MapText(6,"TT")
	char=Bladex.GetEntity("Player1")
	inv=char.GetInventory()
	inv.AddTablet("Tablilla2")
	inv.LinkLeftHand("Tablilla2")
	luztab.TimerFunc=MueveLuz
	luztab.SubscribeToList("Timer60")
	for n in range(4):
		for l in ("u", "d"):
			cl=Bladex.GetEntity("EnergiaTablilla"+`n+1`+l)
			cl.PPS=600
			cl.Time2Live=50
			cl.DeathTime=2.0/60.0

def PolvoTablilla(camera, frame) :
	polvotab=Bladex.CreateEntity("PolvoTablilla", "Entity Particle System D1", 32830.34, 9712.755+var2, 696.075)
 	polvotab.ParticleType="Polvillo"
	polvotab.YGravity=0.0
	polvotab.Friction=0.3
	polvotab.PPS=40
	polvotab.Velocity=0, -1000.0, -1000.0
	polvotab.RandomVelocity=10.0
	polvotab.Time2Live=60
	polvotab.DeathTime=Bladex.GetTime()+20.0/60.0

def DesapareceTablillaGrad(ent_name, time):
	tab.Alpha=tab.Alpha-TABTRVAR
	luztab.Intensity=luztab.Intensity-TABINTVAR
	if tab.Alpha<=0:
		tab.RemoveFromList("Timer60")
		tab.TimerFunc=""
		tab.Alpha=0.0
		luztab.Intensity=0.0

def LanzaEstelaChispas(ent_name, time):
	global estela
	global init_est_time
	global vdespl
	curr_est_time=time-init_est_time
	frac_var=curr_est_time/TABESTTIME
	estela.Position=tab.Position[0]+vdespl[0]*frac_var, tab.Position[1]+vdespl[1]*frac_var, tab.Position[2]+vdespl[2]*frac_var
	if curr_est_time>=TABESTTIME:
		estela.RemoveFromList("Timer60")
		estela.TimerFunc=""
		estela.PPS=200
		estela.RandomVelocity=40   
		estela.DeathTime=Bladex.GetTime()+0.5
		tab.RemoveFromWorld()
		luztab.RemoveFromWorld()

def Incandescencia(camera, frame):
	dat_pos=[32452, 8825, 1329, 32452, 8825, 689, 32850, 9094, 689, 32850, 9094, 1329]
	dat_D=[0, 0, -640, 398, 269, 0, 0, 0, 640, -398, -269, 0]
	for n in range(4):
		inc=Bladex.CreateEntity("Energia2Tablilla"+`n+1`, "Entity Particle System D2", dat_pos[0+n*3], dat_pos[1+n*3]+var3, dat_pos[2+n*3])
		inc.D=dat_D[0+n*3], dat_D[1+n*3], dat_D[2+n*3]
		inc.ParticleType="Energia2"
		inc.YGravity=0.0
		inc.Friction=0.01
		inc.PPS=200
		inc.Velocity=0.0, 0.0, 0.0
		inc.RandomVelocity=4.0
		inc.Time2Live=60
		inc.DeathTime=1.0

def DesapareceTablilla(camera, frame):
	global estela
	global init_est_time
	global vdespl
	char=Bladex.GetEntity("Player1")
	estela=Bladex.CreateEntity("EstelaChispas", "Entity Particle System D1", 0.0, 0.0, 0.0)
	estela.Position=tab.Position
	estela.ParticleType="Chispas"
	estela.YGravity=200
	estela.Friction=0.2
	estela.PPS=100
	estela.Velocity=0.0, 0.0, 0.0
	estela.RandomVelocity=10
	estela.Time2Live=60
	init_est_time=Bladex.GetTime()
	vdespl=char.Position[0]-tab.Position[0], char.Position[1]-tab.Position[1], char.Position[2]-tab.Position[2]
	estela.TimerFunc=LanzaEstelaChispas
	estela.SubscribeToList("Timer60")
	tab.TimerFunc=DesapareceTablillaGrad
	tab.SubscribeToList("Timer60")
	inv=char.GetInventory()
	inv.LinkLeftHand("None")
	tab.PutToWorld()
	luztab.RemoveFromList("Timer60")
	luztab.TimerFunc=""


def ContinuaEscenaTablilla():
	cam=Bladex.GetEntity("Camera")
	char=Bladex.GetEntity("Player1")
	pasostabl=[11, 21, 31, 41, 51, 61, 71, 81, 90, 99, 114, 128]
	for n in pasostabl:
		np=whrandom.randint(1, 3)
		if np==1:
			sndpaso=labyrpasopie1
		elif np==2:
			sndpaso=labyrpasopie2
		else:
			sndpaso=labyrpasopie3
		NetSounds.AddAnimSound(char, char.CharTypeExt[:3]+'_tablilla_laberinto', sndpaso, n/513.0)
	char.Wuea=Reference.WUEA_ENDED
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.LaunchAnmType("tablilla_laberinto")
	char.Position=20995.498, 9959.623, 977.119
	char.Angle=3.14159
	char.SetOnFloor()
	cam.SetMaxCamera("tablilla_lab_cam.cam",0,513)
	cam.AddCameraEvent(-1,FinalEscenaTablilla)
	cam.AddCameraEvent(146,CogeTablilla)
	cam.AddCameraEvent(190,PolvoTablilla)
	cam.AddCameraEvent(205,PolvoTablilla)
	cam.AddCameraEvent(420,Incandescencia)
	cam.AddCameraEvent(425,DesapareceTablilla)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musica_tablilla"))


def InicioEscenaTablilla2():
	Bladex.SetListenerPosition(2)
	AuxFuncs.MoveCamFromTo(24275.0, 6875.0, 3675.0, 21125.0, 8090.0, 3475.0, 24000.0, 11500.0, -2500.0, 29900.0, 10065.0, -925.0, 5.5, "")


def InicioEscenaTablilla():
	global tablillacogida
	if tablillacogida:
		AbrePuertaTablilla()
		return
	BackMisc.DeactivateChaos()
	Scorer.SetVisible(0)
	ScriptSkip.SkipScriptStart("EscenaTablilla")
	#Bladex.DeactivateInput()
	Actions.TurnToFaceEntity("Player1", "Tablilla2")
	ReduceLuz()
	Bladex.AddScheduledFunc(Bladex.GetTime()+4.5, InicioEscenaTablilla2, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, Actions.FreeBothHands, ("Player1",))
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, AbrePuertaTablilla, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+10.5, ContinuaEscenaTablilla, ())




#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************							**************************
#*******************************	Definiciones para Musica.py		**************************
#*******************************							**************************
#*************************************************************************************************
#*************************************************************************************************


def EnciendeMusicaTablilla(trsector_name, entity_name):
	global tablillacogida
	if entity_name=="Player1":
		if tablillacogida:
			Bladex.ExeMusicEvent(Bladex.GetMusicEvent("alcantytabvue"))
		else:
			Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musicatablida"))

def EnciendeMusicaTrampaTablilla(trsector_name, entity_name):
	global tablillacogida
	if entity_name=="Player1":
		if tablillacogida:
			Bladex.ExeMusicEvent(Bladex.GetMusicEvent("entradatrampa"))
			Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musicatrampatabl"))
			Bladex.RemoveTriggerSectorFunc("TrampaTablilla", "OnEnter")

def EnciendeMusica1Anillo(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musica1anillo"))

def EnciendeMusica2Anillo(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musica2anillo"))

def EnciendeMusicaAlcantarillas(trsector_name, entity_name):
	global alcantarillasvistas
	if entity_name=="Player1":
		if not alcantarillasvistas:
			Bladex.ExeMusicEvent(Bladex.GetMusicEvent("entradaalcant"))
			alcantarillasvistas=1
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("alcantytabvue"))

def EnciendeMusicaInicio():
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, MusicTool.LaunchMusicEvent, ("musica1anillo",))

def EnciendeMusicaApChaos():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musicaapchaos"))
	Bladex.AddScheduledFunc(Bladex.GetTime()+19.0, MusicTool.LaunchMusicEvent, ("musica2anillo",))
