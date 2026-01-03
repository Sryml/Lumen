import Bladex
import EnemyTypes
import Enm_Def
import Reference
import AniSound
import Sounds
import Combat
import copy
import Actions
import GameStateAux

TRUE = 1
FALSE = 0



#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Sleeping_Knight.py **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

class SleepingKnight (EnemyTypes.Knight_Traitor):
	def __init__(self, me):
		EnemyTypes.Knight_Traitor.__init__(self, me)
		self.ronquidos=Sounds.CreateEntitySound("../../Sounds/snore-loop.wav", "Ronquidos")
		self.ronquidos.Volume=1
		#self.ronquidos.Scale=1.112
		self.ronquidos.MinDistance= 5000
		self.ronquidos.MaxDistance=25000

		self.PutMeToSleep(self.Name)

	# We sleep against a wall rather than on the floor, so override the basic sleep funcs

	def PutMeToSleep(self,EntityName):
		if not self.Asleep:
			me = Bladex.GetEntity(EntityName)

			self.SleepXOffset = 500
			#me.Position = (me.Position[0]-self.SleepXOffset, me.Position[1], me.Position[2])
			me.Wuea=Reference.WUEA_ENDED
			me.SetTmpAnmFlags(1,1,0,0,0,1,1)
			me.LaunchAnimation("Tkn_sleep_wall")
			me.Blind=1  #just in case
			#me.Deaf=1
			self.Asleep = TRUE
			self.ronquidos.Position = me.Position
			self.ronquidos.PlaySound(-1)


	def WakeMeUp(self,EntityName):
		if self.Asleep:
			me = Bladex.GetEntity(EntityName)
			me.Blind=0  #just in case
			self.ronquidos.StopSound()

			# alert animation
			if me.AnimName[:5] == "Sleep" or me.AnimName[:5] == "sleep":
				me.Position = -1165.91968748, -1112.39664744, 110137.42
				me.Wuea=Reference.WUEA_ENDED
				me.SetTmpAnmFlags(1,0,1,0,1,1)
				me.LaunchAnimation("Tkn_alarm01")
				me.SetOnFloor()
			self.Asleep = FALSE

	# Functions for loading and saving state
	def __getstate__(self):
		print "SleepingKnight.__getstate__"
		NPCPerson_state=EnemyTypes.Knight_Traitor.__getstate__(self)
		if(NPCPerson_state[0]!=1):
			print "ERROR: SleepingKnight.__getstate__(): Base class version differs."
			return NPCPerson_state
		NPCPerson_state[1]["SleepingKnight"]=(self.ronquidos.Name,)
		return NPCPerson_state

	def __setstate__(self,parm):
		print "SleepingKnight.__setstate__"
		# Toma como par⮥tro lo que devuelve __getstate__() y debe recrear la clase
		EnemyTypes.Knight_Traitor.__setstate__(self,parm)
		version=parm[0]
		if version==1:
			parms=parm[1]["SleepingKnight"]
			self.ronquidos=Bladex.GetSound(parms[0])
