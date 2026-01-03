import Bladex

class FLuz:
	def __init__(self):
		self.Fire = 0
		self.Luz = 0
		self.IFire = 0
		self.ILuz = 1

	def Apaga(self):
		if self.ILuz > 0:
			self.ILuz =self.Luz.Intensity = self.ILuz - 0.035
		else:
			self.Luz.Intensity = 0

		self.IFire = self.Fire.Intensity = self.IFire + 0.5

		if self.IFire < 20:
			Bladex.AddScheduledFunc(Bladex.GetTime() + 0.5,self.Apaga,())
			
class Link:
	def __init__(self,sld,y):
		self.y = y
		self.sld = sld
