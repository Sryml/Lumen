import Bladex
import B3DLib
import EnemyTypes
import Actions
import ItemTypes
import math
import Sounds
import darfuncs
import GameStateAux
import ObjStore
import whrandom
import Reference

def EnemyReady(ent_name):
	# print "Borrando '"+ent_name + "quad'"
	o = Bladex.GetEntity(ent_name + "quad")
	if o:
		o.SubscribeToList("Pin")
		Reference.EntitiesSelectionData.pop(o.Name)
	char=Bladex.GetEntity("Player1")
	enm=Bladex.GetEntity(ent_name)
	Bladex.AddScheduledFunc(Bladex.GetTime(),enm.SetOnFloor,())
	enm.InitPos=pos=enm.Position
	v=char.Position[0]-pos[0], 0.0, char.Position[2]-pos[2]
	v=B3DLib.Normalize(v)
	alfa=-(3.14159/2.0)*(v[0]/abs(v[0]))+math.atan(v[2]/v[0])
	enm.Face(alfa)
	enm.Blind=0
	enm.Deaf=0
	#enm.Position = 0,0,0
	#enm.RemoveFromWorld()
	#Bladex.AddScheduledFunc(Bladex.GetTime() + 2.0,enm.Data.enmgendata.GeneratorReady,(ent_name,))

class Point:
	def __init__(self):
		self.Name="Skl"
		self.EnemyType="Skeleton"
		self.WeaponType=""
		self.WeaponBreak=0
		self.ShieldType=""
		self.ShieldBreak=0
		self.Animation=""
		self.Position = [0,0,0]
		self.Level=None


class EnmGenRnd:

	ObjId=0
	Active=0
	Ready=0
	NEnemies=4
	NextEnemy=0
	InitGenFunc=""
	GenerateNotifyFunc=""
	FinishGenFunc=""
	InitGenArgs=()
	NPoints = 0
	OnceEnm = 1
	EnmActivates = 0
	FinishGen = 0
	Points = [0]
	Enemies = [0]
	p = 0
	N_EnmGen = 0
	DifTime = 0
	VirGenPos = [0,0,0]
	Last_Point = -1
	NumDeaths  = 0
	Level = 0
	SonidoGen=None

	def __init__(self):
		self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
		ObjStore.ObjectsStore[self.ObjId]=self
		self.VirGenPos=[0,0,0]
		self.Points = [0]
		self.Enemies = [0]
		self.taken_points = []

	def GeneratorReady(self,ent_name):
		#enm=Bladex.GetEntity(ent_name)
		#enmgen=enm.Data.enmgendata
		#enmgen.Ready=1
		print "Enemigo muero"

		self.NumDeaths = self.NumDeaths-1

		if self.NumDeaths == 0:
			if self.OnEnd:
				self.OnEnd()
		else:
			print "Quedan ",self.NumDeaths,"Enemigos"

		enm = Bladex.GetEntity(ent_name)
		enm.Data.ImDeadFuncX(ent_name)

		self.Enemies[enm.Data.NEnemy] = 0
		self.EnmActivates = self.EnmActivates - 1

		self.GenerateEnemy()


		if (self.FinishGen and self.EnmActivates == 0):
			if self.FinishGenFunc:
				apply(self.FinishGenFunc, (self,))

	def ActivateEnemy(self,point):
		enm = self.Enemies[self.NextEnemy]
		if enm:
			darfuncs.UnhideBadGuy(enm.Name)
			enm.Blind = 1
			enm.Deaf  = 1
			enm.Position = self.Points[point].Position
			enm.Data.NEnemy = self.NextEnemy
		return enm

	def restore_point(self,point):
		self.taken_points.remove(point)

	def GenerateEnemy(self):
		# Refactored -Sryml
		enmgen = self
		char=Bladex.GetEntity("Player1")
		charpos = char.Position
		#
		if enmgen.Ready:
			nenemies = enmgen.OnceEnm - enmgen.EnmActivates
			if nenemies == 0:
				return
			if nenemies > 1 and self.DifTime != 0:
				nenemies = 1
				Bladex.AddScheduledFunc(Bladex.GetTime() + self.DifTime+whrandom.random(),self.GenerateEnemy,())
			#
			retry = 0
			for t in range(nenemies):
				point = self.GetBestGenerationPoint()
				if point is None:
					retry = 1
					continue
				#
				self.taken_points.append(point)
				Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, self.restore_point, (point,))
				enm = self.ActivateEnemy(point)

				enmgen.NextEnemy=enmgen.NextEnemy+1
				enmgen.EnmActivates = enmgen.EnmActivates + 1
				if enmgen.NextEnemy >= enmgen.NEnemies:
					enmgen.Deactivate()
					enmgen.FinishGen = 1

				pos = enm.Position
				v=charpos[0]-pos[0], 0.0, charpos[2]-pos[2]
				v=B3DLib.Normalize(v)
				if v[0] > 0:
					alfa=-(3.14159/2.0)*(v[0]/abs(v[0]))+math.atan(v[2]/v[0])
				else:
					alfa = 3.14 * -v[1]
				enm.Angle=alfa

				if enmgen.Points[point].Animation:
					enm.SetTmpAnmFlags(1,1,1,0,5,1)
					enm.LaunchAnimation(enmgen.Points[point].Animation)
					enm.AnmEndedFunc=EnemyReady
					darfuncs.CreateFalseCube(enm.Position,-1,enm.Name)
				else:
					EnemyReady(enm.Name)

				Actions.TurnToFaceEntityNow(enm.Name,"Player1")
				enm.Data.ImDeadFuncX = enm.ImDeadFunc
				enm.ImDeadFunc=self.GeneratorReady

				if enmgen.InitGenFunc:
					enmgen.SonidoGen.Position = pos
					enmgen.SonidoGen.PlaySound(0)

					apply(enmgen.InitGenFunc, (enm,))
			#
			if retry:
				for i in range(Bladex.GetnScheduledFuncs()):
					if Bladex.GetScheduledFunc(i)[2] == "EnmGenRnd.GenerateEnemy":
						return
				Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, self.GenerateEnemy,(), "EnmGenRnd.GenerateEnemy")
				Reference.debugprint("Next try in 3 seconds.")

	def GetBestGenerationPoint(self):
		# Rewritten -Sryml
		point = (self.Last_Point + 1) % self.NPoints
		for i in range(self.NPoints):
			if point in self.taken_points:
				point = (point + 1) % self.NPoints
				Reference.debugprint("Point %s is already taken." % point)
				continue
			pos = self.Points[point].Position
			if darfuncs.ValidAppear(pos, radius=3100):
				self.Last_Point = point
				return point
			point = (point + 1) % self.NPoints

		return None


	def AddPoint(self,pos,enemydscr=("Skl", "Skeleton", "", 0, "", 0), animation="", Level=None):
		point = Point()

		point.Position = pos
		point.Name=enemydscr[0]
		point.EnemyType=enemydscr[1]
		point.WeaponBreak=enemydscr[3]
		point.WeaponType=enemydscr[2]
		point.ShieldType=enemydscr[4]
		point.ShieldBreak=enemydscr[5]
		point.Animation=animation
		point.Level=Level

		self.Points[self.NPoints:self.NPoints] = [point]
		self.NPoints = self.NPoints + 1


	def CreateEnemy(self,i):
		Rage = self.Points[i].EnemyType
		#Name = self.Points[i].Name
		#pos = self.Points[point].Position
		Name = self.Points[0].Name + `self.N_EnmGen`

		self.Points[i].Enm = enm=Bladex.CreateEntity(Name, Rage, self.VirGenPos[0],self.VirGenPos[1],self.VirGenPos[2],"Person")
		if self.Points[i].Level!=None: enm.Level= self.Points[i].Level
		else: enm.Level= self.Level
		enm.Blind=1
		enm.Deaf=1

		if self.Points[i].WeaponType:
			weapon=Bladex.CreateEntity("Weapon"+Name, self.Points[i].WeaponType, 0.0, 0.0, 0.0,"Weapon")
			ItemTypes.ItemDefaultFuncs(weapon)
			Actions.TakeObject(Name, weapon.Name)

			weapon.RemoveFromWorld()

		if self.Points[i].ShieldType:
			shield=Bladex.CreateEntity("Shield"+Name, self.Points[i].ShieldType, 0.0, 0.0, 0.0,"Weapon")
			ItemTypes.ItemDefaultFuncs(shield)
			Actions.TakeObject(Name, shield.Name)
			shield.RemoveFromWorld()


		EnemyTypes.EnemyDefaultFuncs(enm)

		enm.Data.enmgendata=self
		darfuncs.HideBadGuy(enm.Name)
		self.N_EnmGen = self.N_EnmGen + 1
		self.NumDeaths  = self.NumDeaths+1

		return enm


	def Activate(self):
		if self.NextEnemy<=self.NEnemies:
			self.Active=1
			self.Ready=1

			j = i = 0

			for i in range(self.NEnemies):
				if (j >= self.NPoints):
					j = 0

				en = self.CreateEnemy(j)
				if self.CallBak:
					self.CallBak(en)

				self.Enemies[i:i] = [en]
				j = j + 1

	def Deactivate(self):
		self.Active=0
		self.Ready=0
		#Bladex.RemoveTriggerSectorFunc(self.TrSector, "OnEnter")

	def persistent_id(self):
		return self.ObjId

	def __GetNameEnemies__(self):
		Names = []
		for i in range (self.NEnemies):
			if self.Enemies[i]:
				Names.append(self.Enemies[i].Name)
			else:
				Names.append(None)

		return Names

	def __GetPointsGeneration__(self):
		Points = []
		for i in range(self.NPoints):
			Points.append((self.Points[i].Position,self.Points[i].Animation))
		return Points

	def __SetEnemies__(self,enemies):
		self.Enemies = []

		for i in range(self.NEnemies):
			if enemies[i] <> None:
				self.Enemies.append(Bladex.GetEntity(enemies[i]))
			else:
				self.Enemies.append(0)

	def __SetPoints__(self,points):
		self.Points = []

		for i in range(self.NPoints):
			p = Point()
			p.Position = points[i][0]
			p.Animation = points[i][1]
			self.Points.append(p)

	def __getstate__(self):
		# Tiene que devolver c�mo poder guardar el estado de la clase
		stick_objId=None
		return (1,
				self.ObjId,
				self.Ready,
				self.OnceEnm,
				self.EnmActivates,
				self.DifTime,
				self.NextEnemy,
				self.NEnemies,
				self.FinishGen,
				self.p,
				self.Active,
				self.NPoints,
				self.Last_Point,
				self.NumDeaths,
				GameStateAux.SaveFunctionAux(self.InitGenFunc),
				self.InitGenArgs,
				GameStateAux.SaveFunctionAux(self.GenerateNotifyFunc),
				GameStateAux.SaveFunctionAux(self.FinishGenFunc),
				self.__GetNameEnemies__(),
				self.__GetPointsGeneration__(),
				GameStateAux.SaveEntityAux(self.SonidoGen),
				GameStateAux.SaveNewMembers(self)
				)

	def __setstate__(self,parm):
		# Toma como par�metro lo que devuelve __getstate__() y debe recrear la clase
		if parm[0]==1:
			#self.ObjId=parm[1] En GameStateAux.PersistentObject()
##			GameStateAux.PersistentObject.__setstate__(self,parm)
			self.ObjId=parm[1]
##			GameStateAux.LoadedPickledData[self.ObjId]=self
			ObjStore.ObjectsStore[self.ObjId]=self
			self.Ready=parm[2]
			self.OnceEnm=parm[3]
			self.EnmActivates=parm[4]
			self.DifTime=parm[5]
			self.NextEnemy=parm[6]
			self.NEnemies=parm[7]
			self.FinishGen=parm[8]
			self.p=parm[9]
			self.Active=parm[10]
			self.NPoints=parm[11]
			self.Last_Point=parm[12]
			self.NumDeaths=parm[13]
			GameStateAux.LoadFunctionAux(parm[14],self,"InitGenFunc")
			self.InitGenArgs=parm[15]
			GameStateAux.LoadFunctionAux(parm[16],self,"GenerateNotifyFunc")
			GameStateAux.LoadFunctionAux(parm[17],self,"FinishGenFunc")
			self.__SetEnemies__(parm[18])
			self.__SetPoints__(parm[19])
			self.SonidoGen = GameStateAux.LoadEntityAux(parm[20])
			print "EnmGenRnd.__setstate__ self.SonidoGen",self.SonidoGen
			GameStateAux.LoadNewMembers(self,parm[21])

		else:
			print "Warning -> Version mismatch in EnmGenRnd."
			# Valores de creaci�n por si valen para algo.
			self.Ready=0
			self.OnceEnm=0
			self.EnmActivates=0
			self.DifTime=0
			self.NextEnemy=0
			self.NEnemies=0
			self.FinisGen=0
			self.p=0
			self.Active=0
			self.NPoints=0
			self.Last_Point=0
			self.NumDeaths=0
			self.InitGenArgs=()
			self.InitGenFunc=None
			self.GenerateNotifyFunc=None
			self.FinishGenFunc=None
			self.ObjId=ObjStore.GetNewId()
			ObjStore.ObjectsStore[self.ObjId]=self

def CreateEnemiesGenerator(nenemies=4, enmonce=2,SonidoGen = '../../Sounds/M-GENERADOR-ENTIERRA3.wav'):
	enmgen=EnmGenRnd()
	#enmgen.TrSector=trsector
	enmgen.NEnemies=nenemies
	enmgen.OnceEnm = enmonce

	enmgen.SonidoGen = Sounds.CreateEntitySound(SonidoGen, 'GenTierra')
	enmgen.SonidoGen.Volume=0.3
	enmgen.SonidoGen.MinDistance=5000
	enmgen.SonidoGen.MaxDistance=20000
	enmgen.CallBak = None
	enmgen.OnEnd   = None

	#enmgen.AddPoint((x,y,z))
	#Bladex.SetTriggerSectorData(trsector, enmgen)

	return enmgen

def CreateEnemy(pos,Name,Rage,WeaponType,WeaponBreak,ShieldType,ShieldBreak,Level=0):
	enm=Bladex.CreateEntity(Name, Rage, pos[0],pos[1],pos[2],"Person")
	enm.Blind=1
	enm.Deaf=1
	enm.Level=Level

	if WeaponType:
		weapon=Bladex.CreateEntity("Weapon"+Name, WeaponType, pos[0], pos[1], pos[2],"Weapon")
		ItemTypes.ItemDefaultFuncs(weapon)
		Actions.TakeObject(Name, weapon.Name)

	if ShieldType:
		shield=Bladex.CreateEntity("Shield"+Name, ShieldType, 0.0, 0.0, 0.0)
		ItemTypes.ItemDefaultFuncs(shield)
		Actions.TakeObject(Name, shield.Name)

	EnemyTypes.EnemyDefaultFuncs(enm)
	enm.Data.Position = pos

	#enm.Position = 0,0,0
	darfuncs.HideBadGuy(enm.Name)

	return enm

def ActivateEnemy(enm):
	if hasattr(enm.Data, "Position"):
		enm.Position = enm.Data.Position
	darfuncs.UnhideBadGuy(enm.Name)
