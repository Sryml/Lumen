import whrandom

PasoDefault1=Bladex.CreateSound('../../sounds/paso-piedra-1.wav', 'PasoDefault1')
PasoDefault1.SendNotify=1
PasoDefault1.Volume=0.7
PasoDefault1.MaxDistance=8000.0

PasoDefault2=Bladex.CreateSound('../../sounds/paso-piedra-2.wav', 'PasoDefault2')
PasoDefault2.SendNotify=1
PasoDefault2.Volume=0.7
PasoDefault2.MaxDistance=8000.0

PasoDefault3=Bladex.CreateSound('../../sounds/paso-piedra-3.wav', 'PasoDefault3')
PasoDefault3.SendNotify=1
PasoDefault3.Volume=0.7
PasoDefault3.MaxDistance=8000.0


NetStepSoundList = [PasoDefault1,PasoDefault2,PasoDefault3]

Bladex.AddStepSound("default",PasoDefault1)
Bladex.AddStepSound("default",PasoDefault2)
Bladex.AddStepSound("default",PasoDefault3)

def PlayNetStepSound(Entity):
	snd = NetStepSoundList[whrandom.randint(0,len(NetStepSoundList)-1)]
	snd.Play(Entity.Position[0],Entity.Position[1],Entity.Position[2])




Bladex.AddMaterialStepSound("default","default","default")
Bladex.AddActionStepSound("default","default","default")