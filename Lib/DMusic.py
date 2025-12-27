import Bladex
import whrandom
import pdb

enemiesInCombat=0;


debug_dmusic=0


#To store the handles of enemies facing me!
dictEnemiesInCombatHandles={}


TIMEDELAY=2.0

dictDMusics={}
dictExcludedEntitites={}

def getRnd(strKind):
	if not dictDMusics.has_key(strKind):
		return -1

	tidDMusics = dictDMusics[strKind]
	return tidDMusics[whrandom.randint( 0 , len(tidDMusics)-1 )]

def newKind( strKind, tidEvent ):
	dictDMusics[strKind] = tidEvent

def excludeEnt( strEnt ):
	dictExcludedEntitites[strEnt] = 0










#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------

def MusicWarperDelayNoSeenFunc(strName):
	me = Bladex.GetEntity(strName)

	if debug_dmusic==1:
		print "MusicWarperDelayNoSeenFunc"

	decEnemies(strName)

	me.Data.DelayNoSeenFuncMusicBackUp(strName)

	RemoveMusicWarperDelayNoSeenFunc(strName)

	if debug_dmusic==1:
		print "MusicWarperDelayNoSeenFunc executed"


def RestoreMusicWarperDelayNoSeenFunc(strName):
	me = Bladex.GetEntity(strName)

	if me.Data.imusic_noseen_warp==0:
		#print "Unexpected situation in RestoreMusicWarperDelayNoSeenFunc"
		return

	me.Data.DelayNoSeenFuncMusicBackUp=me.DelayNoSeenFunc
	me.DelayNoSeenFunc=MusicWarperDelayNoSeenFunc

	if debug_dmusic==1:
		print "RestoreMusicWarperDelayNoSeenFunc executed fine"


def AddMusicWarperDelayNoSeenFunc(strName):
	me = Bladex.GetEntity(strName)

	if me.Data.imusic_noseen_warp==1:
		if me.Data.DelayNoSeenFuncMusicBackUp:
			print "Unexpected situation in AddMusicWarperDelayNoSeenFunc"
			return


	me.Data.DelayNoSeenFuncMusicBackUp=me.DelayNoSeenFunc
	me.DelayNoSeenFunc=MusicWarperDelayNoSeenFunc
	me.Data.imusic_noseen_warp=1

	if debug_dmusic==1:
		print "AddMusicWarperDelayNoSeenFunc executed fine"





def RemoveMusicWarperDelayNoSeenFunc(strName):
	me = Bladex.GetEntity(strName)


	if me.Data.imusic_noseen_warp==0:
		print "Unexpected situation in RemoveMusicWarperDelayNoSeenFunc"
		return

	if not me.Data or not me.Data.DelayNoSeenFuncMusicBackUp:
		print " CRITICAL->Unexpected situation in RemoveMusicWarperDelayNoSeenFunc"
		return


	me.DelayNoSeenFunc=me.Data.DelayNoSeenFuncMusicBackUp
	me.Data.DelayNoSeenFuncMusicBackUp=0
	me.Data.imusic_noseen_warp=0





#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------

def incEnemies(strName):
	global enemiesInCombat

	me = Bladex.GetEntity(strName)

	if me.Data.imusic_noseen_warp==1:
		if me.Data.DelayNoSeenFuncMusicBackUp:
			RemoveMusicWarperDelayNoSeenFunc(strName)
			return


	if dictEnemiesInCombatHandles.has_key(strName):
		print "incEnemies-> Avoid to add an enemy IN list!!!" + strName
		return

	print "INC-> enemiesInCombat were " , enemiesInCombat , " removing " + strName
	enemiesInCombat = enemiesInCombat + 1
	ent = Bladex.GetEntity(strName)
	handle=getRnd(ent.Name)
	if handle==-1:
		handle=getRnd(ent.Kind)
	else:
		if debug_dmusic==1:
			print "Handle 4 a SPECIFIC character , NOT race"


	Bladex.ExeMusicEvent(handle)
	dictEnemiesInCombatHandles[strName]=handle

	if debug_dmusic==1:
		print "IncEn-> enemies:",enemiesInCombat


def decEnemies(strName):
	global enemiesInCombat

	if not dictEnemiesInCombatHandles.has_key(strName):
		print "decEnemies-> Avoid to remove an enemy NOT in list!!!" + strName
		return


	enemiesInCombat = enemiesInCombat - 1

	del dictEnemiesInCombatHandles[strName]

	if (enemiesInCombat==0) :
		Bladex.ExeMusicEvent(-1)
	else:
		#Tocar musica con siguiente importancia
		max_prio=-1
		curr_handle=-1

		for x in dictEnemiesInCombatHandles.keys():
			test_handle=dictEnemiesInCombatHandles[x]

			tmp_ent = Bladex.GetEntity(x)
			if not tmp_ent or tmp_ent.Life==0:
				print "Dmusic.decEnemies() -> Deleting music entry due to death?"
				del dictEnemiesInCombatHandles[x]
			elif (Bladex.GetMusicEventPriority(test_handle)>max_prio):
				max_prio=Bladex.GetMusicEventPriority(test_handle)
				curr_handle=test_handle
				tmp_ent=Bladex.GetEntity(x)
				if tmp_ent==None:
					print "ERROR in decEnemies() . CAll Jose ASAP!!!!!"

		#print "FORCED ExeMusicEvent in decEnemies 4 " , strName
		Bladex.ExeMusicEvent(curr_handle,1)

	if debug_dmusic==1:
		print "DecEn-> enemies:",enemiesInCombat


def InformDead(strName):
	if not dictEnemiesInCombatHandles.has_key(strName):
		return
	else:
		if debug_dmusic==1:
			print "Dmusic.InformDead calling decEnemies!!!"
		decEnemies(strName)


def notifyCombat(strName) :
	global enemiesInCombat

	ent = Bladex.GetEntity(strName)


	if (not dictDMusics.has_key(ent.Name) and not dictDMusics.has_key(ent.Kind)) :
		return			# el tipo de enemigo no tiene asignada la musica
	if (dictExcludedEntitites.has_key(ent.Name)) :
		return	# el tipo de enemigo esta en la lista de exclusion



	if (not ent.InCombat) :
		if ent.Life>0:
			AddMusicWarperDelayNoSeenFunc(strName)

			# NOTA IMP : Quityar las dos lineas anteriores y poner en su lugar la siguiente
			#para que la musica interactiva se "vaya" al desencararse el personaje , no al de un rato
			# Por si habia bugs... ( el metodo alternativo es mucho mas robusto)

			#decEnemies(strName)
		else:
			decEnemies(strName)
	else:
		incEnemies(strName)




#
#
#
#
#
#
#
#
#
#

def AddCombatMusic(race_name , file_name , priority , pre_open=0 , volume=1.0 , fin_t=1.0 , fout_t=1.0):
    tag_name= race_name + "_dmusic"

    file_len=len(file_name)

    if (file_name[file_len-1]=='v' or file_name[file_len-1]=='V') and (file_name[file_len-2]=='a' or file_name[file_len-2]=='A') and (file_name[file_len-3]=='w' or file_name[file_len-3]=='W'):
        print "Adding WAV for dinamic music for " + race_name + " , pre_open flag is " + str(pre_open)
        Bladex.AddMusicEventWAV( tag_name , file_name , fin_t , fout_t , volume , priority, 0, -1 , pre_open)
    elif (file_name[file_len-1]=='3') and (file_name[file_len-2]=='p' or file_name[file_len-2]=='P') and (file_name[file_len-3]=='m' or file_name[file_len-3]=='M'):
        print "Adding MP3 for dinamic music for " + race_name
        if pre_open==1:
            print "AddCombatMusic->ERROR, trying to pre open a MP3 file"
        Bladex.AddMusicEventMP3( tag_name , file_name , fin_t , fout_t , volume , priority, 0, -1 )

    tidMusics = ( Bladex.GetMusicEvent(tag_name) , )
    newKind( race_name , tidMusics )


def ExcludeMusicFor(ent_name):
    excludeEnt( ent_name)






"""
def SaveData(filename):
  import cPickle
  import GameStateAux

  funcfile=open(filename,"wt")
  p=cPickle.Pickler(funcfile)
  p.persistent_id=GameStateAux.persistent_id
  d=(dictEnemiesInCombatHandles,)
  p.dump(d)
  funcfile.close()


def LoadData(filename):
  import cPickle
  import GameStateAux

  funcfile=open(filename,"rt")
  p=cPickle.Unpickler(funcfile)
  p.persistent_load=GameStateAux.persistent_load
  d=p.load()
  funcfile.close()
  print d

  global dictEnemiesInCombatHandles

  dictEnemiesInCombatHandles=d[0]

import GameState
GameState.ModulesToBeSaved.append(__import__(__name__))
"""
