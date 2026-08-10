


import Bladex
import copy_reg
import types
import sys
import traceback
import Lumenx
import cPickle

from Lumenx import printx

#
import typing

if typing.TYPE_CHECKING:
    apply = lambda fn, args=(), kwds={}: None
    execfile = lambda filename, globals=None, locals=None: None
    cmp = lambda x, y: None

GlobalModulesCache=None
GlobalFunctionsCache=None
GlobalCFunctionsCache=None

def GetGlobalsAux(): # -Sryml
    return sys.modules["__main__"].__dict__


def GetGlobalsAux2(req_type):
##    global GlobalModulesCache
##    global GlobalFunctionsCache
##    global GlobalCFunctionsCache
##
##    if req_type==types.ModuleType and GlobalModulesCache:
##        return GlobalModulesCache
##    elif (req_type==types.FunctionType or req_type==types.MethodType) and GlobalFunctionsCache:
##        return GlobalFunctionsCache
##    elif req_type==types.BuiltinFunctionType and GlobalCFunctionsCache:
##        return GlobalCFunctionsCache

    g=GetGlobalsAux()
    elems=[]
    for i in g.items():
        if type(i[1])==req_type:
            elems.append(i)

##    if req_type==types.ModuleType:
##        GlobalModulesCache=elems
##    elif req_type==types.FunctionType or req_type==types.MethodType:
##        GlobalFunctionsCache=elems
##    elif req_type==types.BuiltinFunctionType:
##        GlobalCFunctionsCache=elems
    return elems


def ConstSound(sound_name,sound_file,volume,base_volume,min_distance,max_distance,scale,send_notify):
  s=Bladex.CreateSound(sound_file,sound_name)
##  print s
  if not s:
    return
  s.Volume=volume
  s.BaseVolume=base_volume
  s.MinDistance=min_distance
  s.MaxDistance=max_distance
  s.Scale=scale
  s.SendNotify=send_notify
  return s


def RedSound(s):
  return ConstSound,(s.Name,"",s.Volume,s.BaseVolume,s.MinDistance,s.MaxDistance,s.Scale,s.SendNotify)


def RegisterPickSound():
  #Creo uno cualquiera.  ¿Revisar?
  gmadlig=Bladex.CreateSound('../../sounds/golpe-madera-mediana.wav', 'GolpeMaderaMediana')

  copy_reg.pickle(type(gmadlig),RedSound,ConstSound)





def ConstEntity(ent_name):
  if ent_name is None:
    return None
  e=Bladex.GetEntity(ent_name)
  return e


def RedEntity(e):
  # -Sryml
  try:
    return ConstEntity,(e.Name,)
  except:
    printx("PickInit.RedEntity() can not get entity name")
    return ConstEntity,(None,)


def RegisterPickEntity():
  #Creo uno cualquiera.  ¿Revisar?
  #gmadlig=Bladex.CreateEntity('PickEntity','Entity Spot',0,0,0)
  gmadlig=Bladex.GetEntity("Camera") # by Sryml

  copy_reg.pickle(type(gmadlig),RedEntity,ConstEntity)










def FindFunctionAux(module,fun_name):
  return module.__dict__.get(fun_name, None)



def ConstFunction(fun_name, lib_name):
    # Rewritten -Sryml
    if fun_name == "<lambda>":
        return None
        
    __import__(lib_name)
    ret = sys.modules[lib_name].__dict__.get(fun_name, None) # Considering the case of module packages
    if not ret:
        printx("Error: Cannot find function %s in library %s" % (fun_name, lib_name))
    return ret



def RedFunction(f):
  import GameStateAux
  s=GameStateAux.GetFunctionFile(f)

  return ConstFunction,(f.func_name,s)


def RegisterPickFunction():
  import types

  copy_reg.pickle(types.FunctionType,RedFunction,ConstFunction)





def ConstMethod(im_self, method_name): # -Sryml
  import Reference
  import ObjStore
  import GameStateAux

  ret = getattr(im_self, method_name, None)
  if not ret:
    printx("PickInit.ConstMethod() can not find method",method_name,"in object",im_self)
  return ret

  if ObjStore.ObjectsStore.has_key(obj_id):
    obj = ObjStore.ObjectsStore[obj_id]
    if hasattr(obj, method_name):
        return getattr(obj, method_name)
  #   Reference.debugprint("PickInit.ConstMethod() can not find method",method_name,"in object",obj_id)
  # else:
  #   Reference.debugprint("PickInit.ConstMethod() can not find object",obj_id)
  #
  if res_obj is not None:
    if type(res_obj) == type(Bladex.GetEntity("Camera")):
      # printx("FixDataBase.append() Entity->",(obj_id, method_name),res_obj.Name,res_field,obj_id)
      GameStateAux.FixDataBase.append(((obj_id, method_name), res_obj.Name,res_field,obj_id,"Entity"))
    else:
      #print "FixDataBase.append() class->",(obj_id, method_name),res_obj.ObjId,res_field,obj_id
      GameStateAux.FixDataBase.append(((obj_id, method_name), res_obj.ObjId,res_field,obj_id,None))
  else:
    Reference.debugprint("Can not find object to add to FixDataBase", (obj_id, method_name))

  return None


def RedMethod(f): # -Sryml
  im_class = f.im_class
  func_name = f.im_func.func_name
  if im_class == Lumenx.__FunctionDecorator:
    return RedCFunction(f.im_func)
  elif im_class == Lumenx.B_PyEntity_Proxy:
    return RedCFunction(getattr(f.im_self.target, func_name))
  #
  im_self = f.im_self
  if im_self is None:
    # ?????
    im_self = im_class
  return ConstMethod,(im_self,func_name)
  # if hasattr(im_self, "persistent_id"):
  #   return ConstMethod,(im_self,func_name)
  # else:
  #   printx("PickInit.RedMethod() can not register method",f)
  #   return ConstMethod,(None,None)


def RegisterPickMethod():
  import types

  copy_reg.pickle(types.MethodType,RedMethod,ConstMethod)






def ConstCFunction(fun_name, func_self): # -Sryml
  import Reference

  func_self = cPickle.loads(func_self)
  if func_self is None:
    return None

  # Reference.debugprint("ConstCFunction: '%s'," % fun_name, func_self)
  # if func_self is not None:
  #   this_type = func_self[0]
  #   if this_type == "Entity":
  #     o = Bladex.GetEntity(func_self[1])
  #   elif this_type == "Sound":
  #     o = Bladex.GetSound(func_self[1])
  #   elif this_type == "Sector":
  #     o = Bladex.GetSector(func_self[1])
  #   elif this_type == "Inventory":
  #     o = Bladex.GetEntity(func_self[1])
  #     if hasattr(o, "GetInventory"):
  #       o = o.GetInventory()
  #     else:
  #       o = None

  #   assign_func = getattr(o, fun_name, None)
  #   return assign_func

  # La busco en funciones C
  if func_self == "Module":
    func = sys.modules["__builtin__"].__dict__.get(fun_name, None)
    if func:
      return func
    # La busco en los modulos
    # Primero en los de Blade
    import Bladex,Traps_C,B3DLib,BUIxc,BBLibc
    mods=(Bladex,Traps_C,B3DLib,BUIxc,BBLibc)
    for i in mods:
      func=i.__dict__.get(fun_name, None)
      if func:
          return func
    # Y luego en los otros
    # global_mods=GetGlobalsAux2(types.ModuleType)
    # for i in global_mods:
    #   if i not in mods:
    #       func=FindFunctionAux(i[1],fun_name)
    #       if func:
    #           return func
  ret = getattr(func_self, fun_name, None)
  if ret is None:
    printx("Warning, can't find builtin function", (fun_name,func_self))
  return ret



def RedCFunction(f):
  func_self = getattr(f, "__self__", "Module")
  if func_self is None:
    func_self = "Module"
  return ConstCFunction,(f.__name__, cPickle.dumps(func_self))
  # import Reference
  # if getattr(f, "__self__", None) is None: # Asume que es una entidad
  #   return ConstCFunction,(f.__name__,None)
  # else:
  #   this = f.__self__
  #   this_type = type(this)
  #   if this_type == type(Bladex.GetEntity(0)) and hasattr(this, "Name"):
  #     func_self = ("Entity",this.Name)
  #   elif this_type == type(Bladex.GetSound("GolpeMaderaMediana")) and hasattr(this, "Name"):
  #     func_self = ("Sound",this.Name)
  #   elif this_type == type(Bladex.GetSector(0)):
  #     func_self = ("Sector",this.Index)
  #   elif this_type == type(Bladex.GetEntity(0).GetInventory()) and hasattr(this, "Owner"):
  #     func_self = ("Inventory",this.Owner)
  #   else:
  #     Reference.debugprint("RedCFunction() Warning, unknown type for builtin function",f)
  #     return ConstCFunction,(None,None)
    
  #   return ConstCFunction,(f.__name__,func_self)


def RegisterPickCFunction():
  import types

  copy_reg.pickle(types.BuiltinFunctionType,RedCFunction,ConstCFunction)

















def ConstSector(sec_idx):
  e=Bladex.GetSector(sec_idx)
  return e

def RedSector(s):
  return ConstSector,(s.Index,)


def RegisterPickSector():
  gmadlig=Bladex.GetSector(0)
  if not gmadlig:
      print "ERROR in RegisterPickSector()"
      return

  copy_reg.pickle(type(gmadlig),RedSector,ConstSector)

# ---------------------------------
def ConstEntInventory(name):
    if name is None:
        return None
    o = Bladex.GetEntity(name).GetInventory()
    return o


def RedEntInventory(o):
    return ConstEntInventory, (getattr(o, "Owner", None),)


def RegisterPickEntInventory():
    gmadlig = Bladex.GetEntity(0).GetInventory()
    copy_reg.pickle(type(gmadlig), RedEntInventory, ConstEntInventory)


def ConstEllipsis():
    return Ellipsis

def RedEllipsis(o):
    return ConstEllipsis, ()

def RegisterPickEllipsis():
    copy_reg.pickle(types.EllipsisType,RedEllipsis,ConstEllipsis)


# ---------------------------------

def ClearCaches():
  global GlobalModulesCache
  global GlobalFunctionsCache
  global GlobalCFunctionsCache

  GlobalModulesCache=None
  GlobalFunctionsCache=None
  GlobalCFunctionsCache=None




def Init():
  ClearCaches()
  RegisterPickSound()
  RegisterPickEntity()
  # RegisterPickFunction() # Unable to cover serialization behavior
  RegisterPickSector()
  RegisterPickMethod()
  # RegisterPickCFunction() # Unable to cover serialization behavior
  RegisterPickEntInventory()
  RegisterPickEllipsis()
  print "Executed PickInit.Init()"
