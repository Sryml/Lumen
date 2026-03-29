


import Bladex
import copy_reg
import types
import sys

from Lumenx import printx

GlobalModulesCache=None
GlobalFunctionsCache=None
GlobalCFunctionsCache=None

def GetGlobalsAux():
    import sys
    try:
        1 + ''
    except:
        frame = sys.exc_info()[2].tb_frame.f_back

    while frame:
        globs=frame.f_globals
        frame=frame.f_back

    return globs


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
  if hasattr(e, "Name"):
    return ConstEntity,(e.Name,)
  else:
    printx("PickInit.RedEntity() can not get entity name")
    return ConstEntity,(None,)


def RegisterPickEntity():
  #Creo uno cualquiera.  ¿Revisar?
  #gmadlig=Bladex.CreateEntity('PickEntity','Entity Spot',0,0,0)
  gmadlig=Bladex.GetEntity("Camera") # by Sryml

  copy_reg.pickle(type(gmadlig),RedEntity,ConstEntity)










def FindFunctionAux(module,fun_name):

  if module.__dict__.has_key(fun_name):
    return module.__dict__[fun_name]
  return None



def ConstFunction(fun_name, lib_name):
    # Rewritten -Sryml
    if fun_name == "<lambda>":
        return None
    try:
        __import__(lib_name)
        return sys.modules[lib_name].__dict__[fun_name] # Considering the case of module packages
    except:
        printx("Error: Cannot find function %s in library %s" % (fun_name, lib_name))
        return None



def RedFunction(f):
  import GameStateAux
  s=GameStateAux.GetFunctionFile(f)

  return ConstFunction,(f.func_name,s)


def RegisterPickFunction():
  import types

  copy_reg.pickle(types.FunctionType,RedFunction,ConstFunction)





def ConstMethod(obj_id,method_name):
  import types
  import ObjStore

  try:
    obj=ObjStore.ObjectsStore[obj_id]
    assign_func=eval("obj."+method_name)
    return assign_func
  except Exception,exc:
##    import pdb
##    pdb.set_trace()
    print "PickInit.ConstMethod() can not find method",obj_id,method_name
    if ObjStore.ObjectsStore.has_key(obj_id):
        print "Object ",obj_id,"exists. -> ",ObjStore.ObjectsStore[obj_id]
    else:
        print "Object ",obj_id,"does not exist."
        print ObjStore.ObjectsStore

    print "Exception",exc
    return None

def RedMethod(f):
  try:
    return ConstMethod,(f.im_class.persistent_id(f.im_self),f.im_func.func_name)
  except:
    print "PickInit.RedMethod() can not register method",f
    return ConstMethod,(None,None)


def RegisterPickMethod():
  import types

  copy_reg.pickle(types.MethodType,RedMethod,ConstMethod)






def ConstCFunction(fun_name,func_self):
  import Reference
  Reference.debugprint("ConstCFunction: '",fun_name,"','",func_self,"'")
  if func_self is not None:
    this_type = func_self[0]
    if this_type == "Entity":
      o = Bladex.GetEntity(func_self[1])
    elif this_type == "Sound":
      o = Bladex.GetSound(func_self[1])
    elif this_type == "Sector":
      o = Bladex.GetSector(func_self[1])
    elif this_type == "Inventory":
      o = Bladex.GetEntity(func_self[1])
      if hasattr(o, "GetInventory"):
        o = o.GetInventory()
      else:
        o = None

    assign_func = getattr(o, fun_name, None)
    return assign_func

  # La busco en funciones C
  funcs=GetGlobalsAux2(types.BuiltinFunctionType)
  for i in funcs:
    if i[1].__name__==fun_name:
      return i[1]
  # La busco en los modulos
  # Primero en los de Blade
  # import Bladex
  import Traps_C
  import B3DLib
  mods=(Bladex,B3DLib,Traps_C)
  for i in mods:
    func=FindFunctionAux(i,fun_name)
    if func:
        return func
  # Y luego en los otros
  global_mods=GetGlobalsAux2(types.ModuleType)
  for i in global_mods:
    if i not in mods:
        func=FindFunctionAux(i[1],fun_name)
        if func:
            return func

  print "Warning, can't find global function",fun_name
  return None



def RedCFunction(f):
  if getattr(f, "__self__", None) is None: # Asume que es una entidad
    return ConstCFunction,(f.__name__,None)
  else:
    return ConstCFunction,(f.__name__,f.__self__.Name)


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
  RegisterPickFunction()
  RegisterPickSector()
  RegisterPickMethod()
  RegisterPickCFunction()
  RegisterPickEntInventory()
  print "Executed PickInit.Init()"
