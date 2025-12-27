

import Bladex
import GameState
import MemPersistence
import BBLib
import string
import Reference
import ObjStore

class MainCharState(GameState.EntityPersonState):
	"Clase para grabar el estado del jugador"

	def __init__(self,ent_name="Player1",cam_name="Camera"):
		import CharStats
		entity=Bladex.GetEntity(ent_name)
		cam= Bladex.GetEntity(cam_name)

		if not entity or not cam:
			return

		import Actions


		self.Props={}
		self.Props["Life"]=CharStats.GetCharMaxLife(entity.Kind,entity.Level)
		self.Props["Level"]=entity.Level
		self.Props["PartialLevel"]=entity.PartialLevel
		self.Props["Energy"]=entity.Energy
		self.Props["Armor"]=(entity.MeshName,entity.Data.armour_level,entity.Data.armour_prot_factor)
		self.Props["Saves"]=Reference.TimesSaved
		self.Props["Combos"]=Bladex.GetCombos("Player1")
		self.Props["PViewType"]=cam.PViewType
		self.Props["ObjectsTaken"]=entity.Data.ObjectsTaken


		GameState.EntityPersonState.__init__(self,entity)
		inv=entity.GetInventory()
		self.Inventory={}
		self.Inventory["Objects"]=[]
		for i in range(inv.nKindObjects):
			for name in Actions.GetListOfObjectsAt(inv,i):
				self.Inventory["Objects"].append(self.__GetObjAux(name))

		self.Inventory["maxWeapons"]=inv.maxWeapons
		self.Inventory["Weapons"]=[]
		for i in range(inv.nWeapons):
			self.Inventory["Weapons"].append(self.__GetObjAux(inv.GetWeapon(i)))

		self.Inventory["Shields"]=[]
		for i in range(inv.nShields):
			self.Inventory["Shields"].append(self.__GetObjAux(inv.GetShield(i)))

		self.Inventory["Quivers"]=[]
		for i in range(inv.nQuivers):
			try: narrows= Bladex.GetEntity(inv.GetQuiver(i)).Data.NumberOfArrows()
			except: narrows=0
			self.Inventory["Quivers"].append((self.__GetObjAux(inv.GetQuiver(i)),narrows))

		self.Inventory["Keys"]=[]
		for i in range(inv.nKeys):
			self.Inventory["Keys"].append(self.__GetObjAux(inv.GetKey(i)))

		self.Inventory["SpecialKeys"]=[]
		for i in range(inv.nSpecialKeys):
			self.Inventory["SpecialKeys"].append(self.__GetObjAux(inv.GetSpecialKey(i)))

		self.Inventory["Tablets"]=[]
		for i in range(inv.nTablets):
			self.Inventory["Tablets"].append(self.__GetObjAux(inv.GetTablet(i)))

		self.Inventory["InvLeft"]=self.__GetObjAux(entity.InvLeft)
		self.Inventory["InvLeft2"]=self.__GetObjAux(entity.InvLeft2)
		#Avoid to carry standard objects to another map( chairs and similars)
		if Actions.IsRightHandWeaponObject(entity.Name)==0:
			if entity.InvRight:
				print "Not taking right hand object to next map cause it´s not a weapon!"
			self.Inventory["InvRight"]=None
		else:
			self.Inventory["InvRight"]=self.__GetObjAux(entity.InvRight)
		self.Inventory["InvLeftBack"]=self.__GetObjAux(entity.InvLeftBack)
		self.Inventory["InvRightBack"]=self.__GetObjAux(entity.InvRightBack)


	def __GetBOD(self,ent_kind):
		RM=BBLib.GetResourceManager()
		for i in range(RM.NResources(BBLib.B_CID_OBJDSCR)):
			if RM.IsResourceLoaded(BBLib.B_CID_OBJDSCR,i):
				if RM.GetResourceName(BBLib.B_CID_OBJDSCR,i)==ent_kind:
					return RM.GetResourceFile(BBLib.B_CID_OBJDSCR,i)
		return None

	def __GetObjAux(self,obj):
		if not obj:
			return None
		objKind=Bladex.GetEntity(obj).Kind
		return (obj,objKind,self.__GetBOD(objKind))


##	def SaveInventory(self,file_name):
##		f=open('../../Save/'+file_name,'wt')
##		p=cPickle.Pickler(f)
##		temp={}
##		temp["Life"]=self.Props["Life"]
##		temp["Level"]=self.Props["Level"]
##		temp["PartialLevel"]=self.Props["PartialLevel"]
##
##		p.dump((self.CreationProps,temp,self.Inventory))
##		f.close()


	def GetProps(self):
		temp={}
		temp["Life"]=self.Props["Life"]
		temp["Level"]=self.Props["Level"]
		temp["PartialLevel"]=self.Props["PartialLevel"]
		temp["Energy"]=self.Props["Energy"]
		temp["Armor"]=self.Props["Armor"]
		temp["Combos"]=self.Props["Combos"]
		temp["Saves"]=self.Props["Saves"]
		temp["PViewType"]=self.Props["PViewType"]
		temp["ObjectsTaken"]=self.Props["ObjectsTaken"]

		return (self.CreationProps,temp,self.Inventory)

def CreateEntAux(obj_tuple,obj_kind,props=1):
	import ItemTypes
	obj=Bladex.GetEntity(obj_tuple[0])
	if not obj:
		BBLib.ReadBOD(obj_tuple[2])
		obj=Bladex.CreateEntity(obj_tuple[0],obj_tuple[1],0,0,0,obj_kind)
		if props:
			ItemTypes.ItemDefaultFuncs(obj)
	return obj


def CreateMainCharWithProps(props):
	CreationProps=props[0]
	Props=props[1]
	Inventory=props[2]

	import Basic_Funcs
	import AniSound
	import Reference
	import Sparks
	import Breakings
	import Actions


	char=Bladex.CreateEntity("Player1",CreationProps["Kind"],0,0,0,"Person")
	cam=Bladex.GetEntity("Camera")
	char.Data=Basic_Funcs.PlayerPerson(char)
	inv=char.GetInventory()
	AniSound.AsignarSonidosCaballero('Player1')

	char.Level=Props["Level"]
	char.PartialLevel=Props["PartialLevel"]
	char.Life=Props["Life"]
	char.Data.ObjectsTaken=Props["ObjectsTaken"]

	char.Energy=Props["Energy"]
	char.SetMesh(Props["Armor"][0])
	char.Data.armour_level       = Props["Armor"][1]
	char.Data.armour_prot_factor = Props["Armor"][2]
	Reference.TimesSaved         = Props["Saves"]
	Bladex.SetCombos("Player1",Props["Combos"])
	if cam: cam.PViewType=Props["PViewType"]
	else: print "Camera not available for setting PViewType"

	char.SendTriggerSectorMsgs=1



	for i in Inventory["Objects"]:
		CreateEntAux(i,"Physic")
		Actions.ExtendedTakeObject(inv,i[0])

	inv.maxWeapons=Inventory["maxWeapons"]
	for i in Inventory["Weapons"]:
		obj=CreateEntAux(i,"Weapon")
		object_flag=Reference.GiveObjectFlag(i[0])
		if object_flag == Reference.OBJ_BOW:
			inv.AddBow(i[0])
		else:
			flag=Reference.GiveWeaponFlag(i[0])
			inv.AddWeapon(i[0],flag)


	for i in Inventory["Shields"]:
		CreateEntAux(i,"Weapon")
		inv.AddShield(i[0])

	for i in Inventory["Quivers"]:
		obj=CreateEntAux(i[0],"Physic")
		try: obj.Data.SetNumberOfArrows(i[1])
		except: pass
		inv.AddQuiver(i[0][0])

	for i in Inventory["Keys"]:
		CreateEntAux(i,"Physic",0)
		inv.AddKey(i[0])

	for i in Inventory["SpecialKeys"]:
		CreateEntAux(i,"Physic",0)
		inv.AddSpecialKey(i[0])

	for i in Inventory["Tablets"]:
		CreateEntAux(i,"Physic",0)
		inv.AddTablet(i[0])

	if Inventory["InvLeft"]:
		CreateEntAux(Inventory["InvLeft"],"Physic")
		inv.LinkLeftHand(Inventory["InvLeft"][0])

	if Inventory["InvLeft2"]:
		CreateEntAux(Inventory["InvLeft2"],"Physic")
		inv.LinkLeftHand2(Inventory["InvLeft2"][0])

	if Inventory["InvRight"]:
		CreateEntAux(Inventory["InvRight"],"Physic")
		inv.LinkRightHand(Inventory["InvRight"][0])

	if Inventory["InvRightBack"]:
		CreateEntAux(Inventory["InvRightBack"],"Physic")
		inv.LinkRightBack(Inventory["InvRightBack"][0])

	if Inventory["InvLeftBack"]:
		CreateEntAux(Inventory["InvLeftBack"],"Physic")
		inv.LinkLeftBack(Inventory["InvLeftBack"][0])



def RestoreMainCharState(key):
  props=MemPersistence.Get(key)
  if props:
    if string.lower(Bladex.GetCurrentMap()) == "final":
      props[2]["Objects"]      = []
      props[2]["Weapons"]      = []
      props[2]["Shields"]      = []
      props[2]["Quivers"]      = []
      props[2]["Keys"]         = []
      props[2]["SpecialKeys"]  = []
      props[2]["Tablets"]      = []
      props[2]["InvLeft"]      = None
      props[2]["InvLeft2"]     = None
      props[2]["InvRight"]     = None
      props[2]["InvRightBack"] = None
      props[2]["InvLeftBack"]  = None
      
    CreateMainCharWithProps(props)
    return 1
  return 0



def SaveMainCharState(key):
  ent_state=MainCharState('Player1')
  props=ent_state.GetProps()
  MemPersistence.Store(key,props)





#place in scripts
VisitedMaps		= [ 0,0,0,0,
					0,0,
					0,
					0,
					0,0,0,0,0,0,0,0,0] # Maintained outside, 2DMAP

# Once a Tablet is placed on Ianna's update this array
PlacedTablets	= [0,0,0,0,0,0] # Maintained Outside, 2DMAP


# TEXT TO BE SAVED PER MAP
MText	= []
BaList	= []
for a in range(17):
	MText.append([])

# Formerly picked weapons
PWeapons= []

# Formerly picked Items
PItems	= []

# NOTES:
# Llamar a esta funcion desde cualquier script de mapa donde se quiera aniadir texto, el formato es:
# 1) primero se incluye "import GotoMapVars" en el comiezo del archivo (junto con los otros imports)
# 2) Donde se haya de escribir el texto se pone:
#		GotoMapVars.MapText(Numero del mapa, "el texto que se quiera.htm")
def MapText(MapNum,MapTex):
	if MapNum == -1:
		BaList.append(MapTex)
	else:
		MText[MapNum - 1].append(MapTex) # Must include the -1 offset to make mappers work easier.

# Weapon is a string with the internal name of the weapon
def PickedWeapon(Weapon):
	PWeapons.append(Weapon)

# Item is a string with the internal name of the item
def PickedItems(Item):
	PItems.append(Item)


def Set2DMapValuesAux():
	return [VisitedMaps,PlacedTablets,MText,PWeapons,PItems,BaList]


def Get2DMapValuesAux(vals):

	if vals:
		global VisitedMaps
		global PlacedTablets
		global MText
		global PWeapons
		global PItems
		global BaList
		VisitedMaps=vals[0]
		PlacedTablets=vals[1]
		MText=vals[2]
		PWeapons=vals[3]
		PItems=vals[4]
		BaList=vals[5]
		return 1

	return 0




def Get2DMapValues():

	print "Get2DMapValues()"
	vals=MemPersistence.Get('2DMapValues')
	if vals:
		return Get2DMapValuesAux(vals)
	else:
		print "Get2DMapValues() -> can't find vals."
	return 0


def GetCarriedTablets():
	a = [0,0,0,0,0,0]
	for i in MemPersistence.Get('MainChar')[2]["Tablets"]:
		a[string.atoi(i[0][len("tablilla")])-1] = 1

	return a


def BeginLevel():
	pj=RestoreMainCharState('MainChar')
	if pj:
		return Get2DMapValues()
	return 0




# LEVEL ENDING
LevelNames = [	"barb_m1",		"ragnar_m2",	"dwarf_m3",		"ruins_m4",		"mine_m5",	"labyrinth_m6",
				"tomb_m7",		"island_m8",	"orc_m9",		"orlok_m10",	"ice_m11",	"btomb_m12",
				"desert_m13",	"volcano_m14",	"palace_m15",	"tower_m16",	"chaos_m17"]

BackLevelNames = [ "mine_back", "labyrinth_back", "tomb_back", "ice_back", "btomb_back", "desert_back",
                   "palace_back"]


def StoreCharInfo():

	import string
	global VisitedMaps
	global BackLevelNames
	global LevelNames

	# Save lists in this file in c memory
	try:
		pname = Bladex.GetCurrentMap()
		name = string.lower(pname)

		if (name == "palace_m15"):
			name = "palace_back"
		if not(name in BackLevelNames):
			iIndex = LevelNames.index(name)
		else:
			iIndex = BackLevelNames.index(name)
			VisitedMaps[14] = 1
		Bladex.SetStringValue("LastVisitedMap","M_" + str(iIndex+1))
		VisitedMaps[iIndex] = 1
		print iIndex
		MemPersistence.Store('2DMapValues',Set2DMapValuesAux())
	except Exception,exc:
		print "Exception in StoreCharInfo",exc

	SaveMainCharState('MainChar')


def EndOfLevel():

	# Do some python garbage collection
	ObjStore.CheckStore()

	import Language
	import SplashImage
	scr_name="../../Data/Menu/Save/"+Language.Current+"/Cerrando_hi.jpg"
	SplashImage.ShowImage(scr_name,0)

	print "EndOfLevel()"

	print "Preparing main char for the travel."
	import Actions

	print 'Actions.PutAllInBack("Player1")'
	Actions.PutAllInBack("Player1")

	print 'Actions.RemoveAllKeys("Player1")'
	Actions.RemoveAllKeys("Player1")

	print 'Actions.RemoveNoTravelObjects( "Player1" )'
	Actions.RemoveNoTravelObjects( "Player1" )
	StoreCharInfo()

	if (string.lower(Bladex.GetCurrentMap()) == "tower_m16"):
		Bladex.LoadLevel("Chaos_m17")
	else:
		Bladex.LoadLevel("2dMap")

def CreatePJ_PY():
	global VisitedMaps
	global PlacedTablets
	global MText
	global PWeapons
	global PItems
	global BaList

	SaveMainCharState('MainChar')

	cfgfile = open("pj.py",'w')
	cfgfile.write("import GotoMapVars\n")
	cfgfile.write("GotoMapVars.VisitedMaps             = "+`VisitedMaps`+'\n')
	cfgfile.write("GotoMapVars.PlacedTablets           = "+`PlacedTablets`+'\n')
	cfgfile.write("GotoMapVars.MText                   = "+`MText`+'\n')
	cfgfile.write("GotoMapVars.PWeapons                = "+`PWeapons`+'\n')
	cfgfile.write("GotoMapVars.PItems                  = "+`PItems`+'\n')
	cfgfile.write("GotoMapVars.BaList                  = "+`BaList`+'\n')

	cfgfile.write("charprops = "+`MemPersistence.Get('MainChar')`+'\n')
	cfgfile.write("GotoMapVars.CreateMainCharWithProps(charprops)"+'\n')


	cfgfile.close()

def GrantRank():
	print "Calculate Rank"
	global VisitedMaps
	nMaps = 1
	for v in VisitedMaps:
		if v:
			nMaps = nMaps + 1
	print "Visited maps = " + str(nMaps)
	vismap = Reference.TimesSaved/nMaps
	print "vismap = " + str(vismap)
	if Reference.TimesSaved == 0:
		Bladex.TriggerEvent(45)
	elif 0 <= vismap and vismap < 2:
		Bladex.TriggerEvent(46)
	elif 2 <= vismap and vismap < 5:
		Bladex.TriggerEvent(47)
	elif 5 <= vismap and vismap < 9:
		Bladex.TriggerEvent(48)
	elif 9 <= vismap and vismap < 14:
		Bladex.TriggerEvent(49)

	Kind = "Knight_N"
	if MemPersistence.Get('MainChar') != None:
		Kind = MemPersistence.Get('MainChar')[0]['Kind'][0]
	if Kind[0] == "K":
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,Bladex.TriggerEvent,(51,))
	elif Kind[0] == "A":
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,Bladex.TriggerEvent,(53,))
	elif Kind[0] == "D":
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,Bladex.TriggerEvent,(52,))
	elif Kind[0] == "B":
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,Bladex.TriggerEvent,(50,))

