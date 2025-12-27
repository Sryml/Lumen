import Bladex

def GetStepSound(file,name):
	step_sound=Bladex.CreateSound(file,name)
	step_sound.Volume=1.0
	step_sound.MinDistance=1000
	step_sound.MaxDistance=10000
	return(step_sound)

def GetStepSoundSet(file,name):
	s1=GetStepSound(file+"1.wav",name+"1")
	s2=GetStepSound(file+"2.wav",name+"2")
	s3=GetStepSound(file+"3.wav",name+"3")
	return([s1,s2,s3])

stone_step_sounds=GetStepSoundSet("../../sounds/Paso Piedra ","StepStone1")

l_step=0
def StepEventFunc(pj_name,event):
      person=Bladex.GetEntity(pj_name)
      pos=person.Position
	#global l_step
      stone_step_sounds[1].Play(pos[0],pos[1],pos[2],0)
      #l_step=l_step+1

pj=Bladex.GetEntity("Player1")
pj.AddAnmEventFunc("StepH_RFoot",StepEventFunc)
pj.AddAnmEventFunc("StepH_LFoot",StepEventFunc)
