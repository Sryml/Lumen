import def_class
import Bladex
import Enm_Def
import EnemyTypes
import AuxFuncs
import B3DLib
import ItemTypes
import AniSound
import Reference
import Combat
import copy
import Actions
import pocimac
import GameText
import Ontake
import Breakings
import Language



_Pasito=Bladex.CreateSound("../../Sounds/paso-piedra-reverb-1.wav","Pasito")
_Pasito.MinDistance =  50000
_Pasito.MaxDistance =  5000
_Pasito.Volume      =  1.0


_Pasito1=Bladex.CreateSound("../../Sounds/paso-piedra-reverb-2.wav","Pasito1")
_Pasito1.MinDistance =  50000
_Pasito1.MaxDistance =  5000
_Pasito1.Volume      =  1.0


#dialogoragnar=Bladex.CreateSound("../../Sounds/ragnar1.wav", "DialogoRagnar")
#dialogoragnar.Volume=1
#dialogoragnar.Scale=3.41
#dialogoragnar.MinDistance=5000
#dialogoragnar.MaxDistance=150000

cuchillasactivadas=Bladex.CreateSound("../../Sounds/trap-clicked.wav", "CuchillasActivadas")
cuchillasactivadas.Volume=1
cuchillasactivadas.Scale=3.41
cuchillasactivadas.MinDistance=5000
cuchillasactivadas.MaxDistance=25000

language = Language.CheckFallback()

matadle=Bladex.CreateSound("../../Sounds/"+language+"/kill-him.wav", "Matadle")
matadle.Volume=1
matadle.Scale=1.0
matadle.MinDistance=10000
matadle.MaxDistance=100000

graznidocuervo=Bladex.CreateSound("../../Sounds/raven-call.wav", "GraznidoCuervo")
graznidocuervo.Volume=1
graznidocuervo.Scale=3.41
graznidocuervo.MinDistance=5000
graznidocuervo.MaxDistance=50000


sectorsonidocuchillas=Bladex.GetSector(-137500.0, -23263.0, -93000.0)
sectorsonidocuchillas.OnEnter=SonidoActivacion


#########################################
#     Definicion de la clase Ragnar     #
#########################################


#Bladex.LoadSampledAnimation("../../Anm/Rgn_escape.bmv","Rgn_escape",1,"Ragnar")
#Bladex.LoadSampledAnimation("../../Anm/Rgn_escape2.bmv","Rgn_escape2",1,"Ragnar")


##################
#     Ragnar     #
##################

ragnar=Bladex.CreateEntity("Ragnar","Ragnar", 0.0, 0.0, 0.0,"Person")
ragnar.Angle=0.0
ragnar.ActionAreaMin=0
ragnar.ActionAreaMax=0
EnemyTypes.EnemyDefaultFuncs(ragnar)
ragnar.Level=4
ragnar.Deaf=1

ragnar.Data.VeryOldImDeadFunc = ragnar.ImDeadFunc
ragnar.ImDeadFunc = OnRagnarDie

espadaragnar=Bladex.CreateEntity("EspadaRagnar","Espadaromana",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(espadaragnar)
Actions.TakeObject(ragnar.Name,"EspadaRagnar")

escudoragnar=Bladex.CreateEntity("EscudoRagnar","Escudo1",0,0,0)
ItemTypes.ItemDefaultFuncs(escudoragnar)
Actions.TakeObject(ragnar.Name,"EscudoRagnar")

potion=Bladex.CreateEntity("RagnarsPotion","Pocima100",0,0,0)
potion.Static=0
potion.Solid=1
potion.Scale=1.220190
pocimac.CreatePotion("RagnarsPotion")
Actions.TakeObject(ragnar.Name,"RagnarsPotion")
Actions.TakeObject(ragnar.Name,"llaverag")


inv=ragnar.GetInventory()
inv.LinkRightHand("EspadaRagnar")
inv.LinkLeftHand("EscudoRagnar")
#Bladex.LoadSampledAnimation("../../Anm/Rgn_rlx_1h.bmv","Rgn_rlx_1h",1,"Ragnar")


##########################
#     Guardaespaldas     #
##########################

guarda1=Bladex.CreateEntity("Guarda1","Knight_Traitor", 0.0, 0.0, 0.0)
guarda1.Person=1
guarda1.Level=3
guarda1.Angle=0.0
guarda1.ActionAreaMin=0
guarda1.ActionAreaMax=0
EnemyTypes.EnemyDefaultFuncs(guarda1)
guarda1.Blind=1
guarda1.Deaf=1


espadaguarda1=Bladex.CreateEntity("RagnarEspadaGuarda1","Hacha",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(espadaguarda1)
Actions.TakeObject(guarda1.Name, espadaguarda1.Name)

escudoguarda1=Bladex.CreateEntity("RagnarEscudoGuarda1","Escudo5",0,0,0)
ItemTypes.ItemDefaultFuncs(escudoguarda1)
Actions.TakeObject(guarda1.Name, escudoguarda1.Name)

inv=guarda1.GetInventory()
inv.LinkRightHand(espadaguarda1.Name)
inv.LinkLeftHand(escudoguarda1.Name)
Actions.TakeObject(guarda1.Name,"llave10")

guarda2=Bladex.CreateEntity("Guarda2","Knight_Traitor", 0.0, 0.0, 0.0)
guarda2.Person=1
guarda2.Level=3
guarda2.Angle=0.0
guarda2.ActionAreaMin=0
guarda2.ActionAreaMax=0
EnemyTypes.EnemyDefaultFuncs(guarda2)
guarda2.Blind=1
guarda2.Deaf=1


espadaguarda2=Bladex.CreateEntity("RagnarEspadaGuarda2","Gladius",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(espadaguarda2)
Actions.TakeObject(guarda2.Name, espadaguarda2.Name)

escudoguarda2=Bladex.CreateEntity("RagnarEscudoGuarda2","Escudo2",0,0,0)
ItemTypes.ItemDefaultFuncs(escudoguarda2)
Actions.TakeObject(guarda2.Name, escudoguarda2.Name)


inv=guarda2.GetInventory()
inv.LinkRightHand(espadaguarda2.Name)
inv.LinkLeftHand(escudoguarda2.Name)



################################
#     Posiciones iniciales     #
################################

ragnar.Position=-142500.0, -12750.0, -110700.0
guarda1.Position=-141000.0, -12750.0, -108000.0
guarda2.Position=-144250.0, -12750.0, -106500.0

ragnar.SetOnFloor()
guarda1.SetOnFloor()
guarda2.SetOnFloor()

##################################################
#     Ragnar enviando dos enemigos y huyendo     #
##################################################

#Bladex.LoadSampledAnimation("../../Anm/Tkn_rlx_f.bmv","Tkn_rlx_f",1,"Knight_Traitor")


ragnar.SeeFunc=RagnarVeJugadorEnemigos


Ontake.AddOnTakeEvent("PergaminoFin",FundidoFin)


########################################
#     Aparicion de Ragnar al final     #
########################################

Bladex.AddParticleGType("RgDoorDust","SmokeParticle",B_PARTICLE_GTYPE_BLEND,40)

for i in range(40):
	if i>20:
		traux=0.0
	else:
		traux=((20.0-i)/20.0)**0.5
	aux=((40.0-i)/40.0)**0.5
	r=255
	g=230
	b=210
	a=60.0*(1.0-traux)
	size=7.0+aux*700.0
	Bladex.SetParticleGVal("RgDoorDust",i,r,g,b,a,size)



#Bladex.LoadSampledAnimation("../../Anm/Rgn_rlx_f.bmv","Rgn_rlx_f",1,"Ragnar")

#Bladex.LoadSampledAnimation("../../Anm/Rgn_end_ragnar.BMV","Rgn_end_ragnar_ragnar",1,"Ragnar")



sectorfinragnar=Bladex.GetSector(-142500.0, -31750.0, -98800.0)
sectorfinragnar.OnEnter=EntraHabitacionFinal
