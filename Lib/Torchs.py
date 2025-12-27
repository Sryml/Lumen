import Bladex
import InitDataField
import AuxFuncs
import Actions
import Reference


OFF=0
ON=1
DEAD=0
ALIVE=1


tipos_antorcha=("Antorcha", "Antorchaenpared", "Palangana")


class TorchObj:

	pass


def ExtingueGradual(torchobj, torchspot, torchfire, intensity_var, fire_var, fire_int, OnEndExtinctionFunc, OnEndExtinctionArgs):
	if torchspot.Intensity>0.0:
		torchspot.Intensity=torchspot.Intensity-intensity_var
	else:
		torchspot.Intensity = 0
	fire_int=fire_int+fire_var
	torchfire.Intensity=fire_int
	if torchfire.Intensity>=30.0:
#		print "Apagada..."
		torchobj.LiveStatus=DEAD
		torchobj.LightStatus=OFF
		if OnEndExtinctionFunc:
			apply(OnEndExtinctionFunc, OnEndExtinctionArgs)
		return
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, ExtingueGradual, (torchobj, torchspot, torchfire, intensity_var, fire_var, fire_int, OnEndExtinctionFunc, OnEndExtinctionArgs))


def ExtingueAntorcha(torch_name, OnEndExtinctionFunc="", OnEndExtinctionArgs=()):
	torch=Bladex.GetEntity(torch_name)
	torchspot=AuxFuncs.GetSpot(torch)
	torchfire=AuxFuncs.GetFire(torch)
	torchobj=torch.Data.torchobjdata
	if torchspot.Intensity<=0.0:
#		print "Ya esta apagada..."
		return
	intensity_var=torchspot.Intensity/20.0
	fire_var=(30.0-torchfire.Intensity)/60.0
	fire_int=torchfire.Intensity
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, ExtingueGradual, (torchobj, torchspot, torchfire, intensity_var, fire_var, fire_int, OnEndExtinctionFunc, OnEndExtinctionArgs))
	if Reference.EntitiesObjectData.has_key(torch_name): del Reference.EntitiesObjectData[torch_name]

def EnciendeGradual(torchobj, torchspot, torchfire, intensity_var, fire_var, fire_int):
	torchspot.Intensity=torchspot.Intensity+intensity_var
	fire_int=fire_int-fire_var
	torchfire.Intensity=fire_int
	if torchspot.Intensity>=torchobj.LightIntensity:
#		print "Encendida..."
		torchobj.LightStatus=ON
		return
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, EnciendeGradual, (torchobj, torchspot, torchfire, intensity_var, fire_var, fire_int))


def EnciendeAntorcha(torch_name):
	torch=Bladex.GetEntity(torch_name)
	torchspot=AuxFuncs.GetSpot(torch)
	torchfire=AuxFuncs.GetFire(torch)
	torchobj=torch.Data.torchobjdata
	if torchobj.LightStatus==ON:
#		print "Ya esta encendida..."
		return
	intensity_var=torchobj.LightIntensity/20.0
	fire_var=(10.0-torchobj.FireIntensity)/20.0
	torchfire.Intensity=10.0
	fire_int=torchfire.Intensity
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, EnciendeGradual, (torchobj, torchspot, torchfire, intensity_var, fire_var, fire_int))
	Reference.EntitiesObjectData[torch_name]= Reference.DefaultObjectData["AntorchaFuego"]

def EnciendeEstaAntorcha(person_name, event_name):
	pj=Bladex.GetEntity(person_name)
	pj.DelAnmEventFunc(event_name)
	torch=pj.Data.obj_used
	torchobj=torch.Data.torchobjdata
	objright=Bladex.GetEntity(pj.InvRight)
	objrighttorch=objright.Data.torchobjdata
	if objrighttorch.LightStatus==OFF and torchobj.LightStatus==ON:
#		print "Enciendo mi antorcha..."
		EnciendeAntorcha(objright.Name)
		if objrighttorch.Life>0.0:
			Bladex.AddScheduledFunc(Bladex.GetTime()+objrighttorch.Life, ExtingueAntorcha, (objright.Name,))
	else:
#		print "Enciendo la antorcha de la pared..."
		EnciendeAntorcha(torch.Name)
		if torchobj.Life>0.0:
			Bladex.AddScheduledFunc(Bladex.GetTime()+torchobj.Life, ExtingueAntorcha, (torch.Name,))


def TorchUseFunc(torch_name, use_from):
	global UseFunc
	
	torch=Bladex.GetEntity(torch_name)	
	pj=Bladex.GetEntity("Player1")
	objright=Bladex.GetEntity(pj.InvRight)
	if objright and (torch.Kind in tipos_antorcha) and (objright.Kind in tipos_antorcha):
		torchobj=torch.Data.torchobjdata
		objrighttorch=objright.Data.torchobjdata
		if (objrighttorch.LightStatus==OFF and torchobj.LightStatus==OFF) or (objrighttorch.LightStatus==ON and torchobj.LightStatus==ON):
#			print "No puedo encender. Ambas antorchas estan encendidas o apagadas..."
			return
		if (torchobj.LiveStatus==DEAD) or (objrighttorch.LiveStatus==DEAD):
#			print "Esta antorcha esta extinta..."
			return
		Actions.QuickTurnToFaceEntity("Player1", torch_name)
		difalt=-(torch.Position[1]-(pj.Position[1]+pj.Dist2Floor))
		chartype=Bladex.GetCharType(pj.CharType, pj.CharTypeExt)
		if difalt<=chartype.MaxTake1:
			pj.LaunchAnmType("fire_g")
		elif difalt<=chartype.MaxTake2:
			pj.LaunchAnmType("fire0")
		elif difalt<=chartype.MaxTake3:
			pj.LaunchAnmType("fire1")
		elif difalt<=chartype.MaxTake4:
			pj.LaunchAnmType("fire2")
		elif difalt<=chartype.MaxTake5:
			pj.LaunchAnmType("fire3")
		else:
#			print "Demasiado alta..."
			return
		if UseFunc:
			UseFunc(torch.Name, objright.Name)
		pj.AddAnmEventFunc("SetAlightEvent", EnciendeEstaAntorcha)
#	else:
#		print "No tengo antorcha..."


def SetUsable(obj_name, light_int=3.0, fire_int=3.0, life=-1):
	obj=Bladex.GetEntity(obj_name)
	if obj.Kind not in tipos_antorcha:
#		print "El objeto "+obj_name+" no es una antorcha o no esta definido como tal en tipos_antorcha"
		return
	torchobj=TorchObj()
	torchobj.LightIntensity=light_int
	torchobj.FireIntensity=fire_int
	torchobj.Life=life
	if AuxFuncs.GetSpot(obj).Intensity==0.0:
		torchobj.LightStatus=OFF
		if Reference.EntitiesObjectData.has_key(obj_name): del Reference.EntitiesObjectData[obj_name]
	else:
		torchobj.LightStatus=ON
		Reference.EntitiesObjectData[obj_name]= Reference.DefaultObjectData["AntorchaFuego"]
	if life==0:
		torchobj.LiveStatus=DEAD
	else:
		torchobj.LiveStatus=ALIVE
	InitDataField.Initialise(obj)
	obj.Data.torchobjdata=torchobj
	if obj.Kind!="Antorcha":	# This type is carryable
		obj.UseFunc=TorchUseFunc


UseFunc = None         # UseFunc(from,to)


def SaveData(filename):
  import cPickle
  import GameStateAux
  import GameStateAux

  funcfile=open(filename,"wt")
  p=cPickle.Pickler(funcfile)
  p.persistent_id=GameStateAux.persistent_id
  d=(GameStateAux.SaveFunctionAux(UseFunc),tipos_antorcha)

  p.dump(d)
  funcfile.close()


def LoadData(filename):
  import cPickle
  import GameStateAux
  import GameStateAux

  funcfile=open(filename,"rt")
  p=cPickle.Unpickler(funcfile)
  p.persistent_load=GameStateAux.persistent_load
  d=p.load()
  funcfile.close()
  print d

  global UseFunc
  global tipos_antorcha
  
  UseFunc=GameStateAux.LoadFunctionAux(d[0])
  tipos_antorcha=d[1]



import GameState
GameState.ModulesToBeSaved.append(__import__(__name__))
