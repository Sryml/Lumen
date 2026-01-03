import math
import Bladex
import AuxFuncs
import Sounds
import Reference

class PENDULO:
	def __init__(self,Pendulo):
		self.L_Int = 0
		self.F_Int = 20
		self.Pendulo = None
		self.Piv = [0,0,4900]
		self.Axi = [1,0,0]
		self.Angulo = 0
		self.Vel = 0.02
		self.sound1 = 0
		self.sound2 = 0
		self.Dir = 1
		self.Luz = 0
		self.Fire = 0
		self.Activado = 0

	def RotarPendulo(P,entity,timer):
		sin = math.sin(P.Angulo * 1.35)

		if sin < 0:
			isin = sin * -1.0
		else:
			isin = sin

		vel = 0.023 * sin
		ivel = 0.023 * isin
		Angulo = P.Angulo + ivel
		dif = Angulo - P.Angulo

		if (dif < 0.01):
			P.Angulo = P.Angulo + 0.01
		else:
			P.Angulo = Angulo

		P.Pendulo.MessageEvent(Reference.MESSAGE_START_WEAPON,0,0)
		P.Pendulo.RotateRel(P.Piv[0],P.Piv[1],P.Piv[2],P.Axi[0],P.Axi[1],P.Axi[2],vel * P.Dir)

		P.sound1.Position = AuxFuncs.GetSpot(P.Pendulo).Position
		P.sound2.Position = P.sound1.Position

	def Enciende(self,entity,timer):
		self.F_Int = self.Fire.Intensity = self.F_Int - (5.0 /30.0)
		self.L_Int = self.Luz.Intensity = self.L_Int + (2.5 /30.0)

		if (self.F_Int <= 0):
			self.Pendulo.TimerFunc = self.RotarPendulo
			self.Fire.Intensity = 0

	def Apaga(self,entity,timer):
		if (self.Angulo < 4.6544):
			self.RotarPendulo(0,0)
		else:
			self.F_Int = self.Fire.Intensity = self.F_Int + (5.0 /30.0)
			self.L_Int = self.Luz.Intensity = self.L_Int - (2.5 /30.0)
			self.Pendulo.PutToWorld()
			
			if (self.Fire.Intensity >= 20):
				self.Pendulo.RemoveFromList("Timer60")
				

	def Stop(self):		
		self.Pendulo.TimerFunc = self.Apaga
		self.F_Int = 0
		self.L_Int = 10
		self.sound1.StopSound()
		self.sound2.StopSound()
		self.Activado = 0
		self.Angulo = self.Angulo % 4.6544



	def Play(self):
		self.sound1.Position = AuxFuncs.GetSpot(self.Pendulo).Position
		self.sound2.Position = self.sound1.Position
		
		self.sound1.PlaySound(-1)
		self.sound2.PlaySound(-1)
		
		self.Pendulo.SubscribeToList("Timer60")
		self.Pendulo.TimerFunc = self.Enciende
		self.F_Int = 20
		self.L_Int = 0
		self.Activado = 1
		self.Angulo = 0
		self.Pendulo.Data.NoFXOnHit=1