



import os
import cPickle
import BBLib
import Bladex
##import ItemTypes
import Breakings
import PickInit
import types
import ObjStore
import cStringIO
import string
import traceback
import sys

from Lumenx import printx

#
import typing

if typing.TYPE_CHECKING:
    apply = lambda fn, args=(), kwds={}: None
    execfile = lambda filename, globals=None, locals=None: None
    cmp = lambda x, y: None


PickDataBase={}
LoadedPickledData={}
aux_dir='.'

## Objetos que hay que ajustar en una segunda pasada
FixDataBase=[]



##class PersistentObject:
##  def __init__(self):
##    self.ObjId=str(id(self)) # Para identificarlo al grabar/guardar
##
##  def  __setstate__(self,parm):
##    self.ObjId=parm[1]
##    LoadedPickledData[self.ObjId]=self
##
##  def persistent_id(self):
##    return self.ObjId

def LoadGlobalCompVars(filename,dest_dict):

  file=open(filename)
  u=cPickle.Unpickler(file)

  u.persistent_load=persistent_load
  ret=u.load()
  file.close()

  # ret es un diccionario con las variables globales de tipo lista, tupla y diccionario.
  for i in ret.keys():
    dest_dict[i]=ret[i]




def InitGameState(aux_dir):
##  Bladex.SetCallCheck(1)
##  Bladex.OpenDebugChannel("Salida")

  #print "InitGameState",aux_dir
  global PickDataBase
  PickDataBase={}
  #print PickDataBase
  #print "PickDataBase len:",len(PickDataBase.keys())

  filename="%s/PickDataBase.dat"%(aux_dir,)
  funcfile=open(filename,"rt")
  p=cPickle.Unpickler(funcfile)
  PickDataBase=p.load()
  funcfile.close()
  #print "PickDataBase read"
  #print PickDataBase
  #print "PickDataBase len:",len(PickDataBase.keys())


def CleanLoadTemp():
  #print "CleanLoadTemp()"
  global PickDataBase
  PickDataBase={}
  #print PickDataBase
  #print PickDataBase.keys()
  #print "PickDataBase len:",len(PickDataBase.keys())

  global LoadedPickledData
  LoadedPickledData={}



def CleanSaveTemp():
  #print "CleanSaveTemp()"
  global PickDataBase
  PickDataBase={}

  global LoadedPickledData
  LoadedPickledData={}




def EndGameState(aux_dir):

  filename="%s/PickDataBase.dat"%(aux_dir,)
  funcfile=open(filename,"wt")
  p=cPickle.Pickler(funcfile)
  p.dump(PickDataBase)
  funcfile.close()
  #print "PickDataBase written"
  #print PickDataBase.keys()
  #print "PickDataBase len:",len(PickDataBase.keys())




def persistent_id(obj):
  if hasattr(obj, "persistent_id"):
    return obj.persistent_id()
  else:
    return ManualReduction(obj)


def persistent_load(obj_id):
  if obj_id[0] == "*":
    return ManualConstruction(obj_id)
  else:
    #print "Found at ObjStore",ObjStore.ObjectsStore[obj_id],obj_id
    return ObjStore.ObjectsStore.get(obj_id, None)

##  if LoadedPickledData.has_key(filename):
##    print "GameStateAux.persistent_load Found in LoadedPickledData",obj_id
##    return LoadedPickledData[obj_id]
##  else:
##    filename="%s/%s.dat"%(aux_dir,obj_id)
    filename="%s/%s.dat"%("f",obj_id)

    dat=GetPickledData(filename)

    try:
      LoadedPickledData[dat.persistent_id()]=dat
    except KeyError:
      LoadedPickledData[obj_id]=dat
    return dat








def SavePickData(filename,data):
##  print "SavePickData, saving",filename,data
  if PickDataBase.has_key(filename):
    return

  string_file=cStringIO.StringIO()
  p=cPickle.Pickler(string_file)
  p.persistent_id=persistent_id
  # data = SavePickleEnsure(data) #
  p.dump(data)
  PickDataBase[filename]=string_file.getvalue()





def GetPickledData(filename):

  string_file = cStringIO.StringIO(PickDataBase[filename])
  u=cPickle.Unpickler(string_file)

  u.persistent_load=persistent_load
  ret=u.load()
  # ret = LoadPickleEnsure(ret) #
  return ret


# ---------------------------------- Sryml
# 手动归约函数
def ManualReduction(obj):
    ret = None
    construction = None

    data_t = type(obj)
    if data_t == types.FunctionType:
        construction, args = PickInit.RedFunction(obj)
    elif data_t == types.BuiltinFunctionType:
        construction, args = PickInit.RedCFunction(obj)

    if construction is not None:
        ret = "*%s" % repr(((construction.__name__, GetFunctionFile(construction)), args))
    return ret

# 手动构造函数
def ManualConstruction(obj_id):
    (func_name, lib_name), args = eval(obj_id[1:])
    __import__(lib_name)
    construction = sys.modules[lib_name].__dict__[func_name]

    return apply(construction, args)

# def SavePickleEnsure(data):
#     data_t = type(data)
#     if data_t == types.FunctionType:
#         return PickInit.RedFunction(data)
#     elif data_t == types.BuiltinFunctionType:
#         return PickInit.RedCFunction(data)

#     return (None, data)


# def LoadPickleEnsure(data_ex, res_obj=None, res_field=""):
#     reconstructor, data = data_ex
#     if reconstructor is not None:
#         data = apply(reconstructor, data)
    
#     if res_obj:
#         setattr(res_obj, res_field, data)
#     else:
#         return data


def SaveData(filename, d):
    funcfile = open(filename, "wt")
    p = cPickle.Pickler(funcfile)
    p.persistent_id = persistent_id
    p.dump(d)
    funcfile.close()


def LoadData(filename):
    funcfile = open(filename, "rt")
    p = cPickle.Unpickler(funcfile)
    p.persistent_load = persistent_load
    ret = p.load()
    funcfile.close()
    return ret
# ----------------------------------


def GetPickledObjects(filename):
  "Loads the ObjStore file"
  import Reference

  f=open(filename,'rt')
  u=cPickle.Unpickler(f)
  u.persistent_load = ManualConstruction
  ret=u.load()
  f.close()

  global FixDataBase
  for i in FixDataBase:
    # Reference.debugprint("Fixing",i)
    func_id=i[0]
    ob_id, method_name = func_id
    if ObjStore.ObjectsStore.has_key(ob_id):
      cl=ObjStore.ObjectsStore[ob_id]
      #print i[1]
      cl_to_assign=None
      if i[4]=="Entity":
        cl_to_assign=Bladex.GetEntity(i[1])
        # Reference.debugprint("Found Entity",cl_to_assign)
      else:
        cl_to_assign=ObjStore.ObjectsStore[i[1]]
        # Reference.debugprint("Found class",cl_to_assign)

      if cl_to_assign:
        if i[4]=="Object":
          setattr(cl_to_assign, i[2], cl)
          # exec("cl_to_assign."+i[2]+"=cl")
          #print "Fixed relationship for object",i
          #print "Executed cl_to_assign."+str(i[2])+"=cl"
          #print "cl_to_assign:",cl_to_assign
          #print "cl:",cl
        else:
          setattr(cl_to_assign, i[2], getattr(cl, method_name))
          # exec("cl_to_assign."+i[2]+"=cl."+method_name)
          #print "Fixed relationship for function",i
      else:
        Reference.debugprint("Can't fix FixDataBase.",i[1],"Not found.",i)





    else:
      Reference.debugprint("Can't fix FixDataBase.",ob_id,"Not found.")

  FixDataBase=[]



def LoadAutoBODs(dir):
  files=os.listdir(dir)
  for i in files:
    if i[-4:]==".BOD":
      filename="%s/%s"%(dir,i)
      BBLib.ReadAutoBOD(filename)


def LoadMMPs(files):
  for i in files:
    i = string.replace(i, "\\", "/")
    BBLib.ReadMMP(i)


def LoadAlphaBMPs(files):
  for internal_name, path in files.items():
    Bladex.ReadAlphaBitMap(path, internal_name)


def LoadBMPs(files):
  for internal_name, path in files.items():
    Bladex.ReadBitMap(path, internal_name)


def LoadBODs(files):
  for i in files:
    i = string.replace(i, "\\", "/")
    BBLib.ReadBOD(i)







def AddWeaponToInventory(inv,weapon_name):
  import Reference

  object_flag=Reference.GiveObjectFlag(weapon_name)
  if object_flag == Reference.OBJ_BOW:
      inv.AddBow(weapon_name)
  else:
      flag=Reference.GiveWeaponFlag(weapon_name)
      #inv.AddWeapon(i[0],flag)
      inv.AddWeapon(weapon_name,flag)
    

def LinkRight(weapon_name,inv,owner):
	weapon = Bladex.GetEntity(weapon_name)
	owner.Unlink(weapon)
	inv.LinkRightHand(weapon_name)

def LinkLeft(weapon_name,inv,owner):
	weapon = Bladex.GetEntity(weapon_name)
	owner.Unlink(weapon)
	inv.LinkLeftHand(weapon_name)


def LinkBack(weapon_name,inv,owner):
	weapon = Bladex.GetEntity(weapon_name)
	owner.Unlink(weapon)
	inv.LinkBack(weapon_name)

def LinkLeft2B(weapon_name,inv,owner):
	weapon = Bladex.GetEntity(weapon_name)
	owner.Unlink(weapon)
	inv.LinkLeftHand2(weapon_name)

def AddQuiverToInventory(inv,quiver_name):
  obj=Bladex.GetEntity(quiver_name)
##  ItemTypes.ItemDefaultFuncs(obj)
  inv.AddQuiver(quiver_name)


def SaveFunctionAux(func): # -Sryml
  return func
  # return SavePickleEnsure(func)


def LoadFunctionAux(func_id_ex,res_obj=None,res_field="",aux=None): # -Sryml
  if res_obj:
    setattr(res_obj, res_field, func_id_ex)
  else:
    return func_id_ex
  # return LoadPickleEnsure(func_id_ex,res_obj,res_field)



def SaveObjectAux(obj):
  try:
    return ("o",(obj.persistent_id(),None))
  except Exception,exc:
    print "Exception in SaveObjectAux()",exc," with object",obj
    return ("n",(None,None))



def LoadObjectAux(obj_id_ex,res_obj=None,res_field=None,aux=None):
  assign_obj=None
  obj_id=obj_id_ex[1]
  obj_kind=obj_id_ex[0]
  if obj_kind=="o": # Metodo
    ob_id=obj_id[0]
    if ObjStore.ObjectsStore.has_key(ob_id):
      assign_obj=ObjStore.ObjectsStore[ob_id]
    else:
      if res_obj is not None:
        #print "FixDataBase.append() Entity->",obj_id,res_field,ob_id
        FixDataBase.append((obj_id,res_obj.ObjId,res_field,ob_id,"Object"))
      else:
        print "Can not find object to add to FixDataBase",obj_id_ex
  elif func_kind=="n":  # None
    assign_obj=None

  if res_obj:
    exec("res_obj."+res_field+"=assign_obj")
  else:
    return assign_obj


def SaveEntityAux(ent):
  if ent:
    try:
      return ent.Name
    except:
      # traceback.print_exc()
      print "Error getting entity name",ent
      return None
  return None


def LoadEntityAux(ent_id):
  if ent_id:
    return Bladex.GetEntity(ent_id)
  return None


def SaveExtraDataAux(file,aux_dir):
    try:
      import ExtraData

      filename="%s/ExtraData.dat"%(aux_dir,)
      if ExtraData.SaveExtraData(filename):
          file.write('try:\n')
          file.write('  GameStateAux.LoadExtraDataAux("%s")\n'%(filename,))
          file.write('except:\n')
          file.write('  print "Can not load ExtraData"\n\n')
    except:
      pass


def LoadExtraDataAux(filename):
    import ExtraData

    ExtraData.LoadExtraData(filename)

def GetAllBases(check_class):
  ret=[]
  bases=check_class.__bases__
  for i in bases:
    ret.append(i)
    bases_i=GetAllBases(i)
    for j in bases_i:
      ret.append(j)

  return ret




def GetNewMembers(check_class):
  "Obtiene los miembros nuevos de la clase y de sus clases base"

  class_dict={}
##  bases=check_class.__class__.__bases__
  bases=GetAllBases(check_class.__class__)
  for i in bases:
    class_dict.update(i.__dict__)

  class_dict.update(check_class.__class__.__dict__)
  check_dict=check_class.__dict__
  new_members={}
  for j in check_dict.keys():
    if not class_dict.has_key(j):
      new_members[j]=check_dict[j]

  return new_members



def SaveNewMembers(check_class):
  if type(check_class)!=types.InstanceType:
    return ()

  ret=[]
  # entity_type=type(Bladex.GetEntity("Camera")) # -Sryml
  members=GetNewMembers(check_class)
  members_keys=members.keys()
  for i in members_keys:
    member=members[i]
    member_t=type(member)
    #print check_class,i,member_t
    if member_t in (types.FunctionType, types.MethodType, types.BuiltinFunctionType):
      ret.append(("Function",i,SaveFunctionAux(member)))
    # elif member_t==entity_type:
    #   ret.append(("Entity",i,SaveEntityAux(member)))
    else:
      ret.append(("Other",i,member))

##  altered_methods=GetAlteredMethods(check_class)
##  altered_methods_keys=altered_methods.keys()
##  for i in altered_methods_keys:
##    member=altered_methods[i]
##    ret.append(("Function",i,SaveFunctionAux(member)))

  return tuple(ret)


def LoadNewMembers(mod_class,new_members):

  try:
    for i in new_members:
      if i[0]=="Function":
        LoadFunctionAux(i[2],mod_class,i[1])
      elif i[0]=="Entity":
        mod_class.__dict__[i[1]]=LoadEntityAux(i[2])
      else:
        mod_class.__dict__[i[1]]=i[2]
  except Exception,exc:
    print "LoadNewMembers() Error",exc,mod_class,new_members










def GetBaseMethod(check_class,method_name,bases):

  for i in bases:
    try:
      tmp_string="i.__dict__['"+method_name+"']"
      return eval(tmp_string)
    except:
      pass

  return None


def GetAlteredMethods(check_class):
  "Obtiene los metodos de una clase y de sus clases base que han sido cambiados"

  class_dict={}
  bases=GetAllBases(check_class.__class__)
  for i in bases:
    class_dict.update(i.__dict__)

  class_dict.update(check_class.__class__.__dict__)

  altered_beast={}
  for j in class_dict.keys():
    member=eval("check_class."+j)

    if type(member)==types.MethodType:
      found_func=eval("member.im_func")
      tmp_string="check_class.__class__.__dict__['"+j+"']"
      try:
        reference_func=eval(tmp_string)
      except:
        reference_func=GetBaseMethod(check_class,j,bases)

      if found_func!=reference_func:
        altered_beast[j]=member


  return altered_beast



def GetFunctionFile(f):
    # Rewritten -Sryml
    if not f:
        return "Error, None is not  a function"
    try:
        return f.func_globals["__name__"]
    except:
        printx("Exception in GetFunctionFile", f)
        return "Error getting lib"

def LinkLeftBack(weapon_name,inv,owner):
	weapon = Bladex.GetEntity(weapon_name)
	owner.Unlink(weapon)
	inv.LinkLeftBack(weapon_name)
def LinkRightBack(weapon_name,inv,owner):
	weapon = Bladex.GetEntity(weapon_name)
	owner.Unlink(weapon)
	inv.LinkRightBack(weapon_name)

