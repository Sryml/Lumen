#
# ----------------------------------------
#  C O N C E N T R A T I O N   E F F E C T
# ----------------------------------------
#
# For launching a concentration effect :
#	1st) Create it . Ex:
#		c_ef=CONCEN_EF()
#	2nd) When you want to launch it :
#		c_ef.StartConcentrationEffect(Bladex.GetEntity("Player1").Position,"Player1","R_Hand","Aparicion_espada",0.5)
#
#	PARAMETERS of the StartConcentrationEffect function :
#		1- Position in which it will be located
#		2- Name of the entity to be linked with (if the entity moves , the effect will move with it)
#			None if not linked to any entity (it will be in the pos of the first parameter for the whole effect)
#		3- (applies only if par2 was given)
#			Name of the areaof the entity (the 2nd parameter) where the effect will be link
#			Useful to link effects to the hands of a given character , of the eyes , etc ...
#		4- Name of the sound that will be played during the effect
#		5- % of the size of the effect (related to the textures used ...)
#
#		(from now on , the rest of the parameter have got default values)
#
#
#		6- Time that the effect will last (NO perfectly accurate , but will be fix if needed)
#		7- Name of the texture1 name  used
#		8,9,10 - r,g,b components that will be applied to texture1
#		11,12,13,14,15 - As 7-10 , but for texture2
#		16,17,18 - Rgb values of the particles of the particle system
#
#
#
#	If more parameters arte needed , or if you have any questions , ask Jose .
#
#
#

import Bladex

B_PARTICLE_GTYPE_COPY=0
B_PARTICLE_GTYPE_BLEND=1
B_PARTICLE_GTYPE_ADD=2
B_PARTICLE_GTYPE_MUL=3


Bladex.ReadBitMap("../../Data/Prueba Flare Magico 256.bmp","Flare Magico 256")
Bladex.ReadBitMap("../../Data/Prueba Flare Magico 128.bmp","Flare Magico 128")

Bladex.ReadAlphaBitMap("../../Data/GenericPrtl.bmp","GenericParticle")
Bladex.AddParticleGType("Concentrado","GenericParticle",B_PARTICLE_GTYPE_BLEND,600)



class CONCEN_EF:
	luzA=0
	luzB=0
	parts=0
	size_factor=1.0
	main_ent_name=""
	entity_name_link=""
	ent_area=""
	sonido_aparicion=0

	def SetPos(self,pos):
		self.luzA.Position=pos
		self.luzB.Position=pos
		self.parts.Position=pos

	def PosMe(self,ent_name):
		me=Bladex.GetEntity(ent_name)
		if self.entity_name_link:
			ent=Bladex.GetEntity(self.entity_name_link)
			if self.ent_area<>"":
				me.Position=ent.GraspPos(self.ent_area)
			else:
				me.Position=ent.Position


	def RelocateMe(self,ent_name, time):
		self.PosMe(ent_name)


	def GrowMe(self,ent_name, time):
		luz=Bladex.GetEntity(ent_name)
		luz.SizeFactor=luz.SizeFactor+0.2*self.size_factor
		if luz.SizeFactor>15.0*self.size_factor:
			luz.TimerFunc=""
			luz.RemoveFromList("Timer60")
			#luz.TimerFunc=self.StrinkMe
			#self.parts.DeathTime=Bladex.GetTime()+0.0

		if ent_name==self.main_ent_name:
			if luz.SizeFactor<10*self.size_factor:
				luz.Intensity=3.0-(10.0*self.size_factor-luz.SizeFactor)*3.0/(10.0*self.size_factor)
			else:
				luz.Intensity=3
			#print "SizeF is " + `luz.SizeFactor` + " Intensity is  " + ` luz.Intensity `

		self.PosMe(ent_name)


	def StrinkMe(self,ent_name, time):
		luz=Bladex.GetEntity(ent_name)
		if luz.SizeFactor>10*self.size_factor:
			luz.SizeFactor=luz.SizeFactor-0.1*self.size_factor
		else:
			if luz.SizeFactor>5*self.size_factor:
				luz.SizeFactor=luz.SizeFactor-0.2*self.size_factor
			else:
				luz.SizeFactor=luz.SizeFactor-0.4*self.size_factor

		if luz.SizeFactor<0.1*self.size_factor:
			luz.RemoveFromList("Timer60")
			luz.SubscribeToList("Pin")

		if ent_name==self.main_ent_name:
			if luz.SizeFactor<5*self.size_factor:
				luz.Intensity=(5*self.size_factor-luz.SizeFactor)*2.0+3.0
			#print "SizeF is " + `luz.SizeFactor` + " Intensity is  " + ` luz.Intensity `

		self.PosMe(ent_name)


	def EndConcentrationEffect(self):
		self.luzA.TimerFunc=self.StrinkMe
		self.luzA.SubscribeToList("Timer60")
		self.luzB.TimerFunc=self.StrinkMe
		self.luzB.SubscribeToList("Timer60")

		self.parts.DeathTime=Bladex.GetTime()+0.0

	def StartConcentrationEffect(self,pos,ent2follow,ent_bit,sound_name,s_factor,time=2,
								text1_name="Flare Magico 256",text1_r=255,text1_g=255,text1_b=255,
								text2_name="Flare Magico 128",text2_r=128,text2_g=128,text2_b=255,
								part_r=128,part_g=128,part_b=200):

		self.size_factor=s_factor

		self.main_ent_name=Bladex.GenerateEntityName()
		self.luzA=Bladex.CreateEntity(self.main_ent_name,"Entity Spot",0,0,0)
		self.luzA.Color=text1_r,text1_g,text1_b
		self.luzA.Intensity=0
		self.luzA.Precission=0.1
		self.luzA.CastShadows=0
		self.luzA.GlowTexture=text1_name
		self.luzA.GlowTestZ=0
		self.luzA.AngVel=1.59
		self.luzA.SizeFactor=0.05*self.size_factor

		self.luzB=Bladex.CreateEntity(Bladex.GenerateEntityName(),"Entity Spot",0,0,0)
		self.luzB.Color=text2_r,text2_g,text2_b
		self.luzB.Intensity=0.1
		self.luzB.Precission=0.1
		self.luzB.CastShadows=0
		self.luzB.GlowTexture=text2_name
		self.luzB.GlowTestZ=0
		self.luzB.AngVel=-3.14
		self.luzB.SizeFactor=0.05*self.size_factor

		self.luzA.TimerFunc=self.GrowMe
		self.luzA.SubscribeToList("Timer60")
		self.luzB.TimerFunc=self.GrowMe
		self.luzB.SubscribeToList("Timer60")

		self.parts=Bladex.CreateEntity("Parts", "Entity Particle System D1", 0.0, 0.0, 0.0)
		self.parts.ParticleType="Concentrado"
		self.parts.Time2Live=25 #*self.size_factor
		self.parts.YGravity=0
		self.parts.Friction=0
		self.parts.RandomVelocity=-50.0*self.size_factor
		#-100.0*self.size_factor
		self.parts.RandomVelocity_V=0.0
		self.parts.PPS=512

		self.parts.TimerFunc=self.RelocateMe
		self.parts.SubscribeToList("Timer60")

		for i in range(600):
			a=255
			size=33*self.size_factor
			if size<20:
				size=20
			Bladex.SetParticleGVal("Concentrado",i,part_r,part_g,part_b,a,size)

		self.SetPos(pos)

		if ent2follow and ent2follow<>"":
			self.entity_name_link=ent2follow
			if ent_bit and ent_bit<>"":
				self.ent_area=ent_bit
			else:
				self.ent_area=""
		else:
			self.entity_name_link=""
			self.ent_area=""


		file_name="../../Sounds/"+ sound_name +".wav"
		self.sonido_aparicion=Bladex.CreateSound(file_name,"Aparicion")
		self.sonido_aparicion.MaxDistance=20000.0
		self.sonido_aparicion.Play(pos[0], pos[1], pos[2], 0)


		Bladex.AddScheduledFunc(Bladex.GetTime()+time, self.EndConcentrationEffect,   ())








c_ef=CONCEN_EF()
c_ef2=CONCEN_EF()

def LanzaC():
	c_ef.StartConcentrationEffect(Bladex.GetEntity("Player1").Position,"Player1","R_Hand","Aparicion_espada",0.5)
	c_ef2.StartConcentrationEffect(Bladex.GetEntity("Player1").Position,"Player1","Shield","Aparicion_espada",0.5)