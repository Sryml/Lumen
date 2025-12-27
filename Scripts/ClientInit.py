#*******************************************************************************************#
#                              Client initialization routines                               #
#*******************************************************************************************#

import Bladex
import CharStats
import Reference
import Raster
import netgame
import AniSound
ClientActive = 1

import CommonResources
CommonResources.Init()

execfile("../../Scripts/NetworkResources.py")

# empaquetado de objetos
import BODInit
BODInit.Init()


import SolidMask
SolidMask.Init()

import Material
Material.Init()

#
# Sounds
#
import AniSound

#
# Sound for steps (needed before the biped stuff)
#
execfile("../../Scripts/NetStepSounds.py")





#
# Sonidos de los clientes
#
def ClientSoundAsignation(name,kind):
	print "tratando de asignar los sonidos a "+name+" de raza "+kind
	ent = Bladex.GetEntity(name)

	if kind == "Knight_N":
		AniSound.AsignarSonidosCaballero(name)
	elif kind == "Amazon_N":
		AniSound.AsignarSonidosAmazona(name)
	elif kind == "Barbarian_N":
		AniSound.AsignarSonidosBarbaro(name)
	elif kind == "Dwarf_N":
		AniSound.AsignarSonidosEnano(name)
	else:
		print "Sonidos para "+kind+"no implementado"
netgame.SetJoinPlayerFunc(ClientSoundAsignation)
print "Sonidos listos"









Bladex.OpenDebugChannel("Salida")


#
# Animation events (needed b4 the biped stuff)
#
#import anm_def
#anm_def.Init()


#
# Different kind of enemies. Should be called b4 creating ANY PersonEntity!
#
import Enemies
Enemies.Init()



#
# New animation system (biped)
#
#execfile("../../Scripts/KgtBAct.py")
#execfile("../../Scripts/Biped/Biped.py")




#
# The sharing of whole sets of animations
#
#execfile("../../Scripts/anm_conv.py")


#
# Factor of animations (to speed up or slow down animations) - OLD PLACE
#
#execfile("../../Scripts/anm_fact.py")


#
# To modify flags of animations
#
#execfile("../../Scripts/anm_mdf.py")


#
# Factor of animations (to speed up or slow down animations)
#
#execfile("../../Scripts/anm_fact.py")


#
# Particle Systems init
#
# CUIDADO! Valores definidos tambien en InitParticleSystems.py.
B_PARTICLE_GTYPE_COPY=0
B_PARTICLE_GTYPE_BLEND=1
B_PARTICLE_GTYPE_ADD=2
B_PARTICLE_GTYPE_MUL=3

import InitParticleSystems
InitParticleSystems.Init()

#
# Procedural textures
#
execfile("../../Scripts/AutoGenTextures.py")


#
# PJ Init loop...
#

TIME_LIMIT_ERROR         = 60.0
TIME_LIMIT_ERROR_MESSAGE = 30.0

tim = Bladex.GetPTime()

Bladex.ReadBitMap("../../Data/NetError0.BMP","NetError0")
NetError0=Raster.BmpHandle("NetError0")

Bladex.ReadBitMap("../../Data/NetError1.BMP","NetError1")
NetError1=Raster.BmpHandle("NetError1")


while(netgame.CreateMainPlayer()==0):
	tmn = Bladex.GetPTime()-tim
	if ( tmn> TIME_LIMIT_ERROR_MESSAGE):

		Raster.SetRasterParameter("startscene","")
		Raster.SetPosition(4,4)
		Raster.SetPenColor(180,23,44)
		if tmn-int(tmn) < (tmn-TIME_LIMIT_ERROR_MESSAGE)/(TIME_LIMIT_ERROR-TIME_LIMIT_ERROR_MESSAGE):
			Raster.DrawBitmap(NetError1,64,64)
		else:
			Raster.DrawBitmap(NetError0,64,64)
		Raster.SetPosition(0,0)
		Raster.SwapBuffers()
		Raster.SetRasterParameter("endscene","")

	if (tmn > TIME_LIMIT_ERROR):
		print "T I M E O U T     disconecting..."
		Bladex.CreateEntity("Player1","Barbarian_N",0,0,0,"Client")
		netgame.RestartNet()
		Bladex.LoadLevel("Casa")
		break

char=Bladex.GetEntity("Player1")


#
# Timers
#
Bladex.CreateTimer("Timer60",1.0/60.0)
Bladex.CreateTimer("Timer30",1.0/30.0)
Bladex.CreateTimer("Timer15",1.0/15.0)


#
# Controls ( keyborad,mouse...) stuff
#
execfile("../../Scripts/InputInit.py")
if netgame.GetNetState() != 0:
	execfile("../../Scripts/NetMode.py")
import acts
acts.InitBindings("Player1")

try:
  execfile("../../Config/Control.py")
  print "BladeInit -> Executed Control.py"
except:
  execfile("../../Scripts/DefControl.py")
  print "BladeInit -> Executed DefControl.py"

if netgame.GetNetState() != 0:
	import NetScorer
	NetScorer.ActivateScorer()



#
# Menu (el menu de cliente es otro, no esta basura)
#
import Menu
Menu.InitMenuKeys()

import DefaultSelectionData

print "ClientInit.py"
