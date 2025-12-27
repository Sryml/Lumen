
import Bladex
import whrandom
import ObjStore
import GameStateAux

def RepeatPeriodicSound(persound):

  if (persound.OnPlay):
    persound.sound.PlaySound(0)
    variation=whrandom.uniform(-persound.frec_variation, persound.frec_variation)
    Bladex.AddScheduledFunc(Bladex.GetTime()+persound.frecuency+variation, RepeatPeriodicSound, (persound,),"RepeatPeriodicSound")



class PeriodicSound:

  OnPlay=0
  ObjId=None
  sound=None
  frecuency=0
  frec_variation=0

  def __init__(self):
    self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
    ObjStore.ObjectsStore[self.ObjId]=self

  def PlayPeriodic(self):

    self.OnPlay=1
    self.sound.PlaySound(0)
    variation=whrandom.uniform(-self.frec_variation, self.frec_variation)
    Bladex.AddScheduledFunc(Bladex.GetTime()+self.frecuency+variation, RepeatPeriodicSound, (self,),"PeriodicSound::PlayPeriodic")

  def StopPeriodic(self):

    self.OnPlay=0

  def persistent_id(self):
    return self.ObjId


  def __getstate__(self):
    # Tiene que devolver c䮯 poder guardar el estado de la clase
    return (1,
            self.ObjId,
            self.OnPlay,
            GameStateAux.SaveEntityAux(self.sound),
            self.frecuency,
            self.frec_variation
           )

  def __setstate__(self,parm):
    # Toma como par⮥tro lo que devuelve __getstate__() y debe recrear la clase
    if parm[0]==1:
      self.ObjId=parm[1]
      self.OnPlay=parm[2]
      ObjStore.ObjectsStore[self.ObjId]=self
      self.sound=GameStateAux.LoadEntityAux(parm[3])
      self.frecuency=parm[4]
      self.frec_variation=parm[5]
    else:
      print "Warning -> Version mismatch in PeriodicSound.__setstate__()"
      self.OnPlay=0
      self.sound=None
      self.frecuency=0
      self.frec_variation=0
      self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
      ObjStore.ObjectsStore[self.ObjId]=self


def CreatePeriodicSound(file_name, sound_name, frecuency, frec_variation, focus):

  persound=PeriodicSound()
  persound.sound=Bladex.CreateEntity(sound_name, "Entity Sound", focus[0], focus[1], focus[2])
  persound.sound.SetSound(file_name)
  persound.frecuency=frecuency
  persound.frec_variation=frec_variation
  persound.sound.Data=persound
  return persound



def CreateEntitySound(file_name, sound_name, focus=(0.0, 0.0, 0.0)):

  entsound=Bladex.CreateEntity(sound_name, "Entity Sound", focus[0], focus[1], focus[2])
  entsound.SetSound(file_name)
  return entsound
