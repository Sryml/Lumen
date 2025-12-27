



import os
import cPickle
import BBLib
import Bladex
import Reference
##import ItemTypes
import Breakings
import PickInit
import types
import ObjStore
import cStringIO
import string





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
  ret=None
  try:
    ret=obj.persistent_id()
  except AttributeError:
    pass
  except Exception,exc:
    print "GameStateAux.persistent_id()",exc
  return ret



def persistent_load(obj_id):

  if ObjStore.ObjectsStore.has_key(obj_id):
    #print "Found at ObjStore",ObjStore.ObjectsStore[obj_id],obj_id
    return ObjStore.ObjectsStore[obj_id]

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
  p.dump(data)
  PickDataBase[filename]=string_file.getvalue()





def GetPickledData(filename):

  string_file = cStringIO.StringIO(PickDataBase[filename])
  u=cPickle.Unpickler(string_file)

  u.persistent_load=persistent_load
  ret=u.load()
  return ret


def GetPickledObjects(filename):
  "Loads the ObjStore file"

  f=open(filename,'rt')
  u=cPickle.Unpickler(f)
  ret=u.load()
  f.close()

  global FixDataBase
  for i in FixDataBase:
    print "Fixing",i
    func_id=i[0]
    ob_id=func_id[0]
    if ObjStore.ObjectsStore.has_key(ob_id):
      cl=ObjStore.ObjectsStore[ob_id]
      #print i[1]
      cl_to_assign=None
      if i[4]=="Entity":
        cl_to_assign=Bladex.GetEntity(i[1])
        print "Found Entity",cl_to_assign
      else:
        cl_to_assign=ObjStore.ObjectsStore[i[1]]
        print "Found class",cl_to_assign

      if cl_to_assign:
        if i[4]=="Object":
          exec("cl_to_assign."+i[2]+"=cl")
          #print "Fixed relationship for object",i
          #print "Executed cl_to_assign."+str(i[2])+"=cl"
          #print "cl_to_assign:",cl_to_assign
          #print "cl:",cl
        else:
          exec("cl_to_assign."+i[2]+"=cl."+func_id[1])
          #print "Fixed relationship for function",i
      else:
        print "Can't fix FixDataBase.",ob_id,"Not found.",i





    else:
      print "Can't fix FixDataBase.",ob_id,"Not found."

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
  for i in files:
    Bladex.ReadAlphaBitMap(i[0],i[1])


def LoadBMPs(files):
  for i in files:
    Bladex.ReadBitMap(i[0],i[1])


def LoadBODs(files):
  for i in files:
    i = string.replace(i, "\\", "/")
    BBLib.ReadBOD(i)







def AddWeaponToInventory(inv,weapon_name):

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


def SaveFunctionAux(func):

  try:
    func_type=type(func)
    if  func_type == types.MethodType:
      ob_id=func.im_self.persistent_id()
      #print "Saving Method:",ob_id,func.im_func.func_name
      return ("m",(ob_id,func.im_func.func_name))
  ##    try:
  ##      id=func.im_class.persistent_id()
  ##      return (id,func.im_func.func_name)
  ##    except:
  ##      print "WARNING, SaveFunctionAux()-> Omiting method",func.im_func.func_name
  ##      return None

    elif func_type==types.FunctionType:
      return ("f",(func.func_name,GetFunctionFile(func)))
    elif func_type==types.BuiltinFunctionType:
      if not func.__self__:
        return ("cf",(func.__name__,None))
      else: # Asumo que son entidades
        return ("cf",(func.__name__,func.__self__.Name))

    return ("n",(None,None))

  except Exception,exc:
    print "Exception in SaveFunctionAux()",exc," with function",func
    return ("n",(None,None))






def LoadFunctionAux(func_id_ex,res_obj=None,res_field=None,aux=None):

  assign_func=None
  
  if type(func_id_ex) != types.TupleType:
    print "LoadFunctionAux() ERROR, invalid parameters",type(func_id_ex)
    return

  func_id=func_id_ex[1]

  func_kind=func_id_ex[0]
  if func_kind=="m": # Metodo
    ob_id=func_id[0]
    if ObjStore.ObjectsStore.has_key(ob_id):
      cl=ObjStore.ObjectsStore[ob_id]
      #res_obj.__dict__[res_field]=eval("cl."+func_id[1])
      assign_func=eval("cl."+func_id[1])
    else:
      if res_obj is not None:
        if type(res_obj) == type(Bladex.GetEntity(0)):
          #print "FixDataBase.append() Entity->",func_id,res_obj.Name,res_field,ob_id
          FixDataBase.append((func_id,res_obj.Name,res_field,ob_id,"Entity"))
        else:
          #print "FixDataBase.append() class->",func_id,res_obj.ObjId,res_field,ob_id
          FixDataBase.append((func_id,res_obj.ObjId,res_field,ob_id,None))
      else:
        print "Can not find object to add to FixDataBase",func_id_ex
  elif func_kind=="f":  # Funcion
    assign_func=(PickInit.ConstFunction(func_id[0],func_id[1]))
  elif func_kind=="cf": # Funcion C
    assign_func=(PickInit.ConstCFunction(func_id[0],func_id[1]))
  elif func_kind=="n":  # None
    assign_func=None

  #res_obj.__dict__[res_field]=assign_func
  if res_obj:
    exec("res_obj."+res_field+"=assign_func")
  else:
    return assign_func


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
  entity_type=type(Bladex.GetEntity(0))
  members=GetNewMembers(check_class)
  members_keys=members.keys()
  for i in members_keys:
    member=members[i]
    member_t=type(member)
    #print check_class,i,member_t
    if member_t==types.FunctionType or member_t==types.MethodType:
      ret.append(("Function",i,SaveFunctionAux(member)))
    elif member_t==entity_type:
      ret.append(("Entity",i,SaveEntityAux(member)))
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
  if not f:
    return "Error, None is not  a function"
  try:
    # No se si esto depende de W2000
    import string
    s=str(f.func_code)
    s2=string.split(s,'"') # Siempre?
    func_path=s2[1]  # Siempre?

    import os
    filename=os.path.split(func_path)[1]
    filename_noext=os.path.splitext(filename)[0]

    return filename_noext
  except e:
    print "Exception in GetFunctionFile",e
    return "Error getting lib"

def LinkLeftBack(weapon_name,inv,owner):
	weapon = Bladex.GetEntity(weapon_name)
	owner.Unlink(weapon)
	inv.LinkLeftBack(weapon_name)
def LinkRightBack(weapon_name,inv,owner):
	weapon = Bladex.GetEntity(weapon_name)
	owner.Unlink(weapon)
	inv.LinkRightBack(weapon_name)

