import Bladex
import EnemyTypes
import Actions
import math
import B3DLib
import PickInit
import GameStateAux
import darfuncs
import ItemTypes
import ObjStore



def GeneratorReady(ent_name):
	enm=Bladex.GetEntity(ent_name)
	enmgen=enm.Data.enmgendata
	enmgen.Ready=1
	enm.Data.OldImDeadFunc(ent_name)

def EnemyReady(ent_name):
	o = Bladex.GetEntity(ent_name + "quad")
	if o:
		o.SubscribeToList("Pin")
	enm=Bladex.GetEntity(ent_name)
	enm.InitPos=enm.Position
	alfa=B3DLib.GetEntity2EntityAngle(ent_name, "Player1")
	enm.Face(alfa)
	enm.Blind=0
	enm.Deaf=0
	Bladex.AddScheduledFunc(Bladex.GetTime(),enm.SetOnFloor,())
	if enm.Data.CallBackGen != "":
		enm.Data.CallBackGen(enm)
	
def TryToGenerateEnemy(trsector, ent_name):
	enmgen=Bladex.GetTriggerSectorData(trsector)
	darfuncs.ValidAppear(enmgen.Position,GenerateEnemy,(trsector, ent_name))

def GenerateEnemy(trsector, ent_name):
	enmgen=Bladex.GetTriggerSectorData(trsector)
	if ent_name=="Player1":
		if enmgen.Ready:
			enmgen.Ready=0
			enm=Bladex.GetEntity(enmgen.RootName+`enmgen.NextEnemy`)
			enm.UnFreeze()
			enmgen.NextEnemy=enmgen.NextEnemy+1
			if enmgen.NextEnemy>enmgen.NEnemies:
				enmgen.Deactivate()
			if enmgen.Animation:
				char=Bladex.GetEntity("Player1")
				enm.SetTmpAnmFlags(1,1,1,0,5,1,0)
				enm.LaunchAnimation(enmgen.Animation)
				enm.Position=enmgen.Position
				alfa=B3DLib.GetEntity2EntityAngle(enm.Name, "Player1")
				enm.Angle=alfa
				enm.AnmEndedFunc=EnemyReady
				darfuncs.CreateFalseCube(enmgen.Position,-1.0,enm.Name)
			else:
				EnemyReady(enm.Name)
			if enmgen.InitGenFunc:
				apply(enmgen.InitGenFunc, enmgen.InitGenArgs)


class EnmGen:

	def __init__(self):
		self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
		ObjStore.ObjectsStore[self.ObjId]=self

		self.Active=0
		self.Ready=0
		self.Position=0.0, 0.0, 0.0
		self.TrSector=""
		self.NEnemies=4
		self.NextEnemy=1
		self.RootName="Skl"
		self.EnemyType="Skeleton"
		self.WeaponType=""
		self.ShieldType=""
		self.Animation=""
		self.InitGenFunc=""
		self.InitGenArgs=()

	def Activate(self):
		if self.NextEnemy<=self.NEnemies:
			self.Active=1
			self.Ready=1
			Bladex.SetTriggerSectorFunc(self.TrSector, "OnEnter", TryToGenerateEnemy)
		else:
			print "Generador agotado!"

	def Deactivate(self):
		self.Active=0
		self.Ready=0
		Bladex.RemoveTriggerSectorFunc(self.TrSector, "OnEnter")

	def persistent_id(self):
		return self.ObjId

	def __getstate__(self):
		# Tiene que devolver cómo poder guardar el estado de la clase
		return (1,
				self.ObjId,
				self.Active,
				self.Ready,
				self.Position,
				self.TrSector,
				self.NEnemies,
				self.NextEnemy,
				self.RootName,
				self.EnemyType,
				self.WeaponType,
				self.ShieldType,
				self.Animation,
				GameStateAux.SaveFunctionAux(self.InitGenFunc),
				self.InitGenArgs,
				)
		

	def __setstate__(self,parm):
		# Toma como parámetro lo que devuelve __getstate__() y debe recrear la clase
		if parm[0]==1:
			self.ObjId=parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self
			
			self.Active=parm[2]
			self.Ready=parm[3]
			self.Position=parm[4]
			self.TrSector=parm[5]
			self.NEnemies=parm[6]
			self.NextEnemy=parm[7]
			self.RootName=parm[8]
			self.EnemyType=parm[9]
			self.WeaponType=parm[10]
			self.ShieldType=parm[11]
			self.Animation=parm[12]
			GameStateAux.LoadFunctionAux(parm[13],self,"InitGenFunc")
			self.InitGenArgs=parm[14]
		else:
			print "EnmGen.__setstate__() -> Version mismatch"
			# Valores de creación por si valen para algo.
			self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
			ObjStore.ObjectsStore[self.ObjId]=self

			self.Active=0
			self.Ready=0
			self.Position=0.0, 0.0, 0.0
			self.TrSector=""
			self.NEnemies=4
			self.NextEnemy=1
			self.RootName="Skl"
			self.EnemyType="Skeleton"
			self.WeaponType=""
			self.ShieldType=""
			self.Animation=""
			self.InitGenFunc=""
			self.InitGenArgs=()



def CreateEnemiesGenerator(x=0.0, y=0.0, z=0.0, trsector="", nenemies=4, enemydscr=("Skl", "Skeleton", "", 0, "", 0), animation="", CallBack = ""):
	enmgen=EnmGen()
	enmgen.Position=x, y, z
	enmgen.TrSector=trsector
	enmgen.NEnemies=nenemies
	enmgen.RootName=rootname=enemydscr[0]
	enmgen.EnemyType=enemytype=enemydscr[1]
	enmgen.WeaponType=weapontype=enemydscr[2]
	enmgen.ShieldType=shieldtype=enemydscr[4]
	enmgen.Animation=animation
	Bladex.SetTriggerSectorData(trsector, enmgen)
	for n in range(nenemies):
		enm=Bladex.CreateEntity(rootname+`n+1`, enemytype, x, y, z,"Person")
		enm.Angle=0.0
		if weapontype:
			weapon=Bladex.CreateEntity("Weapon"+rootname+`n+1`, weapontype, 0.0, 0.0, 0.0,"Weapon")
			ItemTypes.ItemDefaultFuncs(weapon)
			Actions.TakeObject(enm.Name, weapon.Name)
#			if enemydscr[3]:
#				Breakings.SetBreakableWS(weapon.Name)
		if shieldtype:
			shield=Bladex.CreateEntity("Shield"+rootname+`n+1`, shieldtype, 0.0, 0.0, 0.0)
			ItemTypes.ItemDefaultFuncs(shield)
			Actions.TakeObject(enm.Name, shield.Name)
#			if enemydscr[5]:
#				Breakings.SetBreakableWS(shield.Name)
		if len(enemydscr)==7:
			enm.Level=enemydscr[6]
		EnemyTypes.EnemyDefaultFuncs(enm)
		enm.Blind=1
		enm.Deaf=1
		if n<nenemies-1:
			enm.Data.OldImDeadFunc=enm.ImDeadFunc
			enm.ImDeadFunc=GeneratorReady
		enm.Data.enmgendata=enmgen
		enm.Data.CallBackGen=CallBack
		enm.Freeze()
		enm.RemoveFromWorldWithChilds()
	return enmgen
