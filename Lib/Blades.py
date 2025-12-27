import Traps_C

MESSAGE_START_WEAPON         =	7
MESSAGE_STOP_WEAPON          =	8


class BLADES:
	def __init__(self,name,spline,vel_rot,finish_func):
		self.time = 0
		self.state = 0
		self.vel_rot = vel_rot
		self.finish_func = finish_func
		self.blade_spline = spline
		self.last_time = 0
		self.name = name

	def StartBlade(self):
		self.time = 0
		self.last_time = Bladex.GetTime()

	def StopBlade(self):
		self.state = 0

	def PlayBlade(self):
		if (self.state <> 1):
			self.state = 1
			self.last_time = Bladex.GetTime()
			blade = Bladex.GetEntity(self.name)
			blade.Solid=0
			blade.MessageEvent(MESSAGE_START_WEAPON,0,0)
			blade.TimerFunc=BladeTimerFunc
			blade.SubscribeToList("Timer60")

	def AddNode(self,pos,tang_i,tang_f,time):
		Traps_C.AddSplineNode(self.blade_spline,pos,tang_i,tang_f,time)

def CreateBlade(name,vel_rot,finish_func):
	spline = Traps_C.CreateSpline()

	blade = BLADES(spline,vel_rot,finish_func)

	blade_e = Bladex.GetEntity(name)
	blade_e.Data = blade


Bladex.CreateTimer("Timer60",1.0/60.0)

def Blade0TimerFunc(blade_name,time):
	blade_e = Bladex.GetEntity(blade_name)
	blade = blade_e.Data

	itime = time - blade.last_time
	blade.time = blade.time + itime
	blade.last_time = time

	#chispa = Bladex.GetEntity("Chispas0")

	posnode = Traps_C.GetSplinePos(blade.blade_spline,blade.time)
	blade_e.SetPosition(posnode[0],posnode[1],posnode[2])
	blade_e.Rotate(0.0,1.0,0.0,blade.vel_rot,1)

	"""

	#Sonido_Cuchilla0_Activada.Play(-231922.078132,-23572.057567,90102.453506,0)
		blade.MessageEvent(MESSAGE_START_WEAPON,0,0)
		if (stop_blades):
			if(player == 0):
				StopBlade(blade,chispa)
	"""
	#chispa.Position = blade.Position[0] + 2250, -23672, 90102

	

