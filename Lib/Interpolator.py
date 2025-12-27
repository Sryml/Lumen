 
 

import Bladex
import ObjStore 



class LinearInt:
  def __init__(self,init_value,end_value):
    self.init_value=init_value
    self.end_value=end_value
    self.period=end_value-init_value

  def Execute(self,value):  # value entre 0 y 1.
    return self.init_value+self.period*value

  def EndExecute(self):
    print "Ended LinearInt"



class RGBInt:
  def __init__(self,init_value,end_value):
    self.init_value=init_value
    self.end_value=end_value
    self.periodR=end_value[0]-init_value[0]
    self.periodG=end_value[1]-init_value[1]
    self.periodB=end_value[2]-init_value[2]

  def Execute(self,value):  # value entre 0 y 1.
    return (self.init_value[0]+self.periodR*value,
            self.init_value[1]+self.periodG*value,
            self.init_value[2]+self.periodB*value
           )

  def EndExecute(self):
    print "Ended RGBInt"




class PositionInt:
  def __init__(self,init_value,end_value):
    self.init_value=init_value
    self.end_value=end_value
    self.periodX=end_value[0]-init_value[0]
    self.periodY=end_value[1]-init_value[1]

  def Execute(self,value):  # value entre 0 y 1.
    return (self.init_value[0]+self.periodX*value,
            self.init_value[1]+self.periodY*value
           )

  def EndExecute(self):
    print "Ended RGBInt"





class Interp:
  def AddAction(self,init_time,end_time,interp_class):
    action=(init_time,end_time,interp_class,end_time-init_time)
    self.Actions.append(action) # Subscribir a Timer
    return action

  def RemoveAction(self,action):
    print "Trying to remove action:",action
    self.Actions.remove(action)

  def ExecuteActions(self,time):
    for i in self.Actions:
      end_time=i[1]
      init_time=i[0]
      if time>end_time:
        i[2].EndExecute()
        self.Actions.remove(i) # Desubscribir de Timer
      elif time>init_time:
        interval_time=i[3]
        value=(time-init_time)/interval_time
        i[2].Execute(value)


  def Kill(self):
    Bladex.RemoveAfterFrameFunc("Interp"+self.name)


  def __init__(self,name,make_persistent=1):
    self.Actions=[]
    self.name=name
    self.make_persistent=make_persistent
    Bladex.SetAfterFrameFunc("Interp"+name,self.ExecuteActions)
    self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
    if make_persistent:
      ObjStore.ObjectsStore[self.ObjId]=self


  def __del__(self):
    self.Kill()

  def persistent_id(self):
    return self.ObjId

  def __getstate__(self):
    # Tiene que devolver c䮯 poder guardar el estado de la clase
    return (1,
            self.ObjId,
            self.Actions,
            self.name,
            self.make_persistent
           )

  def __setstate__(self,parm):
    # Toma como par⮥tro lo que devuelve __getstate__() y debe recrear la clase
    if parm[0]==1:
      self.ObjId=parm[1]
      ObjStore.ObjectsStore[self.ObjId]=self
      self.Actions=parm[2]
      self.name=parm[3]
      self.make_persistent=parm[4]
    else:
      print "Warning -> Version mismatch in Interp.__setstate__()"
      self.Actions=[]
      self.name="UnNamed"
      self.make_persistent=1
      Bladex.SetAfterFrameFunc("Interp"+name,self.ExecuteActions)
      self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
      ObjStore.ObjectsStore[self.ObjId]=self
