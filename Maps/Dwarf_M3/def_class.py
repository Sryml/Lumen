import Enm_Def
import copy
import Combat
import Bladex
import AuxTran
import Reference

################################################################################
# Define the Dwf class
################################################################################

class Enano (Enm_Def.NPCPerson):
	def __init__(self, me):
		# base class init		
		Enm_Def.NPCPerson.__init__(self, me)

		# anims
		me.AnmTranFunc=AuxTran.AuxTranOrc

		# Set up orc specific sound priorities
		self.SoundPriorities[Reference.SND_ARROW]   = 10.0
		self.SoundPriorities[Reference.SND_HIT]     = 50.0
		self.SoundPriorities[Reference.SND_NPC]     = 25.0
		self.SoundPriorities[Reference.SND_NOISYPC] = 30.0
		self.SoundPriorities[Reference.SND_PC]      = 80.0

		# Set up sounds made	
		#AniSound.AsignarSonidosOrco(me.Name)

	def ResetCombat (self,EntityName):
		Enm_Def.NPCPerson.ResetCombat(self, EntityName)
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			me.BlockingPropensity = 0.1
			me.AttackList = copy.copy(Combat.EnanoAttackData)
			self.ChanceOfFuryOnHurt = 0.45


